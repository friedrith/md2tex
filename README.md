md2tex
======


## NOM

	
	md2tex, convertisseur mardown vers latex

## SYNOPSIS

	md2tex [options] source.md 
	md2tex [options] source.mardown
	md2tex [options] source.txt
	md2tex --configure-header header.tex
	md2tex --configure-footer footer.tex

## DESCRIPTION

    Il s'agit d'un script permettant de générer du code latex à partir d'une
    source formatée à l'aide du langage markdown. Il peut générer juste la
    partie décrite par le fichier markdown mais en mode COMPLET, il peut aussi
    générer l'ensemble d'un fichier latex compilable. Enfin, il peut aussi
    générer le pdf correspondant au latex.

	Le fichier donné en entré doit être un fichier dont le contenu est formatté
	sous markdown. Il est à noté que l'extension du fichier source ne modifie en
	rien au comportement du convertisseur.

	Par défaut le code généré est affiché sur la sortie standard.

## OPTIONS
	
	-a, --author
		active le mode COMPLET et définit l'auteur du code latex généré. Par
		défaut, le nom de l'auteur est "Unknown author".

	-c, --complete
		active le mode COMPLET qui génére le code complet d'un fichier latex
		capable de compiler en incorporant le code relatif au fichier d'entrée
		à un fichier latex existant. Le header et le footer de ce fichier
		existant sont disponibles dans ~/.md4tex/header.tex et
		~/.md4tex/footer.tex.
	
	--configure-footer [footer]
		remplace le fichier de footer par défaut par le nouveau fichier donné en
		paramètre. Le fichier de footer 

	--configure-header [header]
		remplace le fichier de header par défaut par le nouveau fichier donné en
		paramètre. Afin de pouvoir ultérieurement changer certaines valeurs comme le
		titre, l'auteur ou la date, les emplacements prévus à cet effet dans le nouveau
		header configuré doivent respectivement comporter les chaines '@@@Title@@@',
		'@@@Author@@@' et '@@@Date@@@'.

	-d, --date
		action le mode COMPLET et définit la date du code latex généré. Par
		défault, la date est à \today.

	-o, --output [sortie]
		définit le nom du fichier de sortie. 

	-p, --pdf
		active le mode COMPLET et génère le fichier pdf. Attention, si le
		fichier de sortie n'est pas explicité par l'utilisation de l'option -o,
		les fichiers source.tex et source.pdf sont crées où source désigne la
		basename du fichier donné en entrée.

	-t, --title
		active le mode COMPLET et définit le titre du code latex généré. Par
		défaut, le titre est "Unknown title".

## UTILISATION

    Pour utiliser ce script, il faut impérativement lancer le script
    d'installation 'install.sh'.  Une fois cela fait, il est possible de créer
    un alias dans son fichier de configuration de shell vers le fichier
    ~/.md2tex/md2tex.py

## AUTEUR

	Le code de ce script python a été écrit par Thibault Friedrich.	En cas de problème, 
	de questions, de propositions d'améliorations, vous pouvez me contacter à
	<thibaultfriedrich@gmail.com>

## BUGS

	Il n'existe pas de bugs connus cependant, certaines fonctionnalités du
	langage markdown n'ont pas encore été gérées.


