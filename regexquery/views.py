from django.shortcuts import render

from .form import RegexForm
import re

# Create your views here.
def regexquery_home_view(request):
    if request.method == 'POST':
        form = RegexForm(request.POST)
        if form.is_valid():
            action = request.POST['action']
            regex = form.cleaned_data['regex_input']
            string = form.cleaned_data['string_input']
            mapping = { 'full': re.fullmatch, 
                        'first': re.search,
                        'all': re.findall }
            matches = mapping[action](regex, string)
            if isinstance(matches, list):
                context = {'form': form, 'match': ",".join(matches), 'after': True}
            else:
                context = {'form': form, 'match': matches.group() if matches else None, 'after': True}
            return render(request, 'regexquery/home.html', context)
    else:
        return render(request, 'regexquery/home.html', {'form': RegexForm, 'after': False})