from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article, ArticlesBlock, Views, Like
from .forms import CreateArticleForm, CreateBlocksForm
from django.http import HttpResponseRedirect
from django.urls import reverse
#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
def home(request):
    user_filter_state = request.session.get('user_filter_state','up')
    data = Article.objects.filter(published=True).all().order_by('date_published')
    if request.GET.get('sort_by')=='up':
        request.session[user_filter_state] = 'up'
        user_filter_state = request.session[user_filter_state]
        data=Article.objects.filter(published=True).all().order_by('date_published')
    elif request.GET.get('sort_by')=='down':
        request.session[user_filter_state] = 'down'
        user_filter_state = request.session[user_filter_state]
        data = Article.objects.filter(published=True).all().order_by('-date_published')
    return render(request,'articleapp/home.html',{'articles':data, 'user_filter_state':user_filter_state})


def view_art(request,art_id):
    if request.user.has_perm('articleapp.can_read_article'):
        data = get_object_or_404(Article, pk=art_id, published=True)
        blocks = ArticlesBlock.objects.filter(article=art_id)
        viewscount = Views.objects.filter(article=art_id).count()
        likes_count = Like.objects.filter(article=art_id).count()
        user_liked = Like.objects.filter(user=request.user, article=art_id).exists()
        try:
            v = Views.objects.create(user=request.user, article=data)
        except:
            pass
        return render(request, 'articleapp/view_art.html', {
            'article': data, 'blocks': blocks,
            'viewscount': viewscount, 'likes_count': likes_count,
            'user_liked': user_liked
        })
    else:
        return (HttpResponse('<h2>Access denied </h2>'))


@login_required
def create_article(request):
    if request.method == 'GET':
        return render(request, 'articleapp/create_article.html', {'form': CreateArticleForm()})
    else:
        try:
            form = CreateArticleForm(request.POST, request.FILES)
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articleapp:view_art', article.id)
        except ValueError:
            return render(request, 'articleapp/create_article.html', {'form': CreateArticleForm(), 'error': 'неккоректные значения'})

@login_required
def change_article(request,art_id):
    article=get_object_or_404(Article,pk=art_id,author=request.user)
    if request.method=='GET':
          return render(request,'articleapp/change_article.html',{'article':article})
    else:
        try:
            form=CreateArticleForm(request.POST,request.FILES,instance=article)
            form.save()
            return redirect('articleapp:home')
        except ValueError:
            return render(request,'articleapp/change_article.html',{'error':'неккоректные значения','article':article})


@login_required
def view_article(request,art_id): # переименовать view_art
    article_=get_object_or_404(Article,pk=art_id,author=request.user)
    articleblocks=ArticlesBlock.objects.filter(article=art_id)
    return render(request,'articleapp/view_article.html',{'article':article_,'articleblocks':articleblocks})

@login_required
def delete_article(request,art_id):
    article=get_object_or_404(Article,pk=art_id,author=request.user)
    if request.method=='POST':
        article.published=False
        article.save()
        return redirect('articleapp:home')


@login_required
def create_block(request, art_id):
    article = get_object_or_404(Article, pk=art_id, author=request.user)

    if request.method == 'GET':
        return render(request, 'articleapp/create_block.html', {'form': CreateBlocksForm()})
    else:
        try:
            form = CreateBlocksForm(request.POST, request.FILES)
            newblock = form.save(commit=False)
            newblock.article = article
            newblock.save()
            return redirect('articleapp:view_art', art_id)
        except ValueError:
            return render(request, 'articleapp/create_block.html', {'form': CreateBlocksForm(), 'error': 'неккоректные значения'})




@login_required
def change_block(request, block_id):
    block = get_object_or_404(ArticlesBlock, id=block_id)

    if request.method == 'POST':
        form = ChangeBlockForm(request.POST, instance=block)
        if form.is_valid():
            form.save()
            return redirect('articleapp:view_art', art_id=block.article.id)
    else:
        form = ChangeBlockForm(instance=block)


@login_required
def delete_block(request, block_id):
    block = get_object_or_404(ArticlesBlock, id=block_id)
    article_id = block.article.id
    block.delete()
    return redirect('articleapp:view_art', art_id=article_id)


def like(request, art_id):
    data = get_object_or_404(Article, pk=art_id)
    Like.objects.get_or_create(user=request.user, article=data)

    return HttpResponseRedirect(reverse('articleapp:view_art', args=[art_id]))

def unlike(request, art_id):
    data = get_object_or_404(Article, pk=art_id)
    try:
        like = Like.objects.get(user=request.user, article=data)
        like.delete()
    except Like.DoesNotExist:
        pass

    return HttpResponseRedirect(reverse('articleapp:view_art', args=[art_id]))
