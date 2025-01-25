from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = {
        "first_name": request.form.get("first-name"),
        "last_name": request.form.get("last-name"),
        "phone": request.form.get("phone"),
        "email": request.form.get("email"),
        "initial1": request.form.get("initial1"),
        "initial2": request.form.get("initial2"),
        "material": request.form.get("material"),
        "type": request.form.get("type")
    }

    # Debugging: Print the received data to the console
    print("Received Data:", data)

    # Save data to a CSV file
    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:  # Write header only if file is empty
            writer.writeheader()
        writer.writerow(data)

    return redirect('/thankyou')



@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)

