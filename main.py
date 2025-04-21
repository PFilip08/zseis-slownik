from flask import Flask, render_template
import mysql.connector

def getDB(who):
    conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123",
    database = "zseis"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM "+who)
    rows = cursor.fetchall() 
    conn.close()
    return rows[0]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def zseis1():
    teksty = getDB('zseis1')
    return render_template('ziut.html', header='mich a los', texts=teksty)

@app.route('/2')
def zseis2():
    teksty = getDB('zseis2')
    return render_template('ziut.html', header='chrust11', texts=teksty)

@app.route('/3')
def zseis3():
    teksty = getDB('zseis3')
    return render_template('ziut.html', header='dogs leg', texts=teksty)

@app.route('/4')
def zseis4():
    teksty = getDB('zseis4')
    return render_template('ziut.html', header='zbiax', texts=teksty)

@app.route('/5')
def zseis5():
    teksty = getDB('zseis5')
    return render_template('ziut.html', header='AA', texts=teksty)

if __name__ == '__main__':
    app.run(debug=True)