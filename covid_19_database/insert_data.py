import MySQLdb

def insert_site(db, site_id, country, province, city, other_details):
  cursor = db.cursor()
  insert = """
           insert into site(site_id, country, province, city, other_details)
           values (%i, "%s", "%s", "%s", "%s")"""%(site_id, country, province, city, other_details)
  try:
    cursor.execute(insert)
    db.commit()
    print("insert confirmed")
  except:
    db.rollback()
    print("error, something wrong!")

