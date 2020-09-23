from rest_framework import serializers
from .models import GoodsType

class GoodsTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GoodsType
        fields = (
            'id', 'goods_type', 'temp_min', 'temp_max'
        )

