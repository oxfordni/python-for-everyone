# Project

## Building UIs

There are essentially 4 big Python UI libraries:

1. [Tkinter][tkinter]
1. [wxPython][wxpython]
1. [PyQT][pyqt]
1. [Remi][remi]

Python libraries, in general, make a very good job of abstracting away the
_super technical_. Though everything that we like about Python is nowhere to be
found in using these libraries.

To our delight, however, there is a fourth option. A simpler way to start
building Python UIs is called [PySimpleGUI][pysimplegui]. Under the hood, this
library is using all the 4 popular libraries, but abstracts away the
_super technical_.

We can focus on what matters!

## Example

Let's start with a [simple example][example]: the traditional `Hello, world!`.

<!-- References -->

[example]: ./example/README.md
[pyqt]: https://www.riverbankcomputing.com/software/pyqt/
[pysimplegui]: https://github.com/PySimpleGUI/PySimpleGUI
[remi]: https://github.com/dddomodossola/remi
[tkinter]: https://docs.python.org/3/library/tkinter.html
[wxpython]: https://www.wxpython.org/
