from flask import Flask 

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
  

@app.route("/contact") 
def contact(): 
    return "Hello, Welcome to the Contact Page"
  
if __name__ == "__main__": 
    app.run(debug=True) 