from flask import Flask , request
from operations import add , sub, div, mult

app = Flask(__name__)

math = {"add":add , "sub":sub , "mult":mult , "div":div}



@app.route("/math/<operation>")
def math_operations(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    func = math[operation]
    answer  =  func(a,b)
    return f'<h1>{answer}</h1>'



