# Defines four endpoints for handling CURD (Create, Update, Read, Delete)

from databases import Database
from databases import DatabaseURL
from flask import Flask,jsonify,request

app = Flask(__name__)
db = Database(DatabaseURL("sqlite:///users.db"))

@app.route("/users",methods=["GET"])
async def get_users():
    query = "Select * FROM users"
    collect = await db.fetch_all(query)
    iden = []
    for collect in collect:
        user = {"Name":row[0],"id":row[1],"Points":[2]}
        iden.append(user)
    return jsonify(iden)


@app.route("/users",methods=["POST"])
async def create_user():
    data = request.get_json()
    query = "INSERT INTO users(Name,Points) VALUES (:Name, :Points)"
    await db.execute(query, values=("Name": data["Name"],"Points":data["Points"]))
    return "",204

@app.route("/users/<int:user_id>",methods=["PUT"])
async def update_user(user_id):
    data = request.get_json()
    query = "UPDATE users SET name = :name,points = :points WHERE id = :id"
    await db.execute(query, values=("Name": data["Name"],"Points":data["Points"],"id": user_id))
    return "",204

@app.route("/users/<int:user_id>",methods=["DELETE"])
async def delete_user(user_id):
    query = "DELETE FROM users WHERE id = :id"
    await db.execute(query, values={"id": user_id})
    return "",204
