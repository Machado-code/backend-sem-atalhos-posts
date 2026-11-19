import sys
from playwright.sync_api import sync_playwright

src, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    page.goto(f"file://{src}")
    page.wait_for_timeout(300)
    page.screenshot(path=out, full_page=False)
    browser.close()
print("ok", out)
