from .model.in_out_time import InOutTime

from .model.base import session_factory

class InOutTime_Dao():

	# Read all employees.
	def query_records(self, session):
	    # session = session_factory()
	    inouttime_query = session.query(InOutTime)
	    # session.close()
	    return inouttime_query.all()

	def create_record(self, session, inouttime: InOutTime):
	    # session = session_factory()
	    session.add(inouttime)
	    session.commit()
	    # session.close()

	def update_record(self, session, inouttime: InOutTime):
		# session = session_factory()
		session.add(inouttime)
		session.commit()
		# session.close()

	def delete_record(self, session, inouttime: InOutTime):
	    # session = session_factory()
	    session.delete(inouttime)
	    session.commit()
	    # session.close()
