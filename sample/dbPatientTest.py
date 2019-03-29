from perionet.dbPatient import Patient

p1 = Patient(nameLast='Doe', nameFirst='John', nameDob='03/03/1970')
db.session.add(p1)
p2 = Patient(nameLast='Doe', nameFirst='John', nameDob='03/03/1970')
db.session.add(p2)
db.session.commit()
