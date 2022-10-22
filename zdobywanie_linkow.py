import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import time

urls = [
'http://www.aliortfi.com/',
'http://www.amundi.pl/',
'http://www.baltictfi.pl/',
'http://www.tfi.bnpparibas.pl/',
'http://www.bpstfi.pl/',
'http://www.caspartfi.pl/',
'http://www.eitfi.pl/',
'http://www.esaliens.pl/',
'http://www.generali-investments.pl/',
'http://www.investors.pl/',
'http://www.ipopema.pl/',
'http://www.millenniumtfi.pl/',
'http://www.metlife.pl/',
'http://www.nntfi.pl/',
'http://www.noblefunds.pl/',
'http://www.opera-tfi.pl/',
'http://www.pekaotfi.pl/',
'http://www.pfrtfi.pl/',
'http://www.pkotfi.pl/',
'http://www.qtfi.pl/',
'http://www.rockbridge.pl/',
'http://www.santandertfi.pl/',
'http://www.skarbiec.pl/',
'http://www.superfund.pl/',
'http://www.franklintempleton.pl/',
'http://www.tfiagro.pl/',
'http://www.allianz.pl/',
'http://www.tfienergia.pl/',
'http://www.pzu.pl/',
'http://www.uniqa.pl/',
'http://www.vigcq-tfi.pl/'
]

url = ""
dict_href_links = {}


def getdata(url):
    r = requests.get(url)
    return r.text


def get_links(website_link):
    html_data = getdata(website_link)
    soup = BeautifulSoup(html_data, "html.parser")
    list_links = []
    for link in soup.find_all("a", href=True):

        # Append to list if new link contains original link
        if str(link["href"]).startswith((str(website_link))):
            list_links.append(link["href"])

        # Include all href that do not start with website link but with "/"
        if str(link["href"]).startswith("/"):
            if link["href"] not in dict_href_links:
                print(link["href"])
                dict_href_links[link["href"]] = None
                link_with_www = website_link + link["href"][1:]
                print("adjusted link =", link_with_www)
                list_links.append(link_with_www)

    # Convert list of links to dictionary and define keys as the links and the values as "Not-checked"
    dict_links = dict.fromkeys(list_links, "Not-checked")
    return dict_links


def get_subpage_links(l):
    noww = time.perf_counter()
    for link in tqdm(l):
        if(time.perf_counter()-noww>45):
            print("\n\n\n zwracane jest bq\n\n\n")
            return l
        print("link: " + link)
        # If not crawled through this page start crawling and get links
        if l[link] == "Not-checked":
            dict_links_subpages = get_links(link)
            # Change the dictionary value of the link to "Checked"
            l[link] = "Checked"
        else:
            # Create an empty dictionary in case every link is checked
            dict_links_subpages = {}
        # Add new dictionary to old dictionary
        l = {**dict_links_subpages, **l}
    return l

gigalista = {}
for url in urls:
    # If there is no such folder, the script will create one automatically

    if not os.path.exists("download"):
        os.mkdir("download")

    folder_location = r"download/" + url[7:17:1]
    if not os.path.exists(folder_location): os.mkdir(folder_location)

    dict_href_links = get_links(url)
    # add websuite WITH slash on end
    website = url
    # create dictionary of website
    dict_links = {website: "Not-checked"}

    counter, counter2 = None, 0
    start = time.perf_counter()
    while counter != 0:
        counter2 += 1
        dict_links2 = get_subpage_links(dict_links)
        # Count number of non-values and set counter to 0 if there are no values within the dictionary equal to the string "Not-checked"
        # https://stackoverflow.com/questions/48371856/count-the-number-of-occurrences-of-a-certain-value-in-a-dictionary-in-python
        counter = sum(value == "Not-checked" for value in dict_links2.values())
        # Print some statements
        print("")
        print("THIS IS LOOP ITERATION NUMBER", counter2)
        print("LENGTH OF DICTIONARY WITH LINKS =", len(dict_links2))
        print("NUMBER OF 'Not-checked' LINKS = ", counter)
        print("")
        dict_links = dict_links2
        # Save list in json file

        now = time.perf_counter()
        if (now - start > 300):
            print("\n\n\n wywalane jest\n\n\n")
            break

    gigalista = gigalista | dict_links

a_file = open("data.json", "a")
json.dump(gigalista, a_file)
a_file.close()
