import flask
import MySQLdb

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    db = MySQLdb.connect("localhost","root","pswd","Company" )
    cursor = db.cursor()
    cursor.execute("select * from Employee")
    data = cursor.fetchall()
    print (data)
    values = ','.join(str(v) for v in data)
    return(values)

app.run(host='0.0.0.0')
