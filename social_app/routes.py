
import os
# from PIL import Image
from pathlib import Path
from social_app import app, db
from social_app.forms import ContactForm
from social_app.models import User, Post
from flask import url_for, render_template, redirect, flash, abort, request
from flask_sqlalchemy import Pagination
from sqlalchemy import func
# from essential_generators import DocumentGenerator

# main route. layout.html is used for the general skeleton of all pages.
@app.route('/')
def home():
    title = "Photography Portfolio"


    return render_template('home.html', title=title)


@app.route('/contact')
def contact():
    title = "Contact"
    about_sections = {"use": "This is a blog photo gallery combo",
                      "pages": ["Account", "Blog", "Gallery"],
                      "info": "I am the creator Eli"}


    return render_template('contact.html', title=title, 
                           about_sections=about_sections)


@app.route('/faqs')
def faqs():
    title = "FAQs"
    faq_sections = {"use": "This is a blog photo gallery combo",
                      "search": ["Account", "Blog", "Gallery"],
                      "categories": "I am the creator Eli"}


    return render_template('faqs.html', title=title, 
                           faq_sections=faq_sections)


@app.route('/messages')
def messages():
    title = "Messages"

    return render_template('messages.html', title=title)


@app.route('/explore')
def explore():
    title = "Explore"

    return render_template('explore.html', title=title)


@app.route('/notifications')
def notifications():
    title = "Notifications"

    return render_template('notifications.html', title=title)


@app.route('/profile')
def profile():
    title = "Profile"

    return render_template('profile.html', title=title)


@app.route('/stories')
def stories():
    title = "Stories"

    return render_template('stories.html', title=title)
