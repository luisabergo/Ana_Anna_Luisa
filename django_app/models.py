from django.db import models
from django.db.models import permalink

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True)
    corpo = models.TextField()
    data = models.DateField(db_index=True, auto_now_add=True)
    categoria = models.ForeignKey('django_app.Categoria')

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_url_absoluta(self):
        return ('ver_post_blog', None, { 'slug': self.url })
        
class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    url = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_url_absoluta(self):
        return ('ver_categoria_blog', None, { 'slug': self.url })

class Disciplina(models.Model):
    nome_disc = models.CharField(max_length=100, db_index=True)
    url = models.SlugField(max_length=100, db_index=True)
    descricao = models.CharField(max_length=100, db_index=True)
    horario = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.nome_disc

    @permalink
    def get_url_absoluta(self):
        return ('ver_disciplina_blog', None, { 'slug': self.url })

class Usuario(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    def __unicode__(self):
        return '%s' % self.nome
    @permalink
    def get_url_absoluta(self):
        return ('ver_usuario_blog', None, { })

class Professor(models.Model):
    phone = models.CharField(max_length=15)
    siape = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.siape
    @permalink
    def get_url_absoluta(self):
        return ('ver_professor_blog', None, { })

class Aluno(models.Model):
    pontuacao = models.FloatField()
    matricula = models.CharField(max_length=100, db_index=True)
    def __unicode__(self):
        return '%s' % self.matricula
    @permalink
    def get_url_absoluta(self):
        return ('ver_aluno_blog', None, { })
    
