import requests
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

empl = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Проверка получения списка сотрудников
def test_get_company_workers():
    # Запрос через API
    company_id = empl.get_first_company_id()
    api_result = empl.get_workers_list(company_id)
    
    # Запрос через БД
    db_result = db.get_employees(company_id)

    # Сравниваем результаты
    assert len(api_result) == len(db_result)


    
# Проверка добавления нового сотрудника
def test_add_new_worker():
    # Получить ID первой компании в БД
    company_id = empl.get_first_company_id()

    #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": company_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    # Добавление нового сотрудника
    db.add_new_worker(new_worker)

    # Получим список сотрудников по компании
    db_workers = db.get_employees(company_id)
    # В цикле найдем введенного нового сотрудника
    for w in db_workers:
        if (w["first_name"] == new_worker["first_name"]) and (w["last_name"] == new_worker["last_name"]):
            new_id = w["id"]

    # Получим сотрудника через запрос по API
    worker_api = empl.get_worker(new_id)

    # Получим сотрудника через запрос в БД
    worker_db = db.get_employee_by_id(new_id)

    # Удаляем введенного сотрудника
    db.delete_employee_by_id(new_id)

	# Проверить имя, фамилию и id
    assert worker_api["firstName"] == worker_db["first_name"]
    assert worker_api["lastName"] == worker_db["last_name"]
    assert worker_api["id"] == worker_db["id"]



def test_get_worker_by_id():
    # Получить ID первой компании в БД
    company_id = empl.get_first_company_id()

    #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": company_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    # Добавление нового сотрудника
    db.add_new_worker(new_worker)

    # Получим список сотрудников по компании
    db_workers = db.get_employees(company_id)
    # В цикле найдем введенного нового сотрудника
    for w in db_workers:
        if (w["first_name"] == new_worker["first_name"]) and (w["last_name"] == new_worker["last_name"]):
            worker_id = w["id"]

    # # Находим сотрудника в БД
    worker_db = db.get_employee_by_id(worker_id)

    # Получим сотрудника через запрос по API
    worker_api = empl.get_worker(worker_id)
    
    # # Удаляем введенного сотрудника
    db.delete_employee_by_id(worker_id)

	# Сравниваем имена и фамилии сотрудников
    assert worker_api["firstName"] == worker_db["first_name"]
    assert worker_api["lastName"] == worker_db["last_name"]
    assert worker_api["id"] == worker_db["id"]



def test_edit():
    # Получим ID, первой в списке компании
    company_id = empl.get_first_company_id()

    #Данные нового сотрудника
    new_worker = {
        "first_name": "Sfrt",
        "last_name": "Sham",
        "middle_name": "",
        "company_id": company_id,
        "email": "sfrt@mail.com",
        "avatar_url": "",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    # Добавление нового сотрудника
    db.add_new_worker(new_worker)
    
    # Получим список сотрудников по компании
    db_workers = db.get_employees(company_id)
    # В цикле найдем введенного нового сотрудника
    for w in db_workers:
        if (w["first_name"] == new_worker["first_name"]) and (w["last_name"] == new_worker["last_name"]):
            worker_id = w["id"]


    # Отредактируем данные сотрудника
    edited_worker = {
        "first_name": "Фарит",
        "last_name": "Шам",
        "middle_name": "",
        "company_id": company_id,
        "email": "sfrt@mail.com",
        "avatar_url": "http://1c.ru",
        "phone": "89182793824",
        "birthdate": "1954/05/31",
        "is_active": True
    } 

    db.update_employee(worker_id, edited_worker)

    # Получим данные сотрудника из БД
    worker_db = db.get_employee_by_id(worker_id)

    # Получим сотрудника через запрос по API
    worker_api = empl.get_worker(worker_id)    

    # Удаляем введенного сотрудника
    db.delete_employee_by_id(worker_id)

    # Сравниваем данные, которые вводили с полученными после редатирования
    assert worker_api["lastName"] == worker_db["last_name"]
    assert worker_api["email"] == worker_db["email"]
    assert worker_api["phone"] == worker_db["phone"]
    assert worker_api["id"] == worker_db["id"]
