from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.db.models import Q

# ✅ Home Page View
def home(request):
    return render(request, 'home.html')

# ✅ Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('browse')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# ✅ Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('browse')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ Upload Note View
@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('browse')
    else:
        form = NoteForm()
    return render(request, 'upload.html', {'form': form})

# ✅ Browse Notes View with Search
def browse_notes(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        notes = Note.objects.all()
    return render(request, 'browse.html', {'notes': notes})
