from django import forms
from timesheet.models import SignInEntry, SignOutEntry
import datetime as dt

# Create Time Choices
MINUTES_CHOICES = [0, 15, 30, 45]
HOURS_CHOICES = [x for x in range(0, 24)]
TIME_CHOICES = []
for hour in HOURS_CHOICES:
    for minute in MINUTES_CHOICES:
        create_time = dt.time(hour=hour,minute=minute)
        TIME_CHOICES.append((create_time,create_time.strftime('%I:%M %p')))

# Create Lunch Time Choices
HOURS_CHOICES = [x for x in range(10, 15)]
LUNCH_TIME_CHOICES = []
for hour in HOURS_CHOICES:
    for minute in MINUTES_CHOICES:
        create_time = dt.time(hour=hour,minute=minute)
        LUNCH_TIME_CHOICES.append((create_time,create_time.strftime('%I:%M %p')))

class DateInput(forms.DateInput):
    input_type = 'date'

class SignInEntryForm(forms.ModelForm):
    class Meta:
        model = SignInEntry
        exclude = ["user"]
        widgets = {'date': DateInput(), 'time': forms.Select(choices=TIME_CHOICES)}
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.request.user
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class SignOutEntryForm(forms.ModelForm):
    class Meta:
        model = SignOutEntry
        exclude = ["user"]
        widgets = {'date': DateInput(),
            'time': forms.Select(choices=TIME_CHOICES),
            'lunch_start': forms.Select(choices=LUNCH_TIME_CHOICES),
            'lunch_end': forms.Select(choices=LUNCH_TIME_CHOICES)
            }
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.request.user
        if commit:
            instance.save()
            self.save_m2m()
        return instance