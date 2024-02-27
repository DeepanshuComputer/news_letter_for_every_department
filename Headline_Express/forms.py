from django.forms import ModelForm
from .models import subs_info , news


class Subs_Form(ModelForm):
    class Meta:
         model = subs_info
         fields = "__all__" 
         
         
class News_Form(ModelForm):
    class Meta:
        model = news
        fields = "__all__"
















