import requests

from amf.config import NSSF_GET_SLICES


def search():
    return 'sample users', 200


def put(body):
    # connection to register endpoint (...)
    data = requests.get(NSSF_GET_SLICES)
    return f'Available slices: {data.json()}', 200
