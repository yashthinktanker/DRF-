from .models import *
from rest_framework import serializers


class Brandserializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class Model_nameserializers(serializers.ModelSerializer):
    # brand = serializers.StringRelatedField()
    # brand = Brandserializers()
    # brand = serializers.HyperlinkedRelatedField(read_only=True,view_name="brand-detail")
    class Meta:
        model = Model_name
        fields = '__all__'
        
    def validate(self, data):
        if data['modelname']:
            if Model_name.objects.filter(modelname = data['modelname']).exists():
                raise serializers.ValidationError('select another model')      
        return data