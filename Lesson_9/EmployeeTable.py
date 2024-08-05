from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import NoResultFound

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String, nullable=True)
    company_id = Column(Integer)
    email = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    phone = Column(String)
    birthdate = Column(DateTime, nullable=True)
    is_active = Column(Boolean)

class EmployeeTable:
    scripts = {
        "select employees": text("SELECT * FROM employee WHERE company_id = :company_id"),
        "select employee by ID": text("SELECT * FROM employee WHERE id = :id"),
        "delete employee by ID": text("DELETE FROM employee WHERE id = :id"),
        "update employee": text("UPDATE employee SET first_name = :first_name, last_name = :last_name, "
                                 "middle_name = :middle_name, company_id = :company_id, email = :email, "
                                 "avatar_url = :avatar_url, phone = :phone, birthdate = :birthdate, is_active = :is_active "
                                 "WHERE id = :id")
    }

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def delete_employee_by_id(self, id):
        with self.Session() as session:
            result = session.execute(self.scripts["delete employee by ID"], {'id': id})
            if result.rowcount == 0:
                raise ValueError(f"Employee with ID {id} not found.")
            session.commit()

    def add_new_worker(self, new_worker):
        with self.Session() as session:
            employee = Employee(
                first_name=new_worker["first_name"],
                last_name=new_worker["last_name"],
                middle_name=new_worker["middle_name"],
                company_id=new_worker["company_id"],
                email=new_worker["email"],
                avatar_url=new_worker["avatar_url"],
                phone=new_worker["phone"],
                birthdate=new_worker["birthdate"],
                is_active=new_worker["is_active"]
            )
            session.add(employee)
            session.commit()

    def get_employees(self, company_id):
        with self.Session() as session:
            result = session.execute(self.scripts["select employees"], {'company_id': company_id})
            return [dict(zip(result.keys(), row)) for row in result]
            

    def get_employee_by_id(self, id):
        with self.Session() as session:
            result = session.execute(self.scripts["select employee by ID"], {'id': id})
            employee = result.mappings().first()  # Получаем первую запись как словарь
            if employee is None:
                raise ValueError(f"Employee with ID {id} not found.")
            return dict(employee)

    def update_employee(self, id, updated_info):
        with self.Session() as session:
            result = session.execute(self.scripts["update employee"], {
                'id': id,
                'first_name': updated_info.get("first_name"),
                'last_name': updated_info.get("last_name"),
                'middle_name': updated_info.get("middle_name", ""),
                'company_id': updated_info.get("company_id"),
                'email': updated_info.get("email", ""),
                'avatar_url': updated_info.get("avatar_url"),
                'phone': updated_info.get("phone", ""),
                'birthdate': updated_info.get("birthdate", ""),
                'is_active': updated_info.get("is_active")
            })
            if result.rowcount == 0:
                raise ValueError(f"Employee with ID {id} not found.")
            session.commit()
