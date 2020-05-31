import MySQLdb


def insert_site(db, site_id, country, province, city, other_details):
    cursor = db.cursor()
    insert = """
           insert into site(site_id, country, province, city, other_details)
           values (%i, "%s", "%s", "%s", "%s")"""%(site_id, country, province, city, other_details)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - site")
    except:
        db.rollback()
        print("error, something wrong! - site")


def insert_drug(db, drug_id, drug_name, drug_status, drug_type):
    cursor = db.cursor()
    insert = """
            insert into drug(drug_id, drug_name, drug_status, drug_type):
            values (%i, "%s", "%s", "%s")
             """%(drug_id, drug_name, drug_status, drug_type)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - drug")
    except:
        dn.rollback()
        print("error, something wrong - drug")

def insert_clinical_trial(db, trial_id, title, trial_type, trial_stage, trial_status, record_date, start_date, end_date, bid_institution, trial_institution):
    cursor = db.cursor()
    insert = """
            insert into clinical_trial(trial_id, title, trial_type, trial_stage, trial_status, record_date, start_date, end_date, bid_institution, trial_institution):
            values (%i, "%s", "%s", "%s", "%s", %s, %s, %s, "%s", "%s")
             """%(trial_id, title, trial_type, trial_stage, trial_status, record_date, start_date, end_date, bid_institution, trial_institution)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - clinical_trial")
    except:
        dn.rollback()
        print("error, something wrong - clinical_trial")

def insert_trail_drug(db, trial_id, drug_id):
    cursor = db.cursor()
    insert = """
            insert into trial_drug(trial_id, drug_id):
            values (%i, %i)
             """%(trial_id, drug_id)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - trial_drug")
    except:
        dn.rollback()
        print("error, something wrong - trial_drug")


def insert_researcher(db, researcher_id, first_name, last_name, position, email, phonenumber, department):
    cursor = db.cursor()
    insert = """
            insert into researcher(researcher_id, first_name, last_name, position, email, phonenumber, department):
            values (%i, "%s", "%s", "%s", "%s", "%s", "%s")
             """%(researcher_id, first_name, last_name, position, email, phonenumber, department)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - researcher")
    except:
        dn.rollback()
        print("error, something wrong - researcher")


def insert_researcher(db, institution_id, researcher_id, first_name, last_name, position, email, phonenumber, department):
    cursor = db.cursor()
    insert = """
            insert into researcher(institution_id, researcher_id, first_name, last_name, position, email, phonenumber, department):
            values (%i, %i, "%s", "%s", "%s", "%s", "%s", "%s")
             """%(institution_id, researcher_id, first_name, last_name, position, email, phonenumber, department)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - researcher")
    except:
        db.rollback()
        print("error, something wrong - researcher")


def insert_researcher(db, institution_id, researcher_id, first_name, last_name, position, email, phonenumber, department):
    cursor = db.cursor()
    insert = """
            insert into researcher(institution_id, researcher_id, first_name, last_name, position, email, phonenumber, department):
            values (%i, %i, "%s", "%s", "%s", "%s", "%s", "%s")
             """%(institution_id, researcher_id, first_name, last_name, position, email, phonenumber, department)
    try:
        cursor.execute(insert)
        db.commit()
        print("insert confirmed - researcher")
    except:
        db.rollback()
        print("error, something wrong - researcher")

