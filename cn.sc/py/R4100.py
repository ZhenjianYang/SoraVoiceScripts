from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4100.x',
        MapIndex            = 1,
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '管家菲利普',                           # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '红色的飞艇影子',                       # 12
        '红色的飞艇影子',                       # 13
        '红色的飞艇影子',                       # 14
        '圣海姆门方向',                         # 15
        '艾尔贝周游道方向',                     # 16
        '王都格兰赛尔方向',                     # 17
        '炽炎草',                               # 18
        '炽炎草',                               # 19
        '地狱火爆麻雀',                         # 20
        '地狱火爆麻雀',                         # 21
        '沼泽剑齿吸血魔',                       # 22
        '沼泽剑齿吸血魔',                       # 23
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
        'ED6_DT09/CH10780 ._CH',             # 00
        'ED6_DT09/CH10781 ._CH',             # 01
        'ED6_DT09/CH10790 ._CH',             # 02
        'ED6_DT09/CH10791 ._CH',             # 03
        'ED6_DT09/CH10050 ._CH',             # 04
        'ED6_DT09/CH10051 ._CH',             # 05
        'ED6_DT09/CH10800 ._CH',             # 06
        'ED6_DT09/CH10801 ._CH',             # 07
        'ED6_DT09/CH10810 ._CH',             # 08
        'ED6_DT09/CH10811 ._CH',             # 09
        'ED6_DT09/CH10820 ._CH',             # 0A
        'ED6_DT09/CH10821 ._CH',             # 0B
        'ED6_DT09/CH11220 ._CH',             # 0C
        'ED6_DT09/CH11221 ._CH',             # 0D
        'ED6_DT09/CH11230 ._CH',             # 0E
        'ED6_DT09/CH11231 ._CH',             # 0F
        'ED6_DT07/CH02470 ._CH',             # 10
        'ED6_DT07/CH01600 ._CH',             # 11
        'ED6_DT07/CH01640 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT09/CH10780P._CP',             # 00
        'ED6_DT09/CH10781P._CP',             # 01
        'ED6_DT09/CH10790P._CP',             # 02
        'ED6_DT09/CH10791P._CP',             # 03
        'ED6_DT09/CH10050P._CP',             # 04
        'ED6_DT09/CH10051P._CP',             # 05
        'ED6_DT09/CH10800P._CP',             # 06
        'ED6_DT09/CH10801P._CP',             # 07
        'ED6_DT09/CH10810P._CP',             # 08
        'ED6_DT09/CH10811P._CP',             # 09
        'ED6_DT09/CH10820P._CP',             # 0A
        'ED6_DT09/CH10821P._CP',             # 0B
        'ED6_DT09/CH11220P._CP',             # 0C
        'ED6_DT09/CH11221P._CP',             # 0D
        'ED6_DT09/CH11230P._CP',             # 0E
        'ED6_DT09/CH11231P._CP',             # 0F
        'ED6_DT07/CH02470P._CP',             # 10
        'ED6_DT07/CH01600P._CP',             # 11
        'ED6_DT07/CH01640P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 124800,
        Z                   = -2000,
        Y                   = 6110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 124800,
        Z                   = -2000,
        Y                   = 3950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        X                   = -41770,
        Z                   = 0,
        Y                   = -5530,
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
        X                   = 137370,
        Z                   = -2050,
        Y                   = 5100,
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
        X                   = -16930,
        Z                   = 0,
        Y                   = 111160,
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
        X                   = 13640,
        Z                   = -40,
        Y                   = -2250,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x296,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16650,
        Z                   = 300,
        Y                   = 2360,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x296,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15450,
        Z                   = -30,
        Y                   = 56010,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13350,
        Z                   = 110,
        Y                   = 68880,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60840,
        Z                   = 10,
        Y                   = 16239,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105890,
        Z                   = -1980,
        Y                   = 18620,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 93600,
        Y                   = -6000,
        Z                   = 5400,
        Range               = 97500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x62D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 14000,
        Y                   = -2000,
        Z                   = 30430,
        Range               = 37950,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x5F0A,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -31650,
        Y                   = -100,
        Z                   = -14830,
        Range               = -30070,
        Unknown_10          = 0x6B8,
        Unknown_14          = 0xB86,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 126430,
        Y                   = -2000,
        Z                   = 11520,
        Range               = 127710,
        Unknown_10          = 0xFFFFFCAE,
        Unknown_14          = 0xFFFFFCC2,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = 31170,
        TriggerZ            = 0,
        TriggerY            = 32450,
        TriggerRange        = 1500,
        ActorX              = 31170,
        ActorZ              = 1700,
        ActorY              = 32450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29270,
        TriggerZ            = 0,
        TriggerY            = 21060,
        TriggerRange        = 1500,
        ActorX              = 29270,
        ActorZ              = 1800,
        ActorY              = 21060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34440,
        TriggerZ            = 0,
        TriggerY            = 31310,
        TriggerRange        = 1500,
        ActorX              = 34440,
        ActorZ              = 1700,
        ActorY              = 31310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F6",          # 00, 0
        "Function_1_429",          # 01, 1
        "Function_2_4AB",          # 02, 2
        "Function_3_579",          # 03, 3
        "Function_4_5D5",          # 04, 4
        "Function_5_639",          # 05, 5
        "Function_6_11B3",         # 06, 6
        "Function_7_17F8",         # 07, 7
        "Function_8_1885",         # 08, 8
        "Function_9_1B9F",         # 09, 9
        "Function_10_1C33",        # 0A, 10
        "Function_11_1CCC",        # 0B, 11
        "Function_12_1D4D",        # 0C, 12
        "Function_13_1DA6",        # 0D, 13
        "Function_14_2138",        # 0E, 14
        "Function_15_2482",        # 0F, 15
        "Function_16_24D3",        # 10, 16
        "Function_17_2512",        # 11, 17
    )


    def Function_0_3F6(): pass

    label("Function_0_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_428")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_428")

    Return()

    # Function_0_3F6 end

    def Function_1_429(): pass

    label("Function_1_429")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE90D0, 0x23003B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_47A")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_492")
    OP_B1("R4100_y")
    Jump("loc_4AA")

    label("loc_492")

    OP_B1("R4100_n")
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)

    label("loc_4AA")

    Return()

    # Function_1_429 end

    def Function_2_4AB(): pass

    label("Function_2_4AB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_563")

    label("loc_4D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_563")

    label("loc_4E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_502")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_563")

    label("loc_502")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_563")

    label("loc_51B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_534")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_563")

    label("loc_534")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_563")

    label("loc_54D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_563")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_563")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_578")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_563")

    label("loc_578")

    Return()

    # Function_2_4AB end

    def Function_3_579(): pass

    label("Function_3_579")

    TalkBegin(0x9)

    ChrTalk(    #0
        0xFE,
        (
            "因为紧急情况的缘故，\x01",
            "整个艾尔贝周游道地区都被封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "抱歉，你们不能过去。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_3_579 end

    def Function_4_5D5(): pass

    label("Function_4_5D5")

    TalkBegin(0xA)

    ChrTalk(    #2
        0xFE,
        (
            "袭击艾尔贝离宫的\x01",
            "武装集团似乎潜伏在\x01",
            "周游道附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "现在正在开展封锁作战\x01",
            "来追击他们。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_5D5 end

    def Function_5_639(): pass

    label("Function_5_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_646")
    Return()

    label("loc_646")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    Call(0, 10)
    Call(0, 11)
    AddParty(0x2E, 0xFF, 0xFF)
    FadeToBright(0, 0)

    label("loc_66A")

    SetChrPos(0x8, 77770, 0, 14150, 90)

    NpcTalk(    #4
        0x8,
        "男性的声音",
        "哎呀，你们是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(94100, -2000, 12960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 95390, -2000, 11850, 270)
    SetChrPos(0x8, 86980, -250, 13060, 90)
    SetChrPos(0x12F, 97900, -2000, 12150, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C8")
    SetChrPos(0x105, 95530, -2000, 12900, 270)
    SetChrPos(0xF7, 96600, -2000, 12700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_784")
    SetChrPos(0x104, 96820, -2000, 11620, 270)
    Jump("loc_7C5")

    label("loc_784")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A6")
    SetChrPos(0x107, 96820, -2000, 11620, 270)
    Jump("loc_7C5")

    label("loc_7A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C5")
    SetChrPos(0x108, 96820, -2000, 11620, 270)

    label("loc_7C5")

    Jump("loc_7FB")

    label("loc_7C8")

    SetChrPos(0xF7, 95530, -2000, 12900, 270)
    SetChrPos(0xF8, 96670, -2000, 12700, 270)
    SetChrPos(0xF9, 96820, -2000, 11620, 270)

    label("loc_7FB")

    OP_8E(0x8, 0x16CCE, 0xFFFFF830, 0x311A, 0x7D0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABC")

    ChrTalk(    #5
        0x101,
        "#1004F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#044F#2P啊……\x01",
            "菲利普先生。\x02\x03",

            "#040F好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#720F#5P好久不见。\x01",
            "科洛蒂娅殿下、艾丝蒂尔小姐。\x02\x03",

            "你们几位去过艾尔贝离宫了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1006F嗯，是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#542F#2P菲利普先生\x01",
            "到王都去有事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#720F#5P是的，公爵阁下\x01",
            "吩咐我出来买东西。\x02\x03",

            "#721F……莫非你们\x01",
            "在离宫已经遇见殿下了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1016F嗯、嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#045F#2P我们和久违多时的他\x01",
            "稍微寒暄了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#722F#5P……看来\x01",
            "他又得罪了你们吧。\x02\x03",

            "实在是对不起。\x01",
            "我以臣下的身份向各位道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#047F#2P呵呵，您太客气了。\x02\x03",

            "#040F我听说叔叔他被软禁，\x01",
            "所以感到有点担心……\x02\x03",

            "不过他看起来很有精神，我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#720F#5P您能够这么说，我真是高兴。\x02\x03",

            "那么我就先告辞了……\x01",
            "各位，失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB8")

    label("loc_ABC")


    ChrTalk(    #16
        0x101,
        (
            "#1004F咦……\x01",
            "这不是菲利普先生吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#720F#5P艾丝蒂尔小姐。\x01",
            "好久不见。\x02\x03",

            "你们几位去过艾尔贝离宫了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1006F嗯，是的……\x02\x03",

            "菲利普先生\x01",
            "来王都办事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#720F#5P是的，公爵阁下\x01",
            "吩咐我出来买东西。\x02\x03",

            "#721F……莫非你们\x01",
            "在离宫已经遇见殿下了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1025F嗯、嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#722F#5P……看来他又无心\x01",
            "得罪了你们吧。\x02\x03",

            "实在是对不起。\x01",
            "我以臣下的身份向各位道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016F也不是，他倒没\x01",
            "说过什么失礼的话。\x02\x03",

            "#1006F我并不介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#720F#5P您能够这么说，我真是高兴。\x02\x03",

            "那么我就先告辞了……\x01",
            "各位，失陪了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB8")


    def lambda_CBE():
        OP_8E(0xFE, 0x1737C, 0xFFFFF830, 0x2A12, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CBE)

    def lambda_CD9():

        label("loc_CD9")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_CD9")

    QueueWorkItem2(0x101, 1, lambda_CD9)

    def lambda_CEA():

        label("loc_CEA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_CEA")

    QueueWorkItem2(0x12F, 1, lambda_CEA)

    def lambda_CFB():

        label("loc_CFB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_CFB")

    QueueWorkItem2(0xF7, 1, lambda_CFB)

    def lambda_D0C():

        label("loc_D0C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_D0C")

    QueueWorkItem2(0xF8, 1, lambda_D0C)

    def lambda_D1D():

        label("loc_D1D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_D1D")

    QueueWorkItem2(0xF9, 1, lambda_D1D)
    WaitChrThread(0x8, 0x1)

    def lambda_D33():
        OP_8E(0xFE, 0x1A626, 0xFFFFF830, 0x2148, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D33)

    def lambda_D4E():
        OP_6D(99610, -2000, 11170, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D4E)

    def lambda_D66():
        OP_67(0, 8680, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D66)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)

    def lambda_D88():
        OP_6D(96350, -2000, 12530, 1600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D88)

    def lambda_DA0():
        OP_67(0, 8680, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DA0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0x12F, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #24
        0x101,
        (
            "#1007F呼～他还是\x01",
            "那么辛苦。\x02\x03",

            "#1015F他好像从公爵小时候起\x01",
            "就一直负责照顾公爵的起居……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECD")
    OP_8C(0x105, 180, 400)

    ChrTalk(    #25
        0x105,
        (
            "#040F#2P好像已经照顾了\x01",
            "20年以上了。\x02\x03",

            "据说在那之前\x01",
            "他是在亲卫队工作的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 360, 400)

    ChrTalk(    #26
        0x101,
        (
            "#1004F咦，真的吗！？\x02\x03",

            "#1006F唔～果然是\x01",
            "人不可貌相呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECD")


    ChrTalk(    #27
        0x12F,
        (
            "#264F#7P…………………………\x02\x03",

            "#263F刚才那爷爷……\x01",
            "绝不是简单的人物。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F1D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F1D)
    Sleep(50)

    def lambda_F30():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_F30)
    Sleep(50)

    def lambda_F43():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_F43)
    Sleep(50)

    def lambda_F56():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F56)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9A")

    ChrTalk(    #28
        0x101,
        "#1004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        "#064F怎么了？小玲？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FBE")

    label("loc_F9A")


    ChrTalk(    #30
        0x101,
        (
            "#1004F啊……\x02\x03",

            "怎么突然这么说？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBE")

    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #31
        0x12F,
        (
            "#260F因为，他可以\x01",
            "闭着眼睛走路嘛。\x02\x03",

            "玲就绝对做不到。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1054")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1092")

    label("loc_1054")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107B")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1092")

    label("loc_107B")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1092")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B9")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10F7")

    label("loc_10B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E0")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10F7")

    label("loc_10E0")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_10F7")

    Sleep(1500)

    ChrTalk(    #32
        0x101,
        (
            "#1016F唔，我想\x01",
            "那不是闭着眼睛，\x01",
            "应该是眯着眼睛……\x02\x03",

            "#1006F而且他吃惊的时候，\x01",
            "眼睛还是会睁得大大的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x12F,
        (
            "#264F哎呀？是吗？\x02\x03",

            "#261F呵呵，我也好想\x01",
            "看看他吃惊的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A2(0x1618)
    EventEnd(0x0)
    Return()

    # Function_5_639 end

    def Function_6_11B3(): pass

    label("Function_6_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11CA")
    Return()

    label("loc_11CA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11EA")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_11EA")

    OP_20(0x7D0)
    Fade(1000)
    SetChrPos(0x101, 26220, 0, 27190, 0)
    SetChrPos(0x102, 27510, 0, 27180, 0)
    SetChrPos(0xF8, 26280, 0, 25750, 0)
    SetChrPos(0xF9, 27640, 0, 25770, 0)
    OP_6D(27520, 0, 25330, 0)
    OP_67(0, 7360, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(147000, 0)
    OP_6E(349, 0)
    OP_0D()
    OP_43(0x101, 0x3, 0x0, 0x7)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CD")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1301")

    label("loc_12CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1301")

    label("loc_12EF")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1301")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1323")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1357")

    label("loc_1323")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1345")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1357")

    label("loc_1345")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1357")

    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#1004F#6P咦……这是？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #35
        0x106,
        (
            "#052F#2P什么啊，这不是\x01",
            "飞船的引擎声吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_13B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F7")

    ChrTalk(    #36
        0x103,
        (
            "#023F#2P什么啊，这不是\x01",
            "飞船的引擎声吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_13F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142E")

    ChrTalk(    #37
        0x108,
        (
            "#073F#2P这是……\x01",
            "飞船的引擎声吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142E")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147E")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_14B2")

    label("loc_147E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A0")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_14B2")

    label("loc_14A0")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_14B2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_150D")

    label("loc_14D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FB")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_150D")

    label("loc_14FB")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_150D")

    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0xF8)
    OP_63(0xF9)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1582")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15C0")

    label("loc_1582")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A9")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15C0")

    label("loc_15A9")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15C0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EC")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_162A")

    label("loc_15EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1613")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_162A")

    label("loc_1613")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_162A")

    Sleep(1000)

    ChrTalk(    #38
        0x101,
        "#1020F#6P等、等等！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168A")

    ChrTalk(    #39
        0x107,
        (
            "#065F#2P这、这种时候\x01",
            "飞船怎么还能飞……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1701")

    label("loc_168A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C6")

    ChrTalk(    #40
        0x108,
        (
            "#076F#2P这种时候\x01",
            "飞船怎么还能飞……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1701")

    label("loc_16C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1701")

    ChrTalk(    #41
        0x103,
        (
            "#024F#2P这种时候\x01",
            "飞船怎么还可以飞……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1701")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 135, 500)

    ChrTalk(    #42
        0x102,
        "#1046F#6P在那里……！\x02",
    )

    CloseMessageWindow()

    def lambda_1745():
        OP_6D(35140, 0, 17330, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1745)

    def lambda_175D():
        OP_67(0, 11840, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_175D)

    def lambda_1775():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1775)

    def lambda_1785():
        OP_6C(111000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1785)

    def lambda_1795():
        OP_6E(427, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1795)

    def lambda_17A5():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A5)
    Sleep(50)

    def lambda_17B8():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_17B8)
    Sleep(50)

    def lambda_17CB():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_17CB)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_11B3 end

    def Function_7_17F8(): pass

    label("Function_7_17F8")

    OP_22(0x79, 0x1, 0x32)
    Sleep(200)
    OP_24(0x79, 0x35)
    Sleep(200)
    OP_24(0x79, 0x38)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x3F)
    Sleep(200)
    OP_24(0x79, 0x42)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x49)
    Sleep(200)
    OP_24(0x79, 0x4C)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x53)
    Sleep(200)
    OP_24(0x79, 0x56)
    Sleep(200)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x5D)
    Sleep(200)
    OP_24(0x79, 0x60)
    Sleep(200)
    OP_24(0x79, 0x64)
    Return()

    # Function_7_17F8 end

    def Function_8_1885(): pass

    label("Function_8_1885")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18AA")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_18AA")

    OP_22(0x79, 0x1, 0x64)
    SetChrPos(0x101, 26590, 0, 26840, 135)
    SetChrPos(0x102, 28060, 0, 26570, 135)
    SetChrPos(0xF8, 26420, 0, 24940, 135)
    SetChrPos(0xF9, 27850, 0, 24990, 135)
    OP_6D(27140, 0, 26500, 0)
    OP_67(0, 8210, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_A1(0xB, 0x0)
    OP_A1(0xC, 0x1)
    OP_A1(0xD, 0x2)
    SetChrPos(0xB, 43360, 2000, 11200, 315)
    SetChrPos(0xC, 48360, 2000, 16200, 315)
    SetChrPos(0xD, 38360, 2000, 6200, 315)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1991():
        OP_90(0xFE, 0xFFFF63C0, 0x0, 0x9C40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1991)
    Sleep(800)

    def lambda_19B1():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19B1)
    Sleep(50)

    def lambda_19C4():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_19C4)
    Sleep(60)

    def lambda_19D7():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_19D7)
    Sleep(50)

    def lambda_19EA():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_19EA)

    def lambda_19F8():
        OP_90(0xFE, 0xFFFF63C0, 0x0, 0x9C40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19F8)
    Sleep(1000)

    def lambda_1A18():
        OP_90(0xFE, 0xFFFF63C0, 0x0, 0x9C40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A18)
    WaitChrThread(0xD, 0x1)
    OP_43(0x102, 0x2, 0x0, 0x9)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)

    ChrTalk(    #43
        0x101,
        (
            "#1020F#6P『结社』的飞艇……\x01",
            "为、为什么会在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1046F#4P不好……\x01",
            "那是王都的方向！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(    #45
        0x106,
        (
            "#057F#6P这可不是闹着玩的！\x01",
            "我们赶快追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B52")

    label("loc_1AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B28")

    ChrTalk(    #46
        0x103,
        (
            "#022F#6P这……\x01",
            "看来动作必须快一点了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B52")

    label("loc_1B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B52")

    ChrTalk(    #47
        0x108,
        "#076F#6P赶快追上去吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1B52")

    OP_A2(0x2038)
    OP_28(0x9C, 0x4, 0x2)
    OP_28(0x9C, 0x4, 0x8)
    OP_28(0x9C, 0x1, 0x1)
    OP_28(0xB5, 0x4, 0x40)
    OP_28(0xB6, 0x4, 0x40)
    OP_28(0xB7, 0x4, 0x40)
    OP_28(0xB8, 0x4, 0x40)
    OP_28(0xB9, 0x4, 0x40)
    OP_28(0xBA, 0x4, 0x40)
    OP_28(0xBB, 0x4, 0x40)
    OP_28(0xBC, 0x4, 0x40)
    OP_28(0xBD, 0x4, 0x40)
    OP_28(0xBE, 0x4, 0x40)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_8_1885 end

    def Function_9_1B9F(): pass

    label("Function_9_1B9F")

    OP_24(0x79, 0x5F)
    Sleep(300)
    OP_24(0x79, 0x5A)
    Sleep(300)
    OP_24(0x79, 0x55)
    Sleep(300)
    OP_24(0x79, 0x50)
    Sleep(300)
    OP_24(0x79, 0x4B)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x41)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x37)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x2D)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x23)
    Sleep(300)
    OP_24(0x79, 0x1E)
    Sleep(300)
    OP_24(0x79, 0x19)
    Sleep(300)
    OP_24(0x79, 0x14)
    Sleep(300)
    OP_23(0x79)
    Return()

    # Function_9_1B9F end

    def Function_10_1C33(): pass

    label("Function_10_1C33")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CAD"),
        (1, "loc_1CB3"),
        (SWITCH_DEFAULT, "loc_1CB9"),
    )


    label("loc_1CAD")

    OP_A2(0x1200)
    Jump("loc_1CB9")

    label("loc_1CB3")

    OP_A2(0x1201)
    Jump("loc_1CB9")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1CC7")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1CCB")

    label("loc_1CC7")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1CCB")

    Return()

    # Function_10_1C33 end

    def Function_11_1CCC(): pass

    label("Function_11_1CCC")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1D0F")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_1D2D")

    label("loc_1D0F")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_1D2D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_11_1CCC end

    def Function_12_1D4D(): pass

    label("Function_12_1D4D")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_12_1D4D end

    def Function_13_1DA6(): pass

    label("Function_13_1DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E58")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E00")

    ChrTalk(    #48
        0x101,
        (
            "#1002F现在不是到处闲逛的时候。\x01",
            "……要赶快返回协会才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3D")

    label("loc_1E00")


    ChrTalk(    #49
        0x109,
        (
            "#1063F现在不是到处闲逛的时候。\x01",
            "……赶紧去王都的协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3D")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_1FD6")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1E81"),
        (1, "loc_1EB5"),
        (2, "loc_1EE9"),
        (5, "loc_1F1C"),
        (7, "loc_1F4F"),
        (6, "loc_1F84"),
        (SWITCH_DEFAULT, "loc_1FB3"),
    )


    label("loc_1E81")


    ChrTalk(    #50
        0x101,
        (
            "#1002F没时间去别的地方了。\x01",
            "快点前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB3")

    label("loc_1EB5")


    ChrTalk(    #51
        0x102,
        (
            "#1042F没时间去别处了。\x01",
            "要尽快前往王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB3")

    label("loc_1EE9")


    ChrTalk(    #52
        0x103,
        (
            "#022F没时间去别的地方了。\x01",
            "赶紧前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB3")

    label("loc_1F1C")


    ChrTalk(    #53
        0x106,
        (
            "#057F没时间去别的地方了。\x01",
            "赶紧前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB3")

    label("loc_1F4F")


    ChrTalk(    #54
        0x108,
        (
            "#072F没时间去别的地方了啊。\x01",
            "赶紧前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB3")

    label("loc_1F84")


    ChrTalk(    #55
        0x107,
        (
            "#062F没时间去别处了。\x01",
            "必须赶紧去王都！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB3")

    label("loc_1FB3")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2137")

    label("loc_1FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_2137")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1FFF"),
        (1, "loc_202F"),
        (2, "loc_205F"),
        (5, "loc_208C"),
        (7, "loc_20B9"),
        (6, "loc_20E0"),
        (SWITCH_DEFAULT, "loc_2117"),
    )


    label("loc_1FFF")


    ChrTalk(    #56
        0x101,
        (
            "#1002F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2117")

    label("loc_202F")


    ChrTalk(    #57
        0x102,
        (
            "#1042F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2117")

    label("loc_205F")


    ChrTalk(    #58
        0x103,
        (
            "#022F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2117")

    label("loc_208C")


    ChrTalk(    #59
        0x106,
        (
            "#057F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2117")

    label("loc_20B9")


    ChrTalk(    #60
        0x108,
        (
            "#072F不是这边。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2117")

    label("loc_20E0")


    ChrTalk(    #61
        0x107,
        (
            "#065F那个那个……不是这边。\x01",
            "要赶紧去王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2117")

    label("loc_2117")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2137")

    Return()

    # Function_13_1DA6 end

    def Function_14_2138(): pass

    label("Function_14_2138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_22DD")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2161"),
        (1, "loc_218F"),
        (2, "loc_21BD"),
        (5, "loc_21EA"),
        (7, "loc_2217"),
        (6, "loc_2244"),
        (SWITCH_DEFAULT, "loc_2275"),
    )


    label("loc_2161")


    ChrTalk(    #62
        0x101,
        (
            "#1002F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2275")

    label("loc_218F")


    ChrTalk(    #63
        0x102,
        (
            "#1042F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2275")

    label("loc_21BD")


    ChrTalk(    #64
        0x103,
        (
            "#022F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2275")

    label("loc_21EA")


    ChrTalk(    #65
        0x106,
        (
            "#057F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2275")

    label("loc_2217")


    ChrTalk(    #66
        0x108,
        (
            "#072F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2275")

    label("loc_2244")


    ChrTalk(    #67
        0x107,
        (
            "#062F没时间去别处了。\x01",
            "要赶紧去王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2275")

    label("loc_2275")

    OP_59()
    Fade(1000)
    SetChrPos(0x0, 123990, -2000, 5010, 275)
    SetChrPos(0x1, 123990, -2000, 5010, 275)
    SetChrPos(0x2, 123990, -2000, 5010, 275)
    SetChrPos(0x3, 123990, -2000, 5010, 275)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 275, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2481")

    label("loc_22DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_2481")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2306"),
        (1, "loc_2336"),
        (2, "loc_2364"),
        (5, "loc_2391"),
        (7, "loc_23BE"),
        (6, "loc_23E5"),
        (SWITCH_DEFAULT, "loc_241C"),
    )


    label("loc_2306")


    ChrTalk(    #68
        0x101,
        (
            "#1002F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2336")


    ChrTalk(    #69
        0x102,
        (
            "#1042F不，不是这边！\x01",
            "……赶紧去王都！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2364")


    ChrTalk(    #70
        0x103,
        (
            "#022F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2391")


    ChrTalk(    #71
        0x106,
        (
            "#057F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_23BE")


    ChrTalk(    #72
        0x108,
        (
            "#072F不是这边。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_23E5")


    ChrTalk(    #73
        0x107,
        (
            "#065F那个那个……不是这边。\x01",
            "要赶紧去王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_241C")

    OP_59()
    Fade(1000)
    SetChrPos(0x0, 123990, -2000, 5010, 275)
    SetChrPos(0x1, 123990, -2000, 5010, 275)
    SetChrPos(0x2, 123990, -2000, 5010, 275)
    SetChrPos(0x3, 123990, -2000, 5010, 275)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 275, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2481")

    Return()

    # Function_14_2138 end

    def Function_15_2482(): pass

    label("Function_15_2482")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #74
        "\x07\x05北　王都格兰赛尔　１７９塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_2482 end

    def Function_16_24D3(): pass

    label("Function_16_24D3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #75
        "\x07\x05南　圣海姆门\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_24D3 end

    def Function_17_2512(): pass

    label("Function_17_2512")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #76
        "\x07\x05东　艾尔贝离宫　　２２４塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_2512 end

    SaveToFile()

Try(main)
