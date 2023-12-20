from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Tree
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {
        'birds': birds
    })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    id_list = bird.trees.all().values_list('id')
    available_trees = Tree.objects.exclude(id__in=id_list)
    # Instantiate the FeedingForm to be rendered in detail.html:
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
        'bird': bird,
        'feeding_form': feeding_form,
        'trees': available_trees
    })

def add_feeding(request, bird_id):
    # Create a ModelForm instance using the data in request.POST:
    form = FeedingForm(request.POST)
    # Validate the form:
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)

def assoc_tree(request, bird_id, tree_id):
    Bird.objects.get(id=bird_id).trees.add(tree_id)
    return redirect('detail', bird_id=bird_id)

def unassoc_tree(request, bird_id, tree_id):
    Bird.objects.get(id=bird_id).trees.remove(tree_id)
    return redirect('detail', bird_id=bird_id)

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'species', 'description', 'age']

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['species', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds'

class TreeList(ListView):
    model = Tree

class TreeDetail(DetailView):
    model = Tree

class TreeCreate(CreateView):
    model = Tree
    fields = '__all__'

class TreeUpdate(UpdateView):
    model = Tree
    fields = ['name', 'color']

class TreeDelete(DeleteView):
    model = Tree
    success_url = '/trees'