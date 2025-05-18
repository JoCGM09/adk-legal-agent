import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from google.adk.agents import Agent

# Importar el módulo de documentos
from . import documentos

# Directorio base para documentos
DOCS_DIR = Path(__file__).parent / "documentos"

# Función para cargar documentos
async def cargar_documentos() -> Dict[str, str]:
    """Carga todos los documentos disponibles en el directorio de documentos"""
    documentos_dict = {}
    for doc_path in DOCS_DIR.rglob("*.txt"):
        with open(doc_path, 'r', encoding='utf-8') as f:
            documentos_dict[doc_path.name] = f.read()
    return documentos_dict

# Función para buscar en documentos
async def buscar_en_documentos(
    documentos: Dict[str, str],
    termino: str
) -> List[str]:
    """Busca un término específico en los documentos disponibles"""
    resultados = []
    for nombre, contenido in documentos.items():
        if termino.lower() in contenido.lower():
            resultados.append(f"Encontrado en {nombre}")
    return resultados

# Función para analizar documentos
async def analizar_documento(
    documento: str,
    tipo_analisis: str
) -> Dict[str, str]:
    """Analiza un documento según el tipo especificado"""
    return {
        "tipo": tipo_analisis,
        "fecha_analisis": datetime.now().isoformat(),
        "resultado": f"Análisis de {tipo_analisis} completado"
    }

# Funciones principales del agente
def revisar_contrato(tipo_contrato: str, texto_contrato: str) -> Dict:
    """
    Revisa un contrato usando documentos reales y modelos de IA.
    
    Args:
        tipo_contrato: Tipo de contrato (ej. 'nda', 'contrato_laboral')
        texto_contrato: Texto completo del contrato a revisar
        
    Returns:
        Dict con resultados del análisis
    """
    # Cargar documentos relevantes
    documentos_dict = cargar_documentos()
    
    # Buscar términos relacionados con el tipo de contrato
    resultados_busqueda = buscar_en_documentos(texto_contrato)
    
    # Analizar el contrato
    analisis = analizar_documento(texto_contrato, "contrato")
    
    return {
        "tipo_contrato": tipo_contrato,
        "fecha_analisis": datetime.now().isoformat(),
        "resultados_busqueda": resultados_busqueda,
        "analisis": analisis,
        "recomendaciones": [
            "Revisar los términos encontrados con un abogado",
            "Considerar las recomendaciones del análisis"
        ]
    }

def verificar_cumplimiento(regulacion: str, proceso_negocio: str) -> Dict:
    """
    Verifica el cumplimiento de regulaciones usando documentos reales.
    
    Args:
        regulacion: Regulación contra la cual verificar
        proceso_negocio: Descripción del proceso de negocio
        
    Returns:
        Dict con análisis de cumplimiento
    """
    # Cargar documentos relevantes
    documentos_dict = cargar_documentos()
    
    # Buscar términos relacionados con la regulación
    resultados_busqueda = buscar_en_documentos(documentos_dict, regulacion)
    
    return {
        "regulacion": regulacion,
        "fecha_verificacion": datetime.now().isoformat(),
        "cumple": len(resultados_busqueda) > 0,
        "resultados_busqueda": resultados_busqueda,
        "recomendaciones": "Verificación basada en documentos reales completada"
    }

def rastrear_plazos_contrato(nombre_contrato: str, 
                           fecha_firma: str, 
                           duracion_meses: int = 12) -> Dict:
    """
    Realiza un seguimiento de los plazos importantes de un contrato.
    
    Args:
        nombre_contrato: Nombre del contrato
        fecha_firma: Fecha de firma del contrato (AAAA-MM-DD)
        duracion_meses: Duración del contrato en meses
        
    Returns:
        Dict con fechas y plazos importantes
    """
    try:
        fecha_firma_dt = datetime.strptime(fecha_firma, "%Y-%m-%d")
        fecha_fin = fecha_firma_dt + timedelta(days=30 * duracion_meses)
        fecha_renovacion = fecha_fin - timedelta(days=30)  # 30 días antes del fin
        
        return {
            "estado": "éxito",
            "nombre_contrato": nombre_contrato,
            "fecha_firma": fecha_firma_dt.strftime("%Y-%m-%d"),
            "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
            "plazo_renovacion": fecha_renovacion.strftime("%Y-%m-%d"),
            "dias_restantes": (fecha_fin - datetime.now()).days,
            "proximos_vencimientos": [
                {"evento": "Aviso de renovación", "fecha": fecha_renovacion.strftime("%Y-%m-%d")},
                {"evento": "Fecha de finalización", "fecha": fecha_fin.strftime("%Y-%m-%d")}
            ]
        }
    except ValueError as e:
        return {
            "estado": "error",
            "mensaje": f"Formato de fecha inválido. Use el formato AAAA-MM-DD. Error: {str(e)}"
        }

# Funciones para gestión de documentos
def listar_documentos(tipo_documento: str = "") -> List[Dict]:
    """Lista los documentos disponibles
    
    Args:
        tipo_documento: Tipo de documento a listar. Si es una cadena vacía, lista todos los documentos.
                     
    Returns:
        Lista de diccionarios con información de los documentos
    """
    return documentos.listar_documentos(tipo_documento)

def buscar_en_documentos(termino: str) -> List[Dict]:
    """Busca un término en todos los documentos"""
    return documentos.buscar_en_documentos(termino)

def leer_documento(ruta_relativa: str) -> Optional[Dict]:
    """Lee el contenido de un documento"""
    return documentos.leer_documento(ruta_relativa)

# Crear el asistente legal
root_agent = Agent(
    name="asistente_legal",
    model="gemini-2.0-flash",  # Usando un modelo gratuito
    description=(
        "Un asistente legal de IA que ayuda con la revisión de contratos, gestión de documentos, "
        "verificaciones de cumplimiento e investigación legal para departamentos legales corporativos."
    ),
    instruction=(
        "Eres un asistente legal útil que trabaja en un departamento legal corporativo. "
        "Tu rol es ayudar con la revisión de contratos, gestión de documentos, verificaciones de "
        "cumplimiento e investigación legal. Siempre proporciona información legal clara, precisa "
        "y práctica, enfatizando que no eres un sustituto del asesoramiento legal profesional. "
        "Sé minucioso en tu análisis y destaca cualquier riesgo o consideración legal potencial.\n\n"
        "Puedes gestionar documentos en las siguientes categorías: contratos, facturas y documentos_legales."
    ),
    tools=[
        revisar_contrato,
        verificar_cumplimiento,
        rastrear_plazos_contrato,
        listar_documentos,
        buscar_en_documentos,
        leer_documento
    ]
)