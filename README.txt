DEMANGE Alessi - NOEL Victor - L3 Informatique

-----Avant de lancer les programmes :
Il faut télécharger certaines librairies pour faire fonctionner les programmes.
Pour cela il suffit de faire ces commandes:
python3 -m pip install --user scipy xlwt

Pour lancer les programmes (exemple pour question3):
python3 question3.py

(chaque question qui demande un programme a son ficher en .py, donc pour chaque question
il suffit de noter python questionX.py où X correspond au numéro de la question) 

-----POUR TOUS LES PROGRAMMES:
Le fichier test.txt correspond à la valeur de sortie du programme.

-----POUR LES QUESTIONS DE 3 à 6:
Dans chacun des fichiers correspondants à la question, il existe une variable "vGLOBAL" qui correspond à la graine 
que l'on initialise avant de faire tourner les générateurs. 
Si vous voulez changer la graine, il faut donc changer la valeurs de "vGLOBAL"

-----POUR LA QUESTION 6:
Le programme a déjà été lancé donc les valeurs se trouvent dans le fichier excel "excel_question6.xls".
Néanmoins vous pouvez changer la valeur de "vGLOBAL" et donc changer les résultats.
Le programme question6.py écrit directement dans le fichier "excel_question6.xls" pour tous les générateurs.
Il faudra seulement regénérer les histogrammes dans le fichier excel si vous relancez le programme question6.py.

