from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Student(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)
#     name=models.CharField(max_length=20)
#     roll=models.IntegerField()
#     Address=models.CharField(max_length=30)
#     Active=models.BooleanField()
#     image = models.ImageField(upload_to='images',null=True, blank=True)

# def __str__(self):
#     return self.name

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=20)
    SUBJECT_CHOICES = [
        ('full', 'Full-Stack Web Development'),
        ('mobile', 'Mobile App Development'),
        ('data', 'Data Science'),
        ('big_data', 'Big Data and Hadoop'),
        ('ethical', 'Ethical Hacking and Peenertration Testing'),
        ('cyber', 'Cybersecurity Fundamentals'),
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='full')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    SUBJECTT_CHOICES = [
        ('onlinne', 'Online'),
        ('Phyical', 'Physical'),
            ]
    Address=models.CharField(max_length=30)
    Class_type=models.CharField(max_length=50, choices=SUBJECTT_CHOICES, default='physical')
    image = models.ImageField(upload_to='images',null=True, blank=True)

    def __str__(self):
        return self.name


    def get_subject_cost(self):
        subject_costs = {
            'full': 30000.00,
            'mobile': 25000.00,
            'data': 35000.00,
            'big_data': 28000.00,
            'ethical': 25000.00,
            'cyber': 18000.00,
        }
        return subject_costs.get(self.subject, 0.00)
