from app import app, db
from app.models import User
from flask import jsonify, request

@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"

@app.route('/users')
def users():
  all_user = db.session.query(User).all()
  res = [user.to_dict() for user in all_user]
  print(all_user)
  return jsonify({ 'list': res })

@app.route('/user/<int:id>', methods=['GET'])
def getUser(id):
  user = User.query.get(id)
  print(user)
  return jsonify(user.to_dict())

@app.route('/user', methods=['POST'])
def creatUser():
  username = request.form.get('username')
  email = request.form.get('email')
  u = User(username = username, email = email)
  db.session.add(u)
  db.session.commit()
  print(u)
  return jsonify(u.to_dict())
