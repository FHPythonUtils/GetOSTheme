"""Use this module to get the OS theme (dark/light)
"""
import platform
import importlib


def isLightMode_Mac():
	"""For MacOS BSD-3-Clause albertosottile
	(https://github.com/albertosottile/darkdetect)

	Returns:
		bool: Windows is in light mode
	"""
	import ctypes

	appkit = ctypes.cdll.LoadLibrary(ctypes.util.find_library('AppKit'))
	objc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('objc'))

	void_p = ctypes.c_void_p
	ull = ctypes.c_uint64

	objc.objc_getClass.restype = void_p
	objc.sel_registerName.restype = void_p
	objc.objc_msgSend.restype = void_p
	objc.objc_msgSend.argtypes = [void_p, void_p]

	msg = objc.objc_msgSend

	def _utf8(s):
		if not isinstance(s, bytes):
			s = s.encode('utf8')
		return s

	def n(name):
		return objc.sel_registerName(_utf8(name))

	def C(classname):
		return objc.objc_getClass(_utf8(classname))

	def theme():
		NSAutoreleasePool = objc.objc_getClass('NSAutoreleasePool')
		pool = msg(NSAutoreleasePool, n('alloc'))
		pool = msg(pool, n('init'))

		NSUserDefaults = C('NSUserDefaults')
		stdUserDef = msg(NSUserDefaults, n('standardUserDefaults'))

		NSString = C('NSString')

		key = msg(NSString, n("stringWithUTF8String:"), _utf8('AppleInterfaceStyle'))
		appearanceNS = msg(stdUserDef, n('stringForKey:'), void_p(key))
		appearanceC = msg(appearanceNS, n('UTF8String'))

		if appearanceC is not None:
			out = ctypes.string_at(appearanceC)
		else:
			out = None

		msg(pool, n('release'))

		if out is not None:
			return out.decode('utf-8')
		return 'Light'

	return theme() == 'Light'


def isLightMode_Windows():
	"""For Windows OS MIT clxmente
	(https://github.com/clxmente/Windows-Dark-Mode-Check)

	Returns:
		bool: Windows is in light mode
	"""
	from winreg import ConnectRegistry, OpenKey, QueryValueEx, HKEY_CURRENT_USER
	keyAt = 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'
	registryHive = ConnectRegistry(None, HKEY_CURRENT_USER)
	openedKey = OpenKey(registryHive, keyAt)
	return QueryValueEx(openedKey, "AppsUseLightTheme")[0] != 0


def isLightMode_Linux():
	"""For Linux OS MIT FredHappyface

	Returns:
		bool: Linux is in light mode
	"""
	if importlib.util.find_spec("PyQt5"): # Qt5
		from PyQt5.QtWidgets import QApplication
		from PyQt5.QtGui import QPalette
		bgcolor = QApplication([]).palette().color(QPalette.Background)
		return bgcolor.red() + bgcolor.green() + bgcolor.blue() > 255 / 2 * 3
	elif importlib.util.find_spec("gi") is not None: # Gtk3
		import gi
		gi.require_version('Gtk', '3.0')
		from gi.repository import Gtk
		bgcolor = Gtk.Window().get_style_context().get_background_color(Gtk.StateFlags.NORMAL)
		return bgcolor.red + bgcolor.green + bgcolor.blue > 0.5 * 3
	return True


def isLightMode():
	"""Call isLightMode_OS

	Returns:
		bool: OS is in light mode
	"""
	if platform.system() == "Darwin":
		return isLightMode_Mac()
	if platform.system() == "Windows":
		return isLightMode_Windows()
	if platform.system() == "Linux":
		return isLightMode_Linux()
	return True


def isDarkMode():
	"""
	Returns:
		bool: OS is in dark mode
	"""
	return not isLightMode()
