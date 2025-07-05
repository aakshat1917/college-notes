from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Note
from .forms import NoteForm
from django.db.models import Q


# ✅ Signup View
def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect('upload')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ✅ Upload Note View (only for logged-in users)
@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploader = request.user
            note.save()
            return redirect('browse')
    else:
        form = NoteForm()
    return render(request, 'upload.html', {'form': form})


# ✅ Browse Notes View with Search Support
def browse_notes(request):
    query = request.GET.get('q')
    filter_by = request.GET.get('filter')

    notes = Note.objects.all()

    if query:
        notes = notes.filter(
            Q(title__icontains=query) |
            Q(subject__icontains=query) |
            Q(tags__icontains=query)
        )

    if filter_by == 'free':
        notes = notes.filter(is_paid=False)
    elif filter_by == 'paid':
        notes = notes.filter(is_paid=True)

    return render(request, 'browse.html', {'notes': notes})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
