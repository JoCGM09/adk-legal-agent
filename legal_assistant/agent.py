import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from google.adk.agents import Agent

# Importar el módulo de documentos
from . import documentos

# Base de datos legal (en una aplicación real, esto estaría conectado a una base de datos)
BASE_DE_DATOS_LEGAL = {
    "nda": {
        "terminos_estandar": {
            "periodo_confidencialidad": "2 años",
            "ley_aplicable": "Estado de California, EE. UU.",
            "jurisdiccion": "Tribunales de California"
        },
        "problemas_comunes": [
            "Definiciones de confidencialidad demasiado amplias",
            "Uso ilimitado de información confidencial",
            "Exclusiones vagas de confidencialidad"
        ]
    },
    "contrato_laboral": {
        "terminos_estandar": {
            "periodo_preaviso": "30 días",
            "duracion_no_competencia": "1 año",
            "propiedad_intelectual": "La empresa posee toda la PI relacionada con el trabajo"
        },
        "problemas_comunes": [
            "Cláusulas de no competencia excesivamente restrictivas",
            "Términos de cesión de PI poco claros",
            "Condiciones de terminación vagas"
        ]
    }
}

# Base de conocimiento legal (en una aplicación real, esto sería más completo)
BASE_DE_CONOCIMIENTO_LEGAL = {
    "lgpd": {
        "resumen": "La Ley General de Protección de Datos (LGPD) es una regulación brasileña sobre protección de datos personales y privacidad.",
        "requisitos_clave": [
            "Derecho al olvido",
            "Portabilidad de datos",
            "Notificación de violación de datos en 72 horas",
            "Privacidad desde el diseño"
        ]
    },
    "ccpa": {
        "resumen": "La Ley de Privacidad del Consumidor de California (CCPA) es un estatuto estatal que mejora los derechos de privacidad y protección del consumidor para residentes de California, Estados Unidos.",
        "requisitos_clave": [
            "Derecho a saber qué datos personales se recopilan",
            "Derecho a eliminar datos personales",
            "Derecho a optar por no vender datos",
            "Derecho a no sufrir discriminación"
        ]
    }
}

def revisar_contrato(tipo_contrato: str, texto_contrato: str) -> Dict:
    """
    Revisa un contrato e identifica posibles problemas según el tipo de contrato.
    
    Args:
        tipo_contrato: Tipo de contrato (ej. 'nda', 'contrato_laboral')
        texto_contrato: Texto completo del contrato a revisar
        
    Returns:
        Dict con resultados de la revisión, problemas potenciales y recomendaciones
    """
    if tipo_contrato.lower() not in BASE_DE_DATOS_LEGAL:
        return {
            "estado": "error",
            "mensaje": f"Tipo de contrato no soportado. Tipos soportados: {', '.join(BASE_DE_DATOS_LEGAL.keys())}"
        }
    
    info_contrato = BASE_DE_DATOS_LEGAL[tipo_contrato.lower()]
    
    # En una aplicación real, esto implicaría un análisis de PNL más sofisticado
    problemas_encontrados = []
    for problema in info_contrato["problemas_comunes"]:
        if any(palabra in texto_contrato.lower() for palabra in problema.lower().split()):
            problemas_encontrados.append(problema)
    
    return {
        "estado": "éxito",
        "tipo_contrato": tipo_contrato,
        "terminos_estandar": info_contrato["terminos_estandar"],
        "problemas_encontrados": problemas_encontrados if problemas_encontrados else ["No se detectaron problemas obvios"],
        "recomendaciones": [
            "Haga revisar el contrato por un abogado calificado antes de firmar",
            "Considere negociar los términos resaltados"
        ]
    }

def verificar_cumplimiento(regulacion: str, proceso_negocio: str) -> Dict:
    """
    Verifica si un proceso de negocio cumple con las regulaciones especificadas.
    
    Args:
        regulacion: Regulación contra la cual verificar (ej. 'lgpd', 'ccpa')
        proceso_negocio: Descripción del proceso de negocio a verificar
        
    Returns:
        Dict con análisis de cumplimiento y recomendaciones
    """
    regulacion = regulacion.lower()
    if regulacion not in BASE_DE_CONOCIMIENTO_LEGAL:
        return {
            "estado": "error",
            "mensaje": f"Regulación no soportada. Regulaciones soportadas: {', '.join(BASE_DE_CONOCIMIENTO_LEGAL.keys())}"
        }
    
    info_regulacion = BASE_DE_CONOCIMIENTO_LEGAL[regulacion]
    
    return {
        "estado": "éxito",
        "regulacion": regulacion.upper(),
        "resumen": info_regulacion["resumen"],
        "requisitos_clave": info_regulacion["requisitos_clave"],
        "recomendaciones": [
            f"Asegúrese de que su proceso de {proceso_negocio} aborde todos los requisitos clave de {regulacion.upper()}",
            "Documente sus medidas de cumplimiento",
            "Revise y actualice regularmente su programa de cumplimiento"
        ]
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
    ],
)
