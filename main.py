from fastapi import FastAPI

app = FastAPI(
    title="UTELYnk",  # Cambia el nombre de la aplicación
    description="Plataforma de integración para sincronización de datos entre SINTAD y MANTRA, y en un futuro SISPAC.",  # Descripción general
    version="1.0.0",  # Puedes cambiar la versión si lo deseas
)

# Endpoint para obtener el estado de la sincronización entre los sistemas
@app.get("/sincronizacion-estados", summary="Obtener estado de sincronización",
         description="Este endpoint permite verificar el estado actual de la sincronización entre los sistemas SINTAD, MANTRA y SISPAC.")
async def obtener_estado_sincronizacion():
    return {"message": "Sincronización de los sistemas en curso."}

# Endpoint para iniciar la sincronización de datos entre los sistemas
@app.post("/iniciar-sincronizacion", summary="Iniciar sincronización de datos",
          description="Este endpoint inicia el proceso de sincronización de datos entre los sistemas SINTAD, MANTRA y SISPAC. "
                      "Asegúrate de tener permisos para iniciar esta operación.")
async def iniciar_sincronizacion():
    return {"message": "Sincronización de datos iniciada correctamente."}

# Endpoint para consultar los KPIs de la operación logística
@app.get("/consultar-kpis", summary="Consultar KPIs de operaciones",
         description="Este endpoint proporciona los KPIs de las operaciones logísticas, como el tiempo de procesamiento de facturas, estado de pedidos y métricas de servicio.")
async def consultar_kpis():
    return {"kpi_1": "Tiempo de procesamiento: 5 minutos", "kpi_2": "Estado de pedidos: 98% completo"}

# Endpoint para obtener los detalles de la facturación de un cliente
@app.get("/detalle-facturacion/{cliente_id}", summary="Obtener detalles de facturación por cliente",
         description="Este endpoint devuelve los detalles de facturación de un cliente específico, incluyendo montos y estado de pagos. "
                     "El 'cliente_id' debe ser proporcionado para obtener la información.")
async def obtener_detalle_facturacion(cliente_id: int):
    return {"cliente_id": cliente_id, "estado_factura": "Pendiente", "monto_factura": 1500.50}

# Endpoint para obtener el estado de la carga
@app.get("/estado-carga/{numero_carga}", summary="Obtener estado de carga",
         description="Este endpoint permite obtener el estado actual de una carga en el sistema. Se debe proporcionar el número de carga para obtener el estado correspondiente.")
async def obtener_estado_carga(numero_carga: int):
    return {"numero_carga": numero_carga, "estado": "En tránsito", "fecha_estimada_entrega": "2025-05-20"}

# Endpoint para generar un reporte de sincronización de sistemas
@app.post("/generar-reporte-sincronizacion", summary="Generar reporte de sincronización",
          description="Este endpoint genera un reporte detallado de la sincronización de los sistemas SINTAD, MANTRA y SISPAC, "
                      "que incluye los errores detectados, tiempos de sincronización y estado general de los sistemas.")
async def generar_reporte_sincronizacion():
    return {"message": "Reporte de sincronización generado exitosamente."}

# Endpoint para finalizar la operación y cerrar la factura de un cliente
@app.post("/finalizar-operacion/{cliente_id}", summary="Finalizar operación y cerrar factura",
          description="Este endpoint finaliza la operación logística de un cliente y cierra la factura correspondiente. "
                      "El 'cliente_id' debe ser proporcionado para cerrar la factura y completar la operación.")
async def finalizar_operacion(cliente_id: int):
    return {"message": f"Operación finalizada y factura cerrada para el cliente {cliente_id}."}
