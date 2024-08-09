import requests
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Проверка добавления нового сотрудника
def test_add_new_worker():
    # Создаем компанию и получаем его ID
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

    # Добавление нового сотрудника
    empl_id = db.create_employee(new_worker)

    # Получим сотрудника через запрос по API
    api_worker = api.get_worker(empl_id)

    # Получим сотрудника через запрос в БД
    db_worker = db.get_employee_by_id(empl_id)

    # Удаляем введенного сотрудника
    db.delete_employee(empl_id)

    # Удаляем введенную компанию
    db.delete_company(comp_id)

	# Проверить имя, фамилию и id
    assert api_worker["firstName"] == db_worker["first_name"]
    assert api_worker["lastName"] == db_worker["last_name"]
    assert api_worker["id"] == db_worker["id"]


# Проверка редактирования данных сотрудника
def test_edit_employee():
    # Создаем компанию и получаем его ID
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

    # Добавление нового сотрудника
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

    ###db.edit_employee(empl_id, edited_worker)
    api.edit_employee(empl_id, edited_worker)

    # Получим данные сотрудника из БД
    worker_db = db.get_employee_by_id(empl_id)

    # Получим сотрудника через запрос по API
    worker_api = api.get_worker(empl_id)

    # Удаляем введенного сотрудника
    db.delete_employee(empl_id)

    # Удаляем введенную компанию
    db.delete_company(comp_id)

    # Сравниваем данные
    assert worker_api["lastName"] == worker_db["last_name"]
    assert worker_api["email"] == worker_db["email"]
    assert worker_api["phone"] == worker_db["phone"]
    assert worker_api["id"] == worker_db["id"]


# Проверка получения сотрудника по ID
def test_get_worker_by_id():
    # Создаем компанию и получаем его ID
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

    # Добавление нового сотрудника
    empl_id = db.create_employee(new_worker)

    # # Находим сотрудника в БД
    worker_db = db.get_employee_by_id(empl_id)
    
    # Получим сотрудника через запрос по API
    worker_api = api.get_worker(empl_id)
    
    # # Удаляем введенного сотрудника
    db.delete_employee(empl_id)

    # Удаляем введенную компанию
    db.delete_company(comp_id)

	# Сравниваем имена и фамилии сотрудников
    assert worker_api["firstName"] == worker_db["first_name"]
    assert worker_api["lastName"] == worker_db["last_name"]
    assert worker_api["id"] == worker_db["id"]

# Проверка получения списка сотрудников
def test_get_company_workers():
    # Создаем новую компанию
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

    # Добавим сотрудника в компанию
    empl_id = db.create_employee(new_worker)

    # Получим список сотрудников запросом в БД
    db_list = db.get_employees_list(comp_id)
        
    # Получим список сотрудников запросом через API
    api_list = api.get_workers_list(comp_id)

    # Удаляем сотрудника
    db.delete_employee(empl_id)
    
    # Удаляем введенную компанию
    db.delete_company(comp_id)

    # Сравниваем результаты
    assert len(api_list) == len(db_list)
