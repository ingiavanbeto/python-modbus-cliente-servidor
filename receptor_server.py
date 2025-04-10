from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification
import logging
import threading
import time

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def monitor_registers(context):
    while True:
        values = context.getValues(3, 0, count=2)  # 3 = holding register
        print(f"📥 Recibido: {values}")
        time.sleep(3)

def run_server():
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [0]*10)
    )
    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'TestVendor'
    identity.ProductName = 'ModbusServer'
    identity.ModelName = 'ModbusServerModel'
    identity.MajorMinorRevision = '1.0'

    # Iniciar hilo para monitorear registros
    threading.Thread(target=monitor_registers, args=(store,), daemon=True).start()

    print("Servidor Modbus TCP escuchando en 0.0.0.0:5020...")
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()
