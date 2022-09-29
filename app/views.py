from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass


@dataclass
class Car:
    name: str
    desc: str
    types: list


cars = {
    "charger": Car("Dodge Charger", "Its powerful engine offerings make it unlike anything else in the sparsely populated large car class. Ride and handling are decent as well. This sedan has roomy and comfortable seating, a spacious trunk, and user-friendly infotainment features.", ["SXT", "GT", "R/T", "Scat Pack", "Scat Pack Widebody", "SRT Hellcat Widebody", "SRT Hellcat Redeye Widebody", "SRT Jailbreak"]),
    "camaro": Car("Chevrolet Camaro", "An iconic American automobile, Camaro continues to push the limits of performance and style. With aerodynamic looks and a refined, driver-centric interior, it’s built to seamlessly integrate form, high-powered function and flair.", ["1LS", "1LT", "2LT", "3LT", "LT1", "1SS", "2SS", "ZL1"]),
    "mustang": Car("Ford Mustang", "Hear the roar of a Mustang as the ground starts to tremble and your legs start to shake. As always, Mustang draws upon its performance roots with features for enhanced handling, high-powered engine options and a classic Mustang design.", ["ECOBOOST Fastback", "GT Fastback", "ECOBOOST Convertible", "GT Premium Fastback", "Mach 1", "Shelby GT500"])

}
# Create your views here.

def car_list(request):
    return render(request, "home.html")

def detail(request, cn):
    choice = cars[cn]
    context = {
        "name":choice.name,
        "desc":choice.desc,
        "types":choice.types,
    }
    return render(request, "detail.html", context)
