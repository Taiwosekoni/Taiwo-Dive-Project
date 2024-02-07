from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='object was created')
    # new class PostModelTest and add a method setUp to create a 
    # new database that has just one entry: a post with a text field 
    # containing the string 'object was created'
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'expected object was post.text')
        # Here we run our firt test called "test_text_content" to check that the
        # database field actually contains a "test". We created a variable called
        # "post" that respresents the first id on our Post Model. If we created
        # another entry for our test Django will automatically give an id = 2
        # f strings let us put variables directly in our strings with the {} brackets.
        # Here we are setting expected_object_name to be the string of 
        # the value in post.text (which is "object was created").
