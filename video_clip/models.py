from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name='nested_category')
    nesting_level = models.IntegerField()
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60)

    def __str__(self):
        return "%s %s %s" % (self.name, self.nesting_level, self.slug)

class Clip(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=300)
    memo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # on_delete는 category가 삭제되었을 때 하위 post들을 어떻게 할 지에 대한 내용인듯..?
    category = models.ForeignKey(Category, on_delete = models.CASCADE)



