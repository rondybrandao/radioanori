from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    author = models.ForeignKey('auth.User')
    comentario = models.CharField(max_length=200, default='SOME STRING')
    
class Post(models.Model):
    
    CATEGORIA_CHOICES = (
        ('policial', 'Policial'),
        ('politica', 'Politica'),
        ('cultura', 'Cultura'),
        ('esporte', 'Esporte'),
    )
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default='SOME STRING')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    comentario = models.ManyToManyField(Comentario)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

