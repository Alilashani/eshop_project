from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(label='نام و نام خانوادگی',
                           max_length=50,
                           error_messages={
                               'required': 'لطفا این فیلد رو پر کن کصکش',
                               'max_length': 'نام و نام کصکشت نمیتونه بیشتر از 50 کارکتر باشه'
                           },
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'نام و نام خانوادگی'
                           }))
    email = forms.EmailField(label='ایمیل', error_messages={
        'required': 'لطفا این فیلد رو پر کن کصکش'
    }, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }
    ))
    subject = forms.CharField(label='متن', error_messages={
        'required': 'لطفا این فیلد رو پر کن کصکش'
    },
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'متن'
                                  }
                              ))


# class IndexForm(forms.Form):
#     start_date = forms.DateField(
#         label='تاریخ ورود',
#         error_messages={
#             'required': 'لطفا تاریخ ورود را مشخص کنید'
#         },
#         widget=forms.DateInput(
#             attrs={
#                 'class': 'col-md-3',
#                 'placeholder': '2023/02/13'
#             }
#         )
#     ),
#     end_date = forms.DateField(
#         label='تاریخ خروج',
#         error_messages={
#             'required': 'لطفا تاریخ خروج را مشخص کنید'
#         },
#         widget=forms.DateInput(
#             attrs={
#                 'class': 'col-md-3',
#                 'placeholder': '2023/02/16'
#             }
#         )
#     ),
#     room_number = forms.IntegerField(
#         label='تعداد اتاق',
#         error_messages={
#             'required': 'لطفا تعداد اتاق ها را مشخص کنید'
#         },
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'col-md-3',
#                 'placeholder': '1'
#             }
#         )
#     )


# class ReservationForm(ModelForm):
#     check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#
#     class Meta:
#         model = Reservation
#         fields = ['room', 'guest', 'check_in', 'check_out']


class ReservationForm(forms.Form):
    start_date = forms.DateField(
        label='تاریخ ورود را وارد کنید',
        error_messages={
            'required': 'لطفا تعداد اتاق ها را مشخص کنید'
        },
        widget=forms.DateInput(
            attrs={
                'class': 'form-group',
                'placeholder': 'mm/dd/yyy',
                'type': 'date'
            }
        ),
        required=True
    ),
    end_date = forms.DateField(
        label='تاریخ خروج را وارد کنید',
        error_messages={
            'required': 'لطفا تعداد اتاق ها را مشخص کنید'
        },
        widget=forms.DateInput(
            attrs={
                'class': 'form-group',
                'placeholder': 'mm/dd/yyy',
                'type': 'date'
            }
        ),
        required=True
    ),
    number_gust = forms.IntegerField(
        label='تعداد مهمان ها',
        error_messages={
            'required': 'لطفا تعداد اتاق ها را مشخص کنید'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'form-group',
                'placeholder': '2'
            }
        ),
        required=True
    )
