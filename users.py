print("hello users")

db.cursor.execute("""select * from users""")
users = db.cursor.fetchall()

return users
