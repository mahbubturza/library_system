from django.db import models
from django.contrib.auth.models import User
from account.models import UserAccount

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title= models.CharField(max_length=200)
    description= models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    genre = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    availability_status = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/', blank = True, null = True)

    def __str__(self):
        return self.title


class Borrower(models.Model):
    name= models.ForeignKey(User,on_delete= models.CASCADE)
    book= models.ForeignKey(Book,on_delete= models.CASCADE)
    borrowDate = models.DateTimeField(auto_now_add=True)
    def create(cls, name , book):
        object = cls(name=name,book=book)
        return object
    def __str__(self):
        return f'{self.name}:{self.book}'
    
    
class Wishlist(models.Model):
    name= models.ForeignKey(User,on_delete= models.CASCADE)
    book= models.ForeignKey(Book,on_delete= models.CASCADE)
    wishlistDate = models.DateTimeField(auto_now_add=True)

    def create(cls, name , book):
        object = cls(name=name,book=book)
        return object
    
    def __str__(self):
        return f'{self.name}:{self.book}'