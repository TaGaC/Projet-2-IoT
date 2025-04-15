# 🛡️ Projet-2-IoT – AdFree  
**Utilisation d’un RAT sur un Google Pixel 5 pour récolter les identifiants d’un serveur domotique personnel.**

---

## 🌐 Objectif
Simuler une attaque réaliste où une victime installe une fausse application Android "AdFree" supposée bloquer les publicités, mais en réalité elle installe un **RAT** qui permet à l’attaquant de :
- collecter des données sur le téléphone,
- retrouver des éléments de connexion,
- accéder à une interface domotique simulée via Flask.

---

## 🧰 Technologies utilisées
- Python 3 + Flask (site Web unique)
- HTML/CSS (templates)
- APK malveillant généré avec **AhMyth**
- Environnement : local ou VPS

---

## 🚀 Lancer le site (localement ou sur un VPS)

### 1. Cloner le dépôt

```bash
git clone <lien_git_du_projet>
cd download-site
```

### 2. Créer un environnement virtuel Python (optionnel mais recommandé)
```bash
python -m venv venv
venv\Scripts\activate  # Sous Windows
# OU
source venv/bin/activate  # Sous Linux/macOS
```

### 2. Installer Flask
```bash
pip3 install -r requirements.txt
```
### 3. Lancer le serveur Flask
```bash
python app.py
```


### 4. Accès aux différentes pages
Une fois lancé, le site est accessible via :
```bash
http://<IP_DU_VPS>:5050
```

### 🔑 Identifiants d’accès à l’interface domotique
Nom d'utilisateur : admin

Mot de passe : SuperSecret123
### 5. Contenu du projet 
```bash
download-site/
├── app.py                # Application Flask (serveur Web unique)
├── ad_free.apk           # APK infecté à télécharger
├── static/
│   ├── style.css         # Styles personnalisés (optionnel)
│   └── app_icon.png      # Icône d’illustration
├── templates/
│   ├── index.html        # Page "AdFree" (téléchargement)
│   ├── login.html        # Interface de connexion IoT
│   └── dashboard.html    # Interface domotique simulée
└── README.md             # Ce fichier
```
### Notes supplémentaires
L’application Flask écoute sur le port 5050 par défaut.

Le projet est compatible avec un hébergement local ou un VPS Ubuntu 22.04.

Pour une version "production", un reverse proxy Nginx peut être ajouté par la suite.

---



