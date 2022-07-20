from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    email = serializers.EmailField(label='Email address',
                                   max_length=254, required=True)
    first_name = serializers.CharField(label='First Name',
                                       max_length=128, required=True)
    last_name = serializers.CharField(label='Last Name',
                                      max_length=128, required=True)
    password = serializers.CharField(max_length=128,
                                     min_length=8, write_only=True,
                                     style={'input_type': 'password'})
    confirm = serializers.CharField(label='Confirm Password',
                                    max_length=128, required=True,
                                    write_only=True,
                                    style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'confirm']

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email address exist'})

        return email

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm'):
            raise serializers.ValidationError({
                'password': 'Password mismatch'
            })

        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        validated_data.pop('confirm')

        user = User.objects.create_user(email, is_active=True,
                                        **validated_data)
        # utils.send_email(user.email, 'register')
        return user
