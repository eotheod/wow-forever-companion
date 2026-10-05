import streamlit as st
import random
import pandas as pd
import json
import os
import base64
import urllib.parse
import xml.etree.ElementTree as ET
import altair as alt

# --- IMPORT DANYCH POMOCNICZYCH ---
from professions_data import PROFESSIONS_CATEGORIES, PROFESSIONS_DATA
from game_mechanics import RACIAL_TRAITS, SPEC_WEIGHTS, calculate_item_score

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="WoW Forever Companion",
    page_icon="⚔",
    layout="wide"
)

PAGE_HOME = "Home"
PAGE_NEWS = "News"
PAGE_GEN = "Generator"
PAGE_PROF = "Profesje"
PAGE_CLASS = "Klasy"
PAGE_STATUS = "Status"

if "page" not in st.session_state:
    st.session_state.page = PAGE_HOME

if "faction" not in st.session_state:
    st.session_state.faction = "Alliance 🦅"

if "lang" not in st.session_state:
    st.session_state.lang = "PL"

def set_page(page_name):
    st.session_state.page = page_name

def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    return ""

# --- SŁOWNIK TŁUMACZEŃ (PL / EN) ---
TRANSLATIONS = {
    "PL": {
        "faction_select": "Wybierz Frakcję (Motyw):",
        "lang_select": "Język / Language:",
        "subtitle": "Baza wiedzy, narzędzia i statystyki — Motyw:",
        "back_home": "⬅️️ Powrót do Strony Główniej",
        "welcome_title": "Witaj w bazie wiedzy WoW Forever!",
        "welcome_desc": "Wybierz moduł klikając w jeden z poniższych przycisków:",
        "nav_news": "📰 News & Blue Posts",
        "nav_news_desc": "Oficjalne ogłoszenia Blizzarda.",
        "nav_gen": "🎲 Generator Imion",
        "nav_gen_desc": "Unikalne nicki RP.",
        "nav_prof": "📜 Profesje",
        "nav_prof_desc": "Leveling 1-300.",
        "nav_class": "🛡️ Klasy & Przedmioty",
        "nav_class_desc": "Porównywarka i staty.",
        "nav_status": "🌐 Status Serwera",
        "nav_status_desc": "Realmy i statystyki.",
        # News
        "news_title": "📰 Oficjalne Wiadomości & Blue Posts (WoW Forever)",
        "news_subtitle": "Najnowsze komunikaty deweloperów Blizzarda i aktualizacje serwera WoW: Forever.",
        "news_source_btn": "🔗 Otwórz pełny Blue Tracker na bluetracker.gg",
        # Generator
        "gen_title": "🎲 Generator Imion (WoW Forever)",
        "gen_race": "Wybierz rasę:",
        "gen_gender": "Płeć:",
        "gen_male": "Mężczyzna",
        "gen_female": "Kobieta",
        "gen_class": "Wybierz klasę:",
        "gen_pattern": "Imię / Nick jako wzór:",
        "gen_count": "Liczba propozycji:",
        "gen_btn": "🎲 Wygeneruj Postacie",
        "gen_rp_name": "Pełna nazwa RP:",
        # Profesje
        "prof_title": "📜 Przewodnik Levelingu Profesji (WoW Forever 1-300)",
        "prof_subtitle": "Wzorowane na wow-professions.com/forever — optymalne, najtańsze trasy, Shopping List oraz porady [KEEP].",
        "prof_cat": "Kategoria profesji:",
        "prof_select": "Wybierz profesję:",
        "prof_tab_route": "🗺 Trasa Krok po Kroku (1-300)",
        "prof_tab_shop": "🛒 Shopping List (Materiały)",
        "prof_tab_keep": "⚠ Porady [KEEP] (Co zachować?)",
        "prof_req_mats": "🧪 Wymagane materiały:",
        "prof_do_count": "Wykonaj:",
        "prof_keep_badge": "⚠ [KEEP] ZACHOWAJ!",
        "prof_shop_desc": "Poniższa lista przedstawia przybliżoną ilość surowców niezbędnych do wbicia poziomu 300 najtańszą i najszybszą ścieżką.",
        "prof_keep_warning": "Wiele profesji w WoW Classic wymaga półproduktów wytworzonych we wczesnych etapach. Sprzedanie ich do vendora oznacza konieczność ponownego kupowania drogich surowców!",
        # Klasy i Przedmioty
        "class_tab_race": "📊 Porównywarka Ras",
        "class_tab_calc": "⚔️ Kalkulator i Porównywarka Przedmiotów",
        "race_title": "📊 Porównanie Ras dla Wybranej Klasy",
        "race_subtitle": "Dogłębna analiza zdolności rasowych (Racials), tier-listy PvE/PvP oraz synergii klasowej.",
        "race_select_class": "Wybierz klasę do analizy:",
        "race_filter_faction": "Filtruj frakcję:",
        "race_all": "Wszystkie",
        "race_available": "Dostępne rasy dla klasy",
        "race_pve": "⚔ Ocena PvE:",
        "race_pvp": "🛡 Ocena PvP:",
        "race_verdict": "🎯 Werdykt i synergia:",
        "race_traits": "Zdolności Rasowe (Racials):",
        "item_calc_title": "⚔ Kalkulator Przedmiotów & Porównywarka Speców",
        "item_calc_subtitle": "Precyzyjne wyliczanie wartości bojowej przedmiotów na podstawie wag statystyk dla twojej klasy i specjalizacji.",
        "item_select_class": "Wybierz klasę:",
        "item_select_spec": "Wybierz specjalizację (Spec):",
        "item_show_weights": "ℹ️ Pokaż priorytety statystyk dla:",
        "item_mode": "Wybierz tryb pracy:",
        "mode_browse": "📦 Przeglądaj Ekwipunek",
        "mode_search": "🔍 Szukaj w Bazie Przedmiotów",
        "mode_compare": "⚖️ Porównaj Przedmioty (A vs B)",
        "item_select_slot": "Wybierz slot ekwipunku (18 slotów):",
        "item_select_item": "Wybierz przedmiot ze slotu:",
        "item_score_breakdown": "📊 Rozbicie Wartości Bojowej:",
        "item_score_desc": "Jak statystyki przedmiotu przekładają się na punkty dla",
        # Status
        "status_title": "🌐 Status Serwerów & Statystyki Społeczności",
        "status_subtitle": "Dane z classicplus.io (census WoW: Forever) — aktualizowane automatycznie.",
        "status_realms_header": "🖥️ Realmy WoW Forever — Podział na Typy Serwerów",
        "status_census_header": "📊 Statystyki Populacji — Live z classicplus.io",
        "status_tested_chars": "📋 Zbadane postacie",
        "status_world_act": "⚔️ Aktywność w Świecie: PvP & Raidy"
    },
    "EN": {
        "faction_select": "Select Faction (Theme):",
        "lang_select": "Language / Język:",
        "subtitle": "Knowledge base, tools & stats — Theme:",
        "back_home": "⬅️ Back to Main Page",
        "welcome_title": "Welcome to WoW Forever Knowledge Base!",
        "welcome_desc": "Choose a module by clicking one of the buttons below:",
        "nav_news": "📰 News & Blue Posts",
        "nav_news_desc": "Official Blizzard updates.",
        "nav_gen": "🎲 Name Generator",
        "nav_gen_desc": "Unique RP Names.",
        "nav_prof": "📜 Professions",
        "nav_prof_desc": "1-300 Leveling Guide.",
        "nav_class": "🛡 Classes & Items",
        "nav_class_desc": "Comparator & Stat Weights.",
        "nav_status": "🌐 Server Status",
        "nav_status_desc": "Realms & Census Stats.",
        # News
        "news_title": "📰 Official News & Blue Posts (WoW Forever)",
        "news_subtitle": "Latest announcements from Blizzard developers and WoW: Forever updates.",
        "news_source_btn": "🔗 Open full Blue Tracker on bluetracker.gg",
        # Generator
        "gen_title": "🎲 Name Generator (WoW Forever)",
        "gen_race": "Select Race:",
        "gen_gender": "Gender:",
        "gen_male": "Male",
        "gen_female": "Female",
        "gen_class": "Select Class:",
        "gen_pattern": "Name / Pattern:",
        "gen_count": "Number of suggestions:",
        "gen_btn": "🎲 Generate Characters",
        "gen_rp_name": "Full RP Name:",
        # Professions
        "prof_title": "📜 Profession Leveling Guide (WoW Forever 1-300)",
        "prof_subtitle": "Inspired by wow-professions.com/forever — optimal routes, shopping list, and [KEEP] tips.",
        "prof_cat": "Profession Category:",
        "prof_select": "Select Profession:",
        "prof_tab_route": "🗺 Step-by-Step Route (1-300)",
        "prof_tab_shop": "🛒 Shopping List (Materials)",
        "prof_tab_keep": "⚠️ [KEEP] Tips (What to retain?)",
        "prof_req_mats": "🧪 Required Materials:",
        "prof_do_count": "Craft:",
        "prof_keep_badge": "⚠ [KEEP] RETAIN!",
        "prof_shop_desc": "The list below provides estimated materials required to reach skill level 300 efficiently.",
        "prof_keep_warning": "Many Classic professions require reagents crafted at earlier stages. Selling them to vendors forces expensive repurchases!",
        # Classes and Items
        "class_tab_race": "📊 Race Comparison",
        "class_tab_calc": "⚔️ Item Calculator & Comparison",
        "race_title": "📊 Race Comparison for Selected Class",
        "race_subtitle": "In-depth analysis of racial traits, PvE/PvP tier lists, and class synergies.",
        "race_select_class": "Select Class to analyze:",
        "race_filter_faction": "Filter Faction:",
        "race_all": "All",
        "race_available": "Available races for class",
        "race_pve": "⚔ PvE Rating:",
        "race_pvp": "🛡️ PvP Rating:",
        "race_verdict": "🎯 Verdict & Synergy:",
        "race_traits": "Racial Traits:",
        "item_calc_title": "⚔ Item Calculator & Spec Comparison",
        "item_calc_subtitle": "Calculate combat value based on specific stat weights for your class and spec.",
        "item_select_class": "Select Class:",
        "item_select_spec": "Select Specialization (Spec):",
        "item_show_weights": "ℹ️ Show stat priorities for:",
        "item_mode": "Select Mode:",
        "mode_browse": "📦 Browse Inventory",
        "mode_search": "🔍 Search Database",
        "mode_compare": "⚖️️ Compare Items (A vs B)",
        "item_select_slot": "Select Equipment Slot (18 slots):",
        "item_select_item": "Select Item from slot:",
        "item_score_breakdown": "📊 Combat Value Breakdown:",
        "item_score_desc": "How item stats translate into points for",
        # Status
        "status_title": "🌐 Server Status & Community Census",
        "status_subtitle": "Data from classicplus.io (WoW: Forever census) — auto-updated.",
        "status_realms_header": "🖥️ WoW Forever Realms — Server Types",
        "status_census_header": "📊 Population Stats — Live from classicplus.io",
        "status_tested_chars": "📋 Scanned Characters",
        "status_world_act": "⚔️ World Activity: PvP & Raids"
    }
}

def t(key):
    return TRANSLATIONS[st.session_state.lang].get(key, key)

# --- MAPOWANIE KLAS I DOKŁADNYCH SPECJALIZACJI (SPECS) ---
CLASS_SPECS = {
    "Hunter 🏹": ["Beast Mastery (BM)", "Marksmanship (MM)", "Survival (SV)"],
    "Warrior ⚔️": ["Arms", "Fury", "Protection (Tank)"],
    "Paladin 🔨": ["Holy (Healer)", "Protection (Tank)", "Retribution"],
    "Rogue 🗡️️": ["Assassination", "Combat", "Subtlety"],
    "Priest ✨": ["Discipline", "Holy (Healer)", "Shadow"],
    "Shaman ⚡": ["Elemental", "Enhancement", "Restoration (Healer)"],
    "Mage 🔮": ["Arcane", "Fire", "Frost"],
    "Warlock 📜": ["Affliction", "Demonology", "Destruction"],
    "Druid 🐾": ["Balance (Boomkin)", "Feral (Bear/Cat)", "Restoration (Healer)"]
}

# --- BAZA DANYCH BLUE POSTÓW ---
BLUE_POSTS_DATA = [
    {
        "title": "The World of Warcraft: Forever Beta Now Live",
        "date": "17 Wrz 2026, 21:00",
        "author": "Blizzard Community Team",
        "url": "https://www.bluetracker.gg/wow/topic/us-en/24304160-the-world-of-warcraft-forever-beta-now-live/",
        "summary": "Gracze zostają zaproszeni do zamkniętej bety World of Warcraft: Forever, aby odkryć na nowo oryginalny Azeroth z nową zawartością Classic+.",
        "content": """
        **Witajcie w World of Warcraft: Forever Beta!**

        Mamy ogromną przyjemność zaprosić pierwszą falę graczy do testów naszej długo oczekiwanej wersji *World of Warcraft: Forever*. 

        **Co nowego czeka na was w becie?**
        * **Przeorganizowany Azeroth Classic+**: Znane drogi i strefy kryją nowe sekrety, unikalne dungeony oraz nowe wątki fabularne.
        * **Długofalowa progresja**: Zwiększone wsparcie dla różnorodnych konfiguracji klasowych i profesji bez naruszania ducha gry z roku 2004.
        * **Dedykowany balans PvP & PvE**: Nowe mechaniki zapobiegające dominacji pojedynczych specjalizacji oraz zaktualizowane tabele statystyk.

        Dziękujemy za wasze stałe wsparcie i opinie na oficjalnych forach!
        """
    },
    {
        "title": "Development Update: Class Tuning & Racial Synergies",
        "date": "28 Wrz 2026, 18:30",
        "author": "Aggrend (WoW Classic Lead)",
        "url": "https://www.bluetracker.gg/wow/category/187-forever/",
        "summary": "Przegląd ostatnich zmian w balancie klas oraz korekty przeliczników siły i krytyka dla paladynów, szamanów i rogalów.",
        "content": """
        Wraz z napływem danych z ostatnich testów raidowych wprowadzamy istotne korekty balansowe:

        * **Paladin & Shaman**: Dopasowanie przeliczników Spell Power i Attack Power dla specjalizacji Hybrydowych (Retribution / Enhancement), aby zwiększyć ich użyteczność w rajdach 40-osobowych.
        * **Professions 1-300**: Skorygowano koszty surowców przy wyższych poziomach Engineering oraz Blacksmithing, redukując frustrujące "puste punkty" w craftingu.
        * **Racial Traits**: Analizujemy synergia zdolności rasowych Przymierza i Hordy pod kątem potyczek na Battlegroundach.
        """
    },
    {
        "title": "Realm Infrastructure & Anti-Queue System Improvements",
        "date": "02 Paź 2026, 14:15",
        "author": "Blizzard Technical Team",
        "url": "https://www.bluetracker.gg/wow/category/187-forever/",
        "summary": "Optymalizacja serwerów Everlook, Nordanaar oraz Warsong przed oficjalną premiarą sezonową.",
        "content": """
        Nasze zespoły inżynieryjne wdrożyły nowe aktualizacje serwerowe zorientowane na redukcję kolejek oraz zwiększenie wydajności w strefach z dużą zagęszczeniem graczy (np. Stranglethorn Vale oraz Blackrock Mountain).

        * Zwiększono przepustowość warstw (layering) przy zachowaniu spójności świata PvP.
        * Poprawiono stabilność integracji API ze statystykami populacji zewnętrznych serwisów.
        """
    }
]

# --- BAZA DANYCH DLA GENERATORA IMION ---
DATA_FOREVER = {
    "RACES": {
        "Human 🦅": {
            "classes": ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Mage", "Warlock"],
            "prefixes": ["Andu", "Artha", "Bol", "Val", "Roder", "Geri", "Ed", "Gaw", "Lorn", "Tael", "Uther", "Jaina", "Aethel", "Casp", "Garr"],
            "suffixes_m": ["in", "as", "var", "rick", "mond", "dor", "wald", "thas", "lion", "gard"],
            "suffixes_f": ["ina", "ria", "wen", "beth", "lynn", "dra", "stele", "vanya", "lora"],
            "surnames": ["Lightbringer", "Proudmoore", "Fordring", "Lothar", "Highwind", "Stormpike", "Valiant", "Brightwood", "Trueshot", "Greymane", "Dawnbringer", "Ironwill"]
        },
        "Dwarf 🍺": {
            "classes": ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Shaman"],
            "prefixes": ["Mural", "Magni", "Brann", "Thra", "Gim", "Bram", "Dur", "Dwer", "Kurg", "Thor", "Grel", "Hark", "Buro", "Garn"],
            "suffixes_m": ["din", "grim", "li", "mar", "gar", "mund", "keg", "oak", "anvil", "stone"],
            "suffixes_f": ["da", "fyr", "nis", "hild", "mora", "gret", "vanya", "thea", "runa"],
            "surnames": ["Bronzebeard", "Thunderbrew", "Ironforge", "Stoneshield", "Wildhammer", "Stormshield", "Alebarrel", "Deepminer", "Fireforge", "Barleybrew"]
        },
        "Orc 🪓": {
            "classes": ["Warrior", "Hunter", "Rogue", "Mage", "Warlock", "Shaman"],
            "prefixes": ["Grom", "Gar", "Throk", "Zug", "Karg", "Kor", "Mug", "Var", "Dra", "Mok", "Gol", "Krag", "Naz", "Rond"],
            "suffixes_m": ["gar", "dok", "gosh", "kash", "rok", "zog", "tar", "nak", "grom", "thar"],
            "suffixes_f": ["sha", "gra", "vka", "zara", "mora", "kya", "tara", "dora"],
            "surnames": ["Ironhide", "Hellscream", "Bloodfury", "Doomhammer", "Warsong", "Skullsplitter", "Frostwolf", "Deathtouch", "Shadowmoon", "Blackrock"]
        },
        "Undead 💀": {
            "classes": ["Warrior", "Paladin", "Rogue", "Priest", "Mage", "Warlock"],
            "prefixes": ["Mor", "Mali", "Dusk", "Grim", "Rath", "Slay", "Rot", "Blight", "Necro", "Varn", "Corps", "Mort", "Dread"],
            "suffixes_m": ["cor", "tis", "mort", "mord", "vus", "kriss", "bane", "rend", "gloom"],
            "suffixes_f": ["na", "vienna", "gloom", "sha", "tess", "rix", "mortis", "shade"],
            "surnames": ["Gravewalker", "Blightbane", "Rotweaver", "Soulrend", "Fellheart", "Plaguerunner", "Deathwhisper", "Dreadfang", "Shadowveil", "Bonecrusher"]
        },
        "Night Elf 🌙": {
            "classes": ["Warrior", "Hunter", "Rogue", "Priest", "Druid"],
            "prefixes": ["Thal", "Illi", "Mala", "Tyran", "Shan", "Fand", "Bael", "Cael", "Ared", "Kal", "Lyra"],
            "suffixes_m": ["dor", "rion", "ris", "dris", "thas", "vian", "lorn", "wind"],
            "suffixes_f": ["de", "ria", "stra", "sandra", "nea", "shara", "vanya", "thra"],
            "surnames": ["Whisperwind", "Stormrage", "Shadowsong", "Starlight", "Moonrunner", "Featherfall", "Nightbreeze", "Silverleaf", "Wildrunner"]
        },
        "Gnome ⚙️": {
            "classes": ["Warrior", "Rogue", "Priest", "Mage", "Warlock"],
            "prefixes": ["Gel", "Mekk", "Fiz", "Tink", "Kog", "Sprock", "Watt", "Volt", "Giz", "Nix"],
            "suffixes_m": ["bin", "fiz", "crank", "sprock", "plug", "bolt", "gear", "zap"],
            "suffixes_f": ["llie", "penn", "trix", "fizz", "spark", "wire", "cog"],
            "surnames": ["Highvoltage", "Gearspring", "Fizzywrench", "Microcog", "Copperwire", "Shortcircuit", "Steamvalve", "Turbine"]
        },
        "Troll 🗿": {
            "classes": ["Warrior", "Hunter", "Rogue", "Priest", "Mage", "Warlock", "Shaman"],
            "prefixes": ["Zul", "Vol", "Rast", "Rok", "Jad", "Sen", "Bwons", "Taz", "Mai"],
            "suffixes_m": ["jin", "zhar", "mar", "khan", "mon", "tul", "vaz"],
            "suffixes_f": ["tra", "mali", "zi", "zara", "voodoo", "nya"],
            "surnames": ["Darkspear", "Bloodscalp", "Skullsplitter", "Voodoo", "Shadowhunter", "Witchdoctor", "Voodoo-master"]
        },
        "Tauren 🐂": {
            "classes": ["Warrior", "Hunter", "Shaman", "Druid"],
            "prefixes": ["Cair", "Baine", "Karn", "Gorn", "Taur", "Mahn", "Mul", "Bov"],
            "suffixes_m": ["ne", "hoof", "brave", "sky", "horn", "runner", "walker"],
            "suffixes_f": ["mi", "toga", "runa", "mula", "flower", "grass"],
            "surnames": ["Bloodhoof", "Runetotem", "Thunderhorn", "Skychaser", "Wildmane", "Sunwalker", "Earthmother"]
        }
    },
    "TITLES": {
        "Warrior": ["Niszczyciel", "Niezłomny", "Żelazna Tarcza", "Mistrz Miecza", "Wściekły Topór"],
        "Paladin": ["Młot Światłości", "Święty Obrońca", "Mroczny Krzyżowiec", "Świetlisty Strażnik"],
        "Hunter": ["Tropiciel", "Ostre Oko", "Władca Bestii", "Cichy Strzelec"],
        "Rogue": ["Cichy Cień", "Niewidzialny", "Skrytobójca", "Mistrz Sztyletów"],
        "Priest": ["Obrońca Światłości", "Powiernik Dusz", "Piewca Cienia", "Apostoł"],
        "Shaman": ["Głos Żywiołów", "Powiadamiacz Burzy", "Opiekun Duchów", "Władca Płomieni"],
        "Mage": ["Tkacz Magii", "Arcymag", "Władca Płomieni", "Mroźny Mistrz"],
        "Warlock": ["Piewca Zagłady", "Przywoływacz Cieni", "Mroczny", "Lord Otchłani"],
        "Druid": ["Strażnik Natury", "Niedźwiedzia Siła", "Leśny Duch", "Władca Kniei"]
    }
}

# --- ULEPSZONY DYNAMICZNY GENERATOR DLA CUSTOM_NAME ---
def transform_custom_name(custom_name, race_data, is_male, index=0):
    clean_name = "".join(e for e in custom_name if e.isalnum())
    suffixes = race_data["suffixes_m"] if is_male else race_data["suffixes_f"]
    prefixes = race_data["prefixes"]
    
    if not clean_name:
        return f"{random.choice(prefixes)}{random.choice(suffixes)}"
    
    method = (index + random.randint(1, 100)) % 6
    suf = random.choice(suffixes)
    pref = random.choice(prefixes)
    
    if method == 0:
        base = clean_name[:3].capitalize() if len(clean_name) >= 3 else clean_name.capitalize()
        return f"{base}{suf}"
    elif method == 1:
        end_part = clean_name[-3:].lower() if len(clean_name) >= 3 else clean_name.lower()
        return f"{pref[:3]}{end_part}"
    elif method == 2:
        consonants = "".join([c for c in clean_name if c.lower() not in "aeeiouyóąęi"])
        base = consonants[:3].capitalize() if len(consonants) >= 2 else clean_name[:2].capitalize()
        return f"{base}{suf}"
    elif method == 3:
        rev_part = clean_name[::-1][:3].lower()
        return f"{pref[:2].capitalize()}{rev_part}{suf}"
    elif method == 4:
        mid = len(clean_name) // 2
        mid_part = clean_name[mid:mid+3].capitalize() if len(clean_name) >= 3 else clean_name.capitalize()
        return f"{mid_part}{suf}"
    else:
        first_letter = clean_name[0].upper()
        return f"{first_letter}{pref[1:].lower()}{suf}"

def generate_identity(dataset, race, char_class, gender, custom_name="", index=0):
    race_data = dataset["RACES"].get(race, list(dataset["RACES"].values())[0])
    is_male = (gender == "Mężczyzna" or gender == "Male")
    
    if custom_name.strip():
        first_name = transform_custom_name(custom_name, race_data, is_male, index=index)
    else:
        first_name = f"{random.choice(race_data['prefixes'])}{random.choice(race_data['suffixes_m'] if is_male else race_data['suffixes_f'])}"
        
    surname = random.choice(race_data["surnames"])
    title = random.choice(dataset["TITLES"].get(char_class, ["Wędrowiec"]))
    
    return first_name, f"{first_name} {surname} ({title})"

SLOTS_LIST = [
    "Głowa (Head)", "Szyja (Neck)", "Barki (Shoulders)", "Plecy (Back)", 
    "Klatka (Chest)", "Nadgarstki (Wrist)", "Dłonie (Hands)", "Pas (Waist)", 
    "Nogi (Legs)", "Stopy (Feet)", "Pierścień (Ring)", "Trinket", 
    "Broń 1H (One-Hand)", "Broń 2H (Two-Handed)", "Main-Hand", "Off-Hand", 
    "Tarcza (Shield)", "Broń Dystansowa (Ranged)"
]

def load_items_db():
    if os.path.exists("items_db.json"):
        try:
            with open("items_db.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for slot in SLOTS_LIST:
                    if slot not in data:
                        data[slot] = {}
                return data
        except Exception:
            pass
    default_db = {slot: {} for slot in SLOTS_LIST}
    default_db["Broń 1H (One-Hand)"]["Thunderfury, Blessed Blade of the Windseeker"] = {
        "id": 19019, "Stamina": 8, "Agility": 5, "AP": 20, "Dmg": "44 - 115", "Speed": "1.90", "DPS": "41.8", "WeaponType": "Miecz (Sword)", "Quality": "Legendary"
    }
    with open("items_db.json", "w", encoding="utf-8") as f:
        json.dump(default_db, f, indent=2, ensure_ascii=False)
    return default_db

def save_item_to_db(slot, item_name, item_data):
    db = load_items_db()
    if slot not in db:
        db[slot] = {}
    db[slot][item_name] = item_data
    with open("items_db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    return db

def search_items(query, selected_slot=None):
    db = load_items_db()
    results = {}
    q = query.strip().lower()
    if not q:
        return results
        
    if selected_slot and selected_slot in db:
        for name, data in db[selected_slot].items():
            if q in name.lower():
                results[f"{name} [{selected_slot}]"] = (selected_slot, name, data)
                
    for slot, items in db.items():
        if selected_slot and slot == selected_slot:
            continue
        for name, data in items.items():
            if q in name.lower():
                results[f"{name} [{slot}]"] = (slot, name, data)
                
    return results

def get_quality_color(item_data, item_name):
    quality = item_data.get("Quality", "")
    if quality == "Legendary" or "Thunderfury" in item_name or "Sulfuras" in item_name:
        return "#ff8000"
    elif quality == "Rare":
        return "#0070dd"
    elif quality == "Uncommon":
        return "#1eff00"
    return "#a335ee"

def render_wow_item_card(item_name, item_data, slot_name, target_spec, custom_border=None):
    color = get_quality_color(item_data, item_name)
    border_style = custom_border if custom_border else f"border: 2px solid {color};"
    score = calculate_item_score(item_data, target_spec)
    
    lines_html = []
    
    w_type = item_data.get("WeaponType", "")
    sub_line = f"<span>{slot_name}</span>"
    if w_type:
        sub_line += f"<span style='float:right;'>{w_type}</span>"
    lines_html.append(f"<div style='color: #ffffff; font-size: 0.95rem; margin-bottom: 5px; display:flex; justify-content:space-between;'>{sub_line}</div>")
    
    if "Dmg" in item_data:
        speed = item_data.get("Speed", "")
        dps = item_data.get("DPS", "")
        dmg_str = f"<span>{item_data['Dmg']} Damage</span>"
        if speed:
            dmg_str += f"<span style='float:right;'>Speed {speed}</span>"
        lines_html.append(f"<div style='color: #ffffff; font-size: 0.95rem; margin-bottom: 2px; display:flex; justify-content:space-between;'>{dmg_str}</div>")
        if dps:
            lines_html.append(f"<div style='color: #b0bec5; font-size: 0.85rem; margin-bottom: 6px;'>({dps} damage per second)</div>")
            
    if item_data.get("Armor", 0) > 0:
        lines_html.append(f"<div style='color: #ffffff; font-size: 0.95rem; margin-bottom: 6px;'>{item_data['Armor']} Armor</div>")
        
    primary_stats = [
        ("Strength", "Siła" if st.session_state.lang == "PL" else "Strength"),
        ("Agility", "Zręczność" if st.session_state.lang == "PL" else "Agility"),
        ("Stamina", "Wytrzymałość" if st.session_state.lang == "PL" else "Stamina"),
        ("Intellect", "Intelekt" if st.session_state.lang == "PL" else "Intellect"),
        ("Spirit", "Duch" if st.session_state.lang == "PL" else "Spirit")
    ]
    has_primary = False
    for key, pl_name in primary_stats:
        val = item_data.get(key, 0)
        if val > 0:
            lines_html.append(f"<div style='color: #ffffff; font-size: 0.95rem;'>+{val} {pl_name}</div>")
            has_primary = True
            
    if has_primary:
        lines_html.append("<div style='margin-bottom: 6px;'></div>")
        
    bonus_html = []
    if item_data.get("Crit", 0) > 0:
        bonus_html.append(f"Equip: Increases critical strike chance by +{item_data['Crit']}%.")
    if item_data.get("Hit", 0) > 0:
        bonus_html.append(f"Equip: Increases hit chance by +{item_data['Hit']}%.")
    if item_data.get("AP", 0) > 0:
        bonus_html.append(f"Equip: Increases attack power by +{item_data['AP']}.")
    if item_data.get("SpellPower", 0) > 0:
        bonus_html.append(f"Equip: Increases damage and healing of spells by up to +{item_data['SpellPower']}.")
        
    for b in bonus_html:
        lines_html.append(f"<div style='color: #1eff00; font-size: 0.92rem; margin-top: 4px; line-height: 1.3;'>{b}</div>")
        
    body_content = "".join(lines_html)
    
    return f"""
    <div style="background: #0d1217; {border_style} border-radius: 8px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.8); margin-bottom: 12px;">
        <div style="font-size: 1.35rem; font-weight: bold; color: {color}; text-shadow: 1px 1px 3px #000; margin-bottom: 8px;">
            {item_name}
        </div>
        {body_content}
        <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid #232c36; display: flex; justify-content: space-between; align-items: center;">
            <span style="color: #94a3b8; font-size: 0.85rem;">Score for: <b style="color: #fff;">{target_spec}</b></span>
            <span style="background: #112818; border: 1px solid #2ecc71; color: #2ecc71; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 1.15rem;">
                ⭐ {score} pts
            </span>
        </div>
    </div>
    """

ITEMS_DB = load_items_db()

# --- STYLIZACJA CSS FACTION THEMES (3D & ORYGINALNE BANERY) ---
if "Alliance" in st.session_state.faction:
    bg_gradient = "radial-gradient(circle at center, #10243e 0%, #070d14 100%)"
    banner_bg = "linear-gradient(180deg, rgba(16,42,69,0.4) 0%, rgba(10,25,47,0.85) 100%)"
    banner_img = "https://images.blz-contentstack.com/v3/assets/blt3452e3b114fab0cd/blt870c9d747a8ef0f9/611a919313cdcd0e89139265/Stormwind_1.jpg"
    border_color = "#00a2ff"
    text_gold = "#66c2ff"
    
    # 3D Przycisk Przymierza
    btn_grad = "linear-gradient(180deg, #1e4570 0%, #0b1f36 50%, #061324 100%)"
    btn_border_top = "#4a8ace"
    btn_border_bottom = "#02070e"
    btn_glow = "rgba(0, 162, 255, 0.5)"
    logo_file = "assets/alliance_logo.jpg"
else:
    bg_gradient = "radial-gradient(circle at center, #3d1010 0%, #0d0404 100%)"
    banner_bg = "linear-gradient(180deg, rgba(69,16,16,0.4) 0%, rgba(42,8,8,0.85) 100%)"
    banner_img = "https://images.blz-contentstack.com/v3/assets/blt3452e3b114fab0cd/blt5696d54d241d7237/611a914108d6d60e7e192739/Orgrimmar_1.jpg"
    border_color = "#ff3333"
    text_gold = "#ff8080"
    
    # 3D Przycisk Hordy
    btn_grad = "linear-gradient(180deg, #701e1e 0%, #360b0b 50%, #240606 100%)"
    btn_border_top = "#ce4a4a"
    btn_border_bottom = "#0e0202"
    btn_glow = "rgba(255, 51, 51, 0.5)"
    logo_file = "assets/horde_logo.jpg"

st.markdown(f"""
<style>
    .main {{ 
        background: {bg_gradient}; 
        color: #e0e0e0; 
        background-attachment: fixed;
    }}
    [data-testid="stSidebar"] {{ display: none; }}

    .title-banner {{
        text-align: center;
        padding: 30px 20px;
        background: url('{banner_img}') center/cover no-repeat, {banner_bg};
        background-blend-mode: overlay;
        border-bottom: 3px solid {border_color};
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.8), 
                    inset 0 0 15px rgba(0, 0, 0, 0.6);
        border: 2px solid {border_color};
    }}
    .title-banner h1 {{
        color: {text_gold};
        font-family: 'Cinzel', serif, sans-serif;
        text-shadow: 3px 3px 8px #000000, 0 0 15px {border_color};
        margin: 0;
        font-size: 2.8rem;
    }}

    .result-card {{
        background: linear-gradient(145deg, #182028 0%, #0d1217 100%);
        border: 2px solid #283545;
        border-left: 6px solid {border_color};
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 16px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.7), 
                    inset 0 1px 1px rgba(255, 255, 255, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }}
    .result-card:hover {{
        transform: translateY(-5px) scale(1.01);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.9), 0 0 15px {btn_glow};
        border-color: {border_color};
    }}

    /* STYL BLUE POSTA BLIZZARDA */
    .blue-post-card {{
        background: linear-gradient(180deg, #0a192f 0%, #06101e 100%);
        border: 2px solid #00a2ff;
        border-left: 6px solid #00a2ff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(0, 162, 255, 0.2);
    }}

    div.stButton > button {{
        background: {btn_grad} !important;
        color: {text_gold} !important;
        border-top: 2px solid {btn_border_top} !important;
        border-left: 2px solid {btn_border_top} !important;
        border-bottom: 4px solid {btn_border_bottom} !important;
        border-right: 3px solid {btn_border_bottom} !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 1.05rem !important;
        text-shadow: 1px 2px 4px #000000 !important;
        padding: 12px 20px !important;
        width: 100% !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.7) !important;
        transition: all 0.15s ease-in-out !important;
        cursor: pointer !important;
    }}

    div.stButton > button:hover {{
        color: #ffffff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.8), 0 0 15px {btn_glow} !important;
        border-top-color: #ffffff !important;
    }}

    div.stButton > button:active {{
        transform: translateY(3px) !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.9) !important;
        border-bottom-width: 1px !important;
    }}
</style>
""", unsafe_allow_html=True)

# WYBÓR FRAKCJI I JĘZYKA W JEDNYM WIERSZU
top_col1, top_col2, top_col3 = st.columns([3, 1.2, 1])
with top_col2:
    selected_faction = st.selectbox(t("faction_select"), ["Alliance 🦅", "Horde 🪓"], index=0 if "Alliance" in st.session_state.faction else 1)
    if selected_faction != st.session_state.faction:
        st.session_state.faction = selected_faction
        st.rerun()

with top_col3:
    selected_lang = st.selectbox(t("lang_select"), ["Polski (PL)", "English (EN)"], index=0 if st.session_state.lang == "PL" else 1)
    new_lang_code = "PL" if "Polski" in selected_lang else "EN"
    if new_lang_code != st.session_state.lang:
        st.session_state.lang = new_lang_code
        st.rerun()

# PRZYGOTOWANIE LOGO DO BANERU
logo_b64 = get_image_base64(logo_file)

if logo_b64:
    header_content = f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="data:image/jpeg;base64,{logo_b64}" style="height: 80px; vertical-align: middle; margin-right: 20px; filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.9)); border-radius: 8px;">
        <div>
            <h1 style="margin: 0;">WOW FOREVER COMPANION</h1>
            <p style="color: #ffffff; text-shadow: 2px 2px 4px #000; margin-top: 5px;">{t("subtitle")} {st.session_state.faction}</p>
        </div>
    </div>
    """
else:
    header_content = f"""
    <div>
        <h1 style="margin: 0;">WOW FOREVER COMPANION</h1>
        <p style="color: #ffffff; text-shadow: 2px 2px 4px #000; margin-top: 5px;">{t("subtitle")} {st.session_state.faction}</p>
    </div>
    """

# BANNER TYTUŁOWY
st.markdown(f'<div class="title-banner">{header_content}</div>', unsafe_allow_html=True)

if st.session_state.page != PAGE_HOME:
    if st.button(t("back_home"), key="btn_back_top"):
        set_page(PAGE_HOME)
        st.rerun()

# ==========================================
# 1. STRONA GŁÓWNA
# ==========================================
if st.session_state.page == PAGE_HOME:
    st.subheader(t("welcome_title"))
    st.write(t("welcome_desc"))
    st.write("---")
    col0, col1, col2, col3, col4 = st.columns(5)
    with col0:
        if st.button(t("nav_news"), use_container_width=True, key="h_btn_news"):
            set_page(PAGE_NEWS)
            st.rerun()
        st.caption(t("nav_news_desc"))
    with col1:
        if st.button(t("nav_gen"), use_container_width=True, key="h_btn_gen"):
            set_page(PAGE_GEN)
            st.rerun()
        st.caption(t("nav_gen_desc"))
    with col2:
        if st.button(t("nav_prof"), use_container_width=True, key="h_btn_prof"):
            set_page(PAGE_PROF)
            st.rerun()
        st.caption(t("nav_prof_desc"))
    with col3:
        if st.button(t("nav_class"), use_container_width=True, key="h_btn_class"):
            set_page(PAGE_CLASS)
            st.rerun()
        st.caption(t("nav_class_desc"))
    with col4:
        if st.button(t("nav_status"), use_container_width=True, key="h_btn_status"):
            set_page(PAGE_STATUS)
            st.rerun()
        st.caption(t("nav_status_desc"))

# ==========================================
# 2. NEWS & BLUE POSTS
# ==========================================
elif st.session_state.page == PAGE_NEWS:
    st.subheader(t("news_title"))
    st.caption(t("news_subtitle"))
    
    st.markdown(f"[🔗 Otwórz Blue Tracker bezpośrednio na bluetracker.gg](https://www.bluetracker.gg/wow/category/187-forever/)")
    st.write("---")
    
    for post in BLUE_POSTS_DATA:
        st.markdown(f"""
        <div class="blue-post-card">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #00a2ff; padding-bottom: 8px; margin-bottom: 12px;">
                <span style="font-size: 1.25rem; font-weight: bold; color: #00a2ff;">🔹 {post['title']}</span>
                <span style="color: #88aacc; font-size: 0.85rem;">{post['date']} | Autor: <b>{post['author']}</b></span>
            </div>
            <div style="font-size: 0.95rem; color: #d0e5ff; margin-bottom: 12px;">
                {post['summary']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"📖 Czytaj pełny Blue Post: {post['title']}", expanded=False):
            st.markdown(post["content"])
            st.markdown(f"[🔗 Zobacz oryginalny wątek na Blue Tracker]({post['url']})")

# ==========================================
# 3. GENERATOR IMION
# ==========================================
elif st.session_state.page == PAGE_GEN:
    st.subheader(t("gen_title"))
    col1, col2 = st.columns(2)
    with col1:
        race_f = st.selectbox(t("gen_race"), list(DATA_FOREVER["RACES"].keys()))
        gender_f = st.radio(t("gen_gender"), [t("gen_male"), t("gen_female")])
    with col2:
        available_classes_f = DATA_FOREVER["RACES"][race_f]["classes"]
        class_f = st.selectbox(t("gen_class"), available_classes_f)
        custom_f = st.text_input(t("gen_pattern"), placeholder="np. Arthas / Shadowmage")

    count_f = st.slider(t("gen_count"), min_value=1, max_value=20, value=5)

    if st.button(t("gen_btn"), type="primary", use_container_width=True):
        st.write("---")
        used_nicks = set()
        for i in range(count_f):
            nick, full_rp = generate_identity(DATA_FOREVER, race_f, class_f, gender_f, custom_f, index=i)
            
            while nick in used_nicks:
                nick += random.choice(["n", "r", "d", "s", "m"])
                full_rp = f"{nick} {random.choice(DATA_FOREVER['RACES'][race_f]['surnames'])}"
            used_nicks.add(nick)
            
            st.markdown(f"""
            <div class="result-card">
                <div style="font-size: 1.3rem; font-weight: bold; color: #fff;">{i+1}. {nick}</div>
                <div style="color: #a0aab5;">{t('gen_rp_name')} <b>{full_rp}</b></div>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 4. PROFESJE (1-300 LEVELING GUIDE)
# ==========================================
elif st.session_state.page == PAGE_PROF:
    st.subheader(t("prof_title"))
    st.caption(t("prof_subtitle"))
    
    col_c1, col_c2 = st.columns([1, 2])
    with col_c1:
        cat_select = st.selectbox(t("prof_cat"), list(PROFESSIONS_CATEGORIES.keys()))
    with col_c2:
        available_profs = PROFESSIONS_CATEGORIES[cat_select]
        selected_prof = st.selectbox(t("prof_select"), available_profs)
        
    prof_info = PROFESSIONS_DATA.get(selected_prof, {})
    
    if prof_info:
        st.markdown(f"""
        <div class="result-card">
            <h3 style="margin-top:0; color:{text_gold};">{selected_prof} — {prof_info.get('category')}</h3>
            <p style="margin-bottom:0;">{prof_info.get('desc', '')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        p_tab1, p_tab2, p_tab3 = st.tabs([t("prof_tab_route"), t("prof_tab_shop"), t("prof_tab_keep")])
        
        with p_tab1:
            st.markdown(f"#### {t('prof_tab_route')}")
            if "steps" in prof_info:
                current_rank = None
                for s in prof_info["steps"]:
                    try:
                        start_lvl = int(s["range"].split("-")[0].strip())
                    except ValueError:
                        start_lvl = 1
                        
                    rank_name = None
                    if start_lvl <= 75 and current_rank != "Apprentice (1 - 75)":
                        rank_name = "🔰 Apprentice (1 - 75)"
                        current_rank = "Apprentice (1 - 75)"
                    elif 75 < start_lvl <= 150 and current_rank != "Journeyman (75 - 150)":
                        rank_name = "🛡️ Journeyman (75 - 150)"
                        current_rank = "Journeyman (75 - 150)"
                    elif 150 < start_lvl <= 225 and current_rank != "Expert (150 - 225)":
                        rank_name = "⚔ Expert (150 - 225)"
                        current_rank = "Expert (150 - 225)"
                    elif start_lvl > 225 and current_rank != "Artisan (225 - 300)":
                        rank_name = "👑 Artisan (225 - 300)"
                        current_rank = "Artisan (225 - 300)"
                    
                    if rank_name:
                        st.markdown(f"### {rank_name}")
                    
                    keep_badge = f'<span style="background-color: #b38600; color: #fff; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem; margin-left: 10px;">{t("prof_keep_badge")}</span>' if s.get("keep") else ''
                    
                    st.markdown(f"""
                    <div style="background: #1c2228; border-left: 4px solid {border_color}; padding: 12px 15px; border-radius: 6px; margin-bottom: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-size: 1.15rem; font-weight: bold; color: #ffffff;">
                                <span style="color: {text_gold}; font-family: monospace;">[{s['range']}]</span> {s['item']} {keep_badge}
                            </span>
                            <span style="background: #2a333c; color: #a0c0e0; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">
                                {t('prof_do_count')} {s['count']}
                            </span>
                        </div>
                        <div style="font-size: 0.95rem; color: #c0c6cc; margin-bottom: 4px;">
                            <b>{t('prof_req_mats')}</b> <span style="color: #ffda79;">{s['mats']}</span>
                        </div>
                        <div style="font-size: 0.88rem; color: #8e9ca8; font-style: italic;">
                            💡 {s['note']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            elif "zones" in prof_info:
                for z in prof_info["zones"]:
                    st.markdown(f"""
                    <div style="background: #1c2228; border-left: 4px solid {border_color}; padding: 14px 16px; border-radius: 6px; margin-bottom: 12px;">
                        <div style="font-size: 1.15rem; font-weight: bold; color: {text_gold}; margin-bottom: 6px;">
                            📍 Level: <span style="font-family: monospace; color: #fff;">[{z['range']}]</span> — {z['ore']}
                        </div>
                        <div style="font-size: 0.95rem; color: #e0e0e0; margin-bottom: 6px;">
                            <b>🗺️️ Recommended Zones / Spots:</b> <span style="color: #66c2ff;">{z['zones']}</span>
                        </div>
                        <div style="font-size: 0.88rem; color: #8e9ca8; font-style: italic;">
                            💡 <b>Tip:</b> {z['tips']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
        with p_tab2:
            st.markdown(f"#### {t('prof_tab_shop')}")
            st.info(t("prof_shop_desc"))
            shop_data = []
            for item, qty, note in prof_info.get("shopping_list", []):
                shop_data.append({
                    "Reagent": item,
                    "Amount": qty,
                    "Note": note
                })
            st.dataframe(pd.DataFrame(shop_data), use_container_width=True, hide_index=True)
            
        with p_tab3:
            st.markdown(f"#### {t('prof_tab_keep')}")
            st.warning(t("prof_keep_warning"))
            for tip in prof_info.get("keep_items", []):
                st.markdown(f"""
                <div style="background: #251e12; border-left: 5px solid #d49a15; padding: 12px 16px; border-radius: 6px; margin-bottom: 10px; color: #ffebaa;">
                    {tip}
                </div>
                """, unsafe_allow_html=True)

# ==========================================
# 5. KLASY I PRZEDMIOTY
# ==========================================
elif st.session_state.page == PAGE_CLASS:
    tab_class, tab_items = st.tabs([t("class_tab_race"), t("class_tab_calc")])
    
    with tab_class:
        st.subheader(t("race_title"))
        st.caption(t("race_subtitle"))
        
        col_cl, col_fa = st.columns([2, 2])
        with col_cl:
            all_classes = sorted(list(set(c for r in DATA_FOREVER["RACES"].values() for c in r["classes"])))
            selected_class = st.selectbox(t("race_select_class"), all_classes, key="sb_class_analysis")
        with col_fa:
            faction_filter = st.radio(t("race_filter_faction"), [t("race_all"), "Alliance 🦅", "Horde 🪓"], horizontal=True)
            
        valid_races = [race for race, data in DATA_FOREVER["RACES"].items() if selected_class in data["classes"]]
        if faction_filter == "Alliance 🦅":
            valid_races = [r for r in valid_races if RACIAL_TRAITS.get(r, {}).get("faction") == "Alliance"]
        elif faction_filter == "Horde 🪓":
            valid_races = [r for r in valid_races if RACIAL_TRAITS.get(r, {}).get("faction") == "Horde"]
            
        st.write(f"{t('race_available')} **{selected_class}**: **{len(valid_races)}**")
        
        for r in valid_races:
            race_meta = RACIAL_TRAITS.get(r, {})
            class_analysis = race_meta.get("class_analysis", {}).get(selected_class, {})
            pve_rating = class_analysis.get("pve", "⭐⭐⭐ (B-Tier)")
            pvp_rating = class_analysis.get("pvp", "⭐⭐⭐ (B-Tier)")
            verdict = class_analysis.get("verdict", "Solid race choice.")
            faction_badge = "🦅 Alliance" if race_meta.get("faction") == "Alliance" else "🪓 Horde"
            
            with st.expander(f"{r} — PvE: {pve_rating.split(' ')[0]} | PvP: {pvp_rating.split(' ')[0]} ({faction_badge})", expanded=True):
                col_r1, col_r2 = st.columns([1, 1])
                with col_r1:
                    st.markdown(f"**{t('race_pve')}** {pve_rating}")
                with col_r2:
                    st.markdown(f"**{t('race_pvp')}** {pvp_rating}")
                
                st.markdown(f"""
                <div style="background: #1b2229; padding: 10px 14px; border-radius: 6px; margin: 8px 0; border-left: 3px solid {border_color};">
                    <b>{t('race_verdict')}</b> {verdict}
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"**{t('race_traits')}**")
                for trait in race_meta.get("traits", []):
                    badge_color = "#3867d6" if trait["type"] == "Active" else "#20bf6b"
                    st.markdown(f"""
                    <div style="margin-bottom: 6px; font-size: 0.9rem;">
                        <span style="background:{badge_color}; color:#fff; padding:2px 6px; border-radius:4px; font-size:0.75rem; font-weight:bold;">{trait['type']}</span>
                        <b style="color: #fff; margin-left: 5px;">{trait['name']}:</b> <span style="color: #b0bec5;">{trait['desc']}</span>
                    </div>
                    """, unsafe_allow_html=True)

    with tab_items:
        st.subheader(t("item_calc_title"))
        st.caption(t("item_calc_subtitle"))
        
        col_c, col_s = st.columns(2)
        with col_c:
            target_class = st.selectbox(t("item_select_class"), list(CLASS_SPECS.keys()), key="item_calc_class")
        with col_s:
            available_specs = CLASS_SPECS[target_class]
            target_spec = st.selectbox(t("item_select_spec"), available_specs, key="item_calc_spec")
            
        weights = SPEC_WEIGHTS.get(target_spec, {})
        with st.expander(f"{t('item_show_weights')} {target_spec}", expanded=False):
            stat_labels = {
                "Strength": "Siła" if st.session_state.lang == "PL" else "Strength",
                "Agility": "Zręczność" if st.session_state.lang == "PL" else "Agility",
                "Stamina": "Wytrzymałość" if st.session_state.lang == "PL" else "Stamina",
                "Intellect": "Intelekt" if st.session_state.lang == "PL" else "Intellect",
                "Spirit": "Duch" if st.session_state.lang == "PL" else "Spirit",
                "AP": "Attack Power", "Crit": "Crit", "Hit": "Hit", "SpellPower": "Spell Power"
            }
            cols_w = st.columns(4)
            c_idx = 0
            for stat_name, weight in weights.items():
                pl = stat_labels.get(stat_name, stat_name)
                with cols_w[c_idx % 4]:
                    st.markdown(f"""
                    <div style="background: #1a222a; border-left: 3px solid {border_color}; padding: 6px 10px; border-radius: 4px; margin-bottom: 6px;">
                        <span style="color: #ffffff; font-size: 0.9rem;">{pl}:</span> <b style="color: {text_gold}; font-size: 0.95rem;">x{weight}</b>
                    </div>
                    """, unsafe_allow_html=True)
                c_idx += 1
            
        st.write("---")
        
        calc_mode = st.radio(
            t("item_mode"), 
            [t("mode_browse"), t("mode_search"), t("mode_compare")], 
            horizontal=True
        )
        
        if calc_mode == t("mode_browse"):
            selected_slot = st.selectbox(t("item_select_slot"), SLOTS_LIST, key="sb_slot_browse")
            items_in_slot = ITEMS_DB.get(selected_slot, {})
            
            if not items_in_slot:
                st.warning(f"No items in slot '{selected_slot}'.")
            else:
                chosen_item_name = st.selectbox(t("item_select_item"), list(items_in_slot.keys()), key="sb_chosen_item")
                item_data = items_in_slot[chosen_item_name]
                
                col_i1, col_i2 = st.columns([1, 1])
                with col_i1:
                    st.markdown(render_wow_item_card(chosen_item_name, item_data, selected_slot, target_spec), unsafe_allow_html=True)
                with col_i2:
                    st.markdown(f"#### {t('item_score_breakdown')}")
                    st.write(f"{t('item_score_desc')} **{target_spec}**:")
                    
                    score_breakdown = []
                    for stat_key, w in weights.items():
                        val = item_data.get(stat_key, 0)
                        if val > 0:
                            pts = round(val * w, 1)
                            score_breakdown.append({
                                "Stat": stat_key,
                                "Item Value": f"+{val}",
                                "Weight": f"x{w}",
                                "Points": f"+{pts} pts"
                            })
                    if score_breakdown:
                        st.dataframe(pd.DataFrame(score_breakdown), use_container_width=True, hide_index=True)

# ==========================================
# 6. STATUS SERWERA & STATS
# ==========================================
elif st.session_state.page == PAGE_STATUS:
    import requests
    import re as re_mod

    st.subheader(t("status_title"))
    st.caption(t("status_subtitle"))

    @st.cache_data(ttl=900)
    def fetch_classicplus_census():
        try:
            url = "https://classicplus.io/"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            r = requests.get(url, headers=headers, timeout=6)
            if r.status_code == 200:
                m = re_mod.search(r'<script id="cp-census" type="application/json">(.*?)</script>', r.text, re_mod.DOTALL)
                if m:
                    return json.loads(m.group(1))
        except Exception:
            pass
        return None

    def compute_census_stats(data, realm_key="all"):
        classes = data["classes"]
        races = data["races"]
        combos = data["combos"]
        counts = data["datasets"][realm_key]["counts"]
        total = sum(counts)
        faction_counts = {"Alliance": 0, "Horde": 0}
        class_counts = {c["name"]: 0 for c in classes}
        for idx, cnt in enumerate(counts):
            if idx >= len(combos):
                continue
            combo = combos[idx]
            r_idx = combo["race"]
            c_idx = combo["class"]
            if r_idx < len(races) and c_idx < len(classes):
                faction_counts[races[r_idx]["faction"]] += cnt
                class_counts[classes[c_idx]["name"]] += cnt
        return total, faction_counts, class_counts

    st.markdown(f"### {t('status_realms_header')}")
    realms_all = [
        {"Nazwa Realmu": "⚔️ Everlook [PvP]", "Kategoria": "PvP", "Typ": "Classic+ PvP", "Zasady": "Otwarte PvP w strefach spornych, walka o bazy i stolice", "Status": "🟢 Online", "Populacja": "High (Full)", "Gracze Online": 6120, "Bilans A:H": "51% : 49%", "Ping": "22 ms"},
        {"Nazwa Realmu": "⚔️ Warsong [PvP]", "Kategoria": "PvP", "Typ": "Classic Fresh PvP", "Zasady": "Dynamiczne potyczki w STV, ranking Honoru i ranga 14", "Status": "🟢 Online", "Populacja": "Medium", "Gracze Online": 2850, "Bilans A:H": "49% : 51%", "Ping": "19 ms"},
        {"Nazwa Realmu": "💀 Tel'Abim [Hardcore PvP]", "Kategoria": "PvP", "Typ": "Hardcore PvP (Permadeath)", "Zasady": "1 życie na postać + włączone otwarte PvP w świecie", "Status": "🟢 Online", "Populacja": "Medium", "Gracze Online": 1245, "Bilans A:H": "48% : 52%", "Ping": "29 ms"},
        {"Nazwa Realmu": "🛡️ Nordanaar [PvE]", "Kategoria": "PvE", "Typ": "Classic+ PvE", "Zasady": "Bezpieczny leveling, PvP na życzenie (/pvp) lub Battlegroundy", "Status": "🟢 Online", "Populacja": "High", "Gracze Online": 4480, "Bilans A:H": "54% : 46%", "Ping": "25 ms"},
        {"Nazwa Realmu": "🛡️ Darrowshire [PvE]", "Kategoria": "PvE", "Typ": "Normal PvE", "Zasady": "Spokojna eksploracja, dungeony i raidy endgame bez ganków", "Status": "🟢 Online", "Populacja": "Low", "Gracze Online": 980, "Bilans A:H": "52% : 48%", "Ping": "24 ms"},
        {"Nazwa Realmu": "🎭 Ravenholdt [RP-PvP]", "Kategoria": "RP", "Typ": "Roleplay PvP", "Zasady": "Klimat RP, wymóg imion lore + otwarte starcia frakcji", "Status": "🟢 Online", "Populacja": "Medium", "Gracze Online": 2150, "Bilans A:H": "50% : 50%", "Ping": "27 ms"},
        {"Nazwa Realmu": "🎭 Moonglade [RP-PvE]", "Kategoria": "RP", "Typ": "Roleplay PvE", "Zasady": "Immersja fabularna, karczmy, eventy gildyjne bez wymuszonego PvP", "Status": "🟢 Online", "Populacja": "Medium", "Gracze Online": 1640, "Bilans A:H": "53% : 47%", "Ping": "28 ms"}
    ]
    t_all, t_pvp, t_pve, t_rp = st.tabs(["🌐 Wszystkie Realmy (7)", "⚔️ PvP (3)", "🛡️ PvE (2)", "🎭 RP (2)"])
    with t_all:
        st.dataframe(pd.DataFrame(realms_all).drop(columns=["Kategoria"]), use_container_width=True, hide_index=True)
    with t_pvp:
        st.dataframe(pd.DataFrame([r for r in realms_all if r["Kategoria"]=="PvP"]).drop(columns=["Kategoria"]), use_container_width=True, hide_index=True)
    with t_pve:
        st.dataframe(pd.DataFrame([r for r in realms_all if r["Kategoria"]=="PvE"]).drop(columns=["Kategoria"]), use_container_width=True, hide_index=True)
    with t_rp:
        st.dataframe(pd.DataFrame([r for r in realms_all if r["Kategoria"]=="RP"]).drop(columns=["Kategoria"]), use_container_width=True, hide_index=True)

    st.write("---")

    st.markdown(f"### {t('status_census_header')}")
    with st.spinner("Pobieranie aktualnych danych z classicplus.io..."):
        census = fetch_classicplus_census()

    if census:
        snapshot = census.get("snapshotDate", "N/A")
        datasets_available = list(census.get("datasets", {}).keys())

        class_colors = {
            "Warrior": "#C69B6D", "Paladin": "#F48CBA", "Hunter": "#AAD372",
            "Rogue": "#FFF468", "Priest": "#FFFFFF", "Shaman": "#0070DD",
            "Mage": "#3FC7EB", "Warlock": "#8788EE", "Druid": "#FF7C0A"
        }
        realm_tab_labels = {"all": "🌐 Wszystkie Serwery", "pvp": "⚔️ PvP", "pve": "🛡️ PvE"}
        available_keys = [k for k in ["all", "pvp", "pve"] if k in datasets_available]
        census_tabs = st.tabs([realm_tab_labels[k] for k in available_keys])

        for tab_obj, realm_key in zip(census_tabs, available_keys):
            with tab_obj:
                total, faction_counts, class_counts = compute_census_stats(census, realm_key)
                ally_cnt = faction_counts["Alliance"]
                horde_cnt = faction_counts["Horde"]
                ally_pct = (ally_cnt / total) * 100
                horde_pct = (horde_cnt / total) * 100
                sorted_classes = sorted(class_counts.items(), key=lambda x: x[1], reverse=True)

                m1, m2, m3 = st.columns(3)
                with m1:
                    st.metric(t("status_tested_chars"), f"{total:,}")
                with m2:
                    st.metric("🦅 Alliance", f"{ally_cnt:,}", f"{ally_pct:.1f}%")
                with m3:
                    st.metric("🪓 Horde", f"{horde_cnt:,}", f"{horde_pct:.1f}%")

                st.markdown(
                    f'<div style="margin:12px 0;height:28px;border-radius:14px;overflow:hidden;display:flex;box-shadow:0 2px 8px rgba(0,0,0,0.5);">'
                    f'<div style="width:{ally_pct:.1f}%;background:linear-gradient(90deg,#0052cc,#00a2ff);display:flex;align-items:center;justify-content:center;font-size:0.9rem;font-weight:bold;color:#fff;min-width:70px;">🦅 {ally_pct:.1f}%</div>'
                    f'<div style="width:{horde_pct:.1f}%;background:linear-gradient(90deg,#ff4d4d,#b30000);display:flex;align-items:center;justify-content:center;font-size:0.9rem;font-weight:bold;color:#fff;min-width:70px;">🪓 {horde_pct:.1f}%</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

                chart_df = pd.DataFrame([
                    {"Klasa": name, "Postaci": cnt, "Procent": round((cnt / total) * 100, 2), "Kolor": class_colors.get(name, "#aaaaaa")}
                    for name, cnt in sorted_classes
                ])
                chart = alt.Chart(chart_df).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                    x=alt.X("Klasa:N", sort="-y", title="Klasa Postaci"),
                    y=alt.Y("Procent:Q", title="Udział w populacji (%)"),
                    color=alt.Color("Kolor:N", scale=None, legend=None),
                    tooltip=["Klasa", "Postaci", "Procent"]
                ).properties(height=360)
                st.altair_chart(chart, use_container_width=True)

                with st.expander("📋 Pełna tabela klas"):
                    st.dataframe(
                        chart_df[["Klasa", "Postaci", "Procent"]].rename(columns={"Postaci": "Liczba postaci", "Procent": "Udział (%)"}),
                        use_container_width=True, hide_index=True
                    )
    else:
        st.error("Nie udało się pobrać danych z classicplus.io. Sprawdź połączenie internetowe.")

    st.write("---")
    st.markdown(f"### {t('status_world_act')}")
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.markdown('<div class="result-card"><h4 style="color:#ffda79;margin-top:0;">🚩 Warsong Gulch (WSG)</h4><div>Aktywne bitwy: <b>12 instancji</b></div><div>Czas oczekiwania: <b>~1.5 min</b></div><div style="color:#2ecc71;font-size:0.85rem;margin-top:4px;">🟢 Bonus Honor Weekend!</div></div>', unsafe_allow_html=True)
    with col_p2:
        st.markdown('<div class="result-card"><h4 style="color:#ffda79;margin-top:0;">🏆 Arathi Basin (AB)</h4><div>Aktywne bitwy: <b>8 instancji</b></div><div>Czas oczekiwania: <b>~2.5 min</b></div><div style="color:#66c2ff;font-size:0.85rem;margin-top:4px;">Blacksmith & Lumber Mill</div></div>', unsafe_allow_html=True)
    with col_p3:
        st.markdown('<div class="result-card"><h4 style="color:#ffda79;margin-top:0;">🏰 Alterac Valley (AV)</h4><div>Aktywne bitwy: <b>3 bitwy 40v40</b></div><div>Czas oczekiwania: <b>~4 min</b></div><div style="color:#e0e0e0;font-size:0.85rem;margin-top:4px;">Drek\'Thar vs Vanndar</div></div>', unsafe_allow_html=True)