from django import forms

BIRTH_YEAR_CHOICES = ['2002', '2003', '2005', '2006']
BIRTH_MONTH_CHOICES = {
    0: 'february', 
    1: 'march', 
    2: 'september', 
    3: 'october', 
    4: 'december'
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
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), min_length=15)
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, months=BIRTH_MONTH_CHOICES))
    price = forms.DecimalField(required=False, label="Price of the comment", initial=7.5)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_country = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COUNTRY_CHOICES)
    favorite_personas = forms.MultipleChoiceField(choices=FAVORITE_PERSONA_CHOICES)
    favorite_players = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_PLAYER_CHOICES)
    agreed = forms.BooleanField(initial=True)