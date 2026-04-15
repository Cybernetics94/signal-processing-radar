import serial, time, sys

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
print("🔴 Serial Monitor LIVE - Ctrl+C zum Beenden")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print(f"📡 Tiva C: {line}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n Serial Monitor beendet")
    ser.close()
