# getostheme

> Auto-generated documentation for [getostheme](../../getostheme/__init__.py) module.

Use this module to get the OS theme (dark/light)

- [Getostheme](../README.md#getostheme-index) / [Modules](../README.md#getostheme-modules) / getostheme
    - [cli](#cli)
    - [isDarkMode](#isdarkmode)
    - [isLightMode](#islightmode)
    - [isLightMode_Linux](#islightmode_linux)
    - [isLightMode_Mac](#islightmode_mac)
    - [isLightMode_Windows](#islightmode_windows)
    - Modules
        - [\_\_main\_\_](module.md#__main__)

## cli

[[find in source code]](../../getostheme/__init__.py#L153)

```python
def cli():
```

CLI entry point

## isDarkMode

[[find in source code]](../../getostheme/__init__.py#L145)

```python
def isDarkMode() -> bool:
```

#### Returns

- `bool` - OS is in dark mode

## isLightMode

[[find in source code]](../../getostheme/__init__.py#L130)

```python
def isLightMode() -> bool:
```

Call isLightMode_OS

#### Returns

- `bool` - OS is in light mode

## isLightMode_Linux

[[find in source code]](../../getostheme/__init__.py#L107)

```python
def isLightMode_Linux() -> bool:
```

For Linux OS MIT FredHappyface

#### Returns

- `bool` - Linux is in light mode

## isLightMode_Mac

[[find in source code]](../../getostheme/__init__.py#L10)

```python
def isLightMode_Mac() -> bool:
```

For MacOS BSD-3-Clause albertosottile
(https://github.com/albertosottile/darkdetect)

#### Raises

- `OSError` - Cannot load objc

#### Returns

- `bool` - Windows is in light mode

## isLightMode_Windows

[[find in source code]](../../getostheme/__init__.py#L92)

```python
def isLightMode_Windows() -> bool:
```

For Windows OS MIT clxmente
(https://github.com/clxmente/Windows-Dark-Mode-Check)

#### Returns

- `bool` - Windows is in light mode
