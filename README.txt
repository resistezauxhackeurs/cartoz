Cartoz by Cédric bertrand / résistez aux hackeurs


Cet outil permet d'énumérer tous les sous-domaines associé à un domaine

===== Outils utilisés =====
- dnsscan (https://github.com/rbsec/dnscan)
- acamar (https://github.com/si9int/Acamar)
- dnsrecon (https://github.com/darkoperator/dnsrecon)
- sublist3r (https://github.com/aboul3la/Sublist3r)


===== Installation =====
apt install -y python3 python3-pip python3-virtualenv python3-setuptools git dnsrecon software-properties-common
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


===== Usage =====
usage: cartoz.py [-h] [-d [DOMAINE [DOMAINE ...]]] [--enum [ENUM [ENUM ...]]] [--scan_file_projet [SCAN_FILE_PROJET [SCAN_FILE_PROJET ...]]]
  -h, --help            show this help message and exit
  -d [DOMAINE [DOMAINE ...]], --domaine [DOMAINE [DOMAINE ...]] : Domaine a analyser
  --enum [ENUM [ENUM ...]], --enum [ENUM [ENUM ...]] : Enumerer les domaines
  --scan_file_projet [SCAN_FILE_PROJET [SCAN_FILE_PROJET ...]], --scan_file_projet [SCAN_FILE_PROJET [SCAN_FILE_PROJET ...]] : Scanner tous les domaines contenus dans un fichier texte
  
===== Exemple =====
python cartoz.py -d resistez-aux-hackeurs.com --enum


===== Résultats ======
fichier des domaines ecrit dans :audits/resistez-aux-hackeurs.com/domaines_resistez-aux-hackeurs.com.txt
www.resistez-aux-hackeurs.com
autoconfig.resistez-aux-hackeurs.com
autodiscover.resistez-aux-hackeurs.com
ftp.resistez-aux-hackeurs.com
resistez-aux-hackeurs.com
www.resistez-aux-hackeurs.com

