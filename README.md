# Catalog Web App

##Purpose of the Catalog project

The Catalog Web App is a app which was created as part of the Fullstack Web Developer Nano Degree program from Udacity.The project was to create an application using `Python` and `PSQL` that could effectively allow a user to login using third party `Aoth2` client login and perform `CRUD` operations using the `Flask` framework and `SQLAlchemy` database.

#Installation

To run the project successfully it is going to require that you download and install some software.

1. `Chrome` 
2. `Python 2.7`
3. `Git`
4. `Virtual Box`
5. `Vagrant`

#Installing Chrome

##Installing Chrome on a Windows based machine

To install Chrome for your user account:

1.Download the installer file, using he following address: `https://www.google.com/chrome/browser/desktop/index.html`.

2.If prompted, click Run or Save.

3.If you chose Save, double-click the installer file to start the installation process.
       *Will automatically import your homepage settings and browser history for you.

4.Start Chrome:
       
       *Windows 7: A Chrome window opens once everything is set up.
       
       *Windows 8 and 8.1: A welcome dialog appears, click Next to select your default browser.
       
       *Windows 10: A Chrome window opens once everything is set up. You can then make Chrome your default browser.

##Instaling Chrome on Mac machine

1.Download the disk image.

2.Open the file called "Google Chrome.dmg."

3.In the window that opens, find the Chrome icon Chrome app. Drag it to the Applications folder. If you don't have              administrative rights, you'll be asked to authenticate. If you're not able to authenticate, drag the icon to a               location on your computer where you do have rights, such as your desktop.

4.Open Chrome. Will automatically import your homepage settings and browser history for you.

5.Open Finder.

6.In the window's sidebar, to the right of Google Chrome, click Eject .

#Installing Chrome on a Linux machine

Use the same software that installs programs on your computer to install Chrome. Make sure you have administrative access first.

1.Download the installer file.

2.Click OK to open the package.

3.Click Install Package.

4.Google Chrome will add its program information to your software manager so that it can be kept up-to-date.

##Installing Python

In your browser, browse to [python/downoads](https://www.python.org/downloads/) >hover your mouse over *Downloads* > A dropdown list will appear with various operating systems.

##Installing Python on Windows

1. From this list select either Windows X86 or Windows X86-64.
2. Once downloaded locate the file in your download file,(or prefered location) double clicking the file and pressing Run when the dialog box pops up.
3. Next select the Install for all usersoption if you are allowing all user's who access your computer, access to the python program then leave this option selected. If you have multiple users and wish to not install python accross all accounts then select the Install just for me option then press Next.
4. Feel free to change the location path however, it is best to leave it as is and simply select 'Next'.
5. Scroll down in the window and find the 'Add Python.exe to Path' and click on the small red 'X' Choose the 'Will be installed on local hard drive' option then press 'Next'.
6. You will notice that the installation will bring up a command prompt window while Python downloads and installs 'Pip'.
7. 'Pip' is just a package management tool. This will allow you to install all the additional Python packages that are available for download through PyPI (Python Package Index).
8. Once the install is complete press 'Finish'.

##Installing Python on a Mac Machine

1. From the download list at python.org select Mac OSX 64.32 bit installer.
2. A pop up screen will appear for you to select the installers file location, once you have selected the location press the save button.
3. Once the installer package has been downloaded click on the completed download.
4. The installer will prompt you to press Continue, until you reach the license agreement.At this point press agree to continue with the install.
5. The install package will then ask you to install a standard instillation, if you are happy with this then click install
Once the install is complete the installer will exit.

##Installing Git

1. In your browser, browse to [git](https://git-scm.com/downloads) and select the download for your operating system.
2. Your download should start automaticaly.
3. A pop up screen will appear for you to select the installers file location, once you have selected the location press the save button.
3. Once the installer package has been downloaded click on the completed download.
4. The installer will prompt you to press Continue, until you reach the license agreement.At this point press agree to continue with the install.
5. The install package will then ask you to install a standard instillation, if you are happy with this then click install
Once the install is complete the installer will exit.

##Installing Virtual Box

1. In your browser, browse to [virtual box](https://www.virtualbox.org/wiki/Downloads) and select the download for your operating system.
2. Your download should start automaticaly.
3. A pop up screen will appear for you to select the installers file location, once you have selected the location press the save button.
3. Once the installer package has been downloaded click on the completed download.
4. The installer will prompt you to press Continue, until you reach the license agreement.At this point press agree to continue with the install.
5. The install package will then ask you to install a standard instillation, if you are happy with this then click install
Once the install is complete the installer will exit.

##Installing vagrant

1. In your browser browse over to [vagrant] (https://www.vagrantup.com/downloads.html)
2. Your download should start automaticaly.
3. A pop up screen will appear for you to select the installers file location, once you have selected the location press the save button.
3. Once the installer package has been downloaded click on the completed download.
4. The installer will prompt you to press Continue, until you reach the license agreement.At this point press agree to continue with the install.
5. The install package will then ask you to install a standard instillation, if you are happy with this then click install
Once the install is complete the installer will exit.

##Final steps for instillation

1. Download the `vm_touranment_master` file which contains the 'catalog' file you require to run this app.
2. Open terminal:
  * Windows: Use the Git Bash program (installed with Git) to get a Unix-style terminal.
  * Other systems: Use your favorite terminal program.

##Running the vagrant box
1. Change to the desired parent directory:
  * Example: `cd Desktop`.
  * and then `/vm_touranment_master/vagrant`.
2. Run vagrant by entering: `vagrant up`.
3. Log into Vagrant VM by entering: `vagrant ssh`.
4. Move to *catalog* directory by entering: `cd /vagrant/catalog/`
5. To install the database in the terminal window tyoe the following command: `python database_setup.py`
6. Type `python lotsofstock.py` to preload the database with some stock for the `music_shop app`.
7.To enable the app enter `python finalproject.py` inot the terminal window, you should see the following in the terminal window.
```
  * Running on http://0.0.0.0:8000/
  * Restarting with reloader
  ```
##Now open a browser window and enter `http://localhost:8000`

##About the `Music Shop App`

The music shop app is designed to allow user's to not only view various `Music Shop's` and there stock of verious instruments, but once a user has logged in they will be able able to `add`, `edit` and `delete` stock of the various `Music Shop's` which *they* have created. Further more a logged in user will also be able to `create`, `edit` or `delete` a `Music Shop` which they have created.

#To Add a `Shop` or `Stock`

1. In the top right hand corner of the screen click on the `log in button`.

2. You will be redirected to the log in page which you can either use your `Google+` account to login with or your `Facebook` account to log in with.

3. Once you have succesfully logged in you will be redirected to the main page with a *list* of `Music Shop's`.

4. Now that you have logged in a `Add Music Shop` button will appear at the top of the page, if you wish to add a `Music Shop` to the list please do so.

5. You can *only* `add`, `edit` or `delete` `instruments` to the `Music Shop's` which you have created.

6. Once you are finished adding `Music Shop's` and `Instruments` please don't forget to click on `log out` in the top right hand corner.

#Stop the server

1. In your `terminal window` press `ctrl c` and the sever will stop running.

##To exit `vagrant`

1. Enter vagrant halt in the terminal window, or in the `virtual box` gui double click on the `virtual machine` and a terminal style window will open.
2. Click on the `exit` (cross) button in the top left(for Mac osx) or top right (windows based) to exit the program.
3. Another window will appear with three options, select `power off the machine` and press `OK` and this will shut down the `virtual machine`.

Thank you for taking the time to read this `Read Me`. `Chrome` install readme, is the work of `Google` and is copied in part from the chrome download website. `Python` install readme, is work of Python and is copied in part from the python dowload website.
