from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # This renders the HTML page containing your dashboard
    return render_template('index.html')


if __name__ == '__main__':
    # Runs the server in debug mode so you can see changes instantly
    app.run(debug=True, port=5000)