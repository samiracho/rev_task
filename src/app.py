import os
from flask import Flask, request
import psycopg2
from functions import *

url = os.environ.get("DATABASE_URL")
connection = psycopg2.connect(url)
app = Flask(__name__)

@app.get("/hello/<string:username>")
def get_user(username):
    """Get user from the DB and returns days left to birthday."""
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT birthday FROM users where username = %s;", (username,))
                row = cursor.fetchone()
                if row is None:
                    return {"message": "ERROR: "+username+" not found"}, 200
                today = datetime.now().date()
                days_left = days_to_birthday(today, row[0])
                if days_left != 0:
                    return {"message": "Hello, "+username+"! Your birthday is in "+str(days_left)+" day(s)"}, 200
                return {"message": "Hello, "+username+"! Happy birthday!"}, 200

    except Exception as exception:
        return {"message": "ERROR: Unexpected error "+str(exception)}, 409


@app.route("/hello/<string:username>", methods=["PUT"])
def hello_username(username):
    """Stores users in the DB."""
    try:
        if not username.isalpha():
            return {"message": "ERROR: Username should contain only letters"}, 409

        birth_date = request.json['dateOfBirth']
        today = datetime.now().date()
        if not check_date(today, birth_date):
            return {"status": "error","message": "dateOfBirth is wrong. Please make sure its valid, it has the format YYYY-MM-DD and it's before the today's date"}, 409

        with connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (username, birthday) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET birthday = EXCLUDED.birthday', (username, birth_date))
        return {}, 204
    except Exception as exception:
        return {"status": "error", "message": "ERROR: "+str(exception)}, 409
