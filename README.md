# Todo
## A simple api for todo app in django
This is an hackathon hosting application created with django and django rest freamework.The app application is divided into three apps.<br>


#### Available API endpoints

'api/tasks' ->  Display the list of all the tasks complete and incomplete<br>
'api/tasks' ->  Create a new task<br><br>
'api/update/<int:pk>' ->  Update any of the existing tasks<br>
'api/complete/<int:pk>' ->  Mark a task as completed<br>
'api/incomplete/<int:pk>' ->  Mark a task a Incomplete<br>
'api/delete/<int:pk>' ->  Delete a particular task<br>

#### Steps To Run
Fork this repo<br>
Clone repo<br>
cd to cloned repo<br>
pip install -r requirements.txt<br>
python manage.py runserver



