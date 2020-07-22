from .model.user import User

from .model.base import session_factory

class User_Dao():
    
	# Read all employees.
	def query_records(self, session):
		# session = session_factory()
		users_query = session.query(User)
		# session.close()
		return users_query.all()

	def create_record(self, session, user: User):
		# session = session_factory()
		session.add(employee)
		session.commit()
		# session.close()

	def update_record(self, session, user: User):
		# session = session_factory()
		session.add(user)
		session.commit()
		# session.close()

	def delete_record(self, session, user: User):
		# session = session_factory()
		session.delete(user)
		session.commit()
		# session.close()
