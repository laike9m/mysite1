from django.shortcuts import render, redirect
from django.http import HttpResponse
from article.models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.core.context_processors import csrf
from django.utils import timezone

# Create your views here.
def hello(request):
    name = 'laike9m'
    html = "<html><body>Hi %s!</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "laike9m"
    return render(request, "article/hello.html", {'name': name})


def articles(request,):
    language = 'en-us'
    session_language = 'en-us'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
    
    args = {}    
    args.update(csrf(request))
    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language
    
    return render(request, 'article/articles.html', args)


def article(request, article_id=1):
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    return render(request, 'article/article.html', args)


def language(request, language):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/articles/all')
    else:
        form = ArticleForm()
    
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'article/create_article.html', args)


def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()  
    return redirect('/articles/get/%s' % article_id)


def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    
    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
            return redirect('/articles/get/%s' % article_id)
    else:
        f = CommentForm()
    
    args = {} 
    args.update(csrf(request))
    args['form'] = f
    args['article'] = a
    return render(request, 'article/add_comment.html', args)


def search_titles(request):
    if request.POST:
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    articles = Article.objects.filter(title__contains=search_text)
    
    return render(request, 'article/ajax_search.html', {'articles': articles})









