from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from events.forms import MoodForm
from events.models import Event
from django.views import generic


@login_required
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login')

class Signup(View):

    def get(self, request):
        form = UserCreationForm(request.GET)
        return render(request, 'Signup.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})


class EventsListView(generic.ListView):
    model = Event
    context_object_name = 'events_list'
    template_name = 'events.html'


class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event_details'
    template_name = 'event_details.html'


class ParticipationView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

    # def get_queryset(self):
    #     return Event.objects.filter()[:5]  # Get 5 events

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(EventListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context



###################################################################################


# class Index(View):
#
#     def get(self, request):
#         user = request.user
#         print(user)
#         form = EventForm(request.GET)
#         events = Event.objects.all()
#         return render(request, 'events.html', {'events': events, 'user': user, 'form': form})
#
#     def post(self,request):
#         form = EventForm(request.POST)
#         print('Printing the form data...\n', form.data)
#         user = request.user
#         print('The current user is: ', user)
#         if form.is_valid():
#             print("Form is valid")
#             try:
#                 obj = form.save()
#                 print("The mood was saved in the database")
#
#                 return render(request, 'participate.html', {'events': form, 'user': user})
#             except:
#                     print("The mood did not save in the database")
#                     pass
#         else:
#             form = EventForm()
#         return render(request, 'events.html', {'form': form})
#
#
# class Participate(View):
#
#     def get(self, request):
#         user = request.user
#
#         form = ParticipateForm(request.GET)
#         return render(request, 'participate.html', {'form': form, 'user': user})
#
#     def post(self,request):
#         form = EventForm(request.POST)
#         print('Printing the form data...\n', form.data)
#         user = request.user
#         print('The current user is: ', user)
#         if form.is_valid():
#             print("Form is valid")
#             try:
#                 obj = form.save()
#                 print("The mood was saved in the database")
#
#                 return render(request, 'participate.html', {'events': form, 'user': user})
#             except:
#                     print("The mood did not save in the database")
#                     pass
#         else:
#             form = EventForm()
#         return render(request, 'events.html', {'form': form})

#################################################################################

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect
from events.forms import MoodForm
from events.models import Mood
from django.forms import modelformset_factory
from .forms import PostModelForm
from events.models import Post


class Index(View):

    def get(self, request):
        form = MoodForm(request.GET)
        return render(request, 'show.html', {'form': form})

    def post(self,request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    print("From index\post\sucess")
                    return redirect('/show')
                except:
                    pass
        else:
            print("From index\post\fail")
            form = MoodForm()
        return render(request,'index.html',{'form':form})




class Index2(View):

    def get(self, request):
        form = MoodForm(request.GET)
        return render(request, 'show.html', {'form': form})

    def post(self,request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            if form.is_valid():
                try:
                    form.save()

                    return redirect('/show')
                except:
                    pass
        else:
            form = MoodForm()
        return render(request,'reg_form.html',{'form':form})


# show all the data on html
class Show(View):

    def get(self, request):
        form = MoodForm(request.GET)
        employees = Mood.objects.all()
        return render(request, "show.html", {'employees': employees})

    def post(self, request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            print("Hii")
            if form.is_valid():
                try:
                    form.save()
                    print('form saved')
                    print(form.data)
                    print(type(form.data))
                    return redirect('/show')
                except:
                    pass
        else:
            print('form did not saved')
            form = MoodForm()
        return render(request, 'index.html', {'form': form})

# for delete perticular record
class Delete(View):

    def get(self,request, id):
        mood = Mood.objects.get(id=id)
        mood.delete()

        return redirect("/show")

    def post(self, request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            if form.is_valid():
                try:
                    return redirect('show')
                except:
                    pass
        else:
            form = MoodForm()
        return render(request, 'index.html', {'form': form})


class Birthday(View):

    def get(self, request):
        employees = Mood.objects.all()
        return render(request, "Birthday.html", {'employees': employees})


class Dance(View):

    def get(self, request):
        employees = Mood.objects.all()
        return render(request, "Dance.html", {'employees': employees})

class Music(View):

    def get(self, request):
        employees = Mood.objects.all()
        return render(request, "Music.html", {'employees': employees})


class SkinBurn(View):

    def get(self, request):
        employees = Mood.objects.all()
        return render(request, "SkinBurn.html", {'employees': employees})

class Ai(View):

    def get(self, request):
        employees = Mood.objects.all()
        return render(request, "Ai.html", {'employees': employees})


############# FORMSET ####################

class Formset(View):

    def get(self,request):

        PostModelFormset = modelformset_factory(Post, form=PostModelForm)
        formset = PostModelFormset(request.POST or None, queryset=Post.objects.all())
        context = {'formset': formset}
        return render(request, 'formset.html', context)


    def post(self,request):
        PostModelFormset = modelformset_factory(Post, form=PostModelForm)
        formset = PostModelFormset(request.POST or None, queryset=Post.objects.all())

        if formset.is_valid():
            for form in formset:
                obj = form.save(commit=False)
                if form.cleaned_data:
                    obj.save()
        context = {'formset': formset}
        return render(request, 'formset.html', context)