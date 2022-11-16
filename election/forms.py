from django import forms

class VoteForm(forms.Form):
    vote_id = forms.CharField(max_length=1)
    