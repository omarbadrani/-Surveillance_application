# Video/Audio Streaming System 📹🎤

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![PyAudio](https://img.shields.io/badge/PyAudio-Audio%20Streaming-orange)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Framework-purple)
![Socket](https://img.shields.io/badge/Sockets-Real%20time-yellow)

Un système complet de streaming vidéo et audio en temps réel avec interface graphique, permettant une communication bidirectionnelle entre client et serveur. Parfait pour la surveillance, les conférences vidéo, ou la transmission multimédia.

## ✨ Fonctionnalités

### 📹 Streaming Vidéo en Temps Réel
- **Capture webcam** : Utilisation de la caméra par défaut
- **Compression JPEG** : Optimisation du flux réseau
- **20 FPS** : Fluidité optimale pour la surveillance
- **Résolution adaptable** : 640x480 par défaut
- **Reconstruction automatique** : Décodage côté serveur

### 🎤 Streaming Audio Synchrone
- **Capture microphone** : Audio 16-bit, 44.1kHz
- **Faible latence** : Buffer de 1024 échantillons
- **Sortie directe** : Lecture immédiate côté serveur
- **Qualité CD** : 44.1kHz, mono
- **Synchronisation** : Flux parallèles synchronisés

### 🌐 Architecture Réseau
- **TCP Sockets** : Connexions fiables
- **Ports séparés** : Vidéo (5000) et Audio (5001)
- **Multi-threading** : Gestion concurrente des flux
- **Reconnexion automatique** : Gestion des déconnexions
- **Adresse IP configurable** : Support réseau local

### 🖥️ Interfaces Graphiques
- **Client Tkinter** : Connexion simple et intuitive
- **Serveur Tkinter** : Visualisation en temps réel
- **Mise à jour dynamique** : Frames actualisés automatiquement
- **Gestion des erreurs** : Messages utilisateur clairs
- **Arrêt propre** : Fermeture sécurisée des ressources

## 🖼️ Architecture du Système

### Diagramme Client-Serveur
```
┌─────────────────┐           ┌─────────────────┐
│     CLIENT      │           │     SERVEUR     │
│                 │           │                 │
│  Webcam ──────┐ │  Video    │ ┌─────────────┐ │
│               ↓ │  Port 5000│ │↓            │ │
│  [Capture]   ──┼─────────────┼─┤[Display]   │ │
│               │ │           │ │             │ │
│  Micro ──────┐ │  Audio     │ ┌─────────────┐ │
│              ↓ │  Port 5001│ │↓            │ │
│  [Capture]   ──┼─────────────┼─┤[Playback]  │ │
│                 │           │ │             │ │
│  Interface     │           │ │  Interface  │ │
│  Tkinter       │           │ │  Tkinter    │ │
└─────────────────┘           └─────────────────┘
```

## 🚀 Installation Rapide

### Prérequis
- Python 3.7 ou supérieur
- Webcam et microphone fonctionnels
- Connexion réseau (local ou Internet)

### Installation des Dépendances

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows :
venv\Scripts\activate
# Linux/Mac :
source venv/bin/activate

# Installer les dépendances
pip install opencv-python pyaudio pillow numpy
```

### Dépendances Détaillées
```txt
opencv-python>=4.5.0      # Traitement vidéo
pyaudio>=0.2.11           # Capture et lecture audio
Pillow>=8.0.0            # Manipulation d'images pour Tkinter
numpy>=1.19.0            # Traitement des données
```

**Note pour Windows** : PyAudio nécessite parfois l'installation manuelle de PortAudio.

## ⚙️ Configuration

### Ports par Défaut
```python
# Client et serveur utilisent les mêmes ports
VIDEO_PORT = 5000
AUDIO_PORT = 5001

# Adresse IP du serveur (à modifier selon votre réseau)
SERVER_IP = "192.168.100.7"  # Exemple pour réseau local
```

### Paramètres Vidéo
```python
# Résolution
WIDTH = 640
HEIGHT = 480
FPS = 20

# Compression JPEG
JPEG_QUALITY = 70  # Équilibre qualité/bande passante
```

### Paramètres Audio
```python
# Configuration PyAudio
SAMPLE_RATE = 44100      # Qualité CD
CHANNELS = 1             # Mono
CHUNK_SIZE = 1024        # Taille du buffer
FORMAT = pyaudio.paInt16 # 16-bit
```

## 🎮 Guide d'Utilisation

### 1. **Démarrer le Serveur**
```bash
python server.py
```
Le serveur affichera : "En écoute sur ports 5000 et 5001"

### 2. **Démarrer le Client**
```bash
python client.py
```
1. Entrez l'adresse IP du serveur
2. Cliquez sur "Se connecter"
3. La webcam et le micro démarrent automatiquement

### 3. **Surveillance**
- **Côté serveur** : Visualisation en temps réel
- **Côté client** : Transmission automatique
- **Arrêt** : Utiliser le bouton "Quitter" sur chaque interface

### 4. **Tests Réseau**
Pour tester sur la même machine :
```python
# Utiliser localhost ou 127.0.0.1
SERVER_IP = "127.0.0.1"
```

## 🔧 Architecture Technique

### Client (Émetteur)
```python
class VideoAudioClient:
    """
    Responsabilités :
    1. Capture vidéo (OpenCV)
    2. Capture audio (PyAudio)
    3. Encodage JPEG
    4. Transmission TCP
    5. Interface utilisateur
    """
    
    def send_video(self):
        # Capture frame → Encode JPEG → Envoi socket
        pass
    
    def send_audio(self):
        # Capture audio → Envoi socket
        pass
```

### Serveur (Récepteur)
```python
class VideoAudioServer:
    """
    Responsabilités :
    1. Réception vidéo TCP
    2. Réception audio TCP
    3. Décodage JPEG
    4. Lecture audio
    5. Affichage interface
    """
    
    def receive_video(self):
        # Réception socket → Décodage → Affichage
        pass
    
    def receive_audio(self):
        # Réception socket → Lecture audio
        pass
```

## 📊 Performances et Optimisation

### Bande Passante Requise
| Résolution | FPS | Qualité | Débit Vidéo | Débit Audio | Total |
|------------|-----|---------|-------------|-------------|-------|
| 640x480 | 20 | 70% | ~500-800 Kbps | ~700 Kbps | ~1.2-1.5 Mbps |
| 320x240 | 15 | 60% | ~200-300 Kbps | ~700 Kbps | ~0.9-1.0 Mbps |
| 1280x720 | 30 | 80% | ~2-3 Mbps | ~700 Kbps | ~2.7-3.7 Mbps |

### Latence
- **Vidéo** : 50-100ms (compression + réseau)
- **Audio** : 20-50ms (buffer minimal)
- **Synchronisation** : < 150ms totale

### Optimisations Implémentées
```python
# 1. Compression JPEG adaptative
quality = 70  # Ajustable selon bande passante

# 2. Buffer audio optimisé
chunk_size = 1024  # Équilibre latence/CPU

# 3. Threads séparés
video_thread = threading.Thread(target=send_video)
audio_thread = threading.Thread(target=send_audio)

# 4. Queue pour UI
frame_queue = queue.Queue()  # Évite le blocage
```

## 🌐 Configuration Réseau

### Réseau Local (LAN)
```python
# Découvrir l'IP locale
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"IP locale: {local_ip}")
```

### Réseau Internet
Pour fonctionner sur Internet :
1. **Port forwarding** sur le routeur
2. **IP publique** du serveur
3. **Firewall** ouvert pour ports 5000-5001

### Dépannage Réseau
```bash
# Vérifier la connectivité
ping SERVER_IP

# Vérifier les ports
telnet SERVER_IP 5000
telnet SERVER_IP 5001

# Vérifier le firewall
netsh advfirewall firewall show rule name=all
```

## 🐛 Dépannage

### Problèmes Courants

#### 1. **Webcam non détectée**
```
Solutions:
- Vérifier les permissions caméra
- Tester avec cv2.VideoCapture(0)
- Redémarrer l'application
- Vérifier les drivers
```

#### 2. **Microphone non détecté**
```
Solutions:
- Vérifier PyAudio installation
- Tester avec un autre programme audio
- Vérifier les permissions microphone
```

#### 3. **Erreur de connexion**
```
Solutions:
- Vérifier l'IP du serveur
- Vérifier le firewall
- Vérifier que le serveur est démarré
- Tester avec localhost (127.0.0.1)
```

#### 4. **Latence élevée**
```
Solutions:
- Réduire la résolution
- Réduire les FPS
- Augmenter la compression
- Vérifier le réseau
```

### Logs de Débogage
```python
# Activer les logs détaillés
import logging
logging.basicConfig(level=logging.DEBUG)

# Tester les composants individuellement
def test_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    print(f"Camera test: {ret}")
    cap.release()
```

## 🔒 Sécurité

### Recommandations
1. **Réseau privé** : Utiliser en LAN seulement
2. **Authentification** : À implémenter pour usage public
3. **Chiffrement** : SSL/TLS pour les flux sensibles
4. **Journalisation** : Logs des connexions

### Améliorations de Sécurité
```python
# Exemple de chiffrement basique
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

secure_socket = context.wrap_socket(client_socket, server_side=True)
```

## 🔮 Fonctionnalités Futures

### Court Terme (v1.1)
- [ ] Enregistrement local des flux
- [ ] Contrôle qualité dynamique
- [ ] Interface de configuration
- [ ] Support multi-clients

### Moyen Terme (v1.5)
- [ ] Chat texte intégré
- [ ] Partage d'écran
- [ ] Effets vidéo/audio
- [ ] Support mobile

### Long Terme (v2.0)
- [ ] WebRTC intégration
- [ ] Cloud streaming
- [ ] Intelligence artificielle
- [ ] API REST

## 📋 Cas d'Utilisation

### 🏠 Surveillance Domestique
- **Baby monitor** : Surveillance enfants
- **Surveillance propriété** : Sécurité maison
- **Animal monitoring** : Surveillance animaux de compagnie
- **Elderly care** : Surveillance personnes âgées

### 🏢 Professionnel
- **Surveillance bureau** : Sécurité entreprise
- **Conférence interne** : Communication équipes
- **Monitoring processus** : Surveillance industrielle
- **Support à distance** : Assistance technique

### 🎓 Éducation
- **Cours en ligne** : Streaming éducatif
- **Laboratoires distants** : Expériences à distance
- **Surveillance examen** : Surveillance en ligne
- **Projets étudiants** : Développement applications

### 🎮 Personnel
- **Streaming gaming** : Partage sessions jeu
- **Vidéoconférence** : Appels personnels
- **Création de contenu** : Production vidéo
- **Expérimentation** : Projets DIY

## 🛠️ Développement

### Structure des Fichiers
```
video-streaming-system/
├── client.py              # Application client
├── server.py              # Application serveur
├── requirements.txt       # Dépendances
├── README.md             # Documentation
└── assets/               # Ressources
    ├── icons/            # Icônes application
    └── config/           # Fichiers configuration
```

### Tests Unitaires
```python
# Exemple de tests
def test_video_capture():
    """Test de la capture vidéo"""
    cap = cv2.VideoCapture(0)
    assert cap.isOpened()
    ret, frame = cap.read()
    assert ret and frame is not None
    cap.release()

def test_audio_stream():
    """Test du stream audio"""
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024
    )
    assert stream.is_active()
    stream.close()
    audio.terminate()
```

## 🤝 Contribution

### Comment Contribuer
1. **Fork** le dépôt
2. **Créez une branche** (`git checkout -b feature/amélioration`)
3. **Commitez vos changements** (`git commit -am 'Ajout de fonctionnalité'`)
4. **Push vers la branche** (`git push origin feature/amélioration`)
5. **Ouvrez une Pull Request**

### Normes de Code
- Suivre PEP 8
- Documenter les fonctions
- Ajouter des tests
- Gérer les erreurs proprement

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2024 Video/Audio Streaming System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## ⚠️ Avertissements

### Vie Privée
- Informez les personnes filmées
- Respectez les lois locales
- Ne diffusez pas sans consentement
- Protégez les données sensibles

### Usage Responsable
- Surveillance légale uniquement
- Respect du droit à l'image
- Conformité RGPD/CNIL
- Usage éthique recommandé

## 👤 Auteur

**Développeur Principal** - [omar badrani](https://github.com/omarbadrani)

## 🙏 Remerciements

- **OpenCV** - Traitement vidéo
- **PyAudio** - Capture audio
- **Tkinter** - Interface graphique
- **Python Socket** - Communication réseau

## 📞 Support

Pour obtenir de l'aide :

1. **Consulter les Issues** sur GitHub
2. **Vérifier la documentation**
3. **Créer une nouvelle issue** avec :
   - Description du problème
   - Messages d'erreur
   - Configuration système
   - Étapes pour reproduire

## 📚 Ressources Utiles

### Documentation
- [OpenCV Documentation](https://docs.opencv.org/)
- [PyAudio Documentation](http://people.csail.mit.edu/hubert/pyaudio/)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)
- [Tkinter Guide](https://tkdocs.com/)

### Tutoriels
- [Real-time Streaming Tutorial](https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)
- [Audio Processing in Python](https://realpython.com/playing-and-recording-sound-python/)
- [Network Programming](https://realpython.com/python-sockets/)

### Outils Complémentaires
- [FFmpeg](https://ffmpeg.org/) - Traitement média avancé
- [GStreamer](https://gstreamer.freedesktop.org/) - Pipeline média
- [WebRTC](https://webrtc.org/) - Standard streaming web

---

⭐ **Si ce projet vous est utile, n'oubliez pas de mettre une étoile sur GitHub !** ⭐

---

## 🚀 Prochaines Étapes

### Pour les Utilisateurs
1. Tester en réseau local
2. Ajuster les paramètres selon vos besoins
3. Intégrer dans vos projets
4. Partager vos retours

### Pour les Développeurs
1. Explorer le code source
2. Ajouter de nouvelles fonctionnalités
3. Optimiser les performances
4. Améliorer la sécurité

### Pour les Entreprises
1. Évaluer les besoins spécifiques
2. Personnaliser l'interface
3. Intégrer avec systèmes existants
4. Déployer à plus grande échelle

---

**Dernière mise à jour** : Janvier 2025  
**Version** : 1.0.0  
**Support Python** : 3.7+  
**Systèmes supportés** : Windows, Linux, macOS

---

*Video/Audio Streaming System - Communication en temps réel, simplifiée* 📹🎤✨
