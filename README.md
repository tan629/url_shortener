# TinyApp Project

TinyApp is a full stack web application built with Python and Django that allows users to shorten long URLs (à la bit.ly).

## Running it using Docker

- Install and **run** Docker in your local machine to start the docker engine
- Clone the repo to your machine (Make sure git config core.autocrlf = false before cloning --> set in command line --> git config --global core.autocrlf false)
- In the root folder of the cloned repo, create an .env file with the following template :
  
  SECRET_KEY= <br/>
  DATABASE_NAME= <br/>
  DATABASE_USER= <br/>
  DATABASE_PASS= <br/>
  HOST=postgres_db

- Fill out the blank spaces according to your choice in the .env file above. **Note :** Keep the HOST name as is - this is because <br/>
  this name of the database host is already assigned in the docket-compose setup.
- Open git bash in the root folder of the project
- Run the following command (this will create images of the web app and postgres DB and will run them in containers -> <br/>
  `docker-compose up --build`
- In the web browser, go to `localhost:8000` to run the app

## Final Product

!["Register page"](https://github.com/tan629/url_shortener/blob/main/docs/REGISTER.png)
!["Login page"](https://github.com/tan629/url_shortener/blob/main/docs/LOGIN_PAGE.png)
!["Home page displaying short URLs"](https://github.com/tan629/url_shortener/blob/main/docs/URLS.png)
!["Edit URL page"](https://github.com/tan629/url_shortener/blob/main/docs/VISITOR_DATA.png)
!["Create Short URL page"](https://github.com/tan629/url_shortener/blob/main/docs/CREATE_URL.png)


