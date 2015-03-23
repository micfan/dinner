from apps import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def book(request):
  j = JsonResult()
  return HttpResponse(j.json())