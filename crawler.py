import time
import getpass
import os
import json
import urllib.request
import shutil
import natsort
import urllib.error
import sys
import chromedriver_autoinstaller
import subprocess
from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get
from tqdm import tqdm
from img2pdf import convert
subprocess.call('python crawler_selenium-ver.py', shell=True)
