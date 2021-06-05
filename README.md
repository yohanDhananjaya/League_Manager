# League_Manager
 In order to run the project please follow the instructions below,<br>
    1. Clone the project from the github repository to local environment and install the python environment (In my case python 3.7)<br>
    2. after activating the environment exceute the following codes to migrate data to database<br>
        &nbsp;&nbsp;i.   pip3 install -r requirments.txt<br>
        &nbsp;&nbsp;ii.  python manage.py makemigrations league<br>
        &nbsp;&nbsp;iii. python manage.py loaddata<br>
    3. Now you are ready to execute the APIs<br>
    4. I have added my postman collection as well in case you need<br>
<br>
*** With every API request the user email should be included and all of the APIs are POST requests ***<br>
*** Permission management for these APIs are done by adding custom decorators ***<br>
<br>
After adding the fake data there are three users available in the system,<br>
    1. yohan1@gmail.com - admin user<br>
    2. yohan2@gmail.com - coach<br>
    3. yohan3@gmail.com - player<br>

To use all APIs put the admin user email when using the API<br>
<br>
-> Login to system - http://127.0.0.1:8000/league/login<br>
-> Logout from the system - http://127.0.0.1:8000/league/logout<br>
-> To retireve all user data and site usage statistics - http://127.0.0.1:8000/league/user_info<br>
-> To retrieve tournament overall progress - http://127.0.0.1:8000/league/tournament_progress<br>
-> To get players details -> http://127.0.0.1:8000/league/get_player_details  (additionally player_id required)<br>
-> To filter players by percentile -> http://127.0.0.1:8000/league/get_players_by_percentile (additionally team_id and percentile required)<br>
