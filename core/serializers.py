from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from core.models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
