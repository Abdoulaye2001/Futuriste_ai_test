from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.urls import reverse
from Blog.models import Posts, Categories, Comment
from Services.models import Services
# Create your views here.

def Blog(request):
        article = Posts.objects.all()
        categorie = Categories.objects.all()
        services = Services.objects.all()
        context = "Futuriste Ai -- Blog"
        return render(request, '../Templates/blog-listing.html',{'article': article, 'context': context, 'categorie': categorie, 'services': services})
def Blog_detail(request, slug):
        article = get_object_or_404(Posts, slug=slug)
        article = Posts.objects.get(slug=slug)
        articles_recents = Posts.objects.all().order_by('-post_day')[:3]
        aticles_populaires = Posts.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')
        services = Services.objects.all()
        comment_count = article.comments.all().count()
        categorie = Categories.objects.all().count()
        categorie_articles = Categories.objects.annotate(num_articles=Count('categorie'))
        articles = Posts.objects.order_by('post_day')
        current_index = list(articles).index(article)
        prev_index = current_index - 1
        next_index = current_index + 1
        if prev_index >= 0:
                previous_posts = articles[prev_index]
        else:
                previous_posts  = None

        if next_index < len(articles):
                next_posts  = articles[next_index]
        else:
                next_posts  = None
        const = {
                'previous_posts' : previous_posts,
                'next_posts' : next_posts
        }
        if request.method == 'POST':
                comment_content = request.POST['content']
                comment_author = request.POST['author']
                comment_email = request.POST['email']
                parent_id = request.POST.get('parent_id')
                parent_comment_name = request.POST.get('parent_comment_name')
                if parent_id:
                        parent_comment = Comment.objects.get(id=parent_comment_name)
                        new_comment = Comment(
                            article = article,
                            content = comment_content,
                            author = comment_author,
                            email = comment_email,
                            parent = parent_comment
                        )
                        new_comment.save()
                        return redirect('blog_detail', slug=slug, parent_id=parent_id)
                else:
                        new_comment = Comment(
                            article = article,
                            content = comment_content,
                            author = comment_author,
                            email = comment_email, 
                        )
                        new_comment.save()
                        return redirect('blog_detail', slug=slug)
        query = request.GET.get('query')
        if query:
            try:
                article = Posts.objects.get(post_title__icontains=query)
                url = reverse('blog_detail', kwargs={'slug': article.slug})
                return redirect(f'{url}?q={query}')
            except Posts.DoesNotExist:
                return redirect('blog')
        context = "Futuriste Ai -- Blog Detail"
        return render(request, '../Templates/blog-detail.html', {'article': article, 'context': context, 'categorie': categorie, 'comment_count': comment_count, 'services': services, 'articles_recents' : articles_recents, 'const' : const, 'aticles_populaires' : aticles_populaires, 'categorie_articles' : categorie_articles})


def Not_found(request, exception):
        return render(request, '../Templates/404.html', status=404)