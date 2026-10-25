from flask import Flask


# Creating an obj out of the flask class    

app = Flask(__name__)

# using decorator for Creating the path of my application
@app.route('/')
def home():  #creating home page
    return "Hello This is Flask Application.. Practice for CI CD task"

#calling main function
if __name__ == "__main__":
    app.run(debug=True)