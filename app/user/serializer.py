from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User Model """

    class Meta:
        model = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {'password':{'write_only':True,'min_length':5}}

    def create(self, validated_data):
        """ Create User with Hashed Password """

        return get_user_model().objects.create_user(**validated_data)