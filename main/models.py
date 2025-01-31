from django.db import models

# Create your models here.
from django.db import models

class EVStation(models.Model):
    name = models.CharField(max_length=255)  # Name of the charging station
    description = models.TextField(blank=True, null=True)  # Optional description of the station
    latitude = models.FloatField()  # Latitude coordinate
    longitude = models.FloatField()  # Longitude coordinate
    address = models.CharField(max_length=500, blank=True, null=True)  # Physical address
    charging_types = models.CharField(max_length=255, blank=True, null=True)  # Example: 'Fast Charging, Level 2'
    availability = models.BooleanField(default=True)  # Whether the station is operational
    created_at = models.DateTimeField(auto_now_add=True)  # When the station was added
    updated_at = models.DateTimeField(auto_now=True)  # When the station details were last updated

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "EV Charging Station"
        verbose_name_plural = "EV Charging Stations"

    @property
    def location(self):
        return (self.latitude, self.longitude)

from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    slug = models.SlugField(unique=True, max_length=200)  # URL-friendly identifier
    author = models.CharField(max_length=100)  # Author of the post
    content = models.TextField()  # Main content of the post
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional image
    excerpt = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates
    categories = models.ManyToManyField('Category', related_name='posts')  # Many-to-Many relationship with categories
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')  # Optional tags
    is_published = models.BooleanField(default=False)  # Whether the post is published or not

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Newest posts appear first


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the category
    slug = models.SlugField(unique=True, max_length=100)  # URL-friendly identifier

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Name of the tag
    slug = models.SlugField(unique=True, max_length=50)  # URL-friendly identifier

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')  # Blog post the comment belongs to
    name = models.CharField(max_length=100)  # Name of the commenter
    email = models.EmailField()  # Email of the commenter
    body = models.TextField()  # The comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the comment was made
    approved = models.BooleanField(default=False)  # Admin approval for visibility

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

class ContactForm(models.Model):
    name = models.CharField(max_length=255)  # Name of the sender
    email = models.EmailField()  # Email address of the sender
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()  # Message content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message was sent

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact Form Messages"



class FeaturedForm(models.Model):
    name = models.CharField(max_length=255)  # Name of the sender
    email = models.EmailField()  # Email address of the sender
    sname = models.CharField(max_length=255)  # Subject of the message
    slocation = models.CharField(max_length=255)  # Subject of the message
    sdesc = models.TextField()  # Message content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message was sent

    def __str__(self):
        return f"{self.name} - {self.sname}"

    class Meta:
        verbose_name = "Feature Form Message"
        verbose_name_plural = "Feature Form Messages"