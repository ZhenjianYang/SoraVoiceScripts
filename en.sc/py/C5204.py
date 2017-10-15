from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5204   ._SN',
        MapName             = 'Other',
        Location            = 'C5204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60063",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12950 ._CH',             # 00
        'ED6_DT29/CH12951 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
        'ED6_DT29/CH12960 ._CH',             # 04
        'ED6_DT29/CH12961 ._CH',             # 05
        'ED6_DT29/CH13010 ._CH',             # 06
        'ED6_DT29/CH13011 ._CH',             # 07
        'ED6_DT29/CH12200 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
        'ED6_DT29/CH13020 ._CH',             # 0A
        'ED6_DT29/CH13021 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12950P._CP',             # 00
        'ED6_DT29/CH12951P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
        'ED6_DT29/CH12960P._CP',             # 04
        'ED6_DT29/CH12961P._CP',             # 05
        'ED6_DT29/CH13010P._CP',             # 06
        'ED6_DT29/CH13011P._CP',             # 07
        'ED6_DT29/CH12200P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
        'ED6_DT29/CH13020P._CP',             # 0A
        'ED6_DT29/CH13021P._CP',             # 0B
    )

    DeclNpc(
        X                   = -150030,
        Z                   = 2000,
        Y                   = 875370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 2390,
        Z                   = 0,
        Y                   = 76600,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x449,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100,
        Z                   = -4000,
        Y                   = 193690,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x520,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2770,
        Z                   = 0,
        Y                   = 326530,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x44A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -75530,
        Z                   = 0,
        Y                   = 464940,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x44B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -147410,
        Z                   = 0,
        Y                   = 551800,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x51E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -131350,
        Z                   = 0,
        Y                   = 659450,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x51F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -145610,
        Z                   = 0,
        Y                   = 674090,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x449,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -245920,
        Z                   = 0,
        Y                   = 774830,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x44A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -399040,
        Z                   = 0,
        Y                   = 877240,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x520,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -72380,
        TriggerZ            = 0,
        TriggerY            = 194000,
        TriggerRange        = 1000,
        ActorX              = -73040,
        ActorZ              = 0,
        ActorY              = 194050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72440,
        TriggerZ            = 0,
        TriggerY            = 194090,
        TriggerRange        = 1000,
        ActorX              = 73080,
        ActorZ              = 0,
        ActorY              = 194160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -150060,
        TriggerZ            = 0,
        TriggerY            = 874750,
        TriggerRange        = 1000,
        ActorX              = -150030,
        ActorZ              = 0,
        ActorY              = 875370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -154610,
        TriggerZ            = 0,
        TriggerY            = 872080,
        TriggerRange        = 1000,
        ActorX              = -155230,
        ActorZ              = 0,
        ActorY              = 872050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -145310,
        TriggerZ            = 0,
        TriggerY            = 872020,
        TriggerRange        = 1000,
        ActorX              = -144650,
        ActorZ              = 0,
        ActorY              = 872050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -253060,
        TriggerZ            = 0,
        TriggerY            = 874800,
        TriggerRange        = 1000,
        ActorX              = -253030,
        ActorZ              = 0,
        ActorY              = 875370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -249970,
        TriggerZ            = 0,
        TriggerY            = 874740,
        TriggerRange        = 1000,
        ActorX              = -250040,
        ActorZ              = 0,
        ActorY              = 875370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -247030,
        TriggerZ            = 0,
        TriggerY            = 874750,
        TriggerRange        = 1000,
        ActorX              = -246990,
        ActorZ              = 0,
        ActorY              = 875370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107900,
        TriggerZ            = 0,
        TriggerY            = 465080,
        TriggerRange        = 1000,
        ActorX              = -108520,
        ActorZ              = 0,
        ActorY              = 465050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_36A",          # 00, 0
        "Function_1_36B",          # 01, 1
        "Function_2_463",          # 02, 2
        "Function_3_479",          # 03, 3
        "Function_4_5A0",          # 04, 4
        "Function_5_72D",          # 05, 5
        "Function_6_910",          # 06, 6
        "Function_7_A51",          # 07, 7
        "Function_8_BCD",          # 08, 8
        "Function_9_D44",          # 09, 9
        "Function_10_E6F",         # 0A, 10
        "Function_11_F96",         # 0B, 11
    )


    def Function_0_36A(): pass

    label("Function_0_36A")

    Return()

    # Function_0_36A end

    def Function_1_36B(): pass

    label("Function_1_36B")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393")
    OP_6F(0xE, 0)
    Jump("loc_39A")

    label("loc_393")

    OP_6F(0xE, 60)

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC")
    OP_6F(0xF, 0)
    Jump("loc_3B3")

    label("loc_3AC")

    OP_6F(0xF, 60)

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5")
    OP_6F(0x10, 0)
    Jump("loc_3CC")

    label("loc_3C5")

    OP_6F(0x10, 60)

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE")
    OP_6F(0x11, 0)
    Jump("loc_3E5")

    label("loc_3DE")

    OP_6F(0x11, 60)

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7")
    OP_6F(0x12, 0)
    Jump("loc_3FE")

    label("loc_3F7")

    OP_6F(0x12, 60)

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410")
    OP_6F(0x13, 0)
    Jump("loc_417")

    label("loc_410")

    OP_6F(0x13, 60)

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429")
    OP_6F(0x14, 0)
    Jump("loc_430")

    label("loc_429")

    OP_6F(0x14, 60)

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442")
    OP_6F(0x15, 0)
    Jump("loc_449")

    label("loc_442")

    OP_6F(0x15, 60)

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B")
    OP_6F(0x16, 0)
    Jump("loc_462")

    label("loc_45B")

    OP_6F(0x16, 60)

    label("loc_462")

    Return()

    # Function_1_36B end

    def Function_2_463(): pass

    label("Function_2_463")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_478")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_463")

    label("loc_478")

    Return()

    # Function_2_463 end

    def Function_3_479(): pass

    label("Function_3_479")

    OP_EA(0x2, 0x1A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x1E)
    OP_73(0xE)
    OP_6F(0xE, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2340)
    Jump("loc_58E")

    label("loc_570")


    AnonymousTalk(    #1
        "\x07\x05You came back! *BLUSH*\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_58E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_479 end

    def Function_4_5A0(): pass

    label("Function_4_5A0")

    OP_EA(0x2, 0x1B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_611")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2341)
    Jump("loc_675")

    label("loc_611")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_675")

    Jump("loc_71F")

    label("loc_678")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Somewhere out there is a person who started\x01",
            "playing Trails in the Sky Second Chapter before\x01",
            "the first game. I bet they're very confused.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_71F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5A0 end

    def Function_5_72D(): pass

    label("Function_5_72D")

    OP_EA(0x2, 0x1C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_817")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_784():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_784)

    def lambda_79F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_79F)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #5
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x522, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_7F2"),
        (2, "loc_804"),
        (1, "loc_814"),
        (SWITCH_DEFAULT, "loc_817"),
    )


    label("loc_7F2")

    OP_A2(0x2343)
    OP_6F(0x10, 60)
    Sleep(500)
    Jump("loc_817")

    label("loc_804")

    OP_6F(0x10, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_814")

    OP_B4(0x0)
    Return()

    label("loc_817")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x180, 1)"), scpexpr(EXPR_END)), "loc_863")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        "Found \x1F\x80\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2342)
    Jump("loc_8C5")

    label("loc_863")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #7
        (
            "Found \x1F\x80\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x80\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_8C5")

    Jump("loc_902")

    label("loc_8C8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        "\x07\x05Sorry, better luck next time.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_902")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_72D end

    def Function_6_910(): pass

    label("Function_6_910")

    OP_EA(0x2, 0x1D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_981")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2344)
    Jump("loc_9E5")

    label("loc_981")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x01\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x01\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_9E5")

    Jump("loc_A43")

    label("loc_9E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05This chest is empty. You looted it already.\x01",
            "This is a haiku.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A43")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_910 end

    def Function_7_A51(): pass

    label("Function_7_A51")

    OP_EA(0x2, 0x1E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B29")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_AC2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2345)
    Jump("loc_B26")

    label("loc_AC2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_B26")

    Jump("loc_BBF")

    label("loc_B29")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05Disappointed by the lack of treasure, you briefly\x01",
            "consider carving a heart and some initials into\x01",
            "the chest. But whose?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BBF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A51 end

    def Function_8_BCD(): pass

    label("Function_8_BCD")

    OP_EA(0x2, 0x1F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_C3E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2346)
    Jump("loc_CA2")

    label("loc_C3E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_CA2")

    Jump("loc_D36")

    label("loc_CA5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05You flip open the lid, knowing full well you won't\x01",
            "find anything. You're still somehow disappointed\x01",
            "by the result.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D36")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_BCD end

    def Function_9_D44(): pass

    label("Function_9_D44")

    OP_EA(0x2, 0x20, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x468, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x14, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C5, 1)"), scpexpr(EXPR_END)), "loc_DB5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "Found \x1F\xC5\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2347)
    Jump("loc_E19")

    label("loc_DB5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "Found \x1F\xC5\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC5\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x14, 60)
    OP_70(0x14, 0x0)

    label("loc_E19")

    Jump("loc_E61")

    label("loc_E1C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Looks like another open-and-shut case!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E61")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D44 end

    def Function_10_E6F(): pass

    label("Function_10_E6F")

    OP_EA(0x2, 0x21, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x1E)
    OP_73(0x15)
    OP_6F(0x15, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2348)
    Jump("loc_F84")

    label("loc_F66")


    AnonymousTalk(    #22
        "\x07\x05Nya-ha! Made you look!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F84")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_E6F end

    def Function_11_F96(): pass

    label("Function_11_F96")

    OP_EA(0x2, 0x22, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_1007")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2349)
    Jump("loc_106B")

    label("loc_1007")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_106B")

    Jump("loc_10BE")

    label("loc_106E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05Could just be your imagination, but...it's empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10BE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_F96 end

    SaveToFile()

Try(main)
