import os

def init():
  os.system('rm ../.vibes.json')
  os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-runner" # avoids a Qt warning
  # Since replit migration to Nix, Qt windows stay blank by default, this is a simple but very limited workaround without user input support...
  #os.environ["QT_QPA_PLATFORM"] = "eglfs"
  # Better workaround however windows cannot be moved, so the Hide menu should be used...
  # Additionally, replit will automatically open Webview, which is not desired.
  # This can be disabled manually in the repl settings.
  os.environ["QT_QPA_PLATFORM"] = "vnc:port=5910"

  import pygame
  pygame.init()
  os.system('chmod +x vibes/VIBes-viewer && ./vibes/VIBes-viewer &')
  import time

  os.system('clear') # removing prior warnings in the terminal

  while not os.path.exists('../.vibes.json'):
    time.sleep(1)
    os.system('clear')
    print("Waiting for VIBes to open...")
  
  os.system('vncviewer -FullScreen=1 127.0.0.1:5910 &') # To be used with os.environ["QT_QPA_PLATFORM"] = "vnc:port=5910"
  time.sleep(1)
  os.system('clear')

def pauseDrawing():
  import sys
  sys.stdin.read(1) # prevent the GUI from closing...

init()