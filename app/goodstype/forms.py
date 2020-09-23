from django import forms
from .models import GoodsType

class GoodsTypeForm(forms.ModelForm):
    goods_type = forms.CharField(help_text = "type name")
    temp_min = forms.IntegerField(help_text = "minimum temperature threshold (in celcius)")
    temp_max = forms.IntegerField(help_text = "maximum temperature threshold (in celcius)")

    class Meta:
        model = GoodsType
        fields = ('goods_type',)