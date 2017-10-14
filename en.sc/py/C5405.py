from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5405   ._SN',
        MapName             = 'Other',
        Location            = 'C5405.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'ヴァンガード',                         # 9
        'ポートシーカー',                       # 10
        'ポートシーカー',                       # 11
        'ヴォーグル570（青）',                  # 12
        'ヴォーグル570（青）',                  # 13
        'ポートシーカー',                       # 14
        'ヴォーグル235（赤）',                  # 15
        'ヴォーグル235（赤）',                  # 16
        'ヴァンガード',                         # 17
        'ポートシーカー',                       # 18
        'ポートシーカー',                       # 19
        'ヴォーグル570（青）',                  # 20
        'ヴォーグル570（青）',                  # 21
        'ポートシーカー',                       # 22
        'ヴォーグル235（赤）',                  # 23
        'ヴォーグル235（赤）',                  # 24
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12350 ._CH',             # 02
        'ED6_DT29/CH12351 ._CH',             # 03
        'ED6_DT29/CH12580 ._CH',             # 04
        'ED6_DT29/CH12581 ._CH',             # 05
        'ED6_DT29/CH12320 ._CH',             # 06
        'ED6_DT29/CH12321 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12350P._CP',             # 02
        'ED6_DT29/CH12351P._CP',             # 03
        'ED6_DT29/CH12580P._CP',             # 04
        'ED6_DT29/CH12581P._CP',             # 05
        'ED6_DT29/CH12320P._CP',             # 06
        'ED6_DT29/CH12321P._CP',             # 07
    )

    DeclMonster(
        X                   = 980,
        Z                   = -1000,
        Y                   = 16570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x425,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16140,
        Z                   = -1000,
        Y                   = 43740,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14260,
        Z                   = -1000,
        Y                   = 43870,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17850,
        Z                   = -1000,
        Y                   = 145970,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12070,
        Z                   = -1000,
        Y                   = 145960,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2860,
        Z                   = -1000,
        Y                   = 174250,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17920,
        Z                   = -1000,
        Y                   = 202020,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12050,
        Z                   = -1000,
        Y                   = 201850,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 980,
        Z                   = -1000,
        Y                   = 16570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16140,
        Z                   = -1000,
        Y                   = 43740,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14260,
        Z                   = -1000,
        Y                   = 43870,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17850,
        Z                   = -1000,
        Y                   = 145970,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12070,
        Z                   = -1000,
        Y                   = 145960,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2860,
        Z                   = -1000,
        Y                   = 174250,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17920,
        Z                   = -1000,
        Y                   = 202020,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12050,
        Z                   = -1000,
        Y                   = 201850,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2C3",          # 01, 1
        "Function_2_357",          # 02, 2
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2")
    Event(0, 2)

    label("loc_2C2")

    Return()

    # Function_0_2AA end

    def Function_1_2C3(): pass

    label("Function_1_2C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E1")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_356")

    label("loc_32E")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_356")

    Return()

    # Function_1_2C3 end

    def Function_2_357(): pass

    label("Function_2_357")

    EventBegin(0x0)
    OP_6D(1020, -1000, -14680, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3790, 0)
    OP_6C(33000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, 1630, -1000, -15000, 0)
    SetChrPos(0x102, 480, -1000, -15000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(1260, -1000, 38780, 0)
    OP_67(0, 7970, -10000, 0)
    OP_6B(4310, 0)
    OP_6C(45000, 0)
    OP_6E(586, 0)
    SetChrPos(0x101, 1630, -1000, -12000, 0)
    SetChrPos(0x102, 480, -1000, -12000, 0)
    OP_0D()
    Sleep(500)

    def lambda_476():
        OP_6D(1440, -1000, 2800, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_476)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(1020, -1000, -11680, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3790, 0)
    OP_6C(33000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#1020F#4PHoly...\x02\x03",

            "Since when does an airship\x01",
            "have its own landing port...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1035FYes... The crimson ark, the Glorious,\x01",
            "pride of the society, is meant to be\x01",
            "a mothership, of sorts.\x02\x03",

            "#1030FIt can provide berthing to up to twelve\x01",
            "smaller vessels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1007F#4PThat's unbelievable!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)

    ChrTalk(    #3
        0x102,
        (
            "#1031F#6PI secured a ship earlier for our escape.\x02\x03",

            "It's in the hangar farthest in.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #4
        0x101,
        "#1006F#4PGot it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C28)
    OP_28(0x99, 0x1, 0x400)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_357 end

    SaveToFile()

Try(main)
