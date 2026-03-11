import customtkinter as ctk
import subprocess  # Nuestro orquestador de procesos
import sys

# Configuramos la elegancia visual
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class RoblesStreamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Arquitectura de la ventana
        self.title("Robles ScreenStreamer 🌟")
        self.geometry("450x300")
        self.resizable(False, False)
        
        # Título
        self.lbl_title = ctk.CTkLabel(self, text="Panel de Control Sintrópico", font=ctk.CTkFont(size=22, weight="bold"))
        self.lbl_title.pack(pady=(30, 20))
        
        # Selector
        self.lbl_codec = ctk.CTkLabel(self, text="Selecciona el Códec de Bienestar:", font=ctk.CTkFont(size=14))
        self.lbl_codec.pack(pady=5)
        
        self.codec_var = ctk.StringVar(value="MJPEG (Universal Driver)")
        self.combo_codec = ctk.CTkOptionMenu(
            self, 
            values=["MJPEG (Universal Driver)", "H.264 (Próximamente)"], 
            variable=self.codec_var,
            width=250
        )
        self.combo_codec.pack(pady=10)
        
        # Botón
        self.btn_start = ctk.CTkButton(
            self, 
            text="▶ Iniciar Transmisión", 
            command=self.toggle_stream, 
            fg_color="#28a745", hover_color="#218838",
            font=ctk.CTkFont(size=15, weight="bold"), height=40
        )
        self.btn_start.pack(pady=(25, 10))
        
        # Variables de estado y control de procesos
        self.is_streaming = False
        self.proceso_motor = None  # Aquí guardaremos el enlace mágico hacia streamer.py
        
        # Protocolo de seguridad: Si haces clic en la "X" de la ventana, apagamos todo
        self.protocol("WM_DELETE_WINDOW", self.cierre_armonico)

    def toggle_stream(self):
        if not self.is_streaming:
            # Encendemos la luz
            if self.codec_var.get() == "MJPEG (Universal Driver)":
                self.btn_start.configure(text="⏹ Detener Transmisión", fg_color="#dc3545", hover_color="#c82333")
                self.is_streaming = True
                print("🌟 Orquestando el encendido del motor MJPEG...")
                
                # Lanzamos streamer.py de forma independiente y armónica
                self.proceso_motor = subprocess.Popen([sys.executable, "streamer.py"])
            else:
                print("✨ El motor H.264 está en fase de diseño. Selecciona MJPEG por ahora.")
        else:
            # Apagamos la luz
            self.btn_start.configure(text="▶ Iniciar Transmisión", fg_color="#28a745", hover_color="#218838")
            self.is_streaming = False
            print("✨ Apagando el motor sintrópico...")
            
            # Si el motor está corriendo, lo detenemos con gracia
            if self.proceso_motor:
                self.proceso_motor.terminate()
                self.proceso_motor = None

    def cierre_armonico(self):
        # Aseguramos el bienestar del sistema apagando el motor antes de cerrar la GUI
        if self.proceso_motor:
            self.proceso_motor.terminate()
        self.destroy()

if __name__ == "__main__":
    app = RoblesStreamerApp()
    app.mainloop()