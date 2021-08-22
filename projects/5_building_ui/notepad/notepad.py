#!./env/bin/python
import os
import PySimpleGUIQt as sg

# We start by defining some settings that can be modified at any time
NOTEPAD_VERSION = '1.0'
NOTEPAD_TITLE = 'Notepad'
UNSAVED_INDICATOR = '*'
NOTEPAD_THEME = 'Dark2'
NOTEPAD_AUTHOR = 'João Carmo'
EDITOR_COLOR_BACKGROUND = '#191919'
EDITOR_COLOR_TEXT = '#ffffff'
EDITOR_FONT = ('Courier New', 14)
EDITOR_SIZE = (800, 600)
EDITOR_BUTTON_COLOR = ('#ffffff', '#282828')
EDITOR_EXTENSION = '.txt'

# Some useful constants
USER_HOME = os.path.expanduser('~')
KEY_EDITOR = '-EDITOR-'
KEY_MENU = '-MENU-'
EVENT_ABOUT = 'About...'
EVENT_COPY = 'Copy'
EVENT_CUT = 'Cut'
EVENT_CLEAR = 'Clear'
EVENT_EXIT = 'Exit'
EVENT_OK = 'OK'
EVENT_OPEN = 'Open'
EVENT_PASTE = 'Paste'
EVENT_QUIT = 'Quit'
EVENT_REDO = 'Redo'
EVENT_SAVE = 'Save'
EVENT_SAVE_AS = 'Save As'
EVENT_SELECTALL = 'Select All'
EVENT_UNDO = 'Undo'
QUIT_EVENTS = (sg.WIN_CLOSED, EVENT_EXIT, EVENT_QUIT)
BUTTON_OPTIONS = {
    'size': (60, 30),
    'border_width': 0,
    'button_color': EDITOR_BUTTON_COLOR,
    'pad': ((0, 4), (4, 0)),
}

# Some helpful globals
CURRENTLY_OPEN_FILE = ''
DOCUMENT_INITIAL_LENGTH = 0
DOCUMENT_INITIAL_HASH = 0
HAS_UNSAVED_CHANGES = False

# Let's apply our overall Theme, for a complete list: sg.theme_list()
sg.theme(NOTEPAD_THEME)
sg.set_options(element_padding=(0, 0))

# The most important part of our notepad is the multiline editor
editor = sg.Multiline(
    default_text='',
    key=KEY_EDITOR,
    font=EDITOR_FONT,
    background_color=EDITOR_COLOR_BACKGROUND,
    text_color=EDITOR_COLOR_TEXT,
    focus=True,
    size=EDITOR_SIZE,
)

# Our app should also have a menu
menu_def = [
    ['&File', [f'&{EVENT_OPEN}', f'&{EVENT_SAVE}', EVENT_SAVE_AS, 'E&xit']],
    [
        '&Edit',
        [
            EVENT_UNDO,
            EVENT_REDO,
            '---',
            EVENT_CUT,
            EVENT_COPY,
            EVENT_PASTE,
            EVENT_CLEAR,
            '---',
            EVENT_SELECTALL,
        ],
    ],
    ['&Help', f'&{EVENT_ABOUT}'],
]

menu = sg.Menu(menu_def, key=KEY_MENU)

# The second most important part of our notepad is the layout of the editor
layout = [
    [menu],
    [editor],
    [
        sg.Button(EVENT_OPEN, **BUTTON_OPTIONS),
        sg.Button(EVENT_SAVE, **BUTTON_OPTIONS),
        sg.Button(EVENT_SAVE_AS, **BUTTON_OPTIONS),
        sg.Button(EVENT_EXIT, **BUTTON_OPTIONS)
    ],
]

# We create a window, and pass it our layout
window = sg.Window(
    NOTEPAD_TITLE,
    layout,
    size=EDITOR_SIZE,
)

# We should always try to split our code into smaller functions
def validate_changes(value):
    """
    Validate the changes to the editor, returns True if there are unsaved
    changes
    """
    if len(value) != DOCUMENT_INITIAL_LENGTH:
        return True
    if hash(value) != DOCUMENT_INITIAL_HASH:
        return True
    return False

def confirm_exit():
    """Confirm exit from the editor, if there are unsaved changes"""
    return sg.popup_ok_cancel(
        'Are you sure you want to exit?',
        title='Unsaved changes',
        button_color=EDITOR_BUTTON_COLOR,
        font=EDITOR_FONT,
        grab_anywhere=True,
    )

def load_file(filename):
    """Load a file into the editor"""
    if not filename:
        return 0, 0
    with open(filename, 'r') as f:
        contents = f.read()
        window[KEY_EDITOR].update(contents)
        return len(contents), hash(contents)

def save_file(filename, contents):
    """Save a file from the editor"""
    if not filename:
        return 0, 0
    with open(filename, 'w') as f:
        f.write(contents)
        return len(contents), hash(contents)

def show_about():
    # We temporarily hide the main window and display an information message
    window.disappear()
    sg.popup(
        f'{NOTEPAD_TITLE} {NOTEPAD_VERSION}',
        f'by {NOTEPAD_AUTHOR}',
        '',
        title=EVENT_ABOUT,
        custom_text=EVENT_OK,
        button_color=EDITOR_BUTTON_COLOR,
        font=EDITOR_FONT,
        grab_anywhere=True,
    )
    window.reappear()

# Our main event loop, this is what keeps the app running and updating
while True:
    # We constantly read the events and values from our window
    event, values = window.read()
    # We can check if changes have been made to the document
    HAS_UNSAVED_CHANGES = validate_changes(values[KEY_EDITOR])
    if event in QUIT_EVENTS:
        # Break out of the loop if the user wants to close the window, checks
        # if there are unsaved changes
        if not HAS_UNSAVED_CHANGES or confirm_exit() == 'OK':
            break
    if event == EVENT_ABOUT:
        # Using a dedicated function to handle the about event
        show_about()
        # We use the continue statement to return to the top of the loop
        continue
    if event == EVENT_OPEN:
        # We open a file browser dialog for the user to select a file to open
        CURRENTLY_OPEN_FILE = sg.popup_get_file(
            'Select a file to open',
            EVENT_OPEN,
            initial_folder=USER_HOME,
            no_window=True,
            default_extension=EDITOR_EXTENSION,
        )
        DOCUMENT_INITIAL_LENGTH, DOCUMENT_INITIAL_HASH = load_file(CURRENTLY_OPEN_FILE)
        continue
    if event == EVENT_SAVE and CURRENTLY_OPEN_FILE:
        # We save the document into the previously opened file
        current_document = values[KEY_EDITOR]
        DOCUMENT_INITIAL_LENGTH, DOCUMENT_INITIAL_HASH = save_file(CURRENTLY_OPEN_FILE, current_document)
        continue
    if (event == EVENT_SAVE_AS or
            (event == EVENT_SAVE and not CURRENTLY_OPEN_FILE)):
        # We open a file browser dialog for the user to select a file to save
        CURRENTLY_OPEN_FILE = sg.popup_get_file(
            'Select a file to save',
            EVENT_SAVE_AS,
            initial_folder=USER_HOME,
            save_as=True,
            no_window=True,
            default_extension=EDITOR_EXTENSION,
        )
        current_document = values[KEY_EDITOR]
        DOCUMENT_INITIAL_LENGTH, DOCUMENT_INITIAL_HASH = save_file(CURRENTLY_OPEN_FILE, current_document)
        continue
    if event == EVENT_UNDO:
        # We undo the last action
        window[KEY_EDITOR].Widget.undo()
        continue
    if event == EVENT_REDO:
        # We redo the last action
        window[KEY_EDITOR].Widget.redo()
        continue
    if event == EVENT_CUT:
        # We copy the contents of the editor into the clipboard
        # and delete the contents of the editor
        window[KEY_EDITOR].Widget.cut()
        continue
    if event == EVENT_PASTE:
        # We paste the contents of the clipboard into the editor
        window[KEY_EDITOR].Widget.paste()
        continue
    if event == EVENT_COPY:
        # We copy the contents of the editor into the clipboard
        window[KEY_EDITOR].Widget.copy()
        continue
    if event == EVENT_CLEAR:
        # We delete the contents of the editor
        window[KEY_EDITOR].Widget.clear()
        continue
    if event == EVENT_SELECTALL:
        # We select all the contents of the editor
        window[KEY_EDITOR].Widget.selectAll()
        continue

# Some cleanup before the app terminates
window.close()
