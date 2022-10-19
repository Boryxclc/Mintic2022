from rest_framework import serializers
from gestionPaquetes.models.user import User
from gestionPaquetes.models.account import Account
from gestionPaquetes.serializers.accountSerializer import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class meta:
        model= User
        fields = ['id','username','password', 'name','email','account']

        def create(self, validated_data):
            accountdata=validated_data.pop('account')
            userInstance= User.create(**validated_data)
            Account.objects.create(user=userInstance,**accountdata)
            return userInstance

        def to_representation(self, obj):
            user= User.objects.get(id=obj.id)
            account= Account.objects.get(user=obj.id)
            return{
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'acount':{
                    'id': account.id,
                    'balance': account.balance,
                    'lastChangeDate': account.lastChangeDate,
                    'isActive':account.isActive,
                }
            }