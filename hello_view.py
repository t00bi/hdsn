from django.http import HttpResponse

def hello(request):
	message = "<html><body>Hello, Django!</body></html>"
	return HttpResponse(message)