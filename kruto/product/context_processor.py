from .forms import CallbackForm

def callback_form(request):
    return {
        'callback_form': CallbackForm()
    }

