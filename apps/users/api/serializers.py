from rest_framework import serializers
from apps.users.models import User

# cuando se usa un ModelSerializer y solo se define la siguiente informacio
# Django por detras en el metodo create realiza lo siguiente 
# return self.model.objects.create(**validated_data)
# en vez de return User.objects.create(**validated_data)
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
        if value == '':
            raise serializers.ValidationError("Hay que indicar un correo")
        #if self.validate_name(self.context["name"]) in value:
            #raise serializers.ValidationError("El email no puede contener el nombre")

        return value

    def validate(self, data):
        return data       

#validated_data es la informacion valida que acaba de recibir el validador
#User.objects.create es el equivalente a un insert into en la base de datos
#User es un modelo con el cual se puede entrar a la propiedad objects el cual 
#sirve como manager y finalmente gracias a objects se accede a create
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
