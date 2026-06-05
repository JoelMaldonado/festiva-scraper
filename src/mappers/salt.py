TAG_MAP: dict[str, int] = {
    # ─── Party (id: 1) ───────────────────────────────────────────────────────
    "bysommer": 1,  # img3: Adama Janlo #konsert #bysommer / múltiples Bysommer
    "club": 1,  # img2: MAGNET #Pride #Electronic #Club
    # img6: Club Gela #afrobeat #club
    "dj": 1,  # img3: DJ Session #dj #uteservering
    "fest": 1,  # del .py original
    "festival": 1,  # CONFIRMADO: Oslo Drag Festival #drag #kickoff #festival
    "kickoff": 1,  # CONFIRMADO: Oslo Drag Festival #drag #kickoff #festival
    "klubb": 1,  # img2: Fredagen med DRAMAqueen #Pride #klubb #Lhbtqia+
    "party": 1,  # img2: SKEIV VERDEN PARTY #Pride #Party
    "åpningsfest": 1,  # CONFIRMADO+img: Oslo Pride Åpningsfest — siempre es la fiesta
    # de apertura de Oslo Pride en SALT → también en LGBTQ+ (7)
    # ─── Afrobeat (id: 3) ────────────────────────────────────────────────────
    "afrobeat": 3,  # CONFIRMADO: Afrobeats Festival #afrobeat
    # img6: Club Gela #afrobeat #club
    # ─── Techno / House (id: 4) ──────────────────────────────────────────────
    # ─── Themed (id: 6) ──────────────────────────────────────────────────────
    "brunsj": 6,  # del .py original
    "fotball": 6,  # img1+: VM-kamper #VM #Sport #Fotball
    "mat": 6,  # del .py original
    "rituale": 6,  # Saunafestival på SALT — ritualer de sauna, meditación y bienestar
    # NOTA: en el .py original estaba en Electronic/Experimental (21)
    # pero el contexto real en SALT es experiencia de sauna → Themed (6)
    "sauna": 6,  # del .py original
    "sport": 6,  # img1+: VM-kamper #VM #Sport #Fotball
    "vm": 6,  # img1+: VM-kamper #VM #Sport #Fotball — Mundial de fútbol
    "vin": 6,  # del .py original
    # ─── LGBTQ+ / Drag (id: 7) ───────────────────────────────────────────────
    "drag": 7,  # img1: Dragbingo #Drag #Bingo #LGBTQIA+
    "lgbtqia+": 7,  # img1: Dragbingo #Drag #Bingo #LGBTQIA+
    "lhbtqia+": 7,  # img2: Oslo Queer Line Dance #Queer #Linedance #LHBTQIA+
    "lipsync": 7,  # del .py original
    "oslopride": 7,  # CONFIRMADO: Oslo Pride Åpningsfest #oslopride #åpningsfest #lgbtqia+
    "pride": 7,  # img2: SKEIV VERDEN PARTY #Pride #Party
    "queer": 7,  # img2: Oslo Queer Line Dance #Queer #Linedance #LHBTQIA+
    "skeiv": 7,  # img1: Varm Melk med Honning #OsloPride #Skeiv #Teater
    "åpningsfest": 7,  # duplicado — Oslo Pride Åpningsfest es 100% LGBTQ+
    # también en Party (1) porque es una fiesta
    # ─── Indie / Rock (id: 8) ────────────────────────────────────────────────
    "alternativ": 8,  # del .py original
    "indie": 8,  # del .py original
    "postpunk": 8,  # del .py original
    "rock": 8,  # img1: Tora Daa #Pride #Funk #Rock
    # img5: GA-20 #bluegrass #rock #blues
    "jazzrock": 8,  # duplicado: también en Jazz & Blues (11)
    # ─── Hip-Hop / R&B (id: 9) ───────────────────────────────────────────────
    "hiphop": 9,  # CONFIRMADO: Typen Din #rap #norsk #hiphop
    "r&b": 9,  # del .py original
    "rnb": 9,  # del .py original
    "rap": 9,  # CONFIRMADO: Typen Din #rap #norsk #hiphop
    # ─── Live Music (id: 10) ─────────────────────────────────────────────────
    "konsert": 10,  # img3+: múltiples Bysommer-konserter #konsert #bysommer
    "kor": 10,  # del .py original
    "minnekonsert": 10,  # img10: På Sterke Vinger #Minnekonsert
    "musikkfest": 10,  # del .py original
    # ─── Jazz & Blues (id: 11) ───────────────────────────────────────────────
    "blues": 11,  # img5: GA-20 #bluegrass #rock #blues
    "jazz": 11,  # del .py original
    "jazzrock": 11,  # duplicado: también en Indie/Rock (8)
    # ─── Disco / Funk (id: 12) ───────────────────────────────────────────────
    "funk": 12,  # img1: Tora Daa #Pride #Funk #Rock
    # img10: D'Sound #Funk #Soul #R'n'B
    "soul": 12,  # img10: RÜ #R&B #HipHop #Soul
    # img10: D'Sound #Funk #Soul #R'n'B
    # ─── Folk / Americana (id: 13) ───────────────────────────────────────────
    "americana": 13,  # del .py original
    "bluegrass": 13,  # img5: GA-20 #bluegrass #rock #blues
    "country": 13,  # img9: Birgitte and The Dusty Trails #konsert #bysommer #country
    "folk": 13,  # del .py original
    "folkemusikk": 13,  # del .py original
    "linedance": 13,  # img2: Oslo Queer Line Dance #Queer #Linedance #LHBTQIA+
    "singer-songwriter": 13,  # del .py original
    "visepop": 13,  # img10: Hoanna #visepop — vise es género folk noruego
    # solo en Folk/Americana (13), no en Pop (15)
    # ─── Games & Quiz (id: 14) ───────────────────────────────────────────────
    "bingo": 14,  # CONFIRMADO: Dragbingo #drag #bingo #lgbtqia+
    # img7: Verdens største danske bingo #bingo #dansk #humor
    # img8: Musikkbingo med Sigurd #musikk #bingo #festival
    "gameshow": 14,  # img7: Gameshow med EmilAlex #gameshow #festival
    # ─── Pop (id: 15) ────────────────────────────────────────────────────────
    "britney": 15,  # del .py original
    "eurovision": 15,  # del .py original
    "pop": 15,  # del .py original
    "roxette": 15,  # img10: ROXETTE EXPERIENCE #roxette #ROX7
    "rox7": 15,  # img10: ROXETTE EXPERIENCE #roxette #ROX7 — tribute band pop
    # ─── Comedy & Shows (id: 16) ─────────────────────────────────────────────
    "comedy": 16,  # img7+: Rat's ass #comedy #english
    "homur": 16,  # del .py original (typo de humor)
    "humor": 16,  # img1+: múltiples #Humor #Standup
    "impro": 16,  # img5+: Nesten Lættis sommershow #impro #humor
    "improv": 16,  # del .py original
    "litteratur": 16,  # del .py original
    "oslofringe": 16,  # CONFIRMADO: Oslo Fringe #oslofringe #scenekunst #humor
    "podcast": 16,  # img8: Bassene LIVE #humor #festival #podkast
    "podkast": 16,  # img8: Bassene LIVE #humor #festival #podkast
    "polsk": 16,  # CONFIRMADO: Rafał Rutkowski #polsk #standup #humor
    # — standup en polaco. El .py original tenía "polish" (inglés)
    # pero el tag real en Broadcast es "polsk" (noruego)
    "scenekunst": 16,  # CONFIRMADO: Oslo Fringe #oslofringe #scenekunst #humor
    "standup": 16,  # img1+: múltiples #Humor #Standup
    # ─── Karaoke (id: 17) ────────────────────────────────────────────────────
    "karaoke": 17,  # del .py original
    "livekaraoke": 17,  # CONFIRMADO: Vokalisten er syk #livekaraoke
    # ─── Christmas (id: 19) ──────────────────────────────────────────────────
    "jul": 19,  # del .py original
    # ─── Electronic / Experimental (id: 21) ──────────────────────────────────
    "electronic": 21,  # img2: MAGNET #Pride #Electronic #Club — tag genérico,
    # consistente con Kafé Hærverk donde también → 21
    "elektronika": 21,  # del .py original — igual que en MIR y Kafé Hærverk
    "elektroika": 21,  # img10: Bayonne #pop #elektronika (typo exacto de elektronika)
    # ─── Culture & Experiences (id: 22) ──────────────────────────────────────
    "arabic": 22,  # del .py original
    "dating": 22,  # img1: Pitch-A-Friend #show #dating
    "kultur": 22,  # del .py original
    "singelevent": 22,  # img7: Marthes SuperDuper SingelShow #singelevent
    # — evento social para solteros, no comedia
    "teater": 22,  # del .py original
    "verdensmijødag": 22,  # del .py original (typo — copiar exacto)
    # ─── Metal (id: 23) ──────────────────────────────────────────────────────
    "hardrock": 23,  # del .py original
    "metal": 23,  # del .py original
    # ─── Reggae & Ska (id: 24) ───────────────────────────────────────────────
    "dancehall": 24,  # CONFIRMADO: Jamaica Fest #reggae #dancehall #soca
    "reggae": 24,  # CONFIRMADO: Jamaica Fest #reggae #dancehall #soca
    "soca": 24,  # CONFIRMADO: Jamaica Fest #reggae #dancehall #soca
    # ─── Hits / Commercial (id: 25) ──────────────────────────────────────────
    "2000-tallet": 25,  # del .py original
    "nostalgi": 25,  # img10: NOSTALGIKLUBBEN #Klubb #2000-tallet #Nostalgi
}

# ─── TAGS ELIMINADOS Y RAZONES ───────────────────────────────────────────────
# "norsk"      → descriptor de idioma/origen, no categoría. Contexto: #rap #norsk #hiphop
# "polish"     → el tag real en Broadcast es "polsk" (ver arriba) — no "polish"
# "svensk"     → no encontrado en ningún evento de SALT en Broadcast
# "dansk"      → descriptor de idioma (#bingo #dansk #humor), igual que "english"
# "musikk"     → solo aparece junto a #bingo — contexto insuficiente para categorizar solo
# "uteservering" → descriptor de área exterior, no categoría
# "gratis"     → precio/gratuito, no categoría
# "english"    → descriptor de idioma, no categoría
# "show"       → demasiado ambiguo (comedia, teatro, concierto...)
# "rituale"    → movido a Themed (6) — contexto real: rituales de sauna, no música experimental
