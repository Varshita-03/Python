#Flask
from flask import Flask
app=Flask(__name__)
#necessary ffuntions that need to be written
@app.route("/") #way to the website ex:www.github.com/varshita-03

def newf():
    return("Hello World!")

if __name__=="__main__":
    app.run(debug=True,port=8000)