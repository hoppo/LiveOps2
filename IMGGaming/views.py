from django.shortcuts import render, render_to_response
from django.template import RequestContext
from IMGGaming.models import Report
from IMGGaming.forms import ReportForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail

def index(request):
    context = RequestContext(request)
    report_list = Report.objects.all()
    context_dict = {'reports': report_list}
    for report in report_list:
        report.url = report.event.replace(' ', '_')
    response = render_to_response('IMGGaming/index.html', context_dict, context)
    visits = int(request.COOKIES.get('visits', '0'))
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).days > 0:
            response.set_cookie('visits', visits+1)
            response.set_cookie('last_visit', datetime.now())
    else:
        response.set_cookie('last_visit', datetime.now())
    return response


def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the about context"}
    return render_to_response('IMGGaming/about.html', context_dict, context)

def report(request, report_name_url):
    context = RequestContext(request)
    report_name = report_name_url.replace('_', ' ')
    try:
        report = Report.objects.get(event=report_name)
    except Report.DoesNotExist:
	return HttpResponse('nothing doing')
    context_dict = {'report_name': report_name, 'report': report}
    return render_to_response('IMGGaming/report.html', context_dict, context)

@login_required
def add_report(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            cd = form.cleaned_data
	    message = 'Diagnosis: '+cd['diagnosis']+'\n'+'Impact: '+cd['impact']+'\n'+'Resolution: '+cd['resolution']+'\n'+'Responsibility: '+cd['responsibility']+'\n'+'Action: '+cd['action']
	    send_mail(
                cd['event'],
                message,
                cd.get('email', 'johnhopkins@gmx.co.uk'),
                ['john@johnhopkins.co.uk'],
            )
	    return index(request)
        else:
            print form.errors
    else:
        form = ReportForm()
    return render_to_response('IMGGaming/add_report.html', {'form': form}, context)

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
            'IMGGaming/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/IMGGaming/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('IMGGaming/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/IMGGaming/')
