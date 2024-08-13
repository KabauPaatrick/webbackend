from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name','last_name','username', 'email', 'phone_number', 'address', 'password')

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = self.context.get('request').data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
