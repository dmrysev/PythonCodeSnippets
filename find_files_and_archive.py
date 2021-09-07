#!/usr/bin/env python

import util.filesystem
import util.archive

files = util.filesystem.find_files_recursively('C:/Users/dmitrirossev/LinuxConfig/scripts', '*.sh')
util.archive.archive_files(files, 'output.zip')