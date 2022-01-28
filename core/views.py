from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from itertools import chain
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import random


@login_required(login_url="signin")
def index(request):
    pass


@login_required(login_url="signin")
def upload(request):
    pass


@login_required(login_url="signin")
def search(request):
    pass


@login_required(login_url="signin")
def like_post(request):
    pass


@login_required(login_url="signin")
def profile(request, pk):
    pass


@login_required(login_url="signin")
def follow(request):
    pass


@login_required(login_url="signin")
def setting(request):
    pass


def signup(request):
    pass


def signin(request):
    pass


@login_required(login_url="signin")
def logout(request):
    pass
