from app import db, Users

db.drop_all()
db.create_all()


user_1 = Users(first_name='Jalal', last_name="Saadat")
db.session.add(user_1)
db.session.commit()