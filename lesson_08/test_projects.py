import pytest
from yougile_api import YougileProjectsPage
from config import YOUGILE_TOKEN, BASE_URL


@pytest.fixture()
def api_client():
    return YougileProjectsPage(BASE_URL, YOUGILE_TOKEN)


@pytest.fixture()
def temp_project(api_client):
    response = api_client.create_project("Временный проект")
    project_id = response.json().get("id")
    yield project_id
    if project_id:
        api_client.delete_project(project_id)


# Тесты для POST

def test_post_project_positive(api_client):
    response = api_client.create_project("Супер Проект")
    assert response.status_code == 201
    assert "id" in response.json()
    api_client.delete_project(response.json().get("id"))


def test_post_project_negative_missing_title(api_client):
    response = api_client.create_project("")
    assert response.status_code == 400
    assert "message" in response.json()


# Тесты для GET

def test_get_project_positive(api_client, temp_project):
    response = api_client.get_project(temp_project)
    assert response.status_code == 200
    assert response.json().get("id") == temp_project


def test_get_project_negative_invalid_id(api_client):
    response = api_client.get_project("fake-id-123")
    assert response.status_code == 404


# Тесты для PUT

def test_put_project_positive(api_client, temp_project):
    response = api_client.update_project(temp_project, "Новое имя")
    assert response.status_code == 200


def test_put_project_negative_invalid_id(api_client):
    response = api_client.update_project("fake-id-123", "Новое имя")
    assert response.status_code == 404
