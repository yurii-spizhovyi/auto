from sqlalchemy import update
from hw26.alchemy.models.models import StudentModel, CourseModel, EnrollmentModel  # Import your models
from hw26.alchemy.session import session  # Import your session


class EnrollmentRepository:
    def __init__(self):
        self.__session = session
        self.__model = EnrollmentModel

    def get_all(self):
        enrollments = self.__session.query(self.__model).all()
        return enrollments

    def get_by_id(self, enrollment_id: int):
        enrollment = self.__session.query(self.__model).filter_by(id=enrollment_id).first()
        return enrollment

    def create_new(self, enrollment_model):
        try:
            self.__session.add(enrollment_model)
            return True
        except:
            return False

    def delete(self, enrollment_id):
        try:
            enrollment = self.get_by_id(enrollment_id)
            self.__session.delete(enrollment)
            return True
        except:
            return False

    def update(self, enrollment_id, enrollment_date):
        enrollment = self.get_by_id(enrollment_id)
        enrollment.enrollment_date = enrollment_date
        self.__session.commit()


if __name__ == "__main__":
    repo = EnrollmentRepository()
    student1 = StudentModel(name='Alice')
    course1 = CourseModel(title='Math', instructor='Dr. Smith')
    # Create a new enrollment
    #new_enrollment = EnrollmentModel(student_id=student1, course_id=course1, enrollment_date="2023-08-30")
    #repo.create_new(new_enrollment)

    # Update an enrollment
    # repo.update(enrollment_id=1, enrollment_date="2023-08-30")

    # Delete an enrollment
    # repo.delete(enrollment_id=2)

    # Retrieve all enrollments
    enrollments = repo.get_all()
    for enrollment in enrollments:
        print(
            f"Enrollment ID: {enrollment.id}, "
            f"Student ID: {enrollment.student_id}, "
            f"Course ID: {enrollment.course_id}, "
            f"Enrollment Date: {enrollment.enrollment_date}"
        )
