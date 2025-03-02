from flask import Flask, request, jsonify, redirect, session
import requests
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Google OAuth credentials
GOOGLE_CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID'
GOOGLE_CLIENT_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:5000/verify-google-login'

@app.route('/verify-google-login', methods=['POST'])
def verify_google_login():
    id_token = request.json.get('idToken')

    # Verify the ID token with Google
    response = requests.post(
        'https://oauth2.googleapis.com/tokeninfo',
        params={ 'id_token': id_token }
    )

    if response.status_code == 200:
        user_info = response.json()
        if user_info.get('aud') == GOOGLE_CLIENT_ID:  # Verify the client ID
            # Store user info in session
            session['user'] = user_info
            return jsonify({ 'success': True })
    
    return jsonify({ 'success': False })

@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session
    session.pop('user', None)
    return jsonify({ 'success': True })

@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login.html')
    return redirect('/index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable if available
    app.run(host='0.0.0.0', port=port)  # Bind to 0.0.0.0
