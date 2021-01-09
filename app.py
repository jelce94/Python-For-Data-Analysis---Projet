from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
	modelpath = 'models/final_prediction_logistic_regression.pickle'
	# Logistic regression by default
	data = request.get_json()
	if 'model' in data.keys():
		if data['model'] == 'LR':
			modelpath = 'models/final_prediction_logistic_regression.pickle'
		elif data['model'] == 'LRS':
			modelpath = 'models/final_prediction_logistic_regression_SMOTE.pickle'
		elif data['model'] == 'RF':
			modelpath = 'models/final_prediction_random_forest.pickle'
		elif data['model'] == 'KNN':
			modelpath= 'models/final_prediction_KNN.pickle'
		elif data['model'] == 'CLF':
			modelpath = 'models/final_prediction_CLF.pickle'
			
	model = p.load(open(modelpath, 'rb'))
	prediction = np.array2string(model.predict(data['values']))

	return jsonify(prediction)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
