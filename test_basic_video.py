#!/usr/bin/env python3
"""
Script de prueba para generar video básico sin problemas de codec
"""

import pygame
import numpy as np
import cv2
import os
import sys

def main():
    print("Inicializando pygame...")
    pygame.init()
    
    # Configuración básica
    WIDTH, HEIGHT = 800, 600
    FPS = 15
    SECONDS = 35
    TOTAL_FRAMES = FPS * SECONDS
    OUTPUT_FILE = "test_basic_working.avi"
    
    print(f"Generando {TOTAL_FRAMES} frames a {FPS} FPS para {SECONDS} segundos")
    
    # Crear surface
    screen = pygame.Surface((WIDTH, HEIGHT))
    
    # Configurar writer de video con codec simple
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # MJPG es más compatible
    video_writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, FPS, (WIDTH, HEIGHT))
    
    if not video_writer.isOpened():
        print("Error: No se pudo abrir el writer de video")
        return False
    
    print("Iniciando generación de frames...")
    
    for frame_num in range(TOTAL_FRAMES):
        # Limpiar pantalla
        screen.fill((0, 0, 20))  # Azul oscuro
        
        # Calcular ángulo de rotación
        angle = (frame_num / FPS) * 0.5  # Rotación lenta
        
        # Dibujar sol en el centro
        sun_x = WIDTH // 2
        sun_y = HEIGHT // 2
        pygame.draw.circle(screen, (255, 255, 0), (sun_x, sun_y), 40)
        
        # Dibujar planetas orbitando
        import math
        for planet_idx in range(3):
            orbit_radius = 100 + planet_idx * 80
            planet_angle = angle + planet_idx * 1.2
            
            planet_x = sun_x + int(math.cos(planet_angle) * orbit_radius)
            planet_y = sun_y + int(math.sin(planet_angle) * orbit_radius)
            
            colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]
            sizes = [15, 20, 12]
            
            pygame.draw.circle(screen, colors[planet_idx], (planet_x, planet_y), sizes[planet_idx])
        
        # Convertir surface a array numpy
        frame_array = pygame.surfarray.array3d(screen)
        frame_array = np.rot90(frame_array)
        frame_array = np.flipud(frame_array)
        
        # Convertir RGB a BGR para OpenCV
        frame_bgr = cv2.cvtColor(frame_array, cv2.COLOR_RGB2BGR)
        
        # Escribir frame al video
        video_writer.write(frame_bgr)
        
        # Mostrar progreso
        if frame_num % 50 == 0 or frame_num == TOTAL_FRAMES - 1:
            progress = ((frame_num + 1) / TOTAL_FRAMES) * 100
            print(f"Progreso: {progress:.1f}% ({frame_num + 1}/{TOTAL_FRAMES} frames)")
    
    # Cerrar writer
    video_writer.release()
    pygame.quit()
    
    # Verificar archivo
    if os.path.exists(OUTPUT_FILE):
        file_size = os.path.getsize(OUTPUT_FILE)
        print(f"✅ Video creado exitosamente: {OUTPUT_FILE}")
        print(f"   Tamaño: {file_size} bytes ({file_size / (1024*1024):.2f} MB)")
        return True
    else:
        print("❌ Error: El archivo no se creó")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
