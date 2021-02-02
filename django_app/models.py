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
        return '%s' % self.titulo

    @permalink
    def get_url_absoluta(self):
        return ('ver_disciplina_blog', None, { 'slug': self.url })
        
        
class Usuario(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=20)
	address=models.TextField(max_length=20)
	password = models.CharField(max_length=20)

	class Meta:
        	abstract=True

class Professor(Usuario):
	phone=models.IntegerField(max_length=15)
	siape = models.CharField(max_length=100, db_index=True)
	
class Aluno(Usuario):
    	pontuacao = models.IntegerField()
    	matricula = models.CharField(max_length=100, db_index=True)
