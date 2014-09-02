from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from whiteboard.models import Match

def index(request):
    context = RequestContext(request)
    match_list = Match.objects.all()
    context_dict = {'matches': match_list}
    if request.method == "POST":
        if 'adi_toggle' in request.POST:
	    adi_toggle = request.POST.get('adi_toggle', None)
	    a = Match.objects.get(id=adi_toggle)
	    if a.adi == False:
	        a.adi = True
	    elif a.adi == True:
	        a.adi = False
    	    a.save()
	elif 'bt_toggle' in request.POST:	
	    bt_toggle = request.POST.get('bt_toggle', None)
            a = Match.objects.get(id=bt_toggle)
            if a.bt == False:
                a.bt = True
            elif a.bt == True:
                a.bt = False
            a.save()
	elif 'gal_toggle' in request.POST:
            gal_toggle = request.POST.get('gal_toggle', None)
            a = Match.objects.get(id=gal_toggle)
            if a.gal == False:
                a.gal = True
            elif a.gal == True:
                a.gal = False
            a.save()
    return render_to_response('whiteboard/index.html', context_dict, context)
