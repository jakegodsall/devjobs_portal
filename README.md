# Job Portal Website

This is a job portal web application built with Python 3.12 and Django 5.
The app allows users to sign up as either job seekers (clients) or companies looking to post job openings,
providing a streamlined interface for both parties to connect.
It includes robust authentication and job management features,
with a focus on a user-friendly experience.

## Features

- User Authentication:
  - Separate user registration and login for clients (job seekers) and companies.
  - Secure password management and authentication using Django's built-in system.
- Client Features:
  - View and apply for available job postings.
  - Manage personal profiles and view application history.
- Company Features:
  - Post job openings and manage applicants.
  - View and edit company profile.
- Job Management:
  - Clients can browse jobs filtered by category, location, and job type.
  - Companies can list, edit, and delete job postings.
- Database:
  - Uses PostgreSQL for data storage.
  - Fully integrated with Docker Compose for isolated and consistent development.
- Dockerized Development:
  - The application uses Docker Compose to manage the development environment.
  - Easily deploy and manage the app and its dependencies using Docker.

## Getting Started

### Development

1. Clone the repository
    ```shell
    git clone https://github.com/jakegodsall/devjobs_portal.git
    cd devjobs_portal
    ```

2. Set up the environment
    Create a `.env` file in the project root (you can copy from `.env.example`) and fill in the necessary environment variables.
3. Build and run the application with Docker Compose
   ```shell
   docker compose up --build
   ```
4. Run migrations
    ```shell
    docker-compose exec web python3 manage.py migrate
    ```
5. Create a superuser for accessing the admin panel
    ```shell
    docker-compose exec web python3 manage.py createsuperuser
    ```
6. Access the application at http://localhost:8000.

### Deployment

This project has been optimised for deployment to [Heroku](https://heroku.com), using a PostgreSQL addon.

1. Create a new Heroku app.
    ```shell
    heroku create devjobs_portal
    ```
2. Add the PostgreSQL addon.
   ```shell
   heroku addons:create heroku-postgresql:essential-0
   ```
3. Configure the environment variables
    ```shell
    heroku config:set DJANGO_ENV=production
    ```
   Note that this `DJANGO_ENV` environment variable is used to choose the appropriate settings file:
   ```python
   # manage.py
   
   # Determine the environment
   env = os.getenv('DJANGO_ENV', 'development')  # Default to development
   # Set the settings module
   if env == 'development':
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devjobs_portal.settings.development')
   elif env == 'production':
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devjobs_portal.settings.production')
   else:
      raise ValueError(f"Unknown DJANGO_ENV: {env}")
   ```
   You may also need to set other environment variables such as `SECRET_KEY`, `ALLOWED_HOSTS`, etc., according to your project’s needs:
   ```shell
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
4. Create a `Procfile` in the root of the project (already included in this repository)
   ```shell
   web: gunicorn devjobs_portal.wsgi --log-file -
   ```
5. Deploy the application
   ```shell
   git add .
   git commit -m "Deploying to Heroku"
   git push heroku main
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) for more details.

