"""
TAG_MAP — Mapeo COMPARTIDO de tags de eventos a IDs de categoría.
 
Los IDs de categoría (1, 3, 4, 6, ...) son globales del sistema (Festiva),
los mismos para todos los venues. Los tags se acumulan venue por venue.
 
Tags presentes en este mapa provienen de:
  - Kafé Hærverk  (origen de la mayoría)
  - KJ10          (marcados con "# KJ10")
  - Parkteatret   (marcados con "# Park")
 
Las entradas comentadas (#) no tienen una categoría clara — revísalas tú.
 
OJO Parkteatret: confirmé estos tags abriendo eventos en broadcast:
  musikk, rock, pop, jazz, prog, metal, folk, folkemusikk, folkrock,
  folkpop, singer-songwriter, hiphop, rap, u18, yngling.
Los ids para folk(13), musikk(10) y rap/hiphop los tomé de tu sistema
Festiva; verifica que sigan siendo correctos en tu esquema actual.
"""
 
TAG_MAP: dict[str, int] = {
    # Party (1)
    "club": 1,
    "nightclub": 1,        # KJ10
    "dancefloor": 1,       # KJ10
    "boilerroom": 1,       # KJ10
    "fest": 1,             # KJ10
    "event": 1,            # KJ10  (genérico)
    "dj": 1,               # KJ10
    "music": 1,            # KJ10  (genérico)
    "oslo": 1,             # KJ10  (genérico / ubicación)
    # Afrobeat (3)
    "afrobeat": 3,
    "soukus": 3,
    "caribbean": 3,
    # Techno / House (4)
    "acid": 4,
    "electro": 4,
    "house": 4,
    "techno": 4,
    "trance": 4,
    # Themed (6)
    # "gøyogmoro": 6,
    "fotball": 6,          # KJ10  (deporte/temático — igual que sport/vm en Festiva)
    # Indie / Rock (8)
    "guitarnois": 8,
    "indie": 8,
    "kraut": 8,
    "postpunk": 8,
    "postrock": 8,
    "prog": 8,             # también Park (WIZRD: #rock #jazz #prog)
    "psych": 8,
    "punk": 8,
    "rock": 8,             # también Park (varios conciertos)
    # Live / Musikk (10)  — id de tu sistema Festiva
    "musikk": 10,          # Park (genérico, aparece en casi todos los conciertos)
    # Jazz & Blues (11)
    "free-jazz": 11,
    "jazz": 11,            # también Park (Sven Wunder, WIZRD)
    "modal": 11,
    # Disco / Funk (12)
    "disco": 12,
    "funk": 12,
    # Folk / Americana (13)  — id de tu sistema Festiva  // Park
    "folk": 13,            # Park
    "folkemusikk": 13,     # Park
    "folkpop": 13,         # Park (Frøkedal)
    "folkrock": 13,        # Park (Frøkedal, John Vincent III)
    "singer-songwriter": 13,  # Park (Eileen Alister)
    # Pop (15)
    "kpop": 15,            # KJ10
    "pop": 15,             # también Park
    "synthpop": 15,
    # Comedy & Shows (16)
    "impro": 16,
    "podcast": 16,
    # Electronic / Experimental (21)
    "avantgard": 21,
    "eksperimentell": 21,
    "ebm": 21,
    "electronic": 21,
    "experimental": 21,
    "minimalist": 21,
    # Culture & Experiences (22)
    "panel": 22,
    "samtale": 22,
    "festival": 22,        # también Park (Orgivm Satanicvm, What The Folk)
    "festivl": 22,
    "musikkfest": 22,
    # Metal (23)
    "blackcore": 23,
    "grindcore": 23,
    "hardcore": 23,
    "metal": 23,           # Park (Orgivm Satanicvm)
    "svartmetall": 23,
    # ─────────────────────────────────────────────────────────────
    # Rap / Hip-hop  — Park (KLIKK9, Arif: #hiphop #rap)
    # No vi un id de Rap/Hip-hop en este mapa. Pon el id que uses
    # en tu esquema (en Festiva no recuerdo que lo fijáramos):
    # "hiphop": ??,        # Park
    # "rap": ??,           # Park
    #
    # Descriptores de edad/formato, NO categorías (igual que en otros venues):
    # "u18": ...,          # Park (conciertos "Yngling / fri alder")
    # "yngling": ...,      # Park
}
