import time

EVENTS = [
    {"title": "Tommy Cash – Oslo Live",      "club": "Jaeger",       "date": "2025-06-15"},
    {"title": "Tiësto at Blå",               "club": "Blå",          "date": "2025-06-20"},
    {"title": "Night Fever w/ DJ Stingray",  "club": "John Dee",     "date": "2025-06-22"},
    {"title": "Prins Thomas DJ Set",         "club": "Blå",          "date": "2025-07-04"},
]

print("[DEMO] Conectando a BD...", flush=True)
time.sleep(1)

print(f"[DEMO] Buscando eventos con estado 'pending'...", flush=True)
time.sleep(0.8)
print(f"[DEMO] {len(EVENTS)} eventos pendientes encontrados.", flush=True)
time.sleep(0.5)
print("", flush=True)

for event in EVENTS:
    print(f"[DEMO] Procesando: {event['title']} ({event['club']})", flush=True)
    time.sleep(0.5)
    print(f"[DEMO]   → Insertando en tabla events...", flush=True)
    time.sleep(0.8)
    print(f"[DEMO]   → Actualizando estado a 'approved'...", flush=True)
    time.sleep(0.4)
    print("", flush=True)

print("[DEMO] " + "=" * 40, flush=True)
print(f"[DEMO] TOTAL promovidos: {len(EVENTS)}", flush=True)
