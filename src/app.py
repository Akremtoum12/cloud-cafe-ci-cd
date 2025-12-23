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


@app.route("/menu")
def get_menu():
    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, price FROM menu_items ORDER BY id;")
                rows = cur.fetchall()

        return jsonify([{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
