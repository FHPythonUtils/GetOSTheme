<a name=".getostheme"></a>
## getostheme

Use this module to get the OS theme (dark/light)

<a name=".getostheme.isLightMode_Mac"></a>
#### isLightMode\_Mac

```python
isLightMode_Mac()
```

For MacOS BSD-3-Clause albertosottile
(https://github.com/albertosottile/darkdetect)

**Returns**:

- `bool` - Windows is in light mode

<a name=".getostheme.isLightMode_Windows"></a>
#### isLightMode\_Windows

```python
isLightMode_Windows()
```

For Windows OS MIT clxmente
(https://github.com/clxmente/Windows-Dark-Mode-Check)

**Returns**:

- `bool` - Windows is in light mode

<a name=".getostheme.isLightMode_Linux"></a>
#### isLightMode\_Linux

```python
isLightMode_Linux()
```

For Linux OS MIT FredHappyface

**Returns**:

- `bool` - Linux is in light mode

<a name=".getostheme.isLightMode"></a>
#### isLightMode

```python
isLightMode()
```

Call isLightMode_OS

**Returns**:

- `bool` - OS is in light mode

<a name=".getostheme.isDarkMode"></a>
#### isDarkMode

```python
isDarkMode()
```

**Returns**:

- `bool` - OS is in dark mode

<a name=".getostheme.cli"></a>
#### cli

```python
cli()
```

CLI entry point

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

