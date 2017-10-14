from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2203   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2203.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Royal Army Officer',                   # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Manoria Village',                      # 12
        'Mercia Orphanage',                     # 13
        'Ruan',                                 # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT29/CH12100 ._CH',             # 00
        'ED6_DT29/CH12101 ._CH',             # 01
        'ED6_DT29/CH12150 ._CH',             # 02
        'ED6_DT29/CH12151 ._CH',             # 03
        'ED6_DT07/CH01600 ._CH',             # 04
        'ED6_DT07/CH01640 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH12100P._CP',             # 00
        'ED6_DT29/CH12101P._CP',             # 01
        'ED6_DT29/CH12150P._CP',             # 02
        'ED6_DT29/CH12151P._CP',             # 03
        'ED6_DT07/CH01600P._CP',             # 04
        'ED6_DT07/CH01640P._CP',             # 05
    )

    DeclNpc(
        X                   = -95890,
        Z                   = -5970,
        Y                   = 5490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -94000,
        Z                   = -6040,
        Y                   = 4900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -86590,
        Z                   = -2090,
        Y                   = 20010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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

    DeclNpc(
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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

    DeclNpc(
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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


    DeclMonster(
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x184,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77980,
        TriggerZ            = -6870,
        TriggerY            = -11780,
        TriggerRange        = 1000,
        ActorX              = -77540,
        ActorZ              = -6730,
        ActorY              = -11140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29A",          # 00, 0
        "Function_1_30A",          # 01, 1
        "Function_2_35E",          # 02, 2
        "Function_3_651",          # 03, 3
        "Function_4_8C3",          # 04, 4
        "Function_5_AE1",          # 05, 5
        "Function_6_C46",          # 06, 6
        "Function_7_D5B",          # 07, 7
        "Function_8_DA5",          # 08, 8
    )


    def Function_0_29A(): pass

    label("Function_0_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, -32430, -1940, 54880, 135)
    SetChrPos(0xA, -117980, -2100, 18390, 135)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_309")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_309")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    label("loc_309")

    Return()

    # Function_0_29A end

    def Function_1_30A(): pass

    label("Function_1_30A")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x230026)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_6F(0x0, 0)
    Jump("loc_344")

    label("loc_33D")

    OP_6F(0x0, 60)

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356")
    OP_6F(0x1, 0)
    Jump("loc_35D")

    label("loc_356")

    OP_6F(0x1, 60)

    label("loc_35D")

    Return()

    # Function_1_30A end

    def Function_2_35E(): pass

    label("Function_2_35E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440")

    ChrTalk(    #0
        0xFE,
        (
            "The royal academy's fallen into enemy\x01",
            "hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "The enemy's plans are unclear, and we\x01",
            "don't know where they might strike next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "For safety's sake, we're patrolling the\x01",
            "village and orphanage.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4FD")

    label("loc_440")


    ChrTalk(    #3
        0xFE,
        (
            "If the worst happens, all we can do is\x01",
            "try to cram the civilians into the patrol\x01",
            "ship and protect them there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "The ships still have plenty to offer,\x01",
            "even if we can't use the guns!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD")

    Jump("loc_64D")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_64D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")

    ChrTalk(    #5
        0xFE,
        "So you're bracers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "You can probably tell by looking at us,\x01",
            "but our patrol ship's currently grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "We've requested rescue, but who\x01",
            "knows how long that'll take.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_64D")

    label("loc_5CD")


    ChrTalk(    #8
        0xFE,
        (
            "We intend to stay on standby here until\x01",
            "rescue comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "We'll be able to watch out for ourselves.\x01",
            "Don't worry about us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64D")

    TalkEnd(0x8)
    Return()

    # Function_2_35E end

    def Function_3_651(): pass

    label("Function_3_651")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_71A")

    ChrTalk(    #10
        0xFE,
        "Our C.O. told us to protect this spot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "If the worst happens, we're to take the\x01",
            "women and children and evac them to\x01",
            "the patrol ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Man, I hope things don't get that bad...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BF")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")

    ChrTalk(    #13
        0xFE,
        (
            "We were on our way back to the fort\x01",
            "when the 'phenomenon' occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "It was close, but we managed to make\x01",
            "an emergency landing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Aidios, we were lucky this beach\x01",
            "was right beneath us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Thanks to that, the worst we suffered\x01",
            "were some bumps and bruises.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8BF")

    label("loc_83C")


    ChrTalk(    #17
        0xFE,
        (
            "We had to take a guy to the nearby village,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "He was just bad enough that we figured\x01",
            "he needed a place with a bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF")

    TalkEnd(0x9)
    Return()

    # Function_3_651 end

    def Function_4_8C3(): pass

    label("Function_4_8C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_99F")

    ChrTalk(    #19
        0xFE,
        (
            "Those soldiers in crimson showed up\x01",
            "somewhere near here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "And according to the rumors,\x01",
            "their guns still work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "How in Gehenna are we supposed to fight\x01",
            "them with nothing but bayonets...?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADD")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6E")

    ChrTalk(    #22
        0xFE,
        (
            "Wow, to think there'd be people on\x01",
            "the roads at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Well, you'll have to keep yourselves safe,\x01",
            "I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I hate to say it, but we've got our\x01",
            "hands full.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_ADD")

    label("loc_A6E")


    ChrTalk(    #25
        0xFE,
        (
            "Aidios, is the rescue squad still\x01",
            "not here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I really don't want to hang out near\x01",
            "all these monsters!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADD")

    TalkEnd(0xFE)
    Return()

    # Function_4_8C3 end

    def Function_5_AE1(): pass

    label("Function_5_AE1")

    OP_EA(0x2, 0xE0, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3DC, 1)"), scpexpr(EXPR_END)), "loc_B52")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "Found \x1F\xDC\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1302)
    Jump("loc_BB6")

    label("loc_B52")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "Found \x1F\xDC\x03\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xDC\x03\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_BB6")

    Jump("loc_C38")

    label("loc_BB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05The chest is empty, but you briefly consider\x01",
            "taking it along with you and selling it to\x01",
            "someone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C38")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_AE1 end

    def Function_6_C46(): pass

    label("Function_6_C46")

    OP_EA(0x2, 0xE1, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_CB7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1303)
    Jump("loc_D1B")

    label("loc_CB7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_D1B")

    Jump("loc_D4D")

    label("loc_D1E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Yep, it's empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D4D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C46 end

    def Function_7_D5B(): pass

    label("Function_7_D5B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05North: Mercia Orphanage\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_D5B end

    def Function_8_DA5(): pass

    label("Function_8_DA5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x05East: City of Ruan - 238 selge\x01",
            "West: Manoria Village - 74 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_DA5 end

    SaveToFile()

Try(main)
