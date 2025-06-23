from app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()
    
    g1 = Guest(name="eliud kipchoge", occupation="marathon runner")
    g2 = Guest(name="maxwell kiplagat", occupation="software developer")
    
    e1 = Episode(date=date(2023, 4, 20), number=101)
    e2 = Episode(date=date(2023, 4, 21), number=102)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()
    print("Smooth as butter ")
