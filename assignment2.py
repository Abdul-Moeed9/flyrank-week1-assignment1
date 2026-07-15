from fastapi import FastAPI
from pwdlib import PasswordHash

app = FastAPI()
password_hash = PasswordHash.recommended()


user_info = {}
logged_in_users = set()

def hash_password(password: str):
    return password_hash.hash(password)

@app.post("/register")
def register_user(username: str, password: str):
    if user_info.get(username):
        return {"message": "this user has already been registered"}
    
    else:
        hashed_pass = hash_password(password)
        user_info[username] = hashed_pass
        return {"message": "this user has now been registered"}

@app.post("/login")
def login_user(username: str, password: str):
    if not user_info.get(username):
        return{"message": "invalid username"}
    
    stored_hash = user_info[username]

    if not password_hash.verify(password, stored_hash):
        return {"message": "invalid password"}
    
    else:
        logged_in_users.add(username)
        return {"message": "login successful"}
    

@app.get("/")
def working_message():
    return {"message": "the backend works"}
    
@app.get("/users")
def get_users(username: str):
    if username not in logged_in_users:
        return {"message": "you are not logged in, only logged in users can see other users."}
    
    return list(user_info.keys())
    
