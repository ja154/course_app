from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Render the single combined HTML page for the homepage
    # Ensure 'index_combined.html' is in your 'templates' folder
    return render_template('index_combined.html')

# The /ai and /tech routes are no longer needed as content is consolidated
# into index_combined.html and accessed via internal links.
# You can remove them or keep them commented out if you anticipate
# needing them for other purposes in the future.
# @app.route('/ai')
# def ai():
#     return render_template('ai.html')

# @app.route('/tech')
# def tech():
#     return render_template('tech.html')

if __name__ == '__main__':
    app.run(debug=True)
