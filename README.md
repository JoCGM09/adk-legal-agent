# Asistente Legal para Departamentos Jurídicos

Un asistente legal impulsado por IA construido con el Kit de Desarrollo de Agentes (ADK) de Google para ayudar a departamentos legales corporativos con revisión de contratos, verificaciones de cumplimiento e investigación legal.

## Características

- **Revisión de Contratos**: Analiza contratos en busca de problemas comunes y riesgos potenciales
- **Verificación de Cumplimiento**: Verifica procesos de negocio frente a regulaciones como LGPD y CCPA
- **Seguimiento de Plazos**: Realiza un seguimiento de fechas importantes y vencimientos de contratos
- **Investigación Legal**: Obtén información rápida sobre temas legales comunes
- **Gestión Documental**: Organiza y gestiona documentos legales de manera eficiente

## Requisitos Previos

- Python 3.9+
- Google ADK (`pip install google-adk`)
- Clave API de Google (obtén una en [Google AI Studio](https://aistudio.google.com/apikey))

## Estructura del Proyecto

```
legal_assistant/
├── agent.py            # Lógica principal del asistente
├── documentos.py       # Gestión de documentos y estructura de carpetas
├── __init__.py         # Inicialización del paquete
├── README.md           # Este archivo
└── documentos/         # Documentos generados automáticamente
    ├── contratos/      # Contratos de ejemplo
    │   ├── contrato_servicios_tecnologicos_2025.txt
    │   ├── nda_cliente_ejemplo.txt
    │   └── arrendamiento_oficinas_2025.txt
    ├── facturas/       # Facturas de ejemplo
    └── documentos_legales/
        └── politica_privacidad.txt
```

## Documentos Generados

El asistente crea automáticamente los siguientes documentos de ejemplo:

### 1. Contrato de Servicios Tecnológicos
- **Ubicación**: `documentos/contratos/contrato_servicios_tecnologicos_2025.txt`
- **Contenido**: Contrato detallado para servicios tecnológicos que incluye términos de servicio, confidencialidad, propiedad intelectual y condiciones de pago.

### 2. Acuerdo de Confidencialidad (NDA)
- **Ubicación**: `documentos/contratos/nda_cliente_ejemplo.txt`
- **Contenido**: Acuerdo de confidencialidad completo con definiciones, obligaciones y excepciones.

### 3. Contrato de Arrendamiento
- **Ubicación**: `documentos/contratos/arrendamiento_oficinas_2025.txt`
- **Contenido**: Contrato de arrendamiento detallado con términos, condiciones y responsabilidades.

### 4. Política de Privacidad
- **Ubicación**: `documentos/documentos_legales/politica_privacidad.txt`
- **Contenido**: Política de privacidad completa que cumple con regulaciones de protección de datos.

## Configuración

1. Clona este repositorio
2. Instala las dependencias:
   ```bash
   pip install google-adk python-dotenv
   ```
3. Copia `.env.example` a `.env` y añade tu clave API de Google:
   ```
   GOOGLE_API_KEY=tu_clave_api_aquí
   ```
4. Ejecuta el asistente:
   ```bash
   adk web
   ```
5. Abre tu navegador en http://localhost:8000

## Uso de Documentos de Prueba

Los documentos generados automáticamente sirven para:
- Probar las funcionalidades del asistente
- Entender la estructura esperada de los documentos
- Usar como plantillas para nuevos documentos
- Realizar pruebas sin necesidad de documentos confidenciales

Puedes modificar estos documentos o reemplazarlos con tus propios archivos en las carpetas correspondientes.
4. Ejecuta el agente:
   ```
   adk web
   ```
   Luego abre http://localhost:8000 en tu navegador

## Ejemplos de Uso

### 1. Revisión del Contrato de Servicios
```
Revisa el contrato de servicios tecnológicos y destaca las obligaciones del cliente
```

### 2. Análisis de Confidencialidad
```
Analiza el NDA y verifica el período de confidencialidad y las excepciones
```

### 3. Verificación de Cumplimiento
```
¿Nuestra política de privacidad cumple con los requisitos del RGPD y la LGPD?
```

### 4. Búsqueda de Términos
```
Busca menciones de "propiedad intelectual" en todos los contratos
```

### 5. Análisis de Plazos
```
Identifica todas las fechas importantes en el contrato de arrendamiento
```

### 6. Comparación de Documentos
```
Compara las cláusulas de confidencialidad entre el NDA y el contrato de servicios
```

### 7. Generación de Recordatorios
```
Crea recordatorios para las fechas de renovación de todos los contratos
```

## Estructura del Proyecto

- `agent.py`: Implementación principal del agente con herramientas legales
- `.env`: Archivo de configuración para claves API
- `__init__.py`: Inicialización del paquete

## Limitaciones

Esta es una aplicación de demostración y no sustituye el asesoramiento legal profesional. Siempre consulta con un abogado calificado para asuntos legales.
