# 📋 Instrucciones de Deploy - GitHub Pages

## 🚀 Pasos para Deploy

### 1. Verificar Archivos
```bash
# Ejecutar script de verificación
./deploy.sh
```

### 2. Commit y Push
```bash
# Añadir todos los archivos
git add .

# Crear commit
git commit -m "🚀 Deploy: GitHub Pages ready with 24 solar system modes"

# Subir a GitHub
git push origin main
```

### 3. Configurar GitHub Pages

1. **Ir a tu repositorio en GitHub**
2. **Settings** → **Pages** (en el menú lateral)
3. **Source:** Deploy from a branch
4. **Branch:** main
5. **Folder:** /docs
6. **Save**

### 4. Verificar Deploy

- El sitio estará disponible en: `https://TU-USUARIO.github.io/NOMBRE-REPO`
- GitHub enviará una notificación cuando esté listo
- El proceso puede tomar 5-10 minutos

## 🔧 Configuración Opcional

### Dominio Personalizado
```bash
# Crear archivo CNAME (opcional)
echo "tudominio.com" > docs/CNAME
```

### Variables de Entorno GitHub
- No necesarias para este proyecto
- Todo está configurado en archivos estáticos

## ✅ Checklist Pre-Deploy

- [ ] Archivo `docs/index.html` presente
- [ ] Archivos estáticos copiados en `docs/static/`
- [ ] Archivo `.nojekyll` presente
- [ ] Videos de demo incluidos
- [ ] Imagen de fondo `obser.png` presente
- [ ] Favicons configurados
- [ ] README actualizado
- [ ] GitHub Actions configurado

## 🌐 URLs Importantes

- **Sitio:** https://papiweb-desarrollos.github.io/system
- **Repo:** https://github.com/papiweb-desarrollos/system
- **Donaciones:** https://link.mercadopago.com.ar/papiweb

## 🎯 Resultado Esperado

Una página web estática moderna que muestra:
- ✨ 24 modos de visualización del sistema solar
- 🎬 Videos de demostración integrados
- 🌌 Fondo astronómico (obser.png)
- 📱 Diseño responsive
- 💳 Enlaces de contacto y donación

---
*Papiweb Desarrollos Informáticos - 2025*
