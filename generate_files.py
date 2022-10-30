import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects, HTTPError
from decouple import config
import logging


def modif_url(url):
    """This function modifies url in order to download dataset files in .csv format"""
    url = '/'.join(url.split('/')[:-1] + ['export?format=csv'])

    return url


def generate_files(c, fecha_carga):

    if c == 'bibliotecas':
        url = config('URL_BIBLIOTECAS')
    elif c == 'cines':
        url = config('URL_CINES')
    else:
        url = config('URL_MUSEOS')

    url = modif_url(url)

    try:
        r = requests.get(url)
        r.raise_for_status()
    except (HTTPError, ConnectionError, Timeout, TooManyRedirects) as e:
        logging.error(e)

    with open(f'{c}/{fecha_carga.year}-{fecha_carga.month}/{c}-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}.csv', 'wb') as f:
        f.write(r.content)
    
    logging.info(
        f'File successfully created: "{c}-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}"')
