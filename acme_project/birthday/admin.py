from django.contrib import admin
from .models import Birthday, Tag, Congratulation

# Регистрация модели Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)  # Поля для отображения в списке
    search_fields = ('tag',)  # Поиск по полю

# Если Birthday ещё не зарегистрирована
@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'author')
    list_filter = ('birthday', 'author')
    search_fields = ('first_name', 'last_name')

# Если Congratulation ещё не зарегистрирована
@admin.register(Congratulation)
class CongratulationAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'birthday', 'created_at')
    list_filter = ('created_at',)
