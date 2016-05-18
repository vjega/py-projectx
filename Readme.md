##Project-X 

### Msys Technologies

### Installation Steps (Ubuntu 12.02 +)

   
###Install Python 2.7 +

	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get update
	sudo apt-get install python2.7

###Install Pip 6.1 +

	sudo apt-get install python-pip python-dev build-essential
	sudo pip install --upgrade pip
	(Ref:http://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/)

###Install Virtual Environments:
	pip install virtualenv
	virtualenv projectenv
	source projectenv/bin/activate
	(Ref:http://docs.python-guide.org/en/latest/dev/virtualenvs/)

###Install Django 1.9 +
	pip install django

###Install Application Dependencies
	pip install -r requirments.txt

###Mysql Installtion
	sudo apt-get build-dep python-mysqldb
	
	if you got any mysql config file missing error install this lib
	sudo apt-get install libmysqlclient-dev

	mysql.server start
	mysql -u root -p password
	create database projectx;
    
	python manage.py makemigrations projectxs
	python manage.py migrate



###To Run django
	python manage.py runserver



