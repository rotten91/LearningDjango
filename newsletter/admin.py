from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    form = SignUpForm
    list_display = ["full_name", "__unicode__", "timestamp", "updated"]
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)

