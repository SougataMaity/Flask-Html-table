from flask import Flask, render_template, request, url_for


app = Flask(__name__)
@app.route('/', methods = ['POST','GET'])
def home():
    head = ['Name', 'Age', 'School']
    len1 = len(head)
    value = [['kk', 26, 'GK'], ['bk', 23, 'Hy']]
    len2 = len(value)
    return render_template('Base.html', head = head, len1 = len1, value = value, len2 = len2)

if __name__ == '__main__':
    app.run(debug=True)