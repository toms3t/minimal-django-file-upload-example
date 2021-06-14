minimal-django-file-upload-example
==================================

Project contains source code that was made originally for the [Django file upload example at StackOverflow](http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example).

The goal with minimal-django-file-upload-example is to demonstrate and teach how file uploading is done with Django. Because of the academic nature of the project all the extra functionality is left out. Otherwise you would have hard time to guess what is important and what is not.

The following Django versions are supported:
- [Django 3.0](https://docs.djangoproject.com/en/dev/releases/3.0/) | [source](../../tree/master/src/for_django_3-0)

Usage (Django 3.0)
------------------
[Django 3.0 supports Python 3.6, 3.7, and 3.8.](https://docs.djangoproject.com/en/dev/releases/3.0/#python-compatibility) Using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) is highly recommended although not strictly required.

	$ git clone https://github.com/axelpale/minimal-django-file-upload-example.git
	$ cd minimal-django-file-upload-example
	$ cd src/for_django_3-0
	$ pip install -r requirements.txt (only if you don't have Django 3.0 installed)
	$ python manage.py migrate
	$ python manage.py runserver

