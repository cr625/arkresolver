# arkresolver
A resolver for Archival Resource Keys

1. Create and set secret key or use the development one already there
2. Set up the db connection (only if you're not using SQLite)
3. cd to the ark directory
4. Make the database migrations  
   
        python manage.py makemigrations resolver

5. Migrate the database  
   
        python manage.py migrate resolver

6. Make a super user  
   
        python manage.py createsuperuser

7. Run the development server  
   
        python manage.py runserver

8. add some records using the admin url (usually 127.0.0.1:8000/admin)
   
9. View the records  http://127.0.0.1:8000/c1/  
    note it is c1 for now because that is the shoulder, the web server will do the translations in production via asgi.py