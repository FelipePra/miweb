from rest_framework import serializers
from apiApp.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    def validar_matricula(self,value):
        existe = Alumno.objects.filter(matricula=value).exists()
        if existe:
            raise serializers.ValidationError('La matricula ya esta registrada')
    class Meta():
        model = Alumno
        fields = '__all__'