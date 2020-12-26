from django.contrib import admin
from .models import *

admin.site.site_header = 'Book Management System'
admin.site.site_title = 'Online Books'
admin.site.index_title = 'Admin'

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)