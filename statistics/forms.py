from django import forms
from django.db.models import Q
from statistics.models import *
from creation.models import FossCategory, TutorialResource, TutorialDetail

class LearnerForm(forms.ModelForm):
    foss = forms.ModelChoiceField(label='Foss', cache_choices=True, widget = forms.Select(attrs = {}), queryset = FossCategory.objects.filter(pk__in = TutorialResource.objects.filter(Q(status = 1) | Q(status = 2), language__name = 'English').values_list('tutorial_detail__foss__id').distinct()), help_text = "", error_messages = {'required':'Foss field required.'})
 
    class Meta:
        model = Learner
