#!/usr/bin/env python

import util.filesystem
import util.archive

files = list(util.filesystem.find_files_recursively('C:/Users/dmitrirossev/LinuxConfig/scripts', '*.sh'))
files += list(util.filesystem.find_files_recursively('C:/Users/dmitrirossev/LinuxConfig/scripts', '*.py'))
util.archive.archive_files(files, 'output.zip')

