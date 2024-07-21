from rest_framework import serializers

def validate_int(value):
    """
    Validate that the input has integer characters.
    """
    try:
        int(value)
    except ValueError:
        raise serializers.ValidationError("Phone No. field must be a solid integer.")
    return value