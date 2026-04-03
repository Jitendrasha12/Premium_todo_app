from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    """
    Serializer for Task objects that doesn't use ModelSerializer (Avoiding ORM ties).
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    due_date = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        # This isn't strictly needed for our raw SQL view, 
        # but satisfies the Serializer interface if used.
        pass

    def update(self, instance, validated_data):
        pass
