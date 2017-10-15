from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4204   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
    )

    DeclMonster(
        X                   = 65650,
        Z                   = 0,
        Y                   = 11910,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x275,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32420,
        Z                   = 0,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x275,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3110,
        Z                   = 0,
        Y                   = -78770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22940,
        Z                   = 0,
        Y                   = -72800,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x275,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -48250,
        Z                   = 1000,
        Y                   = -18050,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39750,
        Z                   = 0,
        Y                   = 5980,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x274,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -20850,
        TriggerZ            = 0,
        TriggerY            = -89270,
        TriggerRange        = 1000,
        ActorX              = -20940,
        ActorZ              = 1500,
        ActorY              = -88690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -48220,
        TriggerZ            = 0,
        TriggerY            = 6340,
        TriggerRange        = 1000,
        ActorX              = -48190,
        ActorZ              = 1500,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_264",          # 02, 2
        "Function_3_3C4",          # 03, 3
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Return()

    # Function_0_21A end

    def Function_1_21B(): pass

    label("Function_1_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D")
    OP_6F(0x0, 0)
    Jump("loc_234")

    label("loc_22D")

    OP_6F(0x0, 60)

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246")
    OP_6F(0x1, 0)
    Jump("loc_24D")

    label("loc_246")

    OP_6F(0x1, 60)

    label("loc_24D")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_21B end

    def Function_2_264(): pass

    label("Function_2_264")

    OP_EA(0x2, 0x7, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2D5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1720)
    Jump("loc_339")

    label("loc_2D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_339")

    Jump("loc_3B6")

    label("loc_33C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05The chest's empty, but if you keep opening and\x01",
            "closing the lid, it looks like it's talking!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3B6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_264 end

    def Function_3_3C4(): pass

    label("Function_3_3C4")

    OP_EA(0x2, 0x8, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x153, 1)"), scpexpr(EXPR_END)), "loc_435")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x53\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1721)
    Jump("loc_499")

    label("loc_435")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x53\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x53\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_499")

    Jump("loc_526")

    label("loc_49C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05This chest is better than the others. Why?\x01",
            "Secret. But we'll tell you if you put what you\x01",
            "took back inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_526")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3C4 end

    SaveToFile()

Try(main)
