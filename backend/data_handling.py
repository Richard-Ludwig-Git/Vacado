import psycopg2
from backend import security



conn = psycopg2.connect(host="localhost", port=5432, dbname="vacado", user="vladtepesch")
cur = conn.cursor()


def store_request(duration: int, theme: str, accommodation: str, budget: str, user_id: int):
    cur.execute(f"""INSERT INTO vacation_request (duration, theme, accommodation_type, budget, user_id, requested)
                    VALUES({duration}, '{theme}', '{accommodation}', '{budget}', {user_id}, current_timestamp);""")
    conn.commit()
    cur.execute(f"""SELECT * FROM vacation_request 
                        WHERE user_id = {user_id};""")
    saved_request = cur.fetchone()
    return saved_request[0]


def store_response(response_opj, request_id):
    cur.execute(f"""INSERT INTO vacation_result (destination, flights, accommodation, activities, tips, request_id)
                    VALUES('{response_opj.destination}', '{response_opj.flights}', '{response_opj.accommodation_type}', '{response_opj.activities}', '{response_opj.food_rec}', {request_id});""")
    conn.commit()
    return "response stored"


def delete_response(response_id: int):
    cur.execute(f"""DELETE FROM vacation_result WHERE id = {response_id};""")
    conn.commit()
    return "response deleted"


def update_request(id: int, duration: int, theme: str, accommodation: str, budget: str):
    cur.execute(f"""UPDATE vacation_request 
                    SET duration = CASE WHEN {duration} = 0 THEN duration ELSE {duration} END, 
                        theme = CASE WHEN '{theme}' = '' THEN theme ELSE '{theme}' END, 
                        accommodation_type = CASE WHEN '{accommodation}' = '' THEN accommodation_type ELSE '{accommodation}' END, 
                        budget = CASE WHEN '{budget}' = '' THEN budget ELSE '{budget}' END 
                    WHERE id = {id};""")
    conn.commit()
    return "request updated"


def get_requests_by_id(request_id: int):
    cur.execute(f"""SELECT * FROM vacation_request 
                    WHERE id = {request_id};""")
    return cur.fetchone()


def get_requests_by_userid(user_id: int):
    cur.execute(f"""SELECT * FROM vacation_request 
                    WHERE user_id = {user_id};""")
    return cur.fetchall()


def delete_request_by_id(request_id: int, user):
    cur.execute(f"""DELETE FROM vacation_request WHERE id = {request_id} and user_id = {user.user_id};""")
    conn.commit()
    return "request deleted"


def get_user(username: str):
    cur.execute(f"""SELECT * FROM user_db
                    WHERE user_name ='{username}';""")
    userdata = cur.fetchone()
    user = security.UserInDB(user_id=userdata[0], user_name=userdata[1], hashed_password=userdata[2], email=userdata[3], disabled=userdata[4])
    if not user:
        return None
    return user


def create_user(username: str, hashed_pw: str, email: str):
    cur.execute(f"""INSERT INTO user_db (user_name, password, email, active) 
                    VALUES('{username}', '{hashed_pw}', '{email}', True);""")
    conn.commit()


def update_user(current_user, username: str, old_normal_pw: str, new_normal_pw: str, email: str):
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
    user = security.authenticate(current_user.user_name, password)
    if not user:
        return "password not correct"
    cur.execute(f"""DELETE FROM user_db WHERE id = {current_user.user_id}""")
    conn.commit()
    return "user deleted"


conn.commit()

