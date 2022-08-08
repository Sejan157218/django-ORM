
from django.db import models


# Abstract model

class BaseItem(models.Model):
    title=models.CharField(max_length=220)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    class Meta:
        abstract=True
        ordering=['title']



class ItemA(BaseItem):
    content=models.TextField()
    class Meta(BaseItem.Meta):
        ordering=['-created']



class ItemB(BaseItem):
    file=models.FileField(upload_to='files')



class ItemC(BaseItem):
    file=models.FileField(upload_to='images')



class ItemD(BaseItem):
    slug=models.SlugField(max_length=222,unique=True)



# Multi-Table

class Books(models.Model):
    title=models.CharField(max_length=220)
    created=models.DateField(auto_now_add=True)


class ISBN(Books):
    ISBN=models.TextField()



# Proxy Model

class BookContent(models.Model):
    title=models.CharField(max_length=220)
    created=models.DateField(auto_now_add=True)


class BookOrder(BookContent):
    class Meta:
        proxy=True;
        ordering=['-created']
