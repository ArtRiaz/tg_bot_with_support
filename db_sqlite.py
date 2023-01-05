import sqlite3 as sq

with sq.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS profile(user_id INTEGER PRIMARY KEY, 
    name VARCHAR(20), surname VARCHAR(20), phone INTEGER, email VARCHAR(30) )""")
    db.commit()


async def create_profiles(user_id):
    user = cursor.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cursor.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cursor.execute(
            "UPDATE profile SET  name = '{}', surname = '{}', phone = '{}', email = '{}' WHERE user_id == '{}'".format(
                data['name'], data['surname'], data['phone'], data['email'], user_id
            ))
        db.commit()
