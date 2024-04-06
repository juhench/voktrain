# voktrain - Vocabulary Trainer

Installation instructions for WSL, tested on Windows 10 with WSL + Ubuntu 20.04.

In start menu, enter wsl and press newline. A terminal window should appear like the one below.
![image](https://github.com/juhench/voktrain/assets/49944492/c99d21a8-c720-4423-a6b2-7da8fe0e5840)

Enter the following commands. You can use the copy & paste button below, then right-click on top of the WSL window to paste:
```bash
sudo apt update; sudo apt -y upgrade; sudo apt -y install git build-essential; git clone https://github.com/juhench/voktrain; cd voktrain; chmod +x *.sh; ./install_voktrain.sh
```
Press newline. It can take a while until the Ubuntu subsystem has been updated and the required software packages have been installed. This will install Python, all required packages, and the voktrain software. At the end, a message should appear that the voktrain software was installed. You can now close the WSL window.

You can start the voktrain software from the Linux command line in the following way. In the Windows start menu, enter wsl to open a WSL terminal window. The enter the following command by copy&paste:
```bash
~/voktrain/starte_Vokabeltrainer_shell_wsl.sh
```

In order to run the voktrain software with a mouse click, the easiest way is to add a shortcut to the desktop. Here is a shortcut as an example. (https://github.com/juhench/voktrain/blob/b3fa370ee76fa89c0920e5cf785c3b1a8e648e5a/Vokabeltrainer.zip)
Unpack the link, e.g., to the desktop. This should start the vocabulary trainer.

If the zipped shortcut file does not work, you can create your own shortcut.
Create a shortcut by a right-click on the desktop, then choose to create a new shortcut.
![image](https://github.com/juhench/voktrain/assets/49944492/ae0b7aa0-70db-4b90-8bf8-667a68ea8967)
A window should open, asking for the name of the new shortcut. Call it "wsl". Then press "weiter" or "next". A penguin icon should appear on the desktop. Right-click on the penguin, then select "Eigenschaften"/"Properties". It should look like this:
![image](https://github.com/juhench/voktrain/assets/49944492/ccc6a473-560c-4d74-b6fb-d3f0a9e209c4)
Unter "Ziel"/"Target", enter the launch command:
```bash
C:\Windows\System32\wsl.exe -e bash -lic "while true; do ~/voktrain/starte_Vokabeltrainer_shell_wsl.sh; done"
```
Confirm the change and then double-click the icon. The shortcut can now also be renamed from WSL to, e.g., Vokabeltrainer.

Vocabulary files can be created with google sheets.
Here is an example:
[https://docs.google.com/spreadsheets/d/14ymLVXnWKFUXAAgZ2oPCVh3M44IuE-K1/edit]

You can create a copy of this document to your own google drive and edit it. Then, you need to share it 'publicly'; i.e., anyone with the link can view. This will allow the voktrain program to read the file. Now that your own document will have a new unique code after the /d/ and before the /edit/. The code of the current document is `14ymLVXnWKFUXAAgZ2oPCVh3M44IuE-K1`. In order to use your own vocabulary file, copy the new code. You will then need to edit the python program. To locate the python program, open Explorer and navigate to My Computer. Then, enter "linux" and press enter. Ubuntu 20.04 should appear.
![image](https://github.com/juhench/voktrain/assets/49944492/6b87588a-3882-4d1c-aaa3-9eb7abc7a2b3)
Navigate to >home>YOURUSERNAME>voktrain and open the file called "Vokabeltrainer..."
![image](https://github.com/juhench/voktrain/assets/49944492/590d7ee2-b04a-48a3-82e1-85633d33ed30)
You can use the Windows Editor program to edit the file. Locate the code that says:
```python
Schluesselliste=[['Englisch','14ymLVXnWKFUXAAgZ2oPCVh3M44IuE-K1',''],
                 ['Latein','12dzw07OguBhtL_gqTHWlQ5sn5SS9LubN',''],
                ]
```
Exchange the language and the code here. Make sure not to delete any brackets, quotation marks, etc. Save the file. Restart the vocabulary trainer.

In order to delete old error file that collect the misspelled vocabulary, you can navigate to here:
![image](https://github.com/juhench/voktrain/assets/49944492/9f48b0c1-e056-4fa8-8116-758adc8cffbb)

You can also create vocabulary files with Excel or LibreOffice in XLSX format as an alternative to google drive.


