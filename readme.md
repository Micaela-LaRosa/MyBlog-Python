# Django Blog Project

This Django project provides a basic platform for managing a blog, allowing registered users to create, view, edit, and delete blog posts. It also includes search functionalities, user authentication, and customizable profiles.

# Features

- Blog Model: The Blog model defines the main characteristics of a blog post, including title, subtitle, body text, author, date, and an optional image.

- Views: Uses class-based views to handle CRUD (Create, Read, Update, Delete) operations for blog posts.

BlogListView: Lists all available blog posts.
BlogDetailView: Displays details of a specific blog post.
BlogCreateView, BlogUpdateView, BlogDeleteView: Allows authorized users to create, update, and delete blog posts.
blogSearch: Enables searching for blog posts by title.

- Authentication and Permissions: Manages user authentication using built-in Django forms (AuthenticationForm, UserCreationForm) and controls access permissions to functionalities such as blog post editing and deletion based on user roles (e.g., regular users vs. staff with admin permissions).

- User Interface: The interface includes a navigation menu with links for searching, viewing the blog list, registration, and login. Depending on the user role, access to different blog functionalities is restricted or allowed.

- Profile Customization: Implements a profile edit form (UserEditForm) to allow users to change their username, email, and password.

- Static Pages: Includes static pages such as "Home" and "About Me," providing information about the author and project context.

- Explanatory Video and Test Cases: The project includes an explanatory video located in the explanation_video folder and test cases for testing purposes.

# Technologies Used

* Django Framework: Used for backend web development.
* SQLite Database: Lightweight database for storing blog posts and user information.
* HTML, CSS, and Bootstrap: Used for user interface and styling.
* Python: Primary programming language.

# Project Configuration

This project is configured with Django 4.2.13.

# Usage

1- Clone the Repository: Clone this repository to your local machine.
2- Install Dependencies: Ensure you have Python and Django installed. You can install dependencies using pip: pip install -r requirements.txt
3- Set Up the Database: Run migrations to create SQLite database tables: python manage.py migrate
4- Run the Development Server: Start the Django development server: python manage.py runserver
5- Access the Site: Open your web browser and visit http://localhost:8000/ to see the application in action.


