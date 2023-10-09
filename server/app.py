#!/usr/bin/env python3

from flask import request, session, make_response
from flask_restful import Resource

from config import app, db, api

from models import User, Project


class Signup(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get("password")

        user = User(username=username)
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        print(user.to_dict())
        return user.to_dict(), 201


class CheckSession(Resource):
    def get(self):
        if session.get("user_id"):
            user = User.query.filter(User.id == session["user_id"]).first()
            return user.to_dict(), 200


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


class Logout(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None
            return {}, 204


class Projects(Resource):
    def get(self):
        projects = []
        for project in Project.query.all():
            project_dict = {
                "title": project.title,
                "description": project.description,
                "start_date": project.start_date,
                "due_date": project.due_date,
                "urgency": project.urgency,
            }
            projects.append(project_dict)
        response = make_response(projects, 200)

        return response


api.add_resource(Signup, "/signup", endpoint="signup")
api.add_resource(CheckSession, "/check_session", endpoint="check_session")
api.add_resource(Login, "/login", endpoint="login")
api.add_resource(Logout, "/logout", endpoint="logout")
api.add_resource(Projects, "/projects", endpoint="projects")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
