from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Advanced Python Final Project: Welcome Page")

	# Begin homepage here
	