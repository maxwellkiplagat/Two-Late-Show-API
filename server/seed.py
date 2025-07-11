import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.user import User
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()
    
    g1 = Guest(name="eliud kipchoge", occupation="marathon runner")
    g2 = Guest(name="maxwell kiplagat", occupation="software developer")
    
    e1 = Episode(date=date(2023, 4, 20), number=101)
    e2 = Episode(date=date(2023, 4, 21), number=102)

    u1 = User(username="admin")
    u1.set_password("password123")

    db.session.add_all([g1, g2, e1, e2, u1])
    db.session.commit()

    print("Smooth as butter!")
