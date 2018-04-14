from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2710   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2710.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '目标用照相机',                         # 9
        '哈恩队长',                             # 10
        '玲',                                   # 11
        '玲的父亲',                             # 12
        '玲的母亲',                             # 13
        '士兵库隆',                             # 14
        '士兵奥塔',                             # 15
        '塞萨尔',                               # 16
        '基恩茨副队长',                         # 17
        '科尼嘉',                               # 18
        '提克',                                 # 19
        '莫莉',                                 # 20
        '士兵尼克斯',                           # 21
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT27/CH03910 ._CH',             # 02
        'ED6_DT27/CH03920 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01270 ._CH',             # 05
        'ED6_DT07/CH01143 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01640 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT27/CH03910P._CP',             # 02
        'ED6_DT27/CH03920P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01270P._CP',             # 05
        'ED6_DT07/CH01143P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01640P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4750,
        Z                   = 0,
        Y                   = 90620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -4800,
        Z                   = 0,
        Y                   = 7900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 93480,
        Z                   = 0,
        Y                   = 85530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 95300,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 93870,
        Z                   = 0,
        Y                   = 13580,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3960,
        Z                   = 0,
        Y                   = 25000,
        Direction           = 273,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2580,
        Z                   = 0,
        Y                   = 16760,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -2580,
        Z                   = 0,
        Y                   = 23040,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 96770,
        Z                   = 0,
        Y                   = 14030,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclEvent(
        X                   = -3939,
        Y                   = -1000,
        Z                   = 1820,
        Range               = 2122,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = -2990,
        TriggerZ            = 0,
        TriggerY            = 7710,
        TriggerRange        = 1000,
        ActorX              = -4800,
        ActorZ              = 1500,
        ActorY              = 7900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93600,
        TriggerZ            = 0,
        TriggerY            = 87450,
        TriggerRange        = 1000,
        ActorX              = 93480,
        ActorZ              = 1500,
        ActorY              = 85530,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 95800,
        TriggerZ            = 0,
        TriggerY            = 13660,
        TriggerRange        = 1000,
        ActorX              = 95300,
        ActorZ              = 1500,
        ActorY              = 16000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2990,
        TriggerZ            = 0,
        TriggerY            = 7710,
        TriggerRange        = 1000,
        ActorX              = -4800,
        ActorZ              = 1500,
        ActorY              = 7900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_352",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_5E4",          # 02, 2
        "Function_3_6B2",          # 03, 3
        "Function_4_6D6",          # 04, 4
        "Function_5_794",          # 05, 5
        "Function_6_799",          # 06, 6
        "Function_7_DBE",          # 07, 7
        "Function_8_DC3",          # 08, 8
        "Function_9_1482",         # 09, 9
        "Function_10_1487",        # 0A, 10
        "Function_11_1B8A",        # 0B, 11
        "Function_12_219B",        # 0C, 12
        "Function_13_2673",        # 0D, 13
        "Function_14_2B10",        # 0E, 14
        "Function_15_2E80",        # 0F, 15
        "Function_16_38E8",        # 10, 16
        "Function_17_3949",        # 11, 17
        "Function_18_39F5",        # 12, 18
        "Function_19_3A4D",        # 13, 19
        "Function_20_400C",        # 14, 20
        "Function_21_52DA",        # 15, 21
        "Function_22_5321",        # 16, 22
        "Function_23_535C",        # 17, 23
        "Function_24_5397",        # 18, 24
        "Function_25_5430",        # 19, 25
        "Function_26_57B5",        # 1A, 26
    )


    def Function_0_352(): pass

    label("Function_0_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3A8")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_394")
    SetChrPos(0x10, -2580, 0, 93750, 180)
    SetChrPos(0x9, -710, 0, 92770, 277)
    Jump("loc_3A5")

    label("loc_394")

    SetChrPos(0x10, -2840, 0, 19000, 270)

    label("loc_3A5")

    Jump("loc_4F4")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3E7")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x12, -2710, 0, 18290, 0)
    SetChrPos(0x13, -2710, 0, 19610, 180)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    Jump("loc_4F4")

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_413")
    SetChrPos(0x9, -670, 0, 92690, 270)
    SetChrPos(0x10, -2400, 0, 92690, 90)
    Jump("loc_4F4")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_41D")
    Jump("loc_4F4")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_442")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x10, -4800, 0, 7900, 90)
    Jump("loc_4F4")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_44C")
    Jump("loc_4F4")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 5)), scpexpr(EXPR_END)), "loc_4AB")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 93664, 0, 87456, 180)
    SetChrPos(0xA, 95770, 0, 87453, 0)
    SetChrPos(0xC, 94561, 0, 88500, 0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xC, 0xA, 0)
    SetChrFlags(0xC, 0x10)
    Jump("loc_4F4")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_END)), "loc_4F4")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -3410, 0, 19050, 270)
    SetChrPos(0xB, -1990, 0, 20610, 135)
    SetChrPos(0xC, -1010, 0, 19120, 315)

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_53B")
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 95590, 200, 7460, 180)
    SetChrFlags(0x11, 0x10)
    OP_44(0x11, 0x0)
    SetChrChipByIndex(0x11, 6)
    SetChrSubChip(0x11, 0)

    label("loc_53B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_547"),
        (SWITCH_DEFAULT, "loc_55F"),
    )


    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_55C")

    Jump("loc_55F")

    label("loc_55F")

    Return()

    # Function_0_352 end

    def Function_1_560(): pass

    label("Function_1_560")

    OP_64(0x3, 0x1)
    OP_1C(0x3, 0x0, 0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_573")
    Jump("loc_5BC")

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_57D")
    Jump("loc_5BC")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_58F")
    OP_65(0x0, 0x1)
    OP_64(0x3, 0x1)
    Jump("loc_5BC")

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_5A1")
    OP_64(0x0, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_5BC")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_5AB")
    Jump("loc_5BC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 5)), scpexpr(EXPR_END)), "loc_5B5")
    Jump("loc_5BC")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_END)), "loc_5BC")

    label("loc_5BC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5D8"),
        (101, "loc_5D8"),
        (102, "loc_5D8"),
        (104, "loc_5D8"),
        (106, "loc_5D8"),
        (SWITCH_DEFAULT, "loc_5E0"),
    )


    label("loc_5D8")

    OP_22(0x1C6, 0x1, 0x64)
    Jump("loc_5E3")

    label("loc_5E0")

    OP_23(0x1C6)

    label("loc_5E3")

    Return()

    # Function_1_560 end

    def Function_2_5E4(): pass

    label("Function_2_5E4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_69C")

    label("loc_609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_622")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_69C")

    label("loc_622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_69C")

    label("loc_63B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_69C")

    label("loc_654")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_69C")

    label("loc_66D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_69C")

    label("loc_686")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_69C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_69C")

    label("loc_6B1")

    Return()

    # Function_2_5E4 end

    def Function_3_6B2(): pass

    label("Function_3_6B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D5")
    OP_8D(0xFE, -1070, 16329, -4540, 25330, 2000)
    Jump("Function_3_6B2")

    label("loc_6D5")

    Return()

    # Function_3_6B2 end

    def Function_4_6D6(): pass

    label("Function_4_6D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_729")

    ChrTalk(    #0
        0xFE,
        (
            "不知道为什么\x01",
            "只有我一个人休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "所以白天就来这里\x01",
            "小酌一杯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790")

    label("loc_729")

    OP_A2(0x8)

    ChrTalk(    #2
        0xFE,
        (
            "哟，详细情况我没听说，\x01",
            "不过据说幽灵骚动解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "而且今天突然不用值勤，\x01",
            "真是好事不断啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790")

    TalkEnd(0xFE)
    Return()

    # Function_4_6D6 end

    def Function_5_794(): pass

    label("Function_5_794")

    Call(0, 6)
    Return()

    # Function_5_794 end

    def Function_6_799(): pass

    label("Function_6_799")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_8E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C")

    ChrTalk(    #4
        0xD,
        (
            "卡鲁迪亚隧道中\x01",
            "现在是一片漆黑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xD,
        (
            "但是，刚才有位旅行者\x01",
            "通过了这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "好像是中央工房的研究者，\x01",
            "要通过现在的隧道\x01",
            "还真不是一般的有胆量啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        (
            "聪明人想的事\x01",
            "说实话真搞不懂。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8E3")

    label("loc_86C")


    ChrTalk(    #8
        0xD,
        (
            "这么说来那个人……\x01",
            "还带着猫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xD,
        (
            "嗯～说不定\x01",
            "那是用来避邪什么的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xD,
        (
            "的、的确有宠物在的话\x01",
            "说不定比较安心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E3")

    Jump("loc_DBA")

    label("loc_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B7")

    ChrTalk(    #11
        0xD,
        (
            "因为门关不上\x01",
            "通行者的检查\x01",
            "也比平常严格很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        (
            "不过，有通知说\x01",
            "要保证游击士们自由通行\x01",
            "所以不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xD,
        (
            "这是协助协会活动\x01",
            "的特别措施……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xD,
        (
            "不过这在以前\x01",
            "可是想都想不到的通知呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_A0B")

    label("loc_9B7")


    ChrTalk(    #15
        0xD,
        (
            "各位游击士\x01",
            "可以自由通行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xD,
        (
            "上面有这样的通知。\x01",
            "以前可是想都想不到的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0B")

    Jump("loc_DBA")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A65")

    ChrTalk(    #17
        0xD,
        (
            "蔡斯的地震\x01",
            "据说已经稳定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        (
            "唉，地震\x01",
            "没到这边来真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_A65")


    ChrTalk(    #19
        0xD,
        (
            "蔡斯的地震\x01",
            "据说已经稳定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xD,
        (
            "好像是中央工房发布的，\x01",
            "大概没错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_AB2")

    Jump("loc_DBA")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B12")

    ChrTalk(    #21
        0xD,
        (
            "刚才从司令部\x01",
            "发来了紧急联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xD,
        (
            "之后队长他们\x01",
            "就没从房间里出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7B")

    label("loc_B12")


    ChrTalk(    #23
        0xD,
        (
            "刚才从司令部\x01",
            "发来了紧急联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xD,
        (
            "之后队长他们\x01",
            "就没从房间里出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xD,
        "发、发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B7B")

    Jump("loc_DBA")

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BCD")

    ChrTalk(    #26
        0xD,
        (
            "蔡斯\x01",
            "据说发生了地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xD,
        (
            "希、希望它不要\x01",
            "可别过来啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3F")

    label("loc_BCD")


    ChrTalk(    #28
        0xD,
        (
            "蔡斯好像\x01",
            "发生了地震呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        (
            "其、其实我……\x01",
            "最讨厌地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "因为地面会摇摆不定哦？\x01",
            "当然会令人不安吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C3F")

    Jump("loc_DBA")

    label("loc_C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C95")

    ChrTalk(    #31
        0xD,
        (
            "看起来还是\x01",
            "游客很少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        (
            "卢安的选举\x01",
            "结束之前都是这样吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDE")

    label("loc_C95")


    ChrTalk(    #33
        0xD,
        (
            "呀，欢迎来到\x01",
            "艾尔·雷登关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "客人还是那么少，\x01",
            "就请自便吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CDE")

    Jump("loc_DBA")

    label("loc_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_D26")

    ChrTalk(    #35
        0xD,
        (
            "队长和副队长\x01",
            "两人一起在叹息呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        "有什么烦恼事吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_DBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D6C")

    ChrTalk(    #37
        0xD,
        "现在游客很少。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "好像因为卢安选举\x01",
            "的影响呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_D6C")

    OP_A2(0x1)

    ChrTalk(    #39
        0xD,
        (
            "呀，欢迎来到\x01",
            "艾尔·雷登关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "现在游客很少,\x01",
            "可以悠闲欣赏瀑布哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBA")

    TalkEnd(0xD)
    Return()

    # Function_6_799 end

    def Function_7_DBE(): pass

    label("Function_7_DBE")

    Call(0, 8)
    Return()

    # Function_7_DBE end

    def Function_8_DC3(): pass

    label("Function_8_DC3")

    TalkBegin(0xE)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE0")
    OP_A9(0x79)
    TalkEnd(0xE)
    Return()

    label("loc_DE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF1")
    TalkEnd(0xE)
    Return()

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_EA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6A")

    ChrTalk(    #41
        0xE,
        (
            "其他的部队\x01",
            "好像发来了通讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xE,
        "难道有什么事件吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "不过，最近\x01",
            "发生事件倒也不觉得稀奇……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_E9F")

    label("loc_E6A")


    ChrTalk(    #44
        0xE,
        (
            "其他的部队\x01",
            "好像发来了通讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xE,
        "有什么事件吗？\x02",
    )

    CloseMessageWindow()

    label("loc_E9F")

    Jump("loc_147E")

    label("loc_EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F21")

    ChrTalk(    #46
        0xE,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xE,
        (
            "导力器的恢复装置\x01",
            "似乎也没有作用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "如果累了就不要勉强，\x01",
            "最好在旅店休息一下哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_F7B")

    label("loc_F21")


    ChrTalk(    #49
        0xE,
        (
            "导力器的恢复装置\x01",
            "似乎也没有作用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xE,
        (
            "既然是这样的状况，\x01",
            "可要多多注意不能勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7B")

    Jump("loc_147E")

    label("loc_F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_102F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FE1")

    ChrTalk(    #51
        0xE,
        (
            "其实雷斯顿要塞\x01",
            "好像也发生了地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xE,
        (
            "虽然没有损害，\x01",
            "听说这事还是吓一大跳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C")

    label("loc_FE1")


    ChrTalk(    #53
        0xE,
        (
            "其实雷斯顿要塞\x01",
            "好像也发生了地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xE,
        (
            "难怪那时队长他们\x01",
            "脸都青了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_102C")

    Jump("loc_147E")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_108E")

    ChrTalk(    #55
        0xE,
        (
            "司令部发来的联络\x01",
            "是经常有的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xE,
        (
            "如果次次都脸色发青\x01",
            "那可没法工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1100")

    label("loc_108E")


    ChrTalk(    #57
        0xE,
        (
            "库隆那家伙真是\x01",
            "太神经质了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        (
            "司令部发来的联络\x01",
            "是经常有的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "如果次次都脸色发青\x01",
            "那可没法工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1100")

    Jump("loc_147E")

    label("loc_1103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_11D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1160")

    ChrTalk(    #60
        0xE,
        (
            "卢安在选举，\x01",
            "而蔡斯是地震……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xE,
        (
            "不过处在中间的\x01",
            "这个关所还真平静啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D6")

    label("loc_1160")


    ChrTalk(    #62
        0xE,
        (
            "蔡斯地震的事。\x01",
            "这里也在传言呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xE,
        (
            "虽说规模好像不大\x01",
            "但感觉真诡异啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xE,
        (
            "王国居然会地震\x01",
            "实在是很少见的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_11D6")

    Jump("loc_147E")

    label("loc_11D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(    #65
        0xE,
        (
            "最近的街道\x01",
            "比以前更加危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "不要勉强，出发前\x01",
            "最好休息一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1273")

    label("loc_1234")


    ChrTalk(    #67
        0xE,
        (
            "欢迎光临。\x01",
            "来得正好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xE,
        (
            "刚才就一直犯困\x01",
            "真是没辙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1273")

    Jump("loc_147E")

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12D1")

    ChrTalk(    #69
        0xE,
        (
            "诞辰庆典的时候\x01",
            "虽然忙得够呛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xE,
        (
            "到现在回想起来，\x01",
            "还是热闹好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1315")

    label("loc_12D1")

    OP_A2(0x2)

    ChrTalk(    #71
        0xE,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xE,
        (
            "现在我们这里有很多空床，\x01",
            "随时都可以住下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1315")

    Jump("loc_147E")

    label("loc_1318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(    #73
        0xE,
        (
            "前阵子来的一家人\x01",
            "看起来真是幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "看到那样的家庭\x01",
            "我也开始憧憬了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_147E")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 5)), scpexpr(EXPR_END)), "loc_1429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13C1")

    ChrTalk(    #75
        0xE,
        (
            "家族旅行\x01",
            "真令人羡慕呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "啊啊，我也想\x01",
            "早点拥有家庭啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1426")

    label("loc_13C1")

    OP_8C(0xE, 0, 0)
    OP_4A(0xB, 255)
    OP_A2(0x2)
    OP_A2(0xA)

    ChrTalk(    #77
        0xE,
        (
            "那么3人\x01",
            "住宿一晚对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        "啊啊，就这样拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        "那么请在这边签字……\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 255)

    label("loc_1426")

    Jump("loc_147E")

    label("loc_1429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_147E")

    ChrTalk(    #80
        0xE,
        (
            "欢迎光临。\x01",
            "这里是为旅客准备的投宿设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        (
            "如果想住的话\x01",
            "请跟我说一声。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147E")

    TalkEnd(0xE)
    Return()

    # Function_8_DC3 end

    def Function_9_1482(): pass

    label("Function_9_1482")

    Call(0, 10)
    Return()

    # Function_9_1482 end

    def Function_10_1487(): pass

    label("Function_10_1487")

    TalkBegin(0xF)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A4")
    OP_A9(0x78)
    TalkEnd(0xF)
    Return()

    label("loc_14A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B5")
    TalkEnd(0xF)
    Return()

    label("loc_14B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_15C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156E")

    ChrTalk(    #82
        0xF,
        (
            "看来这状况\x01",
            "还要继续延长的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xF,
        (
            "这、这么说导力炉子\x01",
            "暂时也不能使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xF,
        (
            "过几天菜单\x01",
            "也需要重新定制了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        (
            "……作为厨师，\x01",
            "有失败的感觉，真不甘心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_15C2")

    label("loc_156E")


    ChrTalk(    #86
        0xF,
        (
            "过几天菜单\x01",
            "也需要重新定制了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xF,
        (
            "嗯，在此之前导力器\x01",
            "恢复原状才是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C2")

    Jump("loc_1B86")

    label("loc_15C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1655")

    ChrTalk(    #88
        0xF,
        (
            "没想到导力器\x01",
            "竟然不能使用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xF,
        (
            "这里还好，\x01",
            "但蔡斯一定发生大骚动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        (
            "因为那里是不管什么都用导力\x01",
            "驱动的城市嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_16B1")

    label("loc_1655")


    ChrTalk(    #91
        0xF,
        (
            "导力器不能使用，\x01",
            "蔡斯一定发生大骚动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xF,
        (
            "因为那里是不管什么都用导力\x01",
            "驱动的城市嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B1")

    Jump("loc_1B86")

    label("loc_16B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1710")

    ChrTalk(    #93
        0xF,
        (
            "利贝尔的大地\x01",
            "好像终于平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xF,
        (
            "正是这样的时候，\x01",
            "才要感谢空之女神啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B86")

    label("loc_1710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_176B")

    ChrTalk(    #95
        0xF,
        (
            "司令部好像传来了什么\x01",
            "重要的联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xF,
        (
            "这个一定\x01",
            "也是和地震相关的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B6")

    label("loc_176B")


    ChrTalk(    #97
        0xF,
        (
            "司令部好像传来了什么\x01",
            "重要的联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        (
            "副队长气势汹汹\x01",
            "飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17B6")

    Jump("loc_1B86")

    label("loc_17B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1812")

    ChrTalk(    #99
        0xF,
        (
            "蔡斯的地震\x01",
            "似乎还在持续啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        (
            "架子上的瓶子\x01",
            "最好还是整理一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1863")

    label("loc_1812")


    ChrTalk(    #101
        0xF,
        (
            "蔡斯的地震\x01",
            "似乎还在持续啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        (
            "以防扩展到这里\x01",
            "还是整理一下架子上吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1863")

    Jump("loc_1B86")

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_18C2")

    ChrTalk(    #103
        0xF,
        (
            "虽然在王国很少见，\x01",
            "地震可是很可怕的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xF,
        (
            "因为地面会突然\x01",
            "喀哒喀哒地摇晃啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B86")

    label("loc_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_191E")

    ChrTalk(    #105
        0xF,
        (
            "基恩茨副队长\x01",
            "好像在办理通行手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xF,
        (
            "嘿嘿，这可有趣了。\x01",
            "待会儿去嘲弄他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B86")

    label("loc_191E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_19DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1983")

    ChrTalk(    #107
        0xF,
        (
            "尽管如此，\x01",
            "那家人看起来好幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xF,
        (
            "感觉像是跟画里描绘的\x01",
            "理想的家庭一样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D8")

    label("loc_1983")

    OP_A2(0x3)

    ChrTalk(    #109
        0xF,
        (
            "前阵子很少有\x01",
            "来了一家子客人的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xF,
        (
            "这里离城市很远，\x01",
            "很少有客人带孩子来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D8")

    Jump("loc_1B86")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A29")

    ChrTalk(    #111
        0xF,
        "看过有名的瀑布了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xF,
        (
            "现在可以不受打扰\x01",
            "好好观赏哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B86")

    label("loc_1A29")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "◇前篇看过说服公爵的任务\x01",      # 0
            "◇没看过说服公爵的任务\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AA2"),
        (1, "loc_1AAA"),
        (SWITCH_DEFAULT, "loc_1AB2"),
    )


    label("loc_1AA2")

    OP_28(0x23, 0x3, 0x10)
    Jump("loc_1AB2")

    label("loc_1AAA")

    OP_28(0x23, 0x4, 0x10)
    Jump("loc_1AB2")

    label("loc_1AB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B2B")

    ChrTalk(    #113
        0xF,
        (
            "哎呀，你是\x01",
            "曾经来过的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xF,
        (
            "现在客人也少,\x01",
            "请好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xF,
        (
            "如果肚子饿了\x01",
            "尝尝新菜如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B86")

    label("loc_1B2B")


    ChrTalk(    #116
        0xF,
        "哎呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xF,
        (
            "现在客人也少,\x01",
            "请好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xF,
        (
            "如果肚子饿了\x01",
            "试试新菜单如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B86")

    TalkEnd(0xF)
    Return()

    # Function_10_1487 end

    def Function_11_1B8A(): pass

    label("Function_11_1B8A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDF")

    ChrTalk(    #119
        0xFE,
        (
            "非常时期还袭击学校\x01",
            "真不是人做的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "真是太过分了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1C1F")

    label("loc_1BDF")


    ChrTalk(    #121
        0xFE,
        (
            "这种非常时期\x01",
            "居然还袭击学校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "还有这种\x01",
            "过分的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1F")

    Jump("loc_2197")

    label("loc_1C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C7A")

    ChrTalk(    #123
        0xFE,
        (
            "协会派来\x01",
            "巡视的小哥很有用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "这个状况下，都不知道\x01",
            "会发生什么事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2197")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1CD9")

    ChrTalk(    #125
        0xFE,
        (
            "差不多该制订\x01",
            "面向签字仪式的警备计划了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "不提出文件\x01",
            "司令部也很烦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4B")

    label("loc_1CD9")


    ChrTalk(    #127
        0xFE,
        (
            "哟，看来地震\x01",
            "好像安定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "总算能松一口气\x01",
            "进行下一项工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "必须制订\x01",
            "面向签字仪式的警备计划了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1D4B")

    Jump("loc_2197")

    label("loc_1D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1E03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DA1")

    ChrTalk(    #130
        0xFE,
        (
            "没想到雷斯顿要塞\x01",
            "都会有地震……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "到底是没法\x01",
            "当作巧合啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E00")

    label("loc_1DA1")


    ChrTalk(    #132
        0xFE,
        (
            "没想到雷斯顿要塞\x01",
            "都会有地震……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "到底是没法\x01",
            "当作巧合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "唉，是我多心了吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1E00")

    Jump("loc_2197")

    label("loc_1E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1E62")

    ChrTalk(    #135
        0xFE,
        (
            "沃尔费堡垒之后\x01",
            "是圣海姆门吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "竟然能这样像有目的似的\x01",
            "发起地震吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED2")

    label("loc_1E62")


    ChrTalk(    #137
        0xFE,
        (
            "沃尔费堡垒之后\x01",
            "圣海姆门发生地震啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "哦，这么说\x01",
            "还忘了蔡斯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "那个城市好像\x01",
            "也发生地震了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1ED2")

    Jump("loc_2197")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1F30")

    ChrTalk(    #140
        0x10,
        (
            "最近沃尔费堡垒\x01",
            "好像地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10,
        (
            "在那里当副队长的\x01",
            "格温和我是同期呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7F")

    label("loc_1F30")


    ChrTalk(    #142
        0x10,
        (
            "最近沃尔费堡垒\x01",
            "好像地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10,
        (
            "嘿嘿，那里的士兵们\x01",
            "想必也惊慌失措吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1F7F")

    Jump("loc_2197")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_202D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1FD8")

    ChrTalk(    #144
        0x10,
        (
            "为什么当副队长的我\x01",
            "会在前台……是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x10,
        "……唉，一言难尽啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_202A")

    label("loc_1FD8")

    OP_A2(0x4)

    ChrTalk(    #146
        0x10,
        (
            "王立学院里\x01",
            "有犯罪组织的人员潜伏吗?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        (
            "总觉得这个事件，\x01",
            "好像还有幕后啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202A")

    Jump("loc_2197")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_20C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_205D")

    ChrTalk(    #148
        0xFE,
        (
            "尼克斯的话好像\x01",
            "是真的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BE")

    label("loc_205D")

    OP_A2(0x4)

    ChrTalk(    #149
        0xFE,
        (
            "从队长那儿听说了，\x01",
            "尼克斯的话好像是真的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "呀～真伤脑筋。\x01",
            "我还狠狠地训了他一顿呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BE")

    Jump("loc_2197")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_211E")

    ChrTalk(    #151
        0xFE,
        (
            "我们的士兵\x01",
            "最近很懈怠啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "明明情报部的余党\x01",
            "和空贼团都还没抓住呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2197")

    label("loc_211E")

    OP_A2(0x4)

    ChrTalk(    #153
        0xFE,
        (
            "我们的士兵\x01",
            "最近很懈怠啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "前阵子还有人在站岗中睡大觉，\x01",
            "真是个闹得满城风雨的白痴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "真是要想想办法了。\x02",
    )

    CloseMessageWindow()

    label("loc_2197")

    TalkEnd(0x10)
    Return()

    # Function_11_1B8A end

    def Function_12_219B(): pass

    label("Function_12_219B")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_225B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_220F")

    ChrTalk(    #156
        0xFE,
        (
            "话说回来，这个关所\x01",
            "是正适合读书的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "和王都的咖啡店一样，\x01",
            "我可是给五星评价的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2258")

    label("loc_220F")


    ChrTalk(    #158
        0xFE,
        (
            "察觉到的时候\x01",
            "已经待了很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "那么，差不多该\x01",
            "准备回王都了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2258")

    Jump("loc_266F")

    label("loc_225B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_22E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_22A9")

    ChrTalk(    #160
        0xFE,
        (
            "哎，也好。\x01",
            "反正和我没什么关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "好了，专心读书吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E5")

    label("loc_22A9")


    ChrTalk(    #162
        0xFE,
        (
            "总觉得士兵们\x01",
            "的行动很慌张呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_22E5")

    Jump("loc_266F")

    label("loc_22E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2336")

    ChrTalk(    #164
        0xFE,
        (
            "哎，也好。\x01",
            "反正和我没什么关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "好了，专心读书吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2381")

    label("loc_2336")


    ChrTalk(    #166
        0xFE,
        (
            "嗯～沃尔费堡垒\x01",
            "发生地震了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "那个士兵\x01",
            "声音好像稍微大了点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2381")

    Jump("loc_266F")

    label("loc_2384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_23E4")

    ChrTalk(    #168
        0xFE,
        (
            "唔，不知为何感觉好像\x01",
            "比平常更能集中精神读书了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "远方回响的水声\x01",
            "好像不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266F")

    label("loc_23E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_24CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2447")

    ChrTalk(    #170
        0xFE,
        (
            "我经常在王都的咖啡店里\x01",
            "读书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "好像在这样有开放感的地方\x01",
            "读书也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C7")

    label("loc_2447")

    OP_A2(0x5)

    ChrTalk(    #172
        0xFE,
        (
            "我经常在王都的咖啡店里\x01",
            "读书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "好像在这样有开放感的地方\x01",
            "读书也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "即使读同样的文章\x01",
            "感受的印象也不一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C7")

    Jump("loc_266F")

    label("loc_24CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_2566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2506")

    ChrTalk(    #175
        0xFE,
        (
            "看着幸福的家庭\x01",
            "我也感受到幸福的心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2563")

    label("loc_2506")

    OP_A2(0x5)

    ChrTalk(    #176
        0xFE,
        (
            "哈哈，正觉着热闹呢，\x01",
            "原来有人带孩子来了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "看起来真开心啊。\x01",
            "好久没来旅行了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2563")

    Jump("loc_266F")

    label("loc_2566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_266F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_25C5")

    ChrTalk(    #178
        0xFE,
        (
            "虽然在利贝尔通讯\x01",
            "看过照片……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "若不真正站在这里\x01",
            "就感受不到这魄力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266F")

    label("loc_25C5")

    OP_A2(0x5)

    ChrTalk(    #180
        0xFE,
        (
            "听说选举期间，卢安的旅游景点\x01",
            "到处都闲置着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "我正打算悠闲地读读书，\x01",
            "就从王都赶来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "话虽如此……\x01",
            "这瀑布真的是很壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "水声好像在身体中回响呢。\x02",
    )

    CloseMessageWindow()

    label("loc_266F")

    TalkEnd(0x11)
    Return()

    # Function_12_219B end

    def Function_13_2673(): pass

    label("Function_13_2673")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_27D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_26FB")

    ChrTalk(    #184
        0xFE,
        (
            "王都之旅就推迟一点，\x01",
            "先去哈肯大门吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "虽说如此，利贝尔的珍珠\x01",
            "格兰赛尔城也难以舍弃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "呜～真头痛啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D0")

    label("loc_26FB")


    ChrTalk(    #187
        0xFE,
        "嗯～接着去哪里呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "圣海姆门也不错，\x01",
            "但也想看看格兰赛尔城呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "但是，王都有签字仪式\x01",
            "警备可能很严格呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "这样的话干脆去柏斯的\x01",
            "哈肯大门看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "作为百日战役史迹巡游旅，\x01",
            "哈肯大门不可或缺哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_27D0")

    Jump("loc_2B0C")

    label("loc_27D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_28E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_285B")

    ChrTalk(    #192
        0xFE,
        (
            "卡鲁迪亚隧道\x01",
            "也想走一次看看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "不过从卢安乘定期船\x01",
            "要放心很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "这还是和茉莉商量一下\x01",
            "再决定比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E1")

    label("loc_285B")


    ChrTalk(    #195
        0xFE,
        (
            "之后虽然打算去\x01",
            "蔡斯地区……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "一考虑发现必须通过\x01",
            "卡鲁迪亚隧道才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "虽然也想走一次看看，\x01",
            "嗯～但还是觉得有点恐怖呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_28E1")

    Jump("loc_2B0C")

    label("loc_28E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_295E")

    ChrTalk(    #198
        0xFE,
        (
            "最近，茉莉经常看\x01",
            "利贝尔通讯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "但是都只看照片\x01",
            "却不读报道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "因为她实在是\x01",
            "不喜欢印刷字嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_295E")


    ChrTalk(    #201
        0xFE,
        (
            "最近，茉莉经常看\x01",
            "利贝尔通讯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "但是都只看照片\x01",
            "却不读报道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "书迷的我正好相反，\x01",
            "她很讨厌印刷字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "孩提时代还经常一起\x01",
            "看图画书来着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "到底在哪里\x01",
            "分道扬镳了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2A18")

    Jump("loc_2B0C")

    label("loc_2A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2A8A")

    ChrTalk(    #206
        0xFE,
        (
            "我们正循着百日战役\x01",
            "这条线在巡游史迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "艾尔·雷登关所\x01",
            "是和书里写的一样美丽的地方哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B0C")

    label("loc_2A8A")


    ChrTalk(    #208
        0xFE,
        (
            "呼～这里就是\x01",
            "那个艾尔·雷登啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "历史悠久的石筑建筑物\x01",
            "和罗蔡水道的瀑布……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "呀～真是和书里写的一样\x01",
            "美丽的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2B0C")

    TalkEnd(0x12)
    Return()

    # Function_13_2673 end

    def Function_14_2B10(): pass

    label("Function_14_2B10")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2B70")

    ChrTalk(    #211
        0xFE,
        (
            "去哈肯大门\x01",
            "说不定是个好主意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "好难得来到这里，\x01",
            "才有这种感觉的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE6")

    label("loc_2B70")


    ChrTalk(    #213
        0xFE,
        (
            "雪白的格兰赛尔城啊。\x01",
            "真想把它拍下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "但是圣海姆门\x01",
            "也确实很有魅力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "从亚宁堡上\x01",
            "一览平原一定很棒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2BE6")

    Jump("loc_2E7C")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2C4E")

    ChrTalk(    #216
        0xFE,
        (
            "瀑布那样运动的\x01",
            "拍摄对象果然很难拍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "利贝尔通讯的摄影记者\x01",
            "是怎样做的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCE")

    label("loc_2C4E")


    ChrTalk(    #218
        0xFE,
        (
            "瀑布那样运动的\x01",
            "拍摄对象果然很难拍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "想表现出跃动感，\x01",
            "却变成模模糊糊的照片……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "拘泥焦点的话\x01",
            "又会丧失速度感。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2CCE")

    Jump("loc_2E7C")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(    #221
        0xFE,
        "利贝尔通讯的照片真厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "要是能拍成那样\x01",
            "就毫无怨言了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_2D27")


    ChrTalk(    #223
        0xFE,
        "利贝尔通讯的照片真厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "要是能拍成那样\x01",
            "就毫无怨言了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "这么说来以前的利贝尔通讯\x01",
            "有这个关所的照片呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "好，我也要拍出\x01",
            "不输给那个的照片。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2DC9")

    Jump("loc_2E7C")

    label("loc_2DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2E25")

    ChrTalk(    #227
        0xFE,
        (
            "我的梦想\x01",
            "是成为摄影记者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "此次的史迹巡游\x01",
            "也是为此修行的一环。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2E25")


    ChrTalk(    #229
        0xFE,
        (
            "和青梅竹马的提克一起\x01",
            "在做史迹巡游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "多多拍摄有名的建筑物\x01",
            "磨练拍摄手法哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2E7C")

    TalkEnd(0x13)
    Return()

    # Function_14_2B10 end

    def Function_15_2E80(): pass

    label("Function_15_2E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2FAC")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F48")

    ChrTalk(    #231
        0xFE,
        (
            "正好学院事件\x01",
            "刚刚发来了联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "据说平安的解决了，\x01",
            "本该感到喜悦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "但乘着这阵混乱再引起的骚动\x01",
            "以后说不定还会发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "所以大家都不能松懈，\x01",
            "还需要继续严格警戒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2FA6")

    label("loc_2F48")


    ChrTalk(    #235
        0xFE,
        (
            "像学院事件一样的骚动\x01",
            "以后说不定还会发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "所以大家都不能松懈，\x01",
            "还需要继续严格警戒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA6")

    TalkEnd(0x9)
    Jump("loc_38E7")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_30E7")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308F")

    ChrTalk(    #237
        0xFE,
        (
            "通信机虽说恢复原状了，\x01",
            "但情报还不足……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "总之强化关所的警备\x01",
            "是最优先的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "因为大门持续\x01",
            "关不上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "卡鲁迪亚隧道的照明也灭了，\x01",
            "现在是一片漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "草率进入会要人命的。\x01",
            "请充分注意。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_30E1")

    label("loc_308F")


    ChrTalk(    #242
        0xFE,
        (
            "现在确保关所的安全\x01",
            "是最优先的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "我们慌慌张张的\x01",
            "只能让市民更加动摇。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E1")

    TalkEnd(0x9)
    Jump("loc_38E7")

    label("loc_30E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 2)), scpexpr(EXPR_END)), "loc_38E3")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3191")

    ChrTalk(    #244
        0x9,
        (
            "配合签字仪式的日期\x01",
            "关所也将强化警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "不仅仅是那个犯罪组织，\x01",
            "情报部的残存势力也令人在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        (
            "王国军的上层部\x01",
            "会变得神经质也是当然。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_3191")


    ChrTalk(    #247
        0x9,
        (
            "连续发生的地震\x01",
            "也已经平息下来的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x9,
        (
            "要塞似乎也没有受到太大的损坏，\x01",
            "不管怎样，可以安心一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        (
            "这下总算平息了，条约签字仪式的\x01",
            "准备工作也能顺利进行下去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_323F")

    Jump("loc_38DD")

    label("loc_3242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_331D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3298")

    ChrTalk(    #250
        0x9,
        (
            "雷斯顿要塞\x01",
            "据说有很强的地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x9,
        "虽说还好没有受到什么损害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_331A")

    label("loc_3298")


    ChrTalk(    #252
        0x9,
        (
            "据说雷斯顿要塞\x01",
            "遭遇了很强的地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "现在正好这边也\x01",
            "刚刚有联络哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x9,
        (
            "虽然有不祥的预感，\x01",
            "但是没有想到真的成为现实……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_331A")

    Jump("loc_38DD")

    label("loc_331D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_33E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_336E")

    ChrTalk(    #255
        0x9,
        (
            "圣海姆门也\x01",
            "好像地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x9,
        (
            "不知为何，\x01",
            "总有种不祥的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E6")

    label("loc_336E")


    ChrTalk(    #257
        0x9,
        (
            "圣海姆门也\x01",
            "好像地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x9,
        (
            "沃尔费堡垒之后，\x01",
            "在军队设施这是第二次了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x9,
        (
            "为何不知道，\x01",
            "有种很糟糕的预感哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_33E6")

    Jump("loc_38DD")

    label("loc_33E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_34D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3454")

    ChrTalk(    #260
        0x9,
        (
            "关于那个犯罪组织\x01",
            "王国军也开始了调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x9,
        (
            "为了不引起市民的不安，\x01",
            "搜查是秘密进行的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CD")

    label("loc_3454")


    ChrTalk(    #262
        0x9,
        "哦哦，游击士的各位啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "关于那个犯罪组织\x01",
            "王国军也在调查呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x9,
        (
            "为了不引起市民的不安，\x01",
            "单纯是秘密搜查而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_34CD")

    Jump("loc_38DD")

    label("loc_34D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_35BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3531")

    ChrTalk(    #265
        0xFE,
        (
            "那个事件\x01",
            "总算也解决了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "虽然还有些疑惑，\x01",
            "但现在就让我说声辛苦了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B7")

    label("loc_3531")

    OP_A2(0x0)

    ChrTalk(    #267
        0xFE,
        (
            "呀，那个事件\x01",
            "总算解决了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "话说回来，犯罪组织的一员\x01",
            "竟然潜伏在王立学院……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "真没想到幽灵骚乱\x01",
            "竟然联系着这样的事件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B7")

    Jump("loc_38DD")

    label("loc_35BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_36A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3611")

    ChrTalk(    #270
        0xFE,
        (
            "我们也会致力于\x01",
            "增加与协会的合作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "也请各位游击士\x01",
            "多多配合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_369D")

    label("loc_3611")

    OP_A2(0x0)

    ChrTalk(    #272
        0xFE,
        (
            "哎呀，是你们啊。\x01",
            "幽灵骚动的调查有进展吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "这边如果掌握了什么\x01",
            "也会马上联系协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "这样的搜查\x01",
            "军队和协会的合作是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369D")

    Jump("loc_38DD")

    label("loc_36A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_3833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3701")

    ChrTalk(    #275
        0xFE,
        (
            "还以为尼克斯那家伙\x01",
            "一定是睡迷糊了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "嗯～这个债\x01",
            "看来不得不找机会还了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3830")

    label("loc_3701")

    OP_A2(0x0)

    ChrTalk(    #277
        0xFE,
        "得到什么情报了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#1000F嗯，看来好像\x01",
            "真的出现了什么。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_376B")

    ChrTalk(    #279
        0x106,
        "#050F虽然还不清楚原形。\x02",
    )

    Jump("loc_378D")

    label("loc_376B")


    ChrTalk(    #280
        0x103,
        "#020F嗯嗯，虽然还不清楚原形。\x02",
    )


    label("loc_378D")

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "唔～是吗……\x01",
            "对不起尼克斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "这个债\x01",
            "不得不找机会还啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1000F那么，我们\x01",
            "就这样继续调查了。\x02\x03",

            "队长，今天谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "啊啊，查出什么的话\x01",
            "请再联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3830")

    Jump("loc_38DD")

    label("loc_3833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_38DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_387F")

    ChrTalk(    #285
        0xFE,
        "隧道入口在关所屋顶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "请沿着柜台旁边的\x01",
            "台阶上去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DD")

    label("loc_387F")

    OP_A2(0x0)

    ChrTalk(    #287
        0xFE,
        (
            "目击了白影的\x01",
            "是名叫尼克斯的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "他现在在卡鲁迪亚隧道\x01",
            "入口放哨\x01",
            "直接问他就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DD")

    TalkEnd(0x9)
    Jump("loc_38E7")

    label("loc_38E3")

    Call(0, 19)

    label("loc_38E7")

    Return()

    # Function_15_2E80 end

    def Function_16_38E8(): pass

    label("Function_16_38E8")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3914")

    ChrTalk(    #289
        0xA,
        "#260F下次碰到再一起玩哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_3914")

    OP_A2(0x9)

    ChrTalk(    #290
        0xA,
        (
            "#260F啊，是姐姐你们啊。\x01",
            "下次再一起玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3945")

    TalkEnd(0xA)
    Return()

    # Function_16_38E8 end

    def Function_17_3949(): pass

    label("Function_17_3949")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_398B")

    ChrTalk(    #291
        0xB,
        (
            "#1363F这次是偶尔\x01",
            "服务家族啦。\x02\x03",

            "平时总是出差嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F1")

    label("loc_398B")

    OP_8C(0xFE, 180, 0)
    OP_4A(0xE, 255)
    OP_A2(0xA)
    OP_A2(0x2)

    ChrTalk(    #292
        0xE,
        (
            "那么３人\x01",
            "住宿一晚对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xB,
        "#1360F啊啊，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xE,
        "那么请在这边签字……\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)

    label("loc_39F1")

    TalkEnd(0xB)
    Return()

    # Function_17_3949 end

    def Function_18_39F5(): pass

    label("Function_18_39F5")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3A25")

    ChrTalk(    #295
        0xC,
        (
            "#1372F很快就完了\x01",
            "乖乖待着哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A49")

    label("loc_3A25")

    OP_A2(0xB)

    ChrTalk(    #296
        0xC,
        (
            "#1372F喂，玲。\x01",
            "乖乖待着啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A49")

    TalkEnd(0xC)
    Return()

    # Function_18_39F5 end

    def Function_19_3A4D(): pass

    label("Function_19_3A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A67")
    Call(0, 24)
    FadeToBright(0, 0)

    label("loc_3A67")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, 2980, 0, 91080, 90)
    SetChrPos(0xF7, 2410, 0, 90010, 90)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #297
        0x101,
        (
            "#1011F#5P那个，打扰一下。\x01",
            "游击士协会的…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B92")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇说服公爵事件未完成】\x01",      # 0
            "【◇说服公爵事件完成】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B79"),
        (1, "loc_3B81"),
        (SWITCH_DEFAULT, "loc_3B89"),
    )


    label("loc_3B79")

    OP_28(0x23, 0x3, 0x10)
    Jump("loc_3B89")

    label("loc_3B81")

    OP_28(0x23, 0x4, 0x10)
    Jump("loc_3B89")

    label("loc_3B89")

    FadeToBright(300, 0)

    label("loc_3B92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C6E")

    ChrTalk(    #298
        0x9,
        "啊啊，辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #299
        0x9,
        (
            "啊，记得你是\x01",
            "上次公爵阁下来时的那位游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        (
            "#1016F#5P啊哈哈。\x01",
            "还记得啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x9,
        (
            "那当然，从没像那时一样\x01",
            "感受到你们游击士\x01",
            "的可贵嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x9,
        "今天什么事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CAD")

    label("loc_3C6E")

    SetChrName("哈恩队长")

    ChrTalk(    #303
        0x9,
        "啊啊，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x9,
        (
            "没见过你啊，\x01",
            "今天有什么事？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CAD")


    ChrTalk(    #305
        0x101,
        (
            "#1002F#5P其实，听说这个关所\x01",
            "有士兵看见了『白影』，\x01",
            "好像就是你部队里的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x9,
        (
            "怎么，都传到\x01",
            "协会那儿去了吗?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x9,
        (
            "真是丢脸啊。\x01",
            "太难为情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#1004F#5P难为情？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x9,
        (
            "当然是睡糊涂了，\x01",
            "才说看见幽灵啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x9,
        (
            "如此松懈怠慢,\x01",
            "一旦出事可要出人命啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x9,
        (
            "而部下的松懈\x01",
            "也是我当队长的责任。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E28")

    ChrTalk(    #312
        0x106,
        (
            "#053F真不巧，这是\x01",
            "你武断行事了。\x02\x03",

            "#050F那个幽灵，在卢安各地\x01",
            "都有被目击呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E80")

    label("loc_3E28")


    ChrTalk(    #313
        0x103,
        (
            "#020F哎呀，这可是\x01",
            "队长武断行事了。\x02\x03",

            "关于那个幽灵\x01",
            "现在卢安各地\x01",
            "好像都有人目击到哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E80")


    ChrTalk(    #314
        0x9,
        "什么……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #315
        (
            "\x07\x05把嘉恩拜托调查的事\x01",
            "向哈恩队长说明了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #316
        0x9,
        (
            "是这样吗?\x01",
            "我还以为一定是\x01",
            "睡糊涂了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x9,
        (
            "看来，这确实\x01",
            "是我主观臆断了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x9,
        "对不起尼克斯了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#1011F#5P尼克斯就是\x01",
            "目击了白影的士兵？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x9,
        "啊啊，对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x9,
        (
            "他现在在卡鲁迪亚隧道\x01",
            "入口处放哨，\x01",
            "直接问他就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x9,
        (
            "请你们跟他说\x01",
            "我相信他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1006F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_4B(0x9, 255)
    OP_A2(0x1212)
    OP_28(0x82, 0x2, 0x2)
    OP_28(0x82, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_19_3A4D end

    def Function_20_400C(): pass

    label("Function_20_400C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401D")
    Call(0, 24)

    label("loc_401D")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-8390, 1000, 6270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -3410, 0, 19050, 270)
    SetChrPos(0xB, -1990, 0, 20610, 225)
    SetChrPos(0xC, -1260, 0, 19050, 270)
    OP_8C(0x0, 90, 0)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    SetChrPos(0x101, -7600, 3000, 8050, 149)
    SetChrPos(0xF7, -8180, 3000, 8050, 180)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_43(0x101, 0x0, 0x0, 0x16)
    Sleep(600)
    OP_43(0xF7, 0x0, 0x0, 0x17)

    def lambda_4107():
        OP_6D(-3350, 0, 5190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4107)

    def lambda_411F():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_411F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    NpcTalk(    #324
        0xA,
        "少女的声音",
        "#6P哇，好厉害哦！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #325
        0xA,
        "少女的声音",
        "#6P爸爸、妈妈，这边哦！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x0)

    def lambda_4195():
        OP_6D(-2740, 0, 19390, 3000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4195)

    def lambda_41AD():
        OP_67(0, 4890, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_41AD)

    def lambda_41C5():
        OP_6B(3330, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_41C5)

    def lambda_41D5():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_41D5)
    TurnDirection(0x101, 0xA, 400)
    TurnDirection(0xF7, 0xA, 400)
    WaitChrThread(0xB, 0x1)

    def lambda_41F8():
        TurnDirection(0xB, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_41F8)
    WaitChrThread(0xC, 0x1)

    def lambda_420B():
        TurnDirection(0xC, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_420B)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xA, 0x3)

    NpcTalk(    #326
        0xB,
        "男性",
        (
            "#1363F#2P喂喂，跑那么快\x01",
            "当心跌倒哦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #327
        0xC,
        "女性",
        (
            "#1371F#6P哈哈哈。\x01",
            "但是真的好漂亮嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 400)
    Sleep(300)

    NpcTalk(    #328
        0xC,
        "女性",
        (
            "#1372F#6P谢谢你，老公。\x01",
            "能带我们一起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    Sleep(300)

    NpcTalk(    #329
        0xB,
        "男性",
        (
            "#1361F#2P哪里，总是让你们\x01",
            "感到寂寞嘛。\x02\x03",

            "这是应该有的家庭责任啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -2060, 0, 7000, 0)
    SetChrPos(0xF7, -850, 0, 5500, 0)

    def lambda_4348():
        OP_6D(-2390, 0, 14690, 1800)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4348)

    def lambda_4360():
        OP_67(0, 4890, -10000, 1800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4360)
    Sleep(1000)

    def lambda_437D():
        OP_8E(0x101, 0xFFFFF858, 0x0, 0x23BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_437D)

    def lambda_4398():
        OP_8E(0xF7, 0xFFFFFE84, 0x0, 0x20F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4398)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0xF7, 0xA, 0)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #330
        0x101,
        (
            "#1017F#5P（嗯～\x01",
            "　关系很好的家庭呢。)\x02\x03",

            "(是来旅行的吧？)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4456")

    ChrTalk(    #331
        0x106,
        (
            "#051F#6P（啊啊，看起来是呢。）\x02\x03",

            "(说不定\x01",
            " 是从外国来的呢。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4499")

    label("loc_4456")


    ChrTalk(    #332
        0x103,
        (
            "#021F#6P（呵呵，大概是吧。）\x02\x03",

            "#020F（说不定\x01",
            "　还是外国人呢。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4499")

    OP_A2(0x1214)

    NpcTalk(    #333
        0xA,
        "女孩子",
        (
            "#261F#8P哇……\x01",
            "好厉害啊。\x02\x03",

            "只是看着\x01",
            "就感觉要被吸引过去一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    NpcTalk(    #334
        0xA,
        "女孩子",
        (
            "#265F#8P对了，这位姐姐。\x02\x03",

            "这个瀑布叫什么名字？\x02\x03",

            "这么多水\x01",
            "是从哪儿来的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        "#1016F#5P哟，突然袭击啊。\x02",
    )

    CloseMessageWindow()

    def lambda_4583():
        OP_6D(-3310, 0, 18760, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4583)

    def lambda_459B():
        OP_67(0, 4890, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_459B)

    def lambda_45B3():
        OP_8E(0x101, 0xFFFFF506, 0x0, 0x4286, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45B3)

    def lambda_45CE():
        TurnDirection(0xB, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_45CE)
    TurnDirection(0xC, 0x101, 400)

    def lambda_45E3():
        OP_8E(0xF7, 0xFFFFFC22, 0x0, 0x3E58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_45E3)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    OP_44(0xB, 0x0)
    OP_44(0xB, 0x1)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #336
        0x101,
        (
            "#1006F#6P这瀑布叫『艾尔·雷登』哦。\x02\x03",

            "是从瓦雷利亚湖，通过太古的水道\x01",
            "流到这里来的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #337
        0xA,
        "女孩子",
        (
            "#265F#5P瓦雷利亚湖我知道的！\x02\x03",

            "飞船到达之前看到的\x01",
            "很大很大的湖对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1004F#6P嗯，是啊……#1990W #20W \x01",
            "#1000F难道你们是从外国来的？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0xA,
        "女孩子",
        (
            "#264F#5P说玲吗？\x02\x03",

            "#263F嗯嗯，是啊。\x01",
            "玲是从很远的地方来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#1001F#6P是吗。　\x01",
            "你叫玲啊。\x02\x03",

            "好可爱的名字哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xA,
        (
            "#261F#5P哈哈哈，是吧？\x02\x03",

            "因为是爸爸和妈妈\x01",
            "给取的名字嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)
    Sleep(300)

    ChrTalk(    #342
        0xC,
        (
            "#1372F#4P玲，给姐姐\x01",
            "添麻烦可不行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xB,
        (
            "#1363F哈哈，不好意思。\x01",
            "尽给素不相识的人添麻烦……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 400)

    ChrTalk(    #344
        0xA,
        (
            "#262F#5P哼～\x01",
            "玲才没有添麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        (
            "#1016F#6P啊哈哈。\x01",
            "请别介意。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_48AB")

    ChrTalk(    #346
        0x106,
        (
            "#051F#6P你们好像是从外国来的，\x01",
            "是来利贝尔旅行的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48DA")

    label("loc_48AB")


    ChrTalk(    #347
        0x103,
        (
            "#020F#6P你们好像是外国人，\x01",
            "来利贝尔旅行？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48DA")

    TurnDirection(0xC, 0xF7, 400)

    ChrTalk(    #348
        0xB,
        (
            "#1361F嗯嗯，我是贸易商人\x01",
            "经常会来利贝尔。\x02\x03",

            "每次来访，都对这个国家的美丽\x01",
            "惊叹不已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xC,
        (
            "#1370F#4P所以这次，正好有商谈\x01",
            "就顺便把我和女儿都带来了。\x02\x03",

            "#1371F呵呵，很少有呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1017F#6P啊哈哈……\x01",
            "真好啊，家庭关系这么好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #351
        0xA,
        (
            "#261F#5P哈哈哈，羡慕吧？\x02\x03",

            "#265F爸爸虽然经常出差\x01",
            "但总会买很多\x01",
            "土产回来……\x02\x03",

            "妈妈平时也都笑眯眯的\x01",
            "制作好吃的饭菜哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        (
            "#1008F#6P这样啊。\x01",
            "嗯～姐姐好羡慕哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xB,
        "#1363F哈哈，真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xC,
        (
            "#1372F#4P不好意思……\x01",
            "她还这么孩子气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xA,
        (
            "#260F#5P唔～能告诉我名字吗？\x02\x03",

            "玲要怎么\x01",
            "称呼姐姐呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        (
            "#1006F#6P哦，被问到姓名\x01",
            "不回答可就失礼了呢。\x02\x03",

            "我叫艾丝蒂尔。\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "#1015F是游击士……\x01",
            "嗯～游击士你知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xA,
        (
            "#266F#5P真是的，别当我是小孩子！\x02\x03",

            "#265F不过姐姐\x01",
            "是游击士啊。\x02\x03",

            "可以消灭\x01",
            "可怕的魔兽吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1006F#6P嗯，有时候会吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xB,
        (
            "#1362F哦……\x01",
            "是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        (
            "#1371F#4P小小年纪就当上游击士\x01",
            "实在是很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "还只是个新人而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4CC4")

    ChrTalk(    #362
        0x106,
        (
            "#051F#6P利贝尔各都市\x01",
            "都有协会的支部。\x02\x03",

            "如果旅行中，有什么困难\x01",
            "随时都可以去求助。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D18")

    label("loc_4CC4")


    ChrTalk(    #363
        0x103,
        (
            "#020F#6P利贝尔五大都市\x01",
            "都有协会的支部。\x02\x03",

            "如果旅行中，有什么困难\x01",
            "请随时去求助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D18")


    ChrTalk(    #364
        0xB,
        (
            "#1361F多谢照顾了。\x02\x03",

            "#1360F……那么我们\x01",
            "去办住宿手续了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #365
        0xC,
        "#1370F#4P来，玲，要走了哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 400)

    ChrTalk(    #366
        0xA,
        (
            "#262F#5P呜～还想和姐姐\x01",
            "多聊会儿呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(    #367
        0xA,
        (
            "#265F#5P还有哦，姐姐。\x01",
            "下次碰到了再一起玩哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        "#1006F#6P嗯，好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xA,
        (
            "#261F#5P哈哈哈，好高兴哦。\x02\x03",

            "#265F再见哦，艾丝蒂尔姐姐。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E48():

        label("loc_4E48")

        TurnDirection(0x101, 0xA, 0)
        OP_48()
        Jump("loc_4E48")

    QueueWorkItem2(0x101, 1, lambda_4E48)

    def lambda_4E59():

        label("loc_4E59")

        TurnDirection(0xF7, 0xB, 0)
        OP_48()
        Jump("loc_4E59")

    QueueWorkItem2(0xF7, 1, lambda_4E59)
    OP_43(0xB, 0x1, 0x0, 0x15)
    Sleep(1000)

    def lambda_4E76():
        OP_6D(-1800, 0, 18780, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4E76)

    def lambda_4E8E():
        OP_67(0, 4890, -10000, 200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4E8E)
    OP_43(0xC, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0x15)
    Sleep(200)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F55")
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇『听过孤儿院孩子们的话』状态】\x01",      # 0
            "【◇不变更】\x01",                            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F4C")
    OP_A2(0x121A)

    label("loc_4F4C")

    FadeToBright(300, 0)

    label("loc_4F55")

    OP_69(0x101, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5112")

    ChrTalk(    #370
        0x106,
        (
            "#051F#6P真老成的小鬼啊。\x02\x03",

            "比提妲\x01",
            "还小一两岁的样子吗?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        (
            "#1017F#5P嗯，差不多吧。\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(400)

    ChrTalk(    #372
        0x106,
        (
            "#050F#6P怎么了。\x01",
            "想起大叔了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #373
        0x101,
        (
            "#1016F#5P嘿嘿……有点。\x02\x03",

            "#1025F还有，初遇约修亚的时候，\x01",
            "差不多也是那孩子那么大的时候呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_50CA")
    OP_28(0x82, 0x1, 0x400)

    ChrTalk(    #374
        0x106,
        (
            "#053F#6P是吗……\x02\x03",

            "#051F……目击情报全部收集到了,\x01",
            "差不多该回卢安了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_510F")

    label("loc_50CA")


    ChrTalk(    #375
        0x106,
        (
            "#053F#6P是吗……\x02\x03",

            "#051F……好了。\x01",
            "赶快去问问\x01",
            "下一条目击情报吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_510F")

    Jump("loc_52B5")

    label("loc_5112")


    ChrTalk(    #376
        0x103,
        (
            "#021F#6P哈哈哈。\x01",
            "好老成的女孩子啊。\x02\x03",

            "比提妲\x01",
            "稍微小一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#1017F#5P嗯，差不多吧。\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(400)

    ChrTalk(    #378
        0x103,
        (
            "#027F#6P呵呵。\x01",
            "想起老师的事了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(400)

    ChrTalk(    #379
        0x101,
        (
            "#1016F#5P嘿嘿……有点。\x02\x03",

            "#1025F还有，遇到约修亚\x01",
            "差不多也是那孩子那么大的时候呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_5275")
    OP_28(0x82, 0x1, 0x400)

    ChrTalk(    #380
        0x103,
        (
            "#026F#6P……是啊。\x02\x03",

            "#020F目击情报全部收集到了,\x01",
            "差不多该回卢安了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52B5")

    label("loc_5275")


    ChrTalk(    #381
        0x103,
        (
            "#026F#6P……是啊。\x02\x03",

            "#020F对了……\x01",
            "去探听下一条目击情报吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B5")


    ChrTalk(    #382
        0x101,
        "#1006F#5P嗯！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_A2(0x1215)
    EventEnd(0x0)
    Return()

    # Function_20_400C end

    def Function_21_52DA(): pass

    label("Function_21_52DA")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xA46, 0x0, 0x51F4, 0x7D0, 0x0)

    def lambda_52FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52FB)
    OP_8E(0xFE, 0xDC0, 0x0, 0x523A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_52DA end

    def Function_22_5321(): pass

    label("Function_22_5321")


    def lambda_5327():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5327)
    OP_8E(0x101, 0xFFFFE296, 0x3E8, 0x137E, 0x7D0, 0x0)
    OP_8E(0x101, 0xFFFFF326, 0x0, 0x13A6, 0x7D0, 0x0)
    Return()

    # Function_22_5321 end

    def Function_23_535C(): pass

    label("Function_23_535C")


    def lambda_5362():
        OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5362)
    OP_8E(0xF7, 0xFFFFE14C, 0x3E8, 0x10EA, 0x7D0, 0x0)
    OP_8E(0xF7, 0xFFFFF11E, 0x0, 0xECE, 0x7D0, 0x0)
    Return()

    # Function_23_535C end

    def Function_24_5397(): pass

    label("Function_24_5397")

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
        (0, "loc_5411"),
        (1, "loc_5417"),
        (SWITCH_DEFAULT, "loc_541D"),
    )


    label("loc_5411")

    OP_A2(0x1200)
    Jump("loc_541D")

    label("loc_5417")

    OP_A2(0x1201)
    Jump("loc_541D")

    label("loc_541D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_542B")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_542F")

    label("loc_542B")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_542F")

    Return()

    # Function_24_5397 end

    def Function_25_5430(): pass

    label("Function_25_5430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_553B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_54B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545B")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_5462")

    label("loc_545B")

    TurnDirection(0x106, 0x0, 400)

    label("loc_5462")


    ChrTalk(    #383
        0x106,
        (
            "#050F前边就是卢安地区了啊。\x02\x03",

            "没时间去别的地方了。\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5520")

    label("loc_54B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54C7")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_54CE")

    label("loc_54C7")

    TurnDirection(0x103, 0x0, 400)

    label("loc_54CE")


    ChrTalk(    #384
        0x103,
        (
            "#020F穿过这里就是卢安地区了吧。\x02\x03",

            "没时间去其它的地方了，\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5520")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_553B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57B4")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_55B0")

    ChrTalk(    #385
        0x108,
        (
            "#070F虽说徒步移动是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去王都\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5618")

    label("loc_55B0")


    ChrTalk(    #386
        0x108,
        (
            "#070F这边是卢安地区吗。\x02\x03",

            "虽说徒步移动是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去王都\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5618")

    Jump("loc_5799")

    label("loc_561B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_56E1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5638")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_563F")

    label("loc_5638")

    TurnDirection(0x106, 0x0, 400)

    label("loc_563F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5699")

    ChrTalk(    #387
        0x106,
        (
            "#053F……要走过去\x01",
            "说实话太浪费时间。\x02\x03",

            "#050F要去王都\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56DE")

    label("loc_5699")


    ChrTalk(    #388
        0x106,
        (
            "#050F前边就是卢安地区了啊。\x02\x03",

            "要去王都\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_56DE")

    Jump("loc_5799")

    label("loc_56E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F7")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_56FE")

    label("loc_56F7")

    TurnDirection(0x103, 0x0, 400)

    label("loc_56FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5758")

    ChrTalk(    #389
        0x103,
        (
            "#026F……要走过去\x01",
            "说实话是浪费时间。\x02\x03",

            "#020F要去王都\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5799")

    label("loc_5758")


    ChrTalk(    #390
        0x103,
        (
            "#020F这边是卢安地区吧。\x02\x03",

            "要去王都\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_5799")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_57B4")

    Return()

    # Function_25_5430 end

    def Function_26_57B5(): pass

    label("Function_26_57B5")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_26_57B5 end

    SaveToFile()

Try(main)
