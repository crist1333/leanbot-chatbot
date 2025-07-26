# 🤖 LeanBot – Asistente Virtual para INGELEAN

LeanBot es un chatbot inteligente desarrollado para INGELEAN S.A.S., una empresa de ingeniería ubicada en Pereira, Risaralda. Su objetivo es mejorar la atención al cliente respondiendo preguntas frecuentes de manera automática, rápida y clara.

## 📍 Descripción

Este proyecto busca reducir los tiempos de respuesta en el servicio al cliente y ofrecer una experiencia de atención más eficiente, personalizada y disponible 24/7.

---

## 🧠 Funcionalidades

| Nivel       | Funcionalidad                            | Implementado |
|-------------|------------------------------------------|--------------|
| Básico      | Respuestas a FAQ predefinidas            | ✅ Sí         |
| Básico      | Manejo de múltiples usuarios (simulado)  | ✅ Sí         |
| Intermedio  | Comprensión de intención (básica)        | ⚠️ Parcial    |
| Intermedio  | Manejo de contexto                       | ❌ No         |
| Intermedio  | Integración con API externa              | ❌ No         |
| Avanzado    | Análisis de sentimiento                  | ❌ No         |
| Avanzado    | Dashboard analítico                      | ❌ No         |
| Avanzado    | Registro con trazabilidad                | ❌ No         |

---

## ⚙️ Tecnologías utilizadas

- **Motor de IA / NLP**: Algoritmo basado en `difflib.get_close_matches` (NLP simple)
- **Lenguajes**: Python (Flask), JavaScript, HTML y CSS
- **Entorno local**: PyCharm / VSCode
- **Despliegue actual**: Localhost (http://localhost:5050)
- **APIs utilizadas**: —
- **Otras herramientas**: GitHub, Postman

---

## 🗂️ Estructura del Proyecto

leanbot-chatbot/
│
├── backend/
│ ├── app.py # Servidor Flask
│ ├── chatbot.py # Lógica de respuesta
│ └── faq.json # Base de conocimientos (FAQs)
│
├── frontend/
│ ├── index.html # Interfaz del chatbot
│ ├── styles.css # Estilos básicos
│ └── script.js # Envío de mensajes y respuestas
│
├── README.md # Este archivo
└── requirements.txt # Dependencias del proyecto

yaml
Copiar
Editar



---

## ✅ Requisitos para correr el proyecto

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate   # En Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar backend
cd backend
python app.py
