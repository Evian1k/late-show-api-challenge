from server.extensions import db
from server.app import app
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Users
        user = User(username='admin')
        user.set_password('password')
        db.session.add(user)

        # Guests
        guest1 = Guest(name='Tom Hanks', occupation='Actor')
        guest2 = Guest(name='Taylor Swift', occupation='Singer')
        db.session.add_all([guest1, guest2])

        # Episodes
        episode1 = Episode(date=date(2025, 6, 1), number=1)
        episode2 = Episode(date=date(2025, 6, 2), number=2)
        db.session.add_all([episode1, episode2])

        db.session.commit()

        # Appearances
        appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
        db.session.add_all([appearance1, appearance2])
        db.session.commit()

if __name__ == "__main__":
    seed()
    print("Database seeded!")
