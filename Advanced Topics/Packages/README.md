# Packages and Package Management

## Simple in name, can get quite complex

I have very little experience with creating packages. I haven't created a real package before, except perhaps with my [undergrad final year project](https://github.com/willspencer171/statistical-thermodynamics), which was never released as a package (perhaps I should recreate this using Python and release it if I like it?)

Anyway, package management is simple in principle - we have a manager that will download a Python package distribution and it will store it in the environment ready to use in a Python program. But how does this work?

## Packages

### Structure

A package is exactly what it says on the tin - it's a collection of files, which have a common use, that can be distributed. The collection of files does have a specific structure to make it a proper package:

```text
realpython-reader/
│
├── src/
│   └── reader/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.toml
│       ├── feed.py
│       └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── LICENSE
├── MANIFEST.in
├── README.md
└── pyproject.toml
```

The package in this case is called `realpython-reader`, containing the source code module `reader`, test files and other files that are used in distribution.

#### \_\_init\_\_.py

This is known as the root of the package. It's usually kept quite simple, but all variables declared here are accessible throughout the package, and do not need to be imported. So this is a good place to put constants:

```python
# __init__.py

from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Version of the realpython-reader package
__version__ = "1.0.0"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("reader", "config.toml"))
URL = _cfg["feed"]["url"]
```

#### \_\_main\__.py

This is the driver code. A package must have a \_\_main\_\_.py file and this is what gets run when the package is called in command line. In order to use it, however, you must include:

```python
if __name__ == "__main__":
    main()
```

or just wrap the whole module in `if __name__ == "__main__":` but that's disgusting so don't do that.

#### config.toml

A TOML (Tom's Obvious Minimal Language) file is a format of configuration file containing key=value pairs separated into sections and tables:

```toml
# config.toml

[feed]
url = "https://realpython.com/atom.xml"
```

A good place to keep default values that can be read in at the start of a call, but can be modified and saved by the user.

### How does one make a package?

A package needs a name. The package name needs to be unique within whatever Package Index you are using. However, the name used to access the package does not need to be unique to the Index, but does need to be unique to the environment. Say we have two packages of similar function: my_first_package and my_second_package. These are unique names. Within the package itself, the name might not be the same as the uploaded package name, meaning that both the packages above could be named `package`.

If both packages are installed in the same environment, and are accessed using the same name, this results in ambiguity. This is resolved simply by using whichever package is found first when the name is used, leading to redundancy of the second package.

### pyproject.toml

pyproject.toml is a TOML file used to specify the build system for your project. You can choose whichever [build system](https://wiki.python.org/moin/ConfigurationAndBuildTools) you like, but a good starting point is Python's `setuptools`. Specifying this build system in the pyproject.toml looks like this:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Then, a lot more information about the package can go into the pyproject.toml file. This should include the package PyPI name, author, (optional) dependencies, package version, python version, etc. It's not a short list.

Other things to note include:

- classifiers
  - Terms used to make the project more easily searchable on a package index
- dependencies
- project.urls
  - Add links to your PyPI page (things like documentation and idk maybe a LinkedIn plug)
- project.scripts
  - command line scripts that can be run. Uses the format `script = "package.module:method"`

### BumpVer

BumpVer is a tool that integrates into your package's pyproject.toml that essentially tracks and maintains changes in the version number of your project. It also integrates with version control systems like Git, such that it won't update version numbers until changes are committed. By default, it uses the version number format MAJOR.MINOR.PATCH but this can be changed in the tool.bumpver section in the TOML.

BumpVer works in the command line so in order to bump the version number you can do the following:

```shell
bumpver update --minor
# INFO    - Old Version: 1.0.0
# INFO    - New Version: 1.1.0
```

### Development of a package

Now, you've got the basics of a package down, but obviously, as a developer, you're still developing it! So you need to be able to install your package (just as anyone else would), whilst also being able to work on it without reinstalling it every time. There is a perfect workflow for this: editable installs

In the command line, you can install your package using `pip install -e .` (more about pip in a bit) which will install your package locally, so you can use it, but also be able to edit it. Amazing!

## pip

pip (pip Installs Packages) is the default package manager that comes with Python when you install it (since 3.4 and 2.7.9). It is essentially a module that works mostly on the command line, and can be used to install, update and uninstall packages within the current Python environment. It will also manage these packages such that they can be manipulated individually, as well as having functionality for producing requirements files

### But how?

The terminal can be used as an interface for working with pip. The path environment variable comes in handy when explaining this - command prompt (cmd), Powershell and Terminal all use this. It stores, essentially, a list of directories in which to search for commands. If python is on the environment path variable, you can use `python` or `python3` as a command in cmd. The same goes for pip. If the module folder for pip is in the path variable, you can use `pip` on the command line. If not, you can always access the pip module via `python -m pip`

Great. That was simple. Not done yet though!

pip comes with commands itself to install, change, and uninstall a package. The most prominent ones are `install` and `uninstall`

### Installing with pip

The `pip install` command can be followed by a package name and other flags in order to install a package. But where does this package come from? More on that to come. In the meantime, flags and switches for `install` can be used to modify an installation of a package. This could be used to update (`--upgrade` or `-U` options) a package. You can also use the `-r [file]` flag to install a list of requirements from a requirements file.

The packages themselves, by default, are accessed from PyPI (everyone says _pie pee eye_ but I like _pie pie_) - the standard Python Package Index. It has over 300,000 packages on it so it is clear to see why it is relatively ubiquitous.

You can, however use a different package index to retrieve your packages. For example, if your company has its own packages that it doesn't want to be publicly available, it can host them on its intranet or another internet-available index. There is a [specific structure](https://peps.python.org/pep-0503/) that a package index needs to be recognised by pip. To specify the package index, you can use the following command:

`pip install -i [Index URL] [package name]`

The `-i` flag is used to specify the index. You can also install a package directly from a GitHub repository using:

`python -m pip install git+https://github.com/path/to/repo`

As well as installing in editable mode:

`python -m pip install -e [package name]`

which allows you to modify a package in your project environment, and storing a link to the package in the site-packages folder so that it can still be accessed globally.

### Requirements.txt

A text file. Nice and simple. It specifies which packages are installed in your project's environment, and their version numbers. They are formatted as follows:

```text
numpy>=x.y.z
pytest>=x.y.z
requests=x.y.z
```

Where the operator can be one of the following (not exhaustive):

- == (equal)
- \>= (greater than or equal)
- , (and)
- | (or)
- < (less than)

If you have a project with a lot of dependencies, the last thing you want to do is type this out manually. So what you can do it use pip to `freeze` the requirements to a text file:

`pip freeze > requirements.txt`

### Uninstalling with pip

This sounds very simple. You just do `pip uninstall`, right? Yes, but that could lead to problems since you will likely be leaving the dependent packages behind. Sure, you might well want them and not need them later, but in order to completely disassemble the dependency tree of a package, you'll need to see the dependencies of the package:

`pip show [package]` will do this for you. Now, you can assess the dependencies of your package and uninstall all of them in one fell swoop by just tacking more packages onto the end of your `pip uninstall` command.

You can also uninstall by using a requirements file with the `-r` flag again. Also, keep in mind that pip will ask permission to uninstall each package as it gets to it, so include the `-y` flag to automatically say yes to uninstalling

## Conda

Conda is a dependency, environment and package management system (the whole package :')) that has an awful lot of use. As part of the Anaconda package, Conda is geared towards data analysis and science, and has its own package index. The best bit about it is that it is an environment manager. This means that you don't have to keep track of whatever environments you've created in the past, and you don't have to use the command prompt as your only interface with virtual environments. Presto!

### Why Anaconda?

It has an intuitive application interface that allows you to see what apps you can create conda environments for (similar to a python environment, but has a specific set of pre-loaded modules for data science, analysis and machine learning). The interface makes creating and managing environments easier, and you can activate and disable packages that are used by the environments without having to explicitly uninstall them.

These are all advantages of the Anaconda interface, but the Conda package manager shares a lot of similarities with pip. However, Conda is not just for Python - it has coverage for R, as well as other languages like Go, Ruby and C++, and has access to PyPI so it doesn't lose the functionality that pip would have.

## Uploading Packages to Package Indexes

Now that you have your own packages and you know how to install packages from different sources, you'll want to know how you can distribute them.

### PyPI

In order to upload to PyPI you need a few things: an account on [PyPI](https://pypi.org/account/register/) (also [TestPyPI](https://test.pypi.org/account/register/) is a good idea), and the Build and Twine packages.

#### Build your Project

Source code isn't uploaded to PyPI, but the package is instead uploaded as a source archive and a wheel (named after cheese wheels, the important thing in the cheese shop). You'll need the Build package to create these for you: `python -m build`

And this creates the wheel and tar.gz files in a dist folder in the package root folder:

```text
my_package/
│
└── dist/
    ├── my_package-1.0.0-py3-none-any.whl
    └── my_package-1.0.0.tar.gz
```

A wheel, as I'm just learning, is a ZIP file with a different name. This means that once the wheel is made, you can check the contents of it by copying it to a zip file, and expanding it:

```text
(venv) PS> cd .\dist
(venv) PS> Copy-Item .\realpython_reader-1.0.0-py3-none-any.whl reader-whl.zip
(venv) PS> Expand-Archive reader-whl.zip
(venv) PS> tree .\reader-whl\ /F
C:\REALPYTHON-READER\DIST\READER-WHL
├───reader
│       config.toml
│       feed.py
│       viewer.py
│       __init__.py
│       __main__.py
│
└───realpython_reader-1.0.0.dist-info
        entry_points.txt
        LICENSE
        METADATA
        RECORD
        top_level.txt
        WHEEL
```

#### Uploading with Twine

Twine is a package used to wrap your cheese wheels in a brown paper package with twine :)

You can use it to check that the source archive and wheel are acceptable:

```shell
twine check dist/*
# Checking distribution dist/my_package-1.0.0-py3-none-any.whl: Passed
# Checking distribution dist/my_package-1.0.0.tar.gz: Passed
```

Then you can upload it!

`twine upload -r testpypi dist/*`

It's not a good idea to upload test things to PyPI as you'll likely be taking up valuable namespaces other people need :/

## Final Words

And this kind of concludes my reading into packages for now. Thank you for reading this far, I know it was a lot of text again and not many fun things, like the whale one I did the other day, but it's all good knowledge!

I hope you have an awesome day and as always, feel free to reach out to me on [Instagram](https://www.instagram.com/will_spencer171) or [LinkedIn](https://www.linkedin.com/in/willspencer171) if you have any comments about what I've written here, or if you have any other interesting topics you'd like to talk about :)
