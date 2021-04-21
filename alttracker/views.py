from django.shortcuts import render, redirect

def home(request):
	# request.session.flush()
    return redirect('wowprof_home')
	# return render(
	# 	request,
	# 	# "home/home.html"
 #        "wowprof/wowprof_home.html")
