import socket
import threading
import cv2
import pyaudio
import tkinter as tk
from tkinter import ttk, messagebox
import struct
import time

class VideoAudioClient:
    def __init__(self, video_port=5000, audio_port=5001):
        # Configuration
        self.server_ip = None
        self.video_port = video_port
        self.audio_port = audio_port
        self.running = False

        # Sockets
        self.video_socket = None
        self.audio_socket = None

        # Interface
        self.root = tk.Tk()
        self.root.title("Client Vidéo/Audio")
        self.setup_ui()

        self.root.protocol("WM_DELETE_WINDOW", self.safe_stop)
        self.root.mainloop()

    def setup_ui(self):
        """Interface utilisateur"""
        self.root.geometry("400x200")
        self.status_var = tk.StringVar(value="Entrez l'IP du serveur et connectez-vous")

        ttk.Label(self.root, text="IP du serveur:").pack(pady=5)
        self.ip_entry = ttk.Entry(self.root)
        self.ip_entry.pack(pady=5)
        self.ip_entry.insert(0, "192.168.100.7")  # Default IP

        ttk.Button(self.root, text="Se connecter", command=self.connect_to_server).pack(pady=10)

        ttk.Label(self.root, textvariable=self.status_var, padding=10).pack()
        ttk.Button(self.root, text="Quitter", command=self.safe_stop).pack()

    def connect_to_server(self):
        """Établit les connexions"""
        self.server_ip = self.ip_entry.get().strip()
        if not self.server_ip:
            messagebox.showerror("Erreur", "Veuillez entrer une IP valide")
            return

        try:
            # Initialiser caméra
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                raise RuntimeError("Caméra non disponible")

            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 20)

            # Initialiser audio
            self.audio = pyaudio.PyAudio()
            self.stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024
            )

            # Connexions réseau
            self.video_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.video_socket.connect((self.server_ip, self.video_port))

            self.audio_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.audio_socket.connect((self.server_ip, self.audio_port))

            self.running = True
            self.status_var.set(f"Connecté à {self.server_ip}")

            # Threads
            threading.Thread(target=self.send_video, daemon=True).start()
            threading.Thread(target=self.send_audio, daemon=True).start()

        except Exception as e:
            messagebox.showerror("Erreur", f"Connexion impossible: {str(e)}")
            self.safe_stop()

    def send_video(self):
        """Envoi vidéo"""
        try:
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    continue

                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
                data = buffer.tobytes()
                self.video_socket.sendall(struct.pack(">L", len(data)) + data)
                time.sleep(0.05)  # ~20 FPS

        except Exception as e:
            if self.running:
                self.status_var.set(f"Erreur vidéo: {str(e)}")
                self.safe_stop()

    def send_audio(self):
        """Envoi audio"""
        try:
            while self.running:
                data = self.stream.read(1024, exception_on_overflow=False)
                self.audio_socket.sendall(data)

        except Exception as e:
            if self.running:
                self.status_var.set(f"Erreur audio: {str(e)}")
                self.safe_stop()

    def safe_stop(self):
        """Arrêt propre"""
        self.running = False

        if hasattr(self, 'cap') and self.cap:
            self.cap.release()

        if hasattr(self, 'stream') and self.stream:
            try:
                self.stream.stop_stream()
                self.stream.close()
            except:
                pass

        if hasattr(self, 'audio') and self.audio:
            self.audio.terminate()

        if self.video_socket:
            try:
                self.video_socket.close()
            except:
                pass

        if self.audio_socket:
            try:
                self.audio_socket.close()
            except:
                pass

        self.root.quit()

if __name__ == "__main__":
    VideoAudioClient()