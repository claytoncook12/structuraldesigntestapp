from django.db import models
import datetime as dt

att_abs_type_choices = [
    ('1REG','1REG'),
    ('6ADL','6ADL'),
    ('ANLL','ANLL')
]

location_choices = [
    ('offi','office'),
    ('home','home'),
    ('fiel','field')
]

class RC(models.Model):
    rc_desc = models.CharField(max_length=50)

    def __str__(self):
        return (f'{self.id} {self.rc_desc}')

class SignInEntry(models.Model):
    att_abs_type = models.CharField(max_length=4,choices=att_abs_type_choices,default='1REG')
    location = models.CharField('Work Location For Day',max_length=4, choices=location_choices, default='offi')
    date = models.DateField('Sign In Date', default=dt.date.today)
    time = models.TimeField('Sign In Time',default=dt.time(7, 00))
    comment = models.TextField('Notes:', null=True, blank=True)

    def __str__(self):
        return (f'Sign_In:{self.date} {self.time} {self.location}')

class SignOutEntry(models.Model):
    date = models.DateField('Sign Out Date', default=dt.date.today)
    time = models.TimeField('Sign Out Time',default=dt.time(7, 00))
    lunch_start = models.TimeField('Lunch Start',default=dt.time(12, 00))
    lunch_end = models.TimeField('Lunch End',default=dt.time(12, 30))
    comment = models.TextField('Notes:', null=True, blank=True)

    def __str__(self):
        return (f'Sign_In:{self.date} {self.time}')
