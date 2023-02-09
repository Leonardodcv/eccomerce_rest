from rest_framework import serializers
from apps.users.models import User

# cuando se usa un ModelSerializer y solo se define la siguiente informacio
# Django por detras en el metodo create realiza lo siguiente 
# return self.model.objects.create(**validated_data)
# en vez de return User.objects.create(**validated_data)

# cuando se crea o se actualiza usando un serializador
# toma lo que se encuentra en el campo fields y cuando se 
# llame al metodo usara la funcion de representacion
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
        #valor predeterminado del metodo create
        #return super().create(validated_data)   

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data["password"])
        updated_user.save()
        return updated_user
        #valor predeterminado del metodo update
        #return super().update(instance, validated_data)      
     
        # Este serisalizador es usado para listar, crear y actuaslizar
        # se pueden crear serializadores para cada parte del crud porque 
        # cada uno responde a procesos, logicas o requerimietos diferentes
        #fields = ("id","username","email","password")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    def to_representation(self, instance):
        #de esta forma es este metodo de forma predeterminada 
        #en el cual se llama al constructor y luego a este metodo
        #return super().to_representation(instance)
        return {
            #se usa de esta forma y no instance.id porque en realidad instance 
            # es un diccionario
            "id" : instance["id"],
            "username" : instance["username"],
            "email" : instance["email"],
            # se puede cambiar los nombres de esta forma para que sean 
            # representados de otra forma al mostrarlos pero al no tomar de la 
            # base de datos todos los valores agilisara la consulta
            "password" : instance["password"],
            #"password" : instance
        }


"""
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


#sobreescribir el metodo save generalmente es utilizado para hacer validaciones
#sin hacer registros en la BdD
    def save():
        pass
"""