import os
import json
from pathlib import Path
from typing import List, Dict, Optional

import os
from pathlib import Path

# Configuración
BASE_DIR = Path(__file__).parent.absolute()
DOCUMENTOS_DIR = BASE_DIR / "documentos"
TIPOS_DOCUMENTO = ["contratos", "facturas", "documentos_legales"]

# Imprimir la ruta para depuración
print(f"Directorio base: {BASE_DIR}")
print(f"Directorio de documentos: {DOCUMENTOS_DIR}")

# Crear estructura de carpetas si no existe
try:
    # Crear directorio principal si no existe
    DOCUMENTOS_DIR.mkdir(exist_ok=True)
    print(f"Directorio principal creado en: {DOCUMENTOS_DIR}")
    
    # Crear subdirectorios
    for tipo in TIPOS_DOCUMENTO:
        tipo_dir = DOCUMENTOS_DIR / tipo
        tipo_dir.mkdir(exist_ok=True)
        print(f"Directorio creado: {tipo_dir}")
        
        # Verificar permisos
        if not os.access(tipo_dir, os.W_OK):
            print(f"ADVERTENCIA: No hay permisos de escritura en {tipo_dir}")
            
except Exception as e:
    print(f"Error al crear directorios: {e}")

# Documentos de prueba
DOCUMENTOS_PRUEBA = {
    "contratos": [
        {
            "nombre": "contrato_servicios_tecnologicos_2025.txt",
            "contenido": """CONTRATO DE PRESTACIÓN DE SERVICIOS TECNOLÓGICOS

ENTRE:
TECNOSOLUCIONES MÉXICO, S.A. DE C.V., representada por el Lic. Roberto Méndez González, Director General, a quien en lo sucesivo se le denominará "EL PRESTADOR".

Y

INNOVACIONES DIGITALES, S.A.P.I. DE C.V., representada por la C.P. Ana Laura Sánchez Ruíz, Directora de Operaciones, a quien en lo sucesivo se le denominará "EL CLIENTE".

PRIMERA. OBJETO
1.1. EL PRESTADOR se obliga a prestar al CLIENTE los siguientes servicios profesionales de consultoría en transformación digital:
   a) Análisis de procesos actuales y diagnóstico tecnológico
   b) Implementación de soluciones de automatización
   c) Migración de infraestructura a la nube
   d) Capacitación al personal técnico
   e) Soporte post-implementación por 6 meses

1.2. Los alcances específicos de cada servicio se detallan en el Anexo Técnico que forma parte integrante de este contrato.

SEGUNDA. DURACIÓN
2.1. El presente contrato tendrá una duración de doce (12) meses contados a partir de la fecha de firma.
2.2. Podrá ser prorrogado por periodos iguales, salvo notificación en contrario con treinta (30) días de anticipación a la fecha de terminación.

TERCERA. HONORARIOS Y FORMA DE PAGO
3.1. Por los servicios prestados, EL CLIENTE pagará a EL PRESTADOR la cantidad de $250,000.00 (DOSCIENTOS CINCUENTA MIL PESOS 00/100 M.N.) más IVA mensuales.
3.2. Los pagos se realizarán mediante transferencia electrónica a la cuenta que para tal efecto indique EL PRESTADOR, dentro de los primeros cinco días hábiles de cada mes.
3.3. Por pagos posteriores a la fecha señalada, se cobrará un interés moratorio del 3% mensual sobre el monto de la renta.

CUARTA. CONFIDENCIALIDAD
4.1. Las partes se comprometen a mantener estricta confidencialidad sobre toda la información intercambiada durante la vigencia de este contrato y hasta tres años después de su terminación.
4.2. Quedan excluidas de esta obligación las informaciones que:
   a) Sean de dominio público
   b) Hayan sido conocidas con anterioridad
   c) Sean recibidas de terceros sin obligación de confidencialidad
   d) Sean requeridas por autoridad competente

QUINTA. PROPIEDAD INTELECTUAL
5.1. Todo el software, documentación y materiales desarrollados específicamente para EL CLIENTE serán de su exclusiva propiedad, una vez que se haya cubierto el pago total de los honorarios acordados.
5.2. Las herramientas, metodologías y know-how propiedad de EL PRESTADOR mantendrán su carácter confidencial y de propiedad exclusiva de EL PRESTADOR.

SEXTA. TERMINACIÓN
6.1. Cualquiera de las partes podrá dar por terminado el presente contrato mediante aviso por escrito con treinta días de anticipación, sin responsabilidad alguna, siempre que no exista incumplimiento de las obligaciones pactadas.
6.2. En caso de terminación anticipada por causa imputable a EL CLIENTE, éste deberá pagar a EL PRESTADOR los honorarios correspondientes a los servicios prestados hasta la fecha de terminación, más una penalización del 20% sobre el monto de los servicios no prestados.

SÉPTIMA. JURISDICCIÓN
7.1. Para todo lo relacionado con la interpretación y cumplimiento de este contrato, las partes se someten a las leyes aplicables en la Ciudad de México y a la jurisdicción de sus tribunales, renunciando expresamente a cualquier otra jurisdicción que por razón de sus domicilios presentes o futuros pudiera corresponderles.

POR EL PRESTADOR:                     POR EL CLIENTE:
___________________________           ___________________________
Lic. Roberto Méndez González          C.P. Ana Laura Sánchez Ruíz
Director General                      Directora de Operaciones
TECNOSOLUCIONES MÉXICO, S.A. DE C.V.  INNOVACIONES DIGITALES, S.A.P.I. DE C.V.

FECHA: 15 de mayo de 2025            FECHA: 15 de mayo de 2025"""
        },
        {
            "nombre": "acuerdo_confidencialidad_nexus.txt",
            "contenido": """ACUERDO DE CONFIDENCIALIDAD (NDA)

Este ACUERDO DE CONFIDENCIALIDAD (en lo sucesivo, el "Acuerdo") se celebra el 10 de mayo de 2025, por y entre:

Por una parte, NEXUS TECHNOLOGIES, S.A. DE C.V., sociedad mexicana, representada en este acto por el Ing. Carlos Eduardo Ramírez Morales, en su carácter de Director de Innovación, a quien en lo sucesivo se le denominará "LA EMPRESA".

Y por la otra, la empresa CONSULTORÍA AVANZADA EN TECNOLOGÍA, S.C., representada por la Lic. Fernanda Gutiérrez del Río, en su carácter de Socia Fundadora, a quien en lo sucesivo se le denominará "EL CONSULTOR".

1. DEFINICIONES
1.1. "Información Confidencial" significa cualquier información, en cualquier forma, incluyendo pero no limitado a: datos técnicos, planes de negocio, estrategias comerciales, información financiera, listas de clientes, códigos fuente, diseños, fórmulas, procesos, técnicas, know-how, invenciones, descubrimientos, conceptos, ideas, documentos, prototipos, muestras, diseños, manuales, especificaciones, informes, estudios, análisis, compilaciones, memorandos, correspondencia y cualquier otra información revelada por cualquiera de las Partes a la otra Parte, ya sea de forma oral, escrita, gráfica, electrónica o en cualquier otro formato.

2. OBLIGACIONES DE CONFIDENCIALIDAD
2.1. El CONSULTOR se compromete a:
   a) Mantener en estricta confidencialidad toda la Información Confidencial que reciba de LA EMPRESA.
   b) No revelar, total o parcialmente, dicha información a terceros sin el consentimiento previo y por escrito de LA EMPRESA.
   c) Utilizar la Información Confidencial únicamente para los fines establecidos en el Contrato de Prestación de Servicios celebrado entre las Partes.
   d) Implementar medidas de seguridad razonables para proteger la Información Confidencial.

3. PLAZO
3.1. Las obligaciones de confidencialidad establecidas en este Acuerdo tendrán una duración de cinco (5) años contados a partir de la fecha de su firma, independientemente de la terminación de cualquier relación comercial entre las Partes.

4. EXCEPCIONES
4.1. Las obligaciones de confidencialidad no se aplicarán a la información que:
   a) Sea o llegue a ser de dominio público sin violación de este Acuerdo;
   b) Esté en posesión del CONSULTOR antes de su divulgación por parte de LA EMPRESA, según conste en registros fehacientes;
   c) Sea recibida de un tercero que no esté obligado a mantener su confidencialidad;
   d) Sea desarrollada independientemente por el CONSULTOR sin uso de la Información Confidencial; o
   e) Sea requerida por orden judicial o administrativa, en cuyo caso el CONSULTOR notificará inmediatamente a LA EMPRESA para que ésta pueda oponerse a dicha revelación.

5. PROPIEDAD INTELECTUAL
5.1. Nada de lo dispuesto en este Acuerdo se interpretará como una licencia o cesión de derechos de propiedad intelectual de LA EMPRESA sobre su Información Confidencial.
5.2. Todos los derechos de propiedad intelectual sobre la Información Confidencial son y seguirán siendo propiedad exclusiva de LA EMPRESA.

6. SANCIONES
6.1. En caso de incumplimiento de las obligaciones de confidencialidad, el CONSULTOR pagará a LA EMPRESA una indemnización por daños y perjuicios equivalente a diez veces el monto total de los honorarios pactados en el Contrato de Prestación de Servicios, sin perjuicio de otras acciones legales a las que hubiere lugar.

7. LEY APLICABLE Y JURISDICCIÓN
7.1. Este Acuerdo se regirá por las leyes de los Estados Unidos Mexicanos y cualquier controversia que surja en relación con el mismo se someterá a la jurisdicción exclusiva de los tribunales competentes de la Ciudad de México, renunciando expresamente a cualquier otra jurisdicción que por razón de sus domicilios presentes o futuros pudiera corresponderles.

POR LA EMPRESA:                         POR EL CONSULTOR:
___________________________             ___________________________
Ing. Carlos Eduardo Ramírez Morales     Lic. Fernanda Gutiérrez del Río
Director de Innovación                  Socia Fundadora
NEXUS TECHNOLOGIES, S.A. DE C.V.        CONSULTORÍA AVANZADA EN TECNOLOGÍA, S.C.

FECHA: 10 de mayo de 2025              FECHA: 10 de mayo de 2025"""
        },
        {
            "nombre": "contrato_arrendamiento_oficinas.txt",
            "contenido": """CONTRATO DE ARRENDAMIENTO DE OFICINAS

En la Ciudad de Monterrey, Nuevo León, siendo las 10:00 horas del día 5 de mayo de 2025, comparecen:

Por una parte, el C. JOSÉ ANTONIO LÓPEZ MARTÍNEZ, mayor de edad, con credencial para votar número LOMJ720315HDFLRS01, con domicilio para oír y recibir notificaciones en Calle San Jerónimo 245, Col. Del Valle, C.P. 66220, San Pedro Garza García, Nuevo León, a quien en lo sucesivo se le denominará "EL ARRENDADOR", 

Y por la otra parte, la sociedad mercantil denominada SOLUCIONES INTEGRALES EN TECNOLOGÍA, S.A. DE C.V., representada en este acto por la C.P. MARÍA FERNANDA GARCÍA HERNÁNDEZ, en su carácter de Directora General, con domicilio fiscal en Av. Gómez Morín 110, Col. Valle del Campestre, C.P. 66265, San Pedro Garza García, Nuevo León, a quien en lo sucesivo se le denominará "EL ARRENDATARIO", 

Al tenor de las siguientes declaraciones y cláusulas:

DECLARACIONES
I. Declara EL ARRENDADOR:
   a) Que es dueño legítimo del inmueble ubicado en Avenida Gómez Morín #1234, Col. Valle del Campestre, C.P. 66265, San Pedro Garza García, Nuevo León, el cual se describe en la escritura pública número 45,890, Volumen 120, del Libro 15 de la Ciudad de Monterrey, N.L., inscrito en el Registro Público de la Propiedad bajo el número 9876543.
   b) Que el inmueble se encuentra libre de gravamen, embargo o cualquier limitación de dominio que impida su arrendamiento.
   c) Que el uso de suelo del inmueble permite su utilización como oficinas corporativas.

II. Declara EL ARRENDATARIO:
   a) Que es una sociedad legalmente constituida de conformidad con las leyes mexicanas, tal como consta en la escritura número 12,345, otorgada ante la fe del Notario Público número 25 del Distrito Federal, e inscrita en el Registro Público de Comercio bajo la hoja electrónica número 123456789.
   b) Que tiene la capacidad legal necesaria para celebrar el presente contrato.
   c) Que el inmueble será utilizado exclusivamente para oficinas administrativas de la empresa.

CLÁUSULAS
PRIMERA. OBJETO
EL ARRENDADOR da en arrendamiento a EL ARRENDATARIO el inmueble ubicado en el domicilio antes señalado, el cual consta de:
   - Superficie total: 350 m²
   - Planta Baja: Recepción, área de espera, 2 baños completos, cocineta
   - Planta Alta: 5 oficinas privadas, sala de juntas, 2 baños completos, área de archivo
   - Estacionamiento: 4 cajones techados
   - Servicios: Agua, luz, gas, drenaje, teléfono, internet de fibra óptica
   - Instalaciones: Aire acondicionado tipo minisplit en cada área, sistema de alarma, circuito cerrado de TV

SEGUNDA. DESTINO
2.1. El inmueble se destinará exclusivamente para oficinas administrativas de EL ARRENDATARIO, quedando estrictamente prohibido darle cualquier otro uso sin el consentimiento previo y por escrito de EL ARRENDADOR.
2.2. Queda expresamente prohibido:
   a) Realizar modificaciones a la estructura del inmueble
   b) Instalar anuncios o letreros sin autorización
   c) Subarrendar total o parcialmente el inmueble
   d) Realizar actividades que generen molestias a los vecinos
   e) Almacenar materiales inflamables o peligrosos

TERCERA. TÉRMINO
3.1. El presente contrato tendrá una vigencia de tres (3) años, contados a partir del 1 de junio de 2025 y hasta el 31 de mayo de 2028.
3.2. El contrato se renovará automáticamente por periodos iguales, salvo denuncia de cualquiera de las partes con 90 días de anticipación a la fecha de terminación.

CUARTA. RENTA Y FORMA DE PAGO
4.1. La renta mensual será de $75,000.00 (SETENTA Y CINCO MIL PESOS 00/100 M.N.) más IVA, cantidad que se actualizará anualmente de acuerdo con el Índice Nacional de Precios al Consumidor publicado por el Banco de México.
4.2. El pago deberá realizarse dentro de los primeros cinco días hábiles de cada mes en la cuenta bancaria que para tal efecto indique EL ARRENDADOR.
4.3. Por pagos posteriores a la fecha señalada, se cobrará un interés moratorio del 3% mensual sobre el monto de la renta.
4.4. Los pagos deberán realizarse mediante transferencia electrónica, depósito bancario o cheque certificado a nombre de EL ARRENDADOR.

QUINTA. DEPÓSITO EN GARANTÍA
5.1. Al momento de la firma del presente contrato, EL ARRENDATARIO entregará a EL ARRENDADOR la cantidad de $150,000.00 (CIENTO CINCUENTA MIL PESOS 00/100 M.N.) en concepto de depósito en garantía.
5.2. Dicho depósito será devuelto dentro de los treinta días siguientes a la terminación del contrato, siempre y cuando:
   a) EL ARRENDATARIO haya cumplido con todas sus obligaciones
   b) El inmueble sea devuelto en las mismas condiciones en que fue recibido, considerando el desgaste natural por el uso ordinario
   c) No exista adeudo alguno por concepto de rentas, servicios o daños
5.3. En caso de incumplimiento de EL ARRENDATARIO, EL ARRENDADOR podrá aplicar el depósito en garantía al pago de los adeudos o daños ocasionados.

SEXTA. MANTENIMIENTO Y REPARACIONES
6.1. EL ARRENDATARIO se obliga a:
   a) Dar al inmueble el uso para el cual está destinado
   b) Realizar las reparaciones menores que sean necesarias
   c) Mantener limpias las instalaciones
   d) Dar aviso inmediato de cualquier daño o desperfecto
6.2. Serán consideradas reparaciones menores aquellas cuyo monto no exceda el equivalente a tres días de renta.
6.3. Las reparaciones mayores que no sean consecuencia del uso normal del inmueble serán responsabilidad de EL ARRENDADOR, quien deberá realizarlas en un plazo no mayor a 15 días hábiles contados a partir de la notificación por escrito.

SÉPTIMA. SERVICIOS
7.1. Los servicios de agua, luz, teléfono, internet, gas y demás servicios que se contraten, serán por cuenta y cargo de EL ARRENDATARIO, quien deberá dar de alta los contratos correspondientes a su nombre.
7.2. EL ARRENDATARIO deberá presentar los recibos de pago de los servicios al momento de realizar el pago de la renta, como comprobante de que se encuentran al corriente.

OCTAVA. TERMINACIÓN
8.1. El presente contrato podrá darse por terminado anticipadamente en los siguientes casos:
   a) Por mutuo acuerdo de las partes
   b) Por incumplimiento de cualquiera de las obligaciones aquí pactadas
   c) Por necesidad de EL ARRENDADOR de ocupar el inmueble para sí o para sus familiares en primer grado, siempre que lo notifique con 90 días de anticipación
   d) Por destrucción total o parcial del inmueble por caso fortuito o fuerza mayor
8.2. En caso de terminación anticipada por causa imputable a EL ARRENDATARIO, éste deberá pagar a EL ARRENDADOR una penalización equivalente a tres meses de renta, sin perjuicio del pago de los daños y perjuicios que se ocasionen.

NOVENA. JURISDICCIÓN
9.1. Para todo lo relacionado con la interpretación y cumplimiento de este contrato, las partes se someten a las leyes del Estado de Nuevo León y a la jurisdicción de los tribunales competentes de la Ciudad de Monterrey, renunciando a cualquier otra jurisdicción que por razón de sus domicilios presentes o futuros pudiera corresponderles.

DÉCIMA. DOMICILIOS
10.1. Para todos los efectos legales derivados del presente contrato, las partes señalan como sus respectivos domicilios los que aparecen en el encabezado de este instrumento.
10.2. Cualquier notificación o comunicación entre las partes deberá realizarse por escrito y se tendrá por hecha al día hábil siguiente de su entrega personal o por correo certificado con acuse de recibo.

LEÍDO QUE FUE EL PRESENTE INSTRUMENTO POR LAS PARTES Y ENTERADAS DE SU CONTENIDO Y ALCANCE LEGAL, LO FIRMAN DE COMÚN ACUERDO, EN EL LUGAR Y FECHA QUE AL CALCE SE INDICA.

_________________________________    _________________________________
C. José Antonio López Martínez         C.P. María Fernanda García Hernández
ARRENDADOR                             REPRESENTANTE LEGAL
                                       SOLUCIONES INTEGRALES EN TECNOLOGÍA, S.A. DE C.V.

TESTIGO: _________________________    TESTIGO: _________________________
Nombre: Lic. Roberto Sánchez Mendoza  Nombre: Lic. Patricia González Ramírez
"""
        }
    ]
}

def inicializar_documentos_prueba():
    """Crea documentos de prueba si no existen"""
    for tipo, docs in DOCUMENTOS_PRUEBA.items():
        for doc in docs:
            ruta = DOCUMENTOS_DIR / tipo / doc["nombre"]
            if not ruta.exists():
                with open(ruta, 'w', encoding='utf-8') as f:
                    f.write(doc["contenido"])

def listar_documentos(tipo_documento: str = "") -> List[Dict]:
    """Lista todos los documentos o los de un tipo específico
    
    Args:
        tipo_documento: Tipo de documento a listar. Si es una cadena vacía, lista todos los documentos.
                      Debe ser uno de los tipos en TIPOS_DOCUMENTO.
        
    Returns:
        Lista de diccionarios con información de los documentos
    """
    documentos = []
    
    if tipo_documento and tipo_documento in TIPOS_DOCUMENTO:
        carpetas = [tipo_documento]
    else:
        carpetas = TIPOS_DOCUMENTO
    
    for carpeta in carpetas:
        ruta_carpeta = DOCUMENTOS_DIR / carpeta
        for archivo in ruta_carpeta.glob('*'):
            if archivo.is_file():
                documentos.append({
                    "nombre": archivo.name,
                    "tipo": carpeta,
                    "ruta": str(archivo),
                    "tamano": archivo.stat().st_size,
                    "fecha_modificacion": archivo.stat().st_mtime
                })
    
    return documentos

def buscar_en_documentos(termino: str) -> List[Dict]:
    """Busca un término en todos los documentos"""
    resultados = []
    for doc in listar_documentos():
        try:
            with open(doc["ruta"], 'r', encoding='utf-8') as f:
                contenido = f.read()
                if termino.lower() in contenido.lower():
                    resultados.append({
                        "documento": doc["nombre"],
                        "tipo": doc["tipo"],
                        "ruta": doc["ruta"],
                        "fragmento": contenido[:200] + "..."  # Primeros 200 caracteres
                    })
        except Exception as e:
            print(f"Error al leer {doc['ruta']}: {e}")
    
    return resultados

def leer_documento(ruta_relativa: str) -> Optional[Dict]:
    """Lee el contenido de un documento"""
    ruta = DOCUMENTOS_DIR / ruta_relativa
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return {
                "nombre": ruta.name,
                "ruta": str(ruta),
                "contenido": f.read()
            }
    except Exception as e:
        print(f"Error al leer el documento: {e}")
        return None

# Inicializar documentos de prueba al importar el módulo
inicializar_documentos_prueba()
