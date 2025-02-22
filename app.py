# import streamlit as st
# import os

# # Import the six scraper functions
# from scrapers.scraper_1 import scraper_1_run
# from scrapers.scraper_2 import scraper_2_run
# from scrapers.scraper_3 import scraper_3_run
# from scrapers.scraper_4 import scraper_4_run
# from scrapers.scraper_5 import scraper_5_run
# from scrapers.scraper_6 import scraper_6_run

# def main():
#     st.title("Modular Multi-Scraper App")

#     st.write("""
#     ### How to Use:
#     1. Paste your URLs below, one per line (or comma-separated).
#     2. Choose or create an output folder path.
#     3. Click 'Start Scraping'.
#     """)

#     # 1) Text area for URLs
#     default_text = '''"https://lovin.co/baghdad/en/latest/unesco-celebrates-the-reconstruction-of-al-hadba-minaret-in-mosul/",
# "https://www.news9live.com/knowledge/mosul-al-nuri-mosque-iraq-historical-site-which-has-risen-from-the-rubbles-with-its-minaret-2819472",
# "https://www.devdiscourse.com/article/entertainment/3261650-revival-of-mosuls-iconic-al-nuri-mosque-a-symbol-of-resilience",
# "https://www.turkiyetoday.com/culture/seljuk-masterpiece-al-hadba-minaret-in-mosul-reopens-after-daesh-destruction-119366/",
# "https://www.rudaw.net/english/middleeast/iraq/06022025",
# "https://www.therogersvillereview.com/news/national/article_fff44584-0b03-548f-9f0a-685efaefdcb3.html",
# "https://uk.news.yahoo.com/iraqs-famed-hunchback-mosul-rebuilt-083314374.html?guccounter=1",
# "https://caliber.az/en/post/historic-minaret-churches-in-mosul-rise-from-ruins-of-isis-destruction",
# "https://shafaq.com/en/Iraq/Mosul-celebrates-minaret-mosque-reopening-soon",
# "https://www.asianews.it/news-en/Mosul-regains-its-minaret.-Abp.-Moussa:-a-new-culture,-fanaticism-will-not-return.-62527.html",
# "https://www.straitstimes.com/world/middle-east/mosul%E2%80%99s-renowned-minaret-restored-from-ravages-of-islamic-state",
# "https://www.msn.com/en-au/news/other/war-ravaged-landmarks-in-iraq-s-mosul-are-reopening-after-unesco-led-restoration-project/ar-AA1yAdgP",
# "https://www.thealbertan.com/religion-news/historic-landmarks-in-iraqs-mosul-are-reopening-as-the-city-heals-from-islamic-state-devastation-10198197",
# "https://www.artnews.com/art-news/news/mosul-heritage-sites-restored-by-unesco-1234731726/",
# "https://www.thenationalnews.com/news/mena/2025/02/05/mosul-isis-unesco-reconstruction-al-nuri-mosque/",
# "https://www.france24.com/en/video/20250205-iraq-mosul-s-historic-al-nuri-mosque-and-al-hadba-minaret-rise-again",
# "https://www.euronews.com/culture/2025/02/07/war-ravaged-landmarks-in-iraqs-mosul-are-reopening-after-unesco-led-restoration-project",
# "https://www.thenationalnews.com/news/mena/2025/02/05/unesco-chief-says-mosul-beacon-of-hope-for-iraq-after-al-nuri-mosque-restoration-completed/",
# "https://www.france24.com/en/live-news/20250205-iraq-s-famed-hunchback-of-mosul-rebuilt-brick-by-brick",
# "https://www.ucanews.com/featured-videos",
# "https://www.voanews.com/a/voa-kurdish-three-religious-and-cultural-projects-restored-in-mosul-/7964418.html",
# "https://www.theartnewspaper.com/2025/02/05/unesco-completes-restoration-mosul-heritage-sites-damaged-under-isis",
# "https://www.dw.com/en/iraq-unesco-supports-reconstruction-of-mosul-treasures/a-71505694",
# "https://news.un.org/en/story/2025/02/1159891",
# "https://www.internationalaffairs.org.au/australianoutlook/heritage-and-healing-a-decade-on-from-the-destruction-of-the-mosul-museum/",
# "https://www.bbc.com/news/articles/cjw4zv533g7o"'''

#     urls_text = st.text_area("Paste URLs (one per line, or comma-separated):", value=default_text, height=300)

#     # 2) Choose or create an output folder
#     folder_path = st.text_input("Output folder path:", value="my_output")

#     if st.button("Start Scraping"):
#         # Parse user input
#         # - We'll remove quotes, split by commas or new lines, and then strip extra whitespace.
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return
        
#         # Attempt to parse the text into a list of URLs
#         # A simple approach: replace newlines with commas, split on commas, strip out quotes/spaces
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]

#         if not urls:
#             st.warning("No valid URLs detected.")
#             return

#         # Ensure the base folder exists
#         os.makedirs(folder_path, exist_ok=True)

#         st.info("Starting all scrapers... please wait.")

#         # Call each scraper in turn
#         try:
#             scraper_1_run(urls, folder_path)
#             scraper_2_run(urls, folder_path)
#             scraper_3_run(urls, folder_path)
#             scraper_4_run(urls, folder_path)
#             scraper_5_run(urls, folder_path)
#             scraper_6_run(urls, folder_path)

#             st.success("All scrapers have completed successfully!")
#             st.write(f"Output saved under: `{folder_path}`")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()












# # app.py (simplified example)
# import streamlit as st
# import os

# # Import the scraper function
# from scrapers.scraper_1 import run_scraper_1

# def main():
#     st.title("Modular Multi-Scraper App")

#     # Text area for URLs
#     urls_text = st.text_area("Paste URLs (comma or newline separated):", height=250)

#     # Output folder input
#     base_folder = st.text_input("Output folder path:", "my_output")

#     if st.button("Start Scraping"):
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return
        
#         # Convert input text to a list of URLs (split on newlines or commas)
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]

#         # Create the base folder if needed
#         os.makedirs(base_folder, exist_ok=True)

#         # Run scraper 1
#         run_scraper_1(urls, base_folder)

#         st.success("Scraper 1 has finished. Check your output folder for results.")

# if __name__ == "__main__":
#     main()









# import streamlit as st
# import os
# import subprocess
# from urllib.parse import quote

# # Import your scraper(s)
# from scrapers.scraper_1 import run_scraper_1

# def main():
#     st.title("Modular Multi-Scraper App")

#     st.write("""
#     ## How to Use
#     1. Paste your URLs below, one per line or comma-separated.
#     2. Enter or create a folder path in the text input (local usage).
#     3. Optionally, click the "Browse Folder" button (may only work if your app is local).
#     4. Click "Start Scraping".
#     """)

#     # 1) URLs text area
#     urls_text = st.text_area("Paste URLs:", height=200)

#     # 2) Output folder input
#     folder_label = "Choose or create an output folder path:"
#     folder_path = st.text_input(folder_label, "my_output")

#     # 2a) Optional: "Browse" button (Windows-only example).
#     # For local usage, this calls an OS file explorer to pick a folder.
#     # Streamlit won't automatically capture the chosen path—this is a hack.
#     if st.button("Browse Folder (Local Only)"):
#         # Attempt to open a system dialog using Python's built-in "explorer.exe" on Windows
#         # This won't automatically pass back the result to Streamlit - user must copy/paste.
#         try:
#             subprocess.Popen(["explorer", "."])  # or explorer folder_path
#             st.info("Explorer opened. Please copy the path from Explorer and paste it above.")
#         except Exception as e:
#             st.error(f"Could not open Explorer: {e}")

#     if st.button("Start Scraping"):
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # 3) Parse the URL text
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # 4) Ensure the base folder exists
#         os.makedirs(folder_path, exist_ok=True)

#         # 5) Run the scraper
#         results_1 = run_scraper_1(urls, folder_path)

#         # Summarise results
#         success_count = sum(r["status"] == "success" for r in results_1)
#         fail_count = sum(r["status"] == "failed" for r in results_1)

#         # 6) Provide a clickable link to the output folder (works if local)
#         # For local paths, we can attempt "file://..." links.
#         folder_url = f"file://{quote(os.path.abspath(folder_path))}"  # url-encoded path
#         st.success(f"Scraper 1 has finished. Successfully scraped {success_count} of {len(urls)} URLs.")
#         st.markdown(f"[Open output folder in Explorer (local only)]({folder_url})")

#         # 7) Expandable / collapsible log of each result
#         with st.expander("Detailed Results"):
#             st.write(f"**Success count**: {success_count}, **Fail count**: {fail_count}")
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item["error"] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

# if __name__ == "__main__":
#     main()













# import streamlit as st
# import os

# # Import your scraper(s)
# from scrapers.scraper_1 import run_scraper_1

# def main():
#     st.title("Modular Multi-Scraper App (Hosted Version)")

#     st.write("""
#     ## How to Use
#     1. Paste your URLs below, one per line or comma-separated.
#     2. Enter or create a folder path in the text input (the app will store files in a subfolder on this server).
#     3. Click "Start Scraping".
#     """)

#     # 1) URLs text area
#     urls_text = st.text_area("Paste URLs:", height=200)

#     # 2) Output folder input (within the app's file system)
#     folder_label = "Choose or create an output folder path (on the server):"
#     folder_path = st.text_input(folder_label, "my_output")

#     # 3) Start Scraping button
#     if st.button("Start Scraping"):
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URL text
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # Ensure the base folder exists
#         os.makedirs(folder_path, exist_ok=True)

#         # Run the scraper
#         results_1 = run_scraper_1(urls, folder_path)

#         # Summarise results
#         success_count = sum(r["status"] == "success" for r in results_1)
#         fail_count = sum(r["status"] == "failed" for r in results_1)
#         total_urls = len(urls)

#         st.success(
#             f"Scraper 1 has finished. "
#             f"Successfully scraped {success_count} of {total_urls} URLs. "
#             f"({fail_count} failed.)"
#         )

#         # Expandable / collapsible log of each result
#         with st.expander("Detailed Results"):
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

# if __name__ == "__main__":
#     main()



















# # app.py
# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scraper(s)
# from scrapers.scraper_1 import run_scraper_1
# # from scrapers.scraper_2 import run_scraper_2
# # etc...

# def main():
#     st.title("Modular Multi-Scraper App with Download Buttons")

#     st.write("""
#     ## How to Use
#     1. Paste your URLs below, one per line or comma-separated.
#     2. Enter or create a folder path in the text input.
#     3. Click "Start Scraping".
#     4. After scraping, download the zipped HTML files via the download button.
#     """)

#     # 1) URLs text area
#     urls_text = st.text_area("Paste URLs:", height=200)

#     # 2) Output folder input
#     folder_label = "Choose or create an output folder path (on the server):"
#     folder_path = st.text_input(folder_label, "my_output")

#     # 3) "Start Scraping" button
#     if st.button("Start Scraping"):
#         # Validate URL input
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URL text
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # Create base folder if needed
#         os.makedirs(folder_path, exist_ok=True)

#         # Run Scraper 1
#         results_1 = run_scraper_1(urls, folder_path)

#         # Summarise results
#         success_count = sum(r["status"] == "success" for r in results_1)
#         fail_count = sum(r["status"] == "failed" for r in results_1)
#         total_urls = len(urls)

#         st.success(
#             f"Scraper 1 has finished. Successfully scraped {success_count} of {total_urls} URLs. "
#             f"({fail_count} failed.)"
#         )

#         # 4) Provide an expander for detailed logs
#         with st.expander("Detailed Results (Scraper 1)"):
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#         # 5) Create a ZIP of all successfully scraped files
#         zip_buffer = BytesIO()
#         with zipfile.ZipFile(zip_buffer, "w") as zf:
#             for item in results_1:
#                 if item["status"] == "success" and item["filename"]:
#                     # The file path on disk
#                     scraper_subfolder = "1_HTML_saved_webpages"
#                     file_path = os.path.join(folder_path, scraper_subfolder, item["filename"])

#                     # Add the file to the ZIP archive
#                     # arcname is how the file will be named inside the ZIP
#                     zf.write(file_path, arcname=item["filename"])

#         # Prepare the ZIP data for download
#         zip_buffer.seek(0)

#         # 6) Download button for the ZIP
#         st.download_button(
#             label="Download Scraper 1 Files (ZIP)",
#             data=zip_buffer.getvalue(),
#             file_name="scraper_1_html_files.zip",
#             mime="application/zip"
#         )

#         # 7) Repeat the same pattern for scraper_2, scraper_3, etc.
#         # results_2 = run_scraper_2(urls, folder_path)
#         # ... create a second expander ...
#         # ... build a second zip ...
#         # st.download_button("Download Scraper 2 Files (ZIP)", data=..., ...)
#         # and so on...

# if __name__ == "__main__":
#     main()














# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scraper(s)
# from scrapers.scraper_1 import run_scraper_1
# # from scrapers.scraper_2 import run_scraper_2
# # etc...

# def main():
#     st.title("Modular Multi-Scraper App")

#     # -------------------------
#     # URL FORMATTING HELPER
#     # -------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```plaintext
#     "https://url1.com",
#     "https://url2.com",
#     "https://url3.com"
#     ```
#     Paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         "Paste raw URLs here (one per line):",
#         value="",
#         height=150
#     )

#     if st.button("Format URLs"):
#         # Split on newlines, strip whitespace
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]

#         if lines:
#             # Wrap each line in double quotes, add a comma except the last line
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 if i < len(lines) - 1:
#                     formatted_lines.append(f"\"{line}\",")
#                 else:
#                     formatted_lines.append(f"\"{line}\"")

#             # Join them back together with line breaks
#             formatted_output = "\n".join(formatted_lines)

#             st.text_area(
#                 "Formatted URLs (copy/paste into the scraper section below):",
#                 value=formatted_output,
#                 height=150
#             )
#         else:
#             st.warning("No valid URLs were detected to format.")

#     st.markdown("---")

#     # -------------------------
#     # SCRAPER SECTION
#     # -------------------------
#     st.subheader("Scraper Input")

#     st.write("""
#     ### How to Use
#     1. Paste your (properly formatted) URLs below, one per line or comma-separated.
#     2. Enter or create a folder path in the text input (for the app's ephemeral file system).
#     3. Click "Start Scraping".
#     4. Download your scraped files before the session ends.
#     """)

#     # 1) URLs text area
#     urls_text = st.text_area("Paste URLs for Scraping:", height=200)

#     # 2) Output folder input
#     folder_label = "Choose or create an output folder path (on the server):"
#     folder_path = st.text_input(folder_label, "my_output")

#     # 3) "Start Scraping" button
#     if st.button("Start Scraping"):
#         # Validate URL input
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URL text
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # Create base folder if needed
#         os.makedirs(folder_path, exist_ok=True)

#         # ------------------------------------
#         # Run Scraper 1 (example)
#         # ------------------------------------
#         results_1 = run_scraper_1(urls, folder_path)

#         # Summarise results
#         success_count = sum(r["status"] == "success" for r in results_1)
#         fail_count = sum(r["status"] == "failed" for r in results_1)
#         total_urls = len(urls)

#         st.success(
#             f"Scraper 1 has finished. "
#             f"Successfully scraped {success_count} of {total_urls} URLs. "
#             f"({fail_count} failed.)"
#         )

#         # Detailed results
#         with st.expander("Detailed Results (Scraper 1)"):
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#         # ZIP creation for download
#         zip_buffer = BytesIO()
#         with zipfile.ZipFile(zip_buffer, "w") as zf:
#             for item in results_1:
#                 if item["status"] == "success" and item["filename"]:
#                     subfolder = "1_HTML_saved_webpages"
#                     file_path = os.path.join(folder_path, subfolder, item["filename"])
#                     zf.write(file_path, arcname=item["filename"])
#         zip_buffer.seek(0)

#         # Download button
#         st.download_button(
#             label="Download Scraper 1 Files (ZIP)",
#             data=zip_buffer.getvalue(),
#             file_name="scraper_1_html_files.zip",
#             mime="application/zip"
#         )

#         # ------------------------------------
#         # Example: Run other scrapers likewise
#         # ------------------------------------
#         # results_2 = run_scraper_2(urls, folder_path)
#         # ... summary, expander, zip ...
#         # st.download_button(...)

# if __name__ == "__main__":
#     main()







# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scraper(s)
# from scrapers.scraper_1 import run_scraper_1
# # from scrapers.scraper_2 import run_scraper_2
# # ... etc ...

# def main():
#     st.title("Modular Multi-Scraper App")

#     # -------------------------
#     # URL FORMATTING HELPER
#     # -------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have **raw URLs** (one per line) and want them in the form:
#     ```
#     "https://example.com",
#     "https://another-site.org",
#     "https://foo.bar"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="e.g.\nhttps://example.com\nhttps://another-site.org\n...",
#         height=150
#     )

#     if st.button("Format URLs"):
#         # Split on newlines, strip whitespace
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]

#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 # Append a comma after each line except the last
#                 if i < len(lines) - 1:
#                     formatted_lines.append(f"\"{line}\",")
#                 else:
#                     formatted_lines.append(f"\"{line}\"")

#             formatted_output = "\n".join(formatted_lines)

#             st.text_area(
#                 label="Formatted URLs (copy/paste these below):",
#                 value=formatted_output,
#                 height=150
#             )
#         else:
#             st.warning("No valid URLs were detected to format.")

#     st.markdown("---")

#     # -------------------------
#     # SCRAPER SECTION
#     # -------------------------
#     st.subheader("Scraper Input")
#     st.write("""
#     ### How to Use
#     1. Paste your URLs below (they can be comma-separated, newline-separated, or the fully formatted form).
#     2. Enter or create an output folder path (files are stored on this server temporarily).
#     3. Click "Start Scraping".
#     4. Download your scraped files (ZIP) when done.
#     """)

#     # 1) URLs text area for actual scraping
#     urls_text = st.text_area("Paste URLs for Scraping:", height=200)

#     # 2) Output folder input
#     folder_label = "Choose or create an output folder path:"
#     folder_path = st.text_input(folder_label, "my_output")

#     # 3) "Start Scraping" button
#     if st.button("Start Scraping"):
#         # Validate URL input
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URL text (splitting on commas or newlines)
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # Create the base output folder (ephemeral storage)
#         os.makedirs(folder_path, exist_ok=True)

#         # ------------------------------------
#         # Run Scraper 1 as an example
#         # ------------------------------------
#         results_1 = run_scraper_1(urls, folder_path)

#         # Summarise results
#         success_count = sum(r["status"] == "success" for r in results_1)
#         fail_count = sum(r["status"] == "failed" for r in results_1)
#         total_urls = len(urls)

#         # Show summary in a success box
#         st.success(
#             f"Scraper 1 completed. "
#             f"Successfully scraped {success_count} of {total_urls} URLs. "
#             f"({fail_count} failed.)"
#         )

#         # Detailed logs in an expander
#         with st.expander("Detailed Results (Scraper 1)"):
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#         # Create a ZIP in memory of all successfully scraped files
#         zip_buffer = BytesIO()
#         with zipfile.ZipFile(zip_buffer, "w") as zf:
#             for item in results_1:
#                 if item["status"] == "success" and item["filename"]:
#                     subfolder = "1_HTML_saved_webpages"
#                     file_path = os.path.join(folder_path, subfolder, item["filename"])
#                     zf.write(file_path, arcname=item["filename"])
#         zip_buffer.seek(0)

#         # Download button for the ZIP
#         st.download_button(
#             label="Download Scraper 1 Files (ZIP)",
#             data=zip_buffer.getvalue(),
#             file_name="scraper_1_html_files.zip",
#             mime="application/zip"
#         )

#         # ------------------------------------
#         # Example: Repeat for additional scrapers
#         # ------------------------------------
#         # results_2 = run_scraper_2(urls, folder_path)
#         # Summarise, expand logs, create ZIP, st.download_button, etc.
#         # ... repeat as needed ...

# if __name__ == "__main__":
#     main()




















# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scraper(s)
# from scrapers.scraper_1 import run_scraper_1
# # from scrapers.scraper_2 import run_scraper_2
# # etc...

# # -------------------------------------------------
# # 1) Custom CSS to style Streamlit buttons
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* All buttons share this style */
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important; /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def main():
#     # Apply the custom style
#     set_button_style()

#     st.title("Modular Multi-Scraper App")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     # If these keys don't exist, initialise them
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""

#     # -------------------------------------------------
#     # 2) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have **raw URLs** (one per line) and want them in the form:
#     ```
#     "https://example.com",
#     "https://another-site.org",
#     "https://foo.bar"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     # Raw input for formatting
#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="e.g.\nhttps://example.com\nhttps://another-site.org\n...",
#         height=150
#     )

#     # "Format URLs" button
#     if st.button("Format URLs"):
#         # Split on newlines, strip whitespace
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]

#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 # Append a comma after each line except the last
#                 if i < len(lines) - 1:
#                     formatted_lines.append(f"\"{line}\",")
#                 else:
#                     formatted_lines.append(f"\"{line}\"")

#             # Store in session state so we can still access it after re-run
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # If we have something in session_state, show it in a text area
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=150
#         )

#         # "Paste to Scraper" button
#         if st.button("Paste to Scraper"):
#             # Move the formatted output into the scraper input area
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs pasted to the scraper input below.")

#     st.markdown("---")

#     # -------------------------------------------------
#     # 3) SCRAPER SECTION
#     # -------------------------------------------------
#     st.subheader("Scraper Input")
#     st.write("""
#     ### How to Use
#     1. Paste your URLs below (comma- or newline-separated, or the fully formatted form).
#     2. Enter or create an output folder path.
#     3. Click "Start Scraping".
#     4. Download your scraped files before the session ends (if using a hosted service).
#     """)

#     # This text area is bound to session_state["scraper_input"]
#     urls_text = st.text_area(
#         "Paste URLs for Scraping:",
#         height=200,
#         key="scraper_input"
#     )

#     # Output folder input
#     folder_label = "Choose or create an output folder path:"
#     folder_path = st.text_input(folder_label, "my_output")

#     # "Start Scraping" button
#     if st.button("Start Scraping"):
#         # Validate URL input
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URL text (splitting on commas or newlines)
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]

#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # Create the base output folder
#         os.makedirs(folder_path, exist_ok=True)

#         # ------------------------------------
#         # Run Scraper 1
#         # ------------------------------------
#         results_1 = run_scraper_1(urls, folder_path)

#         # Summarise results
#         success_count = sum(r["status"] == "success" for r in results_1)
#         fail_count = sum(r["status"] == "failed" for r in results_1)
#         total_urls = len(urls)

#         # Show summary
#         st.success(
#             f"Scraper 1 completed. "
#             f"Successfully scraped {success_count} of {total_urls} URLs. "
#             f"({fail_count} failed.)"
#         )

#         # Detailed logs in an expander
#         with st.expander("Detailed Results (Scraper 1)"):
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#         # Create a ZIP in memory of all successfully scraped files
#         zip_buffer = BytesIO()
#         with zipfile.ZipFile(zip_buffer, "w") as zf:
#             for item in results_1:
#                 if item["status"] == "success" and item["filename"]:
#                     subfolder = "1_HTML_saved_webpages"
#                     file_path = os.path.join(folder_path, subfolder, item["filename"])
#                     zf.write(file_path, arcname=item["filename"])
#         zip_buffer.seek(0)

#         # Download button for the ZIP
#         st.download_button(
#             label="Download Scraper 1 Files (ZIP)",
#             data=zip_buffer.getvalue(),
#             file_name="scraper_1_html_files.zip",
#             mime="application/zip"
#         )

#         # ------------------------------------
#         # Additional scrapers go here...
#         # ------------------------------------
#         # results_2 = run_scraper_2(urls, folder_path)
#         # Summaries, expanders, zips, etc.

# if __name__ == "__main__":
#     main()













# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import scraper 1 & scraper 2
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # 1) Custom CSS to style Streamlit buttons
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* All buttons share this style */
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important; /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def main():
#     # Apply the custom style
#     set_button_style()

#     st.title("Modular Multi-Scraper App (Two Scrapers)")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     # We store these for the formatting helper => scraper input flow.
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""

#     # -------------------------------------------------
#     # 2) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have **raw URLs** (one per line) and want them in the form:
#     ```
#     "https://example.com",
#     "https://another-site.org",
#     "https://foo.bar"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="e.g.\nhttps://example.com\nhttps://another-site.org\n...",
#         height=150
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 if i < len(lines) - 1:
#                     formatted_lines.append(f"\"{line}\",")
#                 else:
#                     formatted_lines.append(f"\"{line}\"")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=150
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs pasted to the scraper input below.")

#     st.markdown("---")

#     # -------------------------------------------------
#     # 3) SCRAPER SECTION
#     # -------------------------------------------------
#     st.subheader("Scraper Input")
#     st.write("""
#     ### How to Use
#     1. Paste your URLs below (comma- or newline-separated, or the fully formatted form).
#     2. Enter or create an output folder path (for ephemeral storage).
#     3. Choose which scrapers to run.
#     4. Click "Start Scraping".
#     5. Download your scraped files before the session ends (if using a hosted service).
#     """)

#     # Text area for scraping input
#     urls_text = st.text_area("Paste URLs for Scraping:", height=200, key="scraper_input")

#     # Output folder
#     folder_path = st.text_input("Choose or create an output folder path:", "my_output")

#     st.markdown("### Select Scrapers")

#     # Single master checkbox: if True => run all scrapers, else show them individually
#     run_all = st.checkbox("Run ALL scrapers (default)", value=True)

#     # By default, if run_all is True => both scrapers selected
#     if run_all:
#         scraper_1_selected = True
#         scraper_2_selected = True
#     else:
#         # Show individual checkboxes
#         scraper_1_selected = st.checkbox("Scraper 1 (Placeholder: basic requests fetch)", value=False)
#         scraper_2_selected = st.checkbox("Scraper 2 (Placeholder: JS rendering w/ Selenium)", value=False)

#     # "Start Scraping" button
#     if st.button("Start Scraping"):
#         # Validate URL input
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URL text
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]

#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         # Ensure the base folder exists
#         os.makedirs(folder_path, exist_ok=True)

#         # We’ll run scrapers in sequence, collecting their results
#         if scraper_1_selected:
#             st.markdown("## Scraper 1 Results")
#             results_1 = run_scraper_1(urls, folder_path)
#             # Summaries
#             success_count = sum(r["status"] == "success" for r in results_1)
#             fail_count = sum(r["status"] == "failed" for r in results_1)
#             total_urls = len(urls)

#             st.success(
#                 f"Scraper 1 completed. "
#                 f"Successfully scraped {success_count} of {total_urls} URLs. "
#                 f"({fail_count} failed.)"
#             )

#             # Detailed logs in an expander
#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Create a ZIP for Scraper 1
#             zip_buffer_1 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_1, "w") as zf:
#                 for item in results_1:
#                     if item["status"] == "success" and item["filename"]:
#                         subfolder = "1_HTML_saved_webpages"
#                         file_path = os.path.join(folder_path, subfolder, item["filename"])
#                         zf.write(file_path, arcname=item["filename"])
#             zip_buffer_1.seek(0)

#             # Download button
#             st.download_button(
#                 label="Download Scraper 1 Files (ZIP)",
#                 data=zip_buffer_1.getvalue(),
#                 file_name="scraper_1_html_files.zip",
#                 mime="application/zip"
#             )

#         if scraper_2_selected:
#             st.markdown("## Scraper 2 Results")
#             results_2 = run_scraper_2(urls, folder_path)
#             # Summaries
#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             total_urls_2 = len(urls)

#             st.success(
#                 f"Scraper 2 completed. "
#                 f"Successfully scraped {success_count_2} of {total_urls_2} URLs. "
#                 f"({fail_count_2} failed.)"
#             )

#             # Detailed logs in an expander
#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Create a ZIP for Scraper 2
#             zip_buffer_2 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_2, "w") as zf:
#                 for item in results_2:
#                     if item["status"] == "success" and item["filename"]:
#                         subfolder = "2_Rendered_HTML_saved_webpages"
#                         file_path = os.path.join(folder_path, subfolder, item["filename"])
#                         zf.write(file_path, arcname=item["filename"])
#             zip_buffer_2.seek(0)

#             # Download button
#             st.download_button(
#                 label="Download Scraper 2 Files (ZIP)",
#                 data=zip_buffer_2.getvalue(),
#                 file_name="scraper_2_html_files.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()




















# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scrapers (now with progress bars)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # 1) Custom CSS to style Streamlit buttons
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* All buttons share this style */
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important; /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def main():
#     set_button_style()

#     st.title("Two-Scraper App with Progress Bars")

#     # -- URL Input
#     urls_text = st.text_area("Paste URLs here (comma- or newline-separated):", height=150)
#     folder_path = st.text_input("Output folder path:", "my_output")

#     st.markdown("### Select Scrapers")
#     run_all = st.checkbox("Run ALL scrapers (default)", value=True)

#     if run_all:
#         scraper_1_selected = True
#         scraper_2_selected = True
#     else:
#         scraper_1_selected = st.checkbox("Scraper 1", value=False)
#         scraper_2_selected = st.checkbox("Scraper 2", value=False)

#     if st.button("Start Scraping"):
#         # Basic validation
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse the URLs
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         os.makedirs(folder_path, exist_ok=True)

#         # Optional: Show a spinner over the entire process
#         with st.spinner("Scraping in progress... Please wait."):
#             # SCRAPER 1
#             if scraper_1_selected:
#                 st.markdown("## Scraper 1 Results")
#                 results_1 = run_scraper_1(urls, folder_path)

#                 # Summaries
#                 success_count_1 = sum(r["status"] == "success" for r in results_1)
#                 fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#                 total_1 = len(urls)
#                 st.success(
#                     f"Scraper 1 completed. Successfully scraped {success_count_1} of {total_1} URLs. "
#                     f"({fail_count_1} failed.)"
#                 )

#                 # Detailed logs in an expander
#                 with st.expander("Detailed Results (Scraper 1)"):
#                     for item in results_1:
#                         status_emoji = "✅" if item["status"] == "success" else "❌"
#                         error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                         st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#                 # ZIP creation
#                 zip_buffer_1 = BytesIO()
#                 with zipfile.ZipFile(zip_buffer_1, "w") as zf:
#                     for item in results_1:
#                         if item["status"] == "success" and item["filename"]:
#                             subfolder = "1_HTML_saved_webpages"
#                             file_path = os.path.join(folder_path, subfolder, item["filename"])
#                             zf.write(file_path, arcname=item["filename"])
#                 zip_buffer_1.seek(0)

#                 st.download_button(
#                     label="Download Scraper 1 Files (ZIP)",
#                     data=zip_buffer_1.getvalue(),
#                     file_name="scraper_1_html_files.zip",
#                     mime="application/zip"
#                 )

#             # SCRAPER 2
#             if scraper_2_selected:
#                 st.markdown("## Scraper 2 Results")
#                 results_2 = run_scraper_2(urls, folder_path)

#                 success_count_2 = sum(r["status"] == "success" for r in results_2)
#                 fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#                 total_2 = len(urls)
#                 st.success(
#                     f"Scraper 2 completed. Successfully scraped {success_count_2} of {total_2} URLs. "
#                     f"({fail_count_2} failed.)"
#                 )

#                 with st.expander("Detailed Results (Scraper 2)"):
#                     for item in results_2:
#                         status_emoji = "✅" if item["status"] == "success" else "❌"
#                         error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                         st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#                 # ZIP creation
#                 zip_buffer_2 = BytesIO()
#                 with zipfile.ZipFile(zip_buffer_2, "w") as zf:
#                     for item in results_2:
#                         if item["status"] == "success" and item["filename"]:
#                             subfolder = "2_Rendered_HTML_saved_webpages"
#                             file_path = os.path.join(folder_path, subfolder, item["filename"])
#                             zf.write(file_path, arcname=item["filename"])
#                 zip_buffer_2.seek(0)

#                 st.download_button(
#                     label="Download Scraper 2 Files (ZIP)",
#                     data=zip_buffer_2.getvalue(),
#                     file_name="scraper_2_html_files.zip",
#                     mime="application/zip"
#                 )

# if __name__ == "__main__":
#     main()







# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scrapers
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # Custom CSS for button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important;
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def reset_state():
#     """Clear all session state so we can re-run scrapers from scratch."""
#     st.session_state.scraper_1_results = None
#     st.session_state.scraper_2_results = None
#     st.session_state.scraping_in_progress = False
#     st.session_state.scraping_complete = False

# def main():
#     set_button_style()
#     st.title("Two-Scraper App with Persisted Results")

#     # -------------------------------------
#     # Initialize Session State
#     # -------------------------------------
#     if "scraper_1_results" not in st.session_state:
#         st.session_state.scraper_1_results = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state.scraper_2_results = None
#     if "scraping_in_progress" not in st.session_state:
#         st.session_state.scraping_in_progress = False
#     if "scraping_complete" not in st.session_state:
#         st.session_state.scraping_complete = False

#     # "Reset" button to clear all stored results
#     if st.button("Reset State"):
#         reset_state()
#         st.experimental_rerun()  # re-run the app so the UI updates

#     # -------------------------------------
#     # Input area for URLs
#     # -------------------------------------
#     urls_text = st.text_area(
#         "Paste URLs here (comma- or newline-separated):",
#         height=100,
#     )

#     folder_path = st.text_input(
#         "Output folder path (ephemeral on hosting):",
#         value="my_output"
#     )

#     # -------------------------------------
#     # Scraper selection
#     # -------------------------------------
#     st.markdown("### Select Scrapers")
#     run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#     if run_all:
#         scraper_1_selected = True
#         scraper_2_selected = True
#     else:
#         scraper_1_selected = st.checkbox("Scraper 1", value=False)
#         scraper_2_selected = st.checkbox("Scraper 2", value=False)

#     # -------------------------------------
#     # Start Scraping Logic
#     # -------------------------------------
#     if st.button("Start Scraping"):
#         if not urls_text.strip():
#             st.warning("Please provide at least one URL.")
#             return

#         # Parse
#         raw_urls = urls_text.replace("\n", ",").split(",")
#         urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#         if not urls:
#             st.warning("No valid URLs found.")
#             return

#         os.makedirs(folder_path, exist_ok=True)

#         # Mark that scraping has started
#         st.session_state.scraper_1_results = None
#         st.session_state.scraper_2_results = None
#         st.session_state.scraping_in_progress = True
#         st.session_state.scraping_complete = False

#         with st.spinner("Scraping in progress... please wait."):
#             # Run Scraper 1 if selected
#             if scraper_1_selected:
#                 results_1 = run_scraper_1(urls, folder_path)
#                 st.session_state.scraper_1_results = results_1

#             # Run Scraper 2 if selected
#             if scraper_2_selected:
#                 results_2 = run_scraper_2(urls, folder_path)
#                 st.session_state.scraper_2_results = results_2

#         st.session_state.scraping_in_progress = False
#         st.session_state.scraping_complete = True
#         st.success("All selected scrapers have finished.")
#         st.experimental_rerun()  # Force a re-run so we can display results below without re-scraping

#     # -------------------------------------
#     # Display Results if Complete
#     # -------------------------------------
#     if st.session_state.scraping_complete:
#         # Scraper 1 Results
#         if st.session_state.scraper_1_results is not None:
#             st.markdown("## Scraper 1 Results")
#             results_1 = st.session_state.scraper_1_results

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Create a ZIP for Scraper 1
#             zip_buffer_1 = BytesIO()
#             import zipfile
#             with zipfile.ZipFile(zip_buffer_1, "w") as zf:
#                 for item in results_1:
#                     if item["status"] == "success" and item["filename"]:
#                         subfolder = "1_HTML_saved_webpages"
#                         file_path = os.path.join(folder_path, subfolder, item["filename"])
#                         zf.write(file_path, arcname=item["filename"])
#             zip_buffer_1.seek(0)

#             st.download_button(
#                 label="Download Scraper 1 Files (ZIP)",
#                 data=zip_buffer_1.getvalue(),
#                 file_name="scraper_1_html_files.zip",
#                 mime="application/zip"
#             )

#         # Scraper 2 Results
#         if st.session_state.scraper_2_results is not None:
#             st.markdown("## Scraper 2 Results")
#             results_2 = st.session_state.scraper_2_results

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Create a ZIP for Scraper 2
#             zip_buffer_2 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_2, "w") as zf:
#                 for item in results_2:
#                     if item["status"] == "success" and item["filename"]:
#                         subfolder = "2_Rendered_HTML_saved_webpages"
#                         file_path = os.path.join(folder_path, subfolder, item["filename"])
#                         zf.write(file_path, arcname=item["filename"])
#             zip_buffer_2.seek(0)

#             st.download_button(
#                 label="Download Scraper 2 Files (ZIP)",
#                 data=zip_buffer_2.getvalue(),
#                 file_name="scraper_2_html_files.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()
















# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scrapers
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important;
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Helper to zip & download a scraper's results
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     set_button_style()
#     st.title("Two-Scraper App (Single-Run with Persistent Data)")

#     # Prepare session state for results
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # A simple reset button if you want to clear everything
#     if st.button("Reset All"):
#         st.session_state.scraper_1_results = None
#         st.session_state.scraper_2_results = None
#         st.session_state.scrapers_ran = False
#         st.experimental_rerun()

#     # If we have NOT run scrapers yet, show input UI
#     if not st.session_state.scrapers_ran:
#         # Input Area
#         urls_text = st.text_area("Paste URLs (comma / newline separated):", height=100)
#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2", value=False)

#         if st.button("Start Scraping"):
#             # Basic validation
#             if not urls_text.strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = urls_text.replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             # Run scrapers in a single pass
#             with st.spinner("Scraping in progress..."):
#                 if scraper_1_selected:
#                     st.session_state.scraper_1_results = run_scraper_1(urls, folder_path)
#                 if scraper_2_selected:
#                     st.session_state.scraper_2_results = run_scraper_2(urls, folder_path)

#             st.session_state.scrapers_ran = True
#             # After scraping, the code continues, no re-run needed.
#     else:
#         # We have already run scrapers: display results
#         folder_path = "my_output"  # or store it in session_state if you want
#         st.success("Scraping completed. See results below.")

#     # --------------------------------------------------
#     # Show results if we have them in session_state
#     # --------------------------------------------------
#     # Scraper 1
#     if st.session_state.scraper_1_results is not None:
#         results_1 = st.session_state.scraper_1_results
#         st.markdown("## Scraper 1 Results")

#         success_count_1 = sum(r["status"] == "success" for r in results_1)
#         fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#         st.success(
#             f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#             f"({fail_count_1} failed.)"
#         )

#         with st.expander("Detailed Results (Scraper 1)"):
#             for item in results_1:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#         create_zip_and_download(
#             results_1,
#             folder_path=folder_path,
#             subfolder_name="1_HTML_saved_webpages",
#             scraper_label="Scraper_1"
#         )

#     # Scraper 2
#     if st.session_state.scraper_2_results is not None:
#         results_2 = st.session_state.scraper_2_results
#         st.markdown("## Scraper 2 Results")

#         success_count_2 = sum(r["status"] == "success" for r in results_2)
#         fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#         st.success(
#             f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#             f"({fail_count_2} failed.)"
#         )

#         with st.expander("Detailed Results (Scraper 2)"):
#             for item in results_2:
#                 status_emoji = "✅" if item["status"] == "success" else "❌"
#                 error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                 st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#         create_zip_and_download(
#             results_2,
#             folder_path=folder_path,
#             subfolder_name="2_Rendered_HTML_saved_webpages",
#             scraper_label="Scraper_2"
#         )

# if __name__ == "__main__":
#     main()















# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scrapers (each has its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # Custom CSS for button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important;
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     set_button_style()
#     st.title("Two-Scraper App with URL Formatting and Persistent Results")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     # This prevents data loss on re-runs triggered by user actions (e.g., clicking download)
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # -------------------------------------------------
#     # 1) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org",
#     "https://site3.co"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     # A text area for unformatted raw URLs
#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     # We'll keep the formatted output in session state for convenience
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""

#     # Format button
#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # Display the formatted output if available
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs (you can paste these below):",
#             value=st.session_state["formatted_output"],
#             height=100
#         )

#     # -------------------------------------------------
#     # 2) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma-separated, newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     # We'll store the final input for scraping in session state, so the user can "Paste to Scraper"
#     # if we want. But let's keep it simple: just a single text area right now.
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # If we haven't run scrapers yet, show the main input UI
#     if not st.session_state["scrapers_ran"]:
#         # The user can choose to manually paste the formatted URLs
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2", value=False)

#         if st.button("Start Scraping"):
#             # Basic validation
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             # Parse URLs
#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # Run scrapers in a single pass
#                 if scraper_1_selected:
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)

#                 if scraper_2_selected:
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         # We have run scrapers. No need to show the input UI again.
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 3) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # If there's a known folder path you used, you can either store it in session_state
#         # or just assume the default.
#         folder_path = "my_output"  # Adjust if you want a different approach

#         # Scraper 1
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # Scraper 2
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

# if __name__ == "__main__":
#     main()








# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scrapers (each has its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # Custom CSS for button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button {
#             background-color: #003366 !important; /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
#         div.stButton > button:hover {
#             background-color: #002244 !important;
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     set_button_style()
#     st.title("Two-Scraper App with URL Formatting and Persistent Results")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # Keep the formatting output in session state so we can paste it directly
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""

#     # Keep the main scraper input in session state for convenience
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 1) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     # A text area for unformatted raw URLs
#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     # Format button
#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # Display the formatted output if available
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True  # just for display
#         )

#         # "Paste to Scraper" button
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 2) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma-separated, newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         # Show the main input UI if scrapers haven't run yet
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2", value=False)

#         if st.button("Start Scraping"):
#             # Basic validation
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             # Parse URLs
#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # Run scrapers in a single pass
#                 if scraper_1_selected:
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)

#                 if scraper_2_selected:
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         # If scrapers_ran is True, we hide the input UI
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 3) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # If there's a known folder path, you could store it in session_state if desired.
#         # For simplicity, let's assume "my_output".
#         folder_path = "my_output"

#         # Scraper 1
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # Scraper 2
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

# if __name__ == "__main__":
#     main()












# import streamlit as st
# import os
# from io import BytesIO
# import zipfile

# # Import your scrapers (each has its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # Custom CSS for button (and download button) styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* Apply dark-blue styling to both normal buttons and download buttons */
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # Apply the custom style
#     set_button_style()

#     st.title("Two-Scraper App with URL Formatting and Persistent Results")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # Keep the formatting output in session state so we can paste it directly
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""

#     # Keep the main scraper input in session state for convenience
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 1) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     # A text area for unformatted raw URLs
#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     # Format button
#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # Display the formatted output if available
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )

#         # "Paste to Scraper" button
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 2) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma-separated, newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         # Show the main input UI if scrapers haven't run yet
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2", value=False)

#         if st.button("Start Scraping"):
#             # Basic validation
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             # Parse URLs
#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # Run scrapers in a single pass
#                 if scraper_1_selected:
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)

#                 if scraper_2_selected:
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         # If scrapers_ran is True, we hide the input UI
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 3) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # If there's a known folder path, you could store it in session_state if desired.
#         # For simplicity, let's assume "my_output".
#         folder_path = "my_output"

#         # Scraper 1
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # Scraper 2
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)"
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

# if __name__ == "__main__":
#     main()




















# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers (each has its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2

# # -------------------------------------------------
# # Custom CSS for button (and download button) styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     set_button_style()

#     st.title("Two-Scraper App with URL Formatting, Persistent Results, and Time Taken")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # We'll store formatted output and scraper input as well
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 1) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 2) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma-separated, newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2", value=False)

#         if st.button("Start Scraping"):
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 ---
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 3) DISPLAY RESULTS
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # For simplicity, assume "my_output" is the folder
#         folder_path = "my_output"

#         # Scraper 1
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)  \n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # Scraper 2
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)  \n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

# if __name__ == "__main__":
#     main()
























# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers (each with its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2
# from scrapers.scraper_3 import run_scraper_3  # NEW Scraper 3 for PDF printing

# # -------------------------------------------------
# # 1) Custom CSS for button and download button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* Apply dark-blue styling to both normal buttons and download buttons */
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )


# # -------------------------------------------------
# # 3) Helper function to set colour
# # -------------------------------------------------
# def set_global_style():
#     st.markdown(
#         """
#         <style>
#         /* Target the checkbox container when checked */
#         [data-testid="stCheckbox"] > label div[role="checkbox"][aria-checked="true"] {
#             background-color: #00AA00 !important; /* Green background */
#             border-color: #00AA00 !important;      /* Remove the contrasting outline */
#         }
        
#         /* Make the check mark white (the SVG icon) */
#         [data-testid="stCheckbox"] > label div[role="checkbox"][aria-checked="true"] svg {
#             stroke: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )




# def main():
#     set_global_style()  # call it here, before creating any checkboxes
#     set_button_style()
#     st.title("Three-Scraper App with URL Formatting, Persistent Results, and Time Taken")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results for each scraper and a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     if "scraper_2_duration" not in st.session_state:
#         st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # Keep the formatting output and main scraper input in session state
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # If we have formatted output, display it and offer "Paste to Scraper"
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#             scraper_3_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF printing)", value=False)

#         if st.button("Start Scraping"):
#             # Validate
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 ---
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 ---
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # Assume "my_output" for folder, or store the chosen path in session state if desired.
#         folder_path = "my_output"

#         # -----------------------
#         # Scraper 1
#         # -----------------------
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # -----------------------
#         # Scraper 2
#         # -----------------------
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results (JS-rendered HTML)")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)\n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

#         # -----------------------
#         # Scraper 3
#         # -----------------------
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF printing)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF files
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()







# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers (each with its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2
# from scrapers.scraper_3 import run_scraper_3  # NEW Scraper 3 for PDF printing

# # -------------------------------------------------
# # 1) Custom CSS for buttons + checkboxes
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* Apply dark-blue styling to both normal buttons and download buttons */
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }

#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }

#         /* 
#            Change the checkbox background when checked.
#            In newer Streamlit versions, the checkbox uses [data-baseweb="checkbox"].
#            This rule forces a green background and white checkmark.
#         */
#         [data-baseweb="checkbox"] [aria-checked="true"] {
#             background-color: #00AA00 !important; /* Green background */
#             border-color: #00AA00 !important;     /* Matches background */
#         }
#         [data-baseweb="checkbox"] [aria-checked="true"] svg {
#             fill: white !important;   /* Tick mark */
#             stroke: white !important; /* Tick outline */
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # 1) Apply custom styles (buttons + checkboxes)
#     set_button_style()

#     st.title("Three-Scraper App with URL Formatting, Persistent Results, Time Taken, and Green Checkboxes")

#     # -------------------------------------------------
#     # Session State Setup
#     # -------------------------------------------------
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     if "scraper_2_duration" not in st.session_state:
#         st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#             scraper_3_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF printing)", value=False)

#         if st.button("Start Scraping"):
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 ---
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 ---
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # Assume "my_output" for folder, or store the chosen path in session state if desired.
#         folder_path = "my_output"

#         # Scraper 1
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # Scraper 2
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results (JS-rendered HTML)")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)\n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

#         # Scraper 3
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF printing)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF files
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()

























# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers (each with its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2
# from scrapers.scraper_3 import run_scraper_3
# from scrapers.scraper_4 import run_scraper_4  # NEW Scraper 4 for PDF_2 printing

# # -------------------------------------------------
# # 1) Custom CSS for button and download button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* Apply dark-blue styling to both normal buttons and download buttons */
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }

#         /* 
#            If you want to attempt green checkboxes in newer Streamlit versions:
#            [data-baseweb="checkbox"] [aria-checked="true"] {
#                background-color: #00AA00 !important;
#                border-color: #00AA00 !important;
#            }
#            [data-baseweb="checkbox"] [aria-checked="true"] svg {
#                fill: white !important;
#                stroke: white !important;
#            }
#         */
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # 1) Apply custom styles (buttons)
#     set_button_style()

#     st.title("Four-Scraper App with URL Formatting, Persistent Results, Time Taken")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results and durations for each scraper, plus a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None
#     if "scraper_4_results" not in st.session_state:
#         st.session_state["scraper_4_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     if "scraper_2_duration" not in st.session_state:
#         st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0
#     if "scraper_4_duration" not in st.session_state:
#         st.session_state["scraper_4_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # Keep the formatting output and main scraper input in session state
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # If we have formatted output, display it and offer "Paste to Scraper"
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#             scraper_3_selected = True
#             scraper_4_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF printing, Page.printToPDF)", value=False)
#             scraper_4_selected = st.checkbox("Scraper 4 (PDF_2 printing, print_page())", value=False)

#         if st.button("Start Scraping"):
#             # Validate
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 ---
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 ---
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#                 # --- Scraper 4 ---
#                 if scraper_4_selected:
#                     start_time_4 = time.time()
#                     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
#                     end_time_4 = time.time()
#                     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # Assume "my_output" for folder, or store the chosen path in session state if desired.
#         folder_path = "my_output"

#         # -------------- SCRAPER 1 --------------
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # -------------- SCRAPER 2 --------------
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results (JS-rendered HTML)")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)\n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

#         # -------------- SCRAPER 3 --------------
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF printing, Page.printToPDF)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF files
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

#         # -------------- SCRAPER 4 --------------
#         if st.session_state["scraper_4_results"] is not None:
#             results_4 = st.session_state["scraper_4_results"]
#             st.markdown("## Scraper 4 Results (PDF_2 printing, print_page())")

#             success_count_4 = sum(r["status"] == "success" for r in results_4)
#             fail_count_4 = sum(r["status"] == "failed" for r in results_4)
#             time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)

#             st.success(
#                 f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
#                 f"({fail_count_4} failed.)\n"
#                 f"**Time Taken**: {time_taken_4:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 4)"):
#                 for item in results_4:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF files (subfolder "4_PDF_2")
#             zip_buffer_4 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_4, "w") as zf:
#                 for item in results_4:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
#                         zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_4.seek(0)

#             st.download_button(
#                 label="Download Scraper_4 PDFs (ZIP)",
#                 data=zip_buffer_4.getvalue(),
#                 file_name="scraper_4_pdfs.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()














# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers (each with its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2
# from scrapers.scraper_3 import run_scraper_3
# from scrapers.scraper_4 import run_scraper_4  # NEW Scraper 4 for PDF_2 printing

# # -------------------------------------------------
# # 1) Custom CSS for button and download button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         /* Apply dark-blue styling to both normal buttons and download buttons */
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }

#         /* 
#            If you want to attempt green checkboxes in newer Streamlit versions:
#            [data-baseweb="checkbox"] [aria-checked="true"] {
#                background-color: #00AA00 !important;
#                border-color: #00AA00 !important;
#            }
#            [data-baseweb="checkbox"] [aria-checked="true"] svg {
#                fill: white !important;
#                stroke: white !important;
#            }
#         */
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # 1) Apply custom styles (buttons)
#     set_button_style()

#     st.title("Four-Scraper App with URL Formatting, Persistent Results, Time Taken")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results and durations for each scraper, plus a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None
#     if "scraper_4_results" not in st.session_state:
#         st.session_state["scraper_4_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     if "scraper_2_duration" not in st.session_state:
#         st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0
#     if "scraper_4_duration" not in st.session_state:
#         st.session_state["scraper_4_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     # Keep the formatting output and main scraper input in session state
#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     # If we have formatted output, display it and offer "Paste to Scraper"
#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#             scraper_3_selected = True
#             scraper_4_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF printing, Page.printToPDF)", value=False)
#             scraper_4_selected = st.checkbox("Scraper 4 (PDF_2 printing, print_page())", value=False)

#         if st.button("Start Scraping"):
#             # Validate
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 ---
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 ---
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#                 # --- Scraper 4 ---
#                 if scraper_4_selected:
#                     start_time_4 = time.time()
#                     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
#                     end_time_4 = time.time()
#                     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         # Assume "my_output" for folder, or store the chosen path in session state if desired.
#         folder_path = "my_output"

#         # -------------- SCRAPER 1 --------------
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # -------------- SCRAPER 2 --------------
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results (JS-rendered HTML)")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)\n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

#         # -------------- SCRAPER 3 --------------
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF printing, Page.printToPDF)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF files
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

#         # -------------- SCRAPER 4 --------------
#         if st.session_state["scraper_4_results"] is not None:
#             results_4 = st.session_state["scraper_4_results"]
#             st.markdown("## Scraper 4 Results (PDF_2 printing, print_page())")

#             success_count_4 = sum(r["status"] == "success" for r in results_4)
#             fail_count_4 = sum(r["status"] == "failed" for r in results_4)
#             time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)

#             st.success(
#                 f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
#                 f"({fail_count_4} failed.)\n"
#                 f"**Time Taken**: {time_taken_4:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 4)"):
#                 for item in results_4:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF files (subfolder "4_PDF_2")
#             zip_buffer_4 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_4, "w") as zf:
#                 for item in results_4:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
#                         zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_4.seek(0)

#             st.download_button(
#                 label="Download Scraper_4 PDFs (ZIP)",
#                 data=zip_buffer_4.getvalue(),
#                 file_name="scraper_4_pdfs.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()












# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers (each with its own progress bar)
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2
# from scrapers.scraper_3 import run_scraper_3
# from scrapers.scraper_4 import run_scraper_4
# from scrapers.scraper_5 import run_scraper_5  # NEW Scraper 5 (async crawler)

# # -------------------------------------------------
# # 1) Custom CSS for buttons/download buttons
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             # Each item might refer to an HTML file or other resource
#             if item["status"] == "success" and item["filename"]:
#                 # Because Scraper 5 might store multiple files, we just zip "page.html"?
#                 # Or we zip the entire folder if you prefer. For consistency, let's do page.html:
#                 # But note each URL in Scraper 5 has a sub-subfolder, so we adapt:
#                 url_sanitized = item["url"].replace("https://", "").replace("http://", "")
#                 url_sanitized = "".join([c if c.isalnum() or c=="_" else "_" for c in url_sanitized])
#                 # The saved HTML is always "page.html" in that subfolder:
#                 file_path = os.path.join(folder_path, subfolder_name, url_sanitized, "page.html")
                
#                 if os.path.exists(file_path):
#                     zf.write(file_path, arcname=f"{url_sanitized}_page.html")
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     set_button_style()

#     st.title("Five-Scraper App (Persistent Results, Time Taken, Async, etc.)")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results/durations for each scraper plus a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None
#     if "scraper_4_results" not in st.session_state:
#         st.session_state["scraper_4_results"] = None
#     if "scraper_5_results" not in st.session_state:
#         st.session_state["scraper_5_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     if "scraper_2_duration" not in st.session_state:
#         st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0
#     if "scraper_4_duration" not in st.session_state:
#         st.session_state["scraper_4_duration"] = 0.0
#     if "scraper_5_duration" not in st.session_state:
#         st.session_state["scraper_5_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#             scraper_3_selected = True
#             scraper_4_selected = True
#             scraper_5_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF, Page.printToPDF)", value=False)
#             scraper_4_selected = st.checkbox("Scraper 4 (PDF_2, print_page())", value=False)
#             scraper_5_selected = st.checkbox("Scraper 5 (Async crawler, aiohttp)", value=False)

#         if st.button("Start Scraping"):
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # Scraper 1
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # Scraper 2
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # Scraper 3
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#                 # Scraper 4
#                 if scraper_4_selected:
#                     start_time_4 = time.time()
#                     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
#                     end_time_4 = time.time()
#                     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

#                 # Scraper 5
#                 if scraper_5_selected:
#                     start_time_5 = time.time()
#                     st.session_state["scraper_5_results"] = run_scraper_5(urls, folder_path)
#                     end_time_5 = time.time()
#                     st.session_state["scraper_5_duration"] = end_time_5 - start_time_5

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         folder_path = "my_output"  # or store user-supplied path in session state if desired

#         # Scraper 1
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # Scraper 2
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results (JS-rendered HTML)")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)\n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

#         # Scraper 3
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF, Page.printToPDF)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download for PDF subfolder "3_PDF_1"
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

#         # Scraper 4
#         if st.session_state["scraper_4_results"] is not None:
#             results_4 = st.session_state["scraper_4_results"]
#             st.markdown("## Scraper 4 Results (PDF_2, print_page())")

#             success_count_4 = sum(r["status"] == "success" for r in results_4)
#             fail_count_4 = sum(r["status"] == "failed" for r in results_4)
#             time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)

#             st.success(
#                 f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
#                 f"({fail_count_4} failed.)\n"
#                 f"**Time Taken**: {time_taken_4:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 4)"):
#                 for item in results_4:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF subfolder "4_PDF_2"
#             zip_buffer_4 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_4, "w") as zf:
#                 for item in results_4:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_4.seek(0)

#             st.download_button(
#                 label="Download Scraper_4 PDFs (ZIP)",
#                 data=zip_buffer_4.getvalue(),
#                 file_name="scraper_4_pdfs.zip",
#                 mime="application/zip"
#             )

#         # Scraper 5
#         if st.session_state["scraper_5_results"] is not None:
#             results_5 = st.session_state["scraper_5_results"]
#             st.markdown("## Scraper 5 Results (Async crawler, aiohttp)")

#             success_count_5 = sum(r["status"] == "success" for r in results_5)
#             fail_count_5 = sum(r["status"] == "failed" for r in results_5)
#             time_taken_5 = st.session_state.get("scraper_5_duration", 0.0)

#             st.success(
#                 f"Scraper 5 completed. Successfully scraped {success_count_5} of {len(results_5)} URLs. "
#                 f"({fail_count_5} failed.)\n"
#                 f"**Time Taken**: {time_taken_5:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 5)"):
#                 for item in results_5:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # If you want a ZIP for the main "page.html" from each URL sub-subfolder:
#             create_zip_and_download(
#                 results_5,
#                 folder_path=folder_path,
#                 subfolder_name="5_crawl4ai_full",
#                 scraper_label="Scraper_5"
#             )

# if __name__ == "__main__":
#     main()





















# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers
# from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2
# from scrapers.scraper_3 import run_scraper_3
# from scrapers.scraper_4 import run_scraper_4
# from scrapers.scraper_5 import run_scraper_5
# from scrapers.scraper_6 import run_scraper_6  # NEW Scraper 6 (BeautifulSoup JSON)

# # -------------------------------------------------
# # 1) Custom CSS for button and download button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.

#     For scrapers that produce multiple files per URL or JSON files,
#     adapt as needed to gather those files or subfolders.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 if os.path.exists(file_path):
#                     # For JSON output, we simply zip the JSON file
#                     zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # 1) Apply custom styles (buttons, etc.)
#     set_button_style()

#     st.title("Bulk URL list site scraper (HTML, JSON, PDF)")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results/durations for each scraper plus a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     if "scraper_2_results" not in st.session_state:
#         st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None
#     if "scraper_4_results" not in st.session_state:
#         st.session_state["scraper_4_results"] = None
#     if "scraper_5_results" not in st.session_state:
#         st.session_state["scraper_5_results"] = None
#     if "scraper_6_results" not in st.session_state:
#         st.session_state["scraper_6_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     if "scraper_2_duration" not in st.session_state:
#         st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0
#     if "scraper_4_duration" not in st.session_state:
#         st.session_state["scraper_4_duration"] = 0.0
#     if "scraper_5_duration" not in st.session_state:
#         st.session_state["scraper_5_duration"] = 0.0
#     if "scraper_6_duration" not in st.session_state:
#         st.session_state["scraper_6_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             scraper_2_selected = True
#             scraper_3_selected = True
#             scraper_4_selected = True
#             scraper_5_selected = True
#             scraper_6_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF, Page.printToPDF)", value=False)
#             scraper_4_selected = st.checkbox("Scraper 4 (PDF_2, print_page)", value=False)
#             scraper_5_selected = st.checkbox("Scraper 5 (Async crawler, aiohttp)", value=False)
#             scraper_6_selected = st.checkbox("Scraper 6 (BeautifulSoup to JSON)", value=False)

#         if st.button("Start Scraping"):
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 ---
#                 if scraper_2_selected:
#                     start_time_2 = time.time()
#                     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                     end_time_2 = time.time()
#                     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 ---
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#                 # --- Scraper 4 ---
#                 if scraper_4_selected:
#                     start_time_4 = time.time()
#                     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
#                     end_time_4 = time.time()
#                     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

#                 # --- Scraper 5 ---
#                 if scraper_5_selected:
#                     start_time_5 = time.time()
#                     st.session_state["scraper_5_results"] = run_scraper_5(urls, folder_path)
#                     end_time_5 = time.time()
#                     st.session_state["scraper_5_duration"] = end_time_5 - start_time_5

#                 # --- Scraper 6 ---
#                 if scraper_6_selected:
#                     start_time_6 = time.time()
#                     st.session_state["scraper_6_results"] = run_scraper_6(urls, folder_path)
#                     end_time_6 = time.time()
#                     st.session_state["scraper_6_duration"] = end_time_6 - start_time_6

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         folder_path = "my_output"

#         # ---------------- SCRAPER 1 ----------------
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # ---------------- SCRAPER 2 ----------------
#         if st.session_state["scraper_2_results"] is not None:
#             results_2 = st.session_state["scraper_2_results"]
#             st.markdown("## Scraper 2 Results (JS-rendered HTML)")

#             success_count_2 = sum(r["status"] == "success" for r in results_2)
#             fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#             time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)

#             st.success(
#                 f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#                 f"({fail_count_2} failed.)\n"
#                 f"**Time Taken**: {time_taken_2:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 2)"):
#                 for item in results_2:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_2,
#                 folder_path=folder_path,
#                 subfolder_name="2_Rendered_HTML_saved_webpages",
#                 scraper_label="Scraper_2"
#             )

#         # ---------------- SCRAPER 3 ----------------
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF, Page.printToPDF)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download for PDF subfolder "3_PDF_1"
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

#         # ---------------- SCRAPER 4 ----------------
#         if st.session_state["scraper_4_results"] is not None:
#             results_4 = st.session_state["scraper_4_results"]
#             st.markdown("## Scraper 4 Results (PDF_2, print_page())")

#             success_count_4 = sum(r["status"] == "success" for r in results_4)
#             fail_count_4 = sum(r["status"] == "failed" for r in results_4)
#             time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)

#             st.success(
#                 f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
#                 f"({fail_count_4} failed.)\n"
#                 f"**Time Taken**: {time_taken_4:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 4)"):
#                 for item in results_4:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF subfolder "4_PDF_2"
#             zip_buffer_4 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_4, "w") as zf:
#                 for item in results_4:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_4.seek(0)

#             st.download_button(
#                 label="Download Scraper_4 PDFs (ZIP)",
#                 data=zip_buffer_4.getvalue(),
#                 file_name="scraper_4_pdfs.zip",
#                 mime="application/zip"
#             )

#         # ---------------- SCRAPER 5 ----------------
#         if st.session_state["scraper_5_results"] is not None:
#             results_5 = st.session_state["scraper_5_results"]
#             st.markdown("## Scraper 5 Results (Async crawler, aiohttp)")

#             success_count_5 = sum(r["status"] == "success" for r in results_5)
#             fail_count_5 = sum(r["status"] == "failed" for r in results_5)
#             time_taken_5 = st.session_state.get("scraper_5_duration", 0.0)

#             st.success(
#                 f"Scraper 5 completed. Successfully scraped {success_count_5} of {len(results_5)} URLs. "
#                 f"({fail_count_5} failed.)\n"
#                 f"**Time Taken**: {time_taken_5:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 5)"):
#                 for item in results_5:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_5,
#                 folder_path=folder_path,
#                 subfolder_name="5_crawl4ai_full",
#                 scraper_label="Scraper_5"
#             )

#         # ---------------- SCRAPER 6 ----------------
#         if st.session_state["scraper_6_results"] is not None:
#             results_6 = st.session_state["scraper_6_results"]
#             st.markdown("## Scraper 6 Results (BeautifulSoup to JSON)")

#             success_count_6 = sum(r["status"] == "success" for r in results_6)
#             fail_count_6 = sum(r["status"] == "failed" for r in results_6)
#             time_taken_6 = st.session_state.get("scraper_6_duration", 0.0)

#             st.success(
#                 f"Scraper 6 completed. Successfully scraped {success_count_6} of {len(results_6)} URLs. "
#                 f"({fail_count_6} failed.)\n"
#                 f"**Time Taken**: {time_taken_6:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 6)"):
#                 for item in results_6:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Zip up the JSON files from '6_BeautifulSoup_json'
#             zip_buffer_6 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_6, "w") as zf:
#                 for item in results_6:
#                     if item["status"] == "success" and item["filename"]:
#                         json_path = os.path.join(folder_path, "6_BeautifulSoup_json", item["filename"])
#                         if os.path.exists(json_path):
#                             zf.write(json_path, arcname=item["filename"])
#             zip_buffer_6.seek(0)

#             st.download_button(
#                 label="Download Scraper_6 JSON (ZIP)",
#                 data=zip_buffer_6.getvalue(),
#                 file_name="scraper_6_json.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()

































# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers
# from scrapers.scraper_1 import run_scraper_1
# # from scrapers.scraper_2 import run_scraper_2  # COMMENTED OUT to remove Scraper 2
# from scrapers.scraper_3 import run_scraper_3
# from scrapers.scraper_4 import run_scraper_4
# from scrapers.scraper_5 import run_scraper_5
# from scrapers.scraper_6 import run_scraper_6  # NEW Scraper 6 (BeautifulSoup JSON)

# # -------------------------------------------------
# # 1) Custom CSS for button and download button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.

#     For scrapers that produce multiple files per URL or JSON files,
#     adapt as needed to gather those files or subfolders.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 if os.path.exists(file_path):
#                     # For JSON output, we simply zip the JSON file
#                     zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # 1) Apply custom styles (buttons, etc.)
#     set_button_style()

#     st.title("Bulk URL list site scraper (HTML, JSON, PDF)")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results/durations for each scraper plus a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     # if "scraper_2_results" not in st.session_state:
#     #     st.session_state["scraper_2_results"] = None
#     if "scraper_3_results" not in st.session_state:
#         st.session_state["scraper_3_results"] = None
#     if "scraper_4_results" not in st.session_state:
#         st.session_state["scraper_4_results"] = None
#     if "scraper_5_results" not in st.session_state:
#         st.session_state["scraper_5_results"] = None
#     if "scraper_6_results" not in st.session_state:
#         st.session_state["scraper_6_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     # if "scraper_2_duration" not in st.session_state:
#     #     st.session_state["scraper_2_duration"] = 0.0
#     if "scraper_3_duration" not in st.session_state:
#         st.session_state["scraper_3_duration"] = 0.0
#     if "scraper_4_duration" not in st.session_state:
#         st.session_state["scraper_4_duration"] = 0.0
#     if "scraper_5_duration" not in st.session_state:
#         st.session_state["scraper_5_duration"] = 0.0
#     if "scraper_6_duration" not in st.session_state:
#         st.session_state["scraper_6_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             # scraper_2_selected = True  # COMMENTED OUT
#             scraper_3_selected = True
#             scraper_4_selected = True
#             scraper_5_selected = True
#             scraper_6_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             # scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)  # COMMENTED OUT
#             scraper_3_selected = st.checkbox("Scraper 3 (PDF, Page.printToPDF)", value=False)
#             scraper_4_selected = st.checkbox("Scraper 4 (PDF_2, print_page)", value=False)
#             scraper_5_selected = st.checkbox("Scraper 5 (Async crawler, aiohttp)", value=False)
#             scraper_6_selected = st.checkbox("Scraper 6 (BeautifulSoup to JSON)", value=False)

#         if st.button("Start Scraping"):
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 (COMMENTED OUT) ---
#                 # if scraper_2_selected:
#                 #     start_time_2 = time.time()
#                 #     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                 #     end_time_2 = time.time()
#                 #     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 ---
#                 if scraper_3_selected:
#                     start_time_3 = time.time()
#                     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                     end_time_3 = time.time()
#                     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#                 # --- Scraper 4 ---
#                 if scraper_4_selected:
#                     start_time_4 = time.time()
#                     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
#                     end_time_4 = time.time()
#                     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

#                 # --- Scraper 5 ---
#                 if scraper_5_selected:
#                     start_time_5 = time.time()
#                     st.session_state["scraper_5_results"] = run_scraper_5(urls, folder_path)
#                     end_time_5 = time.time()
#                     st.session_state["scraper_5_duration"] = end_time_5 - start_time_5

#                 # --- Scraper 6 ---
#                 if scraper_6_selected:
#                     start_time_6 = time.time()
#                     st.session_state["scraper_6_results"] = run_scraper_6(urls, folder_path)
#                     end_time_6 = time.time()
#                     st.session_state["scraper_6_duration"] = end_time_6 - start_time_6

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         folder_path = "my_output"

#         # ---------------- SCRAPER 1 ----------------
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # ---------------- SCRAPER 2 (COMMENTED OUT) ----------------
#         # if st.session_state["scraper_2_results"] is not None:
#         #     results_2 = st.session_state["scraper_2_results"]
#         #     st.markdown("## Scraper 2 Results (JS-rendered HTML)")
#         #
#         #     success_count_2 = sum(r["status"] == "success" for r in results_2)
#         #     fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#         #     time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)
#         #
#         #     st.success(
#         #         f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#         #         f"({fail_count_2} failed.)\n"
#         #         f'**Time Taken**: {time_taken_2:.2f} seconds.'
#         #     )
#         #
#         #     with st.expander("Detailed Results (Scraper 2)"):
#         #         for item in results_2:
#         #             status_emoji = "✅" if item["status"] == "success" else "❌"
#         #             error_text = f"**Error**: {item["error"]}' if item['error'] else ""
#         #             st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")
#         #
#         #     create_zip_and_download(
#         #         results_2,
#         #         folder_path=folder_path,
#         #         subfolder_name="2_Rendered_HTML_saved_webpages",
#         #         scraper_label="Scraper_2"
#         #     )

#         # ---------------- SCRAPER 3 ----------------
#         if st.session_state["scraper_3_results"] is not None:
#             results_3 = st.session_state["scraper_3_results"]
#             st.markdown("## Scraper 3 Results (PDF, Page.printToPDF)")

#             success_count_3 = sum(r["status"] == "success" for r in results_3)
#             fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#             time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)

#             st.success(
#                 f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#                 f"({fail_count_3} failed.)\n"
#                 f"**Time Taken**: {time_taken_3:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 3)"):
#                 for item in results_3:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download for PDF subfolder "3_PDF_1"
#             zip_buffer_3 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#                 for item in results_3:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_3.seek(0)

#             st.download_button(
#                 label="Download Scraper_3 PDFs (ZIP)",
#                 data=zip_buffer_3.getvalue(),
#                 file_name="scraper_3_pdfs.zip",
#                 mime="application/zip"
#             )

#         # ---------------- SCRAPER 4 ----------------
#         if st.session_state["scraper_4_results"] is not None:
#             results_4 = st.session_state["scraper_4_results"]
#             st.markdown("## Scraper 4 Results (PDF_2, print_page())")

#             success_count_4 = sum(r["status"] == "success" for r in results_4)
#             fail_count_4 = sum(r["status"] == "failed" for r in results_4)
#             time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)

#             st.success(
#                 f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
#                 f"({fail_count_4} failed.)\n"
#                 f"**Time Taken**: {time_taken_4:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 4)"):
#                 for item in results_4:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF subfolder "4_PDF_2"
#             zip_buffer_4 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_4, "w") as zf:
#                 for item in results_4:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_4.seek(0)

#             st.download_button(
#                 label="Download Scraper_4 PDFs (ZIP)",
#                 data=zip_buffer_4.getvalue(),
#                 file_name="scraper_4_pdfs.zip",
#                 mime="application/zip"
#             )

#         # ---------------- SCRAPER 5 ----------------
#         if st.session_state["scraper_5_results"] is not None:
#             results_5 = st.session_state["scraper_5_results"]
#             st.markdown("## Scraper 5 Results (Async crawler, aiohttp)")

#             success_count_5 = sum(r["status"] == "success" for r in results_5)
#             fail_count_5 = sum(r["status"] == "failed" for r in results_5)
#             time_taken_5 = st.session_state.get("scraper_5_duration", 0.0)

#             st.success(
#                 f"Scraper 5 completed. Successfully scraped {success_count_5} of {len(results_5)} URLs. "
#                 f"({fail_count_5} failed.)\n"
#                 f"**Time Taken**: {time_taken_5:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 5)"):
#                 for item in results_5:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_5,
#                 folder_path=folder_path,
#                 subfolder_name="5_crawl4ai_full",
#                 scraper_label="Scraper_5"
#             )

#         # ---------------- SCRAPER 6 ----------------
#         if st.session_state["scraper_6_results"] is not None:
#             results_6 = st.session_state["scraper_6_results"]
#             st.markdown("## Scraper 6 Results (BeautifulSoup to JSON)")

#             success_count_6 = sum(r["status"] == "success" for r in results_6)
#             fail_count_6 = sum(r["status"] == "failed" for r in results_6)
#             time_taken_6 = st.session_state.get("scraper_6_duration", 0.0)

#             st.success(
#                 f"Scraper 6 completed. Successfully scraped {success_count_6} of {len(results_6)} URLs. "
#                 f"({fail_count_6} failed.)\n"
#                 f"**Time Taken**: {time_taken_6:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 6)"):
#                 for item in results_6:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Zip up the JSON files from '6_BeautifulSoup_json'
#             zip_buffer_6 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_6, "w") as zf:
#                 for item in results_6:
#                     if item["status"] == "success" and item["filename"]:
#                         json_path = os.path.join(folder_path, "6_BeautifulSoup_json", item["filename"])
#                         if os.path.exists(json_path):
#                             zf.write(json_path, arcname=item["filename"])
#             zip_buffer_6.seek(0)

#             st.download_button(
#                 label="Download Scraper_6 JSON (ZIP)",
#                 data=zip_buffer_6.getvalue(),
#                 file_name="scraper_6_json.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()





















# import streamlit as st
# import os
# import time
# from io import BytesIO
# import zipfile

# # Import your scrapers
# from scrapers.scraper_1 import run_scraper_1
# # from scrapers.scraper_2 import run_scraper_2  # COMMENTED OUT Scraper 2
# # from scrapers.scraper_3 import run_scraper_3  # COMMENTED OUT Scraper 3
# from scrapers.scraper_4 import run_scraper_4
# from scrapers.scraper_5 import run_scraper_5
# from scrapers.scraper_6 import run_scraper_6  # BeautifulSoup JSON

# # -------------------------------------------------
# # 1) Custom CSS for button and download button styling
# # -------------------------------------------------
# def set_button_style():
#     st.markdown(
#         """
#         <style>
#         div.stButton > button,
#         div.stDownloadButton > button {
#             background-color: #003366 !important;  /* Dark Blue */
#             color: white !important;
#             border: none !important;
#             padding: 0.45rem 0.85rem !important;
#         }
        
#         div.stButton > button:hover,
#         div.stDownloadButton > button:hover {
#             background-color: #002244 !important;  /* Even darker on hover */
#             color: white !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------------------------------------
# # 2) Helper function to zip and provide download
# # -------------------------------------------------
# def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
#     """
#     Build a ZIP from the success items in `results`
#     and provide a download button in Streamlit.

#     For scrapers that produce multiple files per URL or JSON files,
#     adapt as needed to gather those files or subfolders.
#     """
#     zip_buffer = BytesIO()
#     with zipfile.ZipFile(zip_buffer, "w") as zf:
#         for item in results:
#             if item["status"] == "success" and item["filename"]:
#                 file_path = os.path.join(folder_path, subfolder_name, item["filename"])
#                 if os.path.exists(file_path):
#                     zf.write(file_path, arcname=item["filename"])
#     zip_buffer.seek(0)
#     st.download_button(
#         label=f"Download {scraper_label} Files (ZIP)",
#         data=zip_buffer.getvalue(),
#         file_name=f"{scraper_label}_files.zip",
#         mime="application/zip"
#     )

# def main():
#     # 1) Apply custom styles (buttons, etc.)
#     set_button_style()

#     st.title("Bulk URL list site scraper (HTML, JSON, PDF)")

#     # -------------------------------------------------
#     # 3) Session State Setup
#     # -------------------------------------------------
#     # We store results/durations for each scraper plus a flag if they've run
#     if "scraper_1_results" not in st.session_state:
#         st.session_state["scraper_1_results"] = None
#     # if "scraper_2_results" not in st.session_state:
#     #     st.session_state["scraper_2_results"] = None
#     # if "scraper_3_results" not in st.session_state:
#     #     st.session_state["scraper_3_results"] = None
#     if "scraper_4_results" not in st.session_state:
#         st.session_state["scraper_4_results"] = None
#     if "scraper_5_results" not in st.session_state:
#         st.session_state["scraper_5_results"] = None
#     if "scraper_6_results" not in st.session_state:
#         st.session_state["scraper_6_results"] = None

#     if "scraper_1_duration" not in st.session_state:
#         st.session_state["scraper_1_duration"] = 0.0
#     # if "scraper_2_duration" not in st.session_state:
#     #     st.session_state["scraper_2_duration"] = 0.0
#     # if "scraper_3_duration" not in st.session_state:
#     #     st.session_state["scraper_3_duration"] = 0.0
#     if "scraper_4_duration" not in st.session_state:
#         st.session_state["scraper_4_duration"] = 0.0
#     if "scraper_5_duration" not in st.session_state:
#         st.session_state["scraper_5_duration"] = 0.0
#     if "scraper_6_duration" not in st.session_state:
#         st.session_state["scraper_6_duration"] = 0.0

#     if "scrapers_ran" not in st.session_state:
#         st.session_state["scrapers_ran"] = False

#     if "formatted_output" not in st.session_state:
#         st.session_state["formatted_output"] = ""
#     if "scraper_input" not in st.session_state:
#         st.session_state["scraper_input"] = ""

#     # -------------------------------------------------
#     # 4) URL FORMATTING HELPER
#     # -------------------------------------------------
#     st.subheader("URL Formatting Helper")
#     st.write("""
#     If you have raw URLs (one per line) and want them in the form:
#     ```
#     "https://site1.com",
#     "https://site2.org"
#     ```
#     paste them below and click **Format URLs**.
#     """)

#     raw_input = st.text_area(
#         label="Paste raw URLs here (one per line):",
#         placeholder="https://example.com\nhttps://another-site.org\n...",
#         height=100
#     )

#     if st.button("Format URLs"):
#         lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
#         if lines:
#             formatted_lines = []
#             for i, line in enumerate(lines):
#                 comma = "," if i < len(lines) - 1 else ""
#                 formatted_lines.append(f"\"{line}\"{comma}")
#             st.session_state["formatted_output"] = "\n".join(formatted_lines)
#         else:
#             st.warning("No valid URLs were detected to format.")
#             st.session_state["formatted_output"] = ""

#     if st.session_state["formatted_output"]:
#         st.text_area(
#             label="Formatted URLs:",
#             value=st.session_state["formatted_output"],
#             height=100,
#             disabled=True
#         )
#         if st.button("Paste to Scraper"):
#             st.session_state["scraper_input"] = st.session_state["formatted_output"]
#             st.info("Formatted URLs have been pasted to the scraper input section below.")

#     # -------------------------------------------------
#     # 5) SCRAPER INPUT
#     # -------------------------------------------------
#     st.markdown("---")
#     st.subheader("Scraper Input")
#     st.write("""
#     Paste your URLs here (comma- or newline-separated, or fully formatted).
#     Choose your output folder and which scrapers to run.
#     """)

#     if not st.session_state["scrapers_ran"]:
#         st.text_area(
#             label="Paste URLs for Scraping:",
#             height=150,
#             key="scraper_input"
#         )

#         folder_path = st.text_input("Output folder path:", "my_output")

#         st.markdown("### Select Scrapers")
#         run_all = st.checkbox("Run ALL scrapers (default)", value=True)
#         if run_all:
#             scraper_1_selected = True
#             # scraper_2_selected = True  # COMMENTED OUT
#             # scraper_3_selected = True  # COMMENTED OUT
#             scraper_4_selected = True
#             scraper_5_selected = True
#             scraper_6_selected = True
#         else:
#             scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
#             # scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
#             # scraper_3_selected = st.checkbox("Scraper 3 (PDF, Page.printToPDF)", value=False)
#             scraper_4_selected = st.checkbox("Scraper 4 (PDF_2, print_page)", value=False)
#             scraper_5_selected = st.checkbox("Scraper 5 (Async crawler, aiohttp)", value=False)
#             scraper_6_selected = st.checkbox("Scraper 6 (BeautifulSoup to JSON)", value=False)

#         if st.button("Start Scraping"):
#             if not st.session_state["scraper_input"].strip():
#                 st.warning("Please provide at least one URL.")
#                 return

#             raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
#             urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
#             if not urls:
#                 st.warning("No valid URLs found.")
#                 return

#             os.makedirs(folder_path, exist_ok=True)

#             with st.spinner("Scraping in progress..."):
#                 # --- Scraper 1 ---
#                 if scraper_1_selected:
#                     start_time_1 = time.time()
#                     st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
#                     end_time_1 = time.time()
#                     st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

#                 # --- Scraper 2 (COMMENTED OUT) ---
#                 # if scraper_2_selected:
#                 #     start_time_2 = time.time()
#                 #     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
#                 #     end_time_2 = time.time()
#                 #     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

#                 # --- Scraper 3 (COMMENTED OUT) ---
#                 # if scraper_3_selected:
#                 #     start_time_3 = time.time()
#                 #     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
#                 #     end_time_3 = time.time()
#                 #     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

#                 # --- Scraper 4 ---
#                 if scraper_4_selected:
#                     start_time_4 = time.time()
#                     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
#                     end_time_4 = time.time()
#                     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

#                 # --- Scraper 5 ---
#                 if scraper_5_selected:
#                     start_time_5 = time.time()
#                     st.session_state["scraper_5_results"] = run_scraper_5(urls, folder_path)
#                     end_time_5 = time.time()
#                     st.session_state["scraper_5_duration"] = end_time_5 - start_time_5

#                 # --- Scraper 6 ---
#                 if scraper_6_selected:
#                     start_time_6 = time.time()
#                     st.session_state["scraper_6_results"] = run_scraper_6(urls, folder_path)
#                     end_time_6 = time.time()
#                     st.session_state["scraper_6_duration"] = end_time_6 - start_time_6

#             st.session_state["scrapers_ran"] = True
#             st.success("Scraping completed! Scroll down to see the results.")
#     else:
#         st.write("Scrapers have been run. Refresh the page if you need to start over.")

#     # -------------------------------------------------
#     # 6) DISPLAY RESULTS (if scrapers_ran)
#     # -------------------------------------------------
#     if st.session_state["scrapers_ran"]:
#         folder_path = "my_output"

#         # ---------------- SCRAPER 1 ----------------
#         if st.session_state["scraper_1_results"] is not None:
#             results_1 = st.session_state["scraper_1_results"]
#             st.markdown("## Scraper 1 Results (Requests)")

#             success_count_1 = sum(r["status"] == "success" for r in results_1)
#             fail_count_1 = sum(r["status"] == "failed" for r in results_1)
#             time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

#             st.success(
#                 f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
#                 f"({fail_count_1} failed.)\n"
#                 f"**Time Taken**: {time_taken_1:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 1)"):
#                 for item in results_1:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_1,
#                 folder_path=folder_path,
#                 subfolder_name="1_HTML_saved_webpages",
#                 scraper_label="Scraper_1"
#             )

#         # ---------------- SCRAPER 2 (COMMENTED OUT) ----------------
#         # if st.session_state["scraper_2_results"] is not None:
#         #     results_2 = st.session_state["scraper_2_results"]
#         #     st.markdown("## Scraper 2 Results (JS-rendered HTML)")
#         #
#         #     success_count_2 = sum(r["status"] == "success" for r in results_2)
#         #     fail_count_2 = sum(r["status"] == "failed" for r in results_2)
#         #     time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)
#         #
#         #     st.success(
#         #         f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
#         #         f"({fail_count_2} failed.)\n"
#         #         f"**Time Taken**: {time_taken_2:.2f} seconds."
#         #     )
#         #
#         #     with st.expander("Detailed Results (Scraper 2)"):
#         #         for item in results_2:
#         #             status_emoji = "✅" if item["status"] == "success" else "❌"
#         #             error_text = f"**Error**: {item['error']}" if item['error'] else ""
#         #             st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")
#         #
#         #     create_zip_and_download(
#         #         results_2,
#         #         folder_path=folder_path,
#         #         subfolder_name="2_Rendered_HTML_saved_webpages",
#         #         scraper_label="Scraper_2"
#         #     )

#         # ---------------- SCRAPER 3 (COMMENTED OUT) ----------------
#         # if st.session_state["scraper_3_results"] is not None:
#         #     results_3 = st.session_state["scraper_3_results"]
#         #     st.markdown("## Scraper 3 Results (PDF, Page.printToPDF)")
#         #
#         #     success_count_3 = sum(r["status"] == "success" for r in results_3)
#         #     fail_count_3 = sum(r["status"] == "failed" for r in results_3)
#         #     time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)
#         #
#         #     st.success(
#         #         f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
#         #         f"({fail_count_3} failed.)\n"
#         #         f"**Time Taken**: {time_taken_3:.2f} seconds."
#         #     )
#         #
#         #     with st.expander("Detailed Results (Scraper 3)"):
#         #         for item in results_3:
#         #             status_emoji = "✅" if item["status"] == "success" else "❌"
#         #             error_text = f"**Error**: {item['error']}" if item['error'] else ""
#         #             st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")
#         #
#         #     # ZIP Download for PDF subfolder "3_PDF_1"
#         #     zip_buffer_3 = BytesIO()
#         #     with zipfile.ZipFile(zip_buffer_3, "w") as zf:
#         #         for item in results_3:
#         #             if item["status"] == "success" and item["filename"]:
#         #                 pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
#         #                 if os.path.exists(pdf_path):
#         #                     zf.write(pdf_path, arcname=item["filename"])
#         #     zip_buffer_3.seek(0)
#         #
#         #     st.download_button(
#         #         label="Download Scraper_3 PDFs (ZIP)",
#         #         data=zip_buffer_3.getvalue(),
#         #         file_name="scraper_3_pdfs.zip",
#         #         mime="application/zip"
#         #     )

#         # ---------------- SCRAPER 4 ----------------
#         if st.session_state["scraper_4_results"] is not None:
#             results_4 = st.session_state["scraper_4_results"]
#             st.markdown("## Scraper 4 Results (PDF_2, print_page())")

#             success_count_4 = sum(r["status"] == "success" for r in results_4)
#             fail_count_4 = sum(r["status"] == "failed" for r in results_4)
#             time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)

#             st.success(
#                 f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
#                 f"({fail_count_4} failed.)\n"
#                 f"**Time Taken**: {time_taken_4:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 4)"):
#                 for item in results_4:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # ZIP Download of PDF subfolder "4_PDF_2"
#             zip_buffer_4 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_4, "w") as zf:
#                 for item in results_4:
#                     if item["status"] == "success" and item["filename"]:
#                         pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
#                         if os.path.exists(pdf_path):
#                             zf.write(pdf_path, arcname=item["filename"])
#             zip_buffer_4.seek(0)

#             st.download_button(
#                 label="Download Scraper_4 PDFs (ZIP)",
#                 data=zip_buffer_4.getvalue(),
#                 file_name="scraper_4_pdfs.zip",
#                 mime="application/zip"
#             )

#         # ---------------- SCRAPER 5 ----------------
#         if st.session_state["scraper_5_results"] is not None:
#             results_5 = st.session_state["scraper_5_results"]
#             st.markdown("## Scraper 5 Results (Async crawler, aiohttp)")

#             success_count_5 = sum(r["status"] == "success" for r in results_5)
#             fail_count_5 = sum(r["status"] == "failed" for r in results_5)
#             time_taken_5 = st.session_state.get("scraper_5_duration", 0.0)

#             st.success(
#                 f"Scraper 5 completed. Successfully scraped {success_count_5} of {len(results_5)} URLs. "
#                 f"({fail_count_5} failed.)\n"
#                 f"**Time Taken**: {time_taken_5:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 5)"):
#                 for item in results_5:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             create_zip_and_download(
#                 results_5,
#                 folder_path=folder_path,
#                 subfolder_name="5_crawl4ai_full",
#                 scraper_label="Scraper_5"
#             )

#         # ---------------- SCRAPER 6 ----------------
#         if st.session_state["scraper_6_results"] is not None:
#             results_6 = st.session_state["scraper_6_results"]
#             st.markdown("## Scraper 6 Results (BeautifulSoup to JSON)")

#             success_count_6 = sum(r["status"] == "success" for r in results_6)
#             fail_count_6 = sum(r["status"] == "failed" for r in results_6)
#             time_taken_6 = st.session_state.get("scraper_6_duration", 0.0)

#             st.success(
#                 f"Scraper 6 completed. Successfully scraped {success_count_6} of {len(results_6)} URLs. "
#                 f"({fail_count_6} failed.)\n"
#                 f"**Time Taken**: {time_taken_6:.2f} seconds."
#             )

#             with st.expander("Detailed Results (Scraper 6)"):
#                 for item in results_6:
#                     status_emoji = "✅" if item["status"] == "success" else "❌"
#                     error_text = f"**Error**: {item['error']}" if item['error'] else ""
#                     st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

#             # Zip up the JSON files from '6_BeautifulSoup_json'
#             zip_buffer_6 = BytesIO()
#             with zipfile.ZipFile(zip_buffer_6, "w") as zf:
#                 for item in results_6:
#                     if item["status"] == "success" and item["filename"]:
#                         json_path = os.path.join(folder_path, "6_BeautifulSoup_json", item["filename"])
#                         if os.path.exists(json_path):
#                             zf.write(json_path, arcname=item["filename"])
#             zip_buffer_6.seek(0)

#             st.download_button(
#                 label="Download Scraper_6 JSON (ZIP)",
#                 data=zip_buffer_6.getvalue(),
#                 file_name="scraper_6_json.zip",
#                 mime="application/zip"
#             )

# if __name__ == "__main__":
#     main()















import streamlit as st
import os
import time
from io import BytesIO
import zipfile

# Import your scrapers
from scrapers.scraper_1 import run_scraper_1
# from scrapers.scraper_2 import run_scraper_2  # COMMENTED OUT Scraper 2
# from scrapers.scraper_3 import run_scraper_3  # COMMENTED OUT Scraper 3
from scrapers.scraper_4 import run_scraper_4  # COMMENTED OUT Scraper 4
from scrapers.scraper_5 import run_scraper_5
from scrapers.scraper_6 import run_scraper_6  # BeautifulSoup JSON

# -------------------------------------------------
# 1) Custom CSS for button and download button styling
# -------------------------------------------------
def set_button_style():
    st.markdown(
        """
        <style>
        div.stButton > button,
        div.stDownloadButton > button {
            background-color: #003366 !important;  /* Dark Blue */
            color: white !important;
            border: none !important;
            padding: 0.45rem 0.85rem !important;
        }
        
        div.stButton > button:hover,
        div.stDownloadButton > button:hover {
            background-color: #002244 !important;  /* Even darker on hover */
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# 2) Helper function to zip and provide download
# -------------------------------------------------
def create_zip_and_download(results, folder_path, subfolder_name, scraper_label):
    """
    Build a ZIP from the success items in `results`
    and provide a download button in Streamlit.

    For scrapers that produce multiple files per URL or JSON files,
    adapt as needed to gather those files or subfolders.
    """
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        for item in results:
            if item["status"] == "success" and item["filename"]:
                file_path = os.path.join(folder_path, subfolder_name, item["filename"])
                if os.path.exists(file_path):
                    zf.write(file_path, arcname=item["filename"])
    zip_buffer.seek(0)
    st.download_button(
        label=f"Download {scraper_label} Files (ZIP)",
        data=zip_buffer.getvalue(),
        file_name=f"{scraper_label}_files.zip",
        mime="application/zip"
    )

def main():
    # 1) Apply custom styles (buttons, etc.)
    set_button_style()

    st.title("Bulk URL list site scraper (HTML, JSON, PDF)")

    # -------------------------------------------------
    # 3) Session State Setup
    # -------------------------------------------------
    # We store results/durations for each scraper plus a flag if they've run
    if "scraper_1_results" not in st.session_state:
        st.session_state["scraper_1_results"] = None
    # if "scraper_2_results" not in st.session_state:
    #     st.session_state["scraper_2_results"] = None
    # if "scraper_3_results" not in st.session_state:
    #     st.session_state["scraper_3_results"] = None
    if "scraper_4_results" not in st.session_state:
        st.session_state["scraper_4_results"] = None
    if "scraper_5_results" not in st.session_state:
        st.session_state["scraper_5_results"] = None
    if "scraper_6_results" not in st.session_state:
        st.session_state["scraper_6_results"] = None

    if "scraper_1_duration" not in st.session_state:
        st.session_state["scraper_1_duration"] = 0.0
    # if "scraper_2_duration" not in st.session_state:
    #     st.session_state["scraper_2_duration"] = 0.0
    # if "scraper_3_duration" not in st.session_state:
    #     st.session_state["scraper_3_duration"] = 0.0
    if "scraper_4_duration" not in st.session_state:
        st.session_state["scraper_4_duration"] = 0.0
    if "scraper_5_duration" not in st.session_state:
        st.session_state["scraper_5_duration"] = 0.0
    if "scraper_6_duration" not in st.session_state:
        st.session_state["scraper_6_duration"] = 0.0

    if "scrapers_ran" not in st.session_state:
        st.session_state["scrapers_ran"] = False

    if "formatted_output" not in st.session_state:
        st.session_state["formatted_output"] = ""
    if "scraper_input" not in st.session_state:
        st.session_state["scraper_input"] = ""

    # -------------------------------------------------
    # 4) URL FORMATTING HELPER
    # -------------------------------------------------
    st.subheader("URL Formatting Helper")
    st.write("""
    If you have raw URLs (one per line) and want them in the form:
    ```
    "https://site1.com",
    "https://site2.org"
    ```
    paste them below and click **Format URLs**.
    """)

    raw_input = st.text_area(
        label="Paste raw URLs here (one per line):",
        placeholder="https://example.com\nhttps://another-site.org\n...",
        height=100
    )

    if st.button("Format URLs"):
        lines = [line.strip() for line in raw_input.strip().split("\n") if line.strip()]
        if lines:
            formatted_lines = []
            for i, line in enumerate(lines):
                comma = "," if i < len(lines) - 1 else ""
                formatted_lines.append(f"\"{line}\"{comma}")
            st.session_state["formatted_output"] = "\n".join(formatted_lines)
        else:
            st.warning("No valid URLs were detected to format.")
            st.session_state["formatted_output"] = ""

    if st.session_state["formatted_output"]:
        st.text_area(
            label="Formatted URLs:",
            value=st.session_state["formatted_output"],
            height=100,
            disabled=True
        )
        if st.button("Paste to Scraper"):
            st.session_state["scraper_input"] = st.session_state["formatted_output"]
            st.info("Formatted URLs have been pasted to the scraper input section below.")

    # -------------------------------------------------
    # 5) SCRAPER INPUT
    # -------------------------------------------------
    st.markdown("---")
    st.subheader("Scraper Input")
    st.write("""
    Paste your URLs here (comma- or newline-separated, or fully formatted).
    Choose your output folder and which scrapers to run.
    """)

    if not st.session_state["scrapers_ran"]:
        st.text_area(
            label="Paste URLs for Scraping:",
            height=150,
            key="scraper_input"
        )

        folder_path = st.text_input("Output folder path:", "my_output")

        st.markdown("### Select Scrapers")
        run_all = st.checkbox("Run ALL scrapers (default)", value=True)
        if run_all:
            scraper_1_selected = True
            # scraper_2_selected = True
            # scraper_3_selected = True
            # scraper_4_selected = True
            scraper_5_selected = True
            scraper_6_selected = True
        else:
            scraper_1_selected = st.checkbox("Scraper 1 (Requests-based)", value=False)
            # scraper_2_selected = st.checkbox("Scraper 2 (JS-rendered HTML)", value=False)
            # scraper_3_selected = st.checkbox("Scraper 3 (PDF, Page.printToPDF)", value=False)
            # scraper_4_selected = st.checkbox("Scraper 4 (PDF_2, print_page)", value=False)
            scraper_5_selected = st.checkbox("Scraper 5 (Async crawler, aiohttp)", value=False)
            scraper_6_selected = st.checkbox("Scraper 6 (BeautifulSoup to JSON)", value=False)

        if st.button("Start Scraping"):
            if not st.session_state["scraper_input"].strip():
                st.warning("Please provide at least one URL.")
                return

            raw_urls = st.session_state["scraper_input"].replace("\n", ",").split(",")
            urls = [u.strip().strip('"').strip("'") for u in raw_urls if u.strip()]
            if not urls:
                st.warning("No valid URLs found.")
                return

            os.makedirs(folder_path, exist_ok=True)

            with st.spinner("Scraping in progress..."):
                # --- Scraper 1 ---
                if scraper_1_selected:
                    start_time_1 = time.time()
                    st.session_state["scraper_1_results"] = run_scraper_1(urls, folder_path)
                    end_time_1 = time.time()
                    st.session_state["scraper_1_duration"] = end_time_1 - start_time_1

                # --- Scraper 2 (COMMENTED OUT) ---
                # if scraper_2_selected:
                #     start_time_2 = time.time()
                #     st.session_state["scraper_2_results"] = run_scraper_2(urls, folder_path)
                #     end_time_2 = time.time()
                #     st.session_state["scraper_2_duration"] = end_time_2 - start_time_2

                # --- Scraper 3 (COMMENTED OUT) ---
                # if scraper_3_selected:
                #     start_time_3 = time.time()
                #     st.session_state["scraper_3_results"] = run_scraper_3(urls, folder_path)
                #     end_time_3 = time.time()
                #     st.session_state["scraper_3_duration"] = end_time_3 - start_time_3

                # --- Scraper 4 (COMMENTED OUT) ---
                # if scraper_4_selected:
                #     start_time_4 = time.time()
                #     st.session_state["scraper_4_results"] = run_scraper_4(urls, folder_path)
                #     end_time_4 = time.time()
                #     st.session_state["scraper_4_duration"] = end_time_4 - start_time_4

                # --- Scraper 5 ---
                if scraper_5_selected:
                    start_time_5 = time.time()
                    st.session_state["scraper_5_results"] = run_scraper_5(urls, folder_path)
                    end_time_5 = time.time()
                    st.session_state["scraper_5_duration"] = end_time_5 - start_time_5

                # --- Scraper 6 ---
                if scraper_6_selected:
                    start_time_6 = time.time()
                    st.session_state["scraper_6_results"] = run_scraper_6(urls, folder_path)
                    end_time_6 = time.time()
                    st.session_state["scraper_6_duration"] = end_time_6 - start_time_6

            st.session_state["scrapers_ran"] = True
            st.success("Scraping completed! Scroll down to see the results.")
    else:
        st.write("Scrapers have been run. Refresh the page if you need to start over.")

    # -------------------------------------------------
    # 6) DISPLAY RESULTS (if scrapers_ran)
    # -------------------------------------------------
    if st.session_state["scrapers_ran"]:
        folder_path = "my_output"

        # ---------------- SCRAPER 1 ----------------
        if st.session_state["scraper_1_results"] is not None:
            results_1 = st.session_state["scraper_1_results"]
            st.markdown("## Scraper 1 Results (Requests)")

            success_count_1 = sum(r["status"] == "success" for r in results_1)
            fail_count_1 = sum(r["status"] == "failed" for r in results_1)
            time_taken_1 = st.session_state.get("scraper_1_duration", 0.0)

            st.success(
                f"Scraper 1 completed. Successfully scraped {success_count_1} of {len(results_1)} URLs. "
                f"({fail_count_1} failed.)\n"
                f"**Time Taken**: {time_taken_1:.2f} seconds."
            )

            with st.expander("Detailed Results (Scraper 1)"):
                for item in results_1:
                    status_emoji = "✅" if item["status"] == "success" else "❌"
                    error_text = f"**Error**: {item['error']}" if item['error'] else ""
                    st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

            create_zip_and_download(
                results_1,
                folder_path=folder_path,
                subfolder_name="1_HTML_saved_webpages",
                scraper_label="Scraper_1"
            )

        # ---------------- SCRAPER 2 (COMMENTED OUT) ----------------
        # if st.session_state["scraper_2_results"] is not None:
        #     results_2 = st.session_state["scraper_2_results"]
        #     st.markdown("## Scraper 2 Results (JS-rendered HTML)")
        #
        #     success_count_2 = sum(r["status"] == "success" for r in results_2)
        #     fail_count_2 = sum(r["status"] == "failed" for r in results_2)
        #     time_taken_2 = st.session_state.get("scraper_2_duration", 0.0)
        #
        #     st.success(
        #         f"Scraper 2 completed. Successfully scraped {success_count_2} of {len(results_2)} URLs. "
        #         f"({fail_count_2} failed.)\n"
        #         f"**Time Taken**: {time_taken_2:.2f} seconds."
        #     )
        #
        #     with st.expander("Detailed Results (Scraper 2)"):
        #         for item in results_2:
        #             status_emoji = "✅" if item["status"] == "success" else "❌"
        #             error_text = f"**Error**: {item['error']}" if item['error'] else ""
        #             st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")
        #
        #     create_zip_and_download(
        #         results_2,
        #         folder_path=folder_path,
        #         subfolder_name="2_Rendered_HTML_saved_webpages",
        #         scraper_label="Scraper_2"
        #     )

        # ---------------- SCRAPER 3 (COMMENTED OUT) ----------------
        # if st.session_state["scraper_3_results"] is not None:
        #     results_3 = st.session_state["scraper_3_results"]
        #     st.markdown("## Scraper 3 Results (PDF, Page.printToPDF)")
        #
        #     success_count_3 = sum(r["status"] == "success" for r in results_3)
        #     fail_count_3 = sum(r["status"] == "failed" for r in results_3)
        #     time_taken_3 = st.session_state.get("scraper_3_duration", 0.0)
        #
        #     st.success(
        #         f"Scraper 3 completed. Successfully scraped {success_count_3} of {len(results_3)} URLs. "
        #         f"({fail_count_3} failed.)\n"
        #         f"**Time Taken**: {time_taken_3:.2f} seconds."
        #     )
        #
        #     with st.expander("Detailed Results (Scraper 3)"):
        #         for item in results_3:
        #             status_emoji = "✅" if item["status"] == "success" else "❌"
        #             error_text = f"**Error**: {item['error']}" if item['error'] else ""
        #             st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")
        #
        #     # ZIP Download for PDF subfolder "3_PDF_1"
        #     zip_buffer_3 = BytesIO()
        #     with zipfile.ZipFile(zip_buffer_3, "w") as zf:
        #         for item in results_3:
        #             if item["status"] == "success" and item["filename"]:
        #                 pdf_path = os.path.join(folder_path, "3_PDF_1", item["filename"])
        #                 if os.path.exists(pdf_path):
        #                     zf.write(pdf_path, arcname=item["filename"])
        #     zip_buffer_3.seek(0)
        #
        #     st.download_button(
        #         label="Download Scraper_3 PDFs (ZIP)",
        #         data=zip_buffer_3.getvalue(),
        #         file_name="scraper_3_pdfs.zip",
        #         mime="application/zip"
        #     )

        # ---------------- SCRAPER 4 (COMMENTED OUT) ----------------
        if st.session_state["scraper_4_results"] is not None:
            results_4 = st.session_state["scraper_4_results"]
            st.markdown("## Scraper 4 Results (PDF_2, print_page())")
        
            success_count_4 = sum(r["status"] == "success" for r in results_4)
            fail_count_4 = sum(r["status"] == "failed" for r in results_4)
            time_taken_4 = st.session_state.get("scraper_4_duration", 0.0)
        
            st.success(
                f"Scraper 4 completed. Successfully scraped {success_count_4} of {len(results_4)} URLs. "
                f"({fail_count_4} failed.)\n"
                f"**Time Taken**: {time_taken_4:.2f} seconds."
            )
        
            with st.expander("Detailed Results (Scraper 4)"):
                for item in results_4:
                    status_emoji = "✅" if item["status"] == "success" else "❌"
                    error_text = f"**Error**: {item['error']}" if item['error'] else ""
                    st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")
        
            # ZIP Download of PDF subfolder "4_PDF_2"
            zip_buffer_4 = BytesIO()
            with zipfile.ZipFile(zip_buffer_4, "w") as zf:
                for item in results_4:
                    if item["status"] == "success" and item["filename"]:
                        pdf_path = os.path.join(folder_path, "4_PDF_2", item["filename"])
                        if os.path.exists(pdf_path):
                            zf.write(pdf_path, arcname=item["filename"])
            zip_buffer_4.seek(0)
        
            st.download_button(
                label="Download Scraper_4 PDFs (ZIP)",
                data=zip_buffer_4.getvalue(),
                file_name="scraper_4_pdfs.zip",
                mime="application/zip"
            )

        # ---------------- SCRAPER 5 ----------------
        if st.session_state["scraper_5_results"] is not None:
            results_5 = st.session_state["scraper_5_results"]
            st.markdown("## Scraper 5 Results (Async crawler, aiohttp)")

            success_count_5 = sum(r["status"] == "success" for r in results_5)
            fail_count_5 = sum(r["status"] == "failed" for r in results_5)
            time_taken_5 = st.session_state.get("scraper_5_duration", 0.0)

            st.success(
                f"Scraper 5 completed. Successfully scraped {success_count_5} of {len(results_5)} URLs. "
                f"({fail_count_5} failed.)\n"
                f"**Time Taken**: {time_taken_5:.2f} seconds."
            )

            with st.expander("Detailed Results (Scraper 5)"):
                for item in results_5:
                    status_emoji = "✅" if item["status"] == "success" else "❌"
                    error_text = f"**Error**: {item['error']}" if item['error'] else ""
                    st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

            create_zip_and_download(
                results_5,
                folder_path=folder_path,
                subfolder_name="5_crawl4ai_full",
                scraper_label="Scraper_5"
            )

        # ---------------- SCRAPER 6 ----------------
        if st.session_state["scraper_6_results"] is not None:
            results_6 = st.session_state["scraper_6_results"]
            st.markdown("## Scraper 6 Results (BeautifulSoup to JSON)")

            success_count_6 = sum(r["status"] == "success" for r in results_6)
            fail_count_6 = sum(r["status"] == "failed" for r in results_6)
            time_taken_6 = st.session_state.get("scraper_6_duration", 0.0)

            st.success(
                f"Scraper 6 completed. Successfully scraped {success_count_6} of {len(results_6)} URLs. "
                f"({fail_count_6} failed.)\n"
                f"**Time Taken**: {time_taken_6:.2f} seconds."
            )

            with st.expander("Detailed Results (Scraper 6)"):
                for item in results_6:
                    status_emoji = "✅" if item["status"] == "success" else "❌"
                    error_text = f"**Error**: {item['error']}" if item['error'] else ""
                    st.write(f"{status_emoji} {item['url']} -> {item['filename'] or 'No file'} {error_text}")

            # Zip up the JSON files from '6_BeautifulSoup_json'
            zip_buffer_6 = BytesIO()
            with zipfile.ZipFile(zip_buffer_6, "w") as zf:
                for item in results_6:
                    if item["status"] == "success" and item["filename"]:
                        json_path = os.path.join(folder_path, "6_BeautifulSoup_json", item["filename"])
                        if os.path.exists(json_path):
                            zf.write(json_path, arcname=item["filename"])
            zip_buffer_6.seek(0)

            st.download_button(
                label="Download Scraper_6 JSON (ZIP)",
                data=zip_buffer_6.getvalue(),
                file_name="scraper_6_json.zip",
                mime="application/zip"
            )

if __name__ == "__main__":
    main()




















