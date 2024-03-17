"""Use this module to get the OS theme (dark/light)."""

# pylint: disable=import-outside-toplevel
from __future__ import annotations

import importlib.util
import platform


def isLightMode_Mac() -> bool:  # pylint: disable=invalid-name
	"""For MacOS BSD-3-Clause albertosottile
	(https://github.com/albertosottile/darkdetect).

	Raises
	------
		OSError: Cannot load objc

	Returns
	-------
		bool: Windows is in light mode

	"""
	import ctypes
	import ctypes.util

	lib = ctypes.util.find_library("objc")
	if not lib:
		msg = "Cannot load objc"
		raise OSError(msg)
	objc = ctypes.cdll.LoadLibrary(lib)

	void_p = ctypes.c_void_p

	objc.objc_getClass.restype = void_p
	objc.sel_registerName.restype = void_p
	objc.objc_msgSend.restype = void_p
	objc.objc_msgSend.argtypes = [void_p, void_p]

	# Objective C msg send
	msgSend = objc.objc_msgSend

	def _encodeUTF8(string: str | bytes) -> bytes:
		"""Encode string as utf8 bytes.

		Args:
		----
			string (Union[str, bytes]): string to encode

		Returns:
		-------
			bytes: bytes

		"""
		if isinstance(string, str):
			string = string.encode("utf8")
		return string

	def objcName(name: str | bytes):
		return objc.sel_registerName(_encodeUTF8(name))

	def objcClass(classname: str | bytes):
		return objc.objc_getClass(_encodeUTF8(classname))

	def theme() -> str:
		"""Get the MAC OS theme string.

		Returns
		-------
			string: Theme string

		"""
		nsAutoreleasePool = objc.objc_getClass("NSAutoreleasePool")
		pool = msgSend(nsAutoreleasePool, objcName("alloc"))
		pool = msgSend(pool, objcName("init"))

		nsUserDefaults = objcClass("NSUserDefaults")
		stdUserDef = msgSend(nsUserDefaults, objcName("standardUserDefaults"))

		nsString = objcClass("NSString")

		key = msgSend(
			nsString, objcName("stringWithUTF8String:"), _encodeUTF8("AppleInterfaceStyle")
		)
		appearanceNS = msgSend(stdUserDef, objcName("stringForKey:"), void_p(key))
		appearanceC = msgSend(appearanceNS, objcName("UTF8String"))

		out = ctypes.string_at(appearanceC) if appearanceC is not None else None

		msgSend(pool, objcName("release"))

		if out is not None:
			return out.decode("utf-8")
		return "Light"

	return theme() == "Light"


def isLightMode_Windows() -> bool:  # pylint: disable=invalid-name
	"""For Windows OS MIT clxmente
	(https://github.com/clxmente/Windows-Dark-Mode-Check).

	Returns
	-------
		bool: Windows is in light mode

	"""
	from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx

	keyAt = "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize"
	registryHive = ConnectRegistry(None, HKEY_CURRENT_USER)
	openedKey = OpenKey(registryHive, keyAt)
	return QueryValueEx(openedKey, "AppsUseLightTheme")[0] != 0


def isLightMode_Linux() -> bool:  # pylint: disable=invalid-name
	"""For Linux OS MIT FredHappyface.

	Returns
	-------
		bool: Linux is in light mode

	"""
	if importlib.util.find_spec("PyQt5"):  # Qt5
		from PyQt5.QtGui import QPalette
		from PyQt5.QtWidgets import QApplication

		bgcolor = QApplication([]).palette().color(QPalette.Background)
		return bgcolor.red() + bgcolor.green() + bgcolor.blue() > 255 / 2 * 3
	if importlib.util.find_spec("gi") is not None:  # Gtk3
		import gi

		gi.require_version("Gtk", "3.0")
		from gi.repository import Gtk

		bgcolor = Gtk.Window().get_style_context().get_background_color(Gtk.StateFlags.NORMAL)
		return bgcolor.red + bgcolor.green + bgcolor.blue > 0.5 * 3
	return True


def isLightMode() -> bool:
	"""Call isLightMode_OS.

	Returns
	-------
		bool: OS is in light mode

	"""
	if platform.system() == "Darwin":
		return isLightMode_Mac()
	if platform.system() == "Windows":
		return isLightMode_Windows()
	if platform.system() == "Linux":
		return isLightMode_Linux()
	return True


def isDarkMode() -> bool:
	"""Is the OS in dark mode?.

	Returns
	-------
		bool: OS is in dark mode

	"""
	return not isLightMode()


def cli() -> None:
	"""CLI entry point."""
	print("OS is in " + ("Light" if isLightMode() else "Dark") + " Mode")
