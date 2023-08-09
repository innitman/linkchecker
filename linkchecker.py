import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter, Retry
import os

s = requests.Session()

retries = Retry(total=2,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])

s.mount('http://', HTTPAdapter(max_retries=retries))

not_found_links = []
all_files_in_directory = os.getcwd()
html_files = []

for filename in os.listdir(all_files_in_directory):
    if filename.endswith('.html') or filename.endswith('.htm'):
        html_files.append(filename)

def _validate_url(url, filename):
    try:
        s.get(url, timeout=1)
    except:
        not_found_links.append("In file: " + filename + " the broken link is: " + url) 

def check_broken_links_in_given_html(html):
    with open(html) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    links = [link.get("href") for link in soup.find_all("a")]
    for link in links:
        _validate_url(link, html)

for file_to_test in html_files:
    check_broken_links_in_given_html(file_to_test)

def write_to_file():
    with open("links.txt", "w") as txt_file:
        txt_file.write("Links with issues \n\n")
        for line in not_found_links:
            txt_file.write(line + "\n")

write_to_file()