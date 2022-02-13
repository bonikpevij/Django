from django.db import models
class Person(models.Model):
    registration_numb = models.IntegerField(max_length=100)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1)
    birth_day = models.DateField()
    email=models.EmailField()
    phone_numb=models.CharField(max_length=20)
    passwords = models.CharField(max_length=50)
    friends=models.ManyToManyField('self')
    faculty = models.ForeignKey('Person',on_delete=models.CASCADE)
class Message(models.Model):
    author = models.ForeignKey('Person',on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(max_length=30)
class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
class Campus(models.Model):
    name = models.CharField(max_length=30)
    adress= models.CharField(max_length=60)
class Job(models.Model):
    title = models.CharField(max_length=30)
class Cursus(models.Model):
    title = models.CharField(max_length=30)
class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus',on_delete=models.CASCADE)
    job = models.ForeignKey('Job',on_delete=models.CASCADE)
class Student(Person):
    cursus = models.ForeignKey('Cursus',on_delete=models.CASCADE)
    year = models.IntegerField()