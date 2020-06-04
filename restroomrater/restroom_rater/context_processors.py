from .forms import get_zip

def search_form(request):
    return {
        'search_form' : get_zip()
    }