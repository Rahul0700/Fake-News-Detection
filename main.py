from flask import Flask, request, render_template
from sklearn.externals import joblib

pipeline = joblib.load('./model.sav')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def get_delay():
    result = request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['content']
    total = query_title + query_author + query_text
    query = [total]
    prediction = pipeline.predict(query)
    dic = {1: 'real', 0: 'fake'}
    return render_template('index.html', result=dic[prediction[0]])


if __name__ == '__main__':
    app.run(port=8080, debug=True)