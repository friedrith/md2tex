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


import shutil
import sys
import getopt
import os
import re
import subprocess

def usage():
    print("launch md4tex -h for the help");


try:
    opts, args = getopt.getopt(sys.argv[1:], "po:ct:a:d:hv",["pdf","output=","complete","title=","author=","date=","help","version","header=","footer=","configure-header","configure-footer"])
except getopt.GetoptError as err:
    # Affiche l'aide et quitte le programme
    print(err) # Va afficher l'erreur en anglais
    usage() # Fonction à écrire rappelant la syntaxe de la commande
    sys.exit(2)


pdf = False;
output = False;

outputFilenameBase = "";
#pdfOutputFilename = "";
outputFilename = "";
#texOutputFilename = "";

complete = False;
pathDir = os.environ['HOME']+'/.md2tex/';
headerFilename = pathDir+"header.tex";
footerFilename = pathDir+"footer.tex";

author = "Unknown author"
title = "Unknown title"
date=r"\\today"




def writeTexFile(texFilename,source):
    try:
        headerFile = open(headerFilename,'r');
        headerContent = headerFile.read();
        headerContent = re.sub(r'@@@Title@@@',title,headerContent);
        headerContent = re.sub(r'@@@Author@@@',author,headerContent);
        headerContent = re.sub(r'@@@Date@@@',date,headerContent);
        footerFile = open(footerFilename,'r');
        footerContent = footerFile.read();
        outputFile = open(texFilename,'w');
        outputFile.write(headerContent);
        outputFile.write(source);
        outputFile.write(footerContent);
        outputFile.close();
        headerFile.close();
        footerFile.close();
        return True;
    except IOError as err:
        print(err);
        return False;


if len(args) > 0:
    inputFilename = args[0]
    outputFilenameBase = re.sub(r'(.*).(txt|md|markdown)',r'\1',inputFilename);

#inputFilename = sys.argv[1];

for o, a in opts:
    if o in ("-p", "--pdf"):
       pdf = True;
       complete = True;
    elif o in ("-o","--output"):
       output = True;
       outputFilename = a; 
    elif o in ("-a","--author"):
       author = a;
    elif o in ("-t","--title"):
       title = a; 
    elif o in ("-d","--date"):
       date = a; 
    elif o in ("-c","--complete"):
        complete = True;
    elif o in ("-h","--help"):
        subprocess.call(["less",pathDir+"README.md"])
        sys.exit(1);
    elif o in ("--configure-header"):
        if len(args) > 0:
            if not os.path.isfile(args[0]):
                print("L'argument doit être un chemin vers un fichier valide");
                sys.exit(2);
            shutil.copyfile(args[0],pathDir+"header.tex");
            sys.exit(0);
        else :
            sys.usage();
    elif o in ("--configure-footer"):
        if len(args) > 0:
            if not os.path.isfile(args[0]):
                print("L'argument doit être un chemin vers un fichier valide");
                sys.exit(2);
            shutil.copyfile(args[0],pathDir+"footer.tex");
            sys.exit(0);
        else :
            sys.usage();
    elif o in ("--header"):
        if os.path.isfile(a):
            headerFilename = a;
        else:
            print("L'argument doit être un chemin vers un fichier valide");
            sys.exit(2);
    elif o in ("--footer"):
        if os.path.isfile(a):
            footerFilename = a;
        else:
            print("L'argument doit être un chemin vers un fichier valide");
            sys.exit(2);
    elif o in ("-v","--version"):
        print("md2tex version 1.0 sous licence GPL v3");
        sys.exit(0);
    else :
        usage();
        sys.exit(2);

#if output:
    #if pdf:
       #pdfOutputFilename = outputFilename;
    #else
       #texOutputFilename = outputFilename;
if len(args) == 0:
    usage();
    sys.exit(2);


try:
    fileSource=open(inputFilename,'r')

    # Conversion en string 
    source = fileSource.read()
    fileSource.close();


    source = re.sub(r'!\((.*) "(.*)"\)',r'\\begin{figure}\n\t\\includegraphics{\1}\n\t\\caption{\2}\n\\end{figure}',source);

    # itemize
    source = re.sub(r'\n\n(?=\* .*)',r'\n\n\\begin{itemize}\n',source);
    source = re.sub(r'\n\* (.*)\n\n',r'\item \1\n\\end{itemize}\n\n',source);
    source = re.sub(r'\n\* (.*)',r'\n\item \1',source);
    source = re.sub(r'\n\t\* (.*)',r'\n\t\subitem \1',source);
    
    # enumerate
    source = re.sub(r'\n\n(?=[0-9]+\. .*)',r'\n\n\\begin{enumerate}\n',source);
    source = re.sub(r'[0-9]+\. (.*)\n\n',r'\item \1\n\\end{enumerate}\n\n',source);
    source = re.sub(r'\n[0-9]+\. (.*)',r'\n\item \1',source);
    source = re.sub(r'\n\t[0-9]+\. (.*)',r'\n\t\subitem \1',source);


    # retour à la ligne
    source = re.sub(r'  \n',r'\n\\newline\n',source,re.MULTILINE);


    # gras **
    source = re.sub(r'(?<!\\)\*\*(([^*{}]|\\.)+?)(?<!\\)\*\*',r'\\textbf{\1}',source)
    # gras __
    source = re.sub(r'(?<!\\)__(([^_{}]|\\_)+?)(?<!\\)(?<!\\)__',r'\\textbf{\1}',source)
    # italique *
    source = re.sub(r'(?<!\\)\*(([^*{}]|\\.)+?)(?<!\\)\*',r'\\textit{\1}',source)
    # italique _
    source = re.sub(r'(?<!\\)_(([^_{}]|\\.)+?)(?<!\\)(?<!\\)_',r'\\textit{\1}',source)

    # subsubsection
    source = re.sub(r'### (.*?)\n',r'\\subsubsection{\1}\n',source)

    # subsection
    source = re.sub(r'## (.*?)\n',r'\\subsection{\1}\n',source)
    source = re.sub(r'(.*?)\n-+\n',r'\\subsection{\1}\n',source)

    # section
    source = re.sub(r'# (.*?)\n',r'\\section{\1}\n',source)
    source = re.sub(r'(.*?)\n=+\n',r'\\section{\1}\n',source)

    if  pdf:
        if output :
            outputFilenameBase = re.sub(r'(.*).pdf',r'\1', outputFilename);

        texFilename = outputFilenameBase+".tex";
        if writeTexFile(texFilename,source):
            subprocess.call(["pdflatex",texFilename])

    else :
        if output:
            writeTexFile(outputFilename,source);
        else:
            try:
                if complete :
                    headerFile = open(headerFilename,'r');
                    headerContent = headerFile.read();
                    headerContent = re.sub(r'@@@Title@@@',title,headerContent);
                    headerContent = re.sub(r'@@@Author@@@',author,headerContent);
                    headerContent = re.sub(r'@@@Date@@@',date,headerContent);
                    footerFile = open(footerFilename,'r');
                    footerContent = footerFile.read();
                    headerFile.close();
                    footerFile.close();
                    print(headerContent);
                    print(source);
                    print(footerContent);
                else :
                    print(source);

            except IOError as err:
                print(err);


except IOError as err:
    print(err);
 
