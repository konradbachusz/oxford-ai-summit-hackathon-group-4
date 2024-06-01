import sqlite3

def init_db():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS posts
              (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, author TEXT)
              ''')
    conn.commit()
    conn.close()

def add_post(title, content, author):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('INSERT INTO posts (title, content, author) VALUES (?, ?, ?)', (title, content, author))
    conn.commit()
    conn.close()

def delete_post(post_id):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()

def get_all_posts():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()
    conn.close()
    return posts
