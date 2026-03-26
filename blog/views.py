from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Post
from .forms import ContactForm


def home(request):
    posts = Post.objects.all()[:3]
    return render(request, 'home.html', {"posts": posts})

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {"posts": posts})

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_detail.html', {"post": post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Consultation Request from {name} — Profile Associate"
            body = f"""New consultation request from the website:

Name: {name}
Email: {email}

Message:
{message}

---
Sent from Profile Associate contact form
"""
            recipient = "radhikari201@gmail.com"
            try:
                msg = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[recipient],
                    reply_to=[email],
                )
                msg.send(fail_silently=False)
                messages.success(
                    request,
                    "Thank you! Your message has been sent. We will get back to you shortly.",
                )
                return redirect("contact")
            except Exception as e:
                messages.error(
                    request,
                    "Sorry, we could not send your message. Please try calling us directly.",
                )
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
