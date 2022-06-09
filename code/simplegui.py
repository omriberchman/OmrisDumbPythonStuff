from urllib import response
import PySimpleGUI as sg
import requests

layout = [
    [sg.Text("I want to hear a joke!")],
    [sg.Button("Joke")]
    ]
window = sg.Window("JokesAPI", layout)

url = "https://v2.jokeapi.dev/joke/Any?type=single"
def print_joke(url):
    result = requests.get(url)
    data = result.json()
    joke = data["joke"]
    return joke

while True:
    event , values = window.read()

    if event == "Joke":
        layout2 = [
            [sg.Text(print_joke(url))]
            ]
        window2 = sg.Window("Joke", layout2)
        window2.read()
    elif event == sg.WIN_CLOSED:
        break