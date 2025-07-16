from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import os

def capture_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="backend/static/screenshot.png", full_page=True)
        browser.close()

def extract_login_form(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    login_form = None

    for form in forms:
        if 'password' in form.text.lower() or form.find('input', {'type': 'password'}):
            login_form = str(form)
            break

    if login_form:
        with open("backend/templates/form.html", "w") as f:
            f.write(login_form)
    else:
        print("No login form found.")

if __name__ == "__main__":
    url = input("Enter the URL of the target website: ")
    capture_screenshot(url)
    extract_login_form(url)
    print("Screenshot and form saved.")
