from django.shortcuts import render_to_response
from search_log_apps.models import Response
from django.template import RequestContext


def view_log(request):
  response = Response.objects.all()
  return render(request, 'search_log_app.html')
