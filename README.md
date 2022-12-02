# SVXLINK REMOTE

Permet d'envoyer des code DTMF à travers le réseau.

Version: 1.0.0


# Dépendances

- Python 3.x
- Flask

# Installation

Pour installer svxlink-remote, tapez les commandes suivantes :


`cd /opt && git clone https://github.com/F4IPA/svxlink-remote.git`

`echo "votre_clé_ici" > svxlink-remote/key.txt`

`sudo pip3 install flask`

`sudo mv svxlink-remote/svxlink-remote.service /etc/systemd/system`

`sudo systemctl enable svxlink-remote.service`

`sudo systemctl start svxlink-remote.service`


# Crédits

Guillaume F4IPA


# Licence

GPL