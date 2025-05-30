from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, insert_contact

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Initialize DB once on startup
init_db()

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/service')
def service():
    return render_template('service.html', active_page='service')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to database
        insert_contact(name, email, message)

        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True)
