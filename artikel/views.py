from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from artikel.models import Kategori, Artikel
from artikel.forms import KategoriForms, ArtikelForms

def detail_artikel(request, id):
    template_name = "landingpage/detail_artikel.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect(not_found_artikel)
    
    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)
    
    context = {
        "title":"Artikel",
        "artikel": artikel,
        "artikel_lainnya":artikel_lainnya
    }
    return render(request, template_name, context)

###################### ADMIN #########################
@login_required(login_url='/auth-login')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
        return redirect(admin_kategori_list)
    forms = KategoriForms
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_kategori_list)
    forms = KategoriForms(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        messages.error(request, 'gagal delete kategori')
    
    return redirect(admin_kategori_list)


###################### Artikel Blog ##########################

@login_required(login_url='/auth-login')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = Artikel.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
        return redirect(admin_artikel_list)
    
    forms = ArtikelForms
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_artikel_update(request, id_kategori):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = Artikel.objects.get(id=id_kategori)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_kategori_list)
    forms = ArtikelForms(instance=Artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_artikel_delete(request, id_artikel):
    try:
        Kategori.objects.get(id=id_artikel).delete()
    except:
        messages.error(request, 'gagal delete kategori')
    
    return redirect(admin_artikel_list)
