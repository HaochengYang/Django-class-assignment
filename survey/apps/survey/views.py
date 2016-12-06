from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def survey(request):
    return render(request, "survey/survey.html")

def result(request):
    context={
        "name": request.POST['name'],
        "location":request.POST['location'],
        "Language": request.POST['Language'],
        "comment":request.POST['comment']
         }
    return render(request, "survey/result.html",context)
