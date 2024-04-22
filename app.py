from flask import Flask, render_template, request, session, redirect
from account import valid_account, valid_credentials, get_name
from events import get_events


app = Flask(__name__)
app.secret_key = 'secret_key'
session = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', session=session)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', session=session)


@app.route('/confirm_login', methods=['POST'])
def confirm_login():
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


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect("/")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', session=session)


@app.route('/confirm_signup', methods=['POST'])
def confirm_signup():
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


@app.route('/about', methods=['POST'])
def about():
    return render_template('about.html', session=session)


@app.route('/profile', methods=['POST'])
def profile():
    return render_template('profile.html', session=session)


@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    return render_template('profile.html', session=session)


@app.route('/search_for_event', methods=['POST'])
def search_for_event():
    event_name = request.form.get('inputField')
    events = get_events(event_name)
    return render_template('events.html', session=session, event_name=event_name, events=events)


if __name__ == '__main__':
    app.run(debug=True)