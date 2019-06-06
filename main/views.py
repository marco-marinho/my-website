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
        'nome': 'Marco Marinho',
        'titulo': 'Doctor of Electrical Engineering and Computer Science',
        'intro': 'Welcome to my personal website. Here you can have an overview of my current and past research topics, have access to the work I have developed and am currently developing, and take a look at the presentations I have used to explain my work. Feel free to contact me directly if any of my research topics or works have interested you.',
        'linkedin': 'https://www.linkedin.com/in/marco-antonio-marques-marinho-166553140/',
        'github': 'https://github.com/marco-marinho',
        'researchgate': 'https://www.researchgate.net/profile/Marco_Marinho2',
        'schoolar': 'https://scholar.google.com.br/citations?user=DwO2P_UAAAAJ&hl=en'
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
        'nome': 'Marco A. M. Marinho',
        'skype': 'marco(dot)marinho(at)outlook(dot)com',
        'email': 'marco(dot)marinho(at)ieee(dot)org',
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
