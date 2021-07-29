from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from timesheet.forms import SignInEntryForm, SignOutEntryForm

def timesheet_home(request):
    if request.user.is_anonymous:
        return redirect('account_login')
    else:
        return render(request, 'timesheet/home.html')

@login_required
def timesheet_signin(request):
    if request.method == 'POST':
        form = SignInEntryForm(request.POST)
        form.user_id = request.user_id
        breakpoint()
        if form.is_valid():
            form.save()
            return redirect('timesheet_home')
    else:
        form = SignInEntryForm()
    return render(request, 'timesheet/timesheet_signin.html', {'form': form})

@login_required
def timesheet_signout(request):
    if request.method == 'POST':
        pass
    else:
        form = SignOutEntryForm()
    return render(request, 'timesheet/timesheet_signout.html', {'form': form})

@login_required
def timesheet_assignhours(request):
    return render(request, 'timesheet/timesheet_assignhours.html')

def timesheet_checklist(request):
    return render(request, 'timesheet/timesheet_checklist.html')