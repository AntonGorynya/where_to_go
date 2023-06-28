from django.shortcuts import render, loader
from django.http import HttpResponse

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
