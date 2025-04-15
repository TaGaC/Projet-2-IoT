
# 🚀 Lancer et arrêter Flask avec `screen` sur le VPS

## 🧰 Objectif
Garder ton serveur Flask actif **même après fermeture de la session SSH**, tout en pouvant le relancer facilement plus tard si besoin.

---

## ✅ 1. Lancer Flask avec `screen`

### a. Se connecter au VPS
```bash
ssh root@<IP_DU_VPS>
```

### b. Lancer une nouvelle session `screen`
```bash
screen -S flask_iot
```

### c. Naviguer vers ton dossier de projet et démarrer Flask
```bash
cd ~/download-site
sudo python3 app.py
```

> **Remarque :** Le port dans `app.py` doit être `8443` ou `80` (port ouvert chez Ionos)

### d. Détacher `screen` (laisser Flask tourner en arrière-plan)
Appuie sur :
```
Ctrl + A puis D
```

---

## 🔁 2. Revenir dans la session plus tard

Pour reprendre la session :
```bash
screen -r flask_iot
```

---

## 🛑 3. Arrêter proprement Flask

1. Reconnecte-toi à la session :
```bash
screen -r flask_iot
```

2. Arrête le serveur Flask :
```
Ctrl + C
```

3. Quitte `screen` :
```bash
exit
```

---

## 🧼 4. Supprimer une session screen bloquée (si besoin)

Lister les sessions existantes :
```bash
screen -ls
```

Tuer une session par ID :
```bash
screen -X -S <id> quit
```

---

## 📦 Résumé des commandes utiles

| Action                   | Commande                          |
|--------------------------|-----------------------------------|
| Créer session            | `screen -S flask_iot`             |
| Détacher                 | `Ctrl + A`, puis `D`              |
| Reprendre session        | `screen -r flask_iot`             |
| Stopper Flask            | `Ctrl + C`                        |
| Fermer session           | `exit`                            |
| Lister les sessions      | `screen -ls`                      |
| Fermer une session bloquée | `screen -X -S <id> quit`        |
