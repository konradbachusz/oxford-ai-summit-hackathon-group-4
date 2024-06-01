import unittest
import sqlite3
from database import init_db, add_post, delete_post, get_all_posts
import time

class TestDatabaseFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the database
        init_db()

    def setUp(self):
        # Clear the posts table before each test
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('DELETE FROM posts')
        conn.commit()
        conn.close()

    def test_add_post(self):
        start_time = time.time()
        # Test adding a post
        add_post("Test Title", "Test Content", "Test Author")
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT * FROM posts')
        posts = c.fetchall()
        conn.close()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0][1], "Test Title")
        self.assertEqual(posts[0][2], "Test Content")
        self.assertEqual(posts[0][3], "Test Author")
        end_time = time.time()
        print(f"test_add_post took {end_time - start_time:.6f} seconds")

    def test_delete_post(self):
        start_time = time.time()
        # Test deleting a post
        add_post("Test Title", "Test Content", "Test Author")
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT id FROM posts')
        post_id = c.fetchone()[0]
        conn.close()

        delete_post(post_id)
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('SELECT * FROM posts')
        posts = c.fetchall()
        conn.close()
        self.assertEqual(len(posts), 0)
        end_time = time.time()
        print(f"test_delete_post took {end_time - start_time:.6f} seconds")

    def test_get_all_posts(self):
        start_time = time.time()
        # Test retrieving all posts
        add_post("Test Title 1", "Test Content 1", "Test Author 1")
        add_post("Test Title 2", "Test Content 2", "Test Author 2")
        posts = get_all_posts()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0][1], "Test Title 1")
        self.assertEqual(posts[0][2], "Test Content 1")
        self.assertEqual(posts[0][3], "Test Author 1")
        self.assertEqual(posts[1][1], "Test Title 2")
        self.assertEqual(posts[1][2], "Test Content 2")
        self.assertEqual(posts[1][3], "Test Author 2")
        end_time = time.time()
        print(f"test_get_all_posts took {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    unittest.main()
