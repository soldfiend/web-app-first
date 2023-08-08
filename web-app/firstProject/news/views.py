from django.shortcuts import render, redirect
from .models import Artickle
from .forms import ArtickleForm
from django.views.generic import DetailView, UpdateView,DeleteView


# Create your views here.
def news_home(request):
    news = Artickle.objects.order_by('title')
    return render(request, 'news/news_home.html', {'news': news})


class NewDetailView(DetailView):
    model = Artickle
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Artickle
    template_name = 'news/create.html'
    form_class = ArtickleForm
class NewsDeleteView(DeleteView):
    model = Artickle
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtickleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Form is error'
    form = ArtickleForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
