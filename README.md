WinScripts
==========

A repository for power shell and command prompts.

## SetLoginBackground.cmd ##

* Images must be less then 256KB, .jpg, and dimensions should match the screen resolution.
* Under HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI:
    * Ensure the registry key of OEMBackground has a value of 1 (create the key if necessary).
    * The registry key ButtonSet indicates if there should be any shadow on the login UI elements.
        * 0 — Light shadow
        * 1 — Dark shadow
        * 2 — No shadow
* Ensure the path C:\Windows\System32\oobe\info\Backgrounds exists. Create the necessary folders if they are missing.
