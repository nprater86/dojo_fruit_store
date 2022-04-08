from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count = 0
    for key, value in request.form.items():
        if key == 'apple' or key == 'strawberry' or key == 'raspberry':
            count += int(value)
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {count} fruits")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    