# -*- coding: utf-8 -*-
"""
Baza mechanik WoW Classic / Forever:
- Zdolności rasowe (Racials) z analizą synergii PvE i PvP
- Wagi statystyk (Stat Weights) dla wszystkich 27 specjalizacji klasowych
- Silnik scoringu przedmiotów
"""

RACIAL_TRAITS = {
    "Human 🦁": {
        "faction": "Alliance",
        "traits": [
            {"name": "Sword Specialization", "type": "Passive", "desc": "+5 do umiejętności posługiwania się mieczami 1H i 2H. Zmniejsza szansę na 'Glancing Blow penalty' w PvE."},
            {"name": "Mace Specialization", "type": "Passive", "desc": "+5 do umiejętności posługiwania się obuchami 1H i 2H."},
            {"name": "Perception", "type": "Active", "desc": "Zwiększa wykrywanie niewidzialności na 20 sek. (3 min CD). Kluczowe w PvP przeciwko Rogalom i Feral Druidom."},
            {"name": "The Human Spirit", "type": "Passive", "desc": "+5% do bazowego współczynnika Spirit (Duch)."},
            {"name": "Diplomacy", "type": "Passive", "desc": "+10% do zdobywanej reputacji ze wszystkimi frakcjami."}
        ],
        "class_analysis": {
            "Warrior": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Absolutny Król PvE DPS w Przymierzu dzięki +5 Sword/Mace Spec."},
            "Rogue": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "BiS dla Combat Swords w raidach. Perception daje przewagę w walce z innymi Rogalami."},
            "Paladin": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "+5 do obuchów i mieczy wspiera Retribution, a Spirit pomaga Holy Paladynom."},
            "Priest": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "+5% Spirit zwiększa manaregen i leczenie z talentu Spiritual Guidance."},
            "Mage": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Brak bezpośrednich bonusów do czarów, ale szybsze wbijanie reputacji."},
            "Warlock": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Perception przydatne w obronie przed gankami, standardowy caster."}
        }
    },
    "Dwarf 🍺": {
        "faction": "Alliance",
        "traits": [
            {"name": "Stoneform", "type": "Active", "desc": "Usuwa efekty Bleed, Poison, Disease i daje +10% Armor na 8 sek. (3 min CD). Potężna obrona w PvP i PvE."},
            {"name": "Gun Specialization", "type": "Passive", "desc": "+5 do umiejętności posługiwania się bronią palną (Guns)."},
            {"name": "Frost Resistance", "type": "Passive", "desc": "+10 do odporności na magię mrozu."},
            {"name": "Find Treasure", "type": "Active", "desc": "Wykrywanie skrzyń ze skarbami na minimapie."},
            {"name": "Fear Ward (Priest Only)", "type": "Active", "desc": "Tarcza chroniąca przed kolejnym efektem Fear na 10 min (30s CD). Kluczowe na Onyxii i Magmadarze!"}
        ],
        "class_analysis": {
            "Warrior": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Stoneform kontruje Bleedy, Poisony i Blind u Rogali w PvP. Świetny tank."},
            "Hunter": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "+5 Gun Spec pod karabiny oraz Stoneform pozwalający uciec z Blind / Viper Sting."},
            "Priest": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "BiS Kapłan w Alliance. Fear Ward jest wymagany przez niemal każdą gildię rajdową."},
            "Paladin": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Niezwykle wytrzymały dzięki podwójnej defensywie: Bubble + Stoneform."},
            "Rogue": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Stoneform pozwala zresetować walkę i wejść w Stealth bez obawy o ticki trucizn i krwawień."}
        }
    },
    "Night Elf 🌙": {
        "faction": "Alliance",
        "traits": [
            {"name": "Shadowmeld", "type": "Active", "desc": "Wtopienie się w cienie (niewidzialność w miejscu poza walką). Umożliwia bezpieczne jedzenie/picie i zasadzki."},
            {"name": "Quickness", "type": "Passive", "desc": "+1% do szansy na unik (Dodge). Znakomity pasyw pod tankowanie."},
            {"name": "Wisp Spirit", "type": "Passive", "desc": "+50% do prędkości poruszania się jako ognik (Wisp) po śmierci."},
            {"name": "Nature Resistance", "type": "Passive", "desc": "+10 do odporności na magię natury."}
        ],
        "class_analysis": {
            "Warrior": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "+1% Dodge przydaje się tankom. Shadowmeld pozwala na niespodziewane Charge z ukrycia."},
            "Hunter": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Shadowmeld + chowaniec w stealth (np. kot) to zabójcza kombinacja na obronie flagi w WSG."},
            "Rogue": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Wyższy poziom ukrycia (Stealth level bonus), dobra mobilność i uniki."},
            "Druid": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Jedyny wybór dla Druida w Alliance. Świetna synergia z Prowl i defensywą."}
        }
    },
    "Gnome ⚙️": {
        "faction": "Alliance",
        "traits": [
            {"name": "Escape Artist", "type": "Active", "desc": "Usuwa wszelkie efekty unieruchomienia (Root) i spowolnienia (Snare) (0.5s cast, 1 min CD). Król PvP!"},
            {"name": "Expansive Mind", "type": "Passive", "desc": "+5% do bazowego współczynnika Intellect (Intelekt). Zwiększa manapool i Spell Crit."},
            {"name": "Engineering Specialization", "type": "Passive", "desc": "+15 do umiejętności Inżynierii."},
            {"name": "Arcane Resistance", "type": "Passive", "desc": "+10 do odporności na magię tajemną."}
        ],
        "class_analysis": {
            "Mage": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "BiS Caster w Alliance. +5% Mana/Crit w PvE oraz darmowe łamanie Frost Novek w PvP."},
            "Warlock": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Więcej many do Life Tap i Escape Artist ratujący przed usidleniem przez Melee."},
            "Rogue": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Escape Artist kontruje spowolnienia Frost Trap i Hamstring, mały hitbox ułatwia uniki."},
            "Warrior": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Najlepszy PvP Warrior w Alliance – likwiduje największą słabość Wojownika: Frost Novy i korzenie!"}
        }
    },
    "Orc 🪓": {
        "faction": "Horde",
        "traits": [
            {"name": "Blood Fury", "type": "Active", "desc": "+25% do bazowego Attack Power na 15 sek. (-50% leczenia otrzymywanego przez ten czas, 2 min CD)."},
            {"name": "Hardiness", "type": "Passive", "desc": "+25% dodatkowej szansy na oparcie się efektom ogłuszenia (Stun Resist). Koszmar każdego Rogala w PvP!"},
            {"name": "Axe Specialization", "type": "Passive", "desc": "+5 do umiejętności posługiwania się toporami 1H i 2H. Zmniejsza glancing penalty w rajdach."},
            {"name": "Command", "type": "Passive", "desc": "+5% do obrażeń zadawanych przez chowańce (Pety)." }
        ],
        "class_analysis": {
            "Warrior": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Absolutny Król Hordy. +5 Axe Spec i Blood Fury miażdżą w PvE, a Hardiness wygrywa pojedynki w PvP."},
            "Hunter": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Pet zadaje +5% więcej obrażeń (Command), a stun resist ratuje przed gankami Rogali."},
            "Rogue": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Blood Fury daje gigantyczny burst, a odporność na stuny czyni Orka Rogala pogromcą w mirror matchach."},
            "Shaman": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Enhancement Shaman z 2H toporem i Blood Fury zadaje dewastujące obrażenia Windfury."},
            "Warlock": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Chowańce biją mocniej, a 25% Stun Resist zamienia Warlocka w prawdziwy czołg w PvP."}
        }
    },
    "Undead 💀": {
        "faction": "Horde",
        "traits": [
            {"name": "Will of the Forsaken (WotF)", "type": "Active", "desc": "Zdejmuje Fear, Sleep, Charm i daje 5 sek. niewrażliwości (2 min CD). Najpotężniejszy skill PvP w grze."},
            {"name": "Cannibalize", "type": "Active", "desc": "Zjada zwłoki humanoida lub nieumarłego, regenerując 7% maksymalnego życia co 2 sek. przez 10 sek."},
            {"name": "Underwater Breathing", "type": "Passive", "desc": "+300% do limitu oddychania pod wodą."},
            {"name": "Shadow Resistance", "type": "Passive", "desc": "+10 do odporności na magię cienia."}
        ],
        "class_analysis": {
            "Rogue": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Ikona PvP. WotF pozwala bezkarnie atakować Priestów i Warlocków z Fearem."},
            "Mage": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Znakomity w pojedynkach PvP i na Battlegroundach. Cannibalize ułatwia oszczędzanie jedzenia."},
            "Warlock": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Warlock z WotF kontruje innych Warlocków i Kapłanów bez utraty kontroli nad chowańcem."},
            "Priest": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Dostęp do Devouring Plague (ogromny DoT i samoleczenie) + WotF."},
            "Warrior": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Dodatkowe łamanie feara obok Berserker Rage sprawia, że jesteś niemal odporny na kontrolę."}
        }
    },
    "Troll 🗿": {
        "faction": "Horde",
        "traits": [
            {"name": "Berserking", "type": "Active", "desc": "Zwiększa szybkość ataku i rzucania czarów o 10% do 30% (zależnie od brakującego zdrowia) na 10 sek."},
            {"name": "Bow & Throwing Specialization", "type": "Passive", "desc": "+5 do umiejętności posługiwania się łukami i bronią miotaną."},
            {"name": "Beast Slaying", "type": "Passive", "desc": "+5% do obrażeń zadawanych bestiom (Znakomite na raid bossach w MC/ZG!)."},
            {"name": "Regeneration", "type": "Passive", "desc": "+10% tempa regeneracji zdrowia; 10% regeneracji działa nawet w trakcie walki."}
        ],
        "class_analysis": {
            "Hunter": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Najwyższy PvE DPS dla Huntera w Hordzie (+5 Bow Spec + Berserking)."},
            "Mage": {"pve": "⭐⭐⭐⭐⭐ (S-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Berserking daje niesamowitą redukcję cast time w oknie burn fazy raidów."},
            "Priest": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Shadowguard zadaje pasywne obrażenia cienia, a Berserking przyspiesza leczenie w kryzysie."},
            "Shaman": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Berserking w połączeniu z Chain Heal potrafi uratować cały raid."},
            "Warrior": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐ (B-Tier)", "verdict": "Solidny PvE DPS i Threat generation dla tanka w walce z bossami."}
        }
    },
    "Tauren 🐂": {
        "faction": "Horde",
        "traits": [
            {"name": "War Stomp", "type": "Active", "desc": "Ogłusza do 5 przeciwników w promieniu 8 jardów na 2 sek. (0.5s cast, 2 min CD)."},
            {"name": "Endurance", "type": "Passive", "desc": "+5% do bazowego maksymalnego zdrowia (Health)."},
            {"name": "Cultivation", "type": "Passive", "desc": "+15 do umiejętności Zielarstwa (Herbalism)."},
            {"name": "Nature Resistance", "type": "Passive", "desc": "+10 do odporności na magię natury."}
        ],
        "class_analysis": {
            "Warrior": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐⭐ (S-Tier)", "verdict": "Większa pula punktów życia czyni Taurena wybitnym Main Tankiem. War Stomp gwarantuje pewne przerwanie czaru."},
            "Druid": {"pve": "⭐⭐⭐⭐ (A-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "Jedyny Druid w Hordzie. Bonus do HP wzmacnia formę niedźwiedzia (Bear Tank)."},
            "Shaman": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "War Stomp pozwala bezpiecznie rzucić Healing Wave lub uciec przed atakiem wrogów."},
            "Hunter": {"pve": "⭐⭐⭐ (B-Tier)", "pvp": "⭐⭐⭐⭐ (A-Tier)", "verdict": "War Stomp daje 2 sekundy na wyjście z Dead Zone i założenie pułapki (Freezing Trap)."}
        }
    }
}

# WAGI STATYSTYK DLA 27 SPECJALIZACJI KLASOWYCH
SPEC_WEIGHTS = {
    # Hunter
    "Beast Mastery (BM)": {"Agility": 2.0, "AP": 1.0, "Crit": 26.0, "Hit": 24.0, "Stamina": 0.4, "Intellect": 0.3},
    "Marksmanship (MM)": {"Agility": 2.4, "AP": 1.0, "Crit": 32.0, "Hit": 28.0, "Stamina": 0.3, "Intellect": 0.4},
    "Survival (SV)": {"Agility": 2.2, "AP": 1.0, "Crit": 28.0, "Hit": 26.0, "Stamina": 0.6, "Intellect": 0.3},

    # Warrior
    "Arms": {"Strength": 2.0, "AP": 1.0, "Crit": 30.0, "Hit": 22.0, "Agility": 1.4, "Stamina": 0.8},
    "Fury": {"Strength": 2.2, "AP": 1.0, "Crit": 32.0, "Hit": 26.0, "Agility": 1.6, "Stamina": 0.5},
    "Protection (Tank)": {"Stamina": 2.2, "Armor": 0.12, "Agility": 1.1, "Strength": 1.0, "Crit": 8.0, "Hit": 15.0},

    # Paladin
    "Holy (Healer)": {"SpellPower": 1.0, "Intellect": 0.8, "Crit": 16.0, "Spirit": 0.3, "Stamina": 0.4},
    "Protection (Tank)": {"Stamina": 2.0, "Armor": 0.12, "SpellPower": 0.8, "Strength": 0.8, "Agility": 0.8},
    "Retribution": {"Strength": 2.0, "AP": 1.0, "Crit": 28.0, "Hit": 22.0, "SpellPower": 0.5, "Agility": 1.2, "Stamina": 0.5},

    # Rogue
    "Assassination": {"Agility": 2.2, "AP": 1.0, "Strength": 1.0, "Crit": 30.0, "Hit": 26.0, "Stamina": 0.5},
    "Combat": {"Agility": 2.0, "AP": 1.0, "Strength": 1.1, "Crit": 28.0, "Hit": 28.0, "Stamina": 0.5},
    "Subtlety": {"Agility": 2.4, "AP": 1.0, "Strength": 1.0, "Crit": 32.0, "Hit": 22.0, "Stamina": 0.7},

    # Priest
    "Discipline": {"SpellPower": 1.0, "Intellect": 0.7, "Spirit": 0.8, "Crit": 10.0, "Stamina": 0.4},
    "Holy (Healer)": {"SpellPower": 1.0, "Spirit": 1.0, "Intellect": 0.6, "Crit": 10.0, "Stamina": 0.4},
    "Shadow": {"SpellPower": 1.0, "Hit": 18.0, "Crit": 12.0, "Intellect": 0.5, "Spirit": 0.3, "Stamina": 0.5},

    # Shaman
    "Elemental": {"SpellPower": 1.0, "Crit": 16.0, "Hit": 18.0, "Intellect": 0.6, "Spirit": 0.2, "Stamina": 0.4},
    "Enhancement": {"Strength": 2.0, "Agility": 1.6, "AP": 1.0, "Crit": 26.0, "Hit": 22.0, "SpellPower": 0.6},
    "Restoration (Healer)": {"SpellPower": 1.0, "Intellect": 0.7, "Spirit": 0.4, "Crit": 12.0, "Stamina": 0.4},

    # Mage
    "Arcane": {"SpellPower": 1.0, "Intellect": 0.7, "Hit": 16.0, "Crit": 12.0, "Spirit": 0.2},
    "Fire": {"SpellPower": 1.0, "Crit": 18.0, "Hit": 16.0, "Intellect": 0.4, "Spirit": 0.1},
    "Frost": {"SpellPower": 1.0, "Hit": 16.0, "Crit": 12.0, "Intellect": 0.5, "Stamina": 0.4},

    # Warlock
    "Affliction": {"SpellPower": 1.0, "Hit": 16.0, "Stamina": 0.6, "Crit": 10.0, "Intellect": 0.4},
    "Demonology": {"Stamina": 1.0, "SpellPower": 1.0, "Intellect": 0.5, "Hit": 14.0, "Crit": 10.0},
    "Destruction": {"SpellPower": 1.0, "Crit": 18.0, "Hit": 16.0, "Intellect": 0.4, "Stamina": 0.4},

    # Druid
    "Balance (Boomkin)": {"SpellPower": 1.0, "Crit": 14.0, "Hit": 16.0, "Intellect": 0.6, "Spirit": 0.3},
    "Feral (Bear/Cat)": {"Strength": 2.0, "Agility": 2.0, "AP": 1.0, "Stamina": 1.5, "Crit": 26.0, "Hit": 22.0, "Armor": 0.15},
    "Restoration (Healer)": {"SpellPower": 1.0, "Spirit": 0.9, "Intellect": 0.6, "Crit": 10.0, "Stamina": 0.4}
}

def calculate_item_score(item_data, spec_name):
    """
    Oblicza znormalizowaną punktację (Item Score) dla danego przedmiotu
    w oparciu o specyfikację wag statystyk (Stat Weights) dla wybranego speca.
    """
    weights = SPEC_WEIGHTS.get(spec_name, {})
    if not weights or not isinstance(item_data, dict):
        return 0.0
    
    score = 0.0
    for stat_key, weight in weights.items():
        val = item_data.get(stat_key, 0)
        try:
            val_float = float(val)
            score += val_float * weight
        except (ValueError, TypeError):
            continue
            
    return round(score, 1)

