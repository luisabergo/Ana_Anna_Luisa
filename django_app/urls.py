from django.conf.urls import patterns, url
from django_app import views
urlpatterns = patterns('',
	url(r'^', views.index, name='index'))

urlpatterns = patterns('',
	url(r'^', views.CadastroProfessor, name='CadastroProfessor'))


urlpatterns = patterns('',
	url(r'^', views.CadastroAluno, name='CadastroAluno'))

urlpatterns = patterns('',
	url(r'^', views.CadastroDisciplina, name='CadastroDisciplina'))
