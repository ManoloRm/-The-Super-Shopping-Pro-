# -The-Super-Shopping-Pro-
# 🛒 Web Automation Framework: SauceDemo Project

Este proyecto es un framework de automatización de pruebas de extremo a extremo (E2E) diseñado para la plataforma **SauceDemo**. El objetivo principal es demostrar habilidades sólidas en arquitectura de pruebas, manejo de esperas asíncronas y validaciones de lógica de negocio en una aplicación e-commerce.

## 🚀 Alcance del Proyecto
Se automatizaron los flujos críticos de la aplicación, incluyendo:
* **Autenticación:** Pruebas de login exitoso, logout y manejo de usuarios bloqueados.
* **Flujo de Compra:** Selección dinámica de productos, gestión del carrito y validación de badges.
* **Validación de Datos:** Verificación de cálculos de impuestos y montos totales en el checkout mediante lógica programática.

## 🛠️ Stack Tecnológico
* **Herramienta Core:** [Playwright / Cypress / Selenium - *Elige uno*] 
* **Lenguaje:** [Python]
* **Patrón de Diseño:** **Page Object Model (POM)** para mejorar la legibilidad y el mantenimiento.
* **Reportes:** Integración con [Allure Reports / Reporte Nativo].

## 🏗️ Arquitectura
El proyecto sigue una estructura modular para separar la lógica de la prueba de los selectores de la interfaz de usuario:
```text
├── pages/       # Clases con selectores y acciones (Page Objects)
├── tests/       # Scripts de prueba organizados por suites
├── data/        # Archivos JSON para parametrización de datos
└── utils/       # Funciones auxiliares y configuraciones globales
