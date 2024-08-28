import logging
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from blog.forms import BlogForm, BlogModeratorForm
from blog.models import Blog
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

logger = logging.getLogger(__name__)


class BlogCreateView(PermissionRequiredMixin, CreateView, LoginRequiredMixin):
    model = Blog
    fields = ('title', 'content', 'preview',)
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        logger.info(f"Incrementing views_counter for post {self.object.pk}")
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Blog
    permission_required = 'blog.change_blog'
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return BlogForm
        if user.has_perm("blog.change_blog") and user.has_perm("blog.add_blog"):
            return BlogModeratorForm
        raise PermissionDenied


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
    permission_required = 'blog.delete_blog'