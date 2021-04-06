from django.shortcuts import render

def home(request):
	# request.session.flush()
	return render(
		request,
		"home/home.html")
