from flask import redirect, session
import hashlib
from .db import get_db


def handle_login(request):
    """
    Handle user login by verifying credentials.
    """
    # Here you would add logic to verify the username and password
    # against your user database.
    email_or_username = request.form.get("email_or_username") 
    password = request.form.get("password")
    # takes what the user inputs

    if not email_or_username or not password:
        return redirect("/login") # page refreshes if something isn't inputted
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # hashes the inputted password so it can compare it to what's in the db
    # b/c abc123 will never == the stored hash

    db = get_db()
    cursor = db.cursor(dictionary=True)

    sql = """
        select * from users
        where (email = %s or username = %s) AND password = %s
    """
### checks if user inputs match whats in the db
    cursor.execute(sql, (email_or_username, email_or_username, hashed_password))
    user = cursor.fetchone() # grabs matching row, and if one matches then thats the user's data
    cursor.close()

    if user: ### if the login is successful
        session['user_id'] = user['id'] 
        session['username'] = user['username']
        return redirect("/")
    else:
        return redirect("/login")