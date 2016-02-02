<span class="s1">(Los objetos de la base de datos se llaman modelo y se
crean en python, así como las relaciones.</span>

<span class="s1">)</span>

<span class="s1">**Create a Django Project**</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Start & Configuration**</span>

<span class="s1"></span>

<span class="s1">**Create Project**</span>

<span class="s1"></span>

<span class="s1">*\$ django-admin startproject* ***mySite*** *.*</span>

<span class="s1"></span>

<span class="s1">**Changing settings**</span>

<span class="s1"></span>

<span class="s1">In mysite/settings.py:</span>

<span class="s1"></span>

<span class="s1">*TIME\_ZONE = ‘Europe/Berlin'*</span>

<span class="s1">*STATIC\_ROOT = os.path.join(BASE\_DIR,
‘static’)*</span>

<span class="s1"></span>

<span class="s1">**Setup a database**</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py migrate*</span>

<span class="s1"></span>

<span class="s1">**Run Server**</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py runserver*</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Django Models**</span>

<span class="s1"></span>

<span class="s1">**Creating an application**</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py startapp* ***blog***</span>

<span class="s1"></span>

<span class="s1">Now we add our new app to the list of installed apps in
*mysite/settings.py:*</span>

<span class="s1">*INSTALLED\_APPS = (*</span>

<span class="s1"></span>   
</span>………*</span>

<span class="s1"></span>   
</span>………*</span>

<span class="s1"></span>   
</span>'****blog****',*</span>

<span class="s1">*)*</span>

<span class="s1"></span>

<span class="s1">**Creating a blog post model**</span>

<span class="s1">In *blog/models.py* create a class containing our
desired model:</span>

<span class="s1"></span>

<span class="s1">*from django.db import models*</span>

<span class="s1">*from django.utils import timezone*</span>

<span class="s1"></span>

<span class="s1">*class* ***Post****(models.Model):*</span>

<span class="s1"></span>author
= models.ForeignKey('auth.User')*</span>

<span class="s1"></span>title =
models.CharField(max\_length=200)*</span>

<span class="s1"></span>#For
long text without a limit TextField*</span>

<span class="s1"></span>text =
models.TextField()*</span>

<span class="s1"></span>   
</span>created\_date = models.DateTimeField(*</span>

<span class="s1"></span>           
</span>default=timezone.now)*</span>

<span class="s1"></span>   
</span>published\_date = models.DateTimeField(*</span>

<span class="s1"></span>           
</span>blank=True, null=True)*</span>

<span class="s1"></span>

<span class="s1"></span>def
publish(self):*</span>

<span class="s1"></span>       
</span>self.published\_date = timezone.now()*</span>

<span class="s1"></span>       
</span>self.save()*</span>

<span class="s1"></span>

<span class="s1"></span>def
\_\_str\_\_(self):*</span>

<span class="s1"></span>       
</span>return self.title*</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Create tables for models in your database**</span>

<span class="s1">The last step here is to add our new model to our
database. First we have to make Django know that we have some changes in
our model.</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py makemigrations blog*</span>

<span class="s1"></span>

<span class="s1">Django prepared for us a migration file that we have to
apply now to our database.</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py migrate blog*</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Django admin**</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">To add, edit and delete posts we've just modeled, we
will use Django admin.</span>

<span class="s1"></span>

<span class="s1">Let's open the *blog/admin.py* file and replace its
content with this:</span>

<span class="s1"></span>

<span class="s1">*from django.contrib import admin*</span>

<span class="s1">*from .models import Post*</span>

<span class="s1"></span>

<span class="s1">*admin.site.register(Post)*</span>

<span class="s1"></span>

<span class="s1">As you can see, we import the Post model defined in the
previous chapter. To make our model visible on the admin page, we need
to register the model with admin.site.register(Post).</span>

<span class="s1"></span>

<span class="s1">*python manage.py runserver*</span>

<span class="s1"></span>

<span class="s1">OK, time to look at our Post model. Remember to
run<span class="Apple-converted-space"> </span></span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py runserver*</span>

<span class="s1"></span>

<span class="s1">in the console to run the web server. Go to the browser
and type the address</span>

<span class="s1"></span>

<span
class="s2">[*http://127.0.0.1:8000/admin/*](http://127.0.0.1:8000/admin/)</span>

<span class="s1"></span>

<span class="s1">You will see the login page.</span>

<span class="s1">To log in, you need to create a superuser. In the
command-line type:</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py createsuperuser*</span>

<span class="s1"></span>

<span class="s1">When prompted, type your username, email address, and
password.</span>

<span class="s1">Now you can log in with the superuser's credentials you
chose.</span>

<span class="s1"></span>

<span class="s1">Go to Posts and experiment a little bit with it. You
can now add blog posts.</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Django urls**</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">We want *http://127.0.0.1:8000/*<span
class="Apple-converted-space">  </span>to be a homepage of our blog and
display a list of posts.</span>

<span class="s1">We will import urls from our blog application to the
main *mysite/urls.py* file.</span>

<span class="s1"></span>

<span class="s1">Append to *urlpatterns* in *mysite/urls.py*:</span>

<span class="s1"></span>

<span class="s1">*url(r'', include(‘blog.urls')),*</span>

<span class="s1"></span>

<span class="s1">**blog.urls**</span>

<span class="s1">Create a new *blog/urls.py* empty file. All right! Add
these two first lines:</span>

<span class="s1"></span>

<span class="s1">*from django.conf.urls import url*</span>

<span class="s1">*from . import views*</span>

<span class="s1"></span>

<span class="s1">*urlpatterns = \[*</span>

<span class="s1"></span>   
</span>url(r'\^\$', views.post\_list, name='post\_list'),*</span>

<span class="s1">*\]*</span>

<span class="s1">(There’s something weird here, in mysite/urls instead
of a list the url function is inside a patterns() function )</span>

<span class="s1"></span>

<span class="s1">Now we have to create a view so that we can see
something in the browser.</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Django views**</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">A view is a place where we put the "logic" of our
application. It will request information from the model you created
before and pass it to a template. We'll create a template in the next
chapter.</span>

<span class="s1"></span>

<span class="s1">Views are placed in the *views.py* file. We will add
our views to the *blog/views.py* file.</span>

<span class="s1"></span>

<span class="s1">**blog/views.py**</span>

<span class="s1">The simplest view can look like this:</span>

<span class="s1"></span>

<span class="s1">*def post\_list(request):*</span>

<span class="s1"></span>return
render(request, 'blog/post\_list.html', {})*</span>

<span class="s1"></span>

<span class="s1">As you can see, we created a function that takes a
request and returns a function </span><span
class="s3">*render*</span><span class="s1"> that will render our
template *blog/post\_list.html*.</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Introduction to HTML**</span>

<span class="s1"></span>

<span class="s1">**Templates**</span>

<span class="s1">Creating a template means creating a template
file.</span>

<span class="s1">Templates are saved in *blog/templates/blog* directory.
So first create a directory called templates inside your blog directory.
Then create another directory called blog inside your templates
directory.</span>

<span class="s1">(You might wonder why we need two directories both
called blog - as you will discover later, this is simply a useful naming
convention that makes life easier when things start to get more
complicated.)</span>

<span class="s1">And now create a *post\_list.html* file inside the
*blog/templates/blog* directory.</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Django ORM and QuerySets**</span>

<span class="s1"></span>

<span class="s1">**What is a QuerySet?**</span>

<span class="s1">A QuerySet is, in essence, a list of objects of a given
Model. QuerySet allows you to read the data from the database, filter it
and order it.</span>

<span class="s1"></span>

<span class="s1">**Django shell**</span>

<span class="s1">To enter Django’s shell type:</span>

<span class="s1"></span>

<span class="s1">*\$ python manage.py shell*</span>

<span class="s1"></span>

<span class="s1">You're now in Django's interactive console. It's just
like Python prompt but with some additional Django magic :). You can use
all the Python commands here too, of course.</span>

<span class="s1"></span>

<span class="s1">**All objects**</span>

<span class="s1">Let's try to display all of our posts first. You can do
that with the following command:</span>

<span class="s1"></span>

<span class="s1">*from blog.models import Post*</span>

<span class="s1">*Post.objects.all()*</span>

<span class="s1"></span>

<span class="s1">It's a list of the posts we created earlier! We created
these posts using the Django admin interface. But, now we want to create
new posts using Python, so how do we do that?</span>

<span class="s1"></span>

<span class="s1">**Create object in the CLI**</span>

<span class="s1">Let's import User model first:</span>

<span class="s1"></span>

<span class="s1">*from django.contrib.auth.models import User*</span>

<span class="s1"></span>

<span class="s1">Lets see what users we have in our database and then
get an instance of the user:</span>

<span class="s1"></span>

<span class="s1">*User.objects.all()*</span>

<span class="s1">*me = User.objects.get(username='ola')*</span>

<span class="s1"></span>

<span class="s1">Now you can create a new Post object in the
database:</span>

<span class="s1"></span>

<span class="s1">*Post.objects.create(author=me, title='Sample title',
text='Test')*</span>

<span class="s1"></span>

<span class="s1">Hurray! Wanna check if it worked?</span>

<span class="s1"></span>

<span class="s1">*Post.objects.all()*</span>

<span class="s1"></span>

<span class="s1">**Filter objects**</span>

<span class="s1">A big part of QuerySets is an ability to filter them.
Let's say, we want to find all posts User ola authored. We will use
*filter* instead of *all* in *Post.objects.all()*. In parentheses we
will state what condition(s) a blog post needs to meet to end up in our
queryset. In our situation it is author that is equal to *me*. The way
to write it in Django is: *author=me*. Now our piece of code looks like
this:</span>

<span class="s1"></span>

<span class="s1">*Post.objects.filter(author=me)*</span>

<span class="s1"></span>

<span class="s1">Or maybe we want to see all the posts that contain a
word 'title' in the title field?</span>

<span class="s1"></span>

<span class="s1">*Post.objects.filter(title\_\_contains='title')*</span>

<span class="s1"></span>

<span class="s1"></span>There
are two underscore characters (\_) between title and contains. Django's
ORM uses this rule to separate field names ("title") and operations or
filters ("contains"). If you only use one underscore, you'll get an
error like "FieldError: Cannot resolve keyword title\_contains".*</span>

<span class="s1"></span>

<span class="s1">You can also get a list of all published posts. We do
it by filtering all the posts that have *published\_date* set in the
past:</span>

<span class="s1"></span>

<span class="s1">*from django.utils import timezone*</span>

<span
class="s1">*Post.objects.filter(published\_date\_\_let=timezone.now())*</span>

<span class="s1"></span>

<span class="s1">Unfortunately, the post we added from the Python
console is not published yet. We can change that! First get an instance
of a post we want to publish:</span>

<span class="s1"></span>

<span class="s1">*post = Post.objects.get(title="Sample title")*</span>

<span class="s1"></span>

<span class="s1">And then publish it with our publish method!</span>

<span class="s1"></span>

<span class="s1">*post.publish()*</span>

<span class="s1"></span>

<span class="s1">Now try to get list of published posts again:</span>

<span class="s1"></span>

<span
class="s1">*Post.objects.filter(published\_date\_\_lte=timezone.now())*</span>

<span class="s1"></span>

<span class="s1">**Ordering objects**</span>

<span class="s1">QuerySets also allow you to order the list of objects.
Let's try to order them by *created\_date* field:</span>

<span class="s1"></span>

<span class="s1">*Post.objects.order\_by('created\_date')*</span>

<span class="s1"></span>

<span class="s1">We can also reverse the ordering by adding - at the
beginning:</span>

<span class="s1"></span>

<span class="s1">*Post.objects.order\_by(‘-created\_date')*</span>

<span class="s1"></span>

<span class="s1">Or we can reverse using python’s functions for
lists:</span>

<span
class="s1">*Post.objects.order\_by(‘created\_date’).reverse()*</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Chaining QuerySets**</span>

<span class="s1">You can also combine QuerySets by chaining them
together:</span>

<span class="s1"></span>

<span
class="s1">*Post.objects.filter(published\_date\_\_lte=timezone.now()).order\_by('published\_date')*</span>

<span class="s1"></span>

<span class="s1">This is really powerful and lets you write quite
complex queries.</span>

<span class="s1"></span>

<span class="s1">Cool! You're now ready for the next part! To close the
shell, type this:</span>

<span class="s1"></span>

<span class="s1">*exit()*</span>

<span class="s1">*\$*</span>

<span class="s1"></span>

<span class="s1">**Dynamic data in templates**</span>

<span class="s1"></span>

<span class="s1">Despite having its own nomenclature, such as naming the
callable objects generating the HTTP responses "views", the core Django
framework can be seen as MVC. It consists of an object-relational mapper
(ORM) which mediates between data models (defined as Python classes) and
a relational database ("Model"); a system for processing HTTP requests
with a web templating system ("View") and a regular-expression-based URL
dispatcher ("Controller").</span>

<span class="s1"></span>

<span class="s1"><span class="Apple-converted-space"> </span>We have
different pieces in place: the Post model is defined in *models.py*, we
have *post\_list* in *views.py* and the template added. But how will we
actually make our posts appear in our HTML template? (What we want to do
is take some content (models saved in the database) and display it
nicely in our template).</span>

<span class="s1"></span>

<span class="s1">This is exactly what views are supposed to do: connect
models and templates. In our *post\_list* view we will need to take
models we want to display and pass them to the template. In a view we
decide what (model) will be displayed in a template.</span>

<span class="s1"></span>

<span class="s1">Now we have to include in *views.py* the model we wrote
in *models.py*.</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**QuerySet**</span>

<span class="s1">You should already be familiar with how QuerySets work.
We talked about it in Django ORM (QuerySets) chapter.</span>

<span class="s1"></span>

<span class="s1">So now we want published blog posts sorted by
*published\_date*, right? We already did that in QuerySets
chapter!</span>

<span class="s1"></span>

<span
class="s1">*Post.objects.filter(published\_date\_\_lte=timezone.now()).order\_by('published\_date')*</span>

<span class="s1"></span>

<span class="s1">Now we put this piece of code inside the
*blog/views.py* file by adding it to the function *def
post\_list(request).*</span>

<span class="s1"></span>

<span class="s1">The last missing part is passing the *posts* QuerySet
to the template. Don't worry we will cover how to display it in a next
chapter.</span>

<span class="s1"></span>

<span class="s1">In the *render* function we already have parameter with
*request* (a request from the Internet) and a template file
'*blog/post\_list.html*'. In last parameter, a dictionary, we can add
things for the template to use.</span>

<span class="s1"></span>

<span class="s1">**Django templates**</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">Time to display some data! Django gives us some helpful
built-in template tags for that.</span>

<span class="s1"></span>

<span class="s1">**What are template tags?**</span>

<span class="s1">You see, in HTML, you can't really write Python code,
because browsers don't understand it. They only know HTML. We know that
HTML is rather static, while Python is much more dynamic.</span>

<span class="s1"></span>

<span class="s1">Django template tags allow us to transfer Python-like
things into HTML, so you can build dynamic websites faster and easier.
Yikes!</span>

<span class="s1"></span>

<span class="s1">**Display post list template**</span>

<span class="s1">In the previous chapter we gave our template a list of
*posts* in the posts variable. Now we will display it in HTML.</span>

<span class="s1"></span>

<span class="s1">To print a variable in Django templates, we use double
curly brackets with the variable's name inside, like this:</span>

<span class="s1"></span>

<span class="s1">*{{ posts }}*</span>

<span class="s1"></span>

<span class="s1">It works! But we want them to be displayed like the
static posts we created earlier in the Introduction to HTML chapter. You
can mix HTML and template tags. Our *body* will look like this:</span>

<span class="s1"></span>

<span class="s1">*&lt;div&gt;*</span>

<span class="s1"></span>   
</span>&lt;h1&gt;&lt;a href="/"&gt;Django Girls
Blog&lt;/a&gt;&lt;/h1&gt;*</span>

<span class="s1">*&lt;/div&gt;*</span>

<span class="s1"></span>

<span class="s1">*{% for post in posts %}*</span>

<span class="s1"></span>   
</span>&lt;div&gt;*</span>

<span class="s1"></span>       
</span>&lt;p&gt;published: {{ post.published\_date }}&lt;/p&gt;*</span>

<span class="s1"></span>       
</span>&lt;h1&gt;&lt;a href=""&gt;{{ post.title
}}&lt;/a&gt;&lt;/h1&gt;*</span>

<span class="s1"></span>       
</span>&lt;p&gt;{{ post.text|linebreaks }}&lt;/p&gt;*</span>

<span class="s1"></span>   
</span>&lt;/div&gt;*</span>

<span class="s1">*{% endfor %}*</span>

<span class="s1"></span>

<span class="s1">Have you noticed that we used a slightly different
notation this time *{{ post.title }}* or *{{ post.text }}*? We are
accessing data in each of the fields defined in our *Post* model. Also
the </span><span class="s4">*|linebreaks*</span><span class="s1"> is
piping the posts' text through a filter to convert line-breaks into
paragraphs.</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**CSS - make it pretty!**</span>

<span class="s1"></span>

<span class="s1">Our blog still looks pretty ugly, right? Time to make
it nice! We will use CSS for that.</span>

<span class="s1"></span>

<span class="s1">**Install Bootstrap**</span>

<span class="s1">To install Bootstrap, you need to add this to your
*&lt;head&gt;* in your *.html* file
(*blog/templates/blog/post\_list.html*):</span>

<span class="s1"></span>

<span class="s1">*&lt;link rel="stylesheet"
href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"&gt;*</span>

<span class="s1">*&lt;link rel="stylesheet"
href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"&gt;*</span>

<span class="s1"></span>

<span class="s1">This doesn't add any files to your project. It just
points to files that exist on the internet. Just go ahead, open your
website and refresh the page.</span>

<span class="s1"></span>

<span class="s1">**Your first CSS file!**</span>

<span class="s1">Let's create a CSS file now, to add your own style to
your web-page. Create a new directory called *css* inside your *static*
directory. Then create a new file called *blog.css* inside
*blog/static/css* directory.</span>

<span class="s1"></span>

<span class="s1">In your *blog/static/css/blog.css* file you should add
the following code:</span>

<span class="s1"></span>

<span class="s1">*h1 a {*</span>

<span class="s1"></span>color:
\#FCA205;*</span>

<span class="s1">*}*</span>

<span class="s1"></span>

<span class="s1">…..</span>

<span class="s1"></span>

<span class="s1">Then, we need to also tell our HTML template that we
added some CSS. Open the *blog/templates/blog/post\_list.html* file and
add this line at the very beginning of it:</span>

<span class="s1"></span>

<span class="s1">*{% load staticfiles %}*</span>

<span class="s1"></span>

<span class="s1">We're just loading static files here :). Between the
*&lt;head&gt;* and *&lt;/head&gt;*, after the links to the Bootstrap CSS
files add this line:</span>

<span class="s1"></span>

<span class="s1">*&lt;link rel="stylesheet" href="{% static
'css/blog.css' %}"&gt;*</span>

<span class="s1"></span>

<span class="s1">Nice work! Maybe we would also like to give our website
a little air and increase the margin on the left side? Let's try
this!</span>

<span class="s1"></span>

<span class="s1">*body {*</span>

<span class="s1"></span>   
</span>padding-left: 15px;*</span>

<span class="s1">*}*</span>

<span class="s1"></span>

<span class="s1">Maybe we can customize the font in our header? Paste
this into your *&lt;head&gt;* in *blog/templates/blog/post\_list.html*
file:</span>

<span class="s1"></span>

<span class="s1">*&lt;link
href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext"
rel="stylesheet" type="text/css"&gt;*</span>

<span class="s1"></span>

<span class="s1">This line will import a font called Lobster from Google
Fonts.</span>

<span class="s1"></span>

<span class="s1">Find the h1 a declaration block (the code between
braces { and }) in the CSS file \`blog/static/css/blog.css. Now add the
line font-family: 'Lobster'; between the braces, and refresh the
page:</span>

<span class="s1"></span>

<span class="s1">*h1 a {*</span>

<span class="s1"></span>color:
\#FCA205;*</span>

<span class="s1"></span>   
</span>font-family: 'Lobster';*</span>

<span class="s1">*}*</span>

<span class="s1"></span>

<span class="s1">(Muchas cosas de css en poco tiempo, no se ni como
resumir)</span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1"></span>

<span class="s1">**Template extending**</span>

<span class="s1">**Create base template**</span>

<span class="s1"></span>

<span class="s1">A base template is the most basic template that you
extend on every page of your website.</span>

<span class="s1"></span>

<span class="s1">Let's create a base.html file in
blog/templates/blog/.</span>
