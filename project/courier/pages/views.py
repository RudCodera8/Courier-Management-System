from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.urls import path
from mainpage import models
# Create your views here.
#def search(request, *args, **kwargs):
#	return render(request, 'search.html', {})
def search(request):
	if request.method=='POST':
		srch = request.POST['srh']

		if srch:
			match = models.student.objects.filter(Q(name__icontains=srch)       |
									   	   Q(rollnumber__icontains=srch) |
									   	   Q(service__icontains=srch)

									       )
			if match:
				return render(request, 'search.html', {'sr':match})
			else:
				messages.error(request, 'nor result found. Please Check Later. It has not reached the mail room.')
		else:
			return HttpResponseRedirect('/search/')
    
	return render(request, 'search.html')
	