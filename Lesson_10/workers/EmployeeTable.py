import pytest
import allure
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

    @allure.step("Создание новой компании")
    def create_company(self, comp_name: str, comp_descr: str) -> str:
        """
        Создает новую компанию и возвращает ее ID
        """
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

    @allure.step("Создание новой сотрудника")
    def create_employee(self, new_worker: dict) -> str:
        """
        Создает нового сотрудника и возвращает его ID
        """
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

    @allure.step("Редактирование данных сотрудника")
    def edit_employee(self, empl_id: str, updated_data: dict) -> None:
        """
        Редактирует (вводит новые данные) сотрудника
        """
        try:
            with self.db.connect() as connection:
                stmt = update(self.employee).where(self.employee.c.id == empl_id).values(updated_data)
                connection.execute(stmt)
                connection.commit()
                print("[INFO] Информация о сотруднике обновлена")
        except Exception as _ex:
            print("[ERROR] Ошибка при обновлении сотрудника", str(_ex))

    @allure.step("Удаление сотрудника c ID = {empl_id}")
    def delete_employee(self, empl_id: str) -> None:
        """
        Удаляет сотрудника
        """
        try:
            with self.db.connect() as connection:
                stmt = delete(self.employee).where(self.employee.c.id == empl_id)
                connection.execute(stmt)
                connection.commit()
                print("[INFO] Сотрудник удален")
        except Exception as _ex:
            print("[ERROR] Ошибка при удалении сотрудника", str(_ex))
        
    @allure.step("Удаление компании")
    def delete_company(self, comp_id: str) -> None:
        """
        Удаляет компанию
        """
        try:    
            with self.db.connect() as connection:
                stmt = delete(self.company).where(self.company.c.id == comp_id)
                connection.execute(stmt)
                connection.commit()
        except Exception as _ex:
            print("[ERROR] Ошибка при удалении сотрудника", str(_ex))

    @allure.step("Получение списка сотрудников")
    def get_employees_list(self, comp_id: str) -> list:
        """
        Возвращает список сотрудников компании (список словарей)
        """
        try:
            with self.db.connect() as connection:
                stmt = self.employee.select().where(self.employee.c.company_id == comp_id)
                result = connection.execute(stmt)
                empl_list = [dict(row) for row in result]
                return empl_list
        except Exception as _ex:
            print("[ERROR] Ошибка при соединении с БД", str(_ex))
            return []

    @allure.step("Получение сотрудника по ID={empl_id}")
    def get_employee_by_id(self, empl_id: str) -> dict:
        """
        Возвращает данные сотрудника (в виде словаря)
        """
        try:
            with self.db.connect() as connection:
                stmt = self.employee.select().where(self.employee.c.id == empl_id)
                result = connection.execute(stmt)
                employee_row = result.fetchone() 
                return dict(employee_row) if employee_row else None  # Возвращаем данные сотрудника или None
        except Exception as _ex:
            print("[ERROR] Ошибка при соединении с БД", str(_ex))
            return None
