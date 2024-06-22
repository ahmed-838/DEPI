from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    mobile = request.form['mobile']
    password = request.form['password']
    if not username or not mobile or not password:
        return "This field is required", 400

    if not mobile.isdigit() or len(mobile) != 10:
        return "Invalid mobile number", 400

    # Save user data to a file
    with open('user_data.txt', 'a') as file:
        file.write(f"Username: {username}, Mobile: {mobile}, Password: {password}\n")

    return f"Sign up successful! \n welcome : {username}"


if __name__ == '__main__':
    app.run(debug=True)
