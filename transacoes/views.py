from rest_framework import viewsets, permissions, status
from django.db.models import Sum
from rest_framework.response import Response
from .models import  Fonte, Transacao
from .serializers import FonteSerializer, TransacaoSerializer
from datetime import datetime

class FonteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fonte.objects.all()
    serializer_class = FonteSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Transacao.objects.filter(usuario=self.request.user)

        data_str = self.request.query_params.get('data')
        mes_str = self.request.query_params.get('mes')
        ano_str = self.request.query_params.get('ano')

        if data_str:
            # filtro dia exato
            try:
                data = datetime.strptime(data_str, '%Y-%m-%d').date()
                qs = qs.filter(data=data)
            except ValueError:
                pass  # ou trate o erro
        else:
            # filtrar por mes e ano
            try:
                if ano_str:
                    ano = int(ano_str)
                    qs = qs.filter(data__year=ano)
                if mes_str:
                    mes = int(mes_str)
                    qs = qs.filter(data__month=mes)
            except ValueError:
                pass  # ignore filtro inválido

        return qs

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Somar o valor das transações do queryset filtrado
        balanco = queryset.aggregate(total=Sum('valor'))['total'] or 0

        return Response({
            'balanco': balanco,
            'transacoes': serializer.data
        }, status=status.HTTP_200_OK)
