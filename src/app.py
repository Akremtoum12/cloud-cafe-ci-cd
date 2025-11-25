from flask import Flask, jsonify

from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Cloud Café CI/CD v2 ☕"})

@app.route("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db": "ok", "result": result[0]})
    except Exception as e:
        return jsonify({"db": "error", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
