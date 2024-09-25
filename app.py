from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

def verify_captcha(captcha_response):
    secret_key = "6Lfat04qAAAAABETh5dbSYePXO6_ck6lFdr8EIu5"
    verification_url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {'secret': secret_key, 'response': captcha_response}
    response = requests.post(verification_url, data=payload)
    return response.json().get('success', False)

@app.route('/')
def home():
    # Render the form with reCAPTCHA
    return render_template_string('html2.0.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Get form data
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Get the reCAPTCHA response from the form
    captcha_response = request.form.get('g-recaptcha-response')

    # Verify the reCAPTCHA response
    if not captcha_response or not verify_captcha(captcha_response):
        return "Captcha validation failed. Please try again.", 400

    # Proceed with the form submission process if captcha is valid
    return f"Form submitted successfully! Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)
