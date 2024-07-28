import requests
from EmployeeApi import EmployeeApi

empl = EmployeeApi("https://x-clients-be.onrender.com")

# Проверка получения списка сотрудников
def test_get_company_workers():
    company_id = empl.get_first_company_id()
    body = empl.get_workers_list(company_id)
    assert len(body) > 0
    
# Проверка добавления новго сотрудника
def test_add_new_worker():
    # Получить количество сотрудников в компании
    company_id = empl.get_first_company_id()
    body = empl.get_workers_list(company_id)
    len_before = len(body)

	#Данные нового сотрудника
    worker = {
        "id": 0,
        "firstName": "Sfrt",
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
    resp = empl.add_new_worker(worker)
    new_id = resp["id"]

	# Получить кол-во сотрудников
    body = empl.get_workers_list(company_id)
    len_after = len(body)

	# Проверить, что +1
    assert len_after - len_before == 1

	# Проверить имя, фамилию и id
    assert body[-1]["firstName"] == worker["firstName"]
    assert body[-1]["lastName"] == worker["lastName"]
    assert body[-1]["id"] == new_id


def test_get_worker_by_id():
    '''
    1 Сначала получаем список компаний
    2 Берем ID последней компании в списке
    3 По полученному ID получаем список сотрудников в этой компании
    4 Берем ID последнего сотрудника в списке
    5 По этому ID получаем сотрудника
    6 Сравниваем имя и фамилию сотрудника в списке и полученного сотрудника
    '''

    # Получим ID, имя и фамилию последнего в списке сотрудника
    company_id = empl.get_first_company_id()
    body = empl.get_workers_list(company_id)
    worker_id = body[-1]["id"]
    worker_name = body[-1]["firstName"]
    worker_last_name = body[-1]["lastName"]
    resp = empl.get_worker(worker_id)

	# Проверим имя и фаилию
    assert body[-1]["firstName"] == resp["firstName"]
    assert body[-1]["lastName"] == resp["lastName"]

def test_edit():
    # Получим ID, первой в списке компании
    company_id = empl.get_first_company_id()

    # Добавим нового сотрудника
    # Данные нового сотрудника
    worker = {
        "id": 0,
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
    resp = empl.add_new_worker(worker)
    new_id = resp["id"]
    #new_name = resp["firstName"]
    #new_last_name = resp["lastName"]

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
    edited_id = body["id"]
    edited_email = body["email"]
    edited_url = body["url"]

    # Сравниваем данные, которые вводили с полученными после редатирования
    assert new_id == edited_id
    assert new_worker["email"] == edited_email
    assert new_worker["url"] == edited_url
