from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Let's make the tech page the homepage for this example
    return render_template('tech.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

# Add other routes as needed (dashboard, courses, etc.)

if __name__ == '__main__':
    app.run(debug=True)