from django.db import models

# Create your models here.


class login_table(models.Model):
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    type= models.CharField(max_length=30)


class user_table(models.Model):
    LOGIN= models.ForeignKey(login_table,on_delete=models.CASCADE)
    Name= models.CharField(max_length=100)
    Place= models.CharField(max_length=100)
    Post= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Phone= models.BigIntegerField()
    Gender= models.CharField(max_length=100)


class complaint_table(models.Model):
    Complaint= models.CharField(max_length=100)
    Date= models.DateField()
    Reply= models.CharField(max_length=100)
    USER= models.ForeignKey(user_table, on_delete=models.CASCADE)

class notification_table(models.Model):
    Notification= models.CharField(max_length=100)
    Date= models.DateField()


class Feedback(models.Model):
    Feedback= models.CharField(max_length=100)
    Rating= models.CharField(max_length=100)
    Date= models.DateField()
    USER= models.ForeignKey(user_table,on_delete=models.CASCADE)


