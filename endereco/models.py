from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField("Logradouro", blank=True, null=True, max_length=150)
    bairro = models.CharField("Bairro", blank=True, null=True, max_length=150)
    cidade = models.CharField("Cidade", blank=True, null=True, max_length=150)
    estado = models.CharField("Estado", blank=True, null=True, max_length=150)
    numero = models.IntegerField("Número", blank=True, null=True)
    principal = models.BooleanField("Endereço principal", blank=False, null=False, default=False)
    ativo = models.BooleanField("Ativo", default=True)



    class Meta:
        verbose_name = "Endereço" 
        verbose_name_plural = "Endereços" 

    def __str__(self):
        return str(self.logradouro)

