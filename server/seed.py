#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Engineers, Project
from random import choice as random

if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        User.query.delete()
        db.session.query(Engineers).delete()
        db.session.query(Project).delete()

        levels = ["junior", "mid", "senior"]
        for _ in range(5):
            first_name = fake.first_name()
            last_name = fake.last_name()
            engineer = Engineers(
                name=first_name, last_name=last_name, level=random(levels)
            )
            db.session.add(engineer)
            db.session.commit()

        urgency = ["high", "medium", "low"]
        for _ in range(10):
            title = fake.text(max_nb_chars=50)
            description = fake.text(max_nb_chars=150)
            start_date = fake.past_date()
            due_date = fake.future_date()
            engineer_id = fake.random_int(min=1, max=5)
            project = Project(
                title=title,
                description=description,
                start_date=start_date,
                due_date=due_date,
                urgency=random(urgency),
                engineer_id=engineer_id,
            )
            db.session.add(project)

        db.session.commit()
