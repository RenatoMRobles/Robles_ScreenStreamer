import customtkinter as ctk

# Configuramos la elegancia visual: un tema oscuro tipo XProtect
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class RoblesStreamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Arquitectura de la ventana
        self.title("Robles ScreenStreamer 🌟")
        self.geometry("450x300")
        self.resizable(False, False)
        
        # Título principal
        self.lbl_title = ctk.CTkLabel(self, text="Panel de Control Sintrópico", font=ctk.CTkFont(size=22, weight="bold"))
        self.lbl_title.pack(pady=(30, 20))
        
        # Etiqueta para el selector
        self.lbl_codec = ctk.CTkLabel(self, text="Selecciona el Códec de Bienestar:", font=ctk.CTkFont(size=14))
        self.lbl_codec.pack(pady=5)
        
        # Selector de Protocolo (El botón deslizable de tu visión)
        self.codec_var = ctk.StringVar(value="MJPEG (Universal Driver)")
        self.combo_codec = ctk.CTkOptionMenu(
            self, 
            values=["MJPEG (Universal Driver)", "H.264 (Próximamente)"], 
            variable=self.codec_var,
            width=250
        )
        self.combo_codec.pack(pady=10)
        
        # Botón de Acción Luminosa
        self.btn_start = ctk.CTkButton(
            self, 
            text="▶ Iniciar Transmisión", 
            command=self.toggle_stream, 
            fg_color="#28a745", # Verde benéfico
            hover_color="#218838",
            font=ctk.CTkFont(size=15, weight="bold"),
            height=40
        )
        self.btn_start.pack(pady=(25, 10))
        
        # Estado lógico
        self.is_streaming = False

    def toggle_stream(self):
        # Esta es la lógica que orquestará el encendido y apagado
        if not self.is_streaming:
            self.btn_start.configure(text="⏹ Detener Transmisión", fg_color="#dc3545", hover_color="#c82333")
            self.is_streaming = True
            print(f"🌟 Preparando motor con códec: {self.codec_var.get()}")
            # Aquí inyectaremos la conexión con tu archivo streamer.py en el próximo paso
        else:
            self.btn_start.configure(text="▶ Iniciar Transmisión", fg_color="#28a745", hover_color="#218838")
            self.is_streaming = False
            print("✨ Transmisión en pausa armónica.")

if __name__ == "__main__":
    app = RoblesStreamerApp()
    app.mainloop()