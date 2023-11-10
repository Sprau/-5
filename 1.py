import allure
import pytest
import requests
from model import Pet

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def pet_data():
    return {
        "id": 1,
        "category_id": 1,
        "name": "TestPet",
        "photo_urls": ["url1", "url2"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available",
    }

@allure.feature("PetStore API")
@allure.story("Pet Operations")
class TestPetStore:

    @allure.title("Add a new pet to the store")
    def test_add_pet(self, pet_data):
        response = requests.post(f"{BASE_URL}/pet", json=pet_data)
        assert response.status_code == 200

    @allure.title("Get pet information by ID")
    def test_get_pet_by_id(self, pet_data):
        #  добавьть питомца
        add_response = requests.post(f"{BASE_URL}/pet", json=pet_data)
        assert add_response.status_code == 200

        pet_id = pet_data["id"]
        response = requests.get(f"{BASE_URL}/pet/{pet_id}")
        assert response.status_code == 200

        #Проверка ответа на соответствие модели Pydantic
        pet = Pet(**response.json()) 
        assert pet == Pet(**pet_data)

    # Add more tests as needed