# Basic:

## 1. Download the Voyager data
Following instructions at README.md file

### 1.1 Uncompress files at VGISS folder
In order to have concordance with actual folder in this repository.

## 2. Install
Install requeried software as INSTALL.md file.

Don't forget set the environment variables!

## 3. Convert to FITS format
Use the converter.py for this purpose

## 4. Preprocessing:
### 4.1 Find objects
Run the SourceDetection.ipynb Notebook file in order to set up the detection method.

Modify the creamarcas1.py script file; this script can create the regions files for the entire dataset!

### 4.2 Generate slots

Run the creaSlots.py script changing "orden" and "clave" variables with the available data!