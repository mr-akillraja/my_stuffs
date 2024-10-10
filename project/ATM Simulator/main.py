from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# ... (ATM class and routes remain the same)
class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Current balance: ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.balance}"
        else:
            return "Insufficient funds. Unable to withdraw."

atm = ATM()

@app.route('/')
def index():
    return render_template('index.html', balance=atm.check_balance())

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.form['amount'])
    message = atm.deposit(amount)
    return render_template('index.html', balance=atm.check_balance(), message=message)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = float(request.form['amount'])
    message = atm.withdraw(amount)
    return render_template('index.html', balance=atm.check_balance(), message=message)

if __name__ == "__main__":
    app.run(debug=True)
