from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0701   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0701.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0701_1 ._SN',
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
        'Airliner, Cecilia',                    # 9
        'Fabree',                               # 10
        'Skip',                                 # 11
        'Zosimov',                              # 12
        'Rolent',                               # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 43100,
        Z                   = 4000,
        Y                   = 31800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 38670,
        Z                   = 0,
        Y                   = 50200,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 28880,
        Z                   = 0,
        Y                   = 3000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 35320,
        Z                   = 0,
        Y                   = -13920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 37790,
        Y                   = 3000,
        Z                   = 40490,
        Range               = 36410,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x92D6,
        Unknown_18          = 0x10000,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 38000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 38000,
        ActorZ              = 2200,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 4000,
        TriggerY            = 41300,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 5500,
        ActorY              = 41800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34500,
        TriggerZ            = 0,
        TriggerY            = 46570,
        TriggerRange        = 800,
        ActorX              = 35000,
        ActorZ              = 1500,
        ActorY              = 46570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_26C",          # 02, 2
        "Function_3_282",          # 03, 3
        "Function_4_65F",          # 04, 4
        "Function_5_9DC",          # 05, 5
        "Function_6_ABF",          # 06, 6
        "Function_7_B7A",          # 07, 7
        "Function_8_C08",          # 08, 8
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    SetChrPos(0x9, 43080, 4000, 32060, 270)

    label("loc_20A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)

    label("loc_21A")

    Return()

    # Function_0_1E6 end

    def Function_1_21B(): pass

    label("Function_1_21B")

    OP_16(0x2, 0xFA0, 0xFFFE98A0, 0xFFFE8518, 0x230007)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_245")
    OP_71(0xA, 0x4)

    label("loc_245")

    OP_72(0xB, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B")
    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xFDE8, 0x0)

    label("loc_26B")

    Return()

    # Function_1_21B end

    def Function_2_26C(): pass

    label("Function_2_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_281")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_26C")

    label("loc_281")

    Return()

    # Function_2_26C end

    def Function_3_282(): pass

    label("Function_3_282")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FD")

    ChrTalk(    #0
        0xFE,
        (
            "Hey, bracer folks.\x01",
            "Good work with all that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Been quite an ordeal, but...\x01",
            "keep a lid on it, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656")

    label("loc_2FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_381")

    ChrTalk(    #2
        0xFE,
        "Okay, hurry up and look inside the ship.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Aidios smite me... I'm pretty much ready\x01",
            "to get fired over this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656")

    label("loc_381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_393")
    Call(1, 3)
    Jump("loc_656")

    label("loc_393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_429")

    ChrTalk(    #4
        0xFE,
        "You're looking for Zosimov?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I...think Zosimov should be around here.\x01",
            "Somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Well, don't give up!\x01",
            "Have a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656")

    label("loc_429")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_4E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_4A1")

    ChrTalk(    #7
        0xFE,
        "Hey. You found the kitty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Seriously, up so late on this,\x01",
            "you guys are real troopers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DD")

    label("loc_4A1")


    ChrTalk(    #9
        0xFE,
        "Hmm? Looking for Quint?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "He went to get some food.\x02",
    )

    CloseMessageWindow()

    label("loc_4DD")

    Jump("loc_656")

    label("loc_4E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_56D")

    ChrTalk(    #11
        0xFE,
        (
            "It was Skip who saw the cat.\x01",
            "I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "You should go ask him what he saw.\x01",
            "He's probably down by the warehouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656")

    label("loc_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_57E")
    Call(1, 0)
    Jump("loc_656")

    label("loc_57E")


    ChrTalk(    #13
        0xFE,
        (
            "Might be pointless, but I'm going over\x01",
            "everything again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Can't just kick back while the\x01",
            "passengers are waiting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "This fog, though.\x01",
            "I feel like I'm SWIMMING, not walking.\x01",
            "My clothes are plastered to me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_656")

    TalkEnd(0x9)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_3_282 end

    def Function_4_65F(): pass

    label("Function_4_65F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6FA")

    ChrTalk(    #16
        0xFE,
        "Yo, bracers. Found the cat, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Fabree seems awfully relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "What I don't get is why it mattered\x01",
            "so much to him, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_6FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_75E")

    ChrTalk(    #19
        0xFE,
        (
            "You guys sure are burning the\x01",
            "midnight oil!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "How about it? You find the cat?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_75E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_7E7")

    ChrTalk(    #21
        0xFE,
        (
            "If you want to look inside the ship,\x01",
            "you should talk to Fabree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He's probably up on deck.\x01",
            "Go look for him there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_7E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_89B")

    ChrTalk(    #23
        0xFE,
        (
            "Heya, guys. Were you able\x01",
            "to find Quint?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Zosimov should be around the dock,\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I say somewhere, but...\x01",
            "I haven't actually SEEN Zosimov lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_925")

    ChrTalk(    #26
        0xFE,
        (
            "Try asking Quint, the helmsman,\x01",
            "about the cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "He just went off to get dinner,\x01",
            "so he should be in town somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_925")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_936")
    Call(1, 1)
    Jump("loc_9D8")

    label("loc_936")


    ChrTalk(    #28
        0xFE,
        (
            "We all talked it over, and decided to\x01",
            "do a thorough check of the engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Of course, this fog's ridiculous, so as\x01",
            "soon as we're done, we're out of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D8")

    TalkEnd(0xA)
    Return()

    # Function_4_65F end

    def Function_5_9DC(): pass

    label("Function_5_9DC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A57")

    ChrTalk(    #30
        0xFE,
        "Found the kitty-cat, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "So she DID have some kittens!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "That explains why she was so noisy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABB")

    label("loc_A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_AAC")

    ChrTalk(    #33
        0xFE,
        "Hey, keep going. No reason to stop now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Best of luck to you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABB")

    label("loc_AAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_ABB")
    Call(1, 2)

    label("loc_ABB")

    TalkEnd(0xB)
    Return()

    # Function_5_9DC end

    def Function_6_ABF(): pass

    label("Function_6_ABF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #35
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Grancel\x01",
            "⇒ To Bose\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #36
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_ABF end

    def Function_7_B7A(): pass

    label("Function_7_B7A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_B7A end

    def Function_8_C08(): pass

    label("Function_8_C08")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        "\x07\x05※Employees Only 《Liberl Orbalship Co.》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_C08 end

    SaveToFile()

Try(main)
