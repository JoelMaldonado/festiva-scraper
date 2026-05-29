import time

CLUBS = [
    {"name": "SALT",        "found": 208, "old": 12, "prod": 190, "dupes": 2, "inserted": 4},
    {"name": "Rockefeller", "found": 231, "old": 8,  "prod": 218, "dupes": 3, "inserted": 2},
    {"name": "Kafehaerverk","found": 19,  "old": 1,  "prod": 16,  "dupes": 0, "inserted": 2},
    {"name": "MIR",         "found": 25,  "old": 2,  "prod": 21,  "dupes": 0, "inserted": 2},
]

print("[DEMO] Conectando a BD...", flush=True)
time.sleep(1)

for club in CLUBS:
    print(f"[DEMO] [{club['name']}] Obteniendo eventos desde API...", flush=True)
    time.sleep(1)
    print(f"[DEMO] [{club['name']}] Filtrando eventos pasados...", flush=True)
    time.sleep(0.5)
    print(f"[DEMO] [{club['name']}] Verificando duplicados en BD...", flush=True)
    time.sleep(1)

print("", flush=True)

total_inserted = 0
for club in CLUBS:
    print(f"[DEMO] [{club['name']}]", flush=True)
    print(f"[DEMO]   Encontrados:           {club['found']}", flush=True)
    print(f"[DEMO]   Descartados por fecha: {club['old']}", flush=True)
    print(f"[DEMO]   Ya en producción:      {club['prod']}", flush=True)
    print(f"[DEMO]   Duplicados:            {club['dupes']}", flush=True)
    print(f"[DEMO]   Insertados:            {club['inserted']}", flush=True)
    print("", flush=True)
    total_inserted += club["inserted"]
    time.sleep(0.3)

print("[DEMO] " + "=" * 40, flush=True)
print(f"[DEMO] TOTAL insertados: {total_inserted}", flush=True)
