from django import forms

BIRTH_YEAR_CHOICES = ['2002', '2003', '2005', '2006']
BIRTH_MONTH_CHOICES = {
    0: 'February', 
    1: 'March', 
    2: 'September', 
    3: 'October', 
    4: 'December'
}
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
FAVORITE_COUNTRY_CHOICES = [
    ('bd', 'Bangladesh'),
    ('pk', "Pakistan"),
    ('in', "India")
]
FAVORITE_PERSONA_CHOICES = [
    ('elon', 'Elon Musk'),
    ('juck', "Mark Juckerburg"),
    ('steve', "Steve Jobs"),
    ('gates', "Bill Gates")
]
FAVORITE_PLAYER_CHOICES = [
    ('mess', 'Leonel Messi'),
    ('ron', "Chirstiano Ronaldo"),
    ('ney', "Neymar Jr")
]

class DemoForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), min_length=15, required=False)
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=False)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, months=BIRTH_MONTH_CHOICES), required=False)
    price = forms.DecimalField(label="Price of the comment", initial=7.5, required=False)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES, required=False)
    favorite_country = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COUNTRY_CHOICES, required=False)
    favorite_personas = forms.MultipleChoiceField(choices=FAVORITE_PERSONA_CHOICES, required=False)
    favorite_players = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_PLAYER_CHOICES, required=False)
    typed_choices = forms.TypedChoiceField(choices=[('test', "Test"), ('test2', "Test2")], required=False)
    duration = forms.DurationField(required=False)
    file = forms.FileField(required=False)
    # file_path = forms.FilePathField(path="/static", required=False)
    url = forms.URLField(required=False)
    time = forms.TimeField(label_suffix="label_suffix", label="Yo", help_text="Yo means time in a language", error_messages={'invalid': "You messed up bro, get out."})
    agreed = forms.BooleanField(initial=True, disabled=True, required=False)