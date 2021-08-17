#!./env/bin/python
import PySimpleGUIQt as sg

# We start by defining some settings that can be modified at any time
NOTEPAD_VERSION = '1.0'
NOTEPAD_TITLE = 'Notepad'
NOTEPAD_THEME = 'Dark2'
EDITOR_COLOR_BACKGROUND = '#191919'
EDITOR_COLOR_TEXT = '#ffffff'
EDITOR_FONT = ('Courier New', 14)
EDITOR_SIZE = (800, 600)

# Some useful constants
KEY_EDITOR = '-EDITOR-'
EVENT_EXIT = 'Exit'
EVENT_LOAD = 'Load'
EVENT_QUIT = 'Quit'
EVENT_SAVE = 'Save'
QUIT_EVENTS = (sg.WIN_CLOSED, EVENT_EXIT, EVENT_QUIT)
btnOpts = {
    'size': (60, 30),
    'border_width': 0,
    'button_color': ('#ffffff', '#282828'),
    'pad': ((0, 4), (4, 0)),
}

# Let's apply our overall Theme, for a complete list: sg.theme_list()
sg.theme(NOTEPAD_THEME)

# The most important part of our notepad is the multiline editor
editor = sg.Multiline(
    default_text='',
    key=KEY_EDITOR,
    font=EDITOR_FONT,
    background_color=EDITOR_COLOR_BACKGROUND,
    text_color=EDITOR_COLOR_TEXT,
    focus=True,
    pad=(0, 0),
    size=EDITOR_SIZE,
    # expand_x=True,
)

# The second most important part of our notepad is the layout of the editor
layout = [
    [editor],
    [sg.Button(EVENT_LOAD, **btnOpts), sg.Button(EVENT_SAVE, **btnOpts), sg.Button(EVENT_EXIT, **btnOpts)],
]

# We create a window, and pass it our layout
window = sg.Window(
    NOTEPAD_TITLE,
    layout,
    size=EDITOR_SIZE,
)

# Our main event loop, this is what keeps the app running and updating
while True:
    event, values = window.read()
    # print(event, values)
    if event in QUIT_EVENTS:
        # Break out of the loop if the user wants to close the window
        break
    if event == EVENT_LOAD:
        print('not implemented yet')
        continue
    if event == EVENT_SAVE:
        print(values[KEY_EDITOR])

# Some cleanup before the app terminates
window.close()
