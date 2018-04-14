from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4102.x',
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
        '王国军士兵',                           # 10
        '王国军士兵',                           # 11
        '红色的飞艇影子',                       # 12
        '红色的飞艇影子',                       # 13
        '红色的飞艇影子',                       # 14
        '艾尔贝周游道方向',                     # 15
        '王都格兰赛尔方向',                     # 16
        '格鲁纳门方向',                         # 17
        '火焰巨鹫',                             # 18
        '丘陵毒蜂',                             # 19
        '沼泽剑齿吸血魔',                       # 20
        '丘陵毒蜂',                             # 21
        '迅猛小鹫',                             # 22
        '剑齿吸血魔',                           # 23
        '丘陵毒蜂',                             # 24
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
        'ED6_DT09/CH10730 ._CH',             # 13
        'ED6_DT09/CH10731 ._CH',             # 14
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
        'ED6_DT09/CH10730P._CP',             # 13
        'ED6_DT09/CH10731P._CP',             # 14
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
        X                   = 152050,
        Z                   = -2000,
        Y                   = -76100,
        Direction           = 0,
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
        X                   = 149980,
        Z                   = -2000,
        Y                   = -76100,
        Direction           = 0,
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
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 150880,
        Z                   = -2000,
        Y                   = -89600,
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
        X                   = 2420,
        Z                   = 0,
        Y                   = 4600,
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
        X                   = 177300,
        Z                   = 0,
        Y                   = 3160,
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
        X                   = 149700,
        Z                   = -2000,
        Y                   = -62310,
        Direction           = 348,
        Unknown2            = 19,
        Unknown3            = 1245184,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 47300,
        Z                   = 10,
        Y                   = -1820,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50160,
        Z                   = 100,
        Y                   = -13420,
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
        X                   = 114570,
        Z                   = -60,
        Y                   = -5920,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140620,
        Z                   = -20,
        Y                   = 4510,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 97120,
        Z                   = 10,
        Y                   = -44670,
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
        X                   = 145000,
        Z                   = -2040,
        Y                   = -47610,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 125500,
        Y                   = -2000,
        Z                   = -60800,
        Range               = 130100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF5038,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 92840,
        Y                   = -500,
        Z                   = -32910,
        Range               = 79430,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0xFFFF8788,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 85840,
        Y                   = -1000,
        Z                   = -25620,
        Range               = 90190,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE516,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = 167920,
        Y                   = -300,
        Z                   = 13000,
        Range               = 166500,
        Unknown_10          = 0x7D9,
        Unknown_14          = 0xFFFFECB4,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 156480,
        Y                   = -2100,
        Z                   = -79210,
        Range               = 145460,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFECF64,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 149700,
        Y                   = -3000,
        Z                   = -62310,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 84450,
        TriggerZ            = 0,
        TriggerY            = -13640,
        TriggerRange        = 1500,
        ActorX              = 84450,
        ActorZ              = 1700,
        ActorY              = -13640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87930,
        TriggerZ            = 0,
        TriggerY            = -13180,
        TriggerRange        = 1500,
        ActorX              = 87930,
        ActorZ              = 1700,
        ActorY              = -13180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 88070,
        TriggerZ            = 0,
        TriggerY            = -25440,
        TriggerRange        = 1500,
        ActorX              = 88070,
        ActorZ              = 1700,
        ActorY              = -25440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_466",          # 00, 0
        "Function_1_499",          # 01, 1
        "Function_2_54B",          # 02, 2
        "Function_3_619",          # 03, 3
        "Function_4_662",          # 04, 4
        "Function_5_719",          # 05, 5
        "Function_6_1284",         # 06, 6
        "Function_7_18C3",         # 07, 7
        "Function_8_1950",         # 08, 8
        "Function_9_1C99",         # 09, 9
        "Function_10_1D2D",        # 0A, 10
        "Function_11_1DC6",        # 0B, 11
        "Function_12_1E47",        # 0C, 12
        "Function_13_1EA0",        # 0D, 13
        "Function_14_1F07",        # 0E, 14
        "Function_15_21F5",        # 0F, 15
        "Function_16_2545",        # 10, 16
        "Function_17_2700",        # 11, 17
        "Function_18_2751",        # 12, 18
        "Function_19_27AF",        # 13, 19
    )


    def Function_0_466(): pass

    label("Function_0_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_498")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_498")

    Return()

    # Function_0_466 end

    def Function_1_499(): pass

    label("Function_1_499")

    OP_16(0x2, 0xFA0, 0xFFFF6B90, 0xFFFDA288, 0x23003D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D5")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_4EA")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_502")
    OP_B1("R4102_y")
    Jump("loc_51A")

    label("loc_502")

    OP_B1("R4102_n")
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_538")
    SetChrFlags(0x11, 0x80)
    OP_B2(0x0, 0x5, 0x80)
    Jump("loc_54A")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A")
    ClearChrFlags(0x11, 0x80)
    OP_B2(0x1, 0x5, 0x80)

    label("loc_54A")

    Return()

    # Function_1_499 end

    def Function_2_54B(): pass

    label("Function_2_54B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_603")

    label("loc_570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_603")

    label("loc_589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_603")

    label("loc_5A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_603")

    label("loc_5BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_603")

    label("loc_5D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ED")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_603")

    label("loc_5ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_603")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_618")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_603")

    label("loc_618")

    Return()

    # Function_2_54B end

    def Function_3_619(): pass

    label("Function_3_619")

    TalkBegin(0x9)

    ChrTalk(    #0
        0xFE,
        (
            "现在王国军已经封锁了\x01",
            "艾尔贝周游道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "任何人都\x01",
            "不能过去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_3_619 end

    def Function_4_662(): pass

    label("Function_4_662")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A7")

    ChrTalk(    #2
        0xFE,
        (
            "这附近也\x01",
            "未必安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "建议你们赶快\x01",
            "回到城里去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_715")

    label("loc_6A7")


    ChrTalk(    #4
        0xFE,
        (
            "因为紧急情况的缘故，\x01",
            "前面禁止任何人进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "而且这附近也\x01",
            "未必安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "建议你们赶快\x01",
            "回到城里去。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_715")

    TalkEnd(0xA)
    Return()

    # Function_4_662 end

    def Function_5_719(): pass

    label("Function_5_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_726")
    Return()

    label("loc_726")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74A")
    Call(0, 10)
    Call(0, 11)
    AddParty(0x2E, 0xFF, 0xFF)
    FadeToBright(0, 0)

    label("loc_74A")

    SetChrPos(0x8, 111020, 0, -52590, 90)

    NpcTalk(    #7
        0x8,
        "男性的声音",
        "哟，你们是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(127830, -2000, -52550, 0)
    OP_67(0, 9160, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 120520, 0, -52830, 90)
    SetChrPos(0x101, 128410, -2000, -51900, 270)
    SetChrPos(0x12F, 131050, -2000, -52330, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A6")
    SetChrPos(0x105, 128500, -2000, -53020, 270)
    SetChrPos(0xF7, 129840, -2000, -51660, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_862")
    SetChrPos(0x104, 129840, -2000, -53020, 270)
    Jump("loc_8A3")

    label("loc_862")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_884")
    SetChrPos(0x107, 129840, -2000, -53020, 270)
    Jump("loc_8A3")

    label("loc_884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A3")
    SetChrPos(0x108, 129840, -2000, -53020, 270)

    label("loc_8A3")

    Jump("loc_8D9")

    label("loc_8A6")

    SetChrPos(0xF7, 128500, -2000, -53020, 270)
    SetChrPos(0xF8, 129840, -2000, -51660, 270)
    SetChrPos(0xF9, 130000, -2000, -52830, 270)

    label("loc_8D9")

    OP_8E(0x8, 0x1EF8C, 0xFFFFF830, 0xFFFF329C, 0x7D0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B89")

    ChrTalk(    #8
        0x101,
        "#1004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#044F#6P啊……\x01",
            "菲利普先生。\x02\x03",

            "#040F好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#720F好久不见。\x01",
            "科洛蒂娅殿下、艾丝蒂尔小姐。\x02\x03",

            "你们几位去过艾尔贝离宫了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1006F#6P嗯，是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#542F#6P菲利普先生\x01",
            "到王都去有事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#720F是的，公爵阁下\x01",
            "吩咐我出来买东西。\x02\x03",

            "#721F……莫非你们在\x01",
            "离宫遇见殿下了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1016F#6P嗯、嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#045F#6P我们久违地\x01",
            "和他寒暄了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#722F……看来\x01",
            "他又得罪了你们吧。\x02\x03",

            "实在是非常对不起。\x01",
            "我以臣下的身份向各位道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#047F#6P呵呵，您太客气了。\x02\x03",

            "#040F我听说叔叔他被软禁，\x01",
            "所以感到有点担心……\x02\x03",

            "不过他看来很有精神，我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#720F您能够这么说，我真是高兴。\x02\x03",

            "那么我就先告辞了……\x01",
            "各位，失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D83")

    label("loc_B89")


    ChrTalk(    #19
        0x101,
        (
            "#1004F#6P咦……\x01",
            "这不是菲利普先生吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#720F艾丝蒂尔小姐。\x01",
            "好久不见。\x02\x03",

            "你们几位去过艾尔贝离宫了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1006F#6P嗯，是的……\x02\x03",

            "菲利普先生\x01",
            "到王都去办事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#720F是的，公爵阁下\x01",
            "吩咐我出来买东西。\x02\x03",

            "#721F……莫非你们\x01",
            "在离宫遇见阁下了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1025F#6P嗯、嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#722F……看来\x01",
            "他又得罪了你们吧。\x02\x03",

            "实在是非常对不起。\x01",
            "我以臣下的身份向各位道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1016F#6P也不是，他倒没有\x01",
            "对我说过什么失礼的话。\x02\x03",

            "#1006F我并不介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#720F您能这么说我真高兴。\x02\x03",

            "那么我就先告辞了……\x01",
            "各位，失陪了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D83")


    def lambda_D89():
        OP_8E(0xFE, 0x1F39C, 0xFFFFF830, 0xFFFF2C66, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D89)

    def lambda_DA4():

        label("loc_DA4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DA4")

    QueueWorkItem2(0x101, 1, lambda_DA4)

    def lambda_DB5():

        label("loc_DB5")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DB5")

    QueueWorkItem2(0x12F, 1, lambda_DB5)

    def lambda_DC6():

        label("loc_DC6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DC6")

    QueueWorkItem2(0xF7, 1, lambda_DC6)

    def lambda_DD7():

        label("loc_DD7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DD7")

    QueueWorkItem2(0xF8, 1, lambda_DD7)

    def lambda_DE8():

        label("loc_DE8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DE8")

    QueueWorkItem2(0xF9, 1, lambda_DE8)
    WaitChrThread(0x8, 0x1)

    def lambda_DFE():
        OP_8E(0xFE, 0x22AB0, 0xFFFFF830, 0xFFFF2A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DFE)

    def lambda_E19():
        OP_6D(131000, -2000, -54400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E19)

    def lambda_E31():
        OP_67(0, 8920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E31)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)

    def lambda_E53():
        OP_6D(129240, -2000, -52490, 1600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E53)

    def lambda_E6B():
        OP_67(0, 8920, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E6B)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0x12F, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #27
        0x101,
        (
            "#1007F#2P呼～他还是\x01",
            "那么辛苦。\x02\x03",

            "#1015F他好像从公爵小时候起\x01",
            "就负责照顾公爵了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9C")
    OP_8C(0x105, 360, 400)

    ChrTalk(    #28
        0x105,
        (
            "#040F#5P听说已经照顾了\x01",
            "二十年以上了。\x02\x03",

            "据说在那之前\x01",
            "他是在亲卫队里工作的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #29
        0x101,
        (
            "#1004F#2P咦，真的吗！？\x02\x03",

            "#1006F唔～果然是\x01",
            "人不可貌相呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9C")


    ChrTalk(    #30
        0x12F,
        (
            "#264F#8P…………………………\x02\x03",

            "#263F刚才那位爷爷……\x01",
            "绝不是个简单的人物。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF0)
    Sleep(50)

    def lambda_1003():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1003)
    Sleep(50)

    def lambda_1016():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1016)
    Sleep(50)

    def lambda_1029():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1029)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106B")

    ChrTalk(    #31
        0x101,
        "#1004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        "#064F怎么了？玲？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1091")

    label("loc_106B")


    ChrTalk(    #33
        0x101,
        (
            "#1004F咦……\x02\x03",

            "怎么会突然这么说？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1091")

    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #34
        0x12F,
        (
            "#260F#6P因为，他可以\x01",
            "闭着眼睛走路嘛。\x02\x03",

            "玲绝对做不到。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1128")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1166")

    label("loc_1128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114F")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1166")

    label("loc_114F")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1166")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118D")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11CB")

    label("loc_118D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B4")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11CB")

    label("loc_11B4")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_11CB")

    Sleep(1500)

    ChrTalk(    #35
        0x101,
        (
            "#1016F唔，我想\x01",
            "那不是闭着眼睛，\x01",
            "应该是眯着眼睛……\x02\x03",

            "#1006F而且他吃惊的时候\x01",
            "眼睛还是会睁大的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x12F,
        (
            "#264F#6P哎呀？是吗？\x02\x03",

            "#261F呵呵，我也好想\x01",
            "看看他吃惊的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A2(0x1618)
    EventEnd(0x0)
    Return()

    # Function_5_719 end

    def Function_6_1284(): pass

    label("Function_6_1284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_129B")
    Return()

    label("loc_129B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12BB")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_12BB")

    OP_20(0x7D0)
    Fade(1000)
    SetChrPos(0x101, 87670, 0, -18210, 270)
    SetChrPos(0x102, 87650, 0, -19540, 270)
    SetChrPos(0xF8, 89210, 0, -18030, 270)
    SetChrPos(0xF9, 89310, 0, -19440, 270)
    OP_6D(89370, 0, -19860, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(1770, 0)
    OP_6C(134000, 0)
    OP_6E(431, 0)
    OP_0D()
    OP_43(0x101, 0x3, 0x0, 0x7)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139E")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_13D2")

    label("loc_139E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C0")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_13D2")

    label("loc_13C0")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_13D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F4")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1428")

    label("loc_13F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1416")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1428")

    label("loc_1416")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1428")

    Sleep(1000)

    ChrTalk(    #37
        0x101,
        "#1004F#5P咦……这是？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(    #38
        0x106,
        (
            "#052F#5P什么啊，这不是\x01",
            "飞船的引擎声吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FB")

    label("loc_1488")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C8")

    ChrTalk(    #39
        0x103,
        (
            "#023F#5P什么啊，这不是\x01",
            "飞船的引擎声吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FB")

    label("loc_14C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FB")

    ChrTalk(    #40
        0x108,
        (
            "#073F#5P这是……\x01",
            "飞船的引擎声？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FB")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154B")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_157F")

    label("loc_154B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156D")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_157F")

    label("loc_156D")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_157F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_15DA")

    label("loc_15A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C8")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_15DA")

    label("loc_15C8")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_15DA")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_168D")

    label("loc_164F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1676")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_168D")

    label("loc_1676")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_168D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F7")

    label("loc_16B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F7")

    label("loc_16E0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16F7")

    Sleep(1000)

    ChrTalk(    #41
        0x101,
        "#1020F#5P等、等等！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1757")

    ChrTalk(    #42
        0x107,
        (
            "#065F#5P这、这种时候\x01",
            "还能飞的飞船是……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CC")

    label("loc_1757")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1793")

    ChrTalk(    #43
        0x108,
        (
            "#076F#5P这种时候\x01",
            "还能飞的飞船是……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CC")

    label("loc_1793")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CC")

    ChrTalk(    #44
        0x103,
        (
            "#024F#5P这种时候\x01",
            "还能飞的飞船是……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CC")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 135, 500)

    ChrTalk(    #45
        0x102,
        "#1046F#6P是那个……！\x02",
    )

    CloseMessageWindow()

    def lambda_1810():
        OP_6D(97800, 0, -23000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1810)

    def lambda_1828():
        OP_67(0, 12960, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1828)

    def lambda_1840():
        OP_6B(2160, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1840)

    def lambda_1850():
        OP_6C(111000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1850)

    def lambda_1860():
        OP_6E(460, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1860)

    def lambda_1870():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1870)
    Sleep(50)

    def lambda_1883():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1883)
    Sleep(50)

    def lambda_1896():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1896)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1284 end

    def Function_7_18C3(): pass

    label("Function_7_18C3")

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

    # Function_7_18C3 end

    def Function_8_1950(): pass

    label("Function_8_1950")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1975")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_1975")

    OP_22(0x79, 0x1, 0x64)
    SetChrPos(0x101, 88010, 0, -18190, 135)
    SetChrPos(0x102, 87420, 0, -19640, 135)
    SetChrPos(0xF8, 89730, 0, -18750, 135)
    SetChrPos(0xF9, 89300, 0, -20100, 135)
    OP_6D(88080, 0, -19230, 0)
    OP_67(0, 8890, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(260000, 0)
    OP_6E(262, 0)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_A1(0xB, 0x0)
    OP_A1(0xC, 0x1)
    OP_A1(0xD, 0x2)
    SetChrPos(0xB, 104090, 2000, -30210, 315)
    SetChrPos(0xC, 109090, 2000, -25210, 315)
    SetChrPos(0xD, 99090, 2000, -35210, 315)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0xB, 0)
    TurnDirection(0xF8, 0xB, 0)
    TurnDirection(0xF9, 0xB, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1A78():

        label("loc_1A78")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1A78")

    QueueWorkItem2(0x101, 3, lambda_1A78)

    def lambda_1A89():

        label("loc_1A89")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1A89")

    QueueWorkItem2(0x102, 3, lambda_1A89)

    def lambda_1A9A():

        label("loc_1A9A")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1A9A")

    QueueWorkItem2(0xF8, 3, lambda_1A9A)

    def lambda_1AAB():

        label("loc_1AAB")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1AAB")

    QueueWorkItem2(0xF9, 3, lambda_1AAB)

    def lambda_1ABC():
        OP_90(0xFE, 0xFFFF8AD0, 0x0, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ABC)
    Sleep(1000)

    def lambda_1ADC():
        OP_90(0xFE, 0xFFFF8AD0, 0x0, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1ADC)
    Sleep(1000)

    def lambda_1AFC():
        OP_90(0xFE, 0xFFFF8AD0, 0x0, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1AFC)
    WaitChrThread(0xD, 0x1)
    OP_43(0x102, 0x2, 0x0, 0x9)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)

    ChrTalk(    #46
        0x101,
        (
            "#1020F#5P『结社』的飞艇……\x01",
            "为、为什么会出现在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#1046F#5P不好……\x01",
            "那里是王都的方向！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE6")

    ChrTalk(    #48
        0x106,
        (
            "#057F#6P这可不是闹着玩的！\x01",
            "我们赶紧追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C22")

    ChrTalk(    #49
        0x103,
        (
            "#022F#6P这……\x01",
            "看来动作必须快一点了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1C22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(    #50
        0x108,
        "#076F#6P赶快追上去吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1C4C")

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

    # Function_8_1950 end

    def Function_9_1C99(): pass

    label("Function_9_1C99")

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

    # Function_9_1C99 end

    def Function_10_1D2D(): pass

    label("Function_10_1D2D")

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
        (0, "loc_1DA7"),
        (1, "loc_1DAD"),
        (SWITCH_DEFAULT, "loc_1DB3"),
    )


    label("loc_1DA7")

    OP_A2(0x1200)
    Jump("loc_1DB3")

    label("loc_1DAD")

    OP_A2(0x1201)
    Jump("loc_1DB3")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1DC1")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1DC5")

    label("loc_1DC1")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1DC5")

    Return()

    # Function_10_1D2D end

    def Function_11_1DC6(): pass

    label("Function_11_1DC6")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1E09")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_1E27")

    label("loc_1E09")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_1E27")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_11_1DC6 end

    def Function_12_1E47(): pass

    label("Function_12_1E47")

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

    # Function_12_1E47 end

    def Function_13_1EA0(): pass

    label("Function_13_1EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F06")
    EventBegin(0x1)

    ChrTalk(    #51
        0x101,
        (
            "#1002F（格鲁纳门在东边！\x01",
            "……………要快点才行！！）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x101, 84130, 0, -28960, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)

    label("loc_1F06")

    Return()

    # Function_13_1EA0 end

    def Function_14_1F07(): pass

    label("Function_14_1F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_2093")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1F30"),
        (1, "loc_1F64"),
        (2, "loc_1F9C"),
        (5, "loc_1FCF"),
        (7, "loc_2002"),
        (6, "loc_2037"),
        (SWITCH_DEFAULT, "loc_2070"),
    )


    label("loc_1F30")


    ChrTalk(    #52
        0x101,
        (
            "#1002F没时间去别的地方了。\x01",
            "快点前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_1F64")


    ChrTalk(    #53
        0x102,
        (
            "#1042F没时间去别的地方了。\x01",
            "要尽快前往王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_1F9C")


    ChrTalk(    #54
        0x103,
        (
            "#022F没时间去别的地方了。\x01",
            "赶紧前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_1FCF")


    ChrTalk(    #55
        0x106,
        (
            "#057F没时间去别的地方了。\x01",
            "赶紧前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_2002")


    ChrTalk(    #56
        0x108,
        (
            "#072F没时间去别的地方了啊。\x01",
            "赶紧前往王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_2037")


    ChrTalk(    #57
        0x107,
        (
            "#062F没时间去别的地方了呢。\x01",
            "要赶紧前往王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_2070")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_21F4")

    label("loc_2093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_21F4")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_20BC"),
        (1, "loc_20EC"),
        (2, "loc_211C"),
        (5, "loc_2149"),
        (7, "loc_2176"),
        (6, "loc_219D"),
        (SWITCH_DEFAULT, "loc_21D4"),
    )


    label("loc_20BC")


    ChrTalk(    #58
        0x101,
        (
            "#1002F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_20EC")


    ChrTalk(    #59
        0x102,
        (
            "#1042F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_211C")


    ChrTalk(    #60
        0x103,
        (
            "#022F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_2149")


    ChrTalk(    #61
        0x106,
        (
            "#057F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_2176")


    ChrTalk(    #62
        0x108,
        (
            "#072F不是这边。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_219D")


    ChrTalk(    #63
        0x107,
        (
            "#065F那个那个……不是这边。\x01",
            "要赶紧去王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_21D4")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_21F4")

    Return()

    # Function_14_1F07 end

    def Function_15_21F5(): pass

    label("Function_15_21F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_239E")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_221E"),
        (1, "loc_224C"),
        (2, "loc_227A"),
        (5, "loc_22A7"),
        (7, "loc_22D4"),
        (6, "loc_2303"),
        (SWITCH_DEFAULT, "loc_2336"),
    )


    label("loc_221E")


    ChrTalk(    #64
        0x101,
        (
            "#1002F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_224C")


    ChrTalk(    #65
        0x102,
        (
            "#1042F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_227A")


    ChrTalk(    #66
        0x103,
        (
            "#022F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_22A7")


    ChrTalk(    #67
        0x106,
        (
            "#057F没时间去别处了。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_22D4")


    ChrTalk(    #68
        0x108,
        (
            "#072F没时间去别处了啊。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_2303")


    ChrTalk(    #69
        0x107,
        (
            "#062F没时间去别处了呢。\x01",
            "要赶紧去王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_2336")

    OP_59()
    Fade(1000)
    SetChrPos(0x0, 151000, -2000, -74190, 0)
    SetChrPos(0x1, 151000, -2000, -74190, 0)
    SetChrPos(0x2, 151000, -2000, -74190, 0)
    SetChrPos(0x3, 151000, -2000, -74190, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2544")

    label("loc_239E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_2544")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_23C7"),
        (1, "loc_23F7"),
        (2, "loc_2427"),
        (5, "loc_2454"),
        (7, "loc_2481"),
        (6, "loc_24A8"),
        (SWITCH_DEFAULT, "loc_24DF"),
    )


    label("loc_23C7")


    ChrTalk(    #70
        0x101,
        (
            "#1002F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_23F7")


    ChrTalk(    #71
        0x102,
        (
            "#1042F不，不是这边！\x01",
            "……赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_2427")


    ChrTalk(    #72
        0x103,
        (
            "#022F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_2454")


    ChrTalk(    #73
        0x106,
        (
            "#057F不对，不是这边！\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_2481")


    ChrTalk(    #74
        0x108,
        (
            "#072F不是这边。\x01",
            "赶紧去王都吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_24A8")


    ChrTalk(    #75
        0x107,
        (
            "#065F那个那个……不是这边。\x01",
            "要赶紧去王都才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_24DF")

    OP_59()
    Fade(1000)
    SetChrPos(0x0, 151000, -2000, -74190, 0)
    SetChrPos(0x1, 151000, -2000, -74190, 0)
    SetChrPos(0x2, 151000, -2000, -74190, 0)
    SetChrPos(0x3, 151000, -2000, -74190, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2544")

    Return()

    # Function_15_21F5 end

    def Function_16_2545(): pass

    label("Function_16_2545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 3)), scpexpr(EXPR_END)), "loc_254D")
    Return()

    label("loc_254D")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2632"),
        (SWITCH_DEFAULT, "loc_2655"),
    )


    label("loc_2632")

    Fade(500)
    OP_89(0x0, 145940, -2000, -57070, 143)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_2655")

    Battle(0xEE5, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 145940, -2000, -57070, 143)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_268E"),
        (1, "loc_2691"),
        (SWITCH_DEFAULT, "loc_2694"),
    )


    label("loc_268E")

    EventEnd(0x0)
    Return()

    label("loc_2691")

    OP_B4(0x0)
    Return()

    label("loc_2694")

    EventBegin(0x1)
    SetChrFlags(0x11, 0x80)
    OP_B2(0x0, 0x5, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x16FB)
    OP_28(0xA9, 0x4, 0x10)
    OP_28(0xA9, 0x4, 0x2)
    OP_28(0xA9, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_16_2545 end

    def Function_17_2700(): pass

    label("Function_17_2700")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05西　王都格兰赛尔　１６８塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_2700 end

    def Function_18_2751(): pass

    label("Function_18_2751")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #79
        (
            "\x07\x05东　洛连特市　　　３６８塞尔矩\x01",
            "　　格鲁纳门\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_2751 end

    def Function_19_27AF(): pass

    label("Function_19_27AF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #80
        "\x07\x05南　艾尔贝离宫　　２５６塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_27AF end

    SaveToFile()

Try(main)
