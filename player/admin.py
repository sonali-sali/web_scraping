from django.contrib import admin
from .models import Team, State,City,Country,Offer,Class,HighSchool,Interest,Player,Position, Twitter

# Register your models here.
admin.site.register(Team)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Offer)
admin.site.register(State)
admin.site.register(Class)
admin.site.register(Position)
admin.site.register(HighSchool)
admin.site.register(Interest)
admin.site.register(Player)
admin.site.register(Twitter)
