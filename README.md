# PySQLchemy
# Project Description
The Personal Blog Management System (PBMS) is a simple command-line tool for blog owners to manage their posts, categories, and comments. It provides easy-to-use options for creating, reading, updating, and deleting (CRUD) blog posts, categories, and comments. This helps blog owners stay organized and efficiently manage content without overwhelming complexity.

# Problem
Blog owners often face challenges like:

Difficulty organizing and categorizing blog posts.
Managing growing comment sections.
Redundancy and manual errors when updating posts or categories.
Solution
The PBMS helps by:

Managing Posts: Add, view, update, and delete blog posts.
Organizing Categories: Create and manage categories for posts.
Tracking Comments: Add, view, and delete comments on posts.
This system simplifies blog management with a command-line interface, keeping things simple and efficient.

# System Features
Create and Manage Posts: Add, update, and delete blog posts.
Create and Manage Categories: Group posts under specific categories.
Manage Comments: Add and delete comments on posts.
Basic Data Integrity: Avoid orphaned posts or comments.
Data Relationships
Posts and Categories:
A category can have many posts.
A post belongs to one category.
Posts and Comments:
A post can have many comments.
Each comment belongs to one post.
User Stories
Post Management
Add Post: Create a new post by specifying title, content, and category.
View Posts: View a list of posts with titles, content previews, and categories.
Update Post: Edit a post's title, content, or category.
Delete Post: Remove a post.
Category Management
Add Category: Create a new category for organizing posts.
View Categories: See all available categories.
Delete Category: Remove a category.
Comment Management
Add Comment: Post a comment on a blog post.
View Comments: See all comments for a specific post.
Delete Comment: Remove a comment from a post.
System Requirements
Programming Language: Python
Database: SQLite (for storing posts, categories, and comments)
CLI: Simple command-line interface for managing the system.
Setup and Installation
Clone the repository:

# bash
Copy code
# git clone <repository-url>
cd personal-blog-management-system
Set up a virtual environment:

# bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install dependencies:

# bash
Copy code
pip install -r requirements.txt
Initialize the database:

# bash
Copy code
python setup.py
Run the application:

# bash
Copy code
python app.py
Commands
Add a New Post:

# bash
Copy code
add_post --title "Introduction to Python" --content "Python is a versatile language..." --category "Technology"
View All Posts:

# bash
Copy code
list_posts
Update Post:

# bash
Copy code
update_post --post_id 1 --title "Updated Python Post" --content "New content here..."
Delete Post:

# bash
Copy code
delete_post --post_id 1
Add a New Category:

# bash
Copy code
add_category --name "Technology"
Add a Comment:

# bash
Copy code
add_comment --post_id 10 --name "John Doe" --content "Great post!"
Conclusion
The PBMS provides an easy way for blog owners to manage content, categories, and comments with a simple CLI tool. It helps keep posts organized and simplifies content management, all with minimal complexity.

 # link google slides
 https://docs.google.com/presentation/d/1LByfbmKYxv5PLhrQ26NslDMBAh970y2DjXN_36jiFhs/edit#slide=id.g321534b1738_0_440
# link for video recording
https://drive.google.com/file/d/1Jb-eD3_yz4l0uvHTsHUXyQHe82EPNzjk/view
