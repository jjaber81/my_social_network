'''
Views.py file
'''

from django.views.generic import TemplateView
class HomePage(TemplateView):
    '''
    Home Page
    '''
    template_name = 'index.html'

class SuccessPage(TemplateView):
    template_name = 'success.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'