from django import forms
from phones.models import Phone


class PhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, fields) in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'
    class Meta:
        BRANDS = (('Apple','Apple'),
                  ('Samsung','Samsung'),
                  ('Huawei', 'Huawei'),
                  ('Lenovo', 'Lenovo'),
                  ('LG', 'LG'),
                  ('Xiaomi', 'Xiaomi'),
                  ('Аnother','Аnother')
                  )
        CONDITIONS = (
            ('Like new','Like new'),
            ('Good','Good'),
            ('Poor','Poor'),
            ('Faulty','Faulty'),

        )
        CAPACITY_CHOICES = (
            ('16','16'),
            ('64','64'),
            ('128','128'),
            ('256','256'),
            ('512','512'),
        )
        model = Phone
        exclude = ('owner',)
        widgets = {
            'brand':forms.Select(choices=BRANDS),
            'condition':forms.Select(choices=CONDITIONS),
            'capacity':forms.Select(choices=CAPACITY_CHOICES)
        }
