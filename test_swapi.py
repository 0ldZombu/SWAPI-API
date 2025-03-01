from request_page import RequestPage
import urllib3
import pytest
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

list_endpoints = []


class TestSwapi:
    @pytest.mark.smoke
    def test_main_page(self):
        page = RequestPage()
        page.main_page_request(list_endpoints)

    @pytest.mark.smoke
    def test_people_page(self):
        page = RequestPage()
        page.people_page(list_endpoints)

    @pytest.mark.smoke
    def test_people_request_ID_1(self):
        page = RequestPage()
        page.people_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_planets_page(self):
        page = RequestPage()
        page.planets_page(list_endpoints)

    @pytest.mark.smoke
    def test_planets_request_ID_1(self):
        page = RequestPage()
        page.planets_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_films_page(self):
        page = RequestPage()
        page.films_page(list_endpoints)

    @pytest.mark.smoke
    def test_films_request_ID_1(self):
        page = RequestPage()
        page.films_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_species_page(self):
        page = RequestPage()
        page.species_page(list_endpoints)

    @pytest.mark.smoke
    def test_species_request_ID_1(self):
        page = RequestPage()
        page.species_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_vehicles_page(self):
        page = RequestPage()
        page.vehicles_page(list_endpoints)

    @pytest.mark.smoke
    def test_vehicles_request_ID_4(self):
        page = RequestPage()
        page.vehicles_request_ID_4(list_endpoints)

    @pytest.mark.smoke
    def test_starships_page(self):
        page = RequestPage()
        page.starships_page(list_endpoints)

    @pytest.mark.smoke
    def test_starships_request_ID_9(self):
        page = RequestPage()
        page.starships_request_ID_9(list_endpoints)

    @pytest.mark.smoke
    def test_generate_allure(self):
        page = RequestPage()
        page.generate_allure()
