import cv2
import numpy as np
import mss
import time
from flask import Flask, Response

app = Flask(__name__)

def generar_fotogramas():
    print("🌟 Motor de captura sintrópico activado...")
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        
        while True:
            tiempo_inicio = time.time()
            
            # Captura y procesamiento
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            frame = cv2.resize(frame, (1280, 720)) 
            
            fps = 1 / (time.time() - tiempo_inicio)
            cv2.putText(frame, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            frame_bytes = buffer.tobytes()
            
            # LA LLAVE MAESTRA PARA MILESTONE: 
            # Calculamos y declaramos el tamaño exacto (Content-Length) de la matriz de bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n'
                   b'Content-Length: ' + str(len(frame_bytes)).encode() + b'\r\n\r\n' + 
                   frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generar_fotogramas(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("🌐 Iniciando servidor luminoso en: http://0.0.0.0:5000/video_feed")
    app.run(host='0.0.0.0', port=5000, threaded=True)