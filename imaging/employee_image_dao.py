from .model.employee_image import EmployeeImage

from .model.base import session_factory


class EmployeeImage_Dao:

    # Read all employees.
    def query_records(self, session):
        # session = session_factory()
        images_query = session.query(EmployeeImage)
        # session.close()
        return images_query.all()

    def create_record(self, session, EmployeeImage: EmployeeImage):
        # session = session_factory()
        session.add(EmployeeImage)
        session.commit()
        # session.close()

    def update_record(self, session, EmployeeImage: EmployeeImage):
        # session = session_factory()
        session.add(EmployeeImage)
        session.commit()
        # session.close()

    def delete_record(self, session, employeeImage: EmployeeImage):
        # session = session_factory()
        session.delete(EmployeeImage)
        session.commit()
        # session.close()
