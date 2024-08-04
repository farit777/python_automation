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
    
# Проверка добавления новго сотрудника
def test_add_new_worker():
    # Получить количество сотрудников в компании
    company_id = empl.get_first_company_id()
#    body = empl.get_workers_list(company_id)
#    len_before = len(body)

	#Данные нового сотрудника
    worker = {
#        "id": 0,
        "firstName": "Sfrt",
        "lastName": "Sham",
        "middleName": "string",
        "companyId": company_id,
        "email": "sfrt777@mail.com",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-07-27T11:12:36.267Z",
        "isActive": True
    } 
    # Добавление нового сотрудника
    new_id= empl.add_new_worker(worker)["id"]

    # Получим сотрудника через запрос по API
    worker_api = empl.get_worker(new_id)

    # Получим сотрудника через запрос в БД
    worker_db = db.get_employee_by_id(new_id)

    # Удаляем введенного сотрудника
    db.delete_employee_by_id(new_id)

	# Проверить имя, фамилию и id
    assert worker_api["firstName"] == worker_db[0][4]
    assert worker_api["lastName"] == worker_db[0][5]
    assert worker_api["id"] == worker_db[0][0]


def test_get_worker_by_id():
    """
    1 Сначала получаем список компаний
    2 Берем ID последней компании в списке
    3 По полученному ID получаем список сотрудников в этой компании
    4 Берем ID последнего сотрудника в списке
    5 По этому ID получаем сотрудника из БД
    6 Сравниваем имя и фамилию сотрудника в списке и полученного сотрудника из БД
    """

    # Получим ID, имя и фамилию последнего в списке сотрудника
    company_id = empl.get_first_company_id()
    body = empl.get_workers_list(company_id)
    worker_id = body[-1]["id"]
    worker_name = body[-1]["firstName"]
    worker_last_name = body[-1]["lastName"]

    # Находим сотрудника в БД
    worker_db = db.get_employee_by_id(worker_id)

    # Удаляем введенного сотрудника
    db.delete_employee_by_id(worker_id)

	# Сравниваем имена и фамилии сотрудников
    assert worker_name == worker_db[0][4]
    assert worker_last_name == worker_db[0][5]

def test_edit():
    # Получим ID, первой в списке компании
    company_id = empl.get_first_company_id()

    # Добавим нового сотрудника
    # Данные нового сотрудника
    worker = {
        #"id": 0,
        "firstName": "Sfrt777",
        "lastName": "Sham",
        "middleName": "",
        "companyId": company_id,
        "email": "sfrt@mail.com",
        "url": "",
        "phone": "",
        "birthdate": "2024-07-27T11:28:31.117Z",
        "isActive": True
    } 
    # Добавление нового сотрудника
    new_id = empl.add_new_worker(worker)["id"]

    # Отредактируем данные сотрудника
    new_worker = {
        "lastName": "Шам",
        "email": "far@mail.com",
        "url": "http://1c.ru",
        "phone": "81234567890",
        "isActive": True
    }
    body = empl.edit(new_id, new_worker)
    
    # Получим данные сотрудника из ответа
    edited_id_api = body["id"]
    edited_email_api = body["email"]
    edited_url_api = body["url"]

    # Получим данные сотрудника из БД
    worker_db = db.get_employee_by_id(edited_id_api)

    # Удаляем введенного сотрудника
    db.delete_employee_by_id(edited_id_api)

    # Сравниваем данные, которые вводили с полученными после редатирования
    assert edited_id_api == worker_db[0][0]
    assert edited_email_api == worker_db[0][8]
    assert edited_url_api == worker_db[0][10]
