from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

class EmployeeTable:
    __scripts = {
        "select employees": text("SELECT * FROM employee WHERE company_id = :company_id"),
        "select employee by ID": text("SELECT * FROM employee WHERE id = :id"),
        "delete employee by ID": text("DELETE FROM employee WHERE id = :id")
    }

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def get_employees(self, id):
        # Создаем сессию
        with self.Session() as session:
            result = session.execute(self.__scripts["select employees"], {'company_id': id})
            return result.fetchall()
        
    def get_employee_by_id(self, id):
        with self.Session() as session:
            result = session.execute(self.__scripts["select employee by ID"], {'id': id})
            return result.fetchall()
        
    def delete_employee_by_id(self, id):
        with self.Session() as session:
            session.execute(self.__scripts["delete employee by ID"], {'id': id})
            session.commit() 





    #   "select only active": "select * from company where \"is_active\" = true  and deleted_at is null",
    #     "delete by id": text("delete from company where id =:id_to_delete"),
    #     "insert new": text("insert into company(\"name\") values (:new_name)"),
    #     "get max id": "select MAX(\"id\") from company where deleted_at is null"