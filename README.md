
![Version](https://img.shields.io/badge/Version-1.0.5-blue.svg)
![Build](https://img.shields.io/badge/Build-passing-green.svg)
![Python](https://img.shields.io/badge/Python-3.6-yellow.svg)


# Passive-Aggressive Bot

This program is designed to walk through our project directory and flag files that need to be cleaned and removed. This is written with the rules of our folders setup. Ie `Year/JOBNumber/_L(Suffix)`

If the program finds files that are placed in the settings list it will then go and find the project leader and staff. It will then email them with the list of files that are suppose to be in a different location.

**Reasoning:** The current files it searches for are videos and point cloud scans. These files are both large and unlikely to be changed. So having them on Jobs drive which is backedup on regular intervals is reduntent and a waste of space on the expensive SAN.

The program could also move these files itself. The idea is however to encourage better filing practices. Also more fun to harras users! 

## How to use
Python must be installed. The program uses python3.6, this means 3.4+ should be fine. 
1. Check settings are filled out correctly. `settings.py`
2. cd to directory where files are located
3. `python main.py`
4. Wait, the program will now either run or throw errors at you. 


## Planned Development
- Check folder structures and file locations against rules, such as should a file be there or not?
- Check Zip file and folder names to see if they are the same and flag
- Remove non existant staff
- Remove double ups incase Proj Leader is also included as staff memember

