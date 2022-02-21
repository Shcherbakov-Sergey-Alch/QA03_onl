import time

import requests


def add_pet(host, json):
    response = requests.post(host, json=json)
    return response


def get_pet_by_id(host, pet_id):
    time.sleep(15)
    response = requests.get(f"{host}/{pet_id}")
    return response


def delete_pet(host, pet_id):
    response = requests.delete(f"{host}/{pet_id}")
    return response
