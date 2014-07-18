Login Background Changer
==========

Windows 7 supports the ability to load images into the background of the login screen without the use of third-party software or manual "hacks". This functionality was designed with OEMs in mind, but is pretty easy to turn on and off using regedit.

### Registry Changes ###
* Run Registry Editor (regedit.exe)
* Under *HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/Authentication/LogonUI/Background*, ensure the registry key of *OEMBackground* has a value of 1 (create the key if necessary) where 1 is for enabling, 0 for disabling
* Under *HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/Authentication/LogonUI*, the registry key *ButtonSet* indicates if there should be any shadow on the login UI elements
    * 0 — Light shadow
    * 1 — Dark shadow
    * 2 — No shadow

### Guidelines/Limitations ###
* Images must be less then 256KB, .jpg, and dimensions should match the screen resolution
* Ensure the path *%WINDIR%\System32\oobe\info\Backgrounds* exists. Create the necessary folders in this path if they are missing
* The *backgroundDefault.jpg* image in the above path is loaded and stretched to fit the screen resolution

### Automating Background Rotation ###

The script *SetLoginBackground.cmd* allows for copying a random image from a folder of jpg images into the special Windows backgrounds folder.

To make the most of the script, schedule the script to run in Task Scheduler. For example, when a user logs in, the background can be updated in preparation for the next login.

A sample Task Scheduler definition is *SampleTaskSchedulerDefinition.xml* which is invoked on login and (session) unlock. Just modify the user from *laptop\Robert* to *<computer_name>\<user_name>* and the executed command to be the local path to *SetLoginBackground.cmd*.
