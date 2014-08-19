from src.apps import *

def book(request):
  j = JsonResult()
  return HttpResponse(j.json())