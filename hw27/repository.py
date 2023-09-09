import pony
from pony.orm import db_session, select

from hw27.models import Title, Employee, Project


class TitleRepo:
    def __init__(self):
        self.model = Title

    @db_session
    def create(self, name):
        self.model(name=name)

    @db_session
    def update_name_by_id(self, id, new_name):
        title = self.model.get(lambda t: t.id == id)
        if title:
            title.name = new_name

    @db_session
    def delete_by_id(self, id):
        title = self.model.get(lambda t: t.id == id)
        if title:
            title.delete()

    @db_session
    def get_by_id(self, id):
        title = self.model.get(lambda t: t.id == id)
        return title

    @db_session
    def get_all(self):
        titles = self.model.select(lambda t: t).page(1).to_list()
        return titles


class EmployeeRepo:
    def __init__(self):
        self.model = Employee

    @db_session
    def create(self, first_name, last_name, years_of_experience, title_id):
        title = Title.get(id=title_id)
        self.model(first_name=first_name, last_name=last_name, years_of_experience=years_of_experience, title_id=title)

    @db_session
    def update_name_by_id(self, id, new_first_name, new_last_name):
        employee = self.model.get(lambda e: e.id == id)
        if employee:
            employee.first_name = new_first_name
            employee.last_name = new_last_name

    @db_session
    def delete_by_id(self, id):
        employee = self.model.get(lambda e: e.id == id)
        if employee:
            employee.delete()

    @db_session
    def get_by_id(self, id):
        employee = self.model.get(lambda e: e.id == id)
        return employee

    @db_session
    def get_all(self):
        employees = self.model.select(lambda e: e).page(1).to_list()
        return employees


class ProjectRepo:
    def __init__(self):
        self.model = Project

    @db_session
    def create(self, name, time, employee_id):
        self.model(name=name, time=time, employee_id=employee_id)

    @db_session
    def update_name_by_id(self, id, new_name):
        project = self.model.get(lambda p: p.id == id)
        if project:
            project.name = new_name

    @db_session
    def delete_by_id(self, id):
        project = self.model.get(lambda p: p.id == id)
        if project:
            project.delete()

    @db_session
    def get_by_id(self, id):
        project = self.model.get(lambda p: p.id == id)
        return project

    @db_session
    def get_all(self):
        project = self.model.select(lambda p: p).page(1).to_list()
        return project


if __name__ == '__main__':
    # Examples of creating titles, employees, and projects
    title_repo = TitleRepo()
    employee_repo = EmployeeRepo()
    project_repo = ProjectRepo()

    #Create Titles
    # title_repo.create("CTO")
    # titles = title_repo.get_all()
    # for title in titles:
    #     print(title)

    # Create Employees
    # titles = title_repo.get_all()
    # for title in titles:
    #     print(title)
    #     if title.name == "CTO":
    #         position_id = title.id
    #         print(position_id)
    # employee_repo.create("Sergiy", "Nimchinskii", 10, position_id)
    #
    #
    # employees = employee_repo.get_all()
    # for employee in employees:
    #     print(employee)
    #
    # # Create Projects
    try:
        project_repo.create("New ERP project", 8, 19)
        print("Project created successfully.")
    except pony.orm.core.TransactionIntegrityError as e:
        if "Key (employee_id)=" in str(e) and "is not present in table \"employees\"" in str(e):
            print("Error: Employee with the specified ID does not exist.")
        else:
            # Handle other types of integrity errors
            print(
                "Error: Failed to create the project due to an integrity error.")
    projects = project_repo.get_all()
    for project in projects:
        print(project)
