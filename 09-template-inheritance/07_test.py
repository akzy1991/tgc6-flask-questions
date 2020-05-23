# test_hello.py
from app import app
from bs4 import BeautifulSoup

def test_index_route_task_1():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.title.string == 'Welcome to my homepage!'
    assert soup.find_all('div')[0].get('id')=='nav'
    assert soup.find('h1').string == 'Welcome to Our Web Store!'
    assert soup.find('p').string.strip() == 'Step right in to find all your online teaching needs'

def test_gallery_route():
    response = app.test_client().get('/gallery')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.title.string == 'Welcome to my homepage!'
    assert soup.find_all('div')[0].get('id')=='nav'

    assert soup.find('h1').string == 'Our Gallery'
    assert soup.find('p').string.strip() == 'Browse our products at your lesiure!'