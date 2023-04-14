#Code for Video 6:
# # I have created this file - Soham
# from django.http import HttpResponse
# def  index(request):
#     return HttpResponse('''<h1> SOHAM RAY </h1> <a href = "https://www.codewithharry.com/videos/python-django-tutorials-hindi-10/"> Django Playlist  </a> <br> <a href = "https://indianrail.gov.in"> Indian Railways  </a><br> <a href = "https://bit.ly/3fi5II1">  Science Archives  </a> <br>  <a href = "https://www.youtube.com"> Youtube </a> <br>  <a href = "https://www.facebook.com"> Facebook  </a>''')
#
# def  about(request):
#     return HttpResponse("About Soham Bhai")

#Code for Video 7:
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Home")
    params = {'name': 'Soham', 'place': 'Serampore'}
    return render (request , 'index.html',params)


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext =  analyzed
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text

    if(removepunc != "on" and fullcaps!="on"and extraspaceremover!="on" and newlineremover != "on" ):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("Newline Remove")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover  <a href = '/'> Back </a>")
#
# def charcount(request):
#     return HttpResponse("charcount ")