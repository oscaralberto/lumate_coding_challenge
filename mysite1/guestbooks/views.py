from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from guestbooks.models import Entry, EntryForm
from django.core.context_processors import csrf
from guestbooks.models import Entry

def results(request):
  latest_guests = Entry.objects.all()
  template = loader.get_template('guestbooks/results.html')
  context = RequestContext(request, {'latest_guests' : latest_guests,})
  return HttpResponse(template.render(context))

def index(request):
  if request.method == 'POST':
    form = EntryForm(request.POST)
    if form.is_valid():
      form.save() 
      '''return HttpResponseRedirect('/guestbooks/results/')'''
      args0 = {}
      args0.update(csrf(request))
      args0['form'] = form
      return render_to_response('guestbooks/information_submitted.html', args0)
  else:
     form = EntryForm()
  '''return render(request, 'guestbooks/index.html', {
       'form': form,
    })'''
  args = {}
  args.update(csrf(request))
  args['form'] = form

  return render_to_response('guestbooks/index.html', args)

