from rest_framework import serializers
from .models import Person, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()

    class Meta:
        model = Person
        #exclude = ['name', 'age']
        #fields = ['name', 'age', 'emp_id']

        fields = '__all__'
        #depth = 1

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('Age Should Be Greater Than 18')
        return data