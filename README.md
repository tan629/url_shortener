# TinyApp Project

TinyApp is a full stack web application built with Python and Django that allows users to shorten long URLs (à la bit.ly).

# Link to Deployed App

[Link to TinyApp](http://tan629.pythonanywhere.com/)

## Final Product

!["Register page"](https://github.com/tan629/url_shortener/blob/main/docs/REGISTER.png)
!["Login page"](https://github.com/tan629/url_shortener/blob/main/docs/LOGIN_PAGE.png)
!["Home page displaying short URLs"](https://github.com/tan629/url_shortener/blob/main/docs/URLS.png)
!["Edit URL page"](https://github.com/tan629/url_shortener/blob/main/docs/VISITOR_DATA.png)
!["Create Short URL page"](https://github.com/tan629/url_shortener/blob/main/docs/CREATE_URL.png)
!["ERD of TinyApp"](https://github.com/tan629/url_shortener/blob/main/docs/tinyapp_users_url.png)


## Dependencies

- crispy-forms
- add all dependencies here


## Getting Started

- Install python 3.10 (required)
- Set up a virtual environment in the root of the cloned project folder -> terminal (powershell or git bash) command -> `python -m venv venv`
- Install all dependencies -> In the root of the project, execute the command -> `pip install -r requirements.txt`
  
- Set up a postgres or sqlite database.  If a postgres database is being used, make sure to populate the following secrets in a .env file ->
  SECRET_KEY=
  DATABASE_NAME=
  DATABASE_USER=
  DATABASE_PASS=
  
- Run the development web server using the `python manage.py runserver` command.
- Run the database migrations using the `python manage.py migrate` command.
- Create a superuser to access the /admin page
