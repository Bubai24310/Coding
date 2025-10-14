from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            c0 = int(request.form['number'])
            s = 0
            while c0 != 1:
                if c0 % 2 == 0:
                    c0 = c0 // 2
                else:
                    c0 = c0 * 3 + 1
                s = s + 1
            result = f"Final value: {c0}, Steps taken: {s}"
        except ValueError:
            result = "Please enter a valid integer."
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
