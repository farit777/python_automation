import pytest
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, MetaData
from sqlalchemy.sql import insert, update, delete

class EmployeeTable:

    def __init__(self, connection_string):

        self.db = create_engine(connection_string)

        # Определение метаданных
        self.metadata = MetaData()

        # Определение таблицы 'company'
        self.company = Table('company', self.metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String),
            Column('description', String, nullable=True),
            Column('is_active', Boolean)
    )

        # Определение таблицы 'employee'
        self.employee = Table('employee', self.metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('first_name', String),
            Column('last_name',String),
            Column('middle_name', String, nullable=True),
            Column('company_id', Integer),
            Column('email', String, nullable=True),
            Column('avatar_url', String, nullable=True),
            Column('phone', String),
            Column('birthdate', DateTime, nullable=True),
            Column('is_active', Boolean)
    )

    # Создание новой компании
    def create_company(self, comp_name, comp_descr):
        try:
            with self.db.connect() as connection:
                stmt = insert(self.company).values(name=comp_name, description=comp_descr).returning(self.company.c.id)
                result = connection.execute(stmt)
                connection.commit()
                comp_id = result.scalar()  # Получаем новый ID
                return comp_id
        except Exception as _ex:
            print("[INFO] Ошибка при соединении с БД", _ex)
            return None

    # Создание нового сотрудника
    def create_employee(self, new_worker):
        try:
            with self.db.connect() as connection:
                stmt = insert(self.employee).values(new_worker).returning(self.employee.c.id)
                result = connection.execute(stmt)
                connection.commit()
                empl_id = result.scalar()  # Получаем ID нового сотрудника
                return empl_id  # Возвращаем ID
        except Exception as _ex:
            print("[INFO] Ошибка при соединении с БД", _ex)
            return None

    # Редактирование данных сотрудника
    def edit_employee(self, empl_id, updated_data):
        try:
            with self.db.connect() as connection:
                stmt = update(self.employee).where(self.employee.c.id == empl_id).values(updated_data)
                connection.execute(stmt)
                connection.commit()
                print("[INFO] Информация о сотруднике обновлена")
        except Exception as _ex:
            print("[ERROR] Ошибка при обновлении сотрудника", str(_ex))

    # Удаление сотрудника
    def delete_employee(self, empl_id):
        try:
            with self.db.connect() as connection:
                stmt = delete(self.employee).where(self.employee.c.id == empl_id)
                connection.execute(stmt)
                connection.commit()
                print("[INFO] Сотрудник удален")
        except Exception as _ex:
            print("[ERROR] Ошибка при удалении сотрудника", str(_ex))
        
    # Удаление компании
    def delete_company(self, comp_id):
        try:    
            with self.db.connect() as connection:
                stmt = delete(self.company).where(self.company.c.id == comp_id)
                connection.execute(stmt)
                connection.commit()
        except Exception as _ex:
            print("[ERROR] Ошибка при удалении сотрудника", str(_ex))

    # Получение списка сотрудников
    def get_employees_list(self, comp_id):
        try:
            with self.db.connect() as connection:
                stmt = self.employee.select().where(self.employee.c.company_id == comp_id)
                result = connection.execute(stmt)
                empl_list = [dict(row) for row in result]
                return empl_list
        except Exception as _ex:
            print("[ERROR] Ошибка при соединении с БД", str(_ex))
            return []

    # Получить сотрудника по ID
    def get_employee_by_id(self, empl_id):
        try:
            with self.db.connect() as connection:
                stmt = self.employee.select().where(self.employee.c.id == empl_id)
                result = connection.execute(stmt)
                employee_row = result.fetchone() 
                return dict(employee_row) if employee_row else None  # Возвращаем данные сотрудника или None
        except Exception as _ex:
            print("[ERROR] Ошибка при соединении с БД", str(_ex))
            return None
