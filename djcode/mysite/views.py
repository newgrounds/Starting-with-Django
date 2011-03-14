from django.http import Http404, HttpResponse
# needed for second implementation
#from django.template import Context
#from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello world")
	
def current_datetime(request):
	current_date = datetime.datetime.now()
	# the following line has been replaced by locals implementation
	#now = datetime.datetime.now()
	# best implementation with shortcuts
	return render_to_response('current_datetime.html', locals())#{'current_date': now})
	
	# new implementation with template
	# this new implementation can be shortened with render_to_response()
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date': now}))
	
	# oldest version commented out:
	#html = "<html><body>It is now %s.</body></html>" % now
	
	# this line is needed for both other implementations
	#return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)