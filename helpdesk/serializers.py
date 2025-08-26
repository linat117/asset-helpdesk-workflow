from rest_framework import serializers 
from .models import Ticket, TicketCategory, TicketComment, TicketUpdateLog

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','title','description','category','status','priority','reported_by','assigned_to','linked_asset','created_at','updated_at']

class TicketCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketCategory
        fields = ['id','name','description']

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = ['id','ticket','comment_by','comment_text','comment_time']

class TicketUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketUpdateLog
        fields = ['id','ticket','updated_by','update_note','update_time']
        