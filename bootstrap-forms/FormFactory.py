from htmlfactory import *

cdns = [
    TagFactory(
        "script",
        src="https://code.jquery.com/"
        + "jquery-3.2.1.slim.min.js",
        integrity="sha384-KJ3o2DKtIkvYIK3UENz"
        + "mM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN",
        crossorigin="anonymous"
    ),
    TagFactory(
        "script",
        src="https://cdnjs.cloudflare.com/ajax/"
        + "libs/popper.js/1.12.9/umd/popper.min.js",
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3m"
        + "gPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q",
        crossorigin="anonymous"
    ),
    TagFactory(
        "script",
        src="https://maxcdn.bootstrapcdn.com/"
        + "bootstrap/4.0.0/js/bootstrap.min.js",
        integrity="sha384-JZR6Spejh4U02d8jOt6v"
        + "LEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl",
        crossorigin="anonymous"
    )
]

bodyTag = TagFactory("body", cdns)
print(bodyTag.pretty_str())


class FormFactory():
    pass