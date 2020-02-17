from flask import Flask, render_template, url_for, request
from forms import UrlForm



# '__name__' to refer the current file
app = Flask(__name__)

# Loading all the variables from the config files
app.config.from_pyfile('config.py',)

app.config.get("DYNAMODB_TABLE")

# class Dynamodb(model):
    
#  def insert():
#     '''
#     This method inserts items into the table
#     '''
#     time = int(time.time())
#     item = client.put_item( TableName=model.name,
#         Item={
#             'long_url':{
#                'S': model.long_url
#             },
#             'timestamp':{
#                'N': time
#                 },
#             'short_url':{
#                 'S': model.short_url
#                 }
#             }
#         }

@app.route('/', methods=['POST','GET'])
def index():
    '''
        This method renders the home page of the app.
    '''
    new_form = UrlForm()
    if new_form.validate_on_submit():
       return redirect(url_for('success'))
    return render_template('index.html', form=new_form)
        
    #     try:
    #         db = Dynamodb(model)
    #         db.insert()
    #     except:
    #         return "YOLO! Dynamodb doesn't Work!"        
    # else:
    # return render_template('index.html')

@app.route("/stats")
def stats():
    '''
        This method is used to display the statistics of the 'active' shortened URL's
    '''
    return render_template('stats.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

