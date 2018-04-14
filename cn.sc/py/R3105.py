from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R3105   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3105.x',
        MapIndex            = 144,
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
        '霍夫曼上尉',                           # 9
        '士兵里诺',                             # 10
        '蔡斯方向',                             # 11
        '沃尔费堡垒方向',                       # 12
        '红莲之塔方向',                         # 13
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
        'ED6_DT09/CH10610 ._CH',             # 00
        'ED6_DT09/CH10611 ._CH',             # 01
        'ED6_DT09/CH10080 ._CH',             # 02
        'ED6_DT09/CH10081 ._CH',             # 03
        'ED6_DT09/CH10120 ._CH',             # 04
        'ED6_DT09/CH10121 ._CH',             # 05
        'ED6_DT09/CH10140 ._CH',             # 06
        'ED6_DT09/CH10141 ._CH',             # 07
        'ED6_DT09/CH10620 ._CH',             # 08
        'ED6_DT09/CH10621 ._CH',             # 09
        'ED6_DT09/CH10600 ._CH',             # 0A
        'ED6_DT09/CH10601 ._CH',             # 0B
        'ED6_DT09/CH10400 ._CH',             # 0C
        'ED6_DT09/CH10401 ._CH',             # 0D
        'ED6_DT09/CH11210 ._CH',             # 0E
        'ED6_DT09/CH11211 ._CH',             # 0F
        'ED6_DT09/CH11250 ._CH',             # 10
        'ED6_DT09/CH11251 ._CH',             # 11
        'ED6_DT07/CH01310 ._CH',             # 12
        'ED6_DT07/CH01640 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT09/CH10610P._CP',             # 00
        'ED6_DT09/CH10611P._CP',             # 01
        'ED6_DT09/CH10080P._CP',             # 02
        'ED6_DT09/CH10081P._CP',             # 03
        'ED6_DT09/CH10120P._CP',             # 04
        'ED6_DT09/CH10121P._CP',             # 05
        'ED6_DT09/CH10140P._CP',             # 06
        'ED6_DT09/CH10141P._CP',             # 07
        'ED6_DT09/CH10620P._CP',             # 08
        'ED6_DT09/CH10621P._CP',             # 09
        'ED6_DT09/CH10600P._CP',             # 0A
        'ED6_DT09/CH10601P._CP',             # 0B
        'ED6_DT09/CH10400P._CP',             # 0C
        'ED6_DT09/CH10401P._CP',             # 0D
        'ED6_DT09/CH11210P._CP',             # 0E
        'ED6_DT09/CH11211P._CP',             # 0F
        'ED6_DT09/CH11250P._CP',             # 10
        'ED6_DT09/CH11251P._CP',             # 11
        'ED6_DT07/CH01310P._CP',             # 12
        'ED6_DT07/CH01640P._CP',             # 13
    )

    DeclNpc(
        X                   = 1400,
        Z                   = -40,
        Y                   = 9260,
        Direction           = 135,
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
        X                   = 2490,
        Z                   = -30,
        Y                   = 7960,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -74130,
        Z                   = 0,
        Y                   = 3100,
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
        X                   = 64319,
        Z                   = 10,
        Y                   = -52920,
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
        X                   = 10040,
        Z                   = -130,
        Y                   = 67800,
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
        X                   = -36940,
        Z                   = -10,
        Y                   = 10890,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28070,
        Z                   = 80,
        Y                   = 10280,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17490,
        Z                   = 0,
        Y                   = -1540,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4150,
        Z                   = -60,
        Y                   = 15540,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32970,
        Z                   = -30,
        Y                   = 25660,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26690,
        Z                   = 50,
        Y                   = 5570,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13500,
        Z                   = -20,
        Y                   = -4890,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34620,
        Z                   = -50,
        Y                   = -10530,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37440,
        Z                   = -50,
        Y                   = -24530,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15930,
        Z                   = 0,
        Y                   = -38970,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35920,
        Z                   = -20,
        Y                   = -35400,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29740,
        Z                   = -110,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19490,
        Z                   = 0,
        Y                   = -17710,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12390,
        Z                   = 50,
        Y                   = -16010,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5230,
        Z                   = 0,
        Y                   = -27150,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -3130,
        TriggerZ            = 30,
        TriggerY            = -11320,
        TriggerRange        = 1000,
        ActorX              = -3130,
        ActorZ              = 30,
        ActorY              = -10750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13630,
        TriggerZ            = 0,
        TriggerY            = 35620,
        TriggerRange        = 1500,
        ActorX              = 13630,
        ActorZ              = 1200,
        ActorY              = 35620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36850,
        TriggerZ            = 80,
        TriggerY            = 17250,
        TriggerRange        = 1000,
        ActorX              = 33720,
        ActorZ              = -1000,
        ActorY              = 13980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3FA",          # 00, 0
        "Function_1_42C",          # 01, 1
        "Function_2_52B",          # 02, 2
        "Function_3_541",          # 03, 3
        "Function_4_8A5",          # 04, 4
        "Function_5_AEA",          # 05, 5
        "Function_6_C30",          # 06, 6
        "Function_7_18C0",         # 07, 7
        "Function_8_18DC",         # 08, 8
        "Function_9_18FD",         # 09, 9
        "Function_10_191E",        # 0A, 10
        "Function_11_193F",        # 0B, 11
        "Function_12_19C6",        # 0C, 12
        "Function_13_1A1F",        # 0D, 13
        "Function_14_1A73",        # 0E, 14
    )


    def Function_0_3FA(): pass

    label("Function_0_3FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_428")
    SetChrPos(0x9, 5620, 20, -7270, 45)

    label("loc_428")

    OP_A2(0x0)
    Return()

    # Function_0_3FA end

    def Function_1_42C(): pass

    label("Function_1_42C")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x23002F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E9")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1C), scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    OP_CE(0x0, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_498")
    OP_28(0x6E, 0x1, 0x40)
    Jump("loc_4E9")

    label("loc_498")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD")
    OP_28(0x6E, 0x1, 0x20)
    Jump("loc_4E9")

    label("loc_4AD")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C2")
    OP_28(0x6E, 0x1, 0x10)
    Jump("loc_4E9")

    label("loc_4C2")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D7")
    OP_28(0x6E, 0x1, 0x8)
    Jump("loc_4E9")

    label("loc_4D7")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    OP_28(0x6E, 0x1, 0x4)

    label("loc_4E9")

    OP_A3(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE")
    OP_6F(0x1, 0)
    Jump("loc_505")

    label("loc_4FE")

    OP_6F(0x1, 60)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_52A")

    Return()

    # Function_1_42C end

    def Function_2_52B(): pass

    label("Function_2_52B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_540")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_52B")

    label("loc_540")

    Return()

    # Function_2_52B end

    def Function_3_541(): pass

    label("Function_3_541")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B")
    Call(0, 6)
    Jump("loc_8A1")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_72F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC")

    ChrTalk(    #0
        0xFE,
        "呀，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "温泉的修理\x01",
            "还顺利吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000F啊，嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1040F顺利解决了。\x02\x03",

            "非常感谢您的帮助\x01",
            "真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "哦哦，很顺利吗。\x01",
            "那就最好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "这样小的工作成果\x01",
            "说不定能让市民们感到安心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "我们王国军也会致力于\x01",
            "治安的维持和地区的稳定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "今后让我们互相配合，\x01",
            "共同去克服这次的难关吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1000F嗯……明白了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20CE)
    Jump("loc_72C")

    label("loc_6CC")


    ChrTalk(    #9
        0xFE,
        (
            "温泉的修理……\x01",
            "成功是再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "那么，今后让我们互相配合，\x01",
            "共同去克服这次的难关吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72C")

    Jump("loc_8A1")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_799")

    ChrTalk(    #11
        0xFE,
        (
            "正是在这种状况下\x01",
            "心情的平和才显得重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "亚尔摩温泉的修复工作，\x01",
            "请诸位务必要多加努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A1")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F")

    ChrTalk(    #13
        0xFE,
        (
            "在前往蔡斯的途中，\x01",
            "突然变得无法操纵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "最后总算将飞艇\x01",
            "降落在这片平原上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "从状况看来，似乎是\x01",
            "导力器无法运作了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "……不过，到底发生了什么事？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8A1")

    label("loc_84F")


    ChrTalk(    #17
        0xFE,
        (
            "在前往蔡斯的途中，\x01",
            "突然变得无法操纵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "最后总算将飞艇\x01",
            "降落在这片平原上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A1")

    TalkEnd(0x8)
    Return()

    # Function_3_541 end

    def Function_4_8A5(): pass

    label("Function_4_8A5")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BF")
    Call(0, 6)
    Jump("loc_AE6")

    label("loc_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92A")

    ChrTalk(    #19
        0xFE,
        (
            "为保险起见，\x01",
            "目前正在检查机体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "哎，说白了\x01",
            "也就是打发时间而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 45, 400)
    SetChrFlags(0x9, 0x10)
    OP_A2(0x2)
    Jump("loc_94D")

    label("loc_92A")


    ChrTalk(    #21
        0xFE,
        (
            "哼哼……\x01",
            "支架好像没有异常啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94D")

    Jump("loc_AE6")

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_A12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C7")

    ChrTalk(    #22
        0xFE,
        (
            "亚尔摩温泉吗～\x01",
            "好久没去了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "呼，到时候真想\x01",
            "悠闲地泡泡澡啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "那么，修理要加油哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_A0F")

    label("loc_9C7")


    ChrTalk(    #25
        0xFE,
        (
            "亚尔摩温泉吗～\x01",
            "好久没去了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "呼，到时候真想\x01",
            "悠闲地泡泡澡啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0F")

    Jump("loc_AE6")

    label("loc_A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A96")

    ChrTalk(    #27
        0xFE,
        (
            "呼，总算\x01",
            "平安着陆了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "结果偏偏是降落在\x01",
            "托兰特平原正中央啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "救援部队要过来\x01",
            "恐怕还得等很久呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_AE6")

    label("loc_A96")


    ChrTalk(    #30
        0xFE,
        (
            "着陆的地方偏偏\x01",
            "托兰特平原正中央啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "救援部队要过来\x01",
            "恐怕还得等很久呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE6")

    TalkEnd(0x9)
    Return()

    # Function_4_8A5 end

    def Function_5_AEA(): pass

    label("Function_5_AEA")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C04")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x0, 0xA)
    AddSepith(0x1, 0xA)
    AddSepith(0x2, 0xA)
    AddSepith(0x3, 0xA)
    AddSepith(0x4, 0xA)
    AddSepith(0x5, 0xA)
    AddSepith(0x6, 0xA)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #32
        (
            "\x07\x00得到了\x01",
            "\x07\x02#56I地之耀晶片×１０\x01",
            "\x07\x02#57I水之耀晶片×１０\x01",
            "\x07\x02#58I火之耀晶片×１０\x01",
            "\x07\x02#59I风之耀晶片×１０\x01",
            "\x07\x02#62I时之耀晶片×１０\x01",
            "\x07\x02#60I空之耀晶片×１０\x01",
            "\x07\x02#61I幻之耀晶片×１０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1506)
    Jump("loc_C1E")

    label("loc_C04")


    AnonymousTalk(    #33
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C1E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_AEA end

    def Function_6_C30(): pass

    label("Function_6_C30")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C55")
    Call(0, 11)
    Call(0, 12)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_C55")

    Fade(1000)
    OP_6D(2520, -50, 8109, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(179000, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, 2690, -70, 10480, 225)
    SetChrPos(0x102, 3500, -20, 9710, 225)
    SetChrPos(0xF8, 3300, 50, 11900, 225)
    SetChrPos(0xF9, 4280, 60, 11100, 225)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_8C(0x8, 45, 0)
    OP_8C(0x9, 45, 0)
    OP_0D()

    ChrTalk(    #34
        0x8,
        "#2P哎呀，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1025F#6P那个，我们是\x01",
            "游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x05艾丝蒂尔等人说明了情况\x01",
            "并试着询问了内燃引擎的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #37
        0x8,
        (
            "#2P是吗……因为那次骚动，\x01",
            "我都完全忘记有这回事了。\x02\x03",

            "我记得，那个内燃引擎\x01",
            "应该保管在货舱里才对。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #38
        0x8,
        "#4P里诺，帮个忙。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #39
        0x9,
        "#5P明白。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)

    def lambda_E51():

        label("loc_E51")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E51")

    QueueWorkItem2(0x101, 2, lambda_E51)

    def lambda_E62():

        label("loc_E62")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_E62")

    QueueWorkItem2(0x102, 2, lambda_E62)

    def lambda_E73():

        label("loc_E73")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E73")

    QueueWorkItem2(0xF8, 2, lambda_E73)

    def lambda_E84():

        label("loc_E84")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_E84")

    QueueWorkItem2(0xF9, 2, lambda_E84)
    OP_6D(2520, -50, 8109, 0)
    OP_67(0, 2970, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(179000, 0)
    OP_6E(359, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_EDC():
        OP_67(0, 4960, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EDC)
    SetChrPos(0x8, 5830, 1000, 1450, 135)
    SetChrPos(0x9, 5830, 1000, 1450, 315)
    ClearChrFlags(0x8, 0x80)

    def lambda_F1B():
        OP_8F(0xFE, 0x546, 0xFFFFFFC4, 0x21F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F1B)
    Sleep(600)
    ClearChrFlags(0x9, 0x80)

    def lambda_F40():
        OP_8F(0xFE, 0x88E, 0xFFFFFFC4, 0x1E6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F40)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_8C(0x8, 45, 400)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 45, 400)

    ChrTalk(    #40
        0x8,
        "#2P呀，让你们久等了。\x02",
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xA96, 0xFFFFFFCE, 0x24EA, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #41
        "\x1F\x0D\x04\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x40D, 1)
    OP_8F(0x9, 0x88E, 0xFFFFFFC4, 0x1E6E, 0x7D0, 0x0)

    ChrTalk(    #42
        0x101,
        "#1006F#6P嗯，我们确实收下了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        "#1040F#6P给您添麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#2P哪里哪里，\x01",
            "劳驾你们特地过来拿\x01",
            "才真是不好意思。\x02\x03",

            "不过，在这危急状况下\x01",
            "居然为了让大家能够泡温泉\x01",
            "而展开行动……\x02\x03",

            "看来游击士的\x01",
            "行动基准果然和我们不同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1013F#6P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#1043F#6P不好意思……\x01",
            "在这么严重的时候我们还做这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#2P不，我并不是\x01",
            "在讽刺你们。\x02\x03",

            "……对我们来说\x01",
            "导力兵器不能使用\x01",
            "是相当令人不安的状况。\x02\x03",

            "我们光顾着考虑\x01",
            "要如何去应对敌人才好……\x02\x03",

            "也许应该稍微学习一下\x01",
            "你们这种从容不迫的态度呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1025F#6P嗯、嗯～\x02\x03",

            "#1016F我们只是……\x01",
            "随便找事情做而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_129B")

    ChrTalk(    #49
        0x108,
        (
            "#070F#6P老实说，我们也\x01",
            "正为了该做些什么而迷惑。\x02\x03",

            "我们大家都只能一边摸索，\x01",
            "一边找到答案吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137A")

    label("loc_129B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_130E")

    ChrTalk(    #50
        0x103,
        (
            "#027F#6P老实说，我们也\x01",
            "正为了该做些什么而迷惑呢。\x02\x03",

            "我们大家都只能一边摸索，\x01",
            "一边找到答案吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137A")

    label("loc_130E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137A")

    ChrTalk(    #51
        0x106,
        (
            "#051F#6P其实，我们\x01",
            "也正为该做些什么而迷惑啊。\x02\x03",

            "我们大家都只能一边摸索，\x01",
            "一边寻找答案吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137A")


    ChrTalk(    #52
        0x8,
        (
            "#2P啊啊……是啊。\x02\x03",

            "不过，正是在这种状况下，\x01",
            "心情的平和才显得重要。\x02\x03",

            "亚尔摩温泉的修复工作，\x01",
            "请诸位务必要多加努力。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1415")

    ChrTalk(    #53
        0x107,
        "#061F#6P是、是。\x02",
    )

    CloseMessageWindow()

    label("loc_1415")


    ChrTalk(    #54
        0x101,
        "#1006F#6P嗯……交给我们吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_6D(15760, -50, -20140, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 15020, 10, -21640, 180)
    SetChrPos(0x102, 15950, -30, -21640, 180)
    SetChrPos(0xF8, 14650, 20, -20780, 180)
    SetChrPos(0xF9, 16400, -30, -20780, 180)
    OP_43(0x101, 0x1, 0x0, 0x7)
    OP_43(0x102, 0x1, 0x0, 0x8)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    Sleep(400)

    def lambda_14EE():
        OP_6D(15150, 70, -30990, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14EE)

    def lambda_1506():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1506)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0xF8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇汽油到手了】\x01",              # 0
            "【◇没有汽油但有介绍信】\x01",      # 1
            "【◇汽油和介绍信都没有】\x01",      # 2
            "【◇不变更】\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15C7"),
        (1, "loc_15CD"),
        (2, "loc_15D6"),
        (SWITCH_DEFAULT, "loc_15DF"),
    )


    label("loc_15C7")

    OP_A2(0x2011)
    Jump("loc_15DF")

    label("loc_15CD")

    OP_A3(0x2011)
    OP_A2(0x2010)
    Jump("loc_15DF")

    label("loc_15D6")

    OP_A3(0x2011)
    OP_A3(0x2010)
    Jump("loc_15DF")

    label("loc_15DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_END)), "loc_1722")
    OP_28(0xC2, 0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1689")
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #55
        0x101,
        (
            "#1006F#6P好了……\x01",
            "这样一来材料就齐全了。\x02\x03",

            "赶快返回亚尔摩\x01",
            "开始改造水泵装置吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #56
        0x107,
        (
            "#061F#5P嗯，我是准备好了，\x01",
            "随时ＯＫ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171F")

    label("loc_1689")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #57
        0x101,
        (
            "#1006F#6P好了……\x01",
            "这样一来材料就齐全了。\x02\x03",

            "#1015F到底还是只有提妲\x01",
            "才能改造水泵装置吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#1040F#2P说得也是。\x02\x03",

            "先返回协会\x01",
            "和提妲会合吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171F")

    Jump("loc_188A")

    label("loc_1722")


    ChrTalk(    #59
        0x101,
        (
            "#1006F#6P好了……\x01",
            "这样内燃引擎就ＯＫ了。\x02\x03",

            "#1015F接下来是汽油……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_END)), "loc_1815")

    ChrTalk(    #60
        0x102,
        (
            "#1040F#2P据玛多克工房长所言，\x01",
            "从共和国订购来的东西\x01",
            "好像已经运抵了卢安的港口。\x02\x03",

            "看来只有过去看看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1006F#6P嗯，既然做到这一步，\x01",
            "就必须坚持到最后才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188A")

    label("loc_1815")


    ChrTalk(    #62
        0x102,
        (
            "#1035F#2P说不定就像之前一样，\x01",
            "有可能会保管在中央工房地下。\x02\x03",

            "#1040F先去那里确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1006F#6P嗯，明白。\x02",
    )

    CloseMessageWindow()

    label("loc_188A")

    OP_A2(0x200F)
    OP_28(0xC2, 0x1, 0x80)
    SetChrPos(0x8, 1400, -40, 9260, 135)
    SetChrPos(0x9, 2590, -40, 7810, 315)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_6_C30 end

    def Function_7_18C0(): pass

    label("Function_7_18C0")

    OP_8E(0xFE, 0x3692, 0x3C, 0xFFFF815C, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_18C0 end

    def Function_8_18DC(): pass

    label("Function_8_18DC")

    Sleep(150)
    OP_8E(0xFE, 0x3CC8, 0x50, 0xFFFF82B0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_18DC end

    def Function_9_18FD(): pass

    label("Function_9_18FD")

    Sleep(350)
    OP_8E(0xFE, 0x3700, 0x32, 0xFFFF8878, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_9_18FD end

    def Function_10_191E(): pass

    label("Function_10_191E")

    Sleep(350)
    OP_8E(0xFE, 0x3D5E, 0x32, 0xFFFF88BE, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_10_191E end

    def Function_11_193F(): pass

    label("Function_11_193F")

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
        (0, "loc_19B9"),
        (1, "loc_19BF"),
        (SWITCH_DEFAULT, "loc_19C5"),
    )


    label("loc_19B9")

    OP_A2(0x1200)
    Jump("loc_19C5")

    label("loc_19BF")

    OP_A2(0x1201)
    Jump("loc_19C5")

    label("loc_19C5")

    Return()

    # Function_11_193F end

    def Function_12_19C6(): pass

    label("Function_12_19C6")

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

    # Function_12_19C6 end

    def Function_13_1A1F(): pass

    label("Function_13_1A1F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #64
        (
            "\x07\x05北　红莲之塔\x01",
            "※魔兽较多，请注意！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1A1F end

    def Function_14_1A73(): pass

    label("Function_14_1A73")

    EventBegin(0x1)

    ChrTalk(    #65
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_1A9F():
        OP_6D(34900, 70, 15500, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A9F)

    def lambda_1AB7():
        OP_6B(3250, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1AB7)

    def lambda_1AC7():
        OP_6C(270000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1AC7)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4E")
    OP_C0(0xE, 0x23, 0x8FF2, 0x50, 0x4362, 0xE1, 0x83B8, 0xFFFFFC18, 0x369C)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_1B5D")

    label("loc_1B4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B5D")
    EventEnd(0x1)

    label("loc_1B5D")

    Return()

    # Function_14_1A73 end

    SaveToFile()

Try(main)
