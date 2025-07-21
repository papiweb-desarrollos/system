# 🌟 Sistema Solar - Generador de Videos

**Papiweb Desarrollos Informáticos**

Generador avanzado de videos del sistema solar con 24 modos únicos de visualización, efectos especiales y interfaz web moderna.

## 🚀 Demo en Vivo

**🌐 Sitio Web:** [papiweb-desarrollos.github.io/system](https://papiweb-desarrollos.github.io/system)

## ✨ Características Principales

- 🎬 **24 modos de visualización únicos**
- 🌌 **Efectos visuales realistas** (partículas, neblinas, fondos astronómicos)
- 🎨 **Interfaz moderna** con fondo de imagen astronómica real
- 📱 **Diseño responsive** optimizado para todos los dispositivos
- ⚡ **Streaming optimizado** con HTTP Range requests
- 🔄 **Auto-cleanup** de archivos con límite de 2 videos
- 🎯 **Deploy automático** en GitHub Pages

## 🛠️ Tecnologías

### Backend
- **Python 3.12** con Flask
- **Pygame** para generación de videos
- **OpenCV** para procesamiento de video
- **NumPy** para cálculos matemáticos

### Frontend
- **HTML5 + CSS3** moderno
- **JavaScript** vanilla para interactividad
- **Video HTML5** con controles personalizados
- **Diseño responsive** con CSS Grid/Flexbox

### DevOps
- **GitHub Actions** para CI/CD
- **GitHub Pages** para hosting estático
- **Docker support** (opcional)

## 📂 Estructura del Proyecto

```
├── 🌐 docs/                    # GitHub Pages (sitio estático)
│   ├── index.html             # Página principal
│   ├── static/                # Recursos estáticos
│   └── videos/                # Videos de demostración
├── 🎬 web_app.py              # Aplicación Flask principal
├── 🌌 solar                   # Generador de videos del sistema solar
├── 📁 templates/              # Templates HTML de Flask
├── 🎨 static/                 # Archivos estáticos (favicons, videos)
├── 🚀 deploy.sh               # Script de deploy
└── ⚙️ .github/workflows/      # GitHub Actions
```

## 🎥 Modos de Visualización

### 🌍 Básicos
- **Básico:** Sistema solar simple
- **Mínimal:** Solo planetas sin etiquetas  
- **Limpio:** Vista simplificada

### 🎨 Artísticos  
- **Artístico:** Estilo pintado
- **Vintage:** Efecto retro
- **Retro:** Colores nostálgicos

### 🔬 Científicos
- **Científico:** Datos precisos
- **Educativo:** Con información
- **Detallado:** Máxima información

### 🌠 Cósmicos
- **Cósmico:** Efectos espaciales
- **Galáctico:** Fondo de galaxia
- **Nebulosa:** Efectos de nebulosa

### 🎬 Cinematográficos
- **Cinematográfico:** Estilo película
- **Épico:** Escala grandiosa
- **Dramático:** Iluminación intensa

### 🌈 Especiales
- **Psicodélico:** Colores vibrantes
- **Fantasía:** Estilo mágico
- **Místico:** Atmósfera misteriosa

### 🔥 Efectos
- **Fuego:** Partículas de fuego
- **Agua:** Efectos acuáticos
- **Energía:** Rayos energéticos
- **Todos los Efectos:** Combinación completa

## 🚀 Instalación y Uso

### Requisitos
- Python 3.12+
- pip
- Git

### Instalación Local
```bash
# Clonar repositorio
git clone https://github.com/papiweb-desarrollos/system.git
cd system

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instalar dependencias
pip install flask pygame opencv-python numpy

# Ejecutar aplicación
python web_app.py
```

### Deploy en GitHub Pages
```bash
# Ejecutar script de preparación
./deploy.sh

# Commit y push
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main
```

## ⚙️ Configuración de GitHub Pages

1. Ve a **Settings** → **Pages** en tu repositorio
2. Selecciona **Source:** Deploy from a branch
3. **Branch:** main
4. **Folder:** /docs
5. ¡Tu sitio estará disponible en pocos minutos!

## 🌐 URLs

- **🏠 Sitio Principal:** [papiweb-desarrollos.github.io/system](https://papiweb-desarrollos.github.io/system)
- **💳 Donaciones:** [link.mercadopago.com.ar/papiweb](https://link.mercadopago.com.ar/papiweb)
- **📧 Contacto:** papiweb.desarrollos@gmail.com

## 🤝 Contribuir

1. Fork del proyecto
2. Crear rama feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🙏 Créditos

- **Desarrollado por:** Papiweb Desarrollos Informáticos
- **Imagen de fondo:** obser.png (imagen astronómica real)
- **Inspiración:** La belleza del cosmos y la divulgación científica

---

**⭐ Si te gusta el proyecto, ¡dale una estrella!**

*Desarrollado con 💛 para la exploración del cosmos*
