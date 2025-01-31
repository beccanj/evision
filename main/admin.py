from django.contrib import admin

from main.models import EVStation, BlogPost, Category, Tag, Comment, ContactForm, FeaturedForm

# Register your models here.

admin.site.site_header = 'EVision'
admin.site.site_title = 'Manage your EV Stations'

class EVStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'availability', 'created_at', 'updated_at')  # Columns to display in the list view
    search_fields = ('name', 'address', 'charging_types')  # Fields to enable search functionality in the admin interface
    list_filter = ('availability',)  # Filter options (you can add more filters based on your needs)
    ordering = ('-created_at',)  # Default ordering of stations by created date, most recent first

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

class FeaturedFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sname', 'slocation', 'created_at')
    search_fields = ('name','email','sname')
    list_filter = ('created_at',)
















admin.site.register(EVStation, EVStationAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(FeaturedForm, FeaturedFormAdmin)