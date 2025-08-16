from rest_framework import serializers 
from .models import Ticket, TicketCategory, TicketComment, TicketUpdateLog

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketCategorySerializer(serializers.ModelField):
    class Meta:
        model = TicketCategory
        fields = '__all__'

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'

class TicketUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketUpdateLog
        fields = '__all__'
        