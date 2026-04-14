from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')
def experience_view(request):
    return render(request, 'pages/experience.html')
def contact_view(request):
    # means the form is submitted and not empty
    # to send email
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # collect the data from the form and send email
        if form.is_valid():
            name = form.cleaned_data['name']
            email =  form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Build the full email content
            message_body = (
                f'You have a new email from you Portfolio \n'
                f'name: {name} \n'
                f'email: {email}\n'
                f'message: {message}\n'
            )
            try:
                # send the email using django's send_email function
                print("send email")
                send_mail(
                    "Email From Portfolio", # subject
                    message_body, # message
                    email, # from email
                    ['rrpieces86@gmail.com']
                )
                form = ContactForm() # clear the form after successful submission
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f'Error sending email: {e}')
                return render(request, 'pages/contact.html',{'form': form})
        else:
            print ("Form is not valid")
            print(form.errors)
            return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})
