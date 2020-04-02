import requests
import json


class TestDogs(object):
    def test_dog(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        dog_get = requests.get('https://dog.ceo/api/breeds/image/random', params=payload)
        response_dict = json.loads(dog_get.content)
        assert response_dict["status"] == 'success'

    def test_dog1(self):
        dog_get1 = requests.get('https://dog.ceo/api/breeds/list/all')
        response_dict = json.loads(dog_get1.content)
        assert response_dict["status"] == 'success'

    def test_dog2(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        dog_get2 = requests.get('https://dog.ceo/api/breed/hound/images/random', params=payload)
        response_dict = json.loads(dog_get2.content)
        assert response_dict["status"] == 'success'

    def test_dog3(self):
        dog_get3 = requests.get('https://dog.ceo/api/breed/hound/list')
        response_dict = json.loads(dog_get3.content)
        assert response_dict["status"] == 'success'

    def test_dog4(self):
        dog_get4 = requests.get('https://dog.ceo/api/breed/hound/afghan/images/random/3')
        response_dict = json.loads(dog_get4.content)
        assert response_dict["status"] == 'success'


class TestBrewery(object):
    def test_brewery(self):
        payload1 = {'key1': 'value1', 'key2': 'value2'}
        brewery_get = requests.get('https://api.openbrewerydb.org/breweries/5494', params=payload1)
        response_dict = json.loads(brewery_get.content)
        assert response_dict["brewery_type"] == "regional"

    def test_brewery1(self):
        payload2 = {'key1': 'value1', 'key2': 'value2'}
        brewery1_get = requests.get('https://api.openbrewerydb.org/breweries?by_type=micro', params=payload2)
        response_dict = json.loads(brewery1_get.content)
        assert response_dict[1]

    def test_brewery2(self):
        brewery2_get = requests.get('https://api.openbrewerydb.org/breweries?page=15')
        response_dict = json.loads(brewery2_get.content)
        assert response_dict[1]

    def test_brewery3(self):
        brewery3_get = requests.get('https://api.openbrewerydb.org/breweries?per_page=25')
        response_dict = json.loads(brewery3_get.content)
        assert response_dict[1]

    def test_brewery4(self):
        brewery4_get = requests.get('https://api.openbrewerydb.org/breweries?by_postal=44107')
        response_dict = json.loads(brewery4_get.content)
        assert response_dict[1]


class Testplace(object):
    def test_place(self):
        payload3 = {'key1': 'value1', 'key2': 'value2'}
        place_get = requests.get('https://jsonplaceholder.typicode.com/todos/1', params=payload3)
        response_dict = json.loads(place_get.content)
        assert response_dict["title"]

    def test_place1(self):
        payload4 = {'key1': 'value1', 'key2': 'value2'}
        place_get1 = requests.get('https://jsonplaceholder.typicode.com/posts', params=payload4)
        response_dict = json.loads(place_get1.content)
        assert response_dict[1]

    def test_place2(self):
        place_get2 = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        response_dict = json.loads(place_get2.content)
        assert response_dict["title"]

    def test_place3(self):
        place_get3 = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
        response_dict = json.loads(place_get3.content)
        assert response_dict[1]

    def test_place4(self):
        place_get4 = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
        response_dict = json.loads(place_get4.content)
        assert response_dict[1]
