from django.db import models
from django.core.validators import RegexValidator

class Banner(models.Model):
    body = models.CharField(max_length=255)
    description = models.CharField(max_length=2555)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    github = models.CharField(max_length=255)

class Experience(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=2555)
    data = models.DateField(auto_now=True)

class Info(models.Model):
    adress = models.CharField(max_length=55)
    phone = models.CharField(max_length=13, blank=True, null=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    email = models.EmailField()
    RegexValidator(
        regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Invalide email',
        code='Invalid email'
    )


class Awards(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=2555)

class Contact(models.Model):
    description = models.CharField(max_length=2555)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)


class Contact_us(models.Model):
    full_name = models.CharField(max_length=155)
    email = models.EmailField()
    RegexValidator(
        regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Invalide email',
        code='Invalid email'
    )
    subject = models.CharField(max_length=255)
    message = models.TextField()