from django.db import models

class Post(models.Model):
    text = models.TextField() 

def __str__(self):
        return self.text[:50]
    # this will display 50 character of the text field in the Admin UI, you can store more characters in the database but in the Admin UI only the first 50 will show up.
