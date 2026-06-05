TAG_MAP: dict[str, int] = {
    # ─── Party (id: 1) ───────────────────────────────────────────────────────
    "club": 1,  # de la captura: HAUSMANIAFESTIVALEN 2026 Oslo Dub Club  →  #club
    # ─── Techno / House (id: 4) ──────────────────────────────────────────────
    "tekno": 4,  # mencionado en descripción Hausmaniafestivalen 24 («jazz, tekno, hiphop»)
    # — probable tag futuro en Broadcast
    # ─── Indie / Rock (id: 8) ────────────────────────────────────────────────
    "rock": 8,  # CONFIRMADO: Hausmaniafestivalen 24 Dag 2  →  Tags: #rock #reggae #punk
    "punk": 8,  # CONFIRMADO: Hausmaniafestivalen 24 Dag 2  →  Tags: #rock #reggae #punk
    # ─── Hip-Hop / R&B (id: 9) ───────────────────────────────────────────────
    "hiphop": 9,  # mencionado en descripción Hausmaniafestivalen 24 («jazz, tekno, hiphop»)
    # ─── Metal (id: 23) ya cubierto via captura:
    # ─── Metal (id: 23) ──────────────────────────────────────────────────────
    "hardcore": 23,  # de la captura: TRUEANDTRUE + DØDEN 505  →  #hardcore #metal #oslo
    "metal": 23,  # de la captura: TRUEANDTRUE + DØDEN 505  →  #hardcore #metal #oslo
    # ─── Jazz & Blues (id: 11) ───────────────────────────────────────────────
    "jazz": 11,  # mencionado en descripción Hausmaniafestivalen 24 («jazz, tekno, hiphop»)
    # ─── Folk / Americana (id: 13) ───────────────────────────────────────────
    "folk": 13,  # CONFIRMADO: HEKATE + Andrea Søgnen  →  Tags: #folk #folkemusikk
    "folkemusikk": 13,  # CONFIRMADO: HEKATE + Andrea Søgnen  →  Tags: #folk #folkemusikk
    # ─── Electronic / Experimental (id: 21) ──────────────────────────────────
    "undergrunnsmusikk": 21,  # CONFIRMADO: Novafest  →  Tags: #undergrunnsmusikk
    # ─── Live Music (id: 10) ─────────────────────────────────────────────────
    "festival": 10,  # CONFIRMADO: Hausmaniafestivalen 2026 — festival musical con bandas en vivo
    # duplicado: también en Culture & Experiences (22)
    # ─── Culture & Experiences (id: 22) ──────────────────────────────────────
    "festival": 22,  # duplicado: también en Live Music (10) — Hausmania festival es a la vez
    # cultural (teatro, arte) y musical
    "exhibition": 22,  # CONFIRMADO: Oslo Open  →  Tags: #exhibition #kunstutstilling #utstilling
    "kunstutstilling": 22,  # CONFIRMADO: Oslo Open  →  Tags: #exhibition #kunstutstilling #utstilling
    "utstilling": 22,  # CONFIRMADO: Oslo Open  →  Tags: #exhibition #kunstutstilling #utstilling
    "naturalstate": 22,  # de la captura: Urban Cross-Pollination  →  nombre del organizador (Natural State)
    # workshop de arte/urbanismo/innovación — Culture & Experiences
    "cross-innovation": 22,  # de la captura: Urban Cross-Pollination  →  formato del evento
    # workshop interdisciplinario arte+innovación — Culture & Experiences
    # ─── Reggae & Ska (id: 24) ───────────────────────────────────────────────
    "reggae": 24,  # CONFIRMADO: Hausmaniafestivalen 24 Dag 2  →  Tags: #rock #reggae #punk
    # + Oslo Dub Club base permanente en Hausmania
    "dub": 24,  # de la captura: HAUSMANIAFESTIVALEN 2026 Oslo Dub Club  →  #club #oslodubclub
    # + Young Warrior 2025: #dub #reggae (vía AllEvents/Facebook)
    "oslodubclub": 24,  # de la captura  →  #club #oslodubclub #hausmania
    "neurofunk": 24,  # CONFIRMADO: Bassline  →  Tags: #neurofunk #bassmusic
    # (neurofunk es un subgénero de drum and bass — mejor encaje en Reggae & Ska
    # que en otras categorías dado el contexto del venue)
    "bassmusic": 24,  # CONFIRMADO: Bassline  →  Tags: #neurofunk #bassmusic
    # NOTA: bass music / drum and bass → Reggae & Ska (24) es el mejor
    # encaje disponible dado que no hay categoría DNB específica
}

# ─── NOTA ────────────────────────────────────────────────────────────────────
# Tags de la captura aún no encontrados en eventos pasados de Broadcast:
#   #naturalstate, #cross-innovation → Culture & Experiences (22) si aparecen
# Tags del perfil del venue que pueden aparecer en Broadcast eventualmente:
#   #latin, #støy (noise marathon mencionado en Hausmaniafestivalen 24)
