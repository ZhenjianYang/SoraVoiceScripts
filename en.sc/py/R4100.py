from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Butler Phillip',                       # 9
        'Royal Army Soldier',                   # 10
        'Royal Army Soldier',                   # 11
        '紅い飛行艇影',                         # 12
        '紅い飛行艇影',                         # 13
        '紅い飛行艇影',                         # 14
        'Sanktheim Gate',                       # 15
        'Erbe Scenic Route',                    # 16
        'Grancel',                              # 17
        'フレイムプラント',                     # 18
        'フレイムプラント',                     # 19
        'ヘルマーズ',                           # 20
        'ヘルマーズ',                           # 21
        '沼チュパカブラ',                       # 22
        '沼チュパカブラ',                       # 23
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
        "Function_4_60E",          # 04, 4
        "Function_5_6E7",          # 05, 5
        "Function_6_1682",         # 06, 6
        "Function_7_1D1C",         # 07, 7
        "Function_8_1DA9",         # 08, 8
        "Function_9_20E3",         # 09, 9
        "Function_10_2177",        # 0A, 10
        "Function_11_220F",        # 0B, 11
        "Function_12_2290",        # 0C, 12
        "Function_13_22E9",        # 0D, 13
        "Function_14_2828",        # 0E, 14
        "Function_15_2D1E",        # 0F, 15
        "Function_16_2D6B",        # 10, 16
        "Function_17_2DB3",        # 11, 17
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
            "We've temporarily closed all roads\x01",
            "to the Erbe Scenic Route as a result\x01",
            "of an emergency situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Sorry, but I can't let you pass.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_3_579 end

    def Function_4_60E(): pass

    label("Function_4_60E")

    TalkBegin(0xA)

    ChrTalk(    #2
        0xFE,
        (
            "The armed group that attacked the\x01",
            "royal villa is apparently still hiding\x01",
            "somewhere along the scenic route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Currently, we're in pursuit and have\x01",
            "closed off all nearby areas to restrict\x01",
            "their movement.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_60E end

    def Function_5_6E7(): pass

    label("Function_5_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F4")
    Return()

    label("loc_6F4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    Call(0, 10)
    Call(0, 11)
    AddParty(0x2E, 0xFF, 0xFF)
    FadeToBright(0, 0)

    label("loc_718")

    SetChrPos(0x8, 77770, 0, 14150, 90)

    NpcTalk(    #4
        0x8,
        "Man's Voice",
        "Ah, yes, you are...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87A")
    SetChrPos(0x105, 95530, -2000, 12900, 270)
    SetChrPos(0xF7, 96600, -2000, 12700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_836")
    SetChrPos(0x104, 96820, -2000, 11620, 270)
    Jump("loc_877")

    label("loc_836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_858")
    SetChrPos(0x107, 96820, -2000, 11620, 270)
    Jump("loc_877")

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_877")
    SetChrPos(0x108, 96820, -2000, 11620, 270)

    label("loc_877")

    Jump("loc_8AD")

    label("loc_87A")

    SetChrPos(0xF7, 95530, -2000, 12900, 270)
    SetChrPos(0xF8, 96670, -2000, 12700, 270)
    SetChrPos(0xF9, 96820, -2000, 11620, 270)

    label("loc_8AD")

    OP_8E(0x8, 0x16CCE, 0xFFFFF830, 0x311A, 0x7D0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D09")

    ChrTalk(    #5
        0x101,
        "#1004F#2PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#044F#2POh, my. Phillip!\x02\x03",

            "#040FHow have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#720F#6PYour concern does me too much credit,\x01",
            "Your Highness. I hope you and Miss Estelle\x01",
            "are well.\x02\x03",

            "Have you been to the villa recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1006F#2PWe have, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#542F#2PYou were, um...'busy' in the capital,\x01",
            "I take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#720F#6PYes, I was making some purchases on\x01",
            "the orders of His Highness the Duke.\x02\x03",

            "#721F...Did you, perchance, encounter His\x01",
            "Highness while you were at the villa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1016F#2PWe 'encountered' him, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#045F#2PWe wanted to be nice and say hello.\x01",
            "It's been some time since the, um,\x01",
            "unpleasantness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#722F#6PFrom your expressions, I take it he\x01",
            "said something thoughtless to you\x01",
            "once again.\x02\x03",

            "As his retainer, you have my utmost\x01",
            "apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#047F#2POh, you don't need to apologize for\x01",
            "him, Phillip.\x02\x03",

            "#040FI have to admit, I was a little worried\x01",
            "when I'd heard he was placed under\x01",
            "house arrest.\x02\x03",

            "He's seems to be taking it well,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#720F#6PIt is kind of you to say so.\x02\x03",

            "Now, I fear I must be off. If you'll\x01",
            "pardon me, Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_D09")


    ChrTalk(    #16
        0x101,
        "#1004F#2PHuh...? Oh, hey. It's Phillip!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#720F#6PMiss Estelle. It has been some time\x01",
            "since we last met.\x02\x03",

            "Have you been to the villa recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1006F#2PWe have, actually.\x02\x03",

            "I guess you had to go to Grancel for\x01",
            "some reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#720F#6PYes, I was making some purchases on\x01",
            "the orders of His Highness the Duke.\x02\x03",

            "#721F...Did you, perchance, encounter His\x01",
            "Highness while you were at the villa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1025F#2PWe 'encountered' him, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#722F#6PFrom your expression, I take it he\x01",
            "said something thoughtless to you\x01",
            "once again.\x02\x03",

            "As his retainer, you have my utmost\x01",
            "apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016F#2PAh, no, he wasn't really rude to ME, \x01",
            "specifically.\x02\x03",

            "#1006FYou don't need to apologize.\x01",
            "I wasn't bothered one bit, I swear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#720F#6PYour kindness does you credit,\x01",
            "Miss Estelle.\x02\x03",

            "Now, I fear I must be off. If you'll\x01",
            "pardon me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104D")


    def lambda_1053():
        OP_8E(0xFE, 0x1737C, 0xFFFFF830, 0x2A12, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1053)

    def lambda_106E():

        label("loc_106E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_106E")

    QueueWorkItem2(0x101, 1, lambda_106E)

    def lambda_107F():

        label("loc_107F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_107F")

    QueueWorkItem2(0x12F, 1, lambda_107F)

    def lambda_1090():

        label("loc_1090")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1090")

    QueueWorkItem2(0xF7, 1, lambda_1090)

    def lambda_10A1():

        label("loc_10A1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10A1")

    QueueWorkItem2(0xF8, 1, lambda_10A1)

    def lambda_10B2():

        label("loc_10B2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10B2")

    QueueWorkItem2(0xF9, 1, lambda_10B2)
    WaitChrThread(0x8, 0x1)

    def lambda_10C8():
        OP_8E(0xFE, 0x1A626, 0xFFFFF830, 0x2148, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10C8)

    def lambda_10E3():
        OP_6D(99610, -2000, 11170, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10E3)

    def lambda_10FB():
        OP_67(0, 8680, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10FB)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)

    def lambda_111D():
        OP_6D(96350, -2000, 12530, 1600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_111D)

    def lambda_1135():
        OP_67(0, 8680, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1135)
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
            "#1007F*sigh* Guess Phillip's job is even\x01",
            "harder now.\x02\x03",

            "#1015FHe's been taking care of Dunan\x01",
            "since Dunan was young, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F3")
    OP_8C(0x105, 180, 400)

    ChrTalk(    #25
        0x105,
        (
            "#040F#4PHe's been Dunan's retainer for\x01",
            "the past twenty years, from what\x01",
            "Grandmother tells me.\x02\x03",

            "I believe he was a member of the\x01",
            "Royal Guard before then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 360, 400)

    ChrTalk(    #26
        0x101,
        (
            "#1004FWait, really? Phillip?!\x02\x03",

            "#1006FWow, guess you really can't\x01",
            "judge by looks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F3")


    ChrTalk(    #27
        0x12F,
        (
            "#264F#2P...Huh.\x02\x03",

            "#263FYou really shouldn't underestimate\x01",
            "him. Even I can tell he's not just any\x01",
            "old guy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1367():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1367)
    Sleep(50)

    def lambda_137A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_137A)
    Sleep(50)

    def lambda_138D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_138D)
    Sleep(50)

    def lambda_13A0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_13A0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EC")

    ChrTalk(    #28
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        "#064FWhat do you mean, Renne?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1416")

    label("loc_13EC")


    ChrTalk(    #30
        0x101,
        (
            "#1004FHuh?\x02\x03",

            "What do you mean, Renne?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1416")

    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #31
        0x12F,
        (
            "#260FOh, um, you know! Like how he\x01",
            "can walk with his eyes closed.\x02\x03",

            "I sure couldn't do that!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1511")

    label("loc_14D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FA")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1511")

    label("loc_14FA")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1538")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1576")

    label("loc_1538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155F")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1576")

    label("loc_155F")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1576")

    Sleep(1500)

    ChrTalk(    #32
        0x101,
        (
            "#1016FI think they're just narrowed, Renne,\x01",
            "not closed...\x02\x03",

            "#1006FI mean, you noticed how he opens\x01",
            "his eyes when surprised, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x12F,
        (
            "#264FReally? I didn't!\x02\x03",

            "#261FI wanna see, I wanna see!\x01",
            "Maybe I can get a good look if\x01",
            "I surprise him next time!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A2(0x1618)
    EventEnd(0x0)
    Return()

    # Function_5_6E7 end

    def Function_6_1682(): pass

    label("Function_6_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1699")
    Return()

    label("loc_1699")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B9")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_16B9")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179C")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_17D0")

    label("loc_179C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BE")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_17D0")

    label("loc_17BE")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_17D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F2")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1826")

    label("loc_17F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1814")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1826")

    label("loc_1814")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1826")

    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#1004F#5PHey, isn't that...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189F")

    ChrTalk(    #35
        0x106,
        (
            "#052F#4PWhat the...? That's the sound\x01",
            "of an airship engine!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1931")

    label("loc_189F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18ED")

    ChrTalk(    #36
        0x103,
        (
            "#023F#4PWhat...? That's the sound\x01",
            "of an airship engine!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1931")

    label("loc_18ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1931")

    ChrTalk(    #37
        0x108,
        (
            "#073F#4PThat's...the sound of\x01",
            "an airship engine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1931")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1981")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_19B5")

    label("loc_1981")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A3")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_19B5")

    label("loc_19A3")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_19B5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DC")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1A10")

    label("loc_19DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FE")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1A10")

    label("loc_19FE")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1A10")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A85")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1AC3")

    label("loc_1A85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AAC")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1AC3")

    label("loc_1AAC")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1AC3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AEF")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B2D")

    label("loc_1AEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B16")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B2D")

    label("loc_1B16")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B2D")

    Sleep(1000)

    ChrTalk(    #38
        0x101,
        "#1020F#5PW-Wait a second!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B97")

    ChrTalk(    #39
        0x107,
        "#065F#4PIf it's an airship that can fly NOW...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2B")

    label("loc_1B97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE0")

    ChrTalk(    #40
        0x108,
        (
            "#076F#4PThe only airships that\x01",
            "can fly now are...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C2B")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C2B")

    ChrTalk(    #41
        0x103,
        (
            "#024F#4POh, no! An airship that\x01",
            "can fly NOW would be...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2B")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 135, 500)

    ChrTalk(    #42
        0x102,
        "#1046F#5PThere!\x02",
    )

    CloseMessageWindow()

    def lambda_1C69():
        OP_6D(35140, 0, 17330, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C69)

    def lambda_1C81():
        OP_67(0, 11840, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C81)

    def lambda_1C99():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C99)

    def lambda_1CA9():
        OP_6C(111000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CA9)

    def lambda_1CB9():
        OP_6E(427, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1CB9)

    def lambda_1CC9():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CC9)
    Sleep(50)

    def lambda_1CDC():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1CDC)
    Sleep(50)

    def lambda_1CEF():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1CEF)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1682 end

    def Function_7_1D1C(): pass

    label("Function_7_1D1C")

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

    # Function_7_1D1C end

    def Function_8_1DA9(): pass

    label("Function_8_1DA9")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DCE")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_1DCE")

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

    def lambda_1EB5():
        OP_90(0xFE, 0xFFFF63C0, 0x0, 0x9C40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EB5)
    Sleep(800)

    def lambda_1ED5():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1ED5)
    Sleep(50)

    def lambda_1EE8():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1EE8)
    Sleep(60)

    def lambda_1EFB():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_1EFB)
    Sleep(50)

    def lambda_1F0E():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_1F0E)

    def lambda_1F1C():
        OP_90(0xFE, 0xFFFF63C0, 0x0, 0x9C40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1F1C)
    Sleep(1000)

    def lambda_1F3C():
        OP_90(0xFE, 0xFFFF63C0, 0x0, 0x9C40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1F3C)
    WaitChrThread(0xD, 0x1)
    OP_43(0x102, 0x2, 0x0, 0x9)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)

    ChrTalk(    #43
        0x101,
        (
            "#1020F#6PSociety airships!\x01",
            "Why are THEY here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1046F#4PDamn. They're heading straight\x01",
            "for the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2025")

    ChrTalk(    #45
        0x106,
        (
            "#057FSon of a bitch!\x01",
            "We need to chase them! NOW!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2096")

    label("loc_2025")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2067")

    ChrTalk(    #46
        0x103,
        (
            "#022FGoddess help us...\x01",
            "We MUST give chase!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2096")

    label("loc_2067")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2096")

    ChrTalk(    #47
        0x108,
        "#076FWe have to chase them!\x02",
    )

    CloseMessageWindow()

    label("loc_2096")

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

    # Function_8_1DA9 end

    def Function_9_20E3(): pass

    label("Function_9_20E3")

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

    # Function_9_20E3 end

    def Function_10_2177(): pass

    label("Function_10_2177")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21F0"),
        (1, "loc_21F6"),
        (SWITCH_DEFAULT, "loc_21FC"),
    )


    label("loc_21F0")

    OP_A2(0x1200)
    Jump("loc_21FC")

    label("loc_21F6")

    OP_A2(0x1201)
    Jump("loc_21FC")

    label("loc_21FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_220A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_220E")

    label("loc_220A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_220E")

    Return()

    # Function_10_2177 end

    def Function_11_220F(): pass

    label("Function_11_220F")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2252")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_2270")

    label("loc_2252")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_2270")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_11_220F end

    def Function_12_2290(): pass

    label("Function_12_2290")

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

    # Function_12_2290 end

    def Function_13_22E9(): pass

    label("Function_13_22E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23BC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2349")

    ChrTalk(    #48
        0x101,
        (
            "#1002FWe're wasting time...\x01",
            "We need to get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_2349")


    ChrTalk(    #49
        0x109,
        (
            "#1063FThis isn't the time to be makin' side\x01",
            "trips. We gotta get back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A1")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_23BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_2612")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_23E5"),
        (1, "loc_2437"),
        (2, "loc_2492"),
        (5, "loc_24E7"),
        (7, "loc_253C"),
        (6, "loc_258F"),
        (SWITCH_DEFAULT, "loc_25EF"),
    )


    label("loc_23E5")


    ChrTalk(    #50
        0x101,
        (
            "#1002FWe don't have time for side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_2437")


    ChrTalk(    #51
        0x102,
        (
            "#1042FWe don't have time to make side trips.\x01",
            "We need to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_2492")


    ChrTalk(    #52
        0x103,
        (
            "#022FWe don't have time for any side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_24E7")


    ChrTalk(    #53
        0x106,
        (
            "#057FWe ain't got time to make side trips.\x01",
            "We gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_253C")


    ChrTalk(    #54
        0x108,
        (
            "#072FWe don't have time for side trips.\x01",
            "We must hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_258F")


    ChrTalk(    #55
        0x107,
        (
            "#062FI don't think we have time to make side\x01",
            "trips. We gotta hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_25EF")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2827")

    label("loc_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_2827")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_263B"),
        (1, "loc_267C"),
        (2, "loc_26CB"),
        (5, "loc_2710"),
        (7, "loc_2761"),
        (6, "loc_27B8"),
        (SWITCH_DEFAULT, "loc_2807"),
    )


    label("loc_263B")


    ChrTalk(    #56
        0x101,
        (
            "#1002FNo, not this way!\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2807")

    label("loc_267C")


    ChrTalk(    #57
        0x102,
        (
            "#1042FNo, this is the wrong way!\x01",
            "We have to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2807")

    label("loc_26CB")


    ChrTalk(    #58
        0x103,
        (
            "#022FThis is the wrong way. Let's hurry\x01",
            "back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2807")

    label("loc_2710")


    ChrTalk(    #59
        0x106,
        (
            "#057FNo, this is the wrong way. C'mon,\x01",
            "we gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2807")

    label("loc_2761")


    ChrTalk(    #60
        0x108,
        (
            "#072FThis isn't the right way. We must get\x01",
            "to the capital as soon as possible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2807")

    label("loc_27B8")


    ChrTalk(    #61
        0x107,
        (
            "#065FI think we're going the wrong way.\x01",
            "We gotta hurry to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2807")

    label("loc_2807")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2827")

    Return()

    # Function_13_22E9 end

    def Function_14_2828(): pass

    label("Function_14_2828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_2AC3")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2851"),
        (1, "loc_28A3"),
        (2, "loc_28FE"),
        (5, "loc_2953"),
        (7, "loc_29A8"),
        (6, "loc_29FB"),
        (SWITCH_DEFAULT, "loc_2A5B"),
    )


    label("loc_2851")


    ChrTalk(    #62
        0x101,
        (
            "#1002FWe don't have time for side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_28A3")


    ChrTalk(    #63
        0x102,
        (
            "#1042FWe don't have time to make side trips.\x01",
            "We need to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_28FE")


    ChrTalk(    #64
        0x103,
        (
            "#022FWe don't have time for any side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_2953")


    ChrTalk(    #65
        0x106,
        (
            "#057FWe ain't got time to make side trips.\x01",
            "We gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_29A8")


    ChrTalk(    #66
        0x108,
        (
            "#072FWe don't have time for side trips.\x01",
            "We must hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_29FB")


    ChrTalk(    #67
        0x107,
        (
            "#062FI don't think we have time to make side\x01",
            "trips. We gotta hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_2A5B")

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
    Jump("loc_2D1D")

    label("loc_2AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_2D1D")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2AEC"),
        (1, "loc_2B2D"),
        (2, "loc_2B7C"),
        (5, "loc_2BC1"),
        (7, "loc_2C12"),
        (6, "loc_2C69"),
        (SWITCH_DEFAULT, "loc_2CB8"),
    )


    label("loc_2AEC")


    ChrTalk(    #68
        0x101,
        (
            "#1002FNo, not this way!\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2B2D")


    ChrTalk(    #69
        0x102,
        (
            "#1042FNo, this is the wrong way!\x01",
            "We have to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2B7C")


    ChrTalk(    #70
        0x103,
        (
            "#022FThis is the wrong way. Let's hurry\x01",
            "back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2BC1")


    ChrTalk(    #71
        0x106,
        (
            "#057FNo, this is the wrong way. C'mon,\x01",
            "we gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2C12")


    ChrTalk(    #72
        0x108,
        (
            "#072FThis isn't the right way. We must get\x01",
            "to the capital as soon as possible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2C69")


    ChrTalk(    #73
        0x107,
        (
            "#065FI think we're going the wrong way.\x01",
            "We gotta hurry to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2CB8")

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

    label("loc_2D1D")

    Return()

    # Function_14_2828 end

    def Function_15_2D1E(): pass

    label("Function_15_2D1E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #74
        "\x07\x05North: Grancel - 179 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_2D1E end

    def Function_16_2D6B(): pass

    label("Function_16_2D6B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #75
        "\x07\x05South: Sanktheim Gate\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_2D6B end

    def Function_17_2DB3(): pass

    label("Function_17_2DB3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #76
        "\x07\x05East: Erbe Royal Villa - 224 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_2DB3 end

    SaveToFile()

Try(main)
