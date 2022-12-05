from django.shortcuts import redirect, render
from .models import SitterProfile
from .models import Comment
from .forms import CommentForm
from django.views.generic import ListView, DeleteView


from django.urls import reverse
from django.db.models import Q


# Create your views here.
class sitterView(ListView):
    model = SitterProfile
    template_name = 'petsitterapp/sitterprofile_list.html'


class ProfileDetailView(DeleteView):
    model = SitterProfile
    template_name = 'petsitterapp/profile_detail.html'
    form = CommentForm

    def get_success_url(self):
        return reverse('profile-detail', args=(self.kwargs['pk'],))


    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.sitterProfile = post
            form.save()

            return redirect(reverse('profile-detail', args=(self.kwargs['pk'],)))

def base(request):
    return render(request, 'petsitterapp/base.html', {})

def index(request):
    return render(request, 'petsitterapp/index.html', {})

# def sitter(request):
#     sitter_list = SitterProfile.objects.all()
#     return render(request, 'petsitterapp/SitterPage.html', {'sitter_list': sitter_list})

def about(request):
    return render(request, 'petsitterapp/about.html', {})

class SearchResultsView(ListView):
    model = SitterProfile
    template_name = "petsitterapp/search.html"

    def get_queryset(self):
        querybig = self.request.GET.getlist("bigq")
        if querybig:
            query_params = Q()
            if querybig[0] is not None and querybig[0] != "":
                query_params &= Q(zipcode__contains=querybig[0])
            if querybig[1] is not None and querybig[1] != "":
                query_params &= Q(price_number__gte=querybig[1])
            if querybig[2] is not None and querybig[2] != "":
                query_params &= Q(price_number__lte=querybig[2])
            sitter_list = SitterProfile.objects.filter(query_params)
        else:
            querymini = self.request.GET.get("q")
            sitter_list = SitterProfile.objects.filter(
            Q(zipcode__contains=querymini) | Q(name__contains=querymini) | Q(address__contains=querymini) | Q(price_number__contains=querymini)
            )
        return sitter_list