import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Nateriver',
    'database': 'blog_app'
}

def getAllPosts():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    cursor.close()
    conn.close()

    return posts