from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from whiteboard.models import Match

def index(request):
    context = RequestContext(request)
    match_list = Match.objects.all()
    context_dict = {'matches': match_list}
    return render_to_response('whiteboard/index.html', context_dict, context)
