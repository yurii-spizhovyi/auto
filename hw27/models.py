from pony.orm import Database, PrimaryKey, Required, Set, Optional

db = Database()
db.bind(provider="postgres", user="postgres", password='123', host='127.0.0.1', database='hw27')


class Title(db.Entity):
    _table_ = 'titles'
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    employees = Set("Employee")

    def __str__(self):
        return f"Id: {self.id}, Position: {self.name}"

    def __repr__(self):
        return f"Id: {self.id}, Position: {self.name}"


class Employee(db.Entity):
    _table_ = 'employees'
    id = PrimaryKey(int, auto=True)
    first_name = Required(str, 100)
    last_name = Required(str, 100)
    years_of_experience = Required(int)
    projects = Set("Project")
    title_id = Required(Title)

    def __str__(self):
        return f"Id: {self.id}, FirstName: {self.first_name}, LastName: {self.last_name}, YearsOfExp: {self.years_of_experience}"

    def __repr__(self):
        return f"Id: {self.id}, FirstName: {self.first_name}, LastName: {self.last_name}, YearsOfExp: {self.years_of_experience}"


class Project(db.Entity):
    _table_ = 'projects'
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    time = Required(int)
    # employees = Set(Employee)
    employee_id = Required(Employee)  # Foreign key to Employee


db.generate_mapping(create_tables=True)
