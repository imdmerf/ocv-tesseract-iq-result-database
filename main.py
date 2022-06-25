from vision import get_iq_name
from visualizing import visual
from parser import downloader

tries = int(input("Enter count of tries:"))
downloader(tries)
get_iq_name()
visual()