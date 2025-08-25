import socket
import threading
import cv2
import numpy as np
import pyaudio
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import struct
import queue

class VideoAudioServer:
    def __init__(self, video_port=5000, audio_port=5001):
        self.host = '0.0.0.0'
        self.video_port = video_port
        self.audio_port = audio_port
        self.running = False

        # Sockets
        self.video_server_socket = None
        self.audio_server_socket = None
        self.video_socket = None
        self.audio_socket = None

        # Queue for thread-safe UI updates
        self.frame_queue = queue.Queue()

        # Interface
        self.root = tk.Tk()
        self.root.title("Serveur de Surveillance")
        self.setup_ui()

        # Démarrer
        self.start_server()

        self.root.protocol("WM_DELETE_WINDOW", self.safe_stop)
        self.root.mainloop()

    def setup_ui(self):
        """Interface serveur"""
        self.root.geometry("800x600")

        # Affichage vidéo
        self.video_label = ttk.Label(self.root)
        self.video_label.pack(fill=tk.BOTH, expand=True)

        # Status
        self.status_var = tk.StringVar(value=f"En attente sur ports {self.video_port} (vidéo) et {self.audio_port} (audio)")
        ttk.Label(self.root, textvariable=self.status_var).pack()

        ttk.Button(self.root, text="Quitter", command=self.safe_stop).pack()

        # Process queue
        self.root.after(100, self.process_queue)

    def start_server(self):
        """Démarre le serveur"""
        try:
            # Video server socket
            self.video_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.video_server_socket.bind((self.host, self.video_port))
            self.video_server_socket.listen(1)

            # Audio server socket
            self.audio_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.audio_server_socket.bind((self.host, self.audio_port))
            self.audio_server_socket.listen(1)

            self.running = True
            self.status_var.set(f"En écoute sur ports {self.video_port} et {self.audio_port}")

            threading.Thread(target=self.accept_video_client, daemon=True).start()
            threading.Thread(target=self.accept_audio_client, daemon=True).start()

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de démarrer: {str(e)}")

    def accept_video_client(self):
        try:
            self.video_socket, addr = self.video_server_socket.accept()
            self.status_var.set(f"Client vidéo connecté: {addr[0]}")
            threading.Thread(target=self.receive_video, daemon=True).start()
        except Exception as e:
            if self.running:
                self.status_var.set(f"Erreur vidéo accept: {str(e)}")

    def accept_audio_client(self):
        try:
            self.audio_socket, addr = self.audio_server_socket.accept()
            self.status_var.set(f"Client audio connecté: {addr[0]}")
            threading.Thread(target=self.receive_audio, daemon=True).start()
        except Exception as e:
            if self.running:
                self.status_var.set(f"Erreur audio accept: {str(e)}")

    def receive_video(self):
        """Reçoit la vidéo"""
        try:
            while self.running:
                # Taille du frame
                size_data = self.video_socket.recv(4)
                if len(size_data) != 4:
                    break

                size = struct.unpack(">L", size_data)[0]
                data = b''

                # Données vidéo
                while len(data) < size:
                    packet = self.video_socket.recv(size - len(data))
                    if not packet:
                        break
                    data += packet

                # Décoder et mettre en queue
                frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
                if frame is not None:
                    self.frame_queue.put(frame)

        except Exception as e:
            self.status_var.set(f"Erreur vidéo: {str(e)}")
        finally:
            if self.video_socket:
                self.video_socket.close()

    def process_queue(self):
        """Traite la queue des frames pour mise à jour UI"""
        try:
            while not self.frame_queue.empty():
                frame = self.frame_queue.get_nowait()
                self.display_frame(frame)
        except queue.Empty:
            pass
        finally:
            if self.running:
                self.root.after(10, self.process_queue)

    def display_frame(self, frame):
        """Affiche le frame"""
        frame = cv2.resize(frame, (640, 480))
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)

        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)

    def receive_audio(self):
        """Reçoit et joue l'audio"""
        try:
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=True,
                frames_per_buffer=1024
            )

            while self.running:
                data = self.audio_socket.recv(1024)
                if not data:
                    break
                stream.write(data)

            stream.stop_stream()
            stream.close()
            audio.terminate()

        except Exception as e:
            self.status_var.set(f"Erreur audio: {str(e)}")
        finally:
            if self.audio_socket:
                self.audio_socket.close()

    def safe_stop(self):
        """Arrêt sécurisé"""
        self.running = False

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

        if self.video_server_socket:
            try:
                self.video_server_socket.close()
            except:
                pass

        if self.audio_server_socket:
            try:
                self.audio_server_socket.close()
            except:
                pass

        self.root.quit()

if __name__ == "__main__":
    VideoAudioServer()