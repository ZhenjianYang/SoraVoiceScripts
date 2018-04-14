from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3400   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3400.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '士兵切斯利',                           # 9
        '黛米',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵儒勒',                             # 14
        '士兵埃克托尔',                         # 15
        '安敦',                                 # 16
        '利库斯',                               # 17
        '士兵沃普',                             # 18
        '士兵欧鲁尼斯',                         # 19
        '冈多夫',                               # 20
        '利塔街道方向',                         # 21
        '庭园大道方向',                         # 22
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01750 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01750P._CP',             # 05
    )

    DeclNpc(
        X                   = 20790,
        Z                   = 11750,
        Y                   = 6470,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 10500,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 10500,
        Z                   = 0,
        Y                   = 3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 14160,
        Z                   = 13400,
        Y                   = 1650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 16520,
        Z                   = 11750,
        Y                   = -540,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 5730,
        Z                   = 0,
        Y                   = 4940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 35310,
        Z                   = 0,
        Y                   = 3610,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 40970,
        Z                   = 0,
        Y                   = 10,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -37360,
        Z                   = 0,
        Y                   = 960,
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
        X                   = 83520,
        Z                   = 0,
        Y                   = 630,
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


    DeclEvent(
        X                   = -25540,
        Y                   = -1000,
        Z                   = -4310,
        Range               = -27840,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x1F90,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = 15150,
        TriggerZ            = 11750,
        TriggerY            = 1650,
        TriggerRange        = 400,
        ActorX              = 14160,
        ActorZ              = 14750,
        ActorY              = 1650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DE",          # 00, 0
        "Function_1_45F",          # 01, 1
        "Function_2_517",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_5E2",          # 04, 4
        "Function_5_606",          # 05, 5
        "Function_6_62A",          # 06, 6
        "Function_7_64E",          # 07, 7
        "Function_8_672",          # 08, 8
        "Function_9_696",          # 09, 9
        "Function_10_6BA",         # 0A, 10
        "Function_11_EF4",         # 0B, 11
        "Function_12_F0D",         # 0C, 12
        "Function_13_F26",         # 0D, 13
        "Function_14_F3F",         # 0E, 14
        "Function_15_1372",        # 0F, 15
        "Function_16_166D",        # 10, 16
        "Function_17_1672",        # 11, 17
        "Function_18_1818",        # 12, 18
        "Function_19_1A01",        # 13, 19
        "Function_20_1E26",        # 14, 20
        "Function_21_2206",        # 15, 21
        "Function_22_2522",        # 16, 22
        "Function_23_2E7F",        # 17, 23
        "Function_24_2EC0",        # 18, 24
        "Function_25_2F59",        # 19, 25
        "Function_26_3084",        # 1A, 26
    )


    def Function_0_2DE(): pass

    label("Function_0_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 20790, 11750, 6470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_311")
    ClearChrFlags(0x13, 0x80)

    label("loc_311")

    Jump("loc_450")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_347")
    OP_43(0x8, 0x0, 0x0, 0x7)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 35300, 0, -3600, 90)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_450")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_35D")
    ClearChrFlags(0xE, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x7)
    Jump("loc_450")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_36E")
    OP_43(0x8, 0x0, 0x0, 0x7)
    Jump("loc_450")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_37F")
    OP_43(0x8, 0x0, 0x0, 0x7)
    Jump("loc_450")

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_429")
    SetChrPos(0x8, 18300, 11750, -10110, 225)
    OP_43(0x8, 0x0, 0x0, 0x3)
    SetChrPos(0xA, 17700, 11750, 12950, 270)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x4)
    SetChrPos(0xB, 17070, 11750, -190, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x5)
    SetChrPos(0xC, 29080, 11750, -1550, 90)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x6)
    SetChrPos(0xF, 16120, 11750, 5980, 270)
    SetChrPos(0x10, 16120, 11750, 4840, 0)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_450")

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_450")
    ClearChrFlags(0xE, 0x80)
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_45E")
    OP_A3(0x10F0)
    Event(0, 22)

    label("loc_45E")

    Return()

    # Function_0_2DE end

    def Function_1_45F(): pass

    label("Function_1_45F")

    OP_16(0x2, 0xFA0, 0xFFFE65D8, 0xFFFE0C00, 0x230056)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A4")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 100)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 100)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 100)
    Jump("loc_4B3")

    label("loc_4A4")

    OP_1C(0x2, 0x0, 0x1A)
    OP_1C(0x3, 0x0, 0x1A)
    OP_1C(0x4, 0x0, 0x1A)

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4C1")
    OP_64(0x0, 0x1)
    Jump("loc_4E4")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_4E4")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4D9")
    OP_64(0x0, 0x1)
    Jump("loc_4E4")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_4E4")
    OP_64(0x0, 0x1)

    label("loc_4E4")

    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_516")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_516")

    Return()

    # Function_1_45F end

    def Function_2_517(): pass

    label("Function_2_517")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_548"),
        (1, "loc_554"),
        (2, "loc_560"),
        (3, "loc_56C"),
        (4, "loc_578"),
        (5, "loc_584"),
        (6, "loc_590"),
        (SWITCH_DEFAULT, "loc_59C"),
    )


    label("loc_548")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5A8")

    label("loc_554")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5A8")

    label("loc_560")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5A8")

    label("loc_56C")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5A8")

    label("loc_578")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5A8")

    label("loc_584")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5A8")

    label("loc_590")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A8")

    label("loc_59C")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A8")

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A8")

    label("loc_5BD")

    Return()

    # Function_2_517 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E1")
    OP_8D(0xFE, 20420, -7160, 16050, -13610, 2000)
    Jump("Function_3_5BE")

    label("loc_5E1")

    Return()

    # Function_3_5BE end

    def Function_4_5E2(): pass

    label("Function_4_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_605")
    OP_8D(0xFE, 15300, 14530, 19530, 9890, 2000)
    Jump("Function_4_5E2")

    label("loc_605")

    Return()

    # Function_4_5E2 end

    def Function_5_606(): pass

    label("Function_5_606")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_629")
    OP_8D(0xFE, 15160, 2490, 19190, -2240, 2000)
    Jump("Function_5_606")

    label("loc_629")

    Return()

    # Function_5_606 end

    def Function_6_62A(): pass

    label("Function_6_62A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64D")
    OP_8D(0xFE, 30170, 1730, 27910, -3560, 2000)
    Jump("Function_6_62A")

    label("loc_64D")

    Return()

    # Function_6_62A end

    def Function_7_64E(): pass

    label("Function_7_64E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_671")
    OP_8D(0xFE, 23750, 7410, 18380, -2820, 2000)
    Jump("Function_7_64E")

    label("loc_671")

    Return()

    # Function_7_64E end

    def Function_8_672(): pass

    label("Function_8_672")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_695")
    OP_8D(0xFE, 9410, 9240, 790, -7190, 2000)
    Jump("Function_8_672")

    label("loc_695")

    Return()

    # Function_8_672 end

    def Function_9_696(): pass

    label("Function_9_696")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B9")
    OP_8D(0xFE, 38690, -4550, 43980, 4290, 2000)
    Jump("Function_9_696")

    label("loc_6B9")

    Return()

    # Function_9_696 end

    def Function_10_6BA(): pass

    label("Function_10_6BA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_7D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_780")

    ChrTalk(    #0
        0xFE,
        (
            "今天浮游岛也\x01",
            "悠哉游哉地浮在空中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "虽然那座岛出现之后\x01",
            "导力器都停止了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "不过感觉它\x01",
            "自身并不坏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "可能是我胡思乱想……\x01",
            "可我能感觉到这东西散发着崇高的气息。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7D0")

    label("loc_780")


    ChrTalk(    #4
        0xFE,
        (
            "那座浮游岛\x01",
            "给人一种神圣的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "我觉得它本身应该\x01",
            "不是什么不好的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D0")

    Jump("loc_EF0")

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886")

    ChrTalk(    #6
        0xFE,
        (
            "从这里可以模模糊糊地\x01",
            "看见那座浮游岛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "所以我总是趁闲暇时\x01",
            "观察着它……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "偶尔能看见岛上面\x01",
            "有东西哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "看上去像是建筑物，\x01",
            "不过到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_8D4")

    label("loc_886")


    ChrTalk(    #10
        0xFE,
        (
            "在那座浮游岛上能\x01",
            "看到像建筑物一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "那个\x01",
            "不过到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D4")

    Jump("loc_EF0")

    label("loc_8D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(    #12
        0xFE,
        (
            "听说在艾尔贝离宫那边\x01",
            "也出现了情报部的家伙们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "包括王都的成员一起，\x01",
            "好像全员都被抓起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_9D8")

    ChrTalk(    #14
        0xFE,
        (
            "互不侵犯条约缔结后\x01",
            "真正的和平能到来就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "可现实是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "比如我实在无法想象\x01",
            "帝国和共和国的边境问题\x01",
            "能通过谈判解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_9D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_A3C")

    ChrTalk(    #17
        0xFE,
        (
            "呼，还是警戒和巡逻这样的\x01",
            "任务能让人平静下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "就算是王国军也\x01",
            "没办法防止地震啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_AC7")

    ChrTalk(    #19
        0xFE,
        (
            "现在艾尔贝离宫\x01",
            "对普通市民也开放哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "虽然有传言说很快这里\x01",
            "就要设置警备本部了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "看样子要去离宫游览\x01",
            "也只能趁现在了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B4D")

    ChrTalk(    #22
        0xFE,
        (
            "希德中校给人的\x01",
            "印象更像是文官，\x01",
            "不过实际上战斗力也十分了得哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "特别是在魔法方面\x01",
            "可是王国军中少数精锐之一。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C12")

    label("loc_B4D")


    ChrTalk(    #24
        0xFE,
        (
            "对签字仪式进行警戒的\x01",
            "好像是雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "而且又是希德中校指挥，\x01",
            "可以说是万无一失了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "印象更像是文官，\x01",
            "中校的战斗力也十分了得哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "特别是在魔法方面\x01",
            "可是王国军中少数精锐之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C12")

    Jump("loc_EF0")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_D2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CA3")

    ChrTalk(    #28
        0xFE,
        (
            "塔顶开始闪光是在\x01",
            "诞辰庆典之后的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "不知何时起开始向天\x01",
            "升起柱子一样的光线来了\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "后来就一直能看到\x01",
            "塔顶上有光亮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2B")

    label("loc_CA3")


    ChrTalk(    #31
        0xFE,
        (
            "从这里能看到托兰特\x01",
            "平原的『红莲之塔』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "最近一直能看到\x01",
            "塔顶有光亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "我向队长也报告过了，\x01",
            "不过还是很在意那是什么光。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D2B")

    Jump("loc_EF0")

    label("loc_D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_D92")

    ChrTalk(    #34
        0xFE,
        (
            "呼，真没办法……\x01",
            "好不容易搞定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "虽然地震很罕见，\x01",
            "不过还是希望不要有第二次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_DEA")

    ChrTalk(    #36
        0xFE,
        (
            "叫黛米的女孩子\x01",
            "听说见过那个怪家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "她在食堂工作，\x01",
            "要不你们去问问？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_E2D")

    ChrTalk(    #38
        0xFE,
        "你们看看这副样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "希望能在晚饭之前\x01",
            "整理好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_EF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E7D")

    ChrTalk(    #40
        0x8,
        "爬城墙可是很危险的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "得好好提醒一下\x01",
            "那个年轻人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_E7D")


    ChrTalk(    #42
        0x8,
        (
            "爬城墙可不正常。\x01",
            "真是的，要是掉下来怎么办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "咦！？　难、难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "你、你没在想什么\x01",
            "搞怪的事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_EF0")

    TalkEnd(0x8)
    Return()

    # Function_10_6BA end

    def Function_11_EF4(): pass

    label("Function_11_EF4")

    TalkBegin(0xA)

    ChrTalk(    #45
        0xA,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_11_EF4 end

    def Function_12_F0D(): pass

    label("Function_12_F0D")

    TalkBegin(0xB)

    ChrTalk(    #46
        0xB,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_12_F0D end

    def Function_13_F26(): pass

    label("Function_13_F26")

    TalkBegin(0xC)

    ChrTalk(    #47
        0xC,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_13_F26 end

    def Function_14_F3F(): pass

    label("Function_14_F3F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1057")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1000")

    ChrTalk(    #48
        0xFE,
        (
            "飞船要是不能飞了\x01",
            "我们的责任就更大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "航空路线既然已经断绝，\x01",
            "能侵入王都的就只有东西两侧的哨所了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "就是说，只要我们的警戒万无一失，\x01",
            "就能够保证王都的安全。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1054")

    label("loc_1000")


    ChrTalk(    #51
        0xFE,
        (
            "大门倒是个问题，\x01",
            "不过说了也没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "问题是在这种状况下\x01",
            "如何对哨所进行警戒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1054")

    Jump("loc_136E")

    label("loc_1057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1132")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E5")

    ChrTalk(    #53
        0xFE,
        (
            "呀，欢迎来到\x01",
            "圣海姆门……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "……虽然想这么说，\x01",
            "不过现在不是说这种话的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "哨所里的人现在也\x01",
            "都如坐针毡呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_112F")

    label("loc_10E5")


    ChrTalk(    #56
        0xFE,
        (
            "本来是想欢迎你们的，\x01",
            "不过现在情况特殊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "旅游的话\x01",
            "请以后再来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112F")

    Jump("loc_136E")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(    #58
        0xFE,
        (
            "欢迎来到圣海姆门。\x01",
            "有事的话请进来说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136E")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11B3")

    ChrTalk(    #59
        0xFE,
        (
            "埃克托尔去帮忙以后\x01",
            "就没回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "是不是先吃饭了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1211")

    label("loc_11B3")


    ChrTalk(    #61
        0xFE,
        (
            "地震的善后\x01",
            "总算是结束了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "不过埃克托尔那家伙还没回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "是不是先吃饭了呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1211")

    Jump("loc_136E")

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_12AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_126F")

    ChrTalk(    #64
        0xFE,
        (
            "门内的大家\x01",
            "都在努力收拾残局。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "我的搭档埃克托尔\x01",
            "也急忙去帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A9")

    label("loc_126F")


    ChrTalk(    #66
        0xFE,
        "刚才摇得挺厉害。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "好久没像这样\x01",
            "感觉到危险了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12A9")

    Jump("loc_136E")

    label("loc_12AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_136E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(    #68
        0xD,
        (
            "欢迎来到圣海姆门！\x01",
            "也欢迎你们来旅游。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136E")

    label("loc_12E8")


    ChrTalk(    #69
        0xD,
        (
            "欢迎来到圣海姆门！\x01",
            "也欢迎你们来旅游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "这里是名叫『亚宁堡』的\x01",
            "古代长城的一部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "作为旅游名胜，\x01",
            "来参观的人也很多哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_136E")

    TalkEnd(0xD)
    Return()

    # Function_14_F3F end

    def Function_15_1372(): pass

    label("Function_15_1372")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_145A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1409")

    ChrTalk(    #72
        0xFE,
        (
            "就因为导力枪不能使用\x01",
            "而发牢骚的那些人真没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "反正一进入混战，\x01",
            "枪就没用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "既然如此，\x01",
            "一开始就用刺刀作战好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1457")

    label("loc_1409")


    ChrTalk(    #75
        0xFE,
        (
            "我从以前起\x01",
            "就更喜欢剑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "因为用那个才能感觉到\x01",
            "是凭自己的力量在战斗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1457")

    Jump("loc_1669")

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(    #77
        0xFE,
        (
            "导力式的门\x01",
            "怎么也放不下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "因为这里是王都防卫的中枢，\x01",
            "所以这个问题挺严重的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "不过就算有人入侵\x01",
            "我们也会把他们挡下的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1544")

    label("loc_14F6")


    ChrTalk(    #80
        0xFE,
        (
            "门关不起来这种事\x01",
            "可是闻所未闻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "不过即便如此，\x01",
            "这里还是要死守的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1544")

    Jump("loc_1669")

    label("loc_1547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_15EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15A8")

    ChrTalk(    #82
        0xFE,
        (
            "说起来很快就有\x01",
            "条约的签字仪式了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "唉，队长又要在那儿\x01",
            "嚷嚷强化警戒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E9")

    label("loc_15A8")


    ChrTalk(    #84
        0xFE,
        (
            "地震好像也\x01",
            "平息下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "旅客和我们都总算\x01",
            "能放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_15E9")

    Jump("loc_1669")

    label("loc_15EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_162B")

    ChrTalk(    #86
        0xE,
        "没事情也没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xE,
        "你们可以随意出入。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1669")

    label("loc_162B")


    ChrTalk(    #88
        0xE,
        "哟，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "如果有什么事情\x01",
            "就和里面的队长说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1669")

    TalkEnd(0xE)
    Return()

    # Function_15_1372 end

    def Function_16_166D(): pass

    label("Function_16_166D")

    Call(0, 17)
    Return()

    # Function_16_166D end

    def Function_17_1672(): pass

    label("Function_17_1672")

    SetChrName("安敦")
    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_16FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16BB")

    ChrTalk(    #90
        0xFE,
        (
            "差、差点就\x01",
            "掉下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "啊～真吓人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_16BB")


    ChrTalk(    #92
        0xFE,
        (
            "呼～呼……\x01",
            "啊～真吓人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "差、差点就\x01",
            "掉下去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_16F8")

    Jump("loc_1814")

    label("loc_16FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1773")
    SetChrSubChip(0xF, 0)

    def lambda_1714():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1714)

    ChrTalk(    #94
        0xF,
        "#3S再见了──！\x02",
    )

    CloseMessageWindow()

    def lambda_1743():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1743)

    ChrTalk(    #95
        0xF,
        "#3S我的青春──！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_1773")

    SetChrSubChip(0xF, 0)

    def lambda_177E():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_177E)

    ChrTalk(    #96
        0xF,
        "#3S诞辰庆典──！\x02",
    )

    CloseMessageWindow()

    def lambda_17AF():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_17AF)

    ChrTalk(    #97
        0xF,
        "#3S我最讨厌了───！！\x02",
    )

    CloseMessageWindow()

    def lambda_17E6():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_17E6)

    ChrTalk(    #98
        0xF,
        "#3S啊啊啊──！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1814")

    TalkEnd(0xF)
    Return()

    # Function_17_1672 end

    def Function_18_1818(): pass

    label("Function_18_1818")

    SetChrName("利库斯")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_182F")
    ClearChrFlags(0x10, 0x10)
    Jump("loc_1834")

    label("loc_182F")

    SetChrFlags(0x10, 0x10)

    label("loc_1834")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_18FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1892")

    ChrTalk(    #99
        0xFE,
        (
            "这家伙地震的时候\x01",
            "正好在爬城墙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "被震感吓着了，\x01",
            "差点就掉下去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FB")

    label("loc_1892")


    ChrTalk(    #101
        0xFE,
        (
            "如果地震再稍微大一点，\x01",
            "说不定真的就掉下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "从这一点上来说，安敦，\x01",
            "可以说你算是走运的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_18FB")

    Jump("loc_19FD")

    label("loc_18FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_19AA")

    ChrTalk(    #103
        0x10,
        (
            "我的搭档安敦在诞辰庆典的时候\x01",
            "向仰慕的女性告白了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "不过残酷的现实是他被\x01",
            "彻底地拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "再次来到这里也算\x01",
            "他好像为了断却这个念想就去爬城墙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FD")

    label("loc_19AA")


    ChrTalk(    #106
        0x10,
        (
            "安敦…\x01",
            "那边是蔡斯的方向啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "如果你恨诞辰庆典的话\x01",
            "至少要面向王都吼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_19FD")

    TalkEnd(0x10)
    Return()

    # Function_18_1818 end

    def Function_19_1A01(): pass

    label("Function_19_1A01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1AEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAE")

    ChrTalk(    #108
        0xFE,
        (
            "虽、虽然前辈们\x01",
            "都泰然自若……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "不过我还是感到不安啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "因为要在不能使用枪的状态下\x01",
            "把守这样的平地地形。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "能不能至少\x01",
            "安排一点路障啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1AE9")

    label("loc_1AAE")


    ChrTalk(    #112
        0xFE,
        (
            "虽、虽然前辈们\x01",
            "都泰然自若……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "我感到还是不安啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1AE9")

    Jump("loc_1E22")

    label("loc_1AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC1")

    ChrTalk(    #114
        0xFE,
        (
            "我是王都那边的门卫，\x01",
            "不过现在过来这边支援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "是为了强化外侧的\x01",
            "蔡斯这边的警戒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "能和儒勒前辈以及埃克托尔前辈\x01",
            "一起站岗真是荣幸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "他们两人都是传闻要光荣\x01",
            "调往亲卫队的人物哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1C10")

    label("loc_1BC1")


    ChrTalk(    #118
        0xFE,
        "今天我是来支援蔡斯这边的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "啊，能和我崇拜的前辈们\x01",
            "一起站岗真是荣幸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C10")

    Jump("loc_1E22")

    label("loc_1C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1CBF")

    ChrTalk(    #120
        0xFE,
        (
            "王都空中出现会飞的\x01",
            "巨大人形兵器是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "如果真的有那种东西的话，\x01",
            "连哈肯大门和雷斯顿要塞\x01",
            "都危险了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "通知里说到的『结社』，\x01",
            "到底是些什么人呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1D38")

    ChrTalk(    #123
        0xFE,
        "你们是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "听说这次的警戒工作是由希德中校的\x01",
            "部队和游击士协会联合进行的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "总之请多关照了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1DAB")

    ChrTalk(    #126
        0xFE,
        (
            "这里的迪尔队长的\x01",
            "严格是出了名的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "虽然军队本身应该是\x01",
            "严格的，不过太顽固的话\x01",
            "就让人感到为难了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1E22")

    ChrTalk(    #128
        0xFE,
        (
            "诞辰庆典前被配属到这个部队\x01",
            "之后已经过了好几个月了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "虽然还有很多问题，\x01",
            "不过总算习惯现在的工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E22")

    TalkEnd(0xFE)
    Return()

    # Function_19_1A01 end

    def Function_20_1E26(): pass

    label("Function_20_1E26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F00")

    ChrTalk(    #130
        0xFE,
        (
            "导力器不能用的话\x01",
            "夜晚的警戒还是让人担心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "没有照明的话\x01",
            "敌人接近了也注意不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "蔡斯\x01",
            "听说有卖在黑暗中\x01",
            "也能看见东西的眼镜的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "真希望我们的部队也\x01",
            "能讨论是不是能引进这东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F5C")

    label("loc_1F00")


    ChrTalk(    #134
        0xFE,
        (
            "导力灯也没有，\x01",
            "夜晚的警戒还是让人担心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "听说有卖在黑暗中\x01",
            "真希望早点装备那个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5C")

    Jump("loc_2202")

    label("loc_1F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_205C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(    #136
        0xFE,
        (
            "一起做门卫的沃普\x01",
            "现在现在去蔡斯那边了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "好像因为那边是外围，\x01",
            "所以要强化警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "虽然我觉得这是理所当然的判断，\x01",
            "不过我也因此变得寂寞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2059")

    label("loc_2009")


    ChrTalk(    #139
        0xFE,
        (
            "一个人做门卫\x01",
            "已经是很久之前的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "有、有什么事的话\x01",
            "得马上去叫增援。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2059")

    Jump("loc_2202")

    label("loc_205C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_20AA")

    ChrTalk(    #141
        0xFE,
        (
            "附近可能还潜伏着\x01",
            "出现在王都的\x01",
            "特务兵的余党。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "请充分注意。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2202")

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(    #143
        0xFE,
        (
            "从今天开始王都的\x01",
            "警戒和巡逻好像开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "艾尔贝离宫好像也\x01",
            "设置了警备本部……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "有一种签字仪式马上\x01",
            "就要开始了的紧张感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2202")

    label("loc_2137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2188")

    ChrTalk(    #146
        0xFE,
        "今天天气不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "这样的日子真想和孩子\x01",
            "拿着盒饭去离宫那边游玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2202")

    label("loc_2188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2202")

    ChrTalk(    #148
        0xFE,
        (
            "蔡斯的地震事件\x01",
            "好像好不容易才解决了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "格兰赛尔现在\x01",
            "很和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "政变以来就\x01",
            "就没发生过什么可疑的事件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2202")

    TalkEnd(0xFE)
    Return()

    # Function_20_1E26 end

    def Function_21_2206(): pass

    label("Function_21_2206")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_251E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2406")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #151
        0xFE,
        "哟，艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "真是辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1011F啊，冈多夫先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22AC")

    ChrTalk(    #155
        0x106,
        "#050F在巡逻吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_2309")

    label("loc_22AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22DD")

    ChrTalk(    #156
        0x103,
        "#020F是在巡逻中吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_2309")

    label("loc_22DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2309")

    ChrTalk(    #157
        0x107,
        "#064F是在巡逻吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    label("loc_2309")


    ChrTalk(    #158
        0xFE,
        "啊，正是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "不管怎么说，警戒工作\x01",
            "可是不能松懈的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "哈，你们就集中精力\x01",
            "完成自己的任务吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "维持治安之类的事情\x01",
            "交给我们就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1002F嗯……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x102,
        (
            "#1040F……那可太好了。\x02\x03",

            "那么，请当心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #164
        0xFE,
        "喔，真周到啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x20D1)
    Jump("loc_251E")

    label("loc_2406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_246C")

    ChrTalk(    #165
        0xFE,
        (
            "在现在这种形势下，\x01",
            "不管再发生什么我也不会惊奇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "我只要做好自己的\x01",
            "警戒就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251E")

    label("loc_246C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D6")

    ChrTalk(    #167
        0xFE,
        "哟，是你们啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "好像工作\x01",
            "很忙的样子嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "总之努力是好，\x01",
            "可别太埋头于工作中哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_251E")

    label("loc_24D6")


    ChrTalk(    #170
        0xFE,
        (
            "好像工作\x01",
            "很忙的样子嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "总之努力是好，\x01",
            "可别太埋头于工作中哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251E")

    TalkEnd(0xFE)
    Return()

    # Function_21_2206 end

    def Function_22_2522(): pass

    label("Function_22_2522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2533")
    Call(0, 24)

    label("loc_2533")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0xC6, 0x0, 0x64)
    OP_6F(0x4, 100)
    OP_72(0x4, 0x10)
    SetChrPos(0x9, 22890, 7250, -24590, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 23390, 7250, -23090, 180)
    SetChrPos(0xF7, 22390, 7250, -23090, 180)
    SetChrPos(0x104, 23390, 7250, -22090, 180)
    SetChrPos(0x105, 22390, 7250, -22090, 180)
    OP_6D(22650, 7250, -20770, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(315000, 0)
    OP_6E(427, 0)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    Sleep(2500)

    def lambda_25FC():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB9B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25FC)
    Sleep(80)

    def lambda_261C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB9B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_261C)
    Sleep(120)

    def lambda_263C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB9B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_263C)
    Sleep(80)

    def lambda_265C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_265C)
    Sleep(120)

    def lambda_267C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_267C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x104, 0x1)
    OP_6A(0xFF)
    Fade(1000)
    OP_6D(22860, 7250, -41960, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(220000, 0)
    OP_6E(427, 0)
    OP_0D()

    ChrTalk(    #172
        0x9,
        (
            "#5P等我到外面看看的时候\x01",
            "他已经不见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #173
        0x9,
        (
            "#5P就是说，是在\x01",
            "这里跟丢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1020F#6P跟、跟丢了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x105,
        "#043F#4P可这里是死路吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#5P嗯，无法想象他能\x01",
            "从这么高的地方跳下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#5P大概觉得他朝这边来了\x01",
            "是我的错觉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "#5P最后，我找了其他的地方\x01",
            "也没发现他的踪影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        "#5P有一点忧郁呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x104,
        (
            "#035F#6P呵呵，可怜的小猫咪。\x02\x03",

            "#037F只要你愿意，就让我\x01",
            "来帮你忘却那种男人吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #181
        0x101,
        "#1019F#5P停！不许浑水摸鱼！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_28F1")

    ChrTalk(    #182
        0x106,
        (
            "#053F#2P原来如此……\x01",
            "大致情况我们了解了。\x02\x03",

            "#051F谢谢，你可帮了我们大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_28F1")


    ChrTalk(    #183
        0x103,
        (
            "#026F#2P原来如此……\x01",
            "大致情况我们了解了。\x02\x03",

            "#526F谢谢，你可帮了我们大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2941")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #184
        0x9,
        "#5P呵呵，不用客气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        (
            "#5P不过那个人……\x01",
            "果然是个逃犯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#5P是个被游击士协会\x01",
            "追踪的冷血杀人狂？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1016F#6P这、这还不能确定……\x01",
            "不过肯定是应该注意的人物。\x02\x03",

            "#1002F如果你看到他\x01",
            "也还是不要靠近的为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        (
            "#5P嗯～\x01",
            "虽然帅，不过也没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "#5P我还有工作，就先\x01",
            "告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        "#5P加油啊，游击士们！\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x0, 0x0, 0x17)

    def lambda_2A8A():

        label("loc_2A8A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2A8A")

    QueueWorkItem2(0x101, 1, lambda_2A8A)

    def lambda_2A9B():

        label("loc_2A9B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2A9B")

    QueueWorkItem2(0xF7, 1, lambda_2A9B)

    def lambda_2AAC():

        label("loc_2AAC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2AAC")

    QueueWorkItem2(0x105, 1, lambda_2AAC)

    def lambda_2ABD():

        label("loc_2ABD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2ABD")

    QueueWorkItem2(0x104, 1, lambda_2ABD)
    Sleep(1000)

    def lambda_2AD3():
        OP_6D(23080, 7250, -38000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AD3)
    WaitChrThread(0x9, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    def lambda_2B0F():
        OP_6D(23080, 7250, -40700, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B0F)
    OP_8C(0x104, 225, 400)
    OP_8C(0xF7, 45, 400)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #191
        0x105,
        (
            "#047F『无法想象他能\x01",
            "从这么高的地方跳下去』。\x02\x03",

            "#042F……艾丝蒂尔。\x01",
            "你有没有想到什么人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1003F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C6, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    Sleep(1000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1002F#5P从女王宫跳下去的\x01",
            "银发男人──洛伦斯少尉。\x02\x03",

            "确实，要是和那家伙水准相当的话\x01",
            "从这里跳下去也没问题……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C8B")

    ChrTalk(    #194
        0x106,
        (
            "#057F#2P嗯……\x02\x03",

            "这样一来太阳眼镜小子的\x01",
            "原形应该可以确定了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD2")

    label("loc_2C8B")


    ChrTalk(    #195
        0x103,
        (
            "#022F#2P嗯……\x02\x03",

            "这样一来戴太阳眼镜的男人的\x01",
            "原形应该可以确定了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD2")


    ChrTalk(    #196
        0x104,
        (
            "#035F#6P是怪盗之后的第二个『执行者』──\x02\x03",

            "#030F可以这么说吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D65")

    ChrTalk(    #197
        0x106,
        (
            "#053F#2P看来没错。\x02\x03",

            "#050F这里的调查都结束了。\x01",
            "我们回协会报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAB")

    label("loc_2D65")


    ChrTalk(    #198
        0x103,
        (
            "#026F#2P看来没错。\x02\x03",

            "#020F这里的调查都结束了。\x01",
            "我们回协会报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DAB")

    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(23030, 7250, -40170, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 23060, 7250, -40220, 16)
    SetChrPos(0x1, 23060, 7250, -40220, 16)
    SetChrPos(0x2, 23060, 7250, -40220, 16)
    SetChrPos(0x3, 23060, 7250, -40220, 16)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_6F(0x4, 0)
    OP_71(0x4, 0x10)
    OP_A2(0x1416)
    OP_28(0x86, 0x1, 0x20)
    OP_28(0x86, 0x1, 0x40)
    OP_28(0x86, 0x1, 0x80)
    OP_28(0x86, 0x1, 0x100)
    Sleep(1000)
    OP_21()
    OP_1D(0x10)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_22_2522 end

    def Function_23_2E7F(): pass

    label("Function_23_2E7F")


    def lambda_2E85():
        OP_8E(0xFE, 0x5F50, 0x1C52, 0xFFFF5D1C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E85)
    WaitChrThread(0x9, 0x1)

    def lambda_2EA5():
        OP_8E(0xFE, 0x5EEC, 0x1C52, 0xFFFF8EB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2EA5)
    WaitChrThread(0x9, 0x1)
    Return()

    # Function_23_2E7F end

    def Function_24_2EC0(): pass

    label("Function_24_2EC0")

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
        (0, "loc_2F3A"),
        (1, "loc_2F40"),
        (SWITCH_DEFAULT, "loc_2F46"),
    )


    label("loc_2F3A")

    OP_A2(0x1200)
    Jump("loc_2F46")

    label("loc_2F40")

    OP_A2(0x1201)
    Jump("loc_2F46")

    label("loc_2F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2F54")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2F58")

    label("loc_2F54")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2F58")

    Return()

    # Function_24_2EC0 end

    def Function_25_2F59(): pass

    label("Function_25_2F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3083")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB4")

    ChrTalk(    #199
        0x101,
        (
            "#1002F……这里的调查\x01",
            "还没结束。\x02\x03",

            "我们赶快\x01",
            "去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3068")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3013")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD1")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_2FD8")

    label("loc_2FD1")

    TurnDirection(0x106, 0x0, 400)

    label("loc_2FD8")


    ChrTalk(    #200
        0x106,
        (
            "#050F这里的调查\x01",
            "还没结束。\x02\x03",

            "我们赶快去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3068")

    label("loc_3013")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3029")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3030")

    label("loc_3029")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3030")


    ChrTalk(    #201
        0x103,
        (
            "#020F这里的调查\x01",
            "还没结束。\x02\x03",

            "我们赶快去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3068")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3083")

    Return()

    # Function_25_2F59 end

    def Function_26_3084(): pass

    label("Function_26_3084")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_26_3084 end

    SaveToFile()

Try(main)
