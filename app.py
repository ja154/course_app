import os
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- CONFIGURATION ---
# Secret key is needed for flashing messages
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Flask-Mail configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS').lower() in ['true', '1', 't']
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Initialize Mail
mail = Mail(app)

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('tech.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')

        try:
            # Create the email message
            msg = Message(
                subject=f"New Contact Form Message: {subject}",
                recipients=[app.config['MAIL_USERNAME']],  # Send to yourself
                body=f"From: {name} <{email}>\n\n{message_body}"
            )
            # Send the email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred while sending the email. Please try again later.', 'danger')
            # For debugging, you might want to print the error
            # print(str(e))

        return redirect(url_for('contact'))

    # For GET request, just render the page
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
