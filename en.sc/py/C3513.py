from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3513   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT09/CH10710 ._CH',             # 00
        'ED6_DT09/CH10711 ._CH',             # 01
        'ED6_DT09/CH10720 ._CH',             # 02
        'ED6_DT09/CH10721 ._CH',             # 03
        'ED6_DT09/CH10730 ._CH',             # 04
        'ED6_DT09/CH10731 ._CH',             # 05
        'ED6_DT09/CH10740 ._CH',             # 06
        'ED6_DT09/CH10741 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10710P._CP',             # 00
        'ED6_DT09/CH10711P._CP',             # 01
        'ED6_DT09/CH10720P._CP',             # 02
        'ED6_DT09/CH10721P._CP',             # 03
        'ED6_DT09/CH10730P._CP',             # 04
        'ED6_DT09/CH10731P._CP',             # 05
        'ED6_DT09/CH10740P._CP',             # 06
        'ED6_DT09/CH10741P._CP',             # 07
    )

    DeclMonster(
        X                   = 13970,
        Z                   = 0,
        Y                   = -14160,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F8,
        Unknown_18          = 5504,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14060,
        Z                   = 0,
        Y                   = -14180,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F8,
        Unknown_18          = 5505,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10,
        Z                   = 0,
        Y                   = -3340,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5506,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3070,
        Z                   = 0,
        Y                   = -30,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5507,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -100,
        Z                   = 0,
        Y                   = 3100,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5508,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3090,
        Z                   = 0,
        Y                   = 40,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5509,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1110,
        Z                   = 0,
        Y                   = -1180,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5510,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1000,
        Z                   = 0,
        Y                   = -1130,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5511,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1090,
        Z                   = 0,
        Y                   = 1010,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5512,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1130,
        Z                   = 0,
        Y                   = 1030,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5513,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -70,
        Z                   = 0,
        Y                   = -40,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5514,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12560,
        Z                   = 0,
        Y                   = 17070,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5515,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13140,
        Z                   = 0,
        Y                   = 17140,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5516,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 12560,
        TriggerZ            = 0,
        TriggerY            = -18130,
        TriggerRange        = 1000,
        ActorX              = 12660,
        ActorZ              = 0,
        ActorY              = -18840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12820,
        TriggerZ            = 0,
        TriggerY            = -17830,
        TriggerRange        = 1000,
        ActorX              = -12820,
        ActorZ              = 0,
        ActorY              = -18490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29E",          # 00, 0
        "Function_1_29F",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_4AC",          # 03, 3
    )


    def Function_0_29E(): pass

    label("Function_0_29E")

    Return()

    # Function_0_29E end

    def Function_1_29F(): pass

    label("Function_1_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1")
    OP_6F(0x0, 0)
    Jump("loc_2B8")

    label("loc_2B1")

    OP_6F(0x0, 60)

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA")
    OP_6F(0x1, 0)
    Jump("loc_2D1")

    label("loc_2CA")

    OP_6F(0x1, 60)

    label("loc_2D1")

    OP_E0(0x0, 0x3C, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x14, 0xBA, 0xFF, 0xFF)
    OP_E0(0x1, 0x28, 0xCE, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0x40, 0xBB, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 0)), scpexpr(EXPR_END)), "loc_2F9")
    SetChrFlags(0x8, 0x80)

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 1)), scpexpr(EXPR_END)), "loc_305")
    SetChrFlags(0x9, 0x80)

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 2)), scpexpr(EXPR_END)), "loc_311")
    SetChrFlags(0xA, 0x80)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 3)), scpexpr(EXPR_END)), "loc_31D")
    SetChrFlags(0xB, 0x80)

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 4)), scpexpr(EXPR_END)), "loc_329")
    SetChrFlags(0xC, 0x80)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 5)), scpexpr(EXPR_END)), "loc_335")
    SetChrFlags(0xD, 0x80)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 6)), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xE, 0x80)

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B0, 7)), scpexpr(EXPR_END)), "loc_34D")
    SetChrFlags(0xF, 0x80)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 0)), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0x10, 0x80)

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 1)), scpexpr(EXPR_END)), "loc_365")
    SetChrFlags(0x11, 0x80)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 2)), scpexpr(EXPR_END)), "loc_371")
    SetChrFlags(0x12, 0x80)

    label("loc_371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 3)), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0x13, 0x80)

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 4)), scpexpr(EXPR_END)), "loc_389")
    SetChrFlags(0x14, 0x80)

    label("loc_389")

    Return()

    # Function_1_29F end

    def Function_2_38A(): pass

    label("Function_2_38A")

    OP_EA(0x2, 0xCB, 0x0, 0x0)
    OP_EA(0x2, 0xB, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B8, 1)"), scpexpr(EXPR_END)), "loc_400")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xB8\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1547)
    Jump("loc_464")

    label("loc_400")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xB8\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xB8\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_464")

    Jump("loc_49E")

    label("loc_467")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Sorry, kid. I'm retired.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_49E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_38A end

    def Function_3_4AC(): pass

    label("Function_3_4AC")

    OP_EA(0x2, 0xCC, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_51D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1548)
    Jump("loc_581")

    label("loc_51D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_581")

    Jump("loc_5B6")

    label("loc_584")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Back again, are we?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5B6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4AC end

    SaveToFile()

Try(main)
