from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from timesheet.forms import SignInEntryForm, SignOutEntryForm
from timesheet.models import SignInEntry

def timesheet_home(request):
    if request.user.is_anonymous:
        return redirect('account_login')
    else:
        entries = SignInEntry.objects.filter(user=request.user)
        return render(request, 'timesheet/home.html', {'entries': entries})

@login_required
def timesheet_signin(request):
    if request.method == 'POST':
        form = SignInEntryForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('timesheet:timesheet_home')
    else:
        form = SignInEntryForm(request)
    return render(request, 'timesheet/timesheet_signin.html', {'form': form})

@login_required
def timesheet_signout(request):
    if request.method == 'POST':
        form = SignOutEntryForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('timesheet:timesheet_home')
    else:
        form = SignOutEntryForm(request)
    return render(request, 'timesheet/timesheet_signout.html', {'form': form})

@login_required
def timesheet_assignhours(request):
    return render(request, 'timesheet/timesheet_assignhours.html')

def timesheet_checklist(request):
    return render(request, 'timesheet/timesheet_checklist.html')