from django.contrib import admin
from apps.base.models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = ("id", "name_ru")
    list_display = ("id", "name_ru", "is_publish",)


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    search_fields = ("id", "name_ru")
    list_display = ("id", "name_ru",)
