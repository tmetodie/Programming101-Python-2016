# Simple User Management with Django for Course System project

This time we are going to implement our own User management on top of Django.

Keep in mind that Django has a fairly complex [Authentication system](https://docs.djangoproject.com/en/1.10/topics/auth/) that is the prefered choice when we want to have users.

**But this time, we want to implement our own system**.

Here are the key parts:

## The User model

We want a dead-simple user model:

```python
class User(models.Model):
  email = models.EmailField(unique=True)
  password = models.CharField(_('password'), max_length=128)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
```

## Student and Lecturer models

You need to create inheritance! One User can be at the same time Student and Lecturer!

The interesting part comes when a student tries to create or delete lectures!
This can be done only by the lecturers.

Only teachers can create and modifies lectures and courses!

Your task is to detect who is the user and does he has the permission to do these kind of actions!


## Registration and Login forms

We need to have a way to register our users.

* Make a registration form that can be accessed at `/register` url.
* Make a login form that can be accessed at `/login` url.

Once a user has logged in, keep him logged in until he decides to log out. In order to to that, you will need [sessions](https://docs.djangoproject.com/en/1.9/topics/http/sessions/)

## Profile page that is login-protected

Create a simple `/profile` page that can only be accessed from a logged user.

If someone tries to access this page without a login, [redirect him to registration](https://docs.djangoproject.com/en/1.9/topics/http/shortcuts/#redirect)

In the profile page, have a logout button.

## Redirect scenarios & decorator check

Add the following redirect scenarios:

* If logged user tries to access `/register`, redirect him to `/profile`
* If logged user tries to access `/login`, redirect him to `/profile`
* If annon user tries to access `/profile`, redirect him to `/login`

In order to achieve that, in your app, in a file called `decorators.py` implement the following decorators:

```python
from .decorators import login_required, annon_required

@annon_required(redirect_url='/profile')
def register(request):
    ...


@annon_required(redirect_url='/profile')
def login(request):
    ...


@login_required(redirect_url='/login')
def profile(request):
    ...
```

## Adding user in the request

In the original Django auth system, there is a `request.user`, which is very helpful to access the user if the user is logged in.

Implement a [middleware](https://docs.djangoproject.com/en/1.9/topics/http/middleware/) that sets `request.user` to the actual logged in user or `None` if there isn't any.
