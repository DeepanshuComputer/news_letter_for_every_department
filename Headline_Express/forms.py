from django.forms import ModelForm
from .models import subs_info


class Subs_Form(ModelForm):
    class Meta:
         model = subs_info
         fields = "__all__" 
















