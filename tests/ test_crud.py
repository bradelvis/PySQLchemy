import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Post, Category, Comment
from io import StringIO
import sys

# Create a temporary in-memory SQLite database for testing
@pytest.fixture(scope='module')
def test_engine():
    engine = create_engine('sqlite:///:memory:')
    Post.metadata.create_all(engine)
    Category.metadata.create_all(engine)
    Comment.metadata.create_all(engine)
    yield engine
    Post.metadata.drop_all(engine)
    Category.metadata.drop_all(engine)
    Comment.metadata.drop_all(engine)

@pytest.fixture(scope='module')
def Session(test_engine):
    Session = sessionmaker(bind=test_engine)
    return Session

# ==================== Test CRUD for Categories =========================

def test_add_category(Session):
    session = Session()
    new_category = Category(name="Technology", description="Tech related posts")
    session.add(new_category)
    session.commit()

    category = session.query(Category).filter_by(name="Technology").first()
    assert category is not None
    assert category.name == "Technology"
    assert category.description == "Tech related posts"
    session.close()

def test_view_categories(Session):
    session = Session()
    categories = session.query(Category).all()
    assert len(categories) > 0  # There should be at least one category in the test data
    session.close()

def test_update_category(Session):
    session = Session()
    category = session.query(Category).filter_by(name="Technology").first()
    category.name = "Science & Tech"
    session.commit()

    updated_category = session.query(Category).filter_by(name="Science & Tech").first()
    assert updated_category is not None
    assert updated_category.name == "Science & Tech"
    session.close()

def test_delete_category(Session):
    session = Session()
    category = session.query(Category).filter_by(name="Science & Tech").first()
    session.delete(category)
    session.commit()

    deleted_category = session.query(Category).filter_by(name="Science & Tech").first()
    assert deleted_category is None
    session.close()

# ==================== Test CRUD for Posts =========================

def test_add_post(Session):
    session = Session()
    category = Category(name="Technology", description="Tech related posts")
    session.add(category)
    session.commit()

    new_post = Post(title="Introduction to Python", content="Python is a versatile programming language.", category_id=category.id, created_at=datetime.utcnow())
    session.add(new_post)
    session.commit()

    post = session.query(Post).filter_by(title="Introduction to Python").first()
    assert post is not None
    assert post.title == "Introduction to Python"
    assert post.content == "Python is a versatile programming language."
    assert post.category_id == category.id
    session.close()

def test_view_posts(Session):
    session = Session()
    posts = session.query(Post).all()
    assert len(posts) > 0  # There should be at least one post in the test data
    session.close()

def test_update_post(Session):
    session = Session()
    post = session.query(Post).filter_by(title="Introduction to Python").first()
    post.title = "Updated Python Post"
    post.content = "Updated content for Python post"
    session.commit()

    updated_post = session.query(Post).filter_by(title="Updated Python Post").first()
    assert updated_post is not None
    assert updated_post.title == "Updated Python Post"
    assert updated_post.content == "Updated content for Python post"
    session.close()

def test_delete_post(Session):
    session = Session()
    post = session.query(Post).filter_by(title="Updated Python Post").first()
    session.delete(post)
    session.commit()

    deleted_post = session.query(Post).filter_by(title="Updated Python Post").first()
    assert deleted_post is None
    session.close()

# ==================== Test CRUD for Comments =========================

def test_add_comment(Session):
    session = Session()
    post = session.query(Post).first()  # Assuming there is already a post in the test database
    new_comment = Comment(post_id=post.id, commenter_name="John Doe", content="Great article!", created_at=datetime.utcnow())
    session.add(new_comment)
    session.commit()

    comment = session.query(Comment).filter_by(commenter_name="John Doe").first()
    assert comment is not None
    assert comment.content == "Great article!"
    assert comment.post_id == post.id
    session.close()

def test_view_comments(Session):
    session = Session()
    post = session.query(Post).first()  # Assuming there is at least one post
    comments = session.query(Comment).filter_by(post_id=post.id).all()
    assert len(comments) > 0  # There should be at least one comment in the test data
    session.close()

def test_update_comment(Session):
    session = Session()
    comment = session.query(Comment).filter_by(commenter_name="John Doe").first()
    comment.content = "Updated comment content!"
    session.commit()

    updated_comment = session.query(Comment).filter_by(commenter_name="John Doe").first()
    assert updated_comment.content == "Updated comment content!"
    session.close()

def test_delete_comment(Session):
    session = Session()
    comment = session.query(Comment).filter_by(commenter_name="John Doe").first()
    session.delete(comment)
    session.commit()

    deleted_comment = session.query(Comment).filter_by(commenter_name="John Doe").first()
    assert deleted_comment is None
    session.close()

# ==================== Running Tests ==============================

if __name__ == "__main__":
    pytest.main()
