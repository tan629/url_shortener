# TinyApp Project

TinyApp is a full stack web application built with Python and Django that allows users to shorten long URLs (à la bit.ly).

# Link to Deployed App

[TinyApp](http://tan629.pythonanywhere.com/)
** notes here **

## Final Product

!["Register page"](https://github.com/tan629/url_shortener/blob/main/docs/REGISTER.png)
!["Login page"](https://github.com/tan629/url_shortener/blob/main/docs/LOGIN_PAGE.png)
!["Home page displaying short URLs"](https://github.com/tan629/url_shortener/blob/main/docs/URLS.png)
!["Edit URL page"](https://github.com/tan629/url_shortener/blob/main/docs/EDIT_URL.png)
!["Create Short URL page"](https://github.com/tan629/url_shortener/blob/main/docs/CREATE_URL.png)
!["ERD of TinyApp"](https://github.com/tan629/url_shortener/blob/main/docs/tinyapp_users_url.png)


## Dependencies

- crispy-forms
- add all dependencies here


## Getting Started

- Set up a virtual environment
- Install all dependencies (using the pip install requirements.txt command).
- Set up a postgres or sqlite database.  If a postgres database is being used, make sure to populate the secrets in a .env file
- Run the development web server using the `python manage.py runserver` command.
- Run the migrations using the `python manage.py migrate` command.
- Create a superuser to access the /admin page
