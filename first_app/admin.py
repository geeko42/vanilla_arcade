from django.contrib import admin
from first_app.models import Contact,WebsiteLogo,Newsletter
# Register your models here.

admin.site.register(Contact)
admin.site.register(WebsiteLogo)
admin.site.register(Newsletter)
