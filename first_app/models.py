from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    message = models.TextField(null=True, blank=True, unique=True)

    def __unicode__(self):
        return self.content

    def save(self, **kwargs):                       # Saving custom text fields
        super(Contact, self).save(**kwargs)

class WebsiteLogo(models.Model):
    img = models.ImageField(upload_to='uploads',null=True,blank=True)

class Newsletter(models.Model):
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __unicode__(self):
        return self.content

    def save(self, **kwargs):                       # Saving custom text fields
        super(Newsletter, self).save(**kwargs)

    # def __unicode__(self):
    #     return self.content
    #
    # def save(self, **kwargs):                       # Saving custom text fields
    #     super(Newsletter, self).save(**kwargs)
