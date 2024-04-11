from flask import Flask, render_template, request, session, redirect
from account import valid_account, valid_credentials


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
        if valid_credentials(session["email"], session["password"]):
            session["logged_in"] = True
            return redirect("/")
        else:
            session["error"] = "Account not found. Please try again."
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
            session["error"] = "Invalid email address. Please try again."
            return redirect("/signup")


@app.route('/about', methods=['POST'])
def about():
    return render_template('about.html', session=session)


@app.route('/profile', methods=['POST'])
def profile():
    return render_template('profile.html', session=session)


@app.route('/search_for_event', methods=['POST'])
def search_for_event():
    event_name = request.form.get('inputField')
    # top_events = get_events_js(event_name)
    return render_template('events.html', session=session, event_name=event_name)
    # return render_template('events.html', event_name=event_name, top_events=top_events)


def get_events_js(event_name):
    return None
    # script_path = 'static/js/script.js'
    # if os.path.exists(script_path):
    #     with open(script_path, 'r') as f:
    #         js_code = f.read()
    #         print("JavaScript file located successfully.")


if __name__ == '__main__':
    app.run(debug=True)