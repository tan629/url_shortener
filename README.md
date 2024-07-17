# TinyApp Project

TinyApp is a full stack web application built with Python and Django that allows users to shorten long URLs (à la bit.ly).

# Link to Deployed App

[Link to TinyApp](http://tan629.pythonanywhere.com/)

## Dependencies
- crispy-forms
- add all dependencies here

## Running it using Docker

- Install and run Docker in your local machine
- Clone the repo to your machine
- In the root folder of the cloned repo, create an .env file with the following template :
  
  SECRET_KEY= <br/>
  DATABASE_NAME= <br/>
  DATABASE_USER= <br/>
  DATABASE_PASS= <br/>
  HOST=postgres_db

- Fill out the blank spaces according to your choice in the .env file above
- Open git bash in the root folder of the project
- Run the following command (this will create images of the web app and postgres DB and will run them in containers -> `docker-compose up --build`
- In the web browser, go to `localhost:8000` to run the app

## Final Product

!["Register page"](https://github.com/tan629/url_shortener/blob/main/docs/REGISTER.png)
!["Login page"](https://github.com/tan629/url_shortener/blob/main/docs/LOGIN_PAGE.png)
!["Home page displaying short URLs"](https://github.com/tan629/url_shortener/blob/main/docs/URLS.png)
!["Edit URL page"](https://github.com/tan629/url_shortener/blob/main/docs/VISITOR_DATA.png)
!["Create Short URL page"](https://github.com/tan629/url_shortener/blob/main/docs/CREATE_URL.png)


