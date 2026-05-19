# Design Web de Alta Qualidade — Referência

Baseado nos princípios da skill `frontend-design` da Anthropic (214k installs no skills.sh) e adaptado para sites de pequenos negócios locais no Brasil.

---

## O Problema que Esta Referência Resolve

Quando uma IA gera um site sem direção de design, o resultado é sempre o mesmo: fundo branco, gradiente roxo, fonte Inter ou Roboto, layout em 3 colunas com ícones de Feature Cards. Isso não vende para ninguém.

Sites de negócios locais (dentistas, médicos, clínicas) precisam de design que transmita **confiança, modernidade e localidade** — não parece template SaaS.

---

## Antes de Codar: Defina a Direção Visual

Antes de escrever uma linha de CSS, responda:

1. **Quem é o público?** Pacientes locais, família, profissionais? (Determina tom: acolhedor vs. técnico)
2. **O que diferencia esse negócio?** Localização, especialidade, equipe, tecnologia, preço?
3. **Qual sensação o site deve transmitir?** Exemplos: "clínica limpa e moderna", "consultório humanizado", "especialista de referência"
4. **Tem identidade visual existente?** Logo, cores? Use como ponto de partida.

Sem responder isso, qualquer design é genérico.

---

## Tipografia

### A regra mais importante

**Nunca use Inter, Roboto, Arial ou Helvetica como fonte principal.** Essas fontes são boas mas associadas a "site de IA" / "template gratuito". Escolha algo que tenha caráter.

### Combinações que funcionam para negócios locais de saúde

| Display (headlines) | Body (texto corrido) | Sensação |
|--------------------|---------------------|----------|
| Playfair Display | Lato | Elegante, premium |
| Merriweather | Source Sans Pro | Confiável, tradicional |
| Nunito | Open Sans | Acolhedor, amigável |
| DM Serif Display | DM Sans | Moderno, limpo |
| Cormorant Garamond | Jost | Sofisticado, luxo |

### Como aplicar no Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
```

### Escala tipográfica

```css
:root {
  --font-display: 'Playfair Display', serif;
  --font-body: 'Lato', sans-serif;
  
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;
  --text-4xl: 2.5rem;
  --text-5xl: 3.5rem;
}

h1 { font-family: var(--font-display); font-size: var(--text-5xl); line-height: 1.1; }
h2 { font-family: var(--font-display); font-size: var(--text-3xl); }
p  { font-family: var(--font-body); font-size: var(--text-base); line-height: 1.7; }
```

---

## Paleta de Cores

### Para saúde/clínicas: paletas que funcionam

**Opção 1 — Azul-Tiffany Profissional**
```css
--primary: #2D6A8E;     /* Azul médico profissional */
--primary-light: #E8F4F8;
--accent: #F0A500;      /* Dourado quente — confiança */
--text: #1A1A2E;
--bg: #FAFAFA;
```

**Opção 2 — Verde Saúde Moderno**
```css
--primary: #2E7D52;     /* Verde saúde saturado */
--primary-light: #E8F5EE;
--accent: #FF6B35;      /* Laranja — urgência suave */
--text: #1C2B2D;
--bg: #F8FFFE;
```

**Opção 3 — Coral Humanizado**
```css
--primary: #C94B4B;     /* Coral-vermelho — medicina, urgência */
--primary-light: #FDF2F2;
--accent: #2D4A6E;      /* Azul navy — confiança */
--text: #222;
--bg: #FFFAF9;
```

### Regras de uso

- Cor primária: headlines, botões principais, bordas de destaque
- Cor primária light: backgrounds de seções alternadas
- Accent: apenas 1 elemento por seção (badge, número, ícone)
- Máximo 3 cores + branco/cinza + preto

---

## Layout e Composição

### Mobile-first obrigatório

60%+ do tráfego de pequenos negócios vem de mobile. Layout quebrado no celular = cliente perdido.

```css
/* Mobile first */
.container {
  width: 100%;
  padding: 0 1.25rem;
}

/* Tablet */
@media (min-width: 768px) {
  .container { max-width: 720px; margin: 0 auto; }
}

/* Desktop */
@media (min-width: 1200px) {
  .container { max-width: 1140px; }
}
```

### Evite o grid de 3 colunas padrão

O grid `display: grid; grid-template-columns: repeat(3, 1fr)` é o sinal mais claro de "template genérico". Alternativas:

- Seções assimétricas (60/40 em vez de 50/50)
- Cards com alturas variadas
- Linha do tempo vertical
- Layout em zigzag (imagem esquerda/direita alternando)

### Hero section que converte

```html
<section class="hero">
  <!-- Não: "Bem-vindo à Clínica X" -->
  <!-- Sim: headline orientada a resultado -->
  <h1>Seu Sorriso Merece<br>Cuidado de Verdade</h1>
  <p>Tratamentos modernos, ambiente acolhedor e atendimento humanizado em [cidade].</p>
  <a href="https://wa.me/NUMERO" class="btn-primary">
    📱 Agendar pelo WhatsApp
  </a>
</section>
```

---

## Micro-animações com CSS Puro

Animações sutis aumentam percepção de qualidade sem JavaScript pesado.

```css
/* Fade in ao scroll — usando Intersection Observer */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Hover em cards */
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.1);
}

/* Botão pulsante para WhatsApp */
@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.4); }
  50%       { box-shadow: 0 0 0 12px rgba(37, 211, 102, 0); }
}
.btn-whatsapp {
  animation: pulse 2s infinite;
}
```

```js
// Intersection Observer para fade-in no scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(el => {
    if (el.isIntersecting) el.target.classList.add('visible');
  });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
```

---

## Componentes Essenciais para Negócios Locais

### Botão WhatsApp Fixo (mobile)

```css
.whatsapp-fixed {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #25D366;
  color: white;
  border-radius: 50px;
  padding: 14px 20px;
  font-weight: 700;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 8px;
}
```

```html
<a href="https://wa.me/NUMERO?text=Olá!%20Vim%20pelo%20site%20e%20gostaria%20de%20agendar."
   class="whatsapp-fixed" target="_blank">
  💬 Fale Conosco
</a>
```

### Cards de Serviço com Ícone

```html
<div class="services-grid">
  <div class="service-card fade-in">
    <div class="service-icon">🦷</div>
    <h3>Clareamento Dental</h3>
    <p>Sorria com confiança. Protocolo profissional com resultados visíveis em 1 sessão.</p>
    <a href="#contato">Saiba mais →</a>
  </div>
</div>
```

### Seção de Prova Social

```html
<section class="social-proof">
  <div class="stat-grid">
    <div class="stat">
      <span class="stat-number">+2.000</span>
      <span class="stat-label">Pacientes Atendidos</span>
    </div>
    <div class="stat">
      <span class="stat-number">15 anos</span>
      <span class="stat-label">de Experiência</span>
    </div>
    <div class="stat">
      <span class="stat-number">4.9 ⭐</span>
      <span class="stat-label">no Google</span>
    </div>
  </div>
</section>
```

---

## Schema Markup para Saúde Local

Sempre inclua no `<head>` do site:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "name": "[NOME DA CLÍNICA]",
  "description": "[DESCRIÇÃO CURTA]",
  "url": "https://[URL]",
  "telephone": "[TELEFONE]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[RUA E NÚMERO]",
    "addressLocality": "[CIDADE]",
    "addressRegion": "[ESTADO]",
    "addressCountry": "BR"
  },
  "openingHours": ["Mo-Fr 08:00-18:00", "Sa 08:00-12:00"],
  "image": "[URL_FOTO]",
  "priceRange": "$$",
  "sameAs": [
    "https://www.instagram.com/[HANDLE]",
    "https://www.facebook.com/[HANDLE]"
  ]
}
</script>
```

Para médicos, use `"@type": "Physician"` com `"medicalSpecialty": "[ESPECIALIDADE]"`.

Para clínicas genéricas, use `"@type": "MedicalOrganization"`.

---

## Acessibilidade — WCAG 2.1 AA (obrigatório)

Roubado da skill `accessibility-review`. Sites acessíveis rankeiam melhor, convertem mais e evitam problemas legais.

### Contraste mínimo obrigatório
| Tipo de elemento | Ratio mínimo | Como verificar |
|-----------------|--------------|----------------|
| Texto normal (< 18px) | **4.5:1** | Use [contrast-ratio.com](https://contrast-ratio.com) |
| Texto grande (≥ 18px ou ≥ 14px bold) | **3:1** | Mais fácil de passar |
| Elementos UI (botões, inputs, ícones) | **3:1** | Borda do botão vs. fundo |

### Regra dos contrastes para as paletas de saúde
```
Opção 1 (Azul): #2D6A8E em #FFFFFF → ratio 5.2:1 ✅
Opção 2 (Verde): #2E7D52 em #FFFFFF → ratio 5.8:1 ✅
Opção 3 (Coral): #C94B4B em #FFFFFF → ratio 4.6:1 ✅

CUIDADO: Texto branco em fundo claro FALHA
#FFFFFF em #E8F4F8 (primary-light) → ratio 1.1:1 ❌ — use texto escuro nesses fundos
```

### Touch targets (mobile — obrigatório)
```css
/* Todo elemento clicável deve ter pelo menos 44×44px */
.btn, a, button, input, select {
  min-height: 44px;
  min-width: 44px;
  /* Para links inline, adicione padding */
  padding: 12px 20px;
}

/* Links de navegação no mobile */
nav a {
  display: block;
  padding: 12px 16px; /* garante área de toque */
}
```

### Foco visível (acessibilidade de teclado)
```css
/* Nunca remova outline sem substituir */
:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 3px;
  border-radius: 3px;
}

/* Estilo customizado para botões */
.btn:focus-visible {
  box-shadow: 0 0 0 3px rgba(45, 106, 142, 0.4);
  outline: none;
}
```

### Alt text em imagens (padrão)
```html
<!-- Foto real da clínica/equipe -->
<img src="clinica.jpg" alt="Sala de atendimento da Clínica X em Curitiba, ambiente moderno e climatizado">

<!-- Foto do profissional -->
<img src="dr-silva.jpg" alt="Dr. Carlos Silva, cirurgião-dentista especialista em implantes, CRO-PR 12345">

<!-- Imagem decorativa (não precisa de alt) -->
<img src="linha-divisoria.svg" alt="" role="presentation">
```

---

## Framework de Crítica Visual (2 segundos)

Baseado na skill `design-critique`. Ao revisar o HTML gerado, faça estes checks:

### Teste dos 5 segundos
1. O **H1** é a primeira coisa que o olho vê?
2. O **CTA principal** está visível sem scroll no mobile?
3. É imediatamente claro **o que a empresa faz**?
4. A **hierarquia visual** guia: headline → benefício → ação?
5. Parece uma empresa **real e confiável** ou um template genérico?

### Verificação de hierarquia
```
✅ CORRETO — ordem de peso visual:
H1 (maior, cor primária) > CTA button (cor de destaque) > H2 (médio) > Corpo (menor)

❌ PROBLEMA — elementos que competem:
- CTA da mesma cor que texto comum
- H1 menor que logo da empresa
- 3 botões com mesmo peso visual na mesma seção
```

### Checklist de consistência
- [ ] Espaçamento segue padrão (múltiplos de 8px: 8, 16, 24, 32, 48, 64)
- [ ] Mesma família de fonte para headings em todas as seções
- [ ] Raio de borda (`border-radius`) consistente nos cards e botões
- [ ] Sombras consistentes (um padrão para cards, outro para modais)
- [ ] Espaçamento entre seções consistente (recomendo 80-120px no desktop, 48-64px mobile)

---

## Checklist Final Antes de Entregar

Antes de passar para a Fase 3 (deploy), verifique:

**SEO e GEO:**
- [ ] Title tag: 50-60 chars, inclui keyword + cidade
- [ ] Meta description: 150-160 chars, tem CTA implícito
- [ ] H1 único e orientado a benefício
- [ ] JSON-LD schema correto para o tipo de negócio
- [ ] Schema FAQPage com 5+ perguntas
- [ ] Canonical tag presente
- [ ] Open Graph tags (og:title, og:description, og:image)
- [ ] Meta viewport presente

**Design e UX:**
- [ ] Google Fonts carregando com `display=swap`
- [ ] Contraste WCAG AA: texto normal ≥ 4.5:1, texto grande ≥ 3:1
- [ ] Touch targets ≥ 44×44px em todos os elementos clicáveis
- [ ] WhatsApp visível acima da dobra no mobile
- [ ] Botão WhatsApp fixo flutuante
- [ ] Foco visível em elementos interativos

**Copy e Conteúdo:**
- [ ] Imagens com `alt` text descritivo
- [ ] CTAs usam verbos de ação (não "Saiba mais")
- [ ] Pelo menos 1 depoimento com nome e transformação
- [ ] NAP (nome, endereço, telefone) visível em texto

**Técnico:**
- [ ] Testar no mobile (375px — iPhone padrão)
- [ ] Testar em 320px (mínimo histórico)
- [ ] Nenhum erro no console do browser
- [ ] Imagens com tamanho razoável (< 200KB cada)
