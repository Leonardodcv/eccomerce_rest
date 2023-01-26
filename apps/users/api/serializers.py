from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):
        #custom validation
        if "Leonardus" in value:
            raise serializers.ValidationError("Error, no puede existir un usuario con ese nombre")

        return value

    def validate_email(self, value):
        if value == "":
            raise serializers.ValidationError("Hay que indicar un valor")
        return value

    def validate(self, value):
        print("validacion general")
        return value                