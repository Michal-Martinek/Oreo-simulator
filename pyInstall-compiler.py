# This file can be used for compiling this project using PyInstaller
    # it runs PyInstaller and creates easier acces to the app and cleanes unnecessary files 

import os
import shutil
from distutils.dir_util import copy_tree
# from swinlnk.swinlnk import SWinLnk
import win32file

destinationFolderName = 'dist'
dataFolderName = 'data'
mainFileName = 'main.py'
assetFolderName = 'Assets'



dataFolderPath = destinationFolderName + '\\' + dataFolderName
scriptname = mainFileName.split('.')[0]
linkName = scriptname + '.lnk'
exeName = scriptname + '.exe'

def makeNewDestinationFolder():
    try:
        shutil.rmtree(destinationFolderName)
    except OSError:
        pass
    os.mkdir(destinationFolderName)
    os.mkdir(dataFolderPath)
def copyAssetsFolder():
    copy_tree(assetFolderName, dataFolderPath + '//' + assetFolderName)
def moveBundledApp():
    bundledAppFolder = f'{dataFolderPath}\\{scriptname}'
    copy_tree(bundledAppFolder, dataFolderPath)
    shutil.rmtree(bundledAppFolder)
def runPyInstaller(flags):
    cmd = f'pyinstaller {" ".join(flags)} {mainFileName}'
    os.system(cmd)
def createExeLink(): # TODO
    exePath = os.getcwd() + f'\\{dataFolderPath}\\{scriptname}.exe'
    destPath = os.getcwd() + f'\\{destinationFolderName}\\{scriptname}.lnk'
    win32file.CreateSymbolicLink(destPath, exePath)
    # SWinLnk().create_lnk(
    #     os.path.join(os.getcwd(), dataFolderPath, scriptname + '.exe'), 
    #     os.path.join(os.getcwd(), destinationFolderName, linkName))

def removeBuildFolder():
    shutil.rmtree(destinationFolderName + '\\build')

flags = [
    '--onedir', '--noconsole',
    f'--distpath {dataFolderPath}', 
    f'--workpath {destinationFolderName}\\build',
    f'--specpath {destinationFolderName}\\build'
]

makeNewDestinationFolder()
runPyInstaller(flags)
moveBundledApp()
removeBuildFolder()
copyAssetsFolder()
# createExeLink()

input('\nEnter to exit...')