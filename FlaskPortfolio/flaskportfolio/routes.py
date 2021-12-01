from datetime import datetime
from enum import unique
from flask import Flask, flash, redirect, url_for, render_template, request, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flaskportfolio import app, db
from flaskportfolio.models import Message
from flaskportfolio.forms import MessageForm


@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About Me")

@app.route("/services")
def services():
    return render_template("services.html", title="My Services")

@app.route("/skills")
def skills():
    return render_template("skills.html", title="My Skills")

@app.route("/reach-out", methods=['POST', 'GET'])
def contact():
    form = MessageForm()
    if form.validate_on_submit(): 
        message = Message(email=form.email.data, subject=form.subject.data, company=form.company.data, message=form.message.data)
        db.session.add(message)
        db.session.commit()
        flash(f'Your message has been submitted, thank you {form.email.data}', 'success')
        return redirect(url_for('home'))
          
    return render_template("contact.html", title="Contact Me", form=form)