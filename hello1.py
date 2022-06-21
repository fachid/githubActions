from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    print(request.headers)
    print(request.headers)
    
    aws_token = "aaeea383-d591-4640-89b7-5e7c798878bd"
    
    vessel_secret="asdlkjadkasd"
    
    return "Hello World!!!!"

if __name__ == "__main__":
    app.run()
