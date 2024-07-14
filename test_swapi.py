from request_page import RequestPage
import urllib3
import pytest
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

list_endpoints = []


class TestSwapi(RequestPage):
    @pytest.mark.smoke
    def test_main_page(self):
        self.main_page_request(list_endpoints)

    @pytest.mark.smoke
    def test_people_page(self):
        self.people_page(list_endpoints)

    @pytest.mark.smoke
    def test_people_request_ID_1(self):
        self.people_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_planets_page(self):
        self.planets_page(list_endpoints)

    @pytest.mark.smoke
    def test_planets_request_ID_1(self):
        self.planets_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_films_page(self):
        self.films_page(list_endpoints)

    @pytest.mark.smoke
    def test_films_request_ID_1(self):
        self.films_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_species_page(self):
        self.species_page(list_endpoints)

    @pytest.mark.smoke
    def test_species_request_ID_1(self):
        self.species_request_ID_1(list_endpoints)

    @pytest.mark.smoke
    def test_vehicles_page(self):
        self.vehicles_page(list_endpoints)

    @pytest.mark.smoke
    def test_vehicles_request_ID_4(self):
        self.vehicles_request_ID_4(list_endpoints)

    @pytest.mark.smoke
    def test_starships_page(self):
        self.starships_page(list_endpoints)

    @pytest.mark.smoke
    def test_starships_request_ID_9(self):
        self.starships_request_ID_9(list_endpoints)
