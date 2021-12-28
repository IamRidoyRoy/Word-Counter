from django.http import HttpResponse
from django.shortcuts import render 
import operator
def homepage(request):
    return render(request, 'home.html', { 'hithere': 'This is me'}) # I can pass here a dictionary 


def about(request):
    return render(request, 'about.html')


def eggs(request):
    return HttpResponse("Hey Eggs are great!")


def count(request):
    fulltext = request.GET["Fulltext"]
    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] =1

    sortword = sorted(worddict.items(), key= operator.itemgetter(1), reverse=True )
   
    return render(request, 'count.html',
     {  'fulltext'  : fulltext, 
        'wcount'    : len(wordlist),
        'sortword'  : sortword, 

    
    })



    
