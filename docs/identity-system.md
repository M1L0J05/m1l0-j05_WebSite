# Sistema de Identidad Visual

## Wordmark

El handle **M1L0_J05** es el activo principal de marca. Identidad 100% tipográfica.

### Variantes

| Variante | Contexto |
|---|---|
| `>_ M1L0_J05█` | Hero section, OG image |
| `M1L0_J05` | Navbar compacto |
| `m1l0_j05` | Footer, bio, menú móvil |
| `M1L0` | Avatar, favicon, iconos sociales |

### Especificación técnica

- **Fuente:** JetBrains Mono ExtraBold (800)
- **Color:** `#00B4D8` (cian eléctrico)
- **Prefijo:** `>_` en gris `#8B949E` (prompt de terminal)
- **Cursor:** `█` animado con CSS keyframes `blink 1s step-end infinite`
- **Tamaño:** 48px desktop, 32px mobile

---

## Paleta de colores

Filosofía: **dark-first**, optimizada para glassmorphism, contraste WCAG AA y coherencia
con interfaces CLI.

### Tokens

| Token | Hex | Uso |
|---|---|---|
| `bg-base` | `#0D1117` | Fondo raíz |
| `bg-card` | `#161B22` | Cards, panels |
| `bg-elevated` | `#1C2128` | Tooltips, modales |
| `accent-cyan` | `#00B4D8` | CTA, links, glow, wordmark |
| `accent-orange` | `#FF6B2B` | Hover states, badges activos |
| `accent-green` | `#3FB950` | Estado online, deploys activos |
| `text-primary` | `#E6EDF3` | Texto principal |
| `text-secondary` | `#8B949E` | Metadatos, fechas, labels |
| `border` | `#30363D` | Divisores, bordes de card |
| `error` | `#F85149` | Alertas, errores |

### Glassmorphism (CSS)

```css
/* Card base */
background: rgba(22, 27, 34, 0.6);
backdrop-filter: blur(12px);
border: 1px solid rgba(48, 54, 61, 0.8);
border-radius: 12px;

/* Hover glow */
box-shadow: 0 0 20px rgba(0, 180, 216, 0.15);
transition: box-shadow 0.3s ease;
```

**Fallback** (navegadores sin `backdrop-filter`):
```css
background: rgba(22, 27, 34, 0.95);
```

---

## Tipografía

Tres familias con roles definidos. **Self-hosted** en formato woff2.

### Jerarquía

| Nivel | Fuente | Peso | Uso |
|---|---|---|---|
| Display | JetBrains Mono | 800 | Wordmark, bloques código |
| H1-H2 | Outfit | 700 | Títulos de sección |
| H3-H4 | Outfit | 500 | Subtítulos, nombres proyecto |
| Body | Inter | 400 | Texto corrido |
| Labels | JetBrains Mono | 400 | Tags, badges, versiones |
| Code | JetBrains Mono | 400 | Comandos, variables |

### Escala (rem)

| Nivel | Tamaño | Px equivalente |
|---|---|---|
| Display | 3.5rem | 56px |
| H1 | 2.5rem | 40px |
| H2 | 1.75rem | 28px |
| H3 | 1.25rem | 20px |
| Body | 1rem | 16px |
| Small | 0.875rem | 14px |
| Micro | 0.75rem | 12px |

### Regla de oro

- **Identidad técnica** (handle, stack tags, código) → JetBrains Mono
- **Contenido narrativo** (títulos, descripciones, textos) → Outfit / Inter

---

## Taglines

| Contexto | Texto |
|---|---|
| Hero principal | Building systems. Automating the rest. |
| SEO / Meta | Full-Stack Engineer · DevOps · Infrastructure Architect — Sevilla, ES |
| Bio corta | I build the backend, the infra, and the pipelines that run on top. |

## UVP

> "Diseño y construyo sistemas completos — desde la capa de aplicación hasta la
> orquestación de infraestructura. Python, contenedores, Kubernetes y automatización
> de pipelines."

---

## Favicon

- **Contenido:** "M1" en JetBrains Mono Bold
- **Color texto:** `#00B4D8`
- **Fondo:** `#0D1117`
- **Tamaños:** 16x16, 32x32, 180x180 (apple-touch), 512x512 (PWA)
- **Formato:** SVG fuente → PNG exports

## OG Image

- **Dimensiones:** 1200x630px
- **Fondo:** `#0D1117`
- **Wordmark centrado:** `#00B4D8`, 72px
- **Tagline debajo:** `#E6EDF3`, 32px
- **Borde exterior:** cian 4px
