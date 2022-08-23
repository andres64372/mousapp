import bcrypt
import jwt
from datetime import datetime, timedelta
import base64

from models.model import User, db
from conf import settings

from domain.login import Login
from domain.signup import SignUp

from request_objects import Response

def validate_user(request: Login) -> Response:
    user = User.query.filter_by(email=request.email).all()
    if not user:
        return Response(data={"error":"bad login"}, status=400)
    if not user[0].status:
        return Response(data={"error":"user not active"}, status=400)
    match = bcrypt.checkpw(request.password.encode('utf-8'), user[0].password.encode('utf-8'))
    if match:
        token = jwt.encode({
                "exp":datetime.utcnow() + timedelta(hours=24), 
                "user":user[0].id},
            settings.SECRET_KEY, algorithm="HS256")
        return Response(data={"token":token}, status=201)
    else:
        return Response(data={"error":"bad login"}, status=400)

def create_user(request: SignUp) -> Response:
    users = User.query.filter_by(email=request.email).all()
    if not '@' in request.email:
        return Response(data={"error":"invalid entries"}, status=400)
    if not users:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(request.password.encode('utf-8'), salt).decode('utf-8')
        id = base64.b64encode(request.email.encode('ascii')).decode('ascii')
        user = User(
            id = id,
            first_name = request.first_name,
            last_name = request.last_name,
            email = request.email,
            password = hashed,
            phone = request.phone
        )
        db.session.add(user)
        db.session.commit()
        return Response(data=None, status=201)
    else:
        return Response(data={"error":"user already exists"}, status=400)
