from django.contrib import admin
from .models import Game, Move
# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    #learn more what else can be customized in admin interface
    list_display = ('id', 'first_player', 'second_player','status')
    list_editable = ('status', )#'first_player','second_player',)


#admin.site.register(Game)
admin.site.register(Move)


