from django.db import models


class Purpose(models.Model):
    name = models.CharField('Name', max_length=80)

    class Meta:
        verbose_name = 'Purpose'
        verbose_name_plural = 'Purposes'
        ordering = ['name']

    def __str__(self):
        return self.name


class Origin(models.Model):
    name = models.CharField('Name', max_length=80)

    class Meta:
        verbose_name = 'Origin'
        verbose_name_plural = 'Origins'
        ordering = ['name']

    def __str__(self):
        return self.name


class Aircraft(models.Model):
    name = models.CharField('Name', max_length=80)
    rank = models.PositiveIntegerField('Rank')
    year = models.PositiveIntegerField('Year')
    origin = models.ForeignKey(
        Origin,
        models.CASCADE,
        verbose_name='Origin',
        related_name='aircrafts'
    )
    purposes = models.ManyToManyField(
        Purpose,
        verbose_name='Purpose',
        related_name='aircrafts'
    )

    class Meta:
        verbose_name = 'Aircraft'
        verbose_name_plural = 'Aircrafts'
        ordering = ['name']

    def __str__(self):
        return self.name
