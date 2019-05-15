from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    userpassword = request.form.get("userpassword")
    return render_template('login.html', username=username, userpassword=userpassword)

if __name__ == '__main__':
    app.run(debug=True)
