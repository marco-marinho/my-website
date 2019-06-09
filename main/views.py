from django.shortcuts import render, get_list_or_404, redirect
from .models import Education, Publication, Research, Teaching, Resource
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

import urllib
import json

def index(request):

    education = Education.objects.order_by('-end_year')

    dados = {
        'nome': 'Stephanie Alvarez',
        'titulo': 'Doctor of Electrical Engineering and Network Information Technologies',
        'intro': 'Stephanie Alvarez holds a PhD in Electrical Engineering and Network Information Technologies from the University of Brasilia (Unb), Brazil in cotutelle with the Open University of Catalonia (UOC), Spain. Before starting her PhD, she concluded her MSc in electrical engineering at Unb from where she built a good background in languages programming such as Matlab, Java, C and the general knowledge about designing different kinds of algorithms, including recursive algorithms. Her main research topics are optimization and simulation, machine learning and adaptive signal processing. Stephanie’s available for new research opportunities on her topics of interest, as well as private consultations.',
        'linkedin': 'https://www.linkedin.com/in/stephanie-alvarez-fernandez-43b58633/',
        'orcid': 'https://orcid.org/0000-0002-0884-8925',
        'researchgate': 'https://www.researchgate.net/profile/Stephanie_Alvarez',
        'lattes': 'http://lattes.cnpq.br/0059463083150585'
    }

    publications = Publication.objects.order_by('-date')[:2]

    context = {
        'dados': dados,
        'education': education,
        'publications': publications,
    }

    return render(request, 'main/main-blue.html', context)


def education(request):

    education = Education.objects.order_by('-end_year')

    context = {
        'education': education,
    }

    return render(request, 'main/education.html', context)


def research(request):

    research = Research.objects.order_by('research')

    context = {
        'research': research,
    }

    return render(request, 'main/research.html', context)


def publications(request):

    publications = Publication.objects.order_by('-date')

    context = {
        'publications': publications,
    }

    return render(request, 'main/publications.html', context)


def teaching(request):

    categories = Teaching.objects.values('level').distinct()
    classes = Teaching.objects.values()

    context = {
        'categories': categories,
        'classes': classes,
    }

    return render(request, 'main/teaching.html', context)


def contact(request):

    context = {
        'nome': 'Stephanie M. Alvarez Fernandez',
        'skype': 'stephaniemaf(at)outlook(dot)com',
        'email': 'stephaniemaf(at)gmail(dot)com',
        # 'linkedin': 'https://www.linkedin.com/in/marco-antonio-marques-marinho-166553140/',
        # 'github': 'https://github.com/marco-marinho',
        # 'researchgate': 'https://www.researchgate.net/profile/Marco_Marinho2',
        # 'schoolar': 'https://scholar.google.com.br/citations?user=DwO2P_UAAAAJ&hl=en'
    }

    return render(request, 'main/contact.html', context)


def resources(request, topicid):

    resource = get_list_or_404(Resource, topic__id=topicid)

    context = {
        'resources': resource
    }

    return render(request, 'main/resources.html', context)


def sendmessage(request):

    if request.method == 'POST':

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:

            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            send_mail(
                'Website contact',
                'Você recebeu uma messagem de: ' + name + '\nE-mail de contato: ' + email + '\n \nMensagem: ' + message,
                'marinho@gmx.com',
                ['marcoobom@gmail.com'],
                fail_silently=False
            )

            messages.success(request, 'Your message has been sent, I will get back to you as soon as possible.')

            return redirect('/contact')
