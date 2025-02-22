# # scraper_6.py

# import os
# import json
# import requests
# import re
# import streamlit as st
# from bs4 import BeautifulSoup

# def run_scraper_6(urls, base_folder):
#     """
#     Scrapes each URL with requests + BeautifulSoup,
#     extracting title, meta description, and main text content.
#     Saves each page's data as a JSON file in '6_BeautifulSoup_json'
#     within base_folder, returning a list of dicts with keys:
#       {'url', 'filename', 'status', 'error'}.

#     Also displays a Streamlit progress bar (for synchronous progress).
#     """
#     subfolder_name = "6_BeautifulSoup_json"
#     output_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(output_folder, exist_ok=True)

#     progress_bar = st.progress(0)
#     progress_text = st.empty()

#     results = []
#     file_count = 1
#     total = len(urls)

#     for i, url in enumerate(urls):
#         data = {"url": url, "filename": None, "status": None, "error": None}
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()  # Raise an HTTPError if status != 200

#             soup = BeautifulSoup(response.text, "html.parser")
#             # Extract page title
#             title_tag = soup.find("title")
#             title = title_tag.get_text(strip=True) if title_tag else "No title found"

#             # Extract meta description
#             desc_tag = soup.find("meta", attrs={"name": "description"})
#             meta_description = desc_tag["content"] if desc_tag and desc_tag.get("content") else ""

#             # Extract main text content
#             main_text = soup.get_text(separator=" ", strip=True)

#             # Prepare dictionary for JSON
#             page_data = {
#                 "url": url,
#                 "title": title,
#                 "meta_description": meta_description,
#                 "text_content": main_text
#             }

#             # Generate a file name based on domain + sequence number
#             domain = url.split("//")[-1].split("/")[0]  # Extract domain
#             domain_sanitized = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", domain)
#             file_name = f"{domain_sanitized}_{file_count}.json"
#             file_path = os.path.join(output_folder, file_name)

#             with open(file_path, "w", encoding="utf-8") as f:
#                 json.dump(page_data, f, indent=4, ensure_ascii=False)

#             data["filename"] = file_name
#             data["status"] = "success"

#             file_count += 1

#         except requests.exceptions.RequestException as e:
#             data["status"] = "failed"
#             data["error"] = f"Request error: {e}"
#         except Exception as e:
#             data["status"] = "failed"
#             data["error"] = str(e)

#         results.append(data)

#         # Update progress
#         current = i + 1
#         percent = int(current / total * 100)
#         progress_bar.progress(percent)
#         progress_text.write(f"Scraper 6 (BeautifulSoup JSON): Processed {current} of {total} URLs")

#     progress_text.write("Scraper 6: Finished!")
#     return results






# scraper_6.py
import os
import json
import requests
import re
import streamlit as st
from bs4 import BeautifulSoup

def run_scraper_6(urls, base_folder):
    subfolder_name = "6_BeautifulSoup_json"
    output_folder = os.path.join(base_folder, subfolder_name)
    os.makedirs(output_folder, exist_ok=True)

    progress_bar = st.progress(0)
    progress_text = st.empty()

    results = []
    file_count = 1
    total = len(urls)

    for i, url in enumerate(urls):
        # Check if user requested stop
        if st.session_state.get("stop_requested"):
            progress_text.write("Scraper 6: Stopped by user request!")
            break

        data = {"url": url, "filename": None, "status": None, "error": None}
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            title_tag = soup.find("title")
            title = title_tag.get_text(strip=True) if title_tag else "No title found"

            desc_tag = soup.find("meta", attrs={"name": "description"})
            meta_description = desc_tag["content"] if desc_tag and desc_tag.get("content") else ""
            main_text = soup.get_text(separator=" ", strip=True)

            page_data = {
                "url": url,
                "title": title,
                "meta_description": meta_description,
                "text_content": main_text
            }

            domain = url.split("//")[-1].split("/")[0]
            domain_sanitized = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", domain)
            file_name = f"{domain_sanitized}_{file_count}.json"
            file_path = os.path.join(output_folder, file_name)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(page_data, f, indent=4, ensure_ascii=False)

            data["filename"] = file_name
            data["status"] = "success"
            file_count += 1

        except requests.exceptions.RequestException as e:
            data["status"] = "failed"
            data["error"] = f"Request error: {e}"
        except Exception as e:
            data["status"] = "failed"
            data["error"] = str(e)

        results.append(data)

        current = i + 1
        percent = int(current / total * 100)
        progress_bar.progress(percent)
        progress_text.write(f"Scraper 6 (BeautifulSoup JSON): Processed {current} of {total} URLs")

    progress_text.write("Scraper 6: Finished!")
    return results
