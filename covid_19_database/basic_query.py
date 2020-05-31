import MySQLdb


def researcher_query(db, location):
	cursor = db.cursor()
	query = """Select researcher.first_name, researcher.last_name
		   From researcher, institution
		   Where researcher.institution_id = institution.institution_id and institution.location = "%s"
		"""%location
	cursor.execute(query)
	cursor.close()
	retrun cursor.fetchall()

	
def drug_query(db, name):
	cursor = db.cursor()
	query = """Select trial_id,trial_stage,trial_status
		   From trial_drug natural join clinical_trial as drugntrial
		   Where drug_id in(select drug_id
		   From drug
		   Where drug_name='%s')"""%name
	cursor.execute(query)
	cursor.close()
	return cursor.fetchall()


def age_query(db):
	cursor = db.cursor()
	query = """Select gender,avg(age)
		   From cases
		   Group by gender)"""
	cursor.execute(query)
	cursor.close()
	return cursor.fetchall()



def age_query(db):
	cursor = db.cursor()
	query = """Select gender,avg(age)
		   From cases
		   Group by gender)"""
	cursor.execute(query)
	cursor.close()
	return cursor.fetchall()


def case_query(db):
	cursor = db.cursor()
	query = """
		with site_suspected(site_id,suspected_case)
		as (select site_id,count(case_id)
		From cases
		where situation='suspected'
		Group by site_id),
		site_confirmed(site_id,confirmed_case)
		As (select site_id,count(case_id)
		From cases
		where situation='confirmed'
		Group by site_id),
		site_dead(site_id,dead_case)
		As (select site_id,count(case_id)
		From cases
			where situation='dead'
		Group by site_id)
		Select site_id,suspected_case,confirmed_case,dead_case
		From site_suspected natural join site_confirmed natural join site_dead
		"""
	cursor.execute(query)
	cursor.close()
	return cursor.fetchall()


def case_query(db):
	cursor = db.cursor()
	query = """
		with site_suspected(site_id,suspected_case)
		as (select site_id,count(case_id)
		From cases
		where situation='suspected'
		Group by site_id),
		site_confirmed(site_id,confirmed_case)
		As (select site_id,count(case_id)
		From cases
		where situation='confirmed'
		Group by site_id),
		site_dead(site_id,dead_case)
		As (select site_id,count(case_id)
		From cases
			where situation='dead'
		Group by site_id)
		Select site_id,suspected_case,confirmed_case,dead_case
		From site_suspected natural join site_confirmed natural join site_dead
		"""
	cursor.execute(query)
	cursor.close()
	return cursor.fetchall()

def volunteer_query(db):
	cursor = db.cursor()
	query = """
		With trial(trial_id)
		As(select trial_id
		From experiment	
		Where experiment.batch_id=1),
		trialndrug(trial_id,drug_name)
		As(select trial_id,drug_name
		From trial_drug natural join drug
		Where trial_id in 
  		(select * from trial)
  		),
		trialnvolunteer(trial_id,volunteer_num)
		As(select trial_id,count(volunteer_id)
		From volunteer_experiment
		Group by trial_id
		Having trial_id in 
  		(select * from trial)
 		 )
		Select *
		From trialndrug natural join trialnvolunteer
		"""
	cursor.execute(query)
	cursor.close()
	return cursor.fetchall()
