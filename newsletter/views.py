from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from proj1.settings import EMAIL_HOST_USER


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
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        form_email = form.cleaned_data.get("email")
        form_fullname = form.cleaned_data.get("fullname")
        form_message = form.cleaned_data.get("message")
        form_subject = "Site contact form message"
        contact_message = "%s: %s via %s" %(form_fullname, form_email, form_message)
        from_email = EMAIL_HOST_USER
        to_email = [from_email]
        send_mail(form_subject, contact_message, from_email, to_email, fail_silently=False)


    return render(request, 'contact.html', context)

























