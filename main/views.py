from django.shortcuts import render
from .models import Education, Publication

def index(request):

    education = Education.objects.order_by('-end_year')

    dados = {
        'nome': 'Marco Marinho',
        'titulo': 'Doctor of Electrical Engineering and Computer Science',
        'intro': 'Welcome to my personal website. Here you can have an overview of my current and past research topics, have access to the work I have developed and am currently developing, and take a look at the presentations I have used to explain my work. Feel free to contact me directly if any of my research topics or works have interested you.',
        'linkedin': 'https://www.linkedin.com/in/marco-antonio-marques-marinho-166553140/',
        'github': 'https://github.com/marco-marinho',
        'researchgate': 'https://www.researchgate.net/profile/Marco_Marinho2',
        'schoolar': 'https://scholar.google.com.br/citations?user=DwO2P_UAAAAJ&hl=en'
    }

    context = {
        'dados': dados,
        'education': education,
    }

    return render(request, 'main/main-blue.html', context)
