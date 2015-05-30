from django.shortcuts import render
from .forms import SignUpForm, ContactForm

def home(request):
    title = "Welcome, Please Sign Up"
    form = SignUpForm(request.POST or None)
    if request.user.is_authenticated():
        title = "Welcome %s" % request.user

    context = {
        "template_title": title,
        "form": form,

    }
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")

        if not full_name:
            full_name = "Mr Anonymous"
        instance.full_name = full_name
        instance.save()
        context = {
            "template_title": "Thanks for joining our newsletter, Have a nice day!"
        }

    return render(request, 'home.html', context)


def contact(request):                           #contact view
    form = ContactForm(request.POST or None)
    context = {

        "form": form

    }
    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value
    #     # email = form.cleaned_data.get("email")
    #     # fullname = form.cleaned_data.get("fullname")
    #     # message = form.cleaned_data.get("message")
    #       print email, fullname, message

    return render(request, 'contact.html', context)

























