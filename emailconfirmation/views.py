from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from emailconfirmation.models import EmailAddress, EmailConfirmation



def confirm(request, confirmation_key):
    confirmation_key = confirmation_key.lower()
    email_address = EmailConfirmation.objects.confirm_email(confirmation_key)
    return render_to_response("emailconfirmation/confirm_email.html", {
        "email_address": email_address,
    }, context_instance=RequestContext(request))


@require_POST
@login_required
def delete(request):
    EmailAddress.objects.filter(user=request.user, email=request.POST.get("email", None)).delete()
    return redirect(request.REQUEST.get("next", "emailconfirmation_delete_done"))
