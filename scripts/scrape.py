import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from src.clubs import (
    club_salt,
    club_rockefeller,
    club_kafehaerverk,
    club_mir,
    club_dattera,
    club_brødsirkus,
    club_brewgata,
    club_parksalongen,
    club_smelteverket,
    club_storgata,
    club_hausmania,
    club_kj10,
    club_parkteatret,
    club_røverstaden,
    club_oconnors_irish_pub,
    club_the_broker,
)
from src.processor import process_events

load_dotenv()


def main():
    all_events = []
    all_events += club_salt.get_events()
    all_events += club_rockefeller.get_events()
    all_events += club_kafehaerverk.get_events()
    all_events += club_mir.get_events()
    all_events += club_dattera.get_events()
    all_events += club_brødsirkus.get_events()
    all_events += club_brewgata.get_events()
    all_events += club_parksalongen.get_events()
    all_events += club_smelteverket.get_events()
    all_events += club_storgata.get_events()
    all_events += club_hausmania.get_events()
    all_events += club_kj10.get_events()
    all_events += club_parkteatret.get_events()
    all_events += club_røverstaden.get_events()
    all_events += club_oconnors_irish_pub.get_events()
    all_events += club_the_broker.get_events()

    process_events(all_events)


if __name__ == "__main__":
    main()
