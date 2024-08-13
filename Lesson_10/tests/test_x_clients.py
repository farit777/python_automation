import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import requests
import allure
from workers.EmployeeApi import EmployeeApi
from workers.EmployeeTable import EmployeeTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

@allure.epic("X-clients")
@allure.title("Добавление нового сотрудника")
@allure.description("Словарь данных и добавление нового сотрудника")
@allure.feature("Тест 1")
@allure.severity(severity_level='normal')
def test_add_new_worker():
    with allure.step("Создаем компанию и получаем его ID"):
        comp_id = db.create_company('Farit & Co', 'Company for tests')

    #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": comp_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    with allure.step("DB: Создаем нового сотрудника и получаем его ID"):
        empl_id = db.create_employee(new_worker)

    with allure.step("API: Получаем сотрудника c id = {empl_id} через запрос по API"):
        api_worker = api.get_worker(empl_id)

    with allure.step("BD: Получим сотрудника c id = {empl_id} через запрос в БД"):
        db_worker = db.get_employee_by_id(empl_id)

    with allure.step("Удаляем введенного сотрудника c id = {empl_id}"):
        db.delete_employee(empl_id)

    with allure.step("Удаляем введенную компанию c id = {comp_id}"):
        db.delete_company(comp_id)

    with allure.step("Сравниваем имя, фамилию  и id"):
        assert api_worker["firstName"] == db_worker["first_name"]
        assert api_worker["lastName"] == db_worker["last_name"]
        assert api_worker["id"] == db_worker["id"]


@allure.epic("X-clients")
@allure.title("Редактирование сотрудника")
@allure.description("Редактирование данных сотрудника")
@allure.feature("Тест 2")
@allure.severity(severity_level='normal')
def test_edit_employee():
    with allure.step("DB: Создаем компанию и получаем его ID"):
        comp_id = db.create_company('Farit & Co', 'Company for tests')

    #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": comp_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    with allure.step("DB: Создаем нового сотрудника и получаем его ID"):
        empl_id = db.create_employee(new_worker)

    # Отредактируем данные сотрудника
    edited_worker = {
        "first_name": "Фарит",
        "last_name": "Шам",
        "middle_name": "",
        "company_id": comp_id,
        "email": "sfrt@mail.com",
        "avatar_url": "http://1c.ru",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 
    with allure.step("DB: Редактируем данные сотрудника c id = {empl_id}"):
        db.edit_employee(empl_id, edited_worker)
    #api.edit_employee(empl_id, edited_worker)

    with allure.step("DB: Получим данные сотрудника c id = {empl_id} из БД"):
        worker_db = db.get_employee_by_id(empl_id)

    with allure.step("API: Получаем сотрудника c id = {empl_id} через запрос по API"):
        worker_api = api.get_worker(empl_id)

    with allure.step("Удаляем введенного сотрудника c id = {empl_id}"):
        db.delete_employee(empl_id)

    with allure.step("Удаляем введенную компанию c id = {comp_id}"):
        db.delete_company(comp_id)

    with allure.step("Сравниваем данные"):
        assert worker_api["lastName"] == worker_db["last_name"]
        assert worker_api["email"] == worker_db["email"]
        assert worker_api["phone"] == worker_db["phone"]
        assert worker_api["id"] == worker_db["id"]


@allure.epic("X-clients")
@allure.title("Получение сотрудника по ID")
@allure.description("Получения сотрудника по ID")
@allure.feature("Тест 3")
@allure.severity(severity_level='normal')
def test_get_worker_by_id():
    with allure.step("DB: Создаем компанию и получаем еe ID"):
        comp_id = db.create_company('Farit & Co', 'Company for tests')

    #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": comp_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    with allure.step("DB: Создаем нового сотрудника и получаем его ID"):
        empl_id = db.create_employee(new_worker)

    with allure.step("DB: Получим данные сотрудника c id = {empl_id} из БД"):
        worker_db = db.get_employee_by_id(empl_id)
    
    with allure.step("API: Получаем сотрудника c id = {empl_id} через запрос по API"):
        worker_api = api.get_worker(empl_id)
    
    with allure.step("Удаляем введенного сотрудника c id = {empl_id}"):
        db.delete_employee(empl_id)

    with allure.step("Удаляем введенную компанию c id = {comp_id}"):
        db.delete_company(comp_id)

    with allure.step("Сравниваем имена, фамилии и id сотрудников"):
        assert worker_api["firstName"] == worker_db["first_name"]
        assert worker_api["lastName"] == worker_db["last_name"]
        assert worker_api["id"] == worker_db["id"]

@allure.epic("X-clients")
@allure.title("Получение списка сотрудников")
@allure.description("Получение списка сотрудников")
@allure.feature("Тест 4")
@allure.severity(severity_level='normal')
def test_get_company_workers():
    with allure.step("DB: Создаем компанию и получаем еe ID"):
        comp_id = db.create_company('Farit & Co', 'Company for tests')

        #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": comp_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    }

    with allure.step("DB: Создаем нового сотрудника и получаем его ID"):
        empl_id = db.create_employee(new_worker)

    with allure.step("DB: Получим список сотрудников компании c id = {comp_id} запросом в БД"):
        db_list = db.get_employees_list(comp_id)
        
    with allure.step("API: Получим список сотрудников компании c id = {comp_id} запросом через API"):
        api_list = api.get_workers_list(comp_id)

    with allure.step("Удаляем введенного сотрудникаc id = {empl_id}"):
        db.delete_employee(empl_id)
    
    with allure.step("Удаляем введенную компанию c id = {comp_id}"):
        db.delete_company(comp_id)

    with allure.step("Сравниваем результаты"):
        assert len(api_list) == len(db_list)
