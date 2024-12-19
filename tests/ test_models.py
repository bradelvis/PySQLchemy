import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Category, Post, Comment  # Import models

# Test configuration: In-memory SQLite database for testing purposes
DATABASE_URL = "sqlite:///:memory:"  # Use in-memory database for testing

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database and session."""
        # Create an in-memory database
        cls.engine = create_engine(DATABASE_URL, echo=True)
        Base.metadata.create_all(cls.engine)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        """Close the session and drop all tables after tests."""
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def test_category_creation(self):
        """Test creating a Category."""
        category = Category(name="Technology", description="Tech-related posts")
        self.session.add(category)
        self.session.commit()

        # Retrieve the Category from the database
        retrieved_category = self.session.query(Category).filter_by(name="Technology").first()
        
        self.assertIsNotNone(retrieved_category)
        self.assertEqual(retrieved_category.name, "Technology")
        self.assertEqual(retrieved_category.description, "Tech-related posts")
    
    def test_post_creation(self):
        """Test creating a Post with an associated Category."""
        category = Category(name="Technology", description="Tech-related posts")
        self.session.add(category)
        self.session.commit()

        post = Post(title="Introduction to Python", content="Python is an easy-to-learn language.", category_id=category.id)
        self.session.add(post)
        self.session.commit()

        # Retrieve the Post and check its properties
        retrieved_post = self.session.query(Post).filter_by(title="Introduction to Python").first()

        self.assertIsNotNone(retrieved_post)
        self.assertEqual(retrieved_post.title, "Introduction to Python")
        self.assertEqual(retrieved_post.content, "Python is an easy-to-learn language.")
        self.assertEqual(retrieved_post.category_id, category.id)

        # Test the relationship: Post -> Category
        retrieved_category = retrieved_post.category
        self.assertEqual(retrieved_category.name, "Technology")

    def test_comment_creation(self):
        """Test creating a Comment for a Post."""
        category = Category(name="Technology", description="Tech-related posts")
        self.session.add(category)
        self.session.commit()

        post = Post(title="Introduction to Python", content="Python is an easy-to-learn language.", category_id=category.id)
        self.session.add(post)
        self.session.commit()

        comment = Comment(content="Great post! Very informative.", post_id=post.id)
        self.session.add(comment)
        self.session.commit()

        # Retrieve the Comment
        retrieved_comment = self.session.query(Comment).filter_by(content="Great post! Very informative.").first()
        
        self.assertIsNotNone(retrieved_comment)
        self.assertEqual(retrieved_comment.content, "Great post! Very informative.")
        self.assertEqual(retrieved_comment.post_id, post.id)

        # Test the relationship: Comment -> Post
        retrieved_post = retrieved_comment.post
        self.assertEqual(retrieved_post.title, "Introduction to Python")

    def test_category_post_relationship(self):
        """Test if the relationship between Category and Post is set correctly."""
        category = Category(name="Technology", description="Tech-related posts")
        post = Post(title="Advanced Python", content="Let's explore Python advanced concepts.", category_id=category.id)
        
        self.session.add(category)
        self.session.add(post)
        self.session.commit()

        # Retrieve category and check the associated posts
        retrieved_category = self.session.query(Category).filter_by(name="Technology").first()
        self.assertIsNotNone(retrieved_category)
        self.assertEqual(len(retrieved_category.posts), 1)
        self.assertEqual(retrieved_category.posts[0].title, "Advanced Python")

    def test_post_comment_relationship(self):
        """Test if the relationship between Post and Comment is set correctly."""
        category = Category(name="Technology", description="Tech-related posts")
        post = Post(title="Advanced Python", content="Let's explore Python advanced concepts.", category_id=category.id)
        comment = Comment(content="This is an advanced post!", post_id=post.id)

        self.session.add(category)
        self.session.add(post)
        self.session.add(comment)
        self.session.commit()

        # Retrieve post and check the associated comments
        retrieved_post = self.session.query(Post).filter_by(title="Advanced Python").first()
        self.assertIsNotNone(retrieved_post)
        self.assertEqual(len(retrieved_post.comments), 1)
        self.assertEqual(retrieved_post.comments[0].content, "This is an advanced post!")

    def test_delete_category_with_posts(self):
        """Test cascading delete when a Category is deleted."""
        category = Category(name="Technology", description="Tech-related posts")
        post = Post(title="Introduction to Python", content="Python basics.", category_id=category.id)
        self.session.add(category)
        self.session.add(post)
        self.session.commit()

        # Delete the category
        self.session.delete(category)
        self.session.commit()

        # Check that the post has been deleted as well
        deleted_post = self.session.query(Post).filter_by(title="Introduction to Python").first()
        self.assertIsNone(deleted_post)

    def test_delete_post_with_comments(self):
        """Test cascading delete when a Post is deleted."""
        category = Category(name="Technology", description="Tech-related posts")
        post = Post(title="Introduction to Python", content="Python basics.", category_id=category.id)
        comment = Comment(content="This is a great post!", post_id=post.id)
        self.session.add(category)
        self.session.add(post)
        self.session.add(comment)
        self.session.commit()

        # Delete the post
        self.session.delete(post)
        self.session.commit()

        # Check that the comment has been deleted as well
        deleted_comment = self.session.query(Comment).filter_by(content="This is a great post!").first()
        self.assertIsNone(deleted_comment)

if __name__ == "__main__":
    unittest.main()
