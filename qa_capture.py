from playwright.sync_api import sync_playwright
import os
import time

html_path = "file:///C:/Users/New%20PC/.gemini/antigravity/scratch/treats-by-tayjah/index.html"
output_dir = "C:/Users/New PC/.gemini/antigravity/brain/09e24cb8-5cf8-449c-aa70-e1d55c2689f4"

viewports = {
    "desktop": {"width": 1920, "height": 1080},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 667}
}

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for name, viewport in viewports.items():
            context = browser.new_context(viewport=viewport)
            page = context.new_page()
            
            page.goto(html_path)
            # Wait for any lazy-loaded images or scripts
            page.wait_for_timeout(2000)
            
            # Full page screenshot
            page.screenshot(path=os.path.join(output_dir, f"qa-responsive-{name}.png"), full_page=True)
            
            if name == "mobile":
                # Test mobile menu interaction
                page.click("#mobile-menu")
                page.wait_for_timeout(1000)
                page.screenshot(path=os.path.join(output_dir, f"qa-mobile-menu-open.png"))
                
            context.close()
            print(f"Captured {name}")
            
        browser.close()
        print("All screenshots captured.")

if __name__ == "__main__":
    capture_screenshots()
