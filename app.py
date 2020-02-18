from flask import Flask, render_template, url_for, redirect, request
from forms import UrlForm
from db import DynamoDB
from time import time
import random
import short_url

# '__name__' to refer the current file
app = Flask(__name__)

# Loading the variables from the config files
app.config.from_pyfile('config.py',)

# Setting the required variables for the application
#app.config.get("DYNAMODB_TABLE")
app.config.get("SECRET_KEY")

#empty dictionary for the inserting form object to db
obj={}

#prefix domain
domain='https://cut.it/'
@app.route('/', methods=['POST','GET'])
def index():
    '''
        This method renders the home page of the app.
    '''
    new_form = UrlForm()
    if new_form.validate_on_submit():
        obj['long_url'] = new_form.long_url.data
        obj['timestamp'] = str(int(time()))
        obj['short_url'] = domain + short_url.encode_url(random.randrange(1,1000,1))        
        #obj['short_url'] = short_url.encode_url(random.randrange(1,1000,1)) need to think

        db_obj = DynamoDB(obj)
        flag, response = db_obj.search()
        if flag == True:
            response = response['Items'][0]['short_url']['S'] 
            print(response) # debug point
            return render_template('index.html', form=new_form, short_url=response)            
        else:
            db_obj.insert()            
            print("insert successful") # debug point
            return render_template('index.html', form=new_form, short_url=obj['short_url'])
        
    return render_template('index.html', form=new_form)

@app.route("/stats")
def stats():
    '''
        This method is used to display the statistics of the 'active' shortened URL's
    '''
    return render_template('stats.html')

@app.route("/<path:short_url>/stats")
def get_stats(short_url):
    
    return render_template('short-stats.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')