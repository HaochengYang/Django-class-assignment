from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class Usermanager(models.Model):
    def reg(self, data):
        error = self.validate_inputs(request)
        if error:
          return(false,error)
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        return(True,User)

    def login(self, data):
        try:
            user = User.objects.get(email=request.POST['email'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.password.encode()):
                return(True, user)
        except ObjectDoesNotExist:
            pass
        return(False,["Invalid Login."])

    def register(self, data):
        if not request.POST['first_name']:
            error.append.POST['First name can not be blank.']
        if not request.POST['last_name']:
            error.append.POST['Last name can not be blank.']
        if not request.POST['email']:
            error.append.POST['Email name can not be blank.']
        elif not EMAIL_REGEX.match(request.POST['email']):
            error.append.POST['Invalid Email']
        if len(request.POST['password']) < 8:
            error.append.POST['Password must be at least 8 characters.']
        if request.POST['password'] != request.POST['confirm']:
            error.append('password and password confirm must match.')


class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.TextField(max_length=1000)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    objects = Usermanager()
