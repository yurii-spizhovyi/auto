from sqlalchemy import Date  # Import the Date type

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class StudentModel(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    enrollments = relationship('EnrollmentModel', back_populates='student')

    def __repr__(self):
        return f"Id - {self.id}  Name - {self.name}, Enrollments - {self.enrollments}"


class CourseModel(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    instructor = Column(String(100), nullable=False)
    enrollments = relationship('EnrollmentModel', back_populates='course')

    def __repr__(self):
        return f"Id - {self.id}  Title - {self.title}  Instructor - {self.instructor}, Enrollments - {self.enrollments}"


class EnrollmentModel(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    enrollment_date = Column(Date)
    student = relationship('StudentModel', back_populates='enrollments')
    course = relationship('CourseModel', back_populates='enrollments')

    def __repr__(self):
        return f"Id - {self.id}  Student - {self.student.name}  Course - {self.course.title}  Date - {self.enrollment_date}"


engine = create_engine("postgresql://admin:admin@localhost:5432/hw26")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student1 = StudentModel(name='Alice')
student2 = StudentModel(name='Bob')

course1 = CourseModel(title='Math', instructor='Dr. Smith')
course2 = CourseModel(title='History', instructor='Prof. Johnson')

enrollment1 = EnrollmentModel(student=student1, course=course1, enrollment_date='2023-08-29')
enrollment2 = EnrollmentModel(student=student1, course=course2, enrollment_date='2023-08-30')
enrollment3 = EnrollmentModel(student=student2, course=course1, enrollment_date='2023-08-30')

session.add_all([student1, student2, course1, course2, enrollment1, enrollment2, enrollment3])
session.commit()

enrollments = session.query(EnrollmentModel).all()
for enrollment in enrollments:
    print(
        f"Student: {enrollment.student.name}, "
        f"Course: {enrollment.course.title}, "
        f"Enrollment Date: {enrollment.enrollment_date}"
    )
