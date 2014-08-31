from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from whiteboard.models import Match

def index(request):
    context = RequestContext(request)
    match_list = Match.objects.all()
    context_dict = {'matches': match_list}
    if request.method == "POST":
        bt_toggle = request.POST.get('bt_toggle', None)
	#toggle match.bt
	a = Match.objects.get(id=bt_toggle)
	if a.bt == False:
	    a.bt = True
	    a.save()
	#return HttpResponse(a.bt)
    return render_to_response('whiteboard/index.html', context_dict, context)
