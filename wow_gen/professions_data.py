# -*- coding: utf-8 -*-
"""
Baza wiedzy profesji WoW Classic / Forever (1-300)
Wzorowana na wow-professions.com/forever
Zawiera: Kategoryzację, Shopping List, Wskazówki [KEEP] oraz trasy levelingowe krok po kroku.
"""

PROFESSIONS_CATEGORIES = {
    "Crafting ⚒️": [
        "Engineering 🔧", 
        "Alchemy 🧪", 
        "Blacksmithing 🔨", 
        "Leatherworking 🥋", 
        "Tailoring 🧵", 
        "Enchanting 🔮"
    ],
    "Gathering 🌿": [
        "Mining ⛏️", 
        "Herbalism 🌿", 
        "Skinning 🔪"
    ],
    "Secondary 🍳": [
        "Cooking 🍳", 
        "First Aid 🩹", 
        "Fishing 🎣"
    ]
}

PROFESSIONS_DATA = {
    "Engineering 🔧": {
        "category": "Crafting ⚒️",
        "desc": "Inżynieria to bezkonkurencyjna profesja do PvP i dungeonów/raidów (bomby, trinkety, jumper cables).",
        "shopping_list": [
            ("Rough Stone", 90, "Do proszków i bomb na start"),
            ("Copper Bar", 60, "Śruby i obudowy miedziane"),
            ("Coarse Stone", 80, "Coarse Blasting Powder"),
            ("Silver Bar", 5, "Silver Contacts"),
            ("Bronze Bar", 75, "Brązowe rurki i zębatki"),
            ("Heavy Stone", 90, "Heavy Blasting Powder"),
            ("Medium Leather", 15, "Wybuchowe owce i ramy"),
            ("Wool Cloth", 30, "Explosive Sheep i izolacje"),
            ("Steel Bar", 4, "Gyromatic Micro-Adjustor (narzędzie)"),
            ("Solid Stone", 90, "Solid Blasting Powder"),
            ("Mithril Bar", 110, "Mithrilowe obudowy i zapalniki"),
            ("Mageweave Cloth", 40, "Zapalniki i gadżety"),
            ("Dense Stone", 60, "Dense Blasting Powder"),
            ("Thorium Bar", 90, "Thorium Widgets i amunicja"),
            ("Runecloth", 30, "Thorium Widgets")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ ok. 40x Rough Blasting Powder – wykorzystasz je bezpośrednio do Handful of Copper Bolts i bomb!",
            "⚠️ [KEEP] ZACHOWAJ 20x Bronze Tubes – NIE sprzedawaj ich do vendora! Będą potrzebne do późniejszego rzemiosła i questów.",
            "⚠️ [KEEP] ZACHOWAJ 1x Gyromatic Micro-Adjustor – to stałe narzędzie inżynierskie wielokrotnego użytku, trzymaj w plecaku.",
            "⚠️ [KEEP] ZACHOWAJ ok. 30x Mithril Tubes & Mithril Casings – niezbędne w przedziale 215-250 do Hi-Explosive Bomb."
        ],
        "steps": [
            {"range": "1 - 30", "item": "Rough Blasting Powder", "mats": "1x Rough Stone", "count": "~40x", "keep": True, "note": "[KEEP] Zachowaj cały proszek do następnych kroków."},
            {"range": "30 - 50", "item": "Handful of Copper Bolts", "mats": "1x Copper Bar", "count": "~35x", "keep": True, "note": "[KEEP] Potrzebne do bomb i mechanizmów."},
            {"range": "50 - 75", "item": "Rough Copper Bomb", "mats": "1x Copper Bar, 1x Copper Bolts, 2x Rough Powder", "count": "~30x", "keep": False, "note": "Dobry sposób na zużycie zachowanego prochu."},
            {"range": "75 - 90", "item": "Coarse Blasting Powder", "mats": "1x Coarse Stone", "count": "~30x", "keep": True, "note": "[KEEP] Odwiedź trenera: Journeyman (wymaga lvl 10)."},
            {"range": "90 - 100", "item": "Silver Contact", "mats": "1x Silver Bar", "count": "~12x", "keep": True, "note": "[KEEP] Przydatne w późniejszych schematach."},
            {"range": "100 - 105", "item": "Practice Lock", "mats": "2x Bronze Bar, 1x Weak Flux", "count": "~8x", "keep": False, "note": "Kup Weak Flux u Engineering Supply vendora."},
            {"range": "105 - 125", "item": "Bronze Tube", "mats": "2x Bronze Bar, 1x Weak Flux", "count": "~25x", "keep": True, "note": "⚠️ [KEEP] Bardzo ważne – zachowaj min. 15-20 sztuk!"},
            {"range": "125 - 150", "item": "Heavy Blasting Powder", "mats": "1x Heavy Stone", "count": "~30x", "keep": True, "note": "⚠️ [KEEP] Odwiedź trenera: Expert (wymaga lvl 20)."},
            {"range": "150 - 160", "item": "Bronze Framework", "mats": "2x Bronze Bar, 1x Medium Leather, 1x Wool Cloth", "count": "~15x", "keep": True, "note": "[KEEP] Zużyjesz w Explosive Sheep."},
            {"range": "160 - 175", "item": "Explosive Sheep", "mats": "2x Wool Cloth, 1x Heavy Powder, 1x Bronze Framework", "count": "~18x", "keep": False, "note": "Świetna zabawa w open worldzie."},
            {"range": "175 - 176", "item": "Gyromatic Micro-Adjustor", "mats": "4x Steel Bar", "count": "1x", "keep": True, "note": "⚠️ [KEEP] Narzędzie – zostaw na zawsze w torbie."},
            {"range": "176 - 195", "item": "Solid Blasting Powder", "mats": "2x Solid Stone", "count": "~40x", "keep": True, "note": "[KEEP] Baza pod detonatory i bomby."},
            {"range": "195 - 200", "item": "Mithril Tube", "mats": "3x Mithril Bar", "count": "~7x", "keep": True, "note": "[KEEP] Potrzebne do późniejszych craftów."},
            {"range": "200 - 215", "item": "Unstable Trigger", "mats": "1x Mithril Bar, 1x Mageweave Cloth, 1x Solid Powder", "count": "~20x", "keep": True, "note": "⚠️ [KEEP] Kluczowy półprodukt do bomb!"},
            {"range": "215 - 235", "item": "Mithril Casing", "mats": "3x Mithril Bar", "count": "~25x", "keep": True, "note": "Odwiedź trenera: Artisan (wymaga lvl 35, Gadgetzan)."},
            {"range": "235 - 250", "item": "Hi-Explosive Bomb", "mats": "2x Mithril Casing, 1x Unstable Trigger, 2x Solid Powder", "count": "~20x", "keep": False, "note": "Silna bomba z stunem na 3 sekundy."},
            {"range": "250 - 260", "item": "Dense Blasting Powder", "mats": "2x Dense Stone", "count": "~25x", "keep": True, "note": "[KEEP] Składnik do pocisków Thorium Shells."},
            {"range": "260 - 285", "item": "Thorium Widget", "mats": "3x Thorium Bar, 1x Runecloth", "count": "~30x", "keep": False, "note": "Recepta u trenera w Gadgetzan / Orgrimmar / Ironforge."},
            {"range": "285 - 300", "item": "Thorium Shells", "mats": "2x Thorium Bar, 1x Dense Blasting Powder", "count": "~20x", "keep": False, "note": "Amunicja high-end – łatwa do sprzedania Hunterom na AH!"}
        ]
    },

    "Alchemy 🧪": {
        "category": "Crafting ⚒️",
        "desc": "Alchemia pozwala na produkcję mikstur leczniczych, eliksirów statystyk i flasków raidowych.",
        "shopping_list": [
            ("Peacebloom", 60, "Minor Healing Potion"),
            ("Silverleaf", 60, "Minor Healing Potion"),
            ("Briarthorn", 80, "Lesser Healing & Wisdom"),
            ("Bruiseweed", 35, "Healing Potion"),
            ("Mageroyal", 35, "Lesser Mana Potion"),
            ("Stranglekelp", 25, "Lesser Mana & Elixir of Agility"),
            ("Kingsblood", 35, "Greater Healing & Mana Potion"),
            ("Liferoot", 35, "Greater Healing Potion"),
            ("Wild Steelbloom", 15, "Elixir of Greater Defense"),
            ("Goldthorn", 45, "Agility & Greater Defense"),
            ("Khadgar's Whisker", 25, "Superior Healing Potion"),
            ("Sungrass", 45, "Superior Healing & Superior Mana"),
            ("Blindweed", 40, "Superior Mana Potion"),
            ("Golden Sansam", 40, "Major Healing Potion"),
            ("Mountain Silversage", 20, "Major Healing Potion")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ 60x Minor Healing Potion – są niezbędnym składnikiem na Lesser Healing Potion!",
            "⚠️ [KEEP] ZACHOWAJ fiolki (Crystal Vials) kupowane u Alchemy Supplier – zawsze miej zapas w torbie.",
            "⚠️ [KEEP] ZACHOWAJ Elixir of Agility / Greater Defense – zamiast sprzedawać do vendora, oddaj tankom i DPSom w gildii."
        ],
        "steps": [
            {"range": "1 - 60", "item": "Minor Healing Potion", "mats": "1x Peacebloom, 1x Silverleaf, 1x Crystal Vial", "count": "~65x", "keep": True, "note": "⚠️ [KEEP] Nie sprzedawaj! Zużyjesz je w kolejnym kroku."},
            {"range": "60 - 110", "item": "Lesser Healing Potion", "mats": "1x Minor Healing Potion, 1x Briarthorn", "count": "~55x", "keep": False, "note": "Ranga Journeyman u trenera (wymaga lvl 10)."},
            {"range": "110 - 140", "item": "Healing Potion", "mats": "1x Bruiseweed, 1x Briarthorn, 1x Leaded Vial", "count": "~35x", "keep": False, "note": "Solidna mikstura na leveling postaci."},
            {"range": "140 - 155", "item": "Lesser Mana Potion", "mats": "1x Mageroyal, 1x Stranglekelp, 1x Empty Vial", "count": "~20x", "keep": False, "note": "Stranglekelp zbiera się pod wodą wzdłuż wybrzeży."},
            {"range": "155 - 185", "item": "Greater Healing Potion", "mats": "1x Liferoot, 1x Kingsblood, 1x Leaded Vial", "count": "~35x", "keep": False, "note": "Ranga Expert u trenera (wymaga lvl 20)."},
            {"range": "185 - 210", "item": "Elixir of Agility", "mats": "1x Stranglekelp, 1x Goldthorn, 1x Leaded Vial", "count": "~30x", "keep": False, "note": "Daje +15 Agility na 1 godzinę."},
            {"range": "210 - 215", "item": "Elixir of Greater Defense", "mats": "1x Wild Steelbloom, 1x Goldthorn, 1x Leaded Vial", "count": "~10x", "keep": False, "note": "Ranga Artisan: Feathermoon (A) / Stonard (H)."},
            {"range": "215 - 235", "item": "Superior Healing Potion", "mats": "1x Sungrass, 1x Khadgar's Whisker, 1x Crystal Vial", "count": "~25x", "keep": False, "note": "Główny pot leczący w dungeonach 45-55."},
            {"range": "235 - 265", "item": "Elixir of Greater Agility", "mats": "1x Sungrass, 1x Goldthorn, 1x Crystal Vial", "count": "~35x", "keep": False, "note": "+25 Agility – bardzo poszukiwane na AH."},
            {"range": "265 - 285", "item": "Superior Mana Potion", "mats": "2x Sungrass, 2x Blindweed, 1x Crystal Vial", "count": "~25x", "keep": False, "note": "Recepta sprzedawana przez vendora w Azshara / Feralas."},
            {"range": "285 - 300", "item": "Major Healing Potion", "mats": "2x Golden Sansam, 1x Mountain Silversage, 1x Crystal Vial", "count": "~20x", "keep": False, "note": "Recepta u Evie Whirlbrew (Everlook, Winterspring)."}
        ]
    },

    "Blacksmithing 🔨": {
        "category": "Crafting ⚒️",
        "desc": "Kowalstwo tworzy pancerze płytowe/kolcze, osełki do broni i potężny oręż rajdowy.",
        "shopping_list": [
            ("Rough Stone", 150, "Rough Sharpening & Grinding Stones"),
            ("Copper Bar", 140, "Paski i łańcuchy miedziane"),
            ("Coarse Stone", 150, "Coarse Grinding Stones"),
            ("Silver Bar", 10, "Silver Rods"),
            ("Bronze Bar", 160, "Brązowe nagolenniki i pasy"),
            ("Heavy Stone", 100, "Heavy Grinding Stones"),
            ("Iron Bar", 200, "Green Iron Bracers i sztaby"),
            ("Steel Bar", 30, "Golden Scale Bracers"),
            ("Solid Stone", 100, "Solid Grinding Stones"),
            ("Mithril Bar", 340, "Heavy Mithril zestawy"),
            ("Mageweave Cloth", 40, "Heavy Mithril Gauntlet"),
            ("Dense Stone", 180, "Dense Sharpening Stones"),
            ("Thorium Bar", 380, "Imperial Plate i Thorium Bracers"),
            ("Rugged Leather", 80, "Thorium Boots i wykończenia")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ wszystkie kamienie szlifierskie (Grinding Stones) – są półproduktem w dziesiątkach receptur broni i pancerza!",
            "⚠️ [KEEP] ZACHOWAJ 20x Iron Buckles – przydadzą się do wykuwania płytowych zbroi na poziomie 150-180.",
            "⚠️ [KEEP] ZACHOWAJ Blacksmith Hammer w ekwipunku – bez niego nie możesz nic wykuć przy kowadle."
        ],
        "steps": [
            {"range": "1 - 30", "item": "Rough Sharpening Stone", "mats": "1x Rough Stone", "count": "~35x", "keep": False, "note": "Podstawowa osełka dająca bonus do obrażeń."},
            {"range": "30 - 65", "item": "Rough Grinding Stone", "mats": "2x Rough Stone", "count": "~40x", "keep": True, "note": "⚠️ [KEEP] Zachowaj każdy wytworzony kamień!"},
            {"range": "65 - 75", "item": "Copper Chain Belt", "mats": "6x Copper Bar", "count": "~12x", "keep": False, "note": "Odwiedź trenera: Journeyman (lvl 10)."},
            {"range": "75 - 90", "item": "Coarse Grinding Stone", "mats": "2x Coarse Stone", "count": "~25x", "keep": True, "note": "⚠️ [KEEP] Półprodukt do brązowych pancerzy."},
            {"range": "90 - 100", "item": "Runed Copper Belt", "mats": "10x Copper Bar", "count": "~12x", "keep": False, "note": "Zużywa pozostałą miedź."},
            {"range": "100 - 105", "item": "Silver Rod", "mats": "1x Silver Bar, 2x Rough Grinding Stone", "count": "~6x", "keep": False, "note": "Kupują to zaklinacze (Enchanterzy) na AH."},
            {"range": "105 - 125", "item": "Rough Bronze Leggings", "mats": "6x Bronze Bar", "count": "~25x", "keep": False, "note": "Wymaga sporo brązu."},
            {"range": "125 - 150", "item": "Heavy Grinding Stone", "mats": "3x Heavy Stone", "count": "~30x", "keep": True, "note": "⚠️ [KEEP] Odwiedź trenera: Expert (wymaga lvl 20)."},
            {"range": "150 - 165", "item": "Green Iron Leggings", "mats": "8x Iron Bar, 1x Heavy Grinding Stone", "count": "~18x", "keep": False, "note": "Dobre do sprzedania u vendora."},
            {"range": "165 - 190", "item": "Green Iron Bracers", "mats": "6x Iron Bar, 1x Green Dye", "count": "~30x", "keep": False, "note": "Green Dye kupisz u Tailoring Supply vendora."},
            {"range": "190 - 200", "item": "Golden Scale Bracers", "mats": "5x Steel Bar, 2x Heavy Grinding Stone", "count": "~12x", "keep": False, "note": "Wymaga stali przetopionej z żelaza i węgla."},
            {"range": "200 - 210", "item": "Solid Grinding Stone", "mats": "4x Solid Stone", "count": "~20x", "keep": True, "note": "⚠️ [KEEP] Podstawa pod mithrilowe pancerze."},
            {"range": "210 - 225", "item": "Heavy Mithril Gauntlet", "mats": "6x Mithril Bar, 4x Mageweave Cloth", "count": "~18x", "keep": False, "note": "Odwiedź trenera: Artisan w Booty Bay."},
            {"range": "225 - 235", "item": "Mithril Scale Bracers", "mats": "8x Mithril Bar", "count": "~12x", "keep": False, "note": "Recepta do kupienia u vendora w Tanaris / Hinterlands."},
            {"range": "235 - 250", "item": "Mithril Coif", "mats": "10x Mithril Bar, 6x Mageweave Cloth", "count": "~18x", "keep": False, "note": "Popularny hełm w dungeonach."},
            {"range": "250 - 260", "item": "Dense Sharpening Stone", "mats": "1x Dense Stone", "count": "~20x", "keep": False, "note": "Bardzo tanie i szybkie punkty."},
            {"range": "260 - 275", "item": "Thorium Bracers", "mats": "8x Thorium Bar", "count": "~20x", "keep": False, "note": "Recepta u trenera."},
            {"range": "275 - 290", "item": "Imperial Plate Bracers", "mats": "12x Thorium Bar", "count": "~20x", "keep": False, "note": "Recepta z questu Imperial Plate w Tanaris."},
            {"range": "290 - 300", "item": "Thorium Boots", "mats": "12x Thorium Bar, 8x Rugged Leather", "count": "~15x", "keep": False, "note": "Ostatnia prosta do mistrzostwa 300!"}
        ]
    },

    "Tailoring 🧵": {
        "category": "Crafting ⚒️",
        "desc": "Krawiectwo pozwala szyć szaty dla casterów, peleryny oraz poszukiwane torby (Bags).",
        "shopping_list": [
            ("Linen Cloth", 160, "Bolts of Linen Cloth"),
            ("Wool Cloth", 180, "Bolts of Wool & Spidersilk"),
            ("Silk Cloth", 760, "Bolts of Silk & Bandages"),
            ("Mageweave Cloth", 500, "Bolts of Mageweave"),
            ("Runecloth", 900, "Bolts of Runecloth & Bags"),
            ("Rugged Leather", 40, "Runecloth Boots/Belt")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ wszystkie belki materiału (Bolts of Cloth) – nie wytwarzaj z nich losowych szat, dopóki nie wymaga tego poradnik!",
            "⚠️ [KEEP] ZACHOWAJ wyprodukowane torby (np. 10-slot Silk Bag, 14-slot Mageweave Bag) – zawsze świetnie sprzedają się na AH.",
            "⚠️ [KEEP] Nici (Coarse Thread, Fine Thread, Silken Thread, Rune Thread) kupuj zawsze u Tailoring Supply vendora – nie przepłacaj na AH!"
        ],
        "steps": [
            {"range": "1 - 45", "item": "Bolt of Linen Cloth", "mats": "2x Linen Cloth", "count": "~80x", "keep": True, "note": "Podstawowy materiał pod pierwsze szaty."},
            {"range": "45 - 70", "item": "Heavy Linen Gloves", "mats": "2x Bolt of Linen, 1x Coarse Thread", "count": "~30x", "keep": False, "note": "Odwiedź trenera: Journeyman (lvl 10)."},
            {"range": "70 - 75", "item": "Reinforced Linen Cape", "mats": "2x Bolt of Linen, 3x Coarse Thread", "count": "~8x", "keep": False, "note": "Końcówka etapu lnianego."},
            {"range": "75 - 105", "item": "Bolt of Woolen Cloth", "mats": "3x Wool Cloth", "count": "~60x", "keep": True, "note": "[KEEP] Zachowaj do koszul i toreb."},
            {"range": "105 - 120", "item": "Gray Woolen Shirt", "mats": "2x Bolt of Wool, 1x Fine Thread, 1x Gray Dye", "count": "~18x", "keep": False, "note": "Ładna koszula kosmetyczna."},
            {"range": "120 - 125", "item": "Double-stitched Woolen Shoulders", "mats": "3x Bolt of Wool, 2x Fine Thread", "count": "~7x", "keep": False, "note": "Odwiedź trenera: Expert (lvl 20)."},
            {"range": "125 - 145", "item": "Bolt of Silk Cloth", "mats": "4x Silk Cloth", "count": "~190x", "keep": True, "note": "Duża partia jedwabiu – będzie potrzebny!"},
            {"range": "145 - 160", "item": "Azure Silk Hood", "mats": "2x Bolt of Silk, 2x Blue Dye, 1x Fine Thread", "count": "~18x", "keep": False, "note": "Blue Dye kup u krawieckiego vendora."},
            {"range": "160 - 175", "item": "Silk Headband", "mats": "3x Bolt of Silk, 2x Fine Thread", "count": "~18x", "keep": False, "note": "Tani craft w jedwabiu."},
            {"range": "175 - 185", "item": "Bolt of Mageweave", "mats": "5x Mageweave Cloth", "count": "~100x", "keep": True, "note": "[KEEP] Magiczny materiał do wysokopoziomowych szat."},
            {"range": "185 - 205", "item": "Crimson Silk Vest", "mats": "4x Bolt of Silk, 2x Red Dye, 2x Fine Thread", "count": "~22x", "keep": False, "note": "Wymaga Red Dye."},
            {"range": "205 - 215", "item": "Crimson Silk Pantaloons", "mats": "4x Bolt of Silk, 2x Red Dye, 2x Silken Thread", "count": "~12x", "keep": False, "note": "Odwiedź trenera: Artisan (lvl 35, Theramore / Dustwallow)."},
            {"range": "215 - 220", "item": "Black Mageweave Leggings", "mats": "2x Bolt of Mageweave, 3x Silken Thread", "count": "~7x", "keep": False, "note": "Cenione za statystyki z magią."},
            {"range": "220 - 230", "item": "Black Mageweave Gloves", "mats": "2x Bolt of Mageweave, 2x Heavy Silken Thread", "count": "~12x", "keep": False, "note": "Kolejny krok mageweave."},
            {"range": "230 - 250", "item": "Black Mageweave Headband", "mats": "3x Bolt of Mageweave, 2x Heavy Silken Thread", "count": "~25x", "keep": False, "note": "Bardzo stabilne wbijanie punktów."},
            {"range": "250 - 260", "item": "Bolt of Runecloth", "mats": "5x Runecloth", "count": "~180x", "keep": True, "note": "[KEEP] Runecloth to kluczowy surowiec endgame."},
            {"range": "260 - 280", "item": "Runecloth Belt", "mats": "3x Bolt of Runecloth, 1x Rune Thread", "count": "~25x", "keep": False, "note": "Rune Thread kupisz u vendora."},
            {"range": "280 - 300", "item": "Runecloth Gloves / Bag", "mats": "4x Bolt of Runecloth, 4x Rugged Leather, 1x Rune Thread", "count": "~25x", "keep": False, "note": "Gratulacje, 300 Tailoring zdobyty!"}
        ]
    },

    "Leatherworking 🥋": {
        "category": "Crafting ⚒️",
        "desc": "Kusznictwo i kaletnictwo tworzy zbroje skórzane dla Rogali i Druidów oraz kolcze dla Shamanów i Hunterów.",
        "shopping_list": [
            ("Light Leather", 260, "Kits, Armor & Gloves"),
            ("Medium Leather", 160, "Hides, Belts & Boots"),
            ("Heavy Leather", 200, "Heavy Armor Kits & Pants"),
            ("Thick Leather", 320, "Nightscape & Thick Armor Kits"),
            ("Rugged Leather", 420, "Wicked Leather & Frostsaber"),
            ("Cured Light/Medium Hide", 30, "Półprodukty skórzane")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ Armor Kity (Light, Medium, Heavy, Thick) – można je nałożyć na własny pancerz lub sprzedać na AH!",
            "⚠️ [KEEP] ZACHOWAJ wygarbowane skóry (Cured Hides) – proces przygotowania zajmuje czas i sól (Salt), nie marnuj ich.",
            "⚠️ [KEEP] W przedziale 260-290 możesz wybrać specjalizację: Dragonscale, Elemental lub Tribal Leatherworking."
        ],
        "steps": [
            {"range": "1 - 45", "item": "Light Armor Kit", "mats": "1x Light Leather", "count": "~50x", "keep": False, "note": "Zwiększa armor klatki, nóg, rąk."},
            {"range": "45 - 55", "item": "Handstitched Leather Cloak", "mats": "2x Light Leather, 1x Coarse Thread", "count": "~15x", "keep": False, "note": "Odwiedź trenera: Journeyman."},
            {"range": "55 - 100", "item": "Embossed Leather Gloves", "mats": "3x Light Leather, 2x Coarse Thread", "count": "~50x", "keep": False, "note": "Stabilne podnoszenie umiejętności."},
            {"range": "100 - 120", "item": "Fine Leather Belt", "mats": "6x Light Leather, 2x Coarse Thread", "count": "~25x", "keep": False, "note": "Zużywa pozostałe lekkie skóry."},
            {"range": "120 - 135", "item": "Dark Leather Boots", "mats": "4x Medium Leather, 2x Fine Thread, 1x Gray Dye", "count": "~18x", "keep": False, "note": "Odwiedź trenera: Expert."},
            {"range": "135 - 150", "item": "Dark Leather Pants", "mats": "12x Medium Leather, 1x Fine Thread, 1x Gray Dye", "count": "~18x", "keep": False, "note": "Zużywa sporo skór średnich."},
            {"range": "150 - 160", "item": "Heavy Armor Kit", "mats": "5x Heavy Leather, 1x Fine Thread", "count": "~15x", "keep": False, "note": "Przydatne na leveling pancerza."},
            {"range": "160 - 180", "item": "Barbaric Shoulders", "mats": "8x Heavy Leather, 1x Cured Heavy Hide, 2x Fine Thread", "count": "~22x", "keep": False, "note": "Można alternatywnie szyć Duskworker Belts."},
            {"range": "180 - 190", "item": "Barbaric Bracers", "mats": "8x Heavy Leather, 1x Cured Heavy Hide, 2x Fine Thread", "count": "~12x", "keep": False, "note": "Kolejny krok w ciężkiej skórze."},
            {"range": "190 - 205", "item": "Barbaric Shoulders / Harness", "mats": "14x Heavy Leather, 1x Fine Thread", "count": "~18x", "keep": False, "note": "Przygotowanie pod Artisan."},
            {"range": "205 - 220", "item": "Nightscape Tunic", "mats": "7x Thick Leather, 2x Silken Thread", "count": "~18x", "keep": False, "note": "Odwiedź trenera: Artisan w Feralas."},
            {"range": "220 - 235", "item": "Nightscape Headband", "mats": "5x Thick Leather, 2x Silken Thread", "count": "~18x", "keep": False, "note": "Tania receptura Thick Leather."},
            {"range": "235 - 250", "item": "Nightscape Pants", "mats": "14x Thick Leather, 4x Silken Thread", "count": "~18x", "keep": False, "note": "Często noszone przez feral druidów."},
            {"range": "250 - 260", "item": "Nightscape Boots", "mats": "16x Thick Leather, 2x Heavy Silken Thread", "count": "~15x", "keep": False, "note": "Ostatnie szlify w grubych skórach."},
            {"range": "260 - 280", "item": "Wicked Leather Gauntlets", "mats": "8x Rugged Leather, 1x Black Dye, 1x Rune Thread", "count": "~25x", "keep": False, "note": "Recepta u vendora w Azshara."},
            {"range": "280 - 300", "item": "Wicked Leather Headband", "mats": "12x Rugged Leather, 1x Black Dye, 1x Rune Thread", "count": "~25x", "keep": False, "note": "Gratulacje, 300 Leatherworking!"}
        ]
    },

    "Enchanting 🔮": {
        "category": "Crafting ⚒️",
        "desc": "Zaklinanie pozwala disenchantować zielone/niebieskie itemy na pyły i esencje oraz ulepszać ekwipunek.",
        "shopping_list": [
            ("Copper / Silver / Golden / Truesilver / Arcanite Rod", 1, "Różdżki bazowe u blacksmitha"),
            ("Strange Dust", 180, "Bracer & Chest Enchants"),
            ("Lesser & Greater Magic Essence", 25, "Rods & Enchants"),
            ("Soul Dust", 120, "Journeyman Enchants"),
            ("Lesser & Greater Astral Essence", 20, "Expert Rod & Enchants"),
            ("Vision Dust", 140, "Expert Enchants"),
            ("Dream Dust", 180, "Artisan Enchants"),
            ("Illusion Dust", 120, "Endgame Enchants 275-300"),
            ("Greater Nether Essence", 15, "Truesilver Rod & High Tier"),
            ("Large Brilliant Shard", 10, "High end enchants & Arcanite Rod")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ wszystkie Runed Rods (Copper, Silver, Golden, Truesilver, Arcanite) – są to narzędzia permanentne, bez nich nie rzucisz czarów!",
            "⚠️ [KEEP] Nie sprzedawaj zielonych przedmiotów z questów i mobów do vendora – disenchantuj je (DE) na surowce!",
            "⚠️ [KEEP] Enchanterzy mogą czarować własne bracery w kółko, aby wbijać punkty bez marnowania dodatkowego gearu."
        ],
        "steps": [
            {"range": "1 - 2", "item": "Runed Copper Rod", "mats": "1x Copper Rod, 1x Strange Dust, 1x Lesser Magic Essence", "count": "1x", "keep": True, "note": "⚠️ [KEEP] Twoje pierwsze narzędzie zaklinacza!"},
            {"range": "2 - 75", "item": "Enchant Bracer - Minor Health", "mats": "1x Strange Dust", "count": "~75x", "keep": False, "note": "Najtańszy enchant na start."},
            {"range": "75 - 85", "item": "Enchant Bracer - Minor Deflection", "mats": "1x Lesser Magic Essence, 1x Strange Dust", "count": "~12x", "keep": False, "note": "Odwiedź trenera: Journeyman."},
            {"range": "85 - 100", "item": "Enchant Bracer - Minor Stamina", "mats": "3x Strange Dust", "count": "~18x", "keep": False, "note": "Popularny enchant na niskie poziomy."},
            {"range": "100 - 101", "item": "Runed Silver Rod", "mats": "1x Silver Rod, 6x Strange Dust, 3x Greater Magic Essence", "count": "1x", "keep": True, "note": "⚠️ [KEEP] Narzędzie poziomu Journeyman."},
            {"range": "101 - 105", "item": "Enchant Bracer - Minor Agility", "mats": "2x Strange Dust, 1x Greater Magic Essence", "count": "~6x", "keep": False, "note": "Szybki przeskok."},
            {"range": "105 - 120", "item": "Enchant Bracer - Minor Agility", "mats": "2x Strange Dust, 1x Greater Magic Essence", "count": "~18x", "keep": False, "note": "Kontynuacja do 120."},
            {"range": "120 - 130", "item": "Enchant Shield - Minor Stamina", "mats": "1x Lesser Astral Essence, 2x Strange Dust", "count": "~12x", "keep": False, "note": "Świetny enchant dla tanków."},
            {"range": "130 - 150", "item": "Enchant Bracer - Lesser Stamina", "mats": "2x Soul Dust", "count": "~25x", "keep": False, "note": "Odwiedź trenera: Expert."},
            {"range": "150 - 151", "item": "Runed Golden Rod", "mats": "1x Golden Rod, 1x Iridescent Pearl, 2x Greater Astral, 2x Soul Dust", "count": "1x", "keep": True, "note": "⚠️ [KEEP] Wymaga perły Iridescent Pearl."},
            {"range": "151 - 160", "item": "Enchant Bracer - Lesser Stamina", "mats": "2x Soul Dust", "count": "~12x", "keep": False, "note": "Kończenie Soul Dust."},
            {"range": "160 - 180", "item": "Enchant Chest - Greater Health", "mats": "3x Soul Dust", "count": "~22x", "keep": False, "note": "Tanie punkty na klatkach."},
            {"range": "180 - 200", "item": "Enchant Bracer - Strength", "mats": "1x Vision Dust", "count": "~22x", "keep": False, "note": "Przejście na Vision Dust."},
            {"range": "200 - 201", "item": "Runed Truesilver Rod", "mats": "1x Truesilver Rod, 1x Black Pearl, 2x Greater Mystic, 2x Vision Dust", "count": "1x", "keep": True, "note": "⚠️ [KEEP] Narzędzie Artisan."},
            {"range": "201 - 225", "item": "Enchant Bracer - Greater Strength", "mats": "2x Vision Dust", "count": "~28x", "keep": False, "note": "Odwiedź trenera: Artisan w Uldaman (Annora)."},
            {"range": "225 - 245", "item": "Enchant Gloves - Agility", "mats": "1x Vision Dust, 1x Lesser Nether Essence", "count": "~22x", "keep": False, "note": "Annora uczy tej receptury."},
            {"range": "245 - 265", "item": "Enchant Boots - Greater Stamina", "mats": "5x Dream Dust", "count": "~22x", "keep": False, "note": "Dream Dust z itemów lvl 45-50."},
            {"range": "265 - 290", "item": "Enchant Shield - Greater Stamina", "mats": "10x Dream Dust", "count": "~28x", "keep": False, "note": "Recepta u vendora w Undercity / Darnassus."},
            {"range": "290 - 299", "item": "Enchant Chest - Major Health", "mats": "6x Small Brilliant Shard, 1x Illusion Dust", "count": "~12x", "keep": False, "note": "Recepta w Winterspring."},
            {"range": "299 - 300", "item": "Runed Arcanite Rod", "mats": "1x Arcanite Rod, 1x Golden Pearl, 10x Illusion Dust, 4x Greater Eternal, 2x Large Brilliant Shard", "count": "1x", "keep": True, "note": "⚠️ [KEEP] Święty Graal Enchantera – pozwala na enchanty raidowe!"}
        ]
    },

    "Mining ⛏️": {
        "category": "Gathering 🌿",
        "desc": "Górnictwo pozwala wydobywać rudy metali, kamienie szlifierskie oraz rzadkie klejnoty z żył minerałów.",
        "shopping_list": [
            ("Mining Pick", 1, "Kup u dowolnego Mining Supply vendora – trzymaj w torbie"),
            ("Wskazówka Smelting", 1, "Przetapianie rud w sztabki (Smelt) daje darmowe żółte/zielone punkty bez biegania po mapie!")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ Mining Pick – bez kilofa w torbie nie da się uderzyć w żadną żyłę rudy!",
            "⚠️ [KEEP] Kamienie (Rough, Coarse, Heavy, Solid, Dense Stone) są skarbem dla Blacksmithów i Inżynierów – zachowaj je lub sprzedaj z zyskiem na AH.",
            "⚠️ [KEEP] ZACHOWAJ rzadkie klejnoty (Malachite, Tigerseye, Shadowgem, Jade, Citrine, Aquamarine, Azerothian Diamond)."
        ],
        "zones": [
            {"range": "1 - 65", "ore": "Copper Ore (Miedź)", "zones": "Durotar, Mulgore, Tirisfal Glades, Elwynn Forest, Dun Morogh, Teldrassil", "tips": "Przetop miedź w sztabki (Smelt Copper) przy piecu (Forge) dla darmowych punktów do 25."},
            {"range": "65 - 125", "ore": "Tin Ore & Silver Ore (Cyna i Srebro)", "zones": "The Barrens, Silverpine Forest, Westfall, Redridge Mountains, Loch Modan", "tips": "Połącz miedź i cynę w piecu, by stworzyć Bronze (Brąz) – również daje punkty skilla!"},
            {"range": "125 - 175", "ore": "Iron Ore & Gold Ore (Żelazo i Złoto)", "zones": "Arathi Highlands, Badlands, Thousand Needles, Hillsbrad Foothills, Desolace", "tips": "Badlands i Arathi to najlepsze strefy na gęstość występowania żył żelaza."},
            {"range": "175 - 230", "ore": "Mithril Ore & Truesilver Ore (Mithril)", "zones": "Tanaris, The Hinterlands, Badlands, Feralas, Searing Gorge", "tips": "W Tanaris obiegaj ściany górskie wokół całej pustyni."},
            {"range": "230 - 275", "ore": "Small Thorium Vein (Mały Tor)", "zones": "Un'Goro Crater, Felwood, Blasted Lands, Winterspring, Azshara", "tips": "Un'Goro Crater to absolutny raj – lataj lub biegaj po wewnętrznym pierścieniu krateru."},
            {"range": "275 - 300", "ore": "Rich Thorium Vein & Dark Iron (Bogaty Tor)", "zones": "Winterspring, Eastern Plaguelands, Silithus, Burning Steppes", "tips": "Wymaga 275 skilla! Z Rich Thorium wypadają cenne Arcane Crystals pod Arcanite Bary."}
        ]
    },

    "Herbalism 🌿": {
        "category": "Gathering 🌿",
        "desc": "Zielarstwo polega na zbieraniu ziół z całego Azeroth, niezbędnych dla Alchemii i tworzenia pigmentów.",
        "shopping_list": [
            ("Herb Pouch (opcjonalnie)", 1, "Specjalna torba na zioła ułatwia zarządzanie miejscem w ekwipunku"),
            ("Włącz 'Find Herbs'", 1, "Pamiętaj o włączeniu śledzenia ziół na minimapie!")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ zioła pod swoją Alchemię lub sprzedawaj w paczkach po 20 sztuk (stack) na Auction House.",
            "⚠️ [KEEP] Fadeleaf i Swiftthistle są ultra-poszukiwane przez Rogali (do Thistle Tea i Vanish Powder) – osiągają wysokie ceny!",
            "⚠️ [KEEP] Black Lotus (Czarny Lotos) to najcenniejsza roślina w grze (pod Flaski raidowe) – jeśli go zobaczysz, zbieraj natychmiast!"
        ],
        "zones": [
            {"range": "1 - 50", "ore": "Peacebloom, Silverleaf, Earthroot", "zones": "Elwynn Forest, Durotar, Dun Morogh, Tirisfal Glades, Mulgore", "tips": "Okolice startowe, rosną na otwartych polanach i przy drzewach."},
            {"range": "50 - 100", "ore": "Mageroyal, Briarthorn, Stranglekelp", "zones": "Westfall, The Barrens, Silverpine Forest, Loch Modan, Darkshore", "tips": "Stranglekelp rośnie wyłącznie pod wodą u wybrzeży oceanu."},
            {"range": "100 - 150", "ore": "Bruiseweed, Wild Steelbloom, Kingsblood", "zones": "Ashenvale, Wetlands, Hillsbrad Foothills, Stonetalon Mountains", "tips": "Wild Steelbloom rośnie na szczytach wzniesień i skał."},
            {"range": "150 - 200", "ore": "Fadeleaf, Goldthorn, Khadgar's Whisker", "zones": "Stranglethorn Vale, Arathi Highlands, Badlands, Swamp of Sorrows", "tips": "STV i Arathi mają ogromne zagęszczenie ziół tego poziomu."},
            {"range": "200 - 250", "ore": "Firebloom, Purple Lotus, Sungrass", "zones": "Tanaris, Feralas, Hinterlands, Searing Gorge, Felwood", "tips": "Firebloom znajdziesz w gorących, pustynnych strefach (Tanaris, Searing Gorge)."},
            {"range": "250 - 300", "ore": "Gromsblood, Dreamfoil, Silversage, Plaguebloom, Black Lotus", "zones": "Felwood, Eastern Plaguelands, Western Plaguelands, Winterspring, Silithus", "tips": "Felwood to najlepsza trasa (dużo Gromsblood i Plaguebloom). Uważaj na wrogich graczy!"}
        ]
    },

    "Skinning 🔪": {
        "category": "Gathering 🌿",
        "desc": "Skórowanie pozwala zdejmować skóry z zabitych bestii, smoków i yeti. Najprostsza profesja do zarabiania w trakcie levelingu.",
        "shopping_list": [
            ("Skinning Knife", 1, "Nóż rzeźnicki – musisz go mieć w torbie, by zdjąć skórę z moba!"),
            ("Zasada", 1, "Mob musi być całkowicie ograbiony z lootu (Looted), zanim będzie można go oskórować.")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ Skinning Knife – bez niego akcja skórowania nie zadziała!",
            "⚠️ [KEEP] Zachowuj Medium/Heavy/Thick Hides – garbowane skóry są rzadkie i poszukiwane.",
            "⚠️ [KEEP] W endgame zbieraj Rugged Leather oraz Devilsaur Leather (z dinozaurów w Un'Goro Crater pod Devilsaur Set)!"
        ],
        "zones": [
            {"range": "1 - 60", "ore": "Ruined Leather Scraps, Light Leather", "zones": "Strefy początkowe (poziomy mobów 1-10: wilki, dziki, koty)", "tips": "Skóruj wszystko co zabijesz. Pamiętaj: (Poziom moba - 10) * 5 to wymagany skill."},
            {"range": "60 - 110", "ore": "Light Leather, Light Hide", "zones": "Westfall, Loch Modan, Darkshore, The Barrens, Silverpine", "tips": "Bestie na poziomach 10-20."},
            {"range": "110 - 150", "ore": "Medium Leather, Medium Hide", "zones": "Redridge, Wetlands, Ashenvale, Hillsbrad Foothills, Duskwood", "tips": "Krokodyle i raptory w Wetlands dają mnóstwo skór."},
            {"range": "150 - 200", "ore": "Heavy Leather, Heavy Hide", "zones": "Stranglethorn Vale (północ), Arathi Highlands, Thousand Needles", "tips": "Obozy raptorów i panter w STV to najszybszy exp i skórowanie."},
            {"range": "200 - 250", "ore": "Thick Leather, Thick Hide", "zones": "Stranglethorn Vale (południe), Feralas, Tanaris, Hinterlands", "tips": "Goryle w południowym STV i bazyliszki w Tanaris."},
            {"range": "250 - 300", "ore": "Rugged Leather, Rugged Hide, Devilsaur Leather", "zones": "Un'Goro Crater, Winterspring, Western/Eastern Plaguelands", "tips": "Dinozaury w Un'Goro i yeti w Winterspring pozwolą bez trudu dobić 300 punktów."}
        ]
    },

    "Cooking 🍳": {
        "category": "Secondary 🍳",
        "desc": "Gotowanie pozwala tworzyć jedzenie dające Well Fed buffy (bonus do Stamina, Spirit, MP5, AP).",
        "shopping_list": [
            ("Simple Flour & Mild Spices", 50, "Kup u Cooking vendora"),
            ("Small Eggs", 30, "Zabijaj ptaki w Westfall / Mulgore / Eversong"),
            ("Stringy Wolf Meat", 30, "Wilki w Elwynn / Dun Morogh / Durotar"),
            ("Crawler Meat / Clam Meat", 40, "Kraby i małże u wybrzeży"),
            ("Tender Wolf Meat / Sandworm Meat", 60, "Mięso z mobów 45-60")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ Flint and Tinder oraz Simple Wood – pozwalają rozpalić własne ognisko (Cooking Fire) w dowolnym miejscu w terenie!",
            "⚠️ [KEEP] ZACHOWAJ Small Eggs w okresie zimowym – są kluczowe w questach świątecznych (Feast of Winter Veil).",
            "⚠️ [KEEP] Po osiągnięciu 285 zrób quest w Silithus na Smoked Desert Dumplings (+20 Str buff dla Melee dps)!"
        ],
        "steps": [
            {"range": "1 - 40", "item": "Spice Bread", "mats": "1x Simple Flour, 1x Mild Spices", "count": "~45x", "keep": False, "note": "Wszystkie składniki kupisz u vendora przy trenerze."},
            {"range": "40 - 75", "item": "Herb Baked Eggs", "mats": "1x Small Egg, 1x Mild Spices", "count": "~40x", "keep": False, "note": "Jaja wypadają z ptaków i sępów."},
            {"range": "75 - 100", "item": "Crab Cake / Smoked Bear Meat", "mats": "1x Crawler Meat / Bear Meat", "count": "~30x", "keep": False, "note": "Odwiedź trenera: Journeyman."},
            {"range": "100 - 150", "item": "Seasoned Wolf Kabob", "mats": "2x Lean Wolf Flank, 1x Stormwind Seasoning Herbs", "count": "~55x", "keep": False, "note": "Recepta w Duskwood / Ashenvale."},
            {"range": "150 - 175", "item": "Curiously Tasty Omelet", "mats": "1x Raptor Egg, 1x Hot Spices", "count": "~30x", "keep": False, "note": "Odwiedź trenera: Expert (Książka w Desolace / Stranglethorn)."},
            {"range": "175 - 225", "item": "Roast Raptor", "mats": "1x Raptor Flesh, 1x Hot Spices", "count": "~55x", "keep": False, "note": "Raptory w Arathi / STV / Dustwallow."},
            {"range": "225 - 275", "item": "Monster Omelet", "mats": "1x Giant Egg, 1x Soothing Spices", "count": "~55x", "keep": False, "note": "Quest Artisan Cooking 'Clamlette Surprise' w Gadgetzan."},
            {"range": "275 - 300", "item": "Smoked Desert Dumplings", "mats": "1x Sandworm Meat, 1x Soothing Spices", "count": "~30x", "keep": False, "note": "Quest w Silithus (Cenarion Hold). Daje +20 Strength na 15 min!"}
        ]
    },

    "First Aid 🩹": {
        "category": "Secondary 🍳",
        "desc": "Pierwsza pomoc pozwala leczyć się za pomocą bandaży podczas i po walce. Obowiązkowa profesja dla każdej klasy bez wyjątku!",
        "shopping_list": [
            ("Linen Cloth", 140, "Linen Bandage & Heavy Linen Bandage"),
            ("Wool Cloth", 125, "Wool Bandage & Heavy Wool Bandage"),
            ("Silk Cloth", 140, "Silk Bandage & Heavy Silk Bandage"),
            ("Mageweave Cloth", 110, "Mageweave Bandage & Heavy Mageweave Bandage"),
            ("Runecloth", 110, "Runecloth Bandage & Heavy Runecloth Bandage")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ zapas gotowych Heavy Runecloth Bandages w torbie – przywracają 2000 HP w 8 sekund i ratują życie w PvP/Raidach!",
            "⚠️ [KEEP] Jeśli grasz klasą bez leczenia (Warrior, Rogue, Hunter, Mage, Warlock), First Aid to twój priorytet numer jeden!",
            "⚠️ [KEEP] Quest Triage na 225 wymaga opatrzenia 15 rannych żołnierzy – używaj klawiszy skrótu i opatruj najciężej rannych (Critically Injured) w pierwszej kolejności."
        ],
        "steps": [
            {"range": "1 - 40", "item": "Linen Bandage", "mats": "1x Linen Cloth", "count": "~45x", "keep": False, "note": "Leczy 66 HP w 6 sek."},
            {"range": "40 - 75", "item": "Heavy Linen Bandage", "mats": "2x Linen Cloth", "count": "~40x", "keep": False, "note": "Leczy 114 HP. Trener: Journeyman (lvl 10)."},
            {"range": "75 - 115", "item": "Wool Bandage", "mats": "1x Wool Cloth", "count": "~45x", "keep": False, "note": "Leczy 161 HP."},
            {"range": "115 - 150", "item": "Heavy Wool Bandage", "mats": "2x Wool Cloth", "count": "~40x", "keep": False, "note": "Leczy 301 HP. Odwiedź trenera / kup książkę Expert First Aid w Stromgarde (A) / Brackenwall (H)."},
            {"range": "150 - 180", "item": "Silk Bandage", "mats": "1x Silk Cloth", "count": "~40x", "keep": False, "note": "Leczy 400 HP."},
            {"range": "180 - 210", "item": "Heavy Silk Bandage", "mats": "2x Silk Cloth", "count": "~40x", "keep": False, "note": "Książka u tego samego vendora."},
            {"range": "210 - 225", "item": "Mageweave Bandage", "mats": "1x Mageweave Cloth", "count": "~20x", "keep": False, "note": "Leczy 800 HP. Ostatni krok przed questem Artisan."},
            {"range": "225 - 260", "item": "Heavy Mageweave Bandage", "mats": "2x Mageweave Cloth", "count": "~40x", "keep": False, "note": "Quest Triage: Theramore (Alliance) / Hammerfall (Horde)."},
            {"range": "260 - 290", "item": "Runecloth Bandage", "mats": "1x Runecloth", "count": "~40x", "keep": False, "note": "Leczy 1360 HP. Nauczy cię tego lekarz od questu Triage."},
            {"range": "290 - 300", "item": "Heavy Runecloth Bandage", "mats": "2x Runecloth", "count": "~20x", "keep": True, "note": "⚠️ [KEEP] Najlepszy bandaż w grze – leczy 2000 HP w 8 sekund!"}
        ]
    },

    "Fishing 🎣": {
        "category": "Secondary 🍳",
        "desc": "Wędkarstwo dostarcza ryb do Gotowania, rzadkich skrzyń z surowcami i potężnych ryb (np. Oily Blackmouth do eliksirów).",
        "shopping_list": [
            ("Fishing Pole", 1, "Podstawowa wędka kupiona u dowolnego Fishing vendora"),
            ("Aquadynamic Fish Attractor / Bright Baubles", 20, "Przynęty (+50 do +100 skilla) zapobiegają ucieczce ryb!")
        ],
        "keep_items": [
            "⚠️ [KEEP] ZACHOWAJ Oily Blackmouth i Firefin Snapper – alchemicy płacą za nie fortunę na AH (do Free Action Potion i Fire Oil)!",
            "⚠️ [KEEP] ZACHOWAJ Nightfin Snapper i Raw Winter Squid – są składnikiem jedzenia na +Mana Regen oraz +10 Agility!",
            "⚠️ [KEEP] Zawsze używaj przynęty (Lure) na łowisku, jeśli ryby zrywają się z haczyka ('Your fish got away')."
        ],
        "zones": [
            {"range": "1 - 75", "ore": "Raw Slitherskin Mackerel, Brilliant Smallfish", "zones": "Stolice (Orgrimmar, Stormwind, Ironforge), Elwynn, Durotar", "tips": "Można bezpiecznie łowić w fosie Stormwind lub stawie w Orgrimmar bez ryzyka zaatakowania przez moby."},
            {"range": "75 - 150", "ore": "Oily Blackmouth, Firefin Snapper, Longjaw Mud Snapper", "zones": "Westfall, Loch Modan, Darkshore, The Barrens, Silverpine Forest", "tips": "Odwiedź trenera: Journeyman. Szukaj wirek rybnych (Schools of Fish) wzdłuż brzegu."},
            {"range": "150 - 225", "ore": "Mithril Head Trout, Raw Bristle Whisker Catfish", "zones": "Hillsbrad Foothills, Wetlands, Ashenvale, Alterac Mountains, Stranglethorn", "tips": "Książkę 'Expert Fishing - The Bass and You' kupisz u vendora w Booty Bay."},
            {"range": "225 - 300", "ore": "Raw Nightfin Snapper, Raw Sunscale Salmon, Raw Winter Squid", "zones": "Feralas (Jademir Lake), Tanaris (Steamwheedle Port), Azshara (Bay of Storms)", "tips": "Quest na Artisan 'Nat Pagle, Extreme Angler' w Dustwallow Marsh. Wymaga przynęty +75/+100!"}
        ]
    }
}

