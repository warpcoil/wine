# $Id: kernel.spec,v 1.3 1993/07/04 04:04:21 root Exp root $
#
name	kernel
id	1
length	415

3   return GetVersion 0 0x301
4   pascal LocalInit(word word word) LocalInit(1 2 3)
5   pascal LocalAlloc(word word) LocalAlloc(1 2)
6   pascal LocalReAlloc(word word word) LocalReAlloc(1 2 3)
7   pascal LocalFree(word) LocalFree(1)
8   pascal LocalLock(word) LocalLock(1)
9   pascal LocalUnlock(word) LocalUnlock(1)
10  pascal LocalSize(word) LocalSize(1)
11  pascal LocalHandle(word) ReturnArg(1)
12  pascal LocalFlags(word) LocalFlags(1)
13  pascal LocalCompact(word) LocalCompact(1)
14  return LocalNotify 4 0
15  pascal GlobalAlloc(word long) GlobalAlloc(1 2)
16  pascal GlobalReAlloc(word long word) GlobalReAlloc(1 2 3)
17  pascal GlobalFree(word) GlobalFree(1)
18  pascal GlobalLock(word) GlobalLock(1)
19  pascal GlobalUnlock(word) GlobalUnlock(1)
20  pascal GlobalSize(word) GlobalSize(1)
21  pascal GlobalHandle(word) GlobalHandle(1)
22  pascal GlobalFlags(word) GlobalFlags(1)
23  pascal LockSegment(s_word) KERNEL_LockSegment(1)
24  pascal UnlockSegment(s_word) KERNEL_UnlockSegment(1)
25  pascal GlobalCompact(long) GlobalCompact(1)
30  pascal WaitEvent(word) KERNEL_WaitEvent(1)
49  pascal GetModuleFileName(word ptr s_word) KERNEL_GetModuleFileName(1 2 3)
50  pascal GetProcAddress(word ptr) GetProcAddress(1 2)
51  pascal MakeProcInstance(ptr word) CALLBACK_MakeProcInstance(1 2)
52  pascal FreeProcInstance(ptr) FreeProcInstance(1)
59  pascal WriteProfileString(ptr ptr ptr) WriteProfileString(1 2 3)
60  pascal FindResource(word ptr ptr) FindResource(1 2 3)
61  pascal LoadResource(word word) LoadResource(1 2)
62  pascal LockResource(word) LockResource(1)
63  pascal FreeResource(word) FreeResource(1)
74  pascal OpenFile(ptr ptr word) KERNEL_OpenFile(1 2 3)
81  pascal _lclose(word) KERNEL__lclose(1)
82  pascal _lread(word ptr word) KERNEL__lread(1 2 3)
85  pascal _lopen(ptr word) KERNEL__lopen(1 2)
86  pascal _lwrite(word ptr word) KERNEL__lwrite(1 2 3)
88  pascal lstrcpy(ptr ptr) lstrcpy(1 2)
89  pascal lstrcat(ptr ptr) lstrcat(1 2)
90  pascal lstrlen(ptr) lstrcpy(1)
91  register InitTask(word word word word word
		      word word word word word) 
	     KERNEL_InitTask()
102 register DOS3Call(word word word word word
		      word word word word word) 
	     KERNEL_DOS3Call()
111 pascal GlobalWire(word) GlobalLock(1)
112 pascal GlobalUnWire(word) GlobalUnlock(1)
115 pascal OutputDebugString(ptr) OutputDebugString(1)
121 return LocalShrink 4 0
127 pascal GetPrivateProfileInt(ptr ptr s_word ptr)
	   GetPrivateProfileInt(1 2 3 4)
128 pascal GetPrivateProfileString(ptr ptr ptr ptr s_word ptr)
	   GetPrivateProfileString(1 2 3 4 5 6)
129 pascal WritePrivateProfileString(ptr ptr ptr ptr)
	   WritePrivateProfileString(1 2 3 4)
131 pascal GetDOSEnvironment() GetDOSEnvironment()
132 return GetWinFlags 0 0x413
154 return GlobalNotify 4 0
163 pascal GlobalLRUOldest(word) ReturnArg(1)
164 pascal GlobalLRUNewest(word) ReturnArg(1)
178 equate __WINFLAGS 0x413
184 return GlobalDOSAlloc 4 0
185 return GlobalDOSFree 2 0
191 pascal GlobalPageLock(word) GlobalLock(1)
192 pascal GlobalPageUnlock(word) GlobalUnlock(1)
197 pascal GlobalFix(word) GlobalLock(1)
198 pascal GlobalUnfix(word) GlobalUnlock(1)
57  pascal GetProfileInt(ptr ptr word) GetProfileInt(1 2 3)
58  pascal GetProfileString(ptr ptr ptr ptr word) GetProfileString(1 2 3 4 5)
199 pascal SetHandleCount(word) SetHandleCount(1)
353 pascal lstrcpyn(ptr ptr word) lstrcpyn(1 2 3)
