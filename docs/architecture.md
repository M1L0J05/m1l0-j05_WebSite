# Arquitectura del Sitio

## Navegación

Modelo **híbrido**: SPA con anclas en la página principal + rutas dedicadas para detalle
de proyectos.

```
milo-jos.es/
├── #hero          → Wordmark + Terminal whoami + CTA
├── #stack         → Skills por capas técnicas
├── #proyectos     → Grid de cards
├── #sobre-mi      → Bio + timeline
└── #contacto      → Email + redes + disponibilidad

/proyectos/:id     → Página detalle individual (opcional)
```

---

## Estructura de archivos

```
milo-jos/                           # Directorio del proyecto v2.0
├── rxconfig.py                     # Configuración Reflex
├── requirements.txt                # Dependencias Python
├── .env.example                    # Variables de entorno (plantilla)
├── .gitignore
├── .dockerignore
├── Dockerfile                      # Multi-stage, ARM64
├── Caddyfile                       # Reverse proxy + HTTPS
├── compose.yaml                    # Orquestación Docker
├── deploy.sh                       # Script de deploy manual
│
├── assets/
│   ├── fonts/                      # Fuentes self-hosted (woff2)
│   ├── images/
│   │   ├── root/                   # Favicon, OG image
│   │   └── projects/               # Screenshots proyectos
│   └── data/
│       └── projects.json           # Datos de proyectos
│
├── milo_jos/                       # Paquete Python principal
│   ├── __init__.py
│   ├── version.py                  # __version__ = "2.0.0"
│   ├── milo_jos.py                 # Punto de entrada, registro de rutas
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── index.py                # SPA principal (ensambla secciones)
│   │   └── project_detail.py       # Ruta dinámica /proyectos/:id
│   │
│   ├── sections/                   # Bloques visuales de la SPA
│   │   ├── __init__.py
│   │   ├── hero.py
│   │   ├── stack.py
│   │   ├── projects.py
│   │   ├── about_me.py
│   │   └── contact.py
│   │
│   ├── components/                 # Componentes UI reutilizables
│   │   ├── __init__.py
│   │   ├── navbar.py
│   │   ├── footer.py
│   │   ├── badge.py
│   │   ├── button.py
│   │   ├── card.py
│   │   ├── timeline.py
│   │   └── terminal.py
│   │
│   ├── templates/
│   │   ├── __init__.py
│   │   └── template.py             # Layout base: navbar + contenido + footer
│   │
│   ├── styles/
│   │   ├── __init__.py
│   │   ├── colors.py               # 10 tokens de color
│   │   ├── fonts.py                # 3 familias, escala rem
│   │   ├── styles.py               # BASE_STYLES, glassmorphism, breakpoints
│   │   └── animations.py           # Keyframes CSS (blink, typewriter, glow)
│   │
│   └── utils/
│       ├── __init__.py
│       └── constants.py            # Constantes de la aplicación
│
└── tests/
    ├── conftest.py
    ├── test_sections.py
    └── test_data.py
```

**Criterio de separación:**
- `pages/` → Solo rutas reales registradas en Reflex
- `sections/` → Bloques visuales que componen la SPA (sin ruta propia)
- `components/` → Piezas UI reutilizables en cualquier sección

---

## Componentes UI

### Navbar
- Posición: sticky top, 64px desktop / 56px mobile
- Glassmorphism: `backdrop-filter: blur(16px)` al scroll
- Wordmark `>_ M1L0_J05` a la izquierda
- Items: Stack · Proyectos · Sobre Mí · Contacto (scroll a anclas)
- CTA derecha: botón outline cian "Contactar"
- Mobile: drawer lateral con fondo `#0D1117`

### Footer
- Links: GitHub, LinkedIn, Gitea
- Copyright dinámico: `2023-{year}`
- Versión importada desde `version.py`

### Badge
- Fuente: JetBrains Mono, 0.75rem, uppercase
- Fondo: `rgba(0, 180, 216, 0.1)`, borde cian 30%
- Hover: borde cian 60% + `scale(1.05)`, transición 200ms

### Button
- **Primario (CTA):** Fondo `#00B4D8`, texto `#0D1117`, hover brightness 1.15 + glow
- **Secundario:** Transparent, borde `#00B4D8`, hover fondo cian 10%
- Ambos: Outfit 600, padding 12x28, border-radius 8px

### Card (proyecto)
- Glassmorphism base (ver identity-system.md)
- Hover: glow cian + `translateY(-4px)`, transición 300ms
- Contenido: badge estado, nombre, descripción, stack badges, botones

### Timeline
- Línea vertical: 2px, `#30363D`
- Dot estándar: 12px, fondo `#30363D`, borde 2px `#00B4D8`
- Dot activo: 16px, fondo `#00B4D8`, glow pulsante 2s infinite
- Fecha: JetBrains Mono 0.875rem, `#8B949E`

### Terminal
- Fondo: `#0D1117`, borde `#30363D`, border-radius 8px
- Prompt: `$` en `#3FB950`, comandos en `#E6EDF3`
- Output: `#8B949E`
- Typewriter: 60ms por carácter (CSS animation)

---

## Secciones

### Hero (`#hero`)
- Layout: viewport completo, centrado vertical
- Fondo: gradiente CSS animado (no SVG)
- Contenido: wordmark → tagline → terminal whoami → 2 CTAs
- Scroll indicator: flecha con bounce CSS

### Stack (`#stack`)
- Layout: 4 columnas desktop → 2 tablet → 1 mobile
- 4 capas: Frontend, Backend, Infra/DevOps, Automation
- Cada capa: icono + badges tech monospace

### Proyectos (`#proyectos`)
- Layout: grid 2 cols desktop → 1 mobile
- Cards con badge estado: `EN DESARROLLO` / `PRODUCCIÓN` / `LAB`
- Proyectos: Minerva, Ares, Proxmox Lab, slot "coming soon"
- Datos desde `assets/data/projects.json`

### Sobre Mí (`#sobre-mi`)
- Layout: 2 columnas (bio izquierda, timeline derecha)
- Bio profesional (sin "entusiasta y apasionado")
- Timeline: 2023 → 2026 (presente)

### Contacto (`#contacto`)
- Layout: minimalista, centrado
- Email directo (sin formulario)
- Links: GitHub, LinkedIn, Gitea
- Badge disponibilidad: `Abierto a proyectos freelance`

---

## Responsive (breakpoints)

| Nombre | Rango | Columnas grid |
|---|---|---|
| Mobile | 320px – 767px | 1 |
| Tablet | 768px – 1023px | 2 |
| Desktop | 1024px – 1439px | 3-4 |
| Desktop XL | 1440px+ | 4 |
