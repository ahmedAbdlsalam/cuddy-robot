from rest_framework import serializers
from .models import *
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    # def create(self, *args, **kwargs):
    #     user = super().create(*args, **kwargs)
    #     p = user.password
    #     user.set_password(p)
    #     user.save()
    #     return user
    #
    # def update(self, *args, **kwargs):
    #     user = super().update(*args, **kwargs)
    #     p = user.password
    #     user.set_password(p)
    #     user.save()
    #     return user
    class Meta:
        model = Account
        fields = ('email', 'password',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('email', 'Student_ID', 'Student_Name', 'PrepYear')

    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')
    #
    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = Student.objects.get(email=email)
    #     except Student.DoesNotExist:
    #         # Unable to find a user, this is fine
    #         return email

    # A user was found with this as a username, raise an error.
    # raise serializers.ValidationError('This email address is already in use.')

    # def validate(self, attrs):
    #     email = attrs.get('email',)
    #     if Student.objects.filter(email):
    #         raise serializers.ValidationError({'email': 'Email is already exists'})
    #     return super().validate(email)


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prepmaterials
        fields = '__all__'


# class StudentMaterilaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student_Prepmaterials