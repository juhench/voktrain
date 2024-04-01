# voktrain - Vocabulary Trainer

Installation instructions for WSL, tested on Windows 10 with WSL + Ubuntu 20.04.

In start menu, enter wsl and press newline. A terminal window should appear like the one below.
![image](https://github.com/juhench/voktrain/assets/49944492/c99d21a8-c720-4423-a6b2-7da8fe0e5840)

Enter the following commands. You can use the copy & paste button below, then right-click on top of the WSL window to paste:
```bash
sudo apt update; sudo apt -y upgrade; sudo apt -y install git build-essential; git clone https://github.com/juhench/voktrain; cd voktrain; chmod +x *.sh; ./install_voktrain.sh
```
Press newline. It can take a while until the Ubuntu subsystem has been updated and the required software packages have been installed. This will install Python, all required packages, and the voktrain software. At the end, a message should appear that the voktrain software was installed. You can now close the WSL window.

