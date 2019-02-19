# Embedded-RPI3-Camera

Le but du projet est de contrôler une caméra via une RPI3. Pour cela nous avons 3 composants principaux à savoir: Un client qui , et 2 serveurs donc 1 pour la caméra et l'autre pour le cerveau moteur  


## Serveur Caméra

### Description

 Il s'agit du serveur en charge de la prise de la photo.
### Cross Compilation du fichier source

### Excution
Lancer la commande
 ./serveur_tcp

## Serveur servoMoteur

### Description
Lancer mon serveurMoteur
 - Lancer la commande  python3.6 serveurMoteur.py
 - le serveur est connecté sur le port 5000
 - Passer des arguments du type a,b,c où a,b,c sont des entiers a: sensRotation b= angleRotation c= tempsRotation
 si a=1 rotation dans le sens des aiguilles d'une montre
si a=2 sens contraire des aiguilles d'une montre

### Execution
Depuis la racine du projet exécuter les commandes suivantes
1. cd ServeurServoMoteurs
2. python3.6  serveurMoteur.py

## ServeurWeb

### Description
Il s'agit du serveur principal qui envoie les pages  au client qui est un navigateur , de via les buttons disponibles sur la page , l'utilisateur peut envoyer des requêttes (prendre une photo, tourner à gauche , tourner à droite )

 - La communication avec le serveur qui contrôle la caméra  se fait par le biais d'une communication TCP sur le port 1977.
 - La communication avec le serveur qui contrÔle les servoMoteurs se fait par le biais d'une connexion   TCP sur le port 5000.

### Excution

  Excuter les commandes suivantes :
  1. cd ServeurIhm
  2. python2.7 serveurWeb.py
  3. ouvrir le navigateur de votre choix , taper http://ip:8080/ (ip est l'adresse de la raspberry pi sur le réseau local, si c'est pour un test sans réseau utiliser 127.0.0.1)
