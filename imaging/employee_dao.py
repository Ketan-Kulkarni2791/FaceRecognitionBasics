from .model.employee import Employee

from .model.base import session_factory

class Employee_Dao():
	
	# Read all employees.
	def query_records(self, session):
		# session = session_factory()
		employee_query = session.query(Employee)
		# session.close()
		return employee_query.all()

	def create_record(self, session, employee: Employee):
		# session = session_factory()
		session.add(employee)
		session.commit()
		# session.close()

	def update_record(self, session, employee: Employee):
		# session = session_factory()
		session.add(employee)
		session.commit()
		# session.close()

	def delete_record(self, session, employee: Employee):
		# session = session_factory()
		session.delete(employee)
		session.commit()
		# session.close()

	def query_by_code(self, session, empcode):
		# session = session_factory()
		employee = session.query(Employee).filter_by(code=empcode).first()
		# session.close()
		return employee

	def query_by_id(self, session, id):
		# session = session_factory()
		employee = session.query(Employee).filter_by(id=id).first()
		# session.close()
		return employee

