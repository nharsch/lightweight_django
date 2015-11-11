from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Sprint, Task

User = get_user_model()

class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPrint
        fields = ('id', 'name', 'descriptions', 'end',)

class TaskSerializer(serializers.ModelSerializer):
    
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False)
    status_dispaly = serializers.SerializerMethodField('get_status_display')

    class Meta:
        model = Task
        fields = ('id', 'name', 'description',
                  'sprint', 'status', 'status_display', 'order',
                  'assigned', 'started', 'due',
                  'completed',)

    def get_status_display(self, obj):
        return obj.get_status_display()


