# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    sobrenome = models.CharField(max_length=255, null=True, blank=True)
    nome_preferido = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Loja(models.Model):

    #__Loja_FIELDS__
    cnpj = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=255, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__Loja_FIELDS__END

    class Meta:
        verbose_name        = _("Loja")
        verbose_name_plural = _("Loja")


class Produto(models.Model):

    #__Produto_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    codigo_sistema = models.IntegerField(null=True, blank=True)
    codigo_interno = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

    #__Produto_FIELDS__END

    class Meta:
        verbose_name        = _("Produto")
        verbose_name_plural = _("Produto")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Pedido(models.Model):

    #__Pedido_FIELDS__
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    numero_pedido = models.IntegerField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #__Pedido_FIELDS__END

    class Meta:
        verbose_name        = _("Pedido")
        verbose_name_plural = _("Pedido")



#__MODELS__END
