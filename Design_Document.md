# Design Document

This file briefly describes the design of the project:

The user interface xml files were created using Qt Designer and are located in the folder named 'UI Files'. The ui files were compiled into python code and are present in the main project folder. A separate xml file, icons.qrc, is made for icons in toolbar each time icons are updated. This file needs to be compiled into python code and imported in order for toolbar to appear with updated icons.

The image files for icons are located inside 'Resources' folder.

image_editor.py implements the code for all image processing functions used in the app.

main.py implements the graphical user interface and calls appropriate functions from image_editor.py.
