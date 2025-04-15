# AdFree – Faux site de téléchargement APK (projet cybersécurité)

##  Lancer le site (localement ou sur VPS)

### 1. Cloner le dépôt
```bash
git clone <lien_git_du_projet>
cd download-site

### 2. Installer Flask

pip3 install -r requirements.txt

### 3. Lancer le serveur

python3 app.py

### 4. Le site sera accessible à l’adresse :
http://<IP_DU_VPS>:5050

### 5. Contenu du projet 
download-site/
├── app.py                # Serveur Flask
├── requirements.txt      # Dépendance Flask
├── ad_free.apk           # APK malveillant
├── static/
│   ├── style.css         # Feuille de style
│   └── app_icon.png      # Icône de l’appli
├── templates/
│   └── index.html        # Page HTML avec design + script
└── README.md


---

###  Étape 4 : Sauvegarde et ferme le fichier


