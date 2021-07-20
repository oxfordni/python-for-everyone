# Python For Everyone

The team behind this course is going to share some helpful resourses for Python
programming as well as some tips and tricks for using Python in your daily
activities.

All the materials used in these lessons will be made available for everyone to
play with and to learn from. These include the presentations and examples.

The summary and notes for each of the lessons are available in the [Wiki][wiki]
while the [examples][examples] are available in this GitHub repository.

## 💡 About Python

Contrary to what you might believe, Python is not a _special language_ that is
only used by certain groups. Python is a general-purpose language that is used
for many things, including:

1. Web applications
1. Desktop and mobile applications
1. Data analysis and machine learning applications
1. Games
1. Command line applications
1. Scripting

Do not be frightned by the name Python 🐍, because its name is actually an
homage to the cult comedy show [Monty Python][why-python].

## 🙏 The Zen Of Python

The core philosophies are summarized in [The Zen Of Python][zen] and are
available in catchy [musical form][music]. These include:

1. Beautiful is better than ugly
1. Explicit is better than implicit
1. Simple is better than complex
1. Complex is better than complicated
1. Flat is better than nested
1. Sparse is better than dense
1. Readability counts
1. In the face of ambiguity, refuse the temptation to guess
1. If the implementation is hard to explain, it's a bad idea
1. If the implementation is easy to explain, it may be a good idea

## 🚀 Installation

Python works in all major operating systems. Every Python program will work as
expected, regardless of the operating system you are using.

### 💻 Windows

The easiest way to install Python on Windows is to visit the
[official page][official-page] and download the latest installer.

### 🍏 macOS

The macOS operating system comes with Python pre-installed. However, you can and
should install the latest version. The recommended way to do this is to use
[homebrew][homebrew].

Open a **Terminal** window and run the following command to install Homebrew:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once that's done, run the following command to install Python 3:

```sh
brew install python
```

### 🐧 Linux

Some Linux distributions come with Python pre-installed. You should be able to
check if this is the case by running the following command in a **Terminal**:

```sh
python3 --version
```

If that doesn't output a version number, you should install Python 3. The way
to do this depends on the distribution you are using. For example, on Ubuntu,
and other Debian-based distributions, you can install Python 3 by running:

```sh
sudo apt-get update && sudo apt-get install python3
```

## 📜 Resources

### 📚 Official

- The [official tutorial][official-tutorial] is a quick hands-on starter guide
- The [PEP-8 Style Guide][style-guide] will make your code more understandable
  to other programmers, including the most crucial of all: your future self

### 🕒 Speedrun

- Learn Python in [10 minutes][10-minutes]
- If that's still too much, learn Python in [5 minutes][5-minutes]

### 👀 Other

- [Blocky][blocky] is a way to program via a visual programming language and you
  can see the respective code behind it in various languages, including Python

<!-- References -->

[10-minutes]: https://www.stavros.io/tutorials/python/
[5-minutes]: https://www.youtube.com/watch?v=I2wURDqiXdM
[blocky]: https://developers.google.com/blockly
[examples]: ./examples
[homebrew]: https://brew.sh/
[music]: https://www.youtube.com/watch?v=i6G6dmVJy74
[official-page]: https://www.python.org/
[official-tutorial]: https://docs.python.org/3/tutorial/
[style-guide]: https://www.python.org/dev/peps/pep-0008/
[why-python]: https://docs.python.org/3/faq/general.html#why-is-it-called-python
[wiki]: ./wiki
[zen]: https://en.wikipedia.org/wiki/Zen_of_Python
