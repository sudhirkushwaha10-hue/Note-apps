import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Local: SQLite. Later on GCP: set DATABASE_URL to the Cloud SQL Postgres URL
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///notes.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("content", "").strip()
    if content:
        db.session.add(Note(content=content))
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("FLASK_DEBUG") == "1")