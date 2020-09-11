Microsoft Windows [Version 10.0.15063]
(c) 2017 Microsoft Corporation. Alle rechten voorbehouden.

C:\Users\sam00\PythonAchievements>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   helloWorld.py


C:\Users\sam00\PythonAchievements>git commit -m helloWorld.py

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'sam00@LAPTOP-0RB8V9J4.(none)')

C:\Users\sam00\PythonAchievements>git config --global user.email 27741@ma-web.nl

C:\Users\sam00\PythonAchievements>git config --global user.name Sam

C:\Users\sam00\PythonAchievements>Omit --global
'Omit' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\sam00\PythonAchievements>commit -m helloWorld.py
'commit' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\sam00\PythonAchievements>git commit -m helloWorld.py
[master (root-commit) 04681e6] helloWorld.py
 1 file changed, 1 insertion(+)
 create mode 100644 helloWorld.py

C:\Users\sam00\PythonAchievements>git status
On branch master
nothing to commit, working tree clean

C:\Users\sam00\PythonAchievements>git log
commit 04681e686e562cce976818932e70f0f344bd46a2 (HEAD -> master)
Author: Sam <27741@ma-web.nl>
Date:   Wed Sep 9 13:03:33 2020 +0200

    helloWorld.py

C:\Users\sam00\PythonAchievements>