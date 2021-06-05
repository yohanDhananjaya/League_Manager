# League_Manager
 In order to run the project please follow the instructions below,
    1. Clone the project from the github repository to local environment and install the python environment (In my case python 3.7)
    2. after activating the environment exceute the following codes to migrate data to database
        i.   pip3 install -r requirments.txt
        ii.  python manage.py makemigrations league
        iii. python manage.py loaddata
    3. Now you are ready to execute the APIs
    4. I have added my postman collection as well in case you need

*** With every API request the user email should be included and all of the APIs are POST requests ***
*** Permission management for these APIs are done by adding custom decorators ***

After adding the fake data there are three users available in the system,
    1. yohan1@gmail.com - admin user
    2. yohan2@gmail.com - coach
    3. yohan3@gmail.com - player

To use all APIs put the admin user email when using the API

-> Login to system - http://127.0.0.1:8000/league/login
-> Logout from the system - http://127.0.0.1:8000/league/logout
-> To retireve all user data and site usage statistics - http://127.0.0.1:8000/league/user_info
-> To retrieve tournament overall progress - http://127.0.0.1:8000/league/tournament_progress
-> To get players details -> http://127.0.0.1:8000/league/get_player_details  (additionally player_id required)
-> To filter players by percentile -> http://127.0.0.1:8000/league/get_players_by_percentile (additionally team_id and percentile required)
