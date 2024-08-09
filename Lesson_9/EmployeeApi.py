import requests

class EmployeeApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url

    # Получить ID первой компании из списка   
    def get_first_company_id(self):
        # Получим список компаний
        resp = requests.get(self.url + '/company')
        company_list = resp.json()
        
        # Вернем ID первой компании из списка
        return company_list[0]['id']

    # Получить список сотрудников компании
    def get_workers_list(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()
    
    # Получить токен авторизации
    def get_token(self, user='leonardo', password='leads'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    # Добавить нового сотрудника
    def add_new_worker(self, new_worker):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=new_worker, headers=my_headers)
        return resp.json()
    
    # Плучить сотрудника по ID
    def get_worker(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    # Редакировать сотрудника
    def edit_employee(self, new_id, worker_dict):
        my_headers = {}
        # Авторизуемся как пользователь
        my_headers["x-client-token"] = self.get_token()
        
        # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.patch(self.url + '/employee/' +
                              str(new_id), headers=my_headers, json=worker_dict)
        
        # Результат вернется в JSON, мы его прокинем в тест
        return resp.json()