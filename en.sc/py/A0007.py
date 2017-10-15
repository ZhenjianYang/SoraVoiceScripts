from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0007   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '12350待機',                            # 9
        '12351移動',                            # 10
        '12352攻撃',                            # 11
        '12353ダメージ',                        # 12
        '12354倒れ',                            # 13
        '12360待機',                            # 14
        '12361移動',                            # 15
        '12362攻撃',                            # 16
        '12363ダメージ',                        # 17
        '12364倒れ',                            # 18
        '12370待機',                            # 19
        '12371移動',                            # 20
        '12372攻撃',                            # 21
        '12373ダメージ',                        # 22
        '12374倒れ',                            # 23
        '12380待機',                            # 24
        '12381移動',                            # 25
        '12382攻撃',                            # 26
        '12383ダメージ',                        # 27
        '12384倒れ',                            # 28
        '12390待機',                            # 29
        '12391移動',                            # 30
        '12392攻撃',                            # 31
        '12393ダメージ',                        # 32
        '12394倒れ',                            # 33
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
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT29/CH12350 ._CH',             # 00
        'ED6_DT29/CH12351 ._CH',             # 01
        'ED6_DT29/CH12352 ._CH',             # 02
        'ED6_DT29/CH12353 ._CH',             # 03
        'ED6_DT29/CH12354 ._CH',             # 04
        'ED6_DT29/CH12364 ._CH',             # 05
        'ED6_DT29/CH12364 ._CH',             # 06
        'ED6_DT29/CH12364 ._CH',             # 07
        'ED6_DT29/CH12364 ._CH',             # 08
        'ED6_DT29/CH12364 ._CH',             # 09
        'ED6_DT29/CH12360 ._CH',             # 0A
        'ED6_DT29/CH12361 ._CH',             # 0B
        'ED6_DT29/CH12362 ._CH',             # 0C
        'ED6_DT29/CH12363 ._CH',             # 0D
        'ED6_DT29/CH12364 ._CH',             # 0E
        'ED6_DT29/CH12364 ._CH',             # 0F
        'ED6_DT29/CH12364 ._CH',             # 10
        'ED6_DT29/CH12364 ._CH',             # 11
        'ED6_DT29/CH12364 ._CH',             # 12
        'ED6_DT29/CH12364 ._CH',             # 13
        'ED6_DT29/CH12370 ._CH',             # 14
        'ED6_DT29/CH12371 ._CH',             # 15
        'ED6_DT29/CH12372 ._CH',             # 16
        'ED6_DT29/CH12373 ._CH',             # 17
        'ED6_DT29/CH12374 ._CH',             # 18
        'ED6_DT29/CH12364 ._CH',             # 19
        'ED6_DT29/CH12364 ._CH',             # 1A
        'ED6_DT29/CH12364 ._CH',             # 1B
        'ED6_DT29/CH12364 ._CH',             # 1C
        'ED6_DT29/CH12364 ._CH',             # 1D
        'ED6_DT29/CH12380 ._CH',             # 1E
        'ED6_DT29/CH12381 ._CH',             # 1F
        'ED6_DT29/CH12382 ._CH',             # 20
        'ED6_DT29/CH12383 ._CH',             # 21
        'ED6_DT29/CH12384 ._CH',             # 22
        'ED6_DT29/CH12364 ._CH',             # 23
        'ED6_DT29/CH12364 ._CH',             # 24
        'ED6_DT29/CH12364 ._CH',             # 25
        'ED6_DT29/CH12364 ._CH',             # 26
        'ED6_DT29/CH12364 ._CH',             # 27
        'ED6_DT29/CH12390 ._CH',             # 28
        'ED6_DT29/CH12391 ._CH',             # 29
        'ED6_DT29/CH12392 ._CH',             # 2A
        'ED6_DT29/CH12393 ._CH',             # 2B
        'ED6_DT29/CH12394 ._CH',             # 2C
        'ED6_DT29/CH12364 ._CH',             # 2D
        'ED6_DT29/CH12364 ._CH',             # 2E
        'ED6_DT29/CH12364 ._CH',             # 2F
        'ED6_DT29/CH12364 ._CH',             # 30
        'ED6_DT29/CH12364 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT29/CH12350P._CP',             # 00
        'ED6_DT29/CH12351P._CP',             # 01
        'ED6_DT29/CH12352P._CP',             # 02
        'ED6_DT29/CH12353P._CP',             # 03
        'ED6_DT29/CH12354P._CP',             # 04
        'ED6_DT29/CH12364P._CP',             # 05
        'ED6_DT29/CH12364P._CP',             # 06
        'ED6_DT29/CH12364P._CP',             # 07
        'ED6_DT29/CH12364P._CP',             # 08
        'ED6_DT29/CH12364P._CP',             # 09
        'ED6_DT29/CH12360P._CP',             # 0A
        'ED6_DT29/CH12361P._CP',             # 0B
        'ED6_DT29/CH12362P._CP',             # 0C
        'ED6_DT29/CH12363P._CP',             # 0D
        'ED6_DT29/CH12364P._CP',             # 0E
        'ED6_DT29/CH12364P._CP',             # 0F
        'ED6_DT29/CH12364P._CP',             # 10
        'ED6_DT29/CH12364P._CP',             # 11
        'ED6_DT29/CH12364P._CP',             # 12
        'ED6_DT29/CH12364P._CP',             # 13
        'ED6_DT29/CH12370P._CP',             # 14
        'ED6_DT29/CH12371P._CP',             # 15
        'ED6_DT29/CH12372P._CP',             # 16
        'ED6_DT29/CH12373P._CP',             # 17
        'ED6_DT29/CH12374P._CP',             # 18
        'ED6_DT29/CH12364P._CP',             # 19
        'ED6_DT29/CH12364P._CP',             # 1A
        'ED6_DT29/CH12364P._CP',             # 1B
        'ED6_DT29/CH12364P._CP',             # 1C
        'ED6_DT29/CH12364P._CP',             # 1D
        'ED6_DT29/CH12380P._CP',             # 1E
        'ED6_DT29/CH12381P._CP',             # 1F
        'ED6_DT29/CH12382P._CP',             # 20
        'ED6_DT29/CH12383P._CP',             # 21
        'ED6_DT29/CH12384P._CP',             # 22
        'ED6_DT29/CH12364P._CP',             # 23
        'ED6_DT29/CH12364P._CP',             # 24
        'ED6_DT29/CH12364P._CP',             # 25
        'ED6_DT29/CH12364P._CP',             # 26
        'ED6_DT29/CH12364P._CP',             # 27
        'ED6_DT29/CH12390P._CP',             # 28
        'ED6_DT29/CH12391P._CP',             # 29
        'ED6_DT29/CH12392P._CP',             # 2A
        'ED6_DT29/CH12393P._CP',             # 2B
        'ED6_DT29/CH12394P._CP',             # 2C
        'ED6_DT29/CH12364P._CP',             # 2D
        'ED6_DT29/CH12364P._CP',             # 2E
        'ED6_DT29/CH12364P._CP',             # 2F
        'ED6_DT29/CH12364P._CP',             # 30
        'ED6_DT29/CH12364P._CP',             # 31
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
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
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_55A",          # 00, 0
        "Function_1_55B",          # 01, 1
        "Function_2_55C",          # 02, 2
        "Function_3_5CF",          # 03, 3
        "Function_4_5D0",          # 04, 4
    )


    def Function_0_55A(): pass

    label("Function_0_55A")

    Return()

    # Function_0_55A end

    def Function_1_55B(): pass

    label("Function_1_55B")

    Return()

    # Function_1_55B end

    def Function_2_55C(): pass

    label("Function_2_55C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_589"),
        (1, "loc_591"),
        (2, "loc_599"),
        (3, "loc_5A1"),
        (4, "loc_5A9"),
        (5, "loc_5B1"),
        (SWITCH_DEFAULT, "loc_5B9"),
    )


    label("loc_589")

    Sleep(100)
    Jump("loc_5B9")

    label("loc_591")

    Sleep(100)
    Jump("loc_5B9")

    label("loc_599")

    Sleep(200)
    Jump("loc_5B9")

    label("loc_5A1")

    Sleep(300)
    Jump("loc_5B9")

    label("loc_5A9")

    Sleep(400)
    Jump("loc_5B9")

    label("loc_5B1")

    Sleep(500)
    Jump("loc_5B9")

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B9")

    label("loc_5CE")

    Return()

    # Function_2_55C end

    def Function_3_5CF(): pass

    label("Function_3_5CF")

    Return()

    # Function_3_5CF end

    def Function_4_5D0(): pass

    label("Function_4_5D0")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_5D0 end

    SaveToFile()

Try(main)
