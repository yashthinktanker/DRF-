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
    
# -------------- InstaUser Seriliser -----------------------
from rest_framework import serializers

class InstaPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaLike
        fields = ['user', 'post']


    def validate(self, data):
        if InstaLike.objects.filter(user = data['user'],post=data['post']).exists():
            raise serializers.ValidationError('Alredy liked')
        return data 

class InstaPostSerializer(serializers.ModelSerializer):
    likes = InstaPostLikeSerializer(many=True, read_only=True)
    total_likes = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = InstaPost
        fields = ["id", "caption", "image", "likes", "total_likes"]
   
class InstaUserSerializer(serializers.ModelSerializer):
    posts = InstaPostSerializer(many=True, read_only=True)
    total_post = serializers.IntegerField(source='posts.count', read_only=True)

    class Meta:
        model = InstaUser
        fields = "__all__"
        


  

