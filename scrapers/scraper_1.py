# import os
# import requests

# def run_scraper_1(urls, base_folder):
#     """
#     Scrapes a list of URLs, saving each page to a subfolder named '1_HTML_saved_webpages'
#     within the provided base folder.

#     :param urls: A list of URLs (strings) to fetch.
#     :param base_folder: The path to the main output folder (user-specified).
#     """
#     # Name of the subfolder for this scraper's output
#     subfolder_name = "1_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     for url in urls:
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()  # Raise error for bad responses

#             # Generate filename from URL
#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)

#             # Save HTML to file
#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(response.text)

#             print(f"[Scraper 1] ✅ Saved: {filename}")

#         except requests.exceptions.RequestException as e:
#             print(f"[Scraper 1] ❌ Failed to fetch {url}: {e}")

#     print("\n[Scraper 1] 🎉 All pages saved successfully in:", save_folder)












# # scraper_1.py
# import os
# import requests

# def run_scraper_1(urls, base_folder):
#     """
#     Scrapes a list of URLs, saving each page to a subfolder named '1_HTML_saved_webpages'
#     within the provided base folder.

#     Returns a list of dicts with fields: {'url', 'status', 'filename', 'error'}.

#     :param urls: A list of URLs to fetch.
#     :param base_folder: The directory in which to create the '1_HTML_saved_webpages' subfolder.
#     """
#     subfolder_name = "1_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     results = []

#     for url in urls:
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()  # Raise error for bad responses

#             # Generate filename from URL
#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)

#             # Save HTML to file
#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(response.text)

#             data["filename"] = filename
#             data["status"] = "success"
#         except requests.exceptions.RequestException as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#     return results









# # scraper_1.py
# import os
# import requests

# def run_scraper_1(urls, base_folder):
#     """
#     Scrapes the URLs, saving each page to '1_HTML_saved_webpages' in the base_folder.
#     Returns a list of dicts with fields: {'url', 'status', 'filename', 'error'}.
#     """
#     subfolder_name = "1_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     results = []

#     for url in urls:
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()

#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)
            
#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(response.text)

#             data["filename"] = filename
#             data["status"] = "success"
#         except requests.exceptions.RequestException as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#     return results







# # scrapers/scraper_1.py
# import os
# import requests
# import streamlit as st  # so we can use st.progress() here

# def run_scraper_1(urls, base_folder):
#     """
#     Scrapes a list of URLs, saving each page to '1_HTML_saved_webpages'.
#     Returns a list of dicts: [{'url', 'status', 'filename', 'error'}, ...]
#     Includes a progress bar to show how many URLs are processed.
#     """
#     subfolder_name = "1_HTML_saved_webpages"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     results = []
#     total = len(urls)

#     # Create a progress bar and a text placeholder for "X of Y" updates
#     progress_bar = st.progress(0)
#     progress_text = st.empty()

#     for i, url in enumerate(urls):
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()

#             filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
#             filepath = os.path.join(save_folder, filename)

#             with open(filepath, "w", encoding="utf-8") as file:
#                 file.write(response.text)

#             data["filename"] = filename
#             data["status"] = "success"
#         except requests.exceptions.RequestException as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#         # Update progress
#         current = i + 1
#         percent = int((current / total) * 100)
#         progress_bar.progress(percent)
#         progress_text.write(f"Scraper 1: Processed {current} of {total} URLs")

#     # Wrap up
#     progress_text.write("Scraper 1: Finished!")
#     return results




# scrapers/scraper_1.py
import os
import requests
import streamlit as st

def run_scraper_1(urls, base_folder):
    """
    Scrapes a list of URLs, saving each page to '1_HTML_saved_webpages'.
    Returns a list of dicts: [{'url', 'status', 'filename', 'error'}, ...]
    Includes a progress bar to show how many URLs are processed.
    """
    subfolder_name = "1_HTML_saved_webpages"
    save_folder = os.path.join(base_folder, subfolder_name)
    os.makedirs(save_folder, exist_ok=True)

    results = []
    total = len(urls)

    progress_bar = st.progress(0)
    progress_text = st.empty()

    for i, url in enumerate(urls):
        data = {"url": url, "filename": None, "status": None, "error": None}
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
            filepath = os.path.join(save_folder, filename)

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(response.text)

            data["filename"] = filename
            data["status"] = "success"
        except requests.exceptions.RequestException as e:
            data["status"] = "failed"
            data["error"] = str(e)

        results.append(data)

        current = i + 1
        percent = int(current / total * 100)
        progress_bar.progress(percent)
        progress_text.write(f"Scraper 1: Processed {current} of {total} URLs")

    progress_text.write("Scraper 1: Finished!")
    return results
