#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api

# Add your model imports
from models import User


# Views go here!


class Signup(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get("password")

        user = User(username=username)
        user.password_hash = password

        try:
            db.session.add(user)
            db.session.commit()

            session["user_id"] = user.id
            print(user.to_dict())
            return user.to_dict(), 201
        except IntegrityError as e:
            errors = []

            required_keys = ["username", "password", "password_confirmation"]

            for key in required_keys:
                if not request_json[key]:
                    errors.append(f"{key} is required")

            if request_json["username"] != request_json["password_confirmation"]:
                errors.append("Password  confirmation failed")

            if isinstance(e, (IntegrityError)):
                for error in e.orig.args:
                    errors.append(str(error))

            return {"errors": errors}, 422


class CheckSession(Resource):
    def get(self):
        if session.get("user_id"):
            user = User.query.filter(User.id == session["user_id"]).first()
            return user.to_dict(), 200
        return {"error": "401 Unauthorized"}, 204


class Login(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get("password")

        user = User.query.filter(User.username == username).first()

        if user:
            if user.authenticate(password):
                session["user_id"] = user.id
                return user.to_dict(), 200

        return {"error": "401 Unauthorized"}, 401


class Logout(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None

            return {}, 204

        return {"error": "401 Unauthorized"}, 401


api.add_resource(Signup, "/signup", endpoint="signup")
api.add_resource(CheckSession, "/check_session", endpoint="check_session")
api.add_resource(Login, "/login", endpoint="login")
api.add_resource(Logout, "/logout", endpoint="logout")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
