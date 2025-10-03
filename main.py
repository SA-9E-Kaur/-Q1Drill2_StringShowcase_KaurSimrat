# main.py
from pyscript import when, display, document

@when("click", "#submit-btn")
def show_profile(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    # Clear previous message
    document.querySelector("#output").innerText = ""

    # Example: assigning strings to variables
    intro = "Student Information"
    divider = "-" * 25

    # Multiline string with escape characters
    message = f"""{intro}\n{divider}
Name:\t{name}
Age:\t{age}
School:\t{school}

Summary:
\"{name}\" is {age} years old and studies at {school}.
This was created using Python strings and displayed with PyScript.
"""

    display(message, target="output")



