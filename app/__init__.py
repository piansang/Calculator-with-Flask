from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

from app import routes
