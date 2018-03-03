from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4162   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4162.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_27F",          # 01, 1
        "Function_2_280",          # 02, 2
        "Function_3_416",          # 03, 3
        "Function_4_636",          # 04, 4
        "Function_5_88C",          # 05, 5
        "Function_6_97B",          # 06, 6
        "Function_7_A68",          # 07, 7
        "Function_8_B58",          # 08, 8
        "Function_9_CE6",          # 09, 9
        "Function_10_EDD",         # 0A, 10
        "Function_11_1100",        # 0B, 11
        "Function_12_1329",        # 0C, 12
        "Function_13_14EA",        # 0D, 13
        "Function_14_1629",        # 0E, 14
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Return()

    # Function_0_27E end

    def Function_1_27F(): pass

    label("Function_1_27F")

    Return()

    # Function_1_27F end

    def Function_2_280(): pass

    label("Function_2_280")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05[Tetracyclic Tower Outer Wall Segment]         Age: Pre-Septian?\x01",
            "This wall segment was cut and carried from a Tetracyclic Tower--\x01",
            "a structure built shortly after the Great Collapse.\x01",
            "Depicted upon it are a staff-wielding priest and a winged god-\x01",
            "like being, typical of period frescas. Scholars continue to\x01",
            "examine the design for any connection with Aidios.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_280 end

    def Function_3_416(): pass

    label("Function_3_416")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05[Septian 1150-1200  ~The Orbal Post-Revolutionary World~]\x01",
            "It's been only 50 years since Prof. C. Epstein invented orbments,\x01",
            "and world technology has advanced at lightning speed ever since.\x01",
            "Perhaps the most notable representative of these advances is the \x01",
            "modern orbal-powered airship. These 'orbalships' are already used\x01",
            "extensively in Liberl, but neighboring nations such as Erebonia\x01",
            "have also begun to devote themselves to their manufacture as well,\x01",
            "and smaller-sized airships are also used.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_416 end

    def Function_4_636(): pass

    label("Function_4_636")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x05[Pre-Septian Calendar  ~The Ancient Civilization of Zemuria~]\x01",
            "Around 1,200 years ago, the advanced civilization of Zemuria was\x01",
            "at its peak. Then, suddenly and inexplicably, it disappeared.\x01",
            "A 'Great Collapse' occurred, destroying the Zemurian culture and\x01",
            "plunging its people into a dark age of ruin. The items exhibited\x01",
            "on the first floor are from the very beginning of this era. They\x01",
            "aren't believed to be products of the ancient civilization itself,\x01",
            "but nonetheless, its influence is clearly visible upon them, giving\x01",
            "them immense academic worth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_636 end

    def Function_5_88C(): pass

    label("Function_5_88C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x05[Ancient Lantern]                              Age: Pre-Septian?\x01",
            "A device built to hold fire. Most often found near towers and\x01",
            "other ceremonial structures. May have religious significance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_88C end

    def Function_6_97B(): pass

    label("Function_6_97B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        (
            "\x07\x05[Stone Pillar with Relief]                     Age: Pre-Septian?\x01",
            "Found at the bottom of Valleria Lake. Adorned with reliefs\x01",
            "similar to those found on the walls of the Tetracyclic Towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_97B end

    def Function_7_A68(): pass

    label("Function_7_A68")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x05[Floor Tile]                                   Age: Pre-Septian?\x01",
            "A piece of tiled floor from inside a ruined building. Broken\x01",
            "stones fit together to create beautiful and intricate patterns.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_A68 end

    def Function_8_B58(): pass

    label("Function_8_B58")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        (
            "\x07\x05[Septian Calendar 1-500  ~The Dark Age of Ruin~]\x01",
            "Immediately following the Great Collapse, the world was plunged\x01",
            "into confusion, signaling the beginning of what came to be\x01",
            "referred to as the Dark Ages. \x01",
            "This era was defined by almost endless conflict between various\x01",
            "powers and numerous nations, large and small, and lasted for \x01",
            "roughly 500 years.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_B58 end

    def Function_9_CE6(): pass

    label("Function_9_CE6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x05[Knights' Equipment]                    Age: Septian Calendar 500\x01",
            "In an era defined by conflict, war became a way of life, and as a\x01",
            "result, warriors came to wield great influence in society. This\x01",
            "eventually led to them becoming a privileged social class of their\x01",
            "own.\x01",
            "The knights wielded armaments like these when they went out onto \x01",
            "the battlefield, returning with more spoils and land, and gradually\x01",
            "increasing their influence and power all the more.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_CE6 end

    def Function_10_EDD(): pass

    label("Function_10_EDD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        (
            "\x07\x05[Septian Calendar 500-1100  ~The Septian Era~]\x01",
            "The first appearance of the Septian Church occurred around the\x01",
            "year 500 and marked the end of the Dark Ages.\x01",
            "The church, centered around the 'Goddess of the Sky' Aidios and\x01",
            "espousing an ideology of human salvation, began to take an active\x01",
            "role in society and rapidly permeated social consciousness. \x01",
            "Eventually, the nobility and knight class could no longer ignore\x01",
            "the church's power, and a new order was established with the \x01",
            "church at the center. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_EDD end

    def Function_11_1100(): pass

    label("Function_11_1100")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x05[Ancient Artifacts]                                 Age: Unknown\x01",
            "'Artifact' (noun) - A relic of any shape or size found in an\x01",
            "ancient ruin and generally of unknown or uncertain purpose.\x01",
            "The church believes these artifacts have some connection with\x01",
            "the Sept-Terrions--gifts from Aidios--and their recovery is\x01",
            "one of the duties that the church fulfills. \x01",
            "Artifacts are said to have supernatural powers, but those on\x01",
            "display here are all ones that have since lost said powers and\x01",
            "are no longer functional.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1100 end

    def Function_12_1329(): pass

    label("Function_12_1329")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x05[Church Ritual Items]          Age: Septian Calendar 900 (approx.)\x01",
            "The church has long been a source of art, and this has been true\x01",
            "since the dawn of the Septian Era. It was around the year 900,\x01",
            "however, that the current likeness of Aidios is thought to have\x01",
            "been first created. Likewise, many of the ritual items used by\x01",
            "the church today first assumed their present forms in this time\x01",
            "period, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_1329 end

    def Function_13_14EA(): pass

    label("Function_13_14EA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #11
        (
            "\x07\x05[Church Testaments, Manuscript]        Age: Septian Calendar 500\x01",
            "A handwritten copy of the scriptures used by the church at the\x01",
            "end of the Dark Ages. The ability to print did not exist in the\x01",
            "Middle Ages, leaving no choice but to copy by hand onto pieces\x01",
            "of parchment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_14EA end

    def Function_14_1629(): pass

    label("Function_14_1629")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x05[Medieval Loom]                        Age: Septian Calendar 900\x01",
            "A man-powered machine used to spin thread. As the Septian Era\x01",
            "continued and people became accustomed to peace, cotton and \x01",
            "other crops became more widely cultivated and sold. This was \x01",
            "also the era in which handicrafts with the intent to obtain money \x01",
            "came into practice.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1629 end

    SaveToFile()

Try(main)
