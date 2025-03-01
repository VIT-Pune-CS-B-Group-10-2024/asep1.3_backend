from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Hardcoded user credentials (for demonstration purposes)
USER_CREDENTIALS = {
    "username": "user",
    "password": "password"
}

# Session management (for demonstration purposes)
logged_in = False

@app.route('/login', methods=['POST'])
def login():
    global logged_in
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        logged_in = True
        return jsonify({ 'success': True })
    else:
        return jsonify({ 'success': False })

@app.route('/logout', methods=['POST'])
def logout():
    global logged_in
    logged_in = False
    return jsonify({ 'success': True })

@app.route('/')
def home():
    if not logged_in:
        return redirect('/login.html')
    return redirect('/index.html')

if __name__ == '__main__':
    app.run(debug=True)