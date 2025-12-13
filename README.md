# 🧠🎥 Sistema Experimental - IA de Reconhecimento Comportamental Multimodal

> **Status geral:** 🚧 Em desenvolvimento

Projeto experimental focado na detecção de padrões emocionais a partir da análise **visual (expressões faciais / microexpressões)** e, futuramente, **auditiva (características da fala)**, utilizando Visão Computacional e Machine Learning.

> ⚠️ **Nota importante:** este sistema **não determina verdades absolutas** (ex.: culpa ou mentira). Ele atua como uma **ferramenta de apoio**, destacando padrões, correlações e variações emocionais ao longo do tempo.

---

## 🎯 Objetivo do Projeto

Desenvolver uma pipeline modular e escalável para:

* Detectar e rastrear rostos em imagens e vídeos
* Extrair landmarks faciais
* Identificar microexpressões e variações temporais
* Correlacionar sinais visuais e sonoros
* Apoiar análises comportamentais em contextos investigativos e experimentais

---

## 🧩 Arquitetura Geral (Roadmap Técnico)

### 🔹 Fase 0 – Setup do Ambiente

* [x] Python 3.x
* [x] Ambiente virtual (venv)
* [x] OpenCV
* [x] MediaPipe
* [ ] TensorFlow / Keras

---

### 🔹 Fase 1 – Detecção Facial 🎯

> **Status:** 🚧 *Em desenvolvimento*

Objetivo: identificar rostos em tempo real a partir de vídeo.

* [x] Captura de vídeo (webcam / arquivo)
* [x] Detecção de rosto
* [x] Bounding box
* [x] Score de confiança
* [ ] Estabilização de FPS
* [ ] Testes em diferentes condições de iluminação

Tecnologias:

* OpenCV
* MediaPipe (Face Detection)

---

### 🔹 Fase 2 – Landmarks Faciais

> **Status:** ⏳ Planejado

Objetivo: mapear pontos-chave do rosto para análise geométrica.

* [ ] Face Mesh (468 landmarks)
* [ ] Normalização de coordenadas
* [ ] Rastreamento temporal dos pontos
* [ ] Persistência dos dados por frame

---

### 🔹 Fase 3 – Extração de Features

> **Status:** ⏳ Planejado

Objetivo: transformar landmarks em dados mensuráveis.

Exemplos de features:

* Abertura dos olhos
* Elevação das sobrancelhas
* Assimetria facial
* Frequência de piscadas
* Microvariações rápidas (microexpressões)

---

### 🔹 Fase 4 – Machine Learning

> **Status:** 🔮 Futuro

Objetivo: identificar padrões emocionais a partir dos dados extraídos.

* [ ] Datasets públicos (FER2013, CK+, AffectNet)
* [ ] CNN para expressões estáticas
* [ ] Modelos temporais (LSTM / Temporal CNN)
* [ ] Avaliação de viés e incerteza

---

### 🔹 Fase 5 – Análise Multimodal (Vídeo + Áudio)

> **Status:** 🧪 Experimental

Objetivo: correlacionar expressões faciais com características da fala.

* [ ] Extração de pitch, jitter, shimmer
* [ ] MFCCs
* [ ] Alinhamento temporal áudio-vídeo
* [ ] Correlação de eventos emocionais

---

## 🛠️ Tecnologias Utilizadas

* Python
* OpenCV
* MediaPipe
* TensorFlow / Keras
* NumPy
* Matplotlib

---

## ⚠️ Limitações e Considerações Éticas

* Emoções não são determinísticas
* Forte dependência de iluminação e qualidade do vídeo
* Viés de datasets
* Interpretação final deve ser humana

---

## 📌 Status Atual

* Projeto em fase inicial
* Foco atual: **detecção facial estável e confiável**

---

## 📜 Licença

Este projeto é experimental e educacional. Uso por conta e risco.

---

> "Não buscamos verdades absolutas, mas padrões que merecem atenção."
