from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Posting, Comment
from rest_framework.fields import ReadOnlyField

class PostingSerializer(serializers.ModelSerializer): #Hyperlinked
    author_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posting
        fields = ('title','like','content','photo','gps','author_username','id')#url ,'created','updated','id',



class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
    author_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posting
        fields = ('title','id','author_username')
    #    fields = ('id','author_username','title','like','content','photo','gps','created','updated')



class CommentSerializer(serializers.ModelSerializer):
    author_username = ReadOnlyField(source='author.username')
    #posting = ReadOnlyField(source='posting')
    class Meta:
        model = Comment
        fields = ('posting','reply','author_username')#(,'posting','reply','c_created','c_updated')

