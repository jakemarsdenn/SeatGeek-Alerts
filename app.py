from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_for_event', methods=['POST'])
def search_for_event():
    event_name = request.form.get('inputField')
    # top_events = get_events_js(event_name)
    return render_template('events.html', event_name=event_name)
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