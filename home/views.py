from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# from glosowania.views import ZliczajWszystko
from glosowania.models import Decyzja
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _


def home(request):
    ongoing = Decyzja.objects.filter(status=4).order_by('data_referendum_start')
    upcoming = Decyzja.objects.filter(status=3).order_by('data_referendum_start')

    # data_referendum_start = ZliczajWszystko.kolejka
    return render(request,
                  'home/home.html',
                  {
                    'ongoing': ongoing,
                   'upcoming': upcoming,
                   })


@login_required
def haslo(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, _('Your password has been changed.'))
            return redirect('haslo')
        else:
            messages.error(request, _('You typed something wrong. See what error appeared above and try again.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home/haslo.html', {
        'form': form
    })
