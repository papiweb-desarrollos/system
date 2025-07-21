from flask import Flask, render_template, request, jsonify, send_file, url_for, Response
from flask_cors import CORS
import subprocess
import os
import glob
from datetime import datetime
import threading
import time

app = Flask(__name__)
CORS(app)

# Configuración
VIDEOS_DIR = "/workspaces/system/static"  # Cambiar a static
WORKSPACE_DIR = "/workspaces/system"  # Directorio base
PYTHON_CMD = "/workspaces/system/.venv/bin/python"
SOLAR_SCRIPT = "/workspaces/system/solar"
MAX_VIDEOS = 2  # Máximo de videos a mantener

# Estado de la aplicación
generation_status = {
    'running': False,
    'progress': 0,
    'message': 'Listo para generar videos',
    'current_video': '',
    'error': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video/<filename>')
def serve_video_optimized(filename):
    """Servir videos con soporte completo para HTTP Range requests"""
    try:
        video_path = os.path.join(VIDEOS_DIR, filename)
        
        if not os.path.exists(video_path):
            return jsonify({'error': 'Video no encontrado'}), 404
        
        # Detectar tipo MIME
        if filename.endswith('.mp4'):
            mimetype = 'video/mp4'
        elif filename.endswith('.avi'):
            mimetype = 'video/x-msvideo'
        else:
            return jsonify({'error': 'Formato de video no soportado'}), 400
        
        # Obtener el tamaño del archivo
        file_size = os.path.getsize(video_path)
        
        # Verificar si es una solicitud de rango
        range_header = request.headers.get('Range', None)
        if range_header:
            # Parsear el header Range
            byte_start = 0
            byte_end = file_size - 1
            
            range_match = range_header.replace('bytes=', '').split('-')
            if range_match[0]:
                byte_start = int(range_match[0])
            if range_match[1]:
                byte_end = int(range_match[1])
            
            # Asegurar que los rangos sean válidos
            byte_start = max(0, byte_start)
            byte_end = min(file_size - 1, byte_end)
            content_length = byte_end - byte_start + 1
            
            # Crear response con el rango solicitado
            def generate():
                with open(video_path, 'rb') as f:
                    f.seek(byte_start)
                    remaining = content_length
                    while remaining:
                        chunk_size = min(8192, remaining)
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break
                        remaining -= len(chunk)
                        yield chunk
            
            response = Response(
                generate(),
                206,  # Partial Content
                headers={
                    'Content-Type': mimetype,
                    'Accept-Ranges': 'bytes',
                    'Content-Length': str(content_length),
                    'Content-Range': f'bytes {byte_start}-{byte_end}/{file_size}',
                    'Cache-Control': 'public, max-age=3600',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, HEAD, OPTIONS',
                    'Access-Control-Allow-Headers': 'Range',
                }
            )
            return response
        else:
            # Solicitud completa del archivo
            response = send_file(
                video_path, 
                mimetype=mimetype,
                as_attachment=False
            )
            response.headers['Accept-Ranges'] = 'bytes'
            response.headers['Cache-Control'] = 'public, max-age=3600'
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Range'
            return response
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/videos')
def list_videos():
    """Listar todos los videos disponibles"""
    video_files = []
    
    # Asegurar que el directorio static existe
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    
    # Buscar archivos .mp4 y .avi en la carpeta static
    video_patterns = [
        os.path.join(VIDEOS_DIR, "*.mp4"),
        os.path.join(VIDEOS_DIR, "*.avi")
    ]
    
    for pattern in video_patterns:
        for video_path in glob.glob(pattern):
            filename = os.path.basename(video_path)
            stats = os.stat(video_path)
            
            # Determinar el tipo MIME
            if filename.endswith('.mp4'):
                mimetype = 'video/mp4'
            else:
                mimetype = 'video/x-msvideo'
            
            video_info = {
                'filename': filename,
                'path': video_path,
                'size': stats.st_size,
                'created': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'url': f'/video/{filename}',  # Usar ruta optimizada
                'mimetype': mimetype
            }
            video_files.append(video_info)
    
    # Ordenar por fecha de creación (más recientes primero)
    video_files.sort(key=lambda x: x['created'], reverse=True)
    
    return jsonify(video_files)

@app.route('/api/generate', methods=['POST'])
def generate_video():
    """Generar un nuevo video del sistema solar"""
    if generation_status['running']:
        return jsonify({'error': 'Ya hay una generación en progreso'}), 400
    
    try:
        data = request.get_json()
        mode = data.get('mode', 'basic')
        seconds = data.get('seconds', 10)
        fps = data.get('fps', 15)
        quality = data.get('quality', 'medium')
        speed = data.get('speed', 1.0)
        output_name = data.get('output', f'solar_{mode}_{int(time.time())}.mp4')
        
        # Validar parámetros
        valid_modes = [
            'basic', 'detailed', 'stars', 'orbits', 'all', 'zoom', 'zoom_pause', 'spaceship',
            'minimal', 'clean', 'realistic', 'cosmic', 'nebula', 'deep_space', 'night_sky',
            'asteroids', 'comets', 'meteor_shower', 'solar_flares', 'glow', 'trails',
            'satellites', 'planet_focus', 'all_effects'
        ]
        if mode not in valid_modes:
            return jsonify({'error': f'Modo inválido. Debe ser uno de: {", ".join(valid_modes)}'}), 400
        
        if not (1 <= seconds <= 120):
            return jsonify({'error': 'La duración debe estar entre 1 y 120 segundos'}), 400
        
        if not (5 <= fps <= 60):
            return jsonify({'error': 'Los FPS deben estar entre 5 y 60'}), 400
            
        if quality not in ['low', 'medium', 'high']:
            return jsonify({'error': 'La calidad debe ser low, medium o high'}), 400
            
        if not (0.1 <= speed <= 5.0):
            return jsonify({'error': 'La velocidad debe estar entre 0.1 y 5.0'}), 400
        
        # Iniciar generación en un hilo separado
        thread = threading.Thread(
            target=run_video_generation,
            args=(mode, seconds, fps, quality, speed, output_name)
        )
        thread.start()
        
        return jsonify({
            'message': 'Generación iniciada',
            'mode': mode,
            'seconds': seconds,
            'fps': fps,
            'quality': quality,
            'speed': speed,
            'output': output_name
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status')
def get_status():
    """Obtener el estado actual de la generación"""
    return jsonify(generation_status)

def cleanup_old_videos():
    """Mantener solo los últimos 2 videos en el directorio static"""
    try:
        video_files = []
        
        # Asegurar que el directorio static existe
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        
        # Buscar archivos .mp4 y .avi en static
        video_patterns = [
            os.path.join(VIDEOS_DIR, "*.mp4"),
            os.path.join(VIDEOS_DIR, "*.avi")
        ]
        
        for pattern in video_patterns:
            for video_path in glob.glob(pattern):
                stats = os.stat(video_path)
                video_files.append({
                    'path': video_path,
                    'mtime': stats.st_mtime
                })
        
        # Ordenar por fecha de modificación (más recientes primero)
        video_files.sort(key=lambda x: x['mtime'], reverse=True)
        
        # Eliminar videos antiguos si hay más de MAX_VIDEOS
        if len(video_files) > MAX_VIDEOS:
            for video_info in video_files[MAX_VIDEOS:]:
                try:
                    os.remove(video_info['path'])
                    print(f"Video eliminado: {video_info['path']}")
                except Exception as e:
                    print(f"Error eliminando video {video_info['path']}: {e}")
                    
    except Exception as e:
        print(f"Error en cleanup_old_videos: {e}")

def run_video_generation(mode, seconds, fps, quality, speed, output_name):
    """Ejecutar la generación de video en un hilo separado"""
    global generation_status
    
    try:
        generation_status.update({
            'running': True,
            'progress': 0,
            'message': f'Generando video en modo {mode} (calidad {quality})...',
            'current_video': output_name,
            'error': None
        })
        
        # Limpiar videos viejos antes de generar uno nuevo
        cleanup_old_videos()
        
        # Asegurar que el directorio static existe
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        
        # Construir la ruta completa del archivo de salida en static
        output_path = os.path.join(VIDEOS_DIR, output_name)
        
        # Comando para ejecutar el script
        cmd = [
            PYTHON_CMD, SOLAR_SCRIPT,
            '--mode', mode,
            '--seconds', str(seconds),
            '--fps', str(fps),
            '--quality', quality,
            '--speed', str(speed),
            '--output', output_path  # Usar ruta completa en static
        ]
        
        # Ejecutar el comando desde el directorio workspace
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=WORKSPACE_DIR  # Ejecutar desde workspace, no desde static
        )
        
        # Simular progreso (ya que el script no reporta progreso real)
        total_frames = seconds * fps
        for i in range(total_frames):
            if process.poll() is not None:
                break
            generation_status['progress'] = int((i / total_frames) * 90)
            time.sleep(0.1)
        
        # Esperar a que termine el proceso
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            # Verificar que el archivo se generó en static (puede ser .mp4 o .avi)
            # El script puede cambiar la extensión a .avi si MP4 no funciona
            output_path_avi = output_path.replace('.mp4', '.avi')
            actual_output_path = None
            
            if os.path.exists(output_path):
                actual_output_path = output_path
            elif os.path.exists(output_path_avi):
                actual_output_path = output_path_avi
                # Actualizar el nombre en el estado
                generation_status['current_video'] = os.path.basename(output_path_avi)
            
            if actual_output_path:
                file_size = os.path.getsize(actual_output_path)
                file_size_mb = file_size / (1024 * 1024)
                
                generation_status.update({
                    'running': False,
                    'progress': 100,
                    'message': f'Video {os.path.basename(actual_output_path)} generado exitosamente en calidad {quality} ({file_size_mb:.1f} MB)',
                    'current_video': os.path.basename(actual_output_path),
                    'error': None
                })
            else:
                generation_status.update({
                    'running': False,
                    'progress': 0,
                    'message': 'Error: Video no encontrado en static',
                    'current_video': '',
                    'error': f'Archivo no generado en {output_path}'
                })
        else:
            generation_status.update({
                'running': False,
                'progress': 0,
                'message': 'Error en la generación',
                'current_video': '',
                'error': stderr or 'Error desconocido'
            })
            
    except Exception as e:
        generation_status.update({
            'running': False,
            'progress': 0,
            'message': 'Error en la generación',
            'current_video': '',
            'error': str(e)
        })

if __name__ == '__main__':
    # Crear directorio de templates si no existe
    os.makedirs('templates', exist_ok=True)
    
    app.run(host='0.0.0.0', port=5001, debug=True)
