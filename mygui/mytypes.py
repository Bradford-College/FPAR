
from ctypes import c_int, c_uint, WinDLL, Structure, pointer, byref
from ctypes import WINFUNCTYPE, sizeof, windll
from ctypes.wintypes import HANDLE, LPCWSTR, LPARAM, WPARAM, HWND, MSG

# globals
WS_EX_APPWINDOW = 0x40000
WS_OVERLAPPEDWINDOW = 0xcf0000
WS_CAPTION = 0xc00000
SW_SHOWNORMAL = 1
SW_SHOW = 5
CS_HREDRAW = 2
CS_VREDRAW = 1
CW_USEDEFAULT = 0x80000000
WM_DESTROY = 2
WHITE_BRUSH = 0

user32 = WinDLL('user32', use_last_error=True)
gdi32 = WinDLL('gdi32', use_last_error=True)
kernel32 = WinDLL('kernel32', use_last_error=True)

WNDPROCTYPE = WINFUNCTYPE(c_int, HWND, c_uint, WPARAM, LPARAM)
user32.DefWindowProcW.argtypes = [HWND, c_uint, WPARAM, LPARAM]
