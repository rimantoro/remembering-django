from django import forms
from .models import GoodsType

class GoodsTypeForm(forms.ModelForm):
    goods_type = forms.CharField(label='Name', help_text = "type name")
    temp_min = forms.IntegerField(label='Min. Temp', help_text = "minimum temperature threshold (in celcius)")
    temp_max = forms.IntegerField(label='Max. Temp', help_text = "maximum temperature threshold (in celcius)")

    class Meta:
        model = GoodsType
        fields = '__all__'