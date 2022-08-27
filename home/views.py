from django.shortcuts import render
from feedback.forms import PeopleForm
from news.models import *
from product.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def homepage(request):
    news_items = News.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True).order_by('-pk')[:6]

    return render(request, 'home.html', locals())


def info_page(request):
    return render(request, 'info.html', locals())


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'tovar.html', locals())


def katalog_common(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products_images = ProductImage.objects.filter(Q(articul__icontains=search_query) | Q(name__icontains=search_query), is_active=True, is_main=True)

    else:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True)

    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, "katalog_common.html", locals())


def k_plugam(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=1)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_plugam.html', context)


def k_boronam(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, category_id=3)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_boronam.html', context)


def borona_bzss(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, podcategory_id=2)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'borona_bzss.html', context)


def borona_bdt(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=3)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'borona_bdt.html', context)


def borona_diskopak(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=4)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'borona_diskopak.html', context)


def borona_bdn(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'borona_bdn.html', context)


def k_kultivatoram(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=4)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kultivatoram.html', context)


def kultiv_AKSH_6(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'kultiv_AKSH_6.html', context)


def kultiv_KH_5(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=7)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'kultiv_KH_5.html', context)


def kultiv_KPS_6(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=8, is_main=True)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'kultiv_KPS_6.html', context)


def k_posevnim(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=5, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_posevnim.html', locals())


def posev_spy_6(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=9, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_spy6.html', locals())


def posev_skp_12(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=10, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_skp12.html', locals())


def posev_app_6a(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=11, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_app_6a.html', locals())


def posev_app_6g(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=12, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_app_6g.html', locals())


def posev_app_6d(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=13, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_app_6d.html', locals())


def posev_app_6p(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=14, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_app_6p.html', locals())


def posev_appm_6(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=15, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=5)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'K_posevnim_appm_6.html', locals())


def k_kosilkam(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=6, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam.html', locals())


def k_kosilkam_fc_352(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=16, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam_fc_352.html', locals())


def k_kosilkam_kdl_3(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=17, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam_kdl_3.html', locals())


def k_kosilkam_disco(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=18, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam_disco.html', locals())


def k_kosilkam_kdn_210(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=19, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam_kdn_210.html', locals())


def k_kosilkam_kmp_9(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=20, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam_kmp_9.html', locals())


def k_kosilkam_kpr_9(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=21, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=6)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kosilkam_kpr_9.html', locals())


def k_grabliam(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=7, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=7)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_grabliam.html', locals())


def k_grabliam_gvb_6(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=22, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=7)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_grabliam_gvb_6.html', locals())


def k_grabliam_liner(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=23, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=7)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_grabliam_liner.html', locals())


def k_grabliam_bbp_7(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=24, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=7)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_grabliam_bbp_7.html', locals())


def k_grabliam_volto(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=25, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=7)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_grabliam_volto.html', locals())


def k_pres_pod(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=8, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=8)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_pres_pod.html', locals())


def k_korm_ubor(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=9, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=9)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_korm_ubor.html', locals())


def k_korm_ubor_kpk_3000(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=27, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=9)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_korm_ubor_kpk_3000.html', locals())


def k_korm_ubor_kvk_800(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=28, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=9)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_korm_ubor_kvk_800.html', locals())


def k_korm_ubor_kvk_8060(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=29, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=9)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_korm_ubor_kvk_8060.html', locals())


def k_korm_ubor_jaguar(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=30, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=9)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_korm_ubor_jaguar.html', locals())


def k_korm_ubor_john(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=31, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=9)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_korm_ubor_john.html', locals())


def k_zern_ubor(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=13, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=13)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_zern_ubor.html', locals())


def k_kartosh_ubor(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=10, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=10)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_kartosh_ubor.html', locals())


def k_rasbrasivat(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=11, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=11)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_rasbrasivat.html', locals())


def k_rasbrasivat_prt_10(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=34, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=11)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_rasbrasivat_prt_10.html', locals())


def k_rasbrasivat_pmf_18(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=35, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=11)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_rasbrasivat_pmf_18.html', locals())


def k_traktoram(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=12, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=12)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_traktoram.html', locals())


def k_traktoram_belarus(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=36, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=12)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_traktoram_belarus.html', locals())


def k_traktoram_mtz(request):
    products_images = ProductImage.objects.filter(is_active=True, podcategory_id=37, is_main=True)
    category = ProductCategory.objects.get(is_active=True, id=12)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'k_traktoram_mtz.html', locals())


def metizi_i_rasxod(request):
    products_images = ProductImage.objects.filter(is_active=True, category_id=14)
    category = ProductCategory.objects.get(is_active=True, id=14)
    paginator = Paginator(products_images, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'page' in request.GET:
        page = request.GET['page']

    else:
        page = 1
    paginator = Paginator(products_images, 16)
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        products_images = paginator.page(1)
    except EmptyPage:
        products_images = paginator.page(paginator.num_pages)

    context = {
        'products_images': products_images,
        'page_obj': page_obj
    }

    return render(request, 'metizi_i_rasxod.html', locals())


def kontacts_page(request):
    form = PeopleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # print(request.POST)
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # print(data["Имя"])

        new_form = form.save()

    return render(request, 'kontacts.html', locals())

# Create your views here.
