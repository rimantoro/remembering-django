# DJANGO FLASHBACK

Cuma buat inget-nget lagi ajaah.

## DEBUG MODE

```
$> # activate your virtual env
$> source your_venv/bin/activate
$> # set debug active
$(python3)> export DEBUG=1
```

## START SERVER

Jangan lupa pakai virtual env untuk python, jangan lupa diactivate juga.

1.  Create migrations 

    ```
    $> python manage.py makemigrations
    Migrations for 'authentication':
      authentication/migrations/0001_initial.py
        - Create model User
    ```

2. Running migrations

   ```
   $ python manage.py migrate
      Operations to perform:
        Apply all migrations: account, admin, auth, authentication, contenttypes, sessions, sites, socialaccount
      Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0001_initial... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying authentication.0001_initial... OK
        Applying account.0001_initial... OK
        Applying account.0002_email_max_length... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying sessions.0001_initial... OK
        Applying sites.0001_initial... OK
        Applying sites.0002_alter_domain_unique... OK
        Applying socialaccount.0001_initial... OK
        Applying socialaccount.0002_token_max_lengths... OK
        Applying socialaccount.0003_extra_data_default_dict... OK
   ```   

3. Create Superuser
   
    ```
    $ python manage.py createsuperuser
    Email address: admin@email.com
    Password: 
    Password (again): 
    Superuser created successfully.
    ```

4. Running server
   
    ```
    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    September 22, 2020 - 13:04:44
    Django version 2.1.15, using settings 'core.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

App frontend ```http://127.0.0.1:8000```. You can register or login using Google (of course, you need to setup first).

Django admin ```http://127.0.0.1:8000/admin```. Login with your superuser.