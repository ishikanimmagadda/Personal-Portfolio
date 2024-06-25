from flask import Flask, request, render_template

app = Flask(__name__) 
    
@app.route("/") 
def index(): 
    return "Homepage for Ishika"

@app.route("/about") 
def about(): 
    return "Hello, Welcome to the About Page"
  

@app.route("/projects") 
def projects(): 
    return "Hello, Welcome to the Projects Page"
  

@app.route("/contact", methods =["GET"] ) 
def contact(): 
    if request.method == 'GET':
        if(request.args.get('email') == None):
            return render_template('contact.html')
        elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid email</h1></body></html>"
        else:
            email = request.args.get('email')
            return render_template('answer.html', 
                                   email = email)


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    email = request.form.get('email')
    if email:
        return f"Hello, Welcome to the Contact Page. We will reach out to {email} soon!"
    else:
        return "No email provided."
    

if __name__ == "__main__": 
    app.run(debug=True) 