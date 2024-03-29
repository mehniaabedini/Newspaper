from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new
from .models import Article
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView  # new
)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):  # new
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.outher == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.outher == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):  # new
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)

    def form_valid(self, form):
        form.instance.author = self.request.user
