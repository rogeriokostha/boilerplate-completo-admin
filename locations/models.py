from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="states"
    )

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.uf})"


class City(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.state.uf}"


class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20, blank=True, null=True)
    complement = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="addresses")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ["city", "street"]

    def __str__(self):
        return f"{self.street}, {self.number or 'S/N'} - {self.city.name}/{self.city.state.uf}"
