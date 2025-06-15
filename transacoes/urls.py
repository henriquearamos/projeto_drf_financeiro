from rest_framework.routers import SimpleRouter
from .views import TransacaoViewSet, FonteViewSet

router = SimpleRouter()
router.register('transacoes', TransacaoViewSet)
router.register('fontes', FonteViewSet)