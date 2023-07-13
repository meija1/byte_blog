from . models import Post, Category


def site_settings(request):

    categories = Category.objects.all()

    return {'categories': categories}
