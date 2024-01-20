# Getostheme

[Getostheme Index](../README.md#getostheme-index) / Getostheme

> Auto-generated documentation for [getostheme](../../../getostheme/__init__.py) module.

- [Getostheme](#getostheme)
  - [cli](#cli)
  - [isDarkMode](#isdarkmode)
  - [isLightMode](#islightmode)
  - [isLightMode_Linux](#islightmode_linux)
  - [isLightMode_Mac](#islightmode_mac)
  - [isLightMode_Windows](#islightmode_windows)
  - [Modules](#modules)

## cli

[Show source in __init__.py:161](../../../getostheme/__init__.py#L161)

CLI entry point.

#### Signature

```python
def cli() -> None: ...
```



## isDarkMode

[Show source in __init__.py:151](../../../getostheme/__init__.py#L151)

Is the OS in dark mode?.

Returns
-------
 bool: OS is in dark mode

#### Signature

```python
def isDarkMode() -> bool: ...
```



## isLightMode

[Show source in __init__.py:135](../../../getostheme/__init__.py#L135)

Call isLightMode_OS.

Returns
-------
 bool: OS is in light mode

#### Signature

```python
def isLightMode() -> bool: ...
```



## isLightMode_Linux

[Show source in __init__.py:111](../../../getostheme/__init__.py#L111)

For Linux OS MIT FredHappyface.

Returns
-------
 bool: Linux is in light mode

#### Signature

```python
def isLightMode_Linux() -> bool: ...
```



## isLightMode_Mac

[Show source in __init__.py:10](../../../getostheme/__init__.py#L10)

For MacOS BSD-3-Clause albertosottile
(https://github.com/albertosottile/darkdetect).

Raises
------
 OSError: Cannot load objc

Returns
-------
 bool: Windows is in light mode

#### Signature

```python
def isLightMode_Mac() -> bool: ...
```



## isLightMode_Windows

[Show source in __init__.py:95](../../../getostheme/__init__.py#L95)

For Windows OS MIT clxmente
(https://github.com/clxmente/Windows-Dark-Mode-Check).

Returns
-------
 bool: Windows is in light mode

#### Signature

```python
def isLightMode_Windows() -> bool: ...
```



## Modules

- [Module](./module.md)