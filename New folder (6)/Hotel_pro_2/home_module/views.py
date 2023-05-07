from django.http import HttpRequest
from django.shortcuts import render, redirect

from home_module.forms import ContactUsForm, ReservationForm
from home_module.models import SettingSite_header, FoodsHotel, AboutSite, Moshtari, Contact, Booking, Reservation


# Create your views here.


def home_view(request: HttpRequest):
    # contact: Contact = Contact.objects.filter(see_text=True).first()
    setting_h: SettingSite_header = SettingSite_header.objects.filter(is_main_setting=True).first()
    food_h: FoodsHotel = FoodsHotel.objects.filter(is_active=True).first()
    about_h: AboutSite = AboutSite.objects.filter(is_active=True).first()
    moshtari: Moshtari = Moshtari.objects.filter(is_active=True).first()

    context = {
        # 'contact': contact,
        'setting_h': setting_h,
        'food_h': food_h,
        'about': about_h,
        'moshtari': moshtari,
        # 'form': form
    }

    return render(request, 'home_module/index_page.html', context)


def contact(request: HttpRequest):
    # contact_form = ContactUsForm(request.POST or None)
    # todo: or down
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contact_model = Contact(
                name=contact_form.cleaned_data.get('name'),
                email=contact_form.cleaned_data.get('email'),
                massage=contact_form.cleaned_data.get('subject')
            )
            contact_model.save()
            return redirect('index_page')

    else:
        contact_form = ContactUsForm()

    return render(request, 'home_module/contact.html', {
        'contact_form': contact_form
    })


# def index_view(request: HttpRequest):
#     if request.method == 'POST':
#         index_form = IndexForm(request.POST)
#         if index_form.is_valid():
#             index_model = Booking(
#                 start_date=index_form.cleaned_data.get('start_date'),
#                 end_date=index_form.cleaned_data.get('end_date'),
#                 room_number=index_form.cleaned_data.get('room_number')
#             )
#             index_model.save()
#             return redirect('index_page')
#
#     else:
#         index_form = IndexForm()
#
#     return render(request, 'home_module/index_page.html', {
#         'index_form': index_form
#     })

# def home(request):
#     rooms = Room.objects.all()
#     return render(request, 'home_module/index_page.html', {'rooms': rooms})
#
#
# def room_detail(request, room_id):
#     room = Room.objects.get(pk=room_id)
#     return render(request, 'home_module/index_page.html', {'room': room})
#
#
# def reservation(request, room_id):
#     room = Room.objects.get(pk=room_id)
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation.room = room
#             reservation.save()
#             return redirect('hotel:home')
#     else:
#         form = ReservationForm()
#     return render(request, 'home_module/index_page.html', {'form': form, 'room': room})


def ReservationView(request: HttpRequest):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            model_reservation = Reservation(
                check_in_date=form.cleaned_data.get('start_date'),
                check_out_date=form.cleaned_data.get('end_date'),
                number_of_guests=form.cleaned_data.get('number_gust')
            )

            model_reservation.save()
            return redirect('index_page')

    else:
        form = ReservationForm(request.POST)

    return render(request, 'home_module/booking.html', {
        'form': form
    })
