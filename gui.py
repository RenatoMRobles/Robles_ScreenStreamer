import customtkinter as ctk
import subprocess
import sys

# Estética visual ejecutiva
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class RoblesStreamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Robles ScreenStreamer 🌟")
        self.geometry("450x300")
        self.resizable(False, False)
        
        self.lbl_title = ctk.CTkLabel(self, text="Panel de Control Sintrópico", font=ctk.CTkFont(size=22, weight="bold"))
        self.lbl_title.pack(pady=(30, 20))
        
        self.lbl_codec = ctk.CTkLabel(self, text="Selecciona el Códec de Bienestar:", font=ctk.CTkFont(size=14))
        self.lbl_codec.pack(pady=5)
        
        # ACTUALIZACIÓN: Nuevas opciones claras para el ingeniero
        self.codec_var = ctk.StringVar(value="MJPEG (Puerto 5000)")
        self.combo_codec = ctk.CTkOptionMenu(
            self, 
            values=["MJPEG (Puerto 5000)", "H.264 (Puerto 8554)"], 
            variable=self.codec_var,
            width=250
        )
        self.combo_codec.pack(pady=10)
        
        self.btn_start = ctk.CTkButton(
            self, text="▶ Iniciar Transmisión", command=self.toggle_stream, 
            fg_color="#28a745", hover_color="#218838",
            font=ctk.CTkFont(size=15, weight="bold"), height=40
        )
        self.btn_start.pack(pady=(25, 10))
        
        self.is_streaming = False
        self.proceso_motor = None
        
        self.protocol("WM_DELETE_WINDOW", self.cierre_armonico)

    def toggle_stream(self):
        if not self.is_streaming:
            self.btn_start.configure(text="⏹ Detener Transmisión", fg_color="#dc3545", hover_color="#c82333")
            self.is_streaming = True
            
            seleccion = self.codec_var.get()
            print(f"🌟 Orquestando motor con perfil: {seleccion}")
            
            if "MJPEG" in seleccion:
                self.proceso_motor = subprocess.Popen([sys.executable, "streamer.py"])
            
            elif "H.264" in seleccion:
                print("🌟 Encendiendo servidor RTSP purificado (MediaMTX)...")
                # 1. El mesero abre las puertas en el puerto universal 8554
                self.proceso_servidor = subprocess.Popen(["mediamtx.exe"])
                
                print("🌟 Cocinando flujo H.264 (FFmpeg)...")
                # 2. El chef cocina y le entrega el video directamente al mesero
                comando_ffmpeg = [
                    "ffmpeg.exe",
                    "-f", "gdigrab",           
                    "-framerate", "15",        
                    "-i", "desktop",           
                    "-c:v", "libx264",         
                    "-preset", "ultrafast",    
                    "-tune", "zerolatency",    
                    "-f", "rtsp",              
                    "rtsp://localhost:8554/bienestar" # El chef entrega el plato aquí
                ]
                self.proceso_motor = subprocess.Popen(comando_ffmpeg)

        else:
            self.btn_start.configure(text="▶ Iniciar Transmisión", fg_color="#28a745", hover_color="#218838")
            self.is_streaming = False
            print("✨ Apagando la arquitectura sintrópica...")
            
            # Apagamos al chef
            if self.proceso_motor:
                self.proceso_motor.terminate()
                self.proceso_motor = None
                
            # Apagamos al mesero
            if getattr(self, 'proceso_servidor', None):
                self.proceso_servidor.terminate()
                self.proceso_servidor = None

    def cierre_armonico(self):
        if self.proceso_motor:
            self.proceso_motor.terminate()
        if getattr(self, 'proceso_servidor', None):
            self.proceso_servidor.terminate()
        self.destroy()

if __name__ == "__main__":
    app = RoblesStreamerApp()
    app.mainloop()