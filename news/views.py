from django.shortcuts import render, redirect
from .models import NewsModel, CommentsModle
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CreateDataForm
from django.views.generic import DetailView

def get_models_list_news_fucntion(request):
    news_list = NewsModel.objects.all()
    context = {'news_list': news_list}
    return render(request, 'news_list.html', context)
   
   
class Products_view_function(DetailView):
    model = NewsModel
    template_name = 'prodtuc_view.html'
    context_object_name = 'news_view'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_str = request.POST.get('comment')
        if comment_str:
            CommentsModle.objects.create(comment=comment_str, user=request.user, news=self.object)
            return redirect('news_details', pk=self.object.pk)
        return render(request, self.template_name, {'news_view': self.object})
    

    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akkount {username} yaratildi!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news:list_news')
            else:
                messages.error(request, 'Xato foydalanuvchi nomi yoki parol!')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('news:login')




def search_data(request):
    query = request.GET.get('q', '')
    if query:
        results = NewsModel.objects.filter(title__icontains=query)
    else:
        results = NewsModel.objects.none()
    return render(request, 'search_results.html', {'results': results})




def create_data_function(request):
    if request.method == 'POST':
        form = CreateDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:list_news')  
        else:
            print(form.errors)
    else:
        form = CreateDataForm()
    return render(request, 'create_news.html', {'form': form})