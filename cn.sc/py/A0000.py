from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0000   ._SN',
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
        '12000待机',                            # 9
        '12001移动',                            # 10
        '12002攻击',                            # 11
        '12003伤害',                            # 12
        '12004倒下',                            # 13
        '12010待机',                            # 14
        '12011移动',                            # 15
        '12012攻击',                            # 16
        '12013伤害',                            # 17
        '12014倒下',                            # 18
        '12020待机',                            # 19
        '12021移动',                            # 20
        '12022攻击',                            # 21
        '12023伤害',                            # 22
        '12024倒下',                            # 23
        '12030待机',                            # 24
        '12031移动',                            # 25
        '12032攻击',                            # 26
        '12033伤害',                            # 27
        '12034倒下',                            # 28
        '12040待机',                            # 29
        '12041移动',                            # 30
        '12042攻击',                            # 31
        '12043伤害',                            # 32
        '12044倒下',                            # 33
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
        'ED6_DT29/CH12000 ._CH',             # 00
        'ED6_DT29/CH12001 ._CH',             # 01
        'ED6_DT29/CH12002 ._CH',             # 02
        'ED6_DT29/CH12003 ._CH',             # 03
        'ED6_DT29/CH12004 ._CH',             # 04
        'ED6_DT29/CH12364 ._CH',             # 05
        'ED6_DT29/CH12364 ._CH',             # 06
        'ED6_DT29/CH12364 ._CH',             # 07
        'ED6_DT29/CH12364 ._CH',             # 08
        'ED6_DT29/CH12364 ._CH',             # 09
        'ED6_DT29/CH12010 ._CH',             # 0A
        'ED6_DT29/CH12011 ._CH',             # 0B
        'ED6_DT29/CH12012 ._CH',             # 0C
        'ED6_DT29/CH12013 ._CH',             # 0D
        'ED6_DT29/CH12014 ._CH',             # 0E
        'ED6_DT29/CH12364 ._CH',             # 0F
        'ED6_DT29/CH12364 ._CH',             # 10
        'ED6_DT29/CH12364 ._CH',             # 11
        'ED6_DT29/CH12364 ._CH',             # 12
        'ED6_DT29/CH12364 ._CH',             # 13
        'ED6_DT29/CH12020 ._CH',             # 14
        'ED6_DT29/CH12021 ._CH',             # 15
        'ED6_DT29/CH12022 ._CH',             # 16
        'ED6_DT29/CH12023 ._CH',             # 17
        'ED6_DT29/CH12024 ._CH',             # 18
        'ED6_DT29/CH12364 ._CH',             # 19
        'ED6_DT29/CH12364 ._CH',             # 1A
        'ED6_DT29/CH12364 ._CH',             # 1B
        'ED6_DT29/CH12364 ._CH',             # 1C
        'ED6_DT29/CH12364 ._CH',             # 1D
        'ED6_DT29/CH12030 ._CH',             # 1E
        'ED6_DT29/CH12031 ._CH',             # 1F
        'ED6_DT29/CH12032 ._CH',             # 20
        'ED6_DT29/CH12033 ._CH',             # 21
        'ED6_DT29/CH12034 ._CH',             # 22
        'ED6_DT29/CH12364 ._CH',             # 23
        'ED6_DT29/CH12364 ._CH',             # 24
        'ED6_DT29/CH12364 ._CH',             # 25
        'ED6_DT29/CH12364 ._CH',             # 26
        'ED6_DT29/CH12364 ._CH',             # 27
        'ED6_DT29/CH12040 ._CH',             # 28
        'ED6_DT29/CH12041 ._CH',             # 29
        'ED6_DT29/CH12042 ._CH',             # 2A
        'ED6_DT29/CH12043 ._CH',             # 2B
        'ED6_DT29/CH12044 ._CH',             # 2C
        'ED6_DT29/CH12364 ._CH',             # 2D
        'ED6_DT29/CH12364 ._CH',             # 2E
        'ED6_DT29/CH12364 ._CH',             # 2F
        'ED6_DT29/CH12364 ._CH',             # 30
        'ED6_DT29/CH12364 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT29/CH12000P._CP',             # 00
        'ED6_DT29/CH12001P._CP',             # 01
        'ED6_DT29/CH12002P._CP',             # 02
        'ED6_DT29/CH12003P._CP',             # 03
        'ED6_DT29/CH12004P._CP',             # 04
        'ED6_DT29/CH12364P._CP',             # 05
        'ED6_DT29/CH12364P._CP',             # 06
        'ED6_DT29/CH12364P._CP',             # 07
        'ED6_DT29/CH12364P._CP',             # 08
        'ED6_DT29/CH12364P._CP',             # 09
        'ED6_DT29/CH12010P._CP',             # 0A
        'ED6_DT29/CH12011P._CP',             # 0B
        'ED6_DT29/CH12012P._CP',             # 0C
        'ED6_DT29/CH12013P._CP',             # 0D
        'ED6_DT29/CH12014P._CP',             # 0E
        'ED6_DT29/CH12364P._CP',             # 0F
        'ED6_DT29/CH12364P._CP',             # 10
        'ED6_DT29/CH12364P._CP',             # 11
        'ED6_DT29/CH12364P._CP',             # 12
        'ED6_DT29/CH12364P._CP',             # 13
        'ED6_DT29/CH12020P._CP',             # 14
        'ED6_DT29/CH12021P._CP',             # 15
        'ED6_DT29/CH12022P._CP',             # 16
        'ED6_DT29/CH12023P._CP',             # 17
        'ED6_DT29/CH12024P._CP',             # 18
        'ED6_DT29/CH12364P._CP',             # 19
        'ED6_DT29/CH12364P._CP',             # 1A
        'ED6_DT29/CH12364P._CP',             # 1B
        'ED6_DT29/CH12364P._CP',             # 1C
        'ED6_DT29/CH12364P._CP',             # 1D
        'ED6_DT29/CH12030P._CP',             # 1E
        'ED6_DT29/CH12031P._CP',             # 1F
        'ED6_DT29/CH12032P._CP',             # 20
        'ED6_DT29/CH12033P._CP',             # 21
        'ED6_DT29/CH12034P._CP',             # 22
        'ED6_DT29/CH12364P._CP',             # 23
        'ED6_DT29/CH12364P._CP',             # 24
        'ED6_DT29/CH12364P._CP',             # 25
        'ED6_DT29/CH12364P._CP',             # 26
        'ED6_DT29/CH12364P._CP',             # 27
        'ED6_DT29/CH12040P._CP',             # 28
        'ED6_DT29/CH12041P._CP',             # 29
        'ED6_DT29/CH12042P._CP',             # 2A
        'ED6_DT29/CH12043P._CP',             # 2B
        'ED6_DT29/CH12044P._CP',             # 2C
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 7,
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
        "Function_5_5E1",          # 05, 5
        "Function_6_AF5",          # 06, 6
        "Function_7_1003",         # 07, 7
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

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
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
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_5D0 end

    def Function_5_5E1(): pass

    label("Function_5_5E1")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        (
            "#1Sあいうえお　#2Sあいうえお\x01",
            "#3Sあいうえお　#4Sあいうえお　#5Sあいうえお\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "#1Sかきくけこ　#2Sかきくけこ\x01",
            "#3Sかきくけこ　#4Sかきくけこ　#5Sかきくけこ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "#1Sさしすせそ　#2Sさしすせそ\x01",
            "#3Sさしすせそ　#4Sさしすせそ　#5Sさしすせそ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "#1Sたちつてと　#2Sたちつてと\x01",
            "#3Sたちつてと　#4Sたちつてと　#5Sたちつてと\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "#1Sなにぬねの　#2Sなにぬねの\x01",
            "#3Sなにぬねの　#4Sなにぬねの　#5Sなにぬねの\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "#1Sはひふへほ　#2Sはひふへほ\x01",
            "#3Sはひふへほ　#4Sはひふへほ　#5Sはひふへほ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "#1Sまみむめも　#2Sまみむめも\x01",
            "#3Sまみむめも　#4Sまみむめも　#5Sまみむめも\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "#1Sやゆよ　#2Sやゆよ\x01",
            "#3Sやゆよ　#4Sやゆよ　#5Sやゆよ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "#1Sらりるれろ　#2Sらりるれろ\x01",
            "#3Sらりるれろ　#4Sらりるれろ　#5Sらりるれろ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "#1Sわをん　#2Sわをん\x01",
            "#3Sわをん　#4Sわをん　#5Sわをん\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "#1Sがぎぐげご　#2Sがぎぐげご\x01",
            "#3Sがぎぐげご　#4Sがぎぐげご　#5Sがぎぐげご\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "#1Sざじずぜぞ　#2Sざじずぜぞ\x01",
            "#3Sざじずぜぞ　#4Sざじずぜぞ　#5Sざじずぜぞ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "#1Sだぢづでど　#2Sだぢづでど\x01",
            "#3Sだぢづでど　#4Sだぢづでど　#5Sだぢづでど\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "#1Sばびぶべぼ　#2Sばびぶべぼ\x01",
            "#3Sばびぶべぼ　#4Sばびぶべぼ　#5Sばびぶべぼ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "#1Sぱぴぷぺぽ　#2Sぱぴぷぺぽ\x01",
            "#3Sぱぴぷぺぽ　#4Sぱぴぷぺぽ　#5Sぱぴぷぺぽ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "#1Sぁぃぅぇぉ　#2Sぁぃぅぇぉ\x01",
            "#3Sぁぃぅぇぉ　#4Sぁぃぅぇぉ　#5Sぁぃぅぇぉ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "#1Sゃゅょっ　#2Sゃゅょっ\x01",
            "#3Sゃゅょっ　#4Sゃゅょっ　#5Sゃゅょっ\x01\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_5E1 end

    def Function_6_AF5(): pass

    label("Function_6_AF5")

    TalkBegin(0xFE)

    ChrTalk(    #18
        0xFE,
        (
            "#1Sアイウエオ　#2Sアイウエオ\x01",
            "#3Sアイウエオ　#4Sアイウエオ　#5Sアイウエオ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "#1Sカキクケコ　#2Sカキクケコ\x01",
            "#3Sカキクケコ　#4Sカキクケコ　#5Sカキクケコ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "#1Sサシスセソ　#2Sサシスセソ\x01",
            "#3Sサシスセソ　#4Sサシスセソ　#5Sサシスセソ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "#1Sタチツテト　#2Sタチツテト\x01",
            "#3Sタチツテト　#4Sタチツテト　#5Sタチツテト\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "#1Sナニヌネノ　#2Sナニヌネノ\x01",
            "#3Sナニヌネノ　#4Sナニヌネノ　#5Sナニヌネノ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "#1Sハヒフヘホ　#2Sハヒフヘホ\x01",
            "#3Sハヒフヘホ　#4Sハヒフヘホ　#5Sハヒフヘホ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "#1Sマミムメモ#2Sマミムメモ\x01",
            "#3Sマミムメモ#4Sマミムメモ#5Sマミムメモ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "#1Sヤユヨ　#2Sヤユヨ\x01",
            "#3Sヤユヨ　#4Sヤユヨ　#5Sヤユヨ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "#1Sラリルレロ　#2Sラリルレロ\x01",
            "#3Sラリルレロ　#4Sラリルレロ　#5Sラリルレロ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "#1Sワオン　#2Sワオン\x01",
            "#3Sワオン　#4Sワオン　#5Sワオン\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "#1Sガギグゲゴ　#2Sガギグゲゴ\x01",
            "#3Sガギグゲゴ　#4Sガギグゲゴ　#5Sガギグゲゴ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "#1Sザジズゼゾ　#2Sザジズゼゾ\x01",
            "#3Sザジズゼゾ　#4Sザジズゼゾ　#5Sザジズゼゾ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "#1Sダヂヅデド　#2Sダヂヅデド\x01",
            "#3Sダヂヅデド　#4Sダヂヅデド　#5Sダヂヅデド\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "#1Sバビブベボ　#2Sバビブベボ\x01",
            "#3Sバビブベボ　#4Sバビブベボ　#5Sバビブベボ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "#1Sパピプペポ　#2Sパピプペポ\x01",
            "#3Sパピプペポ　#4Sパピプペポ　#5Sパピプペポ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "#1Sァィゥェォ　#2Sァィゥェォ\x01",
            "#3Sァィゥェォ　#4Sァィゥェォ　#5Sァィゥェォ\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "#1Sャュョッ　#2Sャュョッ\x01",
            "#3Sャュョッ　#4Sャュョッ　#5Sャュョッ\x01\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_AF5 end

    def Function_7_1003(): pass

    label("Function_7_1003")

    TalkBegin(0xFE)

    ChrTalk(    #35
        0xFE,
        "#5S要恢复原状就指定默认坐标。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "#5S吉米好帅～～！　我爱你～～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "#5S说什么傻话！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "#5S就这样冲进浮游都市！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "#2S只有枪杆值得信赖。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1003 end

    SaveToFile()

Try(main)
