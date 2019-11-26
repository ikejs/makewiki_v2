from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from wiki.models import Page
from wiki.forms import PageForm

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class NewPage(CreateView):
    def get(self, request):
        return render(request, 'new-page.html')

    def post(self, request):
      form = PageForm(request.POST)
      if form.is_valid():
          page = form.save()
          return HttpResponseRedirect(reverse_lazy('page:slug'))
      return render(request, 'new-page', {'form': form})
