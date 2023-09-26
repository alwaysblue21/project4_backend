from .models import Reserv
from rest_framework import serializers

## Class ReservSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class ReservSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the ReservSerializer class.
    class Meta:
        # model to serialize
        model = Reserv
        # fields to show in json
        fields = ('id', 'date', 'name', 'time', 'phone_number', 'number_of_customers')