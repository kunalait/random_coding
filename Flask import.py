from flask import Flask,render_template,redirect,url_for

app=Flask(__name__)

@app.route('/admin')
def home_page():
    return 'hello admin'
@app.route('/guest/<guest>')
def normal_user(guest):
    return guest
@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))


if __name__=='__main__':
    app.run(debug=True)