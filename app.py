from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Set a password for login
PASSWORD = 'kader11000'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == PASSWORD:
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Incorrect password")
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cms_scan', methods=['POST'])
def cms_scan():
    target = request.form['target']
    cms = request.form['cms']
    os_type = request.form['os']

    if cms == "wordpress":
        tool = f"wpscan --url {target} --disable-tls-checks"
    elif cms == "joomla":
        tool = f"joomscan -u {target}"
    elif cms == "drupal":
        tool = f"droopescan scan drupal -u {target}"
    else:
        tool = "echo Unsupported CMS"

    try:
        result = subprocess.getoutput(tool)
    except Exception as e:
        result = f"Error running scan: {str(e)}"

    return f"[Target OS: {os_type}]\n[Tool Used: {tool}]\n\n{result}"

@app.route('/post_exploit', methods=['POST'])
def post_exploit():
    cmd = request.form['cmd']
    try:
        result = subprocess.getoutput(cmd)
    except Exception as e:
        result = f"Error: {str(e)}"
    return result

if __name__ == "__main__":
    app.run(debug=True)
