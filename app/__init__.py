"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaahhm7avj5o48uktjg-a.oregon-postgres.render.com",
        database="todo_kzwn",
        user="todo_kzwn_user",
        password="edywqAC4XDZmYA5gCEPwBzsGYbV7Oyrw")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
