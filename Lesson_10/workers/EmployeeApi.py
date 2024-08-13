import requests
import allure

class EmployeeApi:
    # Инициализация 
    def __init__(self, url: str):
        self.url = url

    # # Получить ID первой компании из списка   
    # def get_first_company_id(self) -> str:
    #     """
    #     Получает список компаний и выводит ID первой в списке компании
    #     """
    #     # Получим список компаний
    #     resp = requests.get(self.url + '/company')
    #     company_list = resp.json()
        
    #     # Вернем ID первой компании из списка
    #     return company_list[0]['id']


    @allure.step("Получим список сотрудников компании c id = {company_id}")
    def get_workers_list(self, company_id: str):
        """
        Возвращает список сотрудников компании
        """
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()
    
    @allure.step("Получить токен авторизации {user}:{password}")
    def get_token(self, user='leonardo', password='leads') -> str:
        """
        Возвращает токен авторизации
        """
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    @allure.step("Получим сотрудника по ID = {id}")
    def get_worker(self, id: str) -> dict:
        """
        Возвращает данные сотрудника компании
        """
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    @allure.step("Изменяем данные сотрудника c ID = {new_id}")# 
    def edit_employee(self, new_id: str, worker_dict: dict) -> any:
        """
        Редактирует данные сотрудника (вводит новые) и возвращает их
        """
        my_headers = {}
        # Авторизуемся как пользователь
        my_headers["x-client-token"] = self.get_token()
        
        # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.patch(self.url + '/employee/' +
                              str(new_id), headers=my_headers, json=worker_dict)
        
        # Результат вернется в JSON
        return resp.json()