from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.views import View

from .models import Event, Ticket_Booking, Categorie, Currencie
from .forms import *
from .decorators import *

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def home(request):
    events = Event.objects.all()
    currencies = Currencie.objects.all()
    default_currency = Currencie.objects.get(name='usd')
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    if request.method == 'POST':
        currency_name = request.POST.get('currency_name')
        currency = Currencie.objects.get(name=currency_name)
        return render(request, 'index.html', context={"currency": currency, "events": events, "currencies": currencies, "group": group})

    context = {
        "events": events,
        "group": group,
        "currencies": currencies,
        "default_currency": default_currency.name,
    }
    return render(request, 'index.html', context=context)


@unauthenticated_user
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            remember_me = request.POST.get('remember-me')
            if remember_me is not True:
                request.session.set_expiry(0)

            if request.GET.get('next') == None:
                return redirect('home')
            elif request.GET.get('next') != None:
                return redirect(request.GET.get('next'))
        else:
            messages.info(request, "User or Password is either incorrect")
            return render(request, "login.html", context={"errors": "User or Password is either incorrect"})
    return render(request, 'login.html')


@login_required(login_url="/login")
def log_out(request):
    logout(request)
    return redirect('home')


def registration(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST.get('username')
            password = request.POST.get('password')

            Users.objects.get(username=username).groups.add(
                Group.objects.get(name='users'))

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if request.GET.get('next') == None:
                    return redirect('home')
                elif request.GET.get('next') != None:
                    return redirect(request.GET.get('next'))
    context = {
        "form": form
    }
    return render(request, 'registration.html', context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['users', 'admin'], action="add_events")
def add_events(request):
    category = Categorie.objects.all()

    context = {
        "category": category,
        "stream": [_[1] for _ in Event.STREAM],
        "event_type": [_[1] for _ in Event.EVENT_TYPE],
    }
    return render(request, 'create-events.html', context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['users', 'admin'], action="book")
def ticket_booking(request, *args, **kwargs):
    event_id = kwargs["pk"]
    event = Event.objects.get(id=event_id)

    currency_name = kwargs['currency']
    currency = Currencie.objects.get(name=currency_name)

    context = {
        'event': event,
        'currency': currency,
        'proper_currency': [proper_locale for (locale, proper_locale) in currency.CURRENCY if currency.name in locale][0],
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'ticket_booking.html', context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['users', 'admin'], action="refund")
def refund(request, *args, **kwargs):
    event_id = kwargs['pk']
    event = Event.objects.get(id=event_id)

    refund_reasons = Refund.reasons

    form = RefundForm()
    if request.method == 'POST':
        form = RefundForm(request.POST)
        if form.is_valid():
            stripe.Refund.create(
                amount=request.POST.get('quantity'),
                price=event.price,
                payment_intent=stripe.PaymentIntent.get(event=event_id)
            )
            return redirect('home')

    context = {
        'event': event,
        'event_id': event_id,
        'form': form,
        'refund_reasons': refund_reasons,
    }
    return render(request, 'refund.html', context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['users', 'admin'], action="edit")
def edit(request, **kwargs):
    event_id = kwargs['pk']
    event = Event.objects.get(id=event_id)

    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "event": event,
        "form": form,
    }
    return render(request, 'edit.html', context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['users', 'admin'], action='delete')
def delete(request, *args, **kwargs):
    event_id = kwargs['pk']
    event = Event.objects.get(id=event_id)

    if request.method == "POST":
        event.delete()

    context = {
        "event": event,
    }
    return render(request, 'delete.html', context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['users', 'admin'], action='create_object')
def create_object(request, *args, **kwargs):

    form = CreateObjectForm(model_name=kwargs.get('model_name'))
    if request.method == 'POST':
        form = CreateObjectForm(
            request.POST, model_name=kwargs.get('model_name'))
        if form.is_valid():
            print(form)
            return redirect(request.META.get('HTTP_REFERER', '/'))

    context = {
        'form': form,
        'model_name': kwargs['model_name']
    }
    return render(request, 'create-model.html', context=context)


@login_required(login_url="/login")
def success(request):
    return render(request, 'success.html')


@login_required(login_url="/login")
def cancel(request):
    return render(request, 'cancel.html')


class CreateCheckoutSession(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        event_id = kwargs["pk"]
        event = Event.objects.get(id=event_id)

        currency_name = kwargs['currency']
        currency = Currencie.objects.get(name=currency_name)

        YOUR_DOMAIN = request.META["HTTP_ORIGIN"]
        print(kwargs, args, request.POST, request.GET)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': currency.name,
                        'unit_amount_decimal': event.price * 100,  # type: ignore
                        'product_data': {
                            'name': event.title,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'product_id': event.id  # type: ignore
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


@login_required(login_url="/login")
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400, content=f"{e}")
    except stripe.error.SignatureVerificationError as e:  # type: ignore
        # Invalid signature
        return HttpResponse(status=400, content=f"{e}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        product_id = session["metadata"]["product_id"]

        product = Event.objects.get(id=product_id)

    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        product_id = intent["metadata"]["product_id"]

        product = Event.objects.get(id=product_id)

    return HttpResponse(status=200)


class PaymentIntent(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        try:
            event_id = kwargs["pk"]
            event = Event.objects.get(id=event_id)

            currency_name = kwargs['currency']
            currency = Currencie.objects.get(name=currency_name)

            intent = stripe.PaymentIntent.create(
                amount=event.price,
                currency=currency.name,
                meta={
                    'event': event.id,
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret'],
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
