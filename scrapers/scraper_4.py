# scraper_4.py

import os
import time
import base64
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.print_page_options import PrintOptions

def run_scraper_4(urls, base_folder):
    """
    Uses Selenium with headless Chrome (old stable headless mode) to print each URL to PDF.
    Saves each PDF in '4_PDF_2' under the provided base folder.

    Returns a list of dicts: [
      {"url": <URL>, "filename": <filename>, "status": "success"/"failed", "error": <error or None>},
      ...
    ]

    Also displays a Streamlit progress bar to track the PDF creation.
    """

    subfolder_name = "4_PDF_2"
    save_folder = os.path.join(base_folder, subfolder_name)
    os.makedirs(save_folder, exist_ok=True)

    # Configure headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")     # old stable headless
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Prepare Selenium 4 PrintOptions
    print_options = PrintOptions()
    # Example: if you want to specify page size, do: print_options.page_size = 'A4'
    #          or print_options.shrink_to_fit = True (optional)

    results = []
    total = len(urls)

    progress_bar = st.progress(0)
    progress_text = st.empty()

    for i, url in enumerate(urls):
        data = {"url": url, "filename": None, "status": None, "error": None}
        try:
            driver.get(url)
            time.sleep(5)  # give the page time to load

            filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".pdf"
            filepath = os.path.join(save_folder, filename)

            # Print to PDF (Base64-encoded)
            pdf_base64 = driver.print_page(print_options)

            with open(filepath, "wb") as f:
                f.write(base64.b64decode(pdf_base64))

            data["filename"] = filename
            data["status"] = "success"
        except Exception as e:
            data["status"] = "failed"
            data["error"] = str(e)

        results.append(data)

        # Update progress bar
        current = i + 1
        percent = int(current / total * 100)
        progress_bar.progress(percent)
        progress_text.write(f"Scraper 4 (PDF_2): Processed {current} of {total} URLs")

    driver.quit()
    progress_text.write("Scraper 4: Finished!")
    return results
