from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_for_event', methods=['POST'])
def search_for_event():
    event_name = request.form.get('inputField')
    return render_template('events.html', event_name=event_name)

if __name__ == '__main__':
    app.run(debug=True)