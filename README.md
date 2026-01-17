# 📹🎤 Video/Audio Streaming System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![PyAudio](https://img.shields.io/badge/PyAudio-Audio%20Streaming-orange)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Framework-purple)
![Socket](https://img.shields.io/badge/Sockets-Real%20time-yellow)

A real-time video and audio streaming system with GUI for bidirectional client-server communication. Perfect for surveillance, video conferencing, and media transmission.

## ✨ Features

### 📹 Real-time Video Streaming
- **Webcam capture** using default camera
- **JPEG compression** for network optimization
- **20 FPS** smooth streaming
- **Adaptable resolution** (640x480 default)
- **Automatic reconstruction** on server side

### 🎤 Synchronous Audio Streaming
- **Microphone capture** (16-bit, 44.1kHz)
- **Low latency** (1024 sample buffer)
- **Direct playback** on server
- **CD quality** (44.1kHz, mono)
- **Stream synchronization**

### 🌐 Network Architecture
- **TCP Sockets** reliable connections
- **Separate ports**: Video (5000) & Audio (5001)
- **Multi-threading** concurrent stream handling
- **Auto-reconnection** on disconnect
- **Configurable IP** for local network

### 🖥️ GUI Interfaces
- **Client Tkinter**: Simple connection interface
- **Server Tkinter**: Real-time visualization
- **Dynamic updates**: Auto-refreshing frames
- **Error handling**: Clear user messages
- **Clean shutdown**: Safe resource closure

## 🚀 Quick Installation

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install opencv-python pyaudio pillow numpy
```

## ⚙️ Configuration

### Default Ports
```python
VIDEO_PORT = 5000
AUDIO_PORT = 5001
SERVER_IP = "192.168.100.7"  # Change to your server IP
```

### Video Settings
```python
WIDTH = 640
HEIGHT = 480
FPS = 20
JPEG_QUALITY = 70
```

### Audio Settings
```python
SAMPLE_RATE = 44100
CHANNELS = 1
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
```

## 🎮 Usage Guide

### 1. **Start Server**
```bash
python server.py
```
Server displays: "Listening on ports 5000 and 5001"

### 2. **Start Client**
```bash
python client.py
```
1. Enter server IP address
2. Click "Connect"
3. Webcam and microphone start automatically

### 3. **Monitoring**
- **Server side**: Real-time visualization
- **Client side**: Automatic transmission
- **Stop**: Use "Quit" button on each interface

### 4. **Local Testing**
Use localhost on same machine:
```python
SERVER_IP = "127.0.0.1"
```

## 📊 Performance

### Bandwidth Requirements
| Resolution | FPS | Quality | Video Bitrate | Audio Bitrate | Total |
|------------|-----|---------|---------------|---------------|-------|
| 640x480 | 20 | 70% | ~500-800 Kbps | ~700 Kbps | ~1.2-1.5 Mbps |
| 320x240 | 15 | 60% | ~200-300 Kbps | ~700 Kbps | ~0.9-1.0 Mbps |

### Latency
- **Video**: 50-100ms
- **Audio**: 20-50ms
- **Total sync**: < 150ms

## 🌐 Network Setup

### Local Network (LAN)
```python
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Local IP: {local_ip}")
```

### Internet Usage
For internet streaming:
1. **Port forwarding** on router
2. **Public IP** of server
3. **Firewall** open for ports 5000-5001

## 🔧 Troubleshooting

### Common Issues:
- **Webcam not detected**: Check permissions, test with `cv2.VideoCapture(0)`
- **Microphone issues**: Verify PyAudio installation, check permissions
- **Connection errors**: Verify server IP, firewall, server status
- **High latency**: Reduce resolution/FPS, check network

## 🛡️ Security Recommendations
1. **Use on private networks** only (LAN recommended)
2. **Implement authentication** for public use
3. **Consider encryption** for sensitive streams
4. **Monitor connection logs**

## 📁 Project Structure
```
video-streaming-system/
├── client.py              # Client application
├── server.py              # Server application
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

## 📄 License
MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author
**omar badrani**  
- GitHub: https://github.com/omarbadrani  
- Email: omarbadrani770@gmail.com

---

⭐ **If this project is useful, please star the repository!** ⭐

---

**Version**: 1.0.0  
**Python**: 3.7+  
**OS**: Windows, Linux, macOS

*Video/Audio Streaming System - Real-time communication made simple* 📹🎤✨
