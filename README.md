# Fake-News-Detection

An ML-model trained and developed using NLP Techniques, Logistic Regression deployed in Flask


###### To develop locally
------

```
git clone https://github.com/Rahul0700/Fake-News-Detection.git

cd Fake-News-Detection

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```
Now move the folder 'nltk_data' inside venv so that the project tree looks like:-

![Project Structure](https://github.com/Rahul0700/Fake-News-Detection/blob/master/Project-Structure.png?raw=true)

###### To run the development server
------
```
export FLASK_APP=app.py

flask run
```

![High Level Design](https://github.com/Rahul0700/Fake-News-Detection/blob/master/High%20level%20design-%20Fake%20News%20Detection.jpg?raw=true)
