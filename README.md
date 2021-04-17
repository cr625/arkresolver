# arkresolver
A resolver for Archival Resource Keys

1. Create and set secret key or use the development one already there
2. Set up the db connection (only if you're not using SQLite)
3. cd to the ark directory
4. Make the database migrations  
        python manage.py makemigrations
5. Migrate the database  
        python manage.py migrate
6. Make a super user  
        python manage.py createsuperuser
7. Run the development server  
        python manage.py runserver

