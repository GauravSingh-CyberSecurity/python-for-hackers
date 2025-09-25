




Burp suite professional edition licence key Bypass:
---

https://github.com/Larrysonp1/Burp-Suite-Update
https://github.com/AnshumanSrivastavaGit/Burp-Suite
https://github.com/gt0day/Burp-Suite.git

![[Burp-Suite-main.zip]]
very imp note:-    move/keep the BurpLoaderKeygen.jar and burpsuite_pro_vxxxx.x.jar in the same folder  



Download link for Burp pro: 
https://portswigger.net/burp/pro

https://portswigger.net/burp/releases/professional-community-2024-1-1-6?requestededition=professional&requestedplatform=


```
sudo apt-get upgrade burpsuite 
```



---




Steps to install/update new JAVA version
---

NOTE: the version should be what you are using at the time of updating java

It seems like there might be an issue with the Java installation or configuration. Let's try the following steps to resolve it:

1. Remove the existing JDK 22 installation:

```bash
sudo apt-get purge jdk-22
```

2. Install the JDK 22 package again:

```bash
sudo dpkg -i ~/Downloads/jdk-22_linux-x64_bin.deb
```

3. Set the Java alternatives to the JDK 22 version:

```bash
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-22-oracle-x64/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-22-oracle-x64/bin/javac 1
sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/jdk-22-oracle-x64/bin/jar 1
```

4. Set the alternatives to the JDK 22 version:

```bash
sudo update-alternatives --set java /usr/lib/jvm/jdk-22-oracle-x64/bin/java
sudo update-alternatives --set javac /usr/lib/jvm/jdk-22-oracle-x64/bin/javac
sudo update-alternatives --set jar /usr/lib/jvm/jdk-22-oracle-x64/bin/jar
```

5. Check the Java version:

```bash
java -version
```

If you encounter any errors or issues during these steps, please let me know.



Desktop shortcut
---
To create a desktop shortcut for Burp Suite, you can follow these steps:

1. Create a desktop file for Burp Suite:
   ```bash
   nano ~/.local/share/applications/burp-suite.desktop
   ```

2. Add the following content to the file:
```

[Desktop Entry]
   Version=1.0
   Type=Application
   Name=Burp Suite
   Exec=/usr/lib/jvm/jdk-22-oracle-x64/bin/java -jar /home/kali/Burp/BurpLoaderKeygen.jar
   Icon=/home/kali/Burp/i4j_extf_6_1dgj151_jehl3v.png
   Terminal=false
   
```
   Replace `/path/to/BurpLoaderKeygen.jar` with the actual path to `BurpLoaderKeygen.jar` and `/path/to/burp-icon.png` with the path to the Burp Suite icon.

3. Make the desktop file executable:
   ```bash
   chmod +x ~/.local/share/applications/burp-suite.desktop
   ```

Now, you should see the Burp Suite icon on your desktop, and you can launch Burp Suite by double-clicking on it.


chatgpt propmpt i used to help me with doing all this installation of latest burpsuite.
https://chatgpt.com/share/f43cf464-8da8-4b99-b951-8ecc8c5071b2


BurpSuite Extensions
---
Logger++
Autorize



----

# For windows

Step 1: Create a folder named burp in c drive(or any drive):-  `c:\burp`

Download latest stable and supported JDK archive folder of windows os for burpsuite in the `\burp` folder :
```
https://www.oracle.com/in/java/technologies/downloads/#jdk21-windows
```

```
https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.zip
```

Extract the JDK zip in the `\burp` folder :
```
eg: c:\burp\jdk-21.0.8
```


Download the  : `BurpLoaderKeygen_h3110w0r1d.jar` in `\burp` folder .
```
[BurpLoaderKeygen_h3110w0r1d.jar](https://github.com/Larrysonp1/Burp-Suite-Update/blob/main/BurpLoaderKeygen_h3110w0r1d.jar "BurpLoaderKeygen_h3110w0r1d.jar")
```

Download the latest `burpsuitePro.jar` file in `\burp` folder.

---

Now  in `\burp` folder , right click>new>text document :

to create a `run.bat` file :
write below script in the file
```
@echo off
"C:\burp\jdk-XX.X.X\bin\java.exe" -jar "C:\burp\BurpLoaderKeygen_h3110w0r1d.jar"
pause
```

and save file > name it `run.bat` > filetype : 'all files' > save.

Now run the `run.bat` file,
the BurpLoaderKeygen_h3110w0r1d.jar will pop up a window,
hit run in the pop up window of BurpLoaderKeygen_h3110w0r1d.jar 

complete the key generation process via manual verification.

----

# for Linux

###### Burp Suite Professional Activation
```
[](https://github.com/Larrysonp1/Burp-Suite-Update/blob/main/README.md#burp-suite-professional-activation)

```
###### Requirement
```
[](https://github.com/Larrysonp1/Burp-Suite-Update/blob/main/README.md#requirement)
```
- Java

- Burp Suite Professional (JAR)
```
> Download From [Here](https://portswigger.net/burp/releases#professional "Burp Suite")

```



##### in Linux
```
[](https://github.com/Larrysonp1/Burp-Suite-Update/blob/main/README.md#linux)
```
- [1] - make a folder in /etc/opt/Burpsuite
    
    > sudo mkdir /etc/opt/Burpsuite
    
- [2] - move the BurpLoaderKeygen.jar and burpsuite_pro_vxxxx.x.jar in the same folder
    
    > sudo mv BurpLoaderKeygen.jar burpsuite_pro_v2023.7.jar /etc/opt/Burpsuite && cd /etc/opt/Burpsuite
    
- [3] - java -jar BurpLoaderKeygen.jar
- [4] - Copy the loader command we need to use for shortcut and press R...
- [5] - Copy license from burpsuite loader and paste in license key in burpsuite and press next
- [6] - Press manual activation and copy request then paste in activation request in burpsuite loeader
- [7] - Copy activation response from burpsuite loader and paste in burpsuite (paste response)
    
    > Finnaly make a shortcut from loader command in step 4.
    

> Happy Hacking :)
