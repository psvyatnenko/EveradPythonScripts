import requests
import unittest

def httpPostRequestCrmApiRU():
    r = requests.post("http://leibniz.crm.safesocks.ru/api/orders",
                      data={'country_code': 'ru', 'address': 'some sreet', 'name': 'some name', 'phone': '+79008500000', 'token': 'secccret', 'landing_id': '99'})
    print(r.status_code, r.reason)

def httpPostRequestCrmApiUA():
    r = requests.post("http://leibniz.crm.safesocks.ru/api/orders",
                      data={'country_code': 'ua', 'address': 'some sreet', 'name': 'some name', 'phone': '+380674443322', 'token': 'secccret', 'landing_id': '99'})
    print(r.status_code, r.reason)

def httpPostRequestCrmApiKZ():
    r = requests.post("http://leibniz.crm.safesocks.ru/api/orders",
                      data={'country_code': 'kz', 'address': 'some sreet', 'name': 'some name', 'phone': '+7291234567', 'token': 'secccret', 'landing_id': '99'})
    print(r.status_code, r.reason)

def httpPostRequestLhApiRU():
    r = requests.post("http://api.lh-master.safesocks.ru/api/orders",
                      data={'country_code': 'ru', 'address': 'some sreet', 'name': 'some name', 'phone': '+79008500000', 'token': 'a500cffe-e718-45fa-b42d-2c0d9f6de42e', 'offer_id': '80'})
    print(r.status_code, r.reason)

def httpPostRequestLhApiUA():
    r = requests.post("http://api.lh-master.safesocks.ru/api/orders",
                      data={'country_code': 'ua', 'address': 'some sreet', 'name': 'some name', 'phone': '+380674443322', 'token': 'a500cffe-e718-45fa-b42d-2c0d9f6de42e', 'offer_id': '80'})
    print(r.status_code, r.reason)

def httpPostRequestLhApiKZ():
    r = requests.post("http://api.lh-master.safesocks.ru/api/orders",
                      data={'country_code': 'kz', 'address': 'some sreet', 'name': 'some name', 'phone': '+7291234567', 'token': 'a500cffe-e718-45fa-b42d-2c0d9f6de42e', 'offer_id': '80'})
    print(r.status_code, r.reason)
