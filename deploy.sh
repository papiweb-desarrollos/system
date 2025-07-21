#!/bin/bash

# Script para preparar y deployar en GitHub Pages
# Papiweb Desarrollos Informáticos

echo "🚀 Preparando deploy para GitHub Pages..."

# Crear directorio docs si no existe
mkdir -p docs/static docs/videos

# Copiar archivos estáticos
echo "📁 Copiando archivos estáticos..."
cp -r static/* docs/static/ 2>/dev/null || true

# Verificar archivos importantes
echo "✅ Verificando archivos importantes..."
if [ -f "docs/index.html" ]; then
    echo "✓ index.html presente"
else
    echo "❌ index.html faltante"
fi

if [ -f "docs/static/obser.png" ]; then
    echo "✓ obser.png presente"
else
    echo "❌ obser.png faltante"
fi

if [ -f "docs/.nojekyll" ]; then
    echo "✓ .nojekyll presente"
else
    echo "❌ .nojekyll faltante"
fi

# Mostrar tamaño de archivos
echo "📊 Tamaño de archivos importantes:"
ls -lh docs/static/*.png docs/static/*.avi 2>/dev/null || echo "Algunos archivos no encontrados"

echo ""
echo "🌟 ¡Preparación completa!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Commit y push de los cambios"
echo "2. Habilitar GitHub Pages en la configuración del repositorio"
echo "3. Seleccionar 'docs' como directorio fuente"
echo "4. El sitio estará disponible en: https://USUARIO.github.io/REPOSITORIO"
echo ""
echo "💡 Para habilitar GitHub Pages:"
echo "   Settings → Pages → Source: Deploy from a branch → Branch: main → Folder: /docs"
