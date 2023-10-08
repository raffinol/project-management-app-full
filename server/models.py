from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise Exception("Cannot access password hashes")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8)"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    def __repr__(self):
        return f"User {self.username}. ID: {self.id}"


class Project(db.Model, SerializerMixin):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(150))
    start_date = db.Column()
    due_date = db.Column()
    urgency = db.Column(db.String(10))

    def __repr__(self):
        return (
            f"\n<project "
            + f"id={self.id}, "
            + f"title={self.title}, "
            + f"description={self.description}, "
            + f"start_date={self.start_date}, "
            + f"due_date={self.due_date}, "
            + f"urgency={self.urgency}, "
            + " >"
        )
