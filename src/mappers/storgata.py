TAG_MAP: dict[str, int] = {
    # ─── LGBTQ+ / Drag (id: 7) ───────────────────────────────────────────────
    "pride": 7,  # del .py original — Pride-fest med Sliteneliten confirmado
    # vía Facebook/Hoopla (no en Broadcast)
    # ─── Live Music (id: 10) ─────────────────────────────────────────────────
    "concert": 10,  # del .py original
    "konsert": 10,  # variante noruega de concert — mismo uso en Broadcast
    # ─── Folk / Americana (id: 13) ───────────────────────────────────────────
    "folk": 13,  # Ektefolk programa visesang, country, americana, singer/songwriter
    # — confirmdado vía folkistorgata.no/ektefolk
    "americana": 13,  # confirmado vía folkistorgata.no/ektefolk
    "country": 13,  # confirmado vía folkistorgata.no/ektefolk
    # + Lars Kolberg (country) en 1. mai-fest på Folk (Underskog)
    "visesang": 13,  # confirmado vía folkistorgata.no/ektefolk
    # ─── Games & Quiz (id: 14) ───────────────────────────────────────────────
    "quiz": 14,  # confirmado vía Quiz i bakgården på Folk (Hoopla/AllEvents)
    # ─── Comedy & Shows (id: 16) ─────────────────────────────────────────────
    "standup": 16,  # confirmado vía Intravenøs Standup (Ticketmaster)
    "comedy": 16,  # del .py original
    # ─── Culture & Experiences (id: 22) ──────────────────────────────────────
    "vm": 22,  # confirmado vía folkistorgata.no — viser fotball-VM på storskjerm
    # ─── Reggae & Ska (id: 24) ───────────────────────────────────────────────
    "ska": 24,  # CONFIRMADO: The Phantoms spiller ska (Hoopla) — banda residente
    "reggae": 24,  # The Phantoms: «låtene spenner fra swing, blues til reggae»
}

# ─── NOTA ────────────────────────────────────────────────────────────────────
# Folk i Storgata usa Broadcast muy poco — casi todos sus eventos van por Hoopla.
# El único evento confirmado en Broadcast tiene tag #misc (17. mai 2024).
# Los tags aquí se basan en el perfil documentado del venue (folkistorgata.no,
# Hoopla, Underskog, Facebook) más que en eventos de Broadcast propiamente.
# Si en el futuro el venue sube más eventos a Broadcast con tags específicos,
# se deberán revisar y ampliar.
