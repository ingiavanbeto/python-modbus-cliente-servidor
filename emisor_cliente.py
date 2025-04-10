from pymodbus.client.sync import ModbusTcpClient
import random
import time
import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def run_modbus_client():
    client = ModbusTcpClient("127.0.0.1", port=5020)
    if not client.connect():
        print("No se pudo conectar al servidor.")
        return

    try:
        while True:
            # Generar 2 enteros aleatorios entre 0 y 256
            value1 = random.randint(0, 256)
            value2 = random.randint(0, 256)

            # Escribirlos en los holding registers 0 y 1
            result = client.write_registers(0, [value1, value2], unit=1)

            if result.isError():
                print("❌ Error al escribir registros:", result)
            else:
                print(f"✅ Escribiendo: [{value1}, {value2}]")

            time.sleep(3)  # Esperar 1 segundo antes de la siguiente escritura

    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        client.close()

if __name__ == "__main__":
    run_modbus_client()