- To install the modules along with Django:

  > pip install -r requirements.txt 

  requirements.txt file is present in the root directory

- To build and migrate the SQLite DB run the following command from the root:

  > python manage.py loaddata data.json
  > python manage.py migrate

- To run the server at 8080 port use the following command

 > python manage.py runserve 8080
