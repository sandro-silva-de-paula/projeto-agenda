from django.shortcuts import render
from contact.models import Contact



def index(request):
    contacts = Contact.objects\
        .order_by("-id")\
        .filter(show=True)[10:20]
    context = {
        'contacts':contacts,
    }
    return render(
        request,
        'contact/index.html',
        context)
