import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects, HTTPError
from decouple import config
import logging


def modif_url(url):
    """This function modifies url in order to download dataset files in .csv format"""
    url = '/'.join(url.split('/')[:-1] + ['export?format=csv'])

    return url


