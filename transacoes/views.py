from rest_framework import viewsets, permissions
from .models import  Fonte, Transacao
from .serializers import FonteSerializer, TransacaoSerializer

class FonteViewSet(viewsets.ModelViewSet):
    queryset = Fonte.objects.all()
    serializer_class = FonteSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transacao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
