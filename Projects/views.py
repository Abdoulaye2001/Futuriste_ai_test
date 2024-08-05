from django.shortcuts import get_object_or_404, render
from .models import Portfolio, Categories_portfolio
from Blog.models import Posts
from Services.models import Services

# Create your views here.

def Projects(request):
        projects = Portfolio.objects.all()
        categories = Categories_portfolio.objects.all()
        services = Services.objects.all()
        articles_recents = Posts.objects.all().order_by('-post_day')[:2]
        context = "Futuriste-Ai -- Portfolio"
        return render(request, '../Templates/portfolio-masonty.html', {'context' : context, 'projects' : projects, 'categories' : categories, 'articles_recents': articles_recents, 'services' : services})

def Projects_detail(request, slug):
        projects = get_object_or_404(Portfolio, slug=slug)
        projects = Portfolio.objects.get(slug=slug)
        services = Services.objects.all()
        project = Portfolio.objects.order_by('portfolio_date')
        current_index = list(project).index(projects)
        prev_index = current_index - 1
        next_index = current_index +1
        if prev_index >= 0:
                previous_project = project[prev_index]
        else:
                previous_project = None

        if next_index < len(project):
                next_project = project[next_index]
        else:
                next_project = None
        const = {
                'previous_project' : previous_project,
                'next_project' : next_project
        }
        context = "Futuriste-Ai -- Portfolio Détails"
        return render(request, '../Templates/portfolio-details.html', {'context' : context, 'projects' : projects, 'const' : const, 'services' : services})