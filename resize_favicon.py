#!/usr/bin/env python3
"""
Script para redimensionar el favicon a tamaños estándar para web
"""

from PIL import Image
import os

def resize_favicon():
    """Redimensiona el favicon a tamaños estándar"""
    
    # Ruta del favicon original
    original_path = "/workspaces/system/static/favicon.png"
    
    if not os.path.exists(original_path):
        print(f"Error: No se encuentra el archivo {original_path}")
        return
    
    try:
        # Abrir la imagen original
        with Image.open(original_path) as img:
            print(f"Imagen original: {img.size[0]}x{img.size[1]} píxeles")
            
            # Crear respaldo del original
            backup_path = "/workspaces/system/static/favicon_original.png"
            img.save(backup_path)
            print(f"Respaldo guardado en: {backup_path}")
            
            # Tamaños estándar para favicon
            sizes = [16, 32, 64]
            
            for size in sizes:
                # Redimensionar manteniendo la proporción
                resized = img.resize((size, size), Image.Resampling.LANCZOS)
                
                # Guardar cada tamaño
                output_path = f"/workspaces/system/static/favicon_{size}x{size}.png"
                resized.save(output_path, optimize=True)
                print(f"Creado: favicon_{size}x{size}.png")
            
            # Crear el favicon principal de 32x32 (tamaño más común)
            main_favicon = img.resize((32, 32), Image.Resampling.LANCZOS)
            main_favicon.save(original_path, optimize=True)
            print(f"Favicon principal actualizado: 32x32 píxeles")
            
            # Crear también un ICO para mayor compatibilidad
            ico_path = "/workspaces/system/static/favicon.ico"
            ico_sizes = [(16, 16), (32, 32)]
            ico_images = []
            
            for size in ico_sizes:
                ico_img = img.resize(size, Image.Resampling.LANCZOS)
                ico_images.append(ico_img)
            
            # Guardar como ICO
            ico_images[0].save(ico_path, format='ICO', sizes=ico_sizes)
            print(f"Favicon ICO creado: {ico_path}")
            
            print("\n✅ Favicon adaptado exitosamente!")
            print("Archivos creados:")
            print("- favicon.png (32x32) - Principal")
            print("- favicon.ico - Formato ICO")
            print("- favicon_16x16.png")
            print("- favicon_32x32.png") 
            print("- favicon_64x64.png")
            print("- favicon_original.png - Respaldo")
            
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    resize_favicon()
