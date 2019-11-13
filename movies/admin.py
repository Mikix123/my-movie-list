from django.contrib import admin

# Register your models here.
from movies.models import AgeRating, Topic, Country, Movie

admin.site.register(AgeRating)
admin.site.register(Topic)
admin.site.register(Country)
admin.site.register(Movie)