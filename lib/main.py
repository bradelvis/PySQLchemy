from config import *
from models import Post, Category, Comment
from datetime import datetime



# Functions for my CRUD Operations
def add_post():
    title = input("Enter Post Title: ")
    content = input("Enter Post Content: ")
    category_id = int(input("Enter Category ID: "))
    post = Post(title=title, content=content, category_id=category_id, created_at=datetime.utcnow())
    session = Session()
    session.add(post)
    session.commit()
    session.close()
    print("Post added successfully.")

def view_posts():
    session = Session()
    posts = session.query(Post).all()
    for post in posts:
        print(f"ID: {post.id} - Title: {post.title} - Category ID: {post.category_id}")
    session.close()

def update_post():
    post_id = int(input("Enter Post ID to update: "))
    session = Session()
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        post.title = input(f"Enter new title (current: {post.title}): ")
        post.content = input(f"Enter new content (current: {post.content}): ")
        post.category_id = int(input(f"Enter new Category ID (current: {post.category_id}): "))
        session.commit()
        session.close()
        print("Post updated successfully.")
    else:
        print("Post not found.")
        session.close()

def delete_post():
    post_id = int(input("Enter Post ID to delete: "))
    session = Session()
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        session.delete(post)
        session.commit()
        session.close()
        print("Post deleted successfully.")
    else:
        print("Post not found.")
        session.close()


# ==================== Category CRUD Operations ==========================

def add_category():
    name = input("Enter Category Name: ")
    description = input("Enter Category Description: ")
    category = Category(name=name, description=description)
    session = Session()
    session.add(category)
    session.commit()
    session.close()
    print("Category added successfully.")

def view_categories():
    session = Session()
    categories = session.query(Category).all()
    for category in categories:
        print(f"ID: {category.id} - Name: {category.name} - Description: {category.description}")
    session.close()

def update_category():
    category_id = int(input("Enter Category ID to update: "))
    session = Session()
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        category.name = input(f"Enter new name (current: {category.name}): ")
        category.description = input(f"Enter new description (current: {category.description}): ")
        session.commit()
        session.close()
        print("Category updated successfully.")
    else:
        print("Category not found.")
        session.close()

def delete_category():
    category_id = int(input("Enter Category ID to delete: "))
    session = Session()
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        session.close()
        print("Category deleted successfully.")
    else:
        print("Category not found.")
        session.close()


# ==================== Comment CRUD Operations ==========================

def add_comment():
    post_id = int(input("Enter Post ID for the comment: "))
    commenter_name = input("Enter Commenter's Name: ")
    content = input("Enter Comment Content: ")
    comment = Comment(post_id=post_id, commenter_name=commenter_name, content=content, created_at=datetime.utcnow())
    session = Session()
    session.add(comment)
    session.commit()
    session.close()
    print("Comment added successfully.")

def view_comments():
    post_id = int(input("Enter Post ID to view comments: "))
    session = Session()
    comments = session.query(Comment).filter_by(post_id=post_id).all()
    for comment in comments:
        print(f"ID: {comment.id} - Commenter: {comment.commenter_name} - Content: {comment.content}")
    session.close()

def update_comment():
    comment_id = int(input("Enter Comment ID to update: "))
    session = Session()
    comment = session.query(Comment).filter_by(id=comment_id).first()
    if comment:
        comment.content = input(f"Enter new content (current: {comment.content}): ")
        session.commit()
        session.close()
        print("Comment updated successfully.")
    else:
        print("Comment not found.")
        session.close()

def delete_comment():
    comment_id = int(input("Enter Comment ID to delete: "))
    session = Session()
    comment = session.query(Comment).filter_by(id=comment_id).first()
    if comment:
        session.delete(comment)
        session.commit()
        session.close()
        print("Comment deleted successfully.")
    else:
        print("Comment not found.")
        session.close()


# ===================== Main CLI App ==============================

def main():
    while True:
        os.system('clear')
        print("Welcome to Personal Blog Management System (PBMS)")
        print("1. Manage Blog Posts")
        print("2. Manage Categories")
        print("3. Manage Comments")
        main_menu_choice = input("Enter your Choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Post")
                print("2. View Posts")
                print("3. Update Post")
                print("4. Delete Post")
                print("5. Back to Main Menu")
                post_menu_choice = input("Enter your Choice: ")
                if post_menu_choice == '1':
                    add_post()
                elif post_menu_choice == '2':
                    view_posts()
                elif post_menu_choice == '3':
                    update_post()
                elif post_menu_choice == '4':
                    delete_post()
                elif post_menu_choice == '5':
                    break
                input("Press Enter to continue...")
        
        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Category")
                print("2. View Categories")
                print("3. Update Category")
                print("4. Delete Category")
                print("5. Back to Main Menu")
                category_menu_choice = input("Enter your Choice: ")
                if category_menu_choice == '1':
                    add_category()
                elif category_menu_choice == '2':
                    view_categories()
                elif category_menu_choice == '3':
                    update_category()
                elif category_menu_choice == '4':
                    delete_category()
                elif category_menu_choice == '5':
                    break
                input("Press Enter to continue...")
        
        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. Add Comment")
                print("2. View Comments")
                print("3. Update Comment")
                print("4. Delete Comment")
                print("5. Back to Main Menu")
                comment_menu_choice = input("Enter your Choice: ")
                if comment_menu_choice == '1':
                    add_comment()
                elif comment_menu_choice == '2':
                    view_comments()
                elif comment_menu_choice == '3':
                    update_comment()
                elif comment_menu_choice == '4':
                    delete_comment()
                elif comment_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        else:
            print("Invalid choice! Please choose again.")
            input("Press Enter to continue...")


# Call the main function
main()