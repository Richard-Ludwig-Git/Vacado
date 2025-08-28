import psycopg2
from backend import security



conn = psycopg2.connect(host="localhost", port=5432, dbname="vacado", user="vladtepesch")
cur = conn.cursor()


def store_request(request: object, user_id: int):
    """SQL communication to store a user vacation request with user_id for identification and returns request ID PKEY"""
    cur.execute(f"""INSERT INTO vacation_request (duration, theme, accommodation_type, budget, user_id, requested)
                    VALUES({request.duration}, '{request.theme}', '{request.accommodation}', '{request.budget}', {user_id}, current_timestamp);""")
    conn.commit()
    cur.execute(f"""SELECT id FROM vacation_request 
                        WHERE user_id = {user_id};""")
    saved_request = cur.fetchone()
    return saved_request


def store_response(response: object, request_id: int):
    """SQL communication to store ai-vacation response together with request_id secKEY to DB"""
    cur.execute(f"""INSERT INTO vacation_result (destination, flights, accommodation, activities, tips, request_id)
                    VALUES('{response.destination}', '{response.flights}', '{response.accommodation_type}', '{response.activities}', '{response.food_rec}', {request_id});""")
    conn.commit()
    return "response stored"


def delete_response(response_id: int):
    """SQL communication to delete ai-vacation response from DB"""
    cur.execute(f"""DELETE FROM vacation_result WHERE id = {response_id};""")
    conn.commit()
    return "response deleted"


def update_request(request_id: int, duration: int, theme: str, accommodation: str, budget: str):
    """SQL communication to update ai-vacation request parameter if changed"""
    cur.execute(f"""UPDATE vacation_request 
                    SET duration = CASE WHEN {duration} = 0 THEN duration ELSE {duration} END, 
                        theme = CASE WHEN '{theme}' = '' THEN theme ELSE '{theme}' END, 
                        accommodation_type = CASE WHEN '{accommodation}' = '' THEN accommodation_type ELSE '{accommodation}' END, 
                        budget = CASE WHEN '{budget}' = '' THEN budget ELSE '{budget}' END 
                    WHERE id = {request_id};""")
    conn.commit()
    return "request updated"


def get_requests_by_userid(user_id: int):
    """SQL communication to show all requests, made by the current user to display in possible fortend page"""
    cur.execute(f"""SELECT * FROM vacation_request 
                    WHERE user_id = {user_id};""")
    return cur.fetchall()


def delete_request_by_id(request_id: int, user):
    """SQL communication to delete a request from the DB"""
    cur.execute(f"""DELETE FROM vacation_request WHERE id = {request_id} and user_id = {user.user_id};""")
    conn.commit()
    return "request deleted"


def get_user(username: str):
    """SQL communication to return user(obj) if exists in DB"""
    cur.execute(f"""SELECT * FROM user_db
                    WHERE user_name ='{username}';""")
    userdata = cur.fetchone()
    user = security.UserInDB(user_id=userdata[0], user_name=userdata[1], hashed_password=userdata[2], email=userdata[3], disabled=userdata[4])
    if not user:
        return None
    return user


def create_user(username: str, hashed_pw: str, email: str):
    """SQL communication to create user in DB"""
    cur.execute(f"""INSERT INTO user_db (user_name, password, email, active) 
                    VALUES('{username}', '{hashed_pw}', '{email}', True);""")
    conn.commit()


def update_user(current_user, username: str, old_normal_pw: str, new_normal_pw: str, email: str):
    """SQL communication to update user in DB if attribute changed by user"""
    user = security.authenticate(current_user.user_name, old_normal_pw)
    if not user:
        return "password not correct"
    new_hashed_pw = security.get_pw_hash(new_normal_pw)
    cur.execute(f"""UPDATE user_db 
                    SET user_name = CASE WHEN '{username}' = '' THEN user_name ELSE '{username}' END,
                        password = CASE WHEN '{new_normal_pw}' = '' THEN password ELSE '{new_hashed_pw}' END,
                        email = CASE WHEN '{email}' = '' THEN email ELSE '{email}' END
                        WHERE id = {current_user.user_id};""")
    conn.commit()
    return "user updated"


def delete_user(current_user, password: str):
    """SQL communication to delete user profile and all requests/results in DB"""
    user = security.authenticate(current_user.user_name, password)
    if not user:
        return "password not correct"
    cur.execute(f"""DELETE FROM vacation_request WHERE user_id = {current_user.user_id} CASCADE""")
    conn.commit()
    cur.execute(f"""DELETE FROM user_db WHERE id = {current_user.user_id}""")
    conn.commit()
    return "user deleted"


conn.commit()

