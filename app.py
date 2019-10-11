from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle = 'Loan Calculator')

@app.route('/calculate', methods=['GET', 'POST'])
def loan():
    if request.method == 'POST':
        form = request.form
        loan = float(form['loanAmt'])
        payments = int(form['payments'])
        interest = float(form['interest'])
        discountFactor = (((1 + interest)**payments) - 1) / (interest*(1 + interest)**payments)
        loanPayment = round(loan/discountFactor, 2)
        return render_template('index.html', display=loanPayment, pageTitle='Loan Calculator')
        
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)