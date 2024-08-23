from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# This is for the serializer where the tokens is creaed use the url in the urls.py, looks like the form.py 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # Accept password when creating a user but don't show the password
   
   # Validate the data 
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}