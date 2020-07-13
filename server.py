from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

data_list = []


@app.route('/')
def default_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def select_page(page_name):
    return render_template(page_name)


# I need a robots.txt page on this

def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    with open('data.txt', mode='a') as data_txt:
        data_txt.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    with open('database.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Something went wrong. Did not save to database'
    else:
        return 'Something went wrong. Please try again. '
