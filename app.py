from click import password_option
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db"
    )
    cursor = conn.cursor()
    cursor.execute("select * from students")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=results)


if __name__ == '__main__':
    app.run(host="localhost",port=5000, debug=True)
