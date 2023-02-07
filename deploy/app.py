import flask
import pickle

with open(f'/linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    elif flask.request.method == 'POST':
        acceleration = int(flask.request.form['acceleration'])
        weight = int(flask.request.form['weight'])

        input_variables = [[acceleration, weight]]

        prediction = int(model.predict(input_variables)[0])

        return flask.render_template('index.html',
                                     original_input={'Acceleration': acceleration,
                                                     'Weight': weight},
                                     result=prediction,
                                     )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
