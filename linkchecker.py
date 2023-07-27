import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter, Retry
  
url = "https://www.amazon.com/nothing_here"

s = requests.Session()

retries = Retry(total=3,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])

s.mount('http://', HTTPAdapter(max_retries=retries))
  
def _validate_url(url):
    try:
        s.get(url, timeout=1)
    except:
        not_found_links.append(url)


with open("index.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')

	# Create a list containing all links with the root domain.
links = [link.get("href") for link in soup.find_all("a")]
	# Initialize list for broken links.
not_found_links = []

for link in links:
    _validate_url(link)

with open("links.txt", "w") as txt_file:
    for line in not_found_links:
        txt_file.write(line + "\n")

