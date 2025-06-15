from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    criacao = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Fonte(Base):
    nome_fonte = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Fonte'
        verbose_name_plural = 'Fontes'
        ordering = ['id']

    def __str__(self):
        return self.nome_fonte

class Transacao(Base):
    TIPO_ENTRADA_CHOICES = [
        ('desconto', 'Desconto'),
        ('credito', 'Crédito'),
    ]

    data = models.DateField()
    tipo_entrada = models.CharField(max_length=10, choices=TIPO_ENTRADA_CHOICES)
    fonte = models.ForeignKey(Fonte, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entradas')

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
        ordering = ['id']

    def save(self, *args, **kwargs):
        if self.tipo_entrada == 'desconto':
            self.valor = -abs(self.valor)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.data} - {self.tipo_entrada} - R${self.valor}"
