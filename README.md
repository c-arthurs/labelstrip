![labels](./docs/banner.png)

<a href="https://www.https://www.linkedin.com/in/callum-arthurs/">
    <img src="https://github.com/c-arthurs/labelstrip/blob/master/docs/App_icon_6060.png" alt="Application logo" title="labelstrip" align="right" height="60" />
</a>

# labelstrip 


This was written to distribute an application to remove labels from whole slide image SVS files. As the original required scripting knowledge to run.

![labels](./docs/gui.png) 

*Figure 1. Image of the GUI for labelstrip.*

## Usage

Download the MAC version of the app - [here](https://github.com/c-arthurs/labelstrip/releases/download/v0.2/labelstrip_macos.app.zip)

<details>
  <summary>Notes on mac app</summary><p align="left">
  <a>
  The user may have to right click and select open to get it to open for the first time</a><br>
</details><br>

Download the PC version of the app - [here](https://github.com/c-arthurs/labelstrip/releases/download/v0.2/labelstrip_windows.exe)

<details>
  <summary>Notes on PC app</summary><p align="left">
  The pc version has been tested using only SVS files but should work on NDPI also </a><br>
</details>

### WARNING

This should work well on scripts that have a slide image. It has been reported that if the WSI was created without a label image then the script may corrupt the file.

Therefore please only use this on files that have been backed up. 

### Acknowledgement 

This script is built around the amazing [anonymize-slide](https://github.com/bgilbert/anonymize-slide). Their script was updated to python three to install it into this GUI. 

If you are looking for the python program to strip the labels without the GUI then please use their scripts directly. 

## Contributing 

We welcome any contributions to this project. The next thing to do on the todo list is add a *save codebreaker* option, which will allow the user to save a codebreaker file with an image of each label before they are removed from the dataset. 

Any issues of can be raised in the issues section and I will try to address them. 

We welcome pull requests for bugs. 
