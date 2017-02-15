# Django Forms

This time we are going to implement all forms in our application using Django Form class

All documentation about the use of [Django Forms](https://docs.djangoproject.com/en/1.10/topics/forms/).

## Refactoring

At this point you have a course system with different types of users.
Your task is to refactor the existing forms in your project.

The registration form, login form, create and edit course/lectures forms, etc. need to inherited the Form class, which Django provides.

### Example of RegisterForm

```python
from django import forms
from .models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
```

Your forms must have `save` methods and validators of the fields.

### Additional information
* [Form widgets](https://docs.djangoproject.com/en/1.10/ref/forms/widgets/)
* [Form Fields](https://docs.djangoproject.com/en/1.10/ref/forms/fields/)
* [Forms API](https://docs.djangoproject.com/en/1.10/ref/forms/api/)
