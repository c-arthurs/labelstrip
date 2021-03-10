![labels](./docs/App_Icon.png)

# labelstrip

This was quickly written to distribute an application to remove labels from whole slide image SVS files. As the original required scripting knowledge to run.

![labels](./docs/gui.png) 

Figure 1. Image of the GUI for labelstrip.

This script is built around the amazing [anonymize-slide](https://github.com/bgilbert/anonymize-slide). Their script was updated to python three to install it into this GUI. 

### WARNING

This should work well on scripts that have a slide image. It has been reported that if the WSI was created without a label image then the script may corrupt the file.

Therefore please only use this on files that have been backed up.
