from django.db import models
from django.utils.safestring import mark_safe
from endereco.models import Endereco

class Cliente(models.Model):
    foto = models.ImageField("Foto", upload_to="img", blank=True, null=True)
    nome = models.CharField("Nome", max_length=150, blank=True, null=True)
    sobrenome = models.CharField("Sobrenome", max_length=150, blank=True, null=True)
    cpf = models.CharField("CPF", max_length=11, blank=True, null=True)
    rg = models.CharField("RG", max_length=15, blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    endereco = models.ManyToManyField(Endereco)
    ativo = models.BooleanField("Ativo", default=True)

    def foto_tag(self):
        if self.foto:
            return mark_safe(u'<img src="%s" width="100px" height=80px/>' % self.foto.url)
        else:
            return None

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome