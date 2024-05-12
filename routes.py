from flask import Flask, render_template, request, session, redirect
from account import *
from events import *
from main import *


app = Flask(__name__)
app.secret_key = 'secret_key'
session = {}


@app.route('/')
def index():
    return render_template('index.html', session=session)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session["email"] = request.form["email"]
        session["password"] = request.form["password"]
        session["name"] = get_name(session["email"])

        if valid_credentials(session["email"], session["password"]):
            session["logged_in"] = True
            return redirect("/")

        else:
            session["login_error"] = True
            return redirect("/login")

    return render_template('login.html', session=session)


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect("/")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["email"] = request.form["email"]
        session["password"] = request.form["password"]

        if valid_account(session["name"], session["email"], session["password"]):
            session["logged_in"] = True
            return redirect("/")

        else:
            session["signup_error"] = True
            return redirect("/signup")

    return render_template('signup.html', session=session)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', session=session)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    tracked_events = get_users_events()

    if request.method == 'POST':
        action_type = request.form.get('action_type')

        if action_type == 'edit-name':
            new_name = request.form.get('name')
            edit_name(new_name, session["email"])
            session["name"] = new_name

        elif action_type == 'edit-password':
            new_password = request.form.get('password')
            edit_password(new_password, session["email"])
            session["password"] = new_password

        elif action_type == 'delete-tracked-event':
            event_id = request.form.get('event_id')
            untrack_event(event_id, session["email"])
            tracked_events = get_users_events()

    return render_template('profile.html', tracked_events=tracked_events, session=session)


def get_users_events():
    tracked_event_ids = get_tracked_events(session["email"])
    tracked_events = []
    for eventID in tracked_event_ids:
        tracked_events.append(get_event(eventID))
    return tracked_events


@app.route('/events', methods=['POST'])
def search_for_event():
    event_name = request.form.get('inputField')
    events = get_events(event_name)
    return render_template('events.html', session=session, event_name=event_name, events=events)


@app.route('/help', methods=['GET'])
def help():
    return render_template('help.html', session=session)


@app.route('/tracking', methods=['GET', 'POST'])
def tracking():
    event = None
    if request.method == 'POST':
        action_type = request.form.get('action_type')

        if action_type == 'search':
            digit1 = request.form.get('digit1')
            digit2 = request.form.get('digit2')
            digit3 = request.form.get('digit3')
            digit4 = request.form.get('digit4')
            digit5 = request.form.get('digit5')
            digit6 = request.form.get('digit6')
            digit7 = request.form.get('digit7')
            event_id = f"{digit1}{digit2}{digit3}{digit4}{digit5}{digit6}{digit7}"
            event = get_event(event_id)

        elif action_type == 'track':
            event_id = request.form.get('eventID')
            track_event(event_id, session["email"])

    return render_template('tracking.html', session=session, event=event)