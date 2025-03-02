from django.contrib import admin

from snippets.models import Snippet


# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'linenos', 'language', 'style')
    list_filter = ('linenos', 'language', 'style')
    search_fields = ('title', 'code')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'code')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('linenos', 'language', 'style')
        }),
    )
