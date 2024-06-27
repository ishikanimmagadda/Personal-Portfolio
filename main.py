
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/") 
def index(): 
    return render_template('home.html')

@app.route("/about") 
def about(): 
    return render_template('about.html')
  

@app.route("/projects") 
def projects(): 
    return render_template('projects.html')
  

@app.route("/contact", methods =["GET"] ) 
def contact(): 
    return render_template('contact.html')

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    email = request.form.get('email')
    if email:
        new_contact = Contact(email=email)
        try: 
            db.session.add(new_contact)
            db.session.commit()
            return f"Hello, Welcome to the Contact Page. I will reach out to {email} soon!"
        except IntegrityError:
            db.session.rollback()
            return f"This email {email} has already been added!"
    else:
        return "No email provided."

if __name__ == "__main__": 
    with app.app_context():
        db.create_all()
    app.run(debug=True)     