from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('index.html')

        # Go to the local HTML file
        page.goto(f'file://{file_path}')

        # Wait for the page to load
        page.wait_for_selector('.container')

        # Take a screenshot of the first step
        page.screenshot(path='jules-scratch/verification/step1.png')

        # Click on "Garage mécanique VL"
        page.click('[data-value="garage-vl"]')

        # Click on "Suivant"
        page.click('#nextBtn1')

        # Wait for the second question to appear
        page.wait_for_selector('#question2.active')

        # Click on "2 à 3" operators
        # Note: The options are dynamically generated, so we need to be careful with the selector.
        # We'll click the first option in the list.
        page.click('#operatorOptions .option:first-child')

        # Click on "Voir les résultats"
        page.click('#nextBtn2')

        # Wait for the results to appear
        page.wait_for_selector('#results.active')

        # Take a screenshot of the results page
        page.screenshot(path='jules-scratch/verification/results.png')

        browser.close()

if __name__ == '__main__':
    main()
