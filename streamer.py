import cv2
import numpy as np
import mss
import time
from flask import Flask, Response

# Iniciamos nuestra aplicación web luminosa
app = Flask(__name__)

def generar_fotogramas():
    print("🌟 Motor de captura sintrópico activado...")
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        
        while True:
            tiempo_inicio = time.time()
            
            # Capturamos la pantalla pura
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            
            # Opcional pero recomendado para bienestar de la red: 
            # Redimensionamos a 720p para un equilibrio perfecto entre calidad y fluidez
            frame = cv2.resize(frame, (1280, 720)) 
            
            # Medimos el rendimiento en FPS
            fps = 1 / (time.time() - tiempo_inicio)
            cv2.putText(frame, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Transformamos la matriz en un formato JPEG altamente compatible
            ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            frame_bytes = buffer.tobytes()
            
            # Entregamos el fotograma en un flujo continuo (multipart/x-mixed-replace)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Creamos la ruta de red donde vivirá el video
@app.route('/video_feed')
def video_feed():
    return Response(generar_fotogramas(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("🌐 Iniciando servidor luminoso en: http://localhost:5000/video_feed")
    # host='0.0.0.0' permite que Milestone, incluso desde otra máquina, pueda ver el flujo
    app.run(host='0.0.0.0', port=5000, threaded=True)