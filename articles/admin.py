from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, TagsArticles, Tag


class TagsArticlesInlineFormset(BaseInlineFormSet):
    def clean(self):
        tags_priority_list = []
        for form in self.forms:
            if form.cleaned_data != {}:
                tags_priority_list.append(form.cleaned_data['priority'])
        if True not in tags_priority_list:
            raise ValidationError('Укажите основной раздел')
        priority_count = 0
        for i in tags_priority_list:
            if i == True:
                priority_count += 1
        if priority_count >= 2:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class TagsArticlesInline(admin.TabularInline):
    model = TagsArticles
    formset = TagsArticlesInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsArticlesInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
