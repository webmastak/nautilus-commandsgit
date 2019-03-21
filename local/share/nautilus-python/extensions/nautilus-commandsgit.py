#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, urllib
from gi.repository import GObject, Nautilus

class Commands(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def commands_git(self, window, files):
        if len(files) != 1:
            return
         
        cmd = 'commands-git {}'.format(str(urllib.unquote(files[0].get_uri()[7:])))
        subprocess.Popen(cmd, shell=True)
        return

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        item = Nautilus.MenuItem(
            name="Commands::Git",
            label="Commands Git",
            tip="Commands Git"
        )

        item.connect('activate', self.commands_git, files)
        return [item]  
