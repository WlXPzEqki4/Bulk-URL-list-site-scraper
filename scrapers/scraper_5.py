# # scraper_5.py

# import os
# import re
# import json
# import nest_asyncio
# import asyncio
# import aiohttp
# import streamlit as st
# from bs4 import BeautifulSoup

# # We apply nest_asyncio so we can run an event loop within Streamlit
# nest_asyncio.apply()

# async def scrape_and_save(url, folder_path, session):
#     """
#     Asynchronously scrapes a URL using aiohttp and BeautifulSoup,
#     saving HTML, potential JSON, and metadata in a dedicated subfolder.
#     Returns a dictionary with {'url', 'filename', 'status', 'error'} for uniformity.
#     """
#     data = {"url": url, "filename": None, "status": None, "error": None}

#     try:
#         async with session.get(url) as response:
#             # Raise for 4xx or 5xx
#             response.raise_for_status()
#             html = await response.text()

#         # Create a subfolder for each URL
#         url_sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", url.replace("https://", "").replace("http://", ""))
#         url_folder = os.path.join(folder_path, url_sanitized)
#         os.makedirs(url_folder, exist_ok=True)

#         # Save the HTML content
#         html_filepath = os.path.join(url_folder, "page.html")
#         with open(html_filepath, "w", encoding="utf-8") as f:
#             f.write(html)

#         # Parse with BeautifulSoup
#         soup = BeautifulSoup(html, "html.parser")

#         # Attempt to extract JSON from <script type="application/json">
#         json_data = None
#         script_tags = soup.find_all("script", type="application/json")
#         if script_tags:
#             for script in script_tags:
#                 try:
#                     json_data = json.loads(script.string)
#                     break  # Take the first valid JSON
#                 except (json.JSONDecodeError, TypeError):
#                     continue

#         if json_data:
#             json_filepath = os.path.join(url_folder, "data.json")
#             try:
#                 with open(json_filepath, "w", encoding="utf-8") as f:
#                     json.dump(json_data, f, indent=4)
#             except Exception as e:
#                 pass  # If for some reason serialization fails, skip

#         # Extract title and meta description
#         title_tag = soup.find("title")
#         title = title_tag.text if title_tag else "No Title Found"
#         desc_tag = soup.find("meta", attrs={"name": "description"})
#         description = desc_tag["content"] if desc_tag and desc_tag.get("content") else "No Description Found"

#         # Save metadata
#         metadata_filepath = os.path.join(url_folder, "metadata.txt")
#         with open(metadata_filepath, "w", encoding="utf-8") as f:
#             f.write(f"URL: {url}\n")
#             f.write(f"Title: {title}\n")
#             f.write(f"Description: {description}\n")

#         data["filename"] = "page.html"
#         data["status"] = "success"

#     except aiohttp.ClientError as e:
#         data["status"] = "failed"
#         data["error"] = f"HTTP error: {e}"
#     except Exception as e:
#         data["status"] = "failed"
#         data["error"] = str(e)

#     return data


# async def async_main(urls, folder_path, progress_bar, progress_text):
#     """
#     Asynchronously gathers the scraping tasks, updating a progress bar after each URL completes.
#     Returns a list of results dicts.
#     """
#     results = []
#     total = len(urls)

#     async with aiohttp.ClientSession() as session:
#         tasks = [scrape_and_save(url, folder_path, session) for url in urls]

#         # We'll run them concurrently, but we want to track them as they complete
#         done_count = 0
#         for future in asyncio.as_completed(tasks):
#             result = await future
#             results.append(result)
#             done_count += 1
#             percent = int(done_count / total * 100)
#             progress_bar.progress(percent)
#             progress_text.write(f"Scraper 5 (aiohttp): Processed {done_count} of {total} URLs")

#     return results


# def run_scraper_5(urls, base_folder):
#     """
#     A top-level function that sets up the "5_crawl4ai_full" folder,
#     runs the asynchronous scraping, and returns a list of results.
#     """
#     subfolder_name = "5_crawl4ai_full"
#     save_folder = os.path.join(base_folder, subfolder_name)
#     os.makedirs(save_folder, exist_ok=True)

#     progress_bar = st.progress(0)
#     progress_text = st.empty()

#     # Because we're in Streamlit (already event-loop-based), nest_asyncio is needed
#     # We'll do an asyncio.run(...) call:
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     results = loop.run_until_complete(async_main(urls, save_folder, progress_bar, progress_text))
#     loop.close()

#     progress_text.write("Scraper 5: Finished!")
#     return results













# scraper_5.py

import os
import re
import json
import nest_asyncio
import asyncio
import aiohttp
import streamlit as st
from bs4 import BeautifulSoup

nest_asyncio.apply()

async def scrape_and_save(url, folder_path, session):
    data = {"url": url, "filename": None, "status": None, "error": None}
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()

        # Create subfolder per URL
        url_sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", url.replace("https://", "").replace("http://", ""))
        url_folder = os.path.join(folder_path, url_sanitized)
        os.makedirs(url_folder, exist_ok=True)

        # Save HTML
        html_filepath = os.path.join(url_folder, "page.html")
        with open(html_filepath, "w", encoding="utf-8") as f:
            f.write(html)

        soup = BeautifulSoup(html, "html.parser")
        # Attempt to extract JSON
        json_data = None
        script_tags = soup.find_all("script", type="application/json")
        for script in script_tags:
            try:
                json_data = json.loads(script.string)
                break
            except (json.JSONDecodeError, TypeError):
                pass

        if json_data:
            json_filepath = os.path.join(url_folder, "data.json")
            try:
                with open(json_filepath, "w", encoding="utf-8") as f:
                    json.dump(json_data, f, indent=4)
            except:
                pass

        # Title + meta description
        title_tag = soup.find("title")
        title = title_tag.text if title_tag else "No Title Found"
        desc_tag = soup.find("meta", attrs={"name":"description"})
        description = desc_tag["content"] if desc_tag and desc_tag.get("content") else "No Description Found"

        # Save metadata
        metadata_filepath = os.path.join(url_folder, "metadata.txt")
        with open(metadata_filepath, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\nTitle: {title}\nDescription: {description}\n")

        # <--- KEY FIX: store subfolder path in data["filename"]
        data["filename"] = f"{url_sanitized}/page.html"
        data["status"] = "success"

    except aiohttp.ClientError as e:
        data["status"] = "failed"
        data["error"] = f"HTTP error: {e}"
    except Exception as e:
        data["status"] = "failed"
        data["error"] = str(e)

    return data


async def async_main(urls, folder_path, progress_bar, progress_text):
    results = []
    total = len(urls)
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_and_save(url, folder_path, session) for url in urls]
        done_count = 0
        for future in asyncio.as_completed(tasks):
            result = await future
            results.append(result)
            done_count += 1
            percent = int(done_count / total * 100)
            progress_bar.progress(percent)
            progress_text.write(f"Scraper 5 (aiohttp): Processed {done_count} of {total} URLs")
    return results


def run_scraper_5(urls, base_folder):
    subfolder_name = "5_crawl4ai_full"
    save_folder = os.path.join(base_folder, subfolder_name)
    os.makedirs(save_folder, exist_ok=True)

    progress_bar = st.progress(0)
    progress_text = st.empty()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(async_main(urls, save_folder, progress_bar, progress_text))
    loop.close()

    progress_text.write("Scraper 5: Finished!")
    return results







