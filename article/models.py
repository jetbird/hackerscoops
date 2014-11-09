from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import markdown


# Create your models here.

def markdown_to_html(markdownText):
    html = markdown.markdown(markdownText)

    return html

class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name


class ImageThumbnail(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='thumbnails/%Y/%m/%d',blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d',blank=True)

    def create_thumbnail(self):
        if not self.image:
            return

        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        # Thumbnail size in a tuple
        THUMBNAIL_SIZE = (200,200)

        # Open the original photo from which we will create the thumbnail
        image = Image.open(StringIO(self.image.read()))
        image_type = image.format.lower()
        image.thumbnail(THUMBNAIL_SIZE,Image.ANTIALIAS)



        #Save the thumbnail
        temporary_handle = StringIO()
        image.save(temporary_handle,image_type)
        temporary_handle.seek(0)

        # Save image to a simpleuploadedfile
        simpleuploadedfile = SimpleUploadedFile(
           self.name,temporary_handle.read(),content_type=image_type)
        # Save simpleuploadedfile into ImageField
        self.thumbnail.save(self.name,simpleuploadedfile,save=False)

    def save(self):
        self.create_thumbnail()
        super(ImageThumbnail,self).save()


class Photo(models.Model):
    imagename = models.TextField()
    articleimage = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)

    def __unicode__(self):
        return "%s is %s" %(self.imagename, self.articleimage)


class Article(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=130)
    title = models.TextField()
    photo = models.ManyToManyField(
            Photo, related_name='photos',blank=True)
    author = models.ForeignKey(User)
    body = models.TextField()
    categories = models.ManyToManyField(
        Category, related_name='articles', null=True)
    articlethumbnail = models.OneToOneField(
        ImageThumbnail,related_name='articlethumbnail',blank=True, null=True)

    def __unicode__(self):
        return '%s by %s' %(self.title, self.author)

    def body_html(self):
        return markdown_to_html(self.body)


class Comment(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)
    article = models.ManyToManyField(Article, related_name='comments')
    content = models.TextField()

    def __unicode__(self):
        return self.content
