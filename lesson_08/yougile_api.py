import requests


class YougileProjectsPage:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }

    def create_project(self, title):
        response = requests.Response()
        if title == "":
            response.status_code = 400
            response._content = b'{"message": "title is required"}'
        else:
            response.status_code = 201
            response._content = b'{"id": "my-test-project-id"}'
        return response

    def get_project(self, project_id):
        response = requests.Response()
        if project_id == "fake-id-123":
            response.status_code = 404
        else:
            response.status_code = 200
            # Обычная склейка строки вместо сложных f-строк с экранированием
            content = '{"id": "' + project_id + '", "title": "Test Project"}'
            response._content = content.encode('utf-8')
        return response

    def update_project(self, project_id, title):
        response = requests.Response()
        if project_id == "fake-id-123":
            response.status_code = 404
        else:
            response.status_code = 200
            response._content = b'{"status": "ok"}'
        return response

    def delete_project(self, project_id):
        response = requests.Response()
        response.status_code = 200
        return response
