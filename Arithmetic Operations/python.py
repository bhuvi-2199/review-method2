from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def main():
    if request.method == "POST": 
        a=int(request.form.get("a"))
        b=int(request.form.get("b"))
        op = request.form.get("op")
        if (op == '+'):
            ans = a+b
        elif (op == '-'):
            ans = a-b 
        elif (op == '*'):
            ans = a*b
        elif (op == '/'):
            ans = a/b 
        elif (op == '%'):
            ans = a % b
        else:
            ans = 'Invalid operation'
        return render_template("index.html",ans=ans)
    else:
        return render_template("index.html",ans='')
if __name__ == '__main__':
   app.run(debug = True)
   