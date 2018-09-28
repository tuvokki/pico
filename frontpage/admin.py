from django.contrib import admin


from .models import Hero
from .models import IconCard
from .models import InfoCard

admin.site.register(Hero)
admin.site.register(IconCard)
admin.site.register(InfoCard)
