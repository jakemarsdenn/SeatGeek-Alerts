from flask import Flask, render_template, request, session, redirect
from account import valid_account, valid_credentials, get_name
from events import get_events, get_event
from main import track_event, save_event


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


@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html', session=session)


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
        event_id = request.form.get('inputField')
        event = get_event(event_id)
    return render_template('tracking.html', session=session, event=event)


@app.route('/track', methods=['POST'])
def track():
    event_id = request.form.get('eventID')
    track_event(event_id, session["email"])
    return "success"


@app.route('/save', methods=['POST'])
def save():
    event_id = request.form.get('eventID')
    save_event(event_id, session["email"])
    return "success"


if __name__ == '__main__':
    app.run(debug=True)