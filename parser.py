import urllib
import urllib.request
import asyncio
import random

number = random.randint(1, 129200)

url = "https://amthauer-ist.com/graph.php?id="
path_to_file = "./images/img"

def downloader(tries):
    for i in range(1, tries + 1):
        number = random.randint(1, 129200)
        urllib.request.urlretrieve(url + str(number), path_to_file + str(i))
    