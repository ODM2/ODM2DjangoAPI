from django.shortcuts import render
from django import forms

# Create your views here.
from django.views.generic.edit import FormView

from odm2.models import *


class ODM2CoreForm(forms.Form):
    people = forms.ModelChoiceField(queryset=People.objects.all())
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    affiliation = forms.ModelChoiceField(queryset=Affiliation.objects.all())
    method = forms.ModelChoiceField(queryset=Method.objects.all())
    action = forms.ModelChoiceField(queryset=Action.objects.all())
    action_by = forms.ModelChoiceField(queryset=ActionBy.objects.all())
    sampling_feature = forms.ModelChoiceField(queryset=SamplingFeature.objects.all())
    feature_action = forms.ModelChoiceField(queryset=FeatureAction.objects.all())
    data_set = forms.ModelChoiceField(queryset=DataSet.objects.all())
    processing_level = forms.ModelChoiceField(queryset=ProcessingLevel.objects.all())
    related_action = forms.ModelChoiceField(queryset=RelatedAction.objects.all())
    taxonomic_classifier = forms.ModelChoiceField(queryset=TaxonomicClassifier.objects.all())
    unit = forms.ModelChoiceField(queryset=Unit.objects.all())
    variable = forms.ModelChoiceField(queryset=Variable.objects.all())
    result = forms.ModelChoiceField(queryset=Result.objects.all())


class ODM2CoreView(FormView):
    template_name = 'odm2/models_template.html'
    form_class = ODM2CoreForm
