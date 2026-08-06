import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "ok", "version": "1.1"})

@app.route('/db')
def db_check():
    try:
        import psycopg2
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'db'),
            database='mydb',
            user='user',
            password='pass'
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        return jsonify({"db_version": version})
    except Exception as e:
        return jsonify({"error": str(e)}, 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
