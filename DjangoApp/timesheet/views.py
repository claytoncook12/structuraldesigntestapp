from django.shortcuts import render, redirect
from timesheet.forms import SignInEntryForm, SignOutEntryForm

# Create your views here.
def timesheet_home(request):
    if request.user.is_anonymous:
        return redirect('account_login')
    else:
        return render(request, 'timesheet/home.html')

def timesheet_signin(request):
    if request.method == 'POST':
        pass
    else:
        form = SignInEntryForm()
    return render(request, 'timesheet/timesheet_signin.html', {'form': form})

def timesheet_signout(request):
    if request.method == 'POST':
        pass
    else:
        form = SignOutEntryForm()
    return render(request, 'timesheet/timesheet_signout.html', {'form': form})

def timesheet_assignhours(request):
    return render(request, 'timesheet/timesheet_assignhours.html')

def timesheet_checklist(request):
    return render(request, 'timesheet/timesheet_checklist.html')