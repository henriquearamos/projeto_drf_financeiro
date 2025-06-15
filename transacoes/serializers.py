from rest_framework import serializers
from .models import Fonte, Transacao

class FonteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fonte
        fields = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    #fonte = FonteSerializer(read_only=True)
    fonte = serializers.SerializerMethodField()
    fonte_id = serializers.PrimaryKeyRelatedField(
        queryset=Fonte.objects.all(), write_only=True, source='fonte'
    )
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transacao
        fields = '__all__'

    def validate_valor(self, valor):
        if valor < 0:
            raise serializers.ValidationError("Não é permitido informar valores negativos.")
        return valor

    def validate(self, data):
        # Para tipo 'desconto', transformar em negativo
        if data.get('tipo_entrada').upper() == 'DESCONTO':
            data['valor'] = -abs(data['valor'])  # garante valor negativo
        return data

    def get_fonte(self, obj):
        return obj.fonte.nome_fonte  # ou o nome que for do seu campo
