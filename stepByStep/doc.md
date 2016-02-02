#Create a Django Project


##Start & Configuration

###Create Project

```
$ django-admin startproject mySite .
```
###Changing settings

In mysite/settings.py:
```
TIME_ZONE = ‘Europe/Berlin'
STATIC_ROOT = os.path.join(BASE_DIR, ‘static’)
```
###Setup a database

```
$ python manage.py migrate
```

###Run Server

```
$ python manage.py runserver
```


##Django Models

###Creating an application

```
$ python manage.py startapp blog
```

Now we add our new app to the list of installed apps in mysite/settings.py:
```python
INSTALLED_APPS = (
    ………
    ………
    'blog',
)
```
###Creating a blog post model
In blog/models.py create a class containing our desired model:

```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    #For long text without a limit TextField
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

###Create tables for models in your database
The last step here is to add our new model to our database. First we have to make Django know that we have some changes in our model.

```
$ python manage.py makemigrations blog
```

Django prepared for us a migration file that we have to apply now to our database.

```
$ python manage.py migrate blog
```


##Django admin


To add, edit and delete posts we've just modeled, we will use Django admin.

Let's open the blog/admin.py file and replace its content with this:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

As you can see, we import the Post model defined in the previous chapter. To make our model visible on the admin page, we need to register the model with admin.site.register(Post).

```
python manage.py runserver
```

OK, time to look at our Post model. Remember to run 

```
$ python manage.py runserver
```

in the console to run the web server. Go to the browser and type the address

```
http://127.0.0.1:8000/admin/
```

You will see the login page.
To log in, you need to create a superuser. In the command-line type:

```
$ python manage.py createsuperuser
```

When prompted, type your username, email address, and password.
Now you can log in with the superuser's credentials you chose.

Go to Posts and experiment a little bit with it. You can now add blog posts.


##Django urls


We want http://127.0.0.1:8000/  to be a homepage of our blog and display a list of posts.
We will import urls from our blog application to the main mysite/urls.py file.

Append to urlpatterns in mysite/urls.py:

```python
url(r'', include(‘blog.urls')),
``
###blog.urls
Create a new blog/urls.py empty file. All right! Add these two first lines:
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
```
(There’s something weird here, in mysite/urls instead of a list the url function is inside a patterns() function )

Now we have to create a view so that we can see something in the browser.


##Django views


A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template. We'll create a template in the next chapter.

Views are placed in the views.py file. We will add our views to the blog/views.py file.

###blog/views.py
The simplest view can look like this:

```python
def post_list(request):
    return render(request, 'blog/post_list.html', {})
```

As you can see, we created a function that takes a request and returns a function render that will render our template blog/post_list.html.







##Introduction to HTML

###Templates
Creating a template means creating a template file.
Templates are saved in blog/templates/blog directory. So first create a directory called templates inside your blog directory. Then create another directory called blog inside your templates directory.
(You might wonder why we need two directories both called blog - as you will discover later, this is simply a useful naming convention that makes life easier when things start to get more complicated.)
And now create a post_list.html file inside the blog/templates/blog directory.


##Django ORM and QuerySets

###What is a QuerySet?
A QuerySet is, in essence, a list of objects of a given Model. QuerySet allows you to read the data from the database, filter it and order it.

###Django shell
To enter Django’s shell type:

```
$ python manage.py shell
```

You're now in Django's interactive console. It's just like Python prompt but with some additional Django magic :). You can use all the Python commands here too, of course.

###All objects
Let's try to display all of our posts first. You can do that with the following command:
```python
from blog.models import Post
Post.objects.all()
```
It's a list of the posts we created earlier! We created these posts using the Django admin interface. But, now we want to create new posts using Python, so how do we do that?

###Create object in the CLI
Let's import User model first:
```python
from django.contrib.auth.models import User
```
Lets see what users we have in our database and then get an instance of the user:
```python
User.objects.all()
me = User.objects.get(username='ola')
```
Now you can create a new Post object in the database:
```python
Post.objects.create(author=me, title='Sample title', text='Test')
```
Hurray! Wanna check if it worked?
```python
Post.objects.all()
```
###Filter objects
A big part of QuerySets is an ability to filter them. Let's say, we want to find all posts User ola authored. We will use filter instead of all in Post.objects.all(). In parentheses we will state what condition(s) a blog post needs to meet to end up in our queryset. In our situation it is author that is equal to me. The way to write it in Django is: author=me. Now our piece of code looks like this:
```python
Post.objects.filter(author=me)
```
Or maybe we want to see all the posts that contain a word 'title' in the title field?
```python
Post.objects.filter(title__contains='title')
```
*There are two underscore characters (_) between title and contains. Django's ORM uses this rule to separate field names ("title") and operations or filters ("contains"). If you only use one underscore, you'll get an error like "FieldError: Cannot resolve keyword title_contains".*

You can also get a list of all published posts. We do it by filtering all the posts that have published_date set in the past:
```python
from django.utils import timezone
Post.objects.filter(published_date__let=timezone.now())
```
Unfortunately, the post we added from the Python console is not published yet. We can change that! First get an instance of a post we want to publish:
```python
post = Post.objects.get(title="Sample title")
```
And then publish it with our publish method!
```python
post.publish()
```
Now try to get list of published posts again:
```python
Post.objects.filter(published_date__lte=timezone.now())
```
###Ordering objects
QuerySets also allow you to order the list of objects. Let's try to order them by created_date field:
```python
Post.objects.order_by('created_date')
```
We can also reverse the ordering by adding - at the beginning:

```python
Post.objects.order_by(‘-created_date')
```
Or we can reverse using python’s functions for lists:
```python
Post.objects.order_by(‘created_date’).reverse()
```

###Chaining QuerySets
You can also combine QuerySets by chaining them together:
```python
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
```
This is really powerful and lets you write quite complex queries.

Cool! You're now ready for the next part! To close the shell, type this:
```python
exit()
```

##Dynamic data in templates

*Despite having its own nomenclature, such as naming the callable objects generating the HTTP responses "views", the core Django framework can be seen as MVC. It consists of an object-relational mapper (ORM) which mediates between data models (defined as Python classes) and a relational database ("Model"); a system for processing HTTP requests with a web templating system ("View") and a regular-expression-based URL dispatcher ("Controller").*

 We have different pieces in place: the Post model is defined in models.py, we have post_list in views.py and the template added. But how will we actually make our posts appear in our HTML template? (What we want to do is take some content (models saved in the database) and display it nicely in our template).

This is exactly what views are supposed to do: connect models and templates. In our post_list view we will need to take models we want to display and pass them to the template. In a view we decide what (model) will be displayed in a template.

Now we have to include in views.py the model we wrote in models.py.


###QuerySet
You should already be familiar with how QuerySets work. We talked about it in Django ORM (QuerySets) chapter.

So now we want published blog posts sorted by published_date, right? We already did that in QuerySets chapter!
```python
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
```
Now we put this piece of code inside the blog/views.py file by adding it to the function def post_list(request).

The last missing part is passing the posts QuerySet to the template. Don't worry we will cover how to display it in a next chapter.

In the render function we already have parameter with request (a request from the Internet) and a template file 'blog/post_list.html'. In last parameter, a dictionary, we can add things for the template to use.

##Django templates


Time to display some data! Django gives us some helpful built-in template tags for that.

###What are template tags?
You see, in HTML, you can't really write Python code, because browsers don't understand it. They only know HTML. We know that HTML is rather static, while Python is much more dynamic.

Django template tags allow us to transfer Python-like things into HTML, so you can build dynamic websites faster and easier. Yikes!

###Display post list template
In the previous chapter we gave our template a list of posts in the posts variable. Now we will display it in HTML.

To print a variable in Django templates, we use double curly brackets with the variable's name inside, like this:
```python
{{ posts }}
```
It works! But we want them to be displayed like the static posts we created earlier in the Introduction to HTML chapter. You can mix HTML and template tags. Our body will look like this:
```html
<div>
    <h1><a href="/">Django Girls Blog</a></h1>
</div>

{% for post in posts %}
    <div>
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
{% endfor %}
```
Have you noticed that we used a slightly different notation this time {{ post.title }} or {{ post.text }}? We are accessing data in each of the fields defined in our Post model. Also the |linebreaks is piping the posts' text through a filter to convert line-breaks into paragraphs.


##CSS - make it pretty!

Our blog still looks pretty ugly, right? Time to make it nice! We will use CSS for that.

###Install Bootstrap
To install Bootstrap, you need to add this to your <head> in your .html file (blog/templates/blog/post_list.html):
```html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
```
This doesn't add any files to your project. It just points to files that exist on the internet. Just go ahead, open your website and refresh the page.

###Your first CSS file!
Let's create a CSS file now, to add your own style to your web-page. Create a new directory called css inside your static directory. Then create a new file called blog.css inside blog/static/css directory.

In your blog/static/css/blog.css file you should add the following code:
```css
h1 a {
    color: #FCA205;
}
```
…..

Then, we need to also tell our HTML template that we added some CSS. Open the blog/templates/blog/post_list.html file and add this line at the very beginning of it:
```python
{% load staticfiles %}
```
We're just loading static files here :). Between the <head> and </head>, after the links to the Bootstrap CSS files add this line:
```html
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```
Nice work! Maybe we would also like to give our website a little air and increase the margin on the left side? Let's try this!
```css
body {
    padding-left: 15px;
}
```
Maybe we can customize the font in our header? Paste this into your <head> in blog/templates/blog/post_list.html file:
```html
<link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
```
This line will import a font called Lobster from Google Fonts.

Find the h1 a declaration block (the code between braces { and }) in the CSS file `blog/static/css/blog.css. Now add the line font-family: 'Lobster'; between the braces, and refresh the page:
```css
h1 a {
    color: #FCA205;
    font-family: 'Lobster';
}
```
(Muchas cosas de css en poco tiempo, no se ni como resumir)




##Template extending
###Create base template

A base template is the most basic template that you extend on every page of your website.

[django template lang documentation](https://docs.djangoproject.com/en/1.7/topics/templates/)

##Extend your application

We've already completed all the different steps necessary for the creation of our website: we know how to write a model, url, view and template. We also know how to make our website pretty.


The first thing we need in our blog is, obviously, a page to display one post, right?
We already have a Post model, so we don't need to add anything to models.py.
[django-girls tutorial](http://tutorial.djangogirls.org/en/extend_your_application/index.html)

##Django Forms
The final thing we want to do on our website is create a way to add and edit blog posts. With forms we will have absolute power over our interface - we can do almost anything we can imagine!

The nice thing about Django forms is that we can either define one from scratch or create a ModelForm which will save the result of the form to the model.
This is exactly what we want to do: we will create a form for our Post model.
Like every important part of Django, forms have their own file: forms.py.
We need to create a file with this name in the blog directory.

Ok, let's open it and type the following code:
```python
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
```
We need to tell Django, that this form is a ModelForm (so Django will do some magic for us) - forms.ModelForm is responsible for that.

Next, we have class Meta, where we tell Django which model should be used to create this form (model = Post). Finally, we can say which field(s) should end up in our form. In this scenario we want only title and text to be exposed - author should be the person who is currently logged in (you!) and created_date should be automatically set when we create a post (i.e in the code), right?

And that's it! All we need to do now is use the form in a view and display it in a template.
So once again we will create: a link to the page, a URL, a view and a template.

###Link to a page with the form

It's time to open blog/templates/blog/base.html. We will add a link in div named page-header:
```html
<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
```
Note that we want to call our new view post_new. The class "glyphicon glyphicon-plus" is provided by the bootstrap theme we are using, and will display a plus sign for us.

After adding the line, your html file should now look like this:
```html
{% load staticfiles %}
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                    {% block content %}
                    {% endblock %}
                </div>
            </div>
        </div>
    </body>
</html>
```
After saving and refreshing the page http://127.0.0.1:8000 you will obviously see a familiar NoReverseMatch error, right?

###URL
We open blog/urls.py and add a line:
```python
url(r'^post/new/$', views.post_new, name='post_new'),
```
After refreshing the site, we see an AttributeError, since we don't have post_new view implemented. Let's add it right now.

###post_new view
Time to open the blog/views.py file and add the following lines with the rest of the from rows:
```python
from .forms import PostForm
```
and our view:
```python
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```
To create a new Post form, we need to call PostForm() and pass it to the template. We will go back to this view, but for now, let's create quickly a template for the form.

###Template

We need to create a file post_edit.html in the blog/templates/blog directory. To make a form work we need several things:

* we have to display the form. We can do that for example with a simple {{ form.as_p }}.
* the line above needs to be wrapped with an HTML form tag: <form method="POST">...</form>
* we need a Save button. We do that with an HTML button: <button type="submit">Save</button>
* and finally just after the opening <form ...> tag we need to add {% csrf_token %}. This is very important, since it makes your forms secure! Django will complain if you forget about this bit if you try to save the form:

(Gives an error)

Ok, so let's see how the HTML in post_edit.html should look:

```html
{% extends 'blog/base.html' %}

{% block content %}
    <h1>New post</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}
```

###Saving the form
When we submit the form, we are brought back to the same view, but this time we have some more data in request, more specifically in request.POST (the naming has nothing to do with a blog "post", it's to do with the fact that we're "posting" data). Remember that in the HTML file our <form> definition had the variable method="POST"? All the fields from the form are now in request.POST. You should not rename POST to anything else (the only other valid value for method is GET, but we have no time to explain what the difference is).

So in our view we have two separate situations to handle. First: when we access the page for the first time and we want a blank form. Second: when we go back to the view with all form's data we just typed. So we need to add a condition (we will use if for that).
```python
if request.method == "POST":
    [...]
else:
    form = PostForm()
```
It's time to fill in the dots [...]. If method is POST then we want to construct the PostForm with data from the form, right? We will do that with:
```python
form = PostForm(request.POST)
```
Easy! Next thing is to check if the form is correct (all required fields are set and no incorrect values will be saved). We do that with form.is_valid().

We check if the form is valid and if so, we can save it!
```python
if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    post.published_date = timezone.now()
    post.save()
``
Basically, we have two things here: we save the form with form.save and we add an author (since there was no author field in the PostForm and this field is required!). commit=False means that we don't want to save Post model yet - we want to add author first. Most of the time you will use form.save(), without commit=False, but in this case, we need to do that. post.save() will preserve changes (adding author) and a new blog post is created!

Finally, it would be awesome if we can immediately go to post_detail page for newly created blog post, right? To do that we need one more import:
```python
from django.shortcuts import redirect
```
Add it at the very beginning of your file. And now we can say: go to post_detail page for a newly created post.
```python
return redirect('post_detail', pk=post.pk)
```
post_detail is the name of the view we want to go to. Remember that this view requires a pk variable? To pass it to the views we use pk=post.pk, where post is the newly created blog post!

Ok, we talked a lot, but we probably want to see what the whole view looks like now, right?
```python
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```
Let's see if it works. Go to the page http://127.0.0.1:8000/post/new/, add a title and text, save it... and voilà! The new blog post is added and we are redirected to post_detail page!

###Form validation
Now, we will show you how cool Django forms are. A blog post needs to have title and text fields. In our Post model we did not say (as opposed to published_date) that these fields are not required, so Django, by default, expects them to be set.

Try to save the form without title and text. Guess, what will happen! Django is taking care of validating that all the fields in our form are correct. Isn't it awesome?

###Edit form

Now we know how to add a new form. But what if we want to edit an existing one? It is very similar to what we just did. Let's create some important things quickly (if you don't understand something, you should ask your coach or look at the previous chapters, since we covered all these steps already).

Open blog/templates/blog/post_detail.html and add this line:
```html
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
```
so that the template will look like:
```html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
        <h1>{{ post.title }}</h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
{% endblock %}
```
In blog/urls.py we add this line:
```python
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
```
We will reuse the template blog/templates/blog/post_edit.html, so the last missing thing is a view.

Let's open a blog/views.py and add at the very end of the file:
```python
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
```
This looks almost exactly the same as our post_new view, right? But not entirely. First thing: we pass an extra pk parameter from urls. Next: we get the Post model we want to edit with get_object_or_404(Post, pk=pk) and then, when we create a form we pass this post as an instance both when we save the form:
```python
form = PostForm(request.POST, instance=post)
```
and when we just opened a form with this post to edit:
```
form = PostForm(instance=post)
```
Ok, let's test if it works! Let's go to post_detail page. There should be an edit button in the top-right corner:
When you click it you will see the form with our blog post.
Feel free to change the title or the text and save changes!

###Security
Being able to create new posts just by clicking a link is awesome! But, right now, anyone that visits your site will be able to post a new blog post and that's probably not something you want. Let's make it so the button shows up for you but not for anyone else.

In blog/templates/blog/base.html, find our page-header div and the anchor tag you put in there earlier. It should look like this:
```html
<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
```
We're going to add another {% if %} tag to this which will make the link only show up for users that are logged into the admin. Right now, that's just you! Change the <a> tag to look like this:
```html
{% if user.is_authenticated %}
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
{% endif %}
```
This {% if %} will cause the link to only be sent to the browser if the user requesting the page is logged in. This doesn't protect the creation of new posts completely, but it's a good first step. We'll cover more security in the extension lessons.

Remember the edit icon we just added to our detail page? We also want to add the same change there, so other people won't be able to edit existing posts.

Open blog/templates/blog/post_detail.html and find:
```html
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
```
Change it to:
```html
{% if user.is_authenticated %}
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
{% endif %}
```
Since you're likely logged in, if you refresh the page, you won't see anything different. Load the page in a new browser or an incognito window, though, and you'll see that the link doesn't show up, and the icon doesn't display either!