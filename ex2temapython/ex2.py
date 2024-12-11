import pandas as pd
import  matplotlib.pyplot as plt
from flask import Flask, render_template

#Vasile George
X=6; Y=6

date=pd.read_csv("data.csv")

date.plot()
plt.savefig('static/images/graf1.png')

date.head(X).plot()
plt.savefig('static/images/graf2.png')

date.tail(Y).plot("Durata","Puls")
plt.savefig('static/images/graf3.png')

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

