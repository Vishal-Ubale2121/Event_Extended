from django import forms
from events.models import Event, Team,Mood


class EventForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].required = False
    #     self.fields['result'].required = False

    class Meta:
        model = Event
        fields = ['event_name']


class ParticipationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ParticipationForm, self).__init__(*args, **kwargs)
        self.fields['event'].required = False

    class Meta:
        model = Team
        fields = ['team_name']


#############################################################

from django import forms
from events.models import Mood
from events.models import Post

class MoodForm(forms.ModelForm):

   # def __init__(self, *args, **kwargs):
   #   super(MoodForm, self).__init__(*args, **kwargs)
   #    self.fields['event1'].required = False
   #    self.fields['event2'].required = False
   #    self.fields['event3'].required = False
   #    self.fields['event4'].required = False
   #    self.fields['event5'].required = False




    class Meta:
        model = Mood
        fields = "__all__"


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title']
        labels = {
            'title': 'Member Name :'
        }
        help_texts = {
            'title': 'Yardum edelum'
        }
        error_messages = {
            'title': {
                'max_length': 'cok uzun baba'
            }
        }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = 'required'
        self.fields['title'].error_messages = {
            'max_length': 10,
            'required': 5
        }
        for field in self.fields.values():
            field.error_messages = {
                'required': '{} field is required.'.format(field.label)
            }


SOME_CHOICES = (
    ('db-value', 'Display Value'),
    ('db-value2', 'Display Value2'),
)
INT_CHOICES = [tuple([x, x]) for x in range(0, 100)]
YEARS = [x for x in range(1980, 2031)]


class SearchForm(forms.Form):
    q = forms.CharField(label='Text', widget=forms.Textarea(attrs={'rows': 4, 'cols': 10}))
    IntegerField = forms.IntegerField(widget=forms.Select(choices=INT_CHOICES))
    EmailField = forms.EmailField()
    DateField = forms.DateField(
        initial='2010-01-10', widget=forms.SelectDateWidget(years=YEARS))

    def clean_q(self, *args, **kwargs):
        q = self.cleaned_data.get('q')
        if q == 'vishal':
            raise forms.ValidationError('You cant search')
        return q

    def clean_IntegerField(self, *args, **kwargs):
        IntegerField = self.cleaned_data.get('IntegerField')
        if IntegerField < 10:
            raise forms.ValidationError('The integer must be greater than 10')
        return IntegerField