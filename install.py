#!/usr/bin/python3.2
# This file is part of md2tex.
# 
# 	Md2tex is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# 	Md2tex is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# 	You should have received a copy of the GNU General Public License along
# with md2tex.  If not, see <http://www.gnu.org/licenses/>.

import os
import shutil


pathDir = os.environ['HOME']+'/.md2tex/';
if not os.path.isdir(pathDir):
    os.mkdir(pathDir);

shutil.copyfile('README.md',pathDir+'README.md');
shutil.copyfile('header-default.tex',pathDir+'header-default.tex');
shutil.copyfile('footer-default.tex',pathDir+'footer-default.tex');
shutil.copyfile('md2tex.py',pathDir+'md2tex.py');
shutil.copyfile('header-default.tex',pathDir+'header.tex');
shutil.copyfile('footer-default.tex',pathDir+'footer.tex');
