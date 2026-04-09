"""
RFPO Automation Script
======================
Runs every hour to:
  1. Open the Opportunity Workflow page for OP Bank (ID: 0012440276)
  2. Generate the RFPO Summary
  3. List all Active Opportunities

Requirements:
    pip install -r requirements.txt
    playwright install chromium

Usage:
    python rfpo_automation.py              # start the hourly scheduler
    python rfpo_automation.py --run-once   # run immediately once and exit
"""

import argparse
import json
import logging
import os
import time
from datetime import datetime
from pathlib import Path

import schedule
from playwright.sync_api import Page, TimeoutError as PWTimeoutError, sync_playwright

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL = "https://mysolutionplannernextgen.accenture.com"
OPPORTUNITY_URL = f"{BASE_URL}/link/OpportunityWorkflow/0012440276/SI"

# Output directory for results (relative to this script)
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

LOG_FILE = OUTPUT_DIR / "rfpo_automation.log"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Browser helpers
# ---------------------------------------------------------------------------

def wait_for_page_ready(page: Page, timeout: int = 30_000) -> None:
    """Wait until the network is idle and no spinners are visible."""
    page.wait_for_load_state("networkidle", timeout=timeout)


def generate_rfpo_summary(page: Page) -> dict:
    """
    Locate and click the 'Generate RFPO Summary' button / action on the page.
    Returns a dict with status and any extracted summary text.
    """
    result = {"status": "not_found", "summary": None}

    # Common selectors for RFPO summary triggers — adjust if the app changes
    selectors = [
        "button:has-text('Generate RFPO Summary')",
        "button:has-text('RFPO Summary')",
        "a:has-text('Generate RFPO Summary')",
        "[data-testid='rfpo-summary-btn']",
        "[aria-label='Generate RFPO Summary']",
    ]

    for sel in selectors:
        try:
            element = page.locator(sel).first
            if element.is_visible(timeout=3_000):
                log.info("Clicking RFPO Summary trigger: %s", sel)
                element.click()
                wait_for_page_ready(page)

                # Try to capture summary text from a modal / panel
                summary_text = None
                for text_sel in [
                    "[data-testid='rfpo-summary-content']",
                    ".rfpo-summary",
                    ".summary-panel",
                    "dialog",
                    "[role='dialog']",
                ]:
                    try:
                        el = page.locator(text_sel).first
                        if el.is_visible(timeout=2_000):
                            summary_text = el.inner_text()
                            break
                    except PWTimeoutError:
                        continue

                result = {"status": "success", "summary": summary_text}
                log.info("RFPO Summary generated successfully.")
                break
        except PWTimeoutError:
            continue

    if result["status"] == "not_found":
        log.warning("RFPO Summary button not found — page may require login or the UI changed.")

    return result


def list_active_opportunities(page: Page) -> dict:
    """
    Navigate to the Active Opportunities view and collect the opportunity list.
    Returns a dict with status and a list of opportunity rows.
    """
    result = {"status": "not_found", "opportunities": []}

    # Try tab / menu items labelled 'Active Opportunities'
    nav_selectors = [
        "button:has-text('Active Opportunities')",
        "a:has-text('Active Opportunities')",
        "[data-testid='active-opportunities-tab']",
        "li:has-text('Active Opportunities')",
    ]

    clicked = False
    for sel in nav_selectors:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=3_000):
                log.info("Navigating to Active Opportunities via: %s", sel)
                el.click()
                wait_for_page_ready(page)
                clicked = True
                break
        except PWTimeoutError:
            continue

    if not clicked:
        log.warning("Active Opportunities nav element not found — attempting to read current table.")

    # Scrape a table / list of opportunities from the current view
    rows = []
    try:
        # Generic table row extraction
        table = page.locator("table").first
        if table.is_visible(timeout=5_000):
            headers = [th.inner_text().strip() for th in table.locator("thead th").all()]
            for tr in table.locator("tbody tr").all():
                cells = [td.inner_text().strip() for td in tr.locator("td").all()]
                if cells:
                    row = dict(zip(headers, cells)) if headers else {"row": cells}
                    rows.append(row)
            log.info("Found %d opportunity rows.", len(rows))
            result = {"status": "success", "opportunities": rows}
    except PWTimeoutError:
        log.warning("No opportunity table found on page.")

    return result


def take_screenshot(page: Page, label: str) -> Path:
    """Save a timestamped screenshot and return its path."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = OUTPUT_DIR / f"{label}_{ts}.png"
    page.screenshot(path=str(path), full_page=True)
    log.info("Screenshot saved: %s", path)
    return path


def save_results(rfpo_result: dict, opps_result: dict) -> Path:
    """Persist run results to a timestamped JSON file."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = OUTPUT_DIR / f"run_{ts}.json"
    payload = {
        "run_timestamp": datetime.now().isoformat(),
        "opportunity_url": OPPORTUNITY_URL,
        "rfpo_summary": rfpo_result,
        "active_opportunities": opps_result,
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("Results saved: %s", out)
    return out


# ---------------------------------------------------------------------------
# Main automation job
# ---------------------------------------------------------------------------

def run_automation() -> None:
    log.info("=" * 60)
    log.info("Starting RFPO automation run at %s", datetime.now().isoformat())
    log.info("=" * 60)

    with sync_playwright() as pw:
        # Launch Chromium (headless=False keeps the browser visible)
        browser = pw.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            # Preserve cookies/session across runs using a persistent storage dir
            storage_state=str(OUTPUT_DIR / "auth_state.json")
            if (OUTPUT_DIR / "auth_state.json").exists()
            else None,
        )
        page = context.new_page()

        try:
            # 1. Navigate to Opportunity Workflow
            log.info("Opening URL: %s", OPPORTUNITY_URL)
            page.goto(OPPORTUNITY_URL, timeout=60_000, wait_until="domcontentloaded")
            wait_for_page_ready(page)
            take_screenshot(page, "01_opportunity_workflow")

            # 2. Generate RFPO Summary
            rfpo_result = generate_rfpo_summary(page)
            take_screenshot(page, "02_rfpo_summary")

            # 3. List Active Opportunities
            opps_result = list_active_opportunities(page)
            take_screenshot(page, "03_active_opportunities")

            # 4. Save results
            save_results(rfpo_result, opps_result)

            # Persist auth cookies for the next run (avoids re-login)
            context.storage_state(path=str(OUTPUT_DIR / "auth_state.json"))

        except Exception as exc:
            log.error("Automation failed: %s", exc, exc_info=True)
            take_screenshot(page, "ERROR")
        finally:
            context.close()
            browser.close()

    log.info("Run complete.\n")


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="RFPO Hourly Automation")
    parser.add_argument(
        "--run-once",
        action="store_true",
        help="Execute once immediately and exit (no scheduler).",
    )
    args = parser.parse_args()

    if args.run_once:
        run_automation()
        return

    log.info("Scheduler started. Job will run every hour. Press Ctrl+C to stop.")
    # Run immediately on start, then every hour
    run_automation()
    schedule.every(1).hours.do(run_automation)

    try:
        while True:
            schedule.run_pending()
            time.sleep(30)  # check every 30 s
    except KeyboardInterrupt:
        log.info("Scheduler stopped by user.")


if __name__ == "__main__":
    main()
