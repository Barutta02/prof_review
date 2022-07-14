from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
# Create your views here.
def review(request):
    submitted = False
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid() & control_form_bad_words(form):
            form.save()
            return HttpResponseRedirect('/review?submitted=True')  
    else:
        form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True
    try:
        filtro = str(request.GET['cognome'])
        recensioni = Review.objects.filter(cognome = filtro )
        recensioni |= Review.objects.filter(nome = filtro ) #operatore di unione, recensioni non è una lista
        return render(request, 'review/index.html' , { 'review':recensioni, 'form':form, 'submitted':submitted})
    except:
        recensioni = Review.objects.all()
        return render(request, 'review/index.html' , { 'review':recensioni , 'form':form , 'submitted':submitted, 'Found':False})
   

badwords = [
        "cazzo",
        "figa",
        "merda",
        "porco",
        "stronzo",
        "bastardo",
        "asshole",
        "boia",
        "fanculo",
        "vaffanculo",
        "negro",
        "frocio",
        "porcodio",
        "porcamadonna",
        "bestia",
        "troia",
        "ass",
        "bitch",
        "bastard",
        "cunt",
        "dick",
        "dike",
        "dildo",
        "fuck",
        "gay",
        "hoe",
        "nigger",
        "pussy",
        "slut",
        "whore",
        "god damn",
        "goddamn",
        ";"
    ]

def block_bad_words(testo):
    testo = testo.lower()
    for word in badwords:
        if word in testo:
             return False
    return True
       
def control_form_bad_words(form):
   return block_bad_words(form['nome'].value()) & block_bad_words(form['cognome'].value()) & block_bad_words(form['descrizione'].value())