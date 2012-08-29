from django.http import *

# Create your views here.
def home(request):
	if not request.user.is_authenticated():
		print "not logged in!"
		return HttpResponseRedirect('/cas/login/')
	else:
		print request.user
		return HttpResponse(request.user.username)
