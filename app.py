from flask import Flask, render_template, request,jsonify
import random
from prediction1 import *

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item_id = int(request.form['item_id'])
        temperature = float(request.form['temperature'])
        month = int(request.form['month'])
        fresh = int(request.form['fresh'])
        disasters = int(request.form['disasters'])
        prediction_result = predict_cost(
            item_id, temperature, month, fresh, disasters)
        return render_template('output.html', prediction_result=prediction_result)

    return render_template('index.html')


if __name__ == '_main_':
    app.run(debug=True)