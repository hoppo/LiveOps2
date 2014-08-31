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
            b = Match.objects.get(id=bt_toggle)
            if b.bt == False:
                b.bt = True
            elif b.bt == True:
                b.bt = False
            b.save()
    return render_to_response('whiteboard/index.html', context_dict, context)
