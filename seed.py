"""Seed database with sample data from CSV Files."""

# from csv import DictReader
# from app import db
# from models import User, Message, Follows


# db.drop_all()
# db.create_all()

# with open('generator/users.csv') as users:
#     db.session.bulk_insert_mappings(User, DictReader(users))

# with open('generator/messages.csv') as messages:
#     db.session.bulk_insert_mappings(Message, DictReader(messages))

# with open('generator/follows.csv') as follows:
#     db.session.bulk_insert_mappings(Follows, DictReader(follows))

# db.session.commit()

from app import app, db
from models import User, Message, Follows
from csv import DictReader
import traceback



try:

    with app.app_context():
        db.drop_all()
        db.create_all()

        with open('generator/users.csv') as users:
            db.session.bulk_insert_mappings(User, DictReader(users))

        with open('generator/messages.csv') as messages:
            db.session.bulk_insert_mappings(Message, DictReader(messages))

        with open('generator/follows.csv') as follows:
            db.session.bulk_insert_mappings(Follows, DictReader(follows))

        db.session.commit()

        print("Database seeded successfully!")

except Exception as e:

    print(f"An error occurred: {str(e)}")

    print(traceback.format_exc())