from faker import Faker
from datetime import datetime
from sqlalchemy.sql import func  # <-- Import the 'func' module from SQLAlchemy
from config import *  # Importing Session and engine configurations
from models import Post, Category, Comment  # Importing the models

# Initialize Faker instance
fake = Faker()

# Create tables if they don't already exist
Category.metadata.create_all(engine)
Post.metadata.create_all(engine)
Comment.metadata.create_all(engine)

# Add some sample Categories if none exist
categories = ["Technology", "Lifestyle", "Health", "Travel", "Food"]
for category_name in categories:
    # Check if the category already exists
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name, description=f"{category_name} related posts")
        session.add(category)
        session.commit()

# Add some sample Posts
for _ in range(20):
    # Randomly assign a category from the existing ones
    category = session.query(Category).order_by(func.random()).first()
    
    post = Post(
        title=fake.sentence(nb_words=6),
        content=fake.paragraph(nb_sentences=5),
        category_id=category.id,
        created_at=datetime.utcnow()
    )
    session.add(post)

# Commit the posts after they are added
session.commit()

# Add some sample Comments for posts
posts = session.query(Post).all()

for post in posts:
    # Generate 3 random comments per post
    for _ in range(3):
        comment = Comment(
            post_id=post.id,
            content=fake.sentence(nb_words=10),
            created_at=datetime.utcnow()
        )
        session.add(comment)

# Commit the comments after they are added
session.commit()

print("Sample categories, posts, and comments have been added successfully!")