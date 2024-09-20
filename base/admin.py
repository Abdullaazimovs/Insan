from django.contrib import admin

from .models import Category, Portfolio, Block


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Category, CategoryAdmin)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_direction', 'client', 'country', 'year', 'is_public', 'post_date')
    search_fields = ('title', 'client', 'country')


admin.site.register(Block)
