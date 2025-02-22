# # scrapers/scraper_2.py
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def run_scraper_2(urls, base_folder):
#     """
#     Uses Selenium (headless Chrome) to fetch fully rendered HTML for each URL.
#     Saves each page to a subfolder named '2_Rendered_HTML_saved_webpages' within 'base_folder'.

#     Returns a list of dicts, each with fields: {'url', 'status', 'filename', 'error'}.
#     """

#     subfolder_name = "2_Rendered_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     results = []

#     # Configure Selenium (headless Chrome)
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")

#     # Create a WebDriver instance
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     for url in urls:
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             driver.get(url)
#             time.sleep(3)  # Wait for JavaScript to render (adjust as needed)

#             # Get fully rendered HTML
#             html_content = driver.page_source

#             # Generate filename from URL
#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)

#             # Save rendered HTML to file
#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(html_content)

#             data["filename"] = filename
#             data["status"] = "success"
#         except Exception as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#     driver.quit()
#     return results









# # scrapers/scraper_2.py
# import os
# import time
# import streamlit as st  # needed for st.progress()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def run_scraper_2(urls, base_folder):
#     """
#     Uses Selenium to fetch fully rendered HTML for each URL.
#     Saves each page to '2_Rendered_HTML_saved_webpages'.
#     Returns a list of dicts: [{'url', 'status', 'filename', 'error'}, ...]
#     Includes a progress bar to show how many URLs are processed.
#     """
#     subfolder_name = "2_Rendered_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     results = []
#     total = len(urls)

#     # Configure Selenium
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     progress_bar = st.progress(0)
#     progress_text = st.empty()

#     for i, url in enumerate(urls):
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             driver.get(url)
#             time.sleep(3)  # Wait for JS to render

#             html_content = driver.page_source

#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)

#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(html_content)

#             data["filename"] = filename
#             data["status"] = "success"
#         except Exception as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#         # Update progress
#         current = i + 1
#         percent = int((current / total) * 100)
#         progress_bar.progress(percent)
#         progress_text.write(f"Scraper 2: Processed {current} of {total} URLs")

#     driver.quit()
#     progress_text.write("Scraper 2: Finished!")
#     return results








# # scrapers/scraper_2.py
# import os
# import time
# import streamlit as st
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def run_scraper_2(urls, base_folder):
#     """
#     Uses Selenium to fetch fully rendered HTML for each URL.
#     Saves each page to '2_Rendered_HTML_saved_webpages'.
#     Returns a list of dicts: [{'url', 'status', 'filename', 'error'}, ...]
#     Includes a progress bar to show how many URLs are processed.
#     """
#     subfolder_name = "2_Rendered_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     results = []
#     total = len(urls)

#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     progress_bar = st.progress(0)
#     progress_text = st.empty()

#     for i, url in enumerate(urls):
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             driver.get(url)
#             time.sleep(3)  # wait for JS

#             html_content = driver.page_source
#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)

#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(html_content)

#             data["filename"] = filename
#             data["status"] = "success"
#         except Exception as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#         current = i + 1
#         percent = int(current / total * 100)
#         progress_bar.progress(percent)
#         progress_text.write(f"Scraper 2: Processed {current} of {total} URLs")

#     driver.quit()
#     progress_text.write("Scraper 2: Finished!")
#     return results










# scrapers/scraper_2.py
import os
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def run_scraper_2(urls, base_folder):
    """
    Uses Selenium (headless Chrome) to fetch fully rendered HTML for each URL.
    Saves each page to '2_Rendered_HTML_saved_webpages'.
    Returns a list of dicts: [{'url', 'status', 'filename', 'error'}, ...]
    Includes a progress bar to show how many URLs are processed.
    Suitable for deployment on Streamlit Cloud.
    """
    subfolder_name = "2_Rendered_HTML_saved_webpages"
    save_folder = os.path.join(base_folder, subfolder_name)
    os.makedirs(save_folder, exist_ok=True)

    results = []
    total = len(urls)

    # Set up headless Chrome for Streamlit Cloud
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use webdriver-manager to install and manage the ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Track progress in the Streamlit UI
    progress_bar = st.progress(0)
    progress_text = st.empty()

    for i, url in enumerate(urls):
        data = {"url": url, "filename": None, "status": None, "error": None}
        try:
            driver.get(url)
            time.sleep(3)  # wait for JS to render (adjust as needed)

            html_content = driver.page_source
            filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
            filepath = os.path.join(save_folder, filename)

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(html_content)

            data["filename"] = filename
            data["status"] = "success"
        except Exception as e:
            data["status"] = "failed"
            data["error"] = str(e)

        results.append(data)

        # Update Streamlit progress
        current = i + 1
        percent = int(current / total * 100)
        progress_bar.progress(percent)
        progress_text.write(f"Scraper 2: Processed {current} of {total} URLs")

    driver.quit()
    progress_text.write("Scraper 2: Finished!")
    return results



