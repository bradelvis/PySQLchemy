from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Define the Category model
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # One-to-many relationship: A Category can have many Posts
    posts = relationship("Post", back_populates="category", cascade="all, delete-orphan")

# Define the Post model
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign key to associate Post with Category
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    # One-to-many relationship: A Post can have many Comments
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

    # Define the relationship with Category
    category = relationship("Category", back_populates="posts")

# Define the Comment model
class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign key to associate Comment with Post
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    # Define the relationship with Post
    post = relationship("Post", back_populates="comments")
