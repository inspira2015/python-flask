import os
import psycopg2
from flask import Flask,jsonify,request
from flask_restful import Resource, Api


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='postgresql',
                            database='postgres',
                            user='daniel',
                            password='secret')
    return conn

@app.route('/returnjson', methods = ['GET'])
def index():
    if (request.method == 'GET'):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        books = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(books)
    

if __name__ == "__main__":
   app.run(debug=True)
