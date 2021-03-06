from django.contrib import admin
from django_app.models import Blog, Categoria, Aluno, Professor, Disciplina

class BlogAdmin(admin.ModelAdmin):
    exclude = ['data']
    prepopulated_fields = {'slug': ('titulo',)}

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Blog)
admin.site.register(Categoria)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
