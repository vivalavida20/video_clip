from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    # nesting_level = models.IntegerField()

    class Meta:
        unique_together = ('slug', 'parent',)

        # verbose_name_plural 이란? - 장고 모델에서 복수일때 노출 시킬 이름 옵션 이거 설정 안하면 장고에선 자동으로 categorys로 설정할 것. 
        # 그럼 이상하잖아. 그렇기때문에 설정하는 건데 장고에서 기본으로 이렇게 노출하는게 어드민 말고 다른데가 또 있나?
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Clip(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=300)
    memo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # on_delete는 category가 삭제되었을 때 하위 post들을 어떻게 할 지에 대한 내용인듯..?
    category = models.ForeignKey(Category, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]




















