TAG_MAP: dict[str, int] = {
    # ─── Indie / Rock (id: 8) ────────────────────────────────────────────────
    "indie": 8,  # CONFIRMADO: Skov  →  Tags: #concert #indie #rock #fett
    "punk": 8,  # CONFIRMADO: Kjöter  →  Tags: #concert #punk #rock #fett
    "rock": 8,  # CONFIRMADO: Kjöter, Skov, fucales
    "gaze": 8,  # CONFIRMADO: fucales, Hiccup Heart
    "råkk": 8,  # CONFIRMADO: 1991  →  Tags: #råkk #råll #bergen
    "råll": 8,  # CONFIRMADO: 1991  →  Tags: #råkk #råll #bergen
    # ─── Jazz & Blues (id: 11) ───────────────────────────────────────────────
    "jazz": 11,  # CONFIRMADO: Jazzjam #16, #18, #23, #24
    "jam": 11,  # CONFIRMADO: Jazzjam #16, #18
    # ─── Folk / Americana (id: 13) ───────────────────────────────────────────
    "americana": 13,  # CONFIRMADO: Johanna Reine-Nilsen  →  Tags: #folk #americana #sjelfullt
    "folk": 13,  # CONFIRMADO: Johanna Reine-Nilsen  →  Tags: #folk #americana #sjelfullt
    # ─── Pop (id: 15) ────────────────────────────────────────────────────────
    "pop": 15,  # CONFIRMADO: Humle  →  Tags: #concert #pop #norsk #humle
    # ─── "norsk" ELIMINADO ───────────────────────────────────────────────────
    # "norsk" solo significa "noruego" — describe origen, no género ni tipo de evento.
    # Podría aparecer en pop, folk, jazz, comedia, o cualquier otra cosa.
    # Si un evento tiene #norsk + #pop, ya lo captura "pop". Sin otro tag de género,
    # es mejor que quede sin categoría que mapearlo incorrectamente.
}
