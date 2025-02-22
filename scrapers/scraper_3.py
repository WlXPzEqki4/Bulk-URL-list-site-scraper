# scraper_3.py

import os
import time
import base64
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def run_scraper_3(urls, base_folder):
    """
    Uses headless Chrome (Selenium + Chrome DevTools Protocol) to print each URL to PDF.
    Saves each PDF in '3_PDF_1' under the provided base_folder.

    Returns a list of dicts: [
      {"url": <URL>, "filename": <filename>, "status": "success"/"failed", "error": <error or None>},
      ...
    ]

    Also displays a Streamlit progress bar to track completion.
    """

    subfolder_name = "3_PDF_1"
    save_folder = os.path.join(base_folder, subfolder_name)
    os.makedirs(save_folder, exist_ok=True)

    # Configure headless Chrome
    chrome_options = Options()
    # "new" headless mode for Chrome 109+
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    results = []
    total = len(urls)

    progress_bar = st.progress(0)
    progress_text = st.empty()

    for i, url in enumerate(urls):
        data = {"url": url, "filename": None, "status": None, "error": None}

        try:
            driver.get(url)
            time.sleep(5)  # Allow time for JavaScript to render

            # Generate a .pdf filename from URL
            filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".pdf"
            filepath = os.path.join(save_folder, filename)

            # Use Chrome DevTools to print page to PDF
            pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {
                "landscape": False,
                "displayHeaderFooter": False,
                "printBackground": True,
                "preferCSSPageSize": True
            })

            # Decode base64 PDF data and write to file
            with open(filepath, "wb") as f:
                f.write(base64.b64decode(pdf_data["data"]))

            data["filename"] = filename
            data["status"] = "success"

        except Exception as e:
            data["status"] = "failed"
            data["error"] = str(e)

        results.append(data)

        # Update progress
        current = i + 1
        percent = int(current / total * 100)
        progress_bar.progress(percent)
        progress_text.write(f"Scraper 3 (PDF): Processed {current} of {total} URLs")

    driver.quit()
    progress_text.write("Scraper 3: Finished!")
    return results
