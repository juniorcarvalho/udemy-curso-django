from django.db import models


# custonManager
class CourseManager(models.Manager):

    def search(self, query):
        # filtro .OR. ( nome ou descricao contem 'query' )
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', blank=True, null=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager() # objects passa ser objects + CourseManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'details', (), {'slug': self.slug}

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['name']
