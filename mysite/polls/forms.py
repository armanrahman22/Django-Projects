from django import forms
from polls.models import PollingLocation,Choice,Poll

class PollForm(forms.Form):
