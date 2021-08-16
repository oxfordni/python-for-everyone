import os
import humanize
import PySimpleGUIWx as ui

# Ask the user to select a file from their drive
filename = ui.popup_get_file('Select the file to process from your drive')

# Get the file size (in bytes)
file_size = os.stat(filename).st_size 

# Convert to human readable (in a multiple of bytes, e.g. KiB, MiB, ...)
readable_file_size = humanize.naturalsize(file_size, binary=True)

# Confirm that the file was selected
ui.popup('You selected:', f'{filename} ({readable_file_size})')
