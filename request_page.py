import requests
import pytest


class RequestPage():
    """"Класс запросов для API SWAPI"""
    def main_page_request(self, list_endpoints):
        """"Запрос к основной странице и получения основных разделов"""
        try:
            responce = requests.get("http://swapi.py4e.com/api", timeout=1)
            assert responce.status_code == 200
            endpoints = (responce.text).replace(
                '{', '').replace('}', '').replace('"', '').split(',')
            for i in range(len(endpoints)):
                list_endpoints.append(
                    (endpoints[i])[(endpoints[i]).find(':')+1:])
            assert responce.status_code == 200
            return list_endpoints
        except AssertionError:
            return pytest.fail()

    def people_page(self, list_endpoints):
        """"Запрос к странице людей и получения списка людей"""
        try:
            responce = requests.get(f"{list_endpoints[0]}", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('count') != 0
        except AssertionError:
            return pytest.fail()

    def people_request_ID_1(self, list_endpoints):
        """"Запрос получения данных о человеке с ID 1"""
        try:
            responce = requests.get(f"{list_endpoints[0]}/1", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('name') == 'Luke Skywalker'
            assert responce.json().get('mass') == '77'
            assert responce.json().get('gender') == 'male'
            assert responce.json().get('skin_color') == "fair"
        except AssertionError:
            return pytest.fail()

    def planets_page(self, list_endpoints):
        """"Запрос к странице планет и получения списка планет"""
        try:
            responce = requests.get(f"{list_endpoints[1]}", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('count') != 0
        except AssertionError:
            return pytest.fail()

    def planets_request_ID_1(self, list_endpoints):
        """"Запрос получения данных о планете с ID 1"""
        try:
            responce = requests.get(f"{list_endpoints[1]}/1", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('name') == 'Tatooine'
            assert responce.json().get('rotation_period') == '23'
            assert responce.json().get('climate') == 'arid'
            assert responce.json().get('terrain') == 'desert'
        except AssertionError:
            return pytest.fail()

    def films_page(self, list_endpoints):
        """"Запрос к странице фильмов и получения списка фильмов"""
        try:
            responce = requests.get(f"{list_endpoints[2]}", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('count') != 0
        except AssertionError:
            return pytest.fail()

    def films_request_ID_1(self, list_endpoints):
        """"Запрос получения данных о фильме с ID 1"""
        try:
            responce = requests.get(f"{list_endpoints[2]}/1", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('title') == 'A New Hope'
            assert responce.json().get('episode_id') == 4
            assert responce.json().get('director') == 'George Lucas'
        except AssertionError:
            return pytest.fail()

    def species_page(self, list_endpoints):
        """"Запрос к странице видов и получения списка видов"""
        try:
            responce = requests.get(f"{list_endpoints[3]}", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('count') != 0
        except AssertionError:
            return pytest.fail()

    def species_request_ID_1(self, list_endpoints):
        """"Запрос получения данных о виде с ID 1"""
        try:
            responce = requests.get(f"{list_endpoints[3]}/1", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('name') == 'Human'
            assert responce.json().get('classification') == 'mammal'
            assert responce.json().get('skin_colors') == \
                'caucasian, black, asian, hispanic'
            assert responce.json().get('language') == 'Galactic Basic'
        except AssertionError:
            return pytest.fail()

    def vehicles_page(self, list_endpoints):
        """"Запрос к странице транспорта и получения списка транспорта"""
        try:
            responce = requests.get(f"{list_endpoints[4]}", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('count') != 0
        except AssertionError:
            return pytest.fail()

    def vehicles_request_ID_4(self, list_endpoints):
        """"Запрос получения данных о транспорте с ID 4"""
        try:
            responce = requests.get(f"{list_endpoints[4]}/4", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('cost_in_credits') == '150000'
            assert responce.json().get('name') == 'Sand Crawler'
            assert responce.json().get('model') == 'Digger Crawler'
            assert responce.json().get('crew') == '46'
        except AssertionError:
            return pytest.fail()

    def starships_page(self, list_endpoints):
        """"Запрос к странице звездолётов и получения списка звездолётов"""
        try:
            responce = requests.get(f"{list_endpoints[5]}", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('count') != 0
        except AssertionError:
            return pytest.fail()

    def starships_request_ID_9(self, list_endpoints):
        """"Запрос получения данных о звездолёте с ID 9"""
        try:
            responce = requests.get(f"{list_endpoints[5]}/9", timeout=1)
            assert responce.status_code == 200
            assert responce.json().get('cost_in_credits') == '1000000000000'
            assert responce.json().get('name') == 'Death Star'
            assert responce.json().get('model') == \
                'DS-1 Orbital Battle Station'
            assert responce.json().get('crew') == '342,953'
        except AssertionError:
            return pytest.fail()
