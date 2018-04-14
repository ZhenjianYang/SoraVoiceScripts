from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0600   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0600.x',
        MapIndex            = 17,
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
        '士兵亚多罗瓦',                         # 9
        '士兵洛克思',                           # 10
        '士兵托马斯',                           # 11
        '古利乌副队长',                         # 12
        '士兵舒托尔',                           # 13
        '士兵巴兰克',                           # 14
        '雾调整',                               # 15
        '艾利兹街道方向',                       # 16
        '庭园大道方向',                         # 17
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = -10690,
        Z                   = 0,
        Y                   = -3640,
        Direction           = 90,
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
        X                   = -10660,
        Z                   = 0,
        Y                   = 3600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -21590,
        Z                   = 11750,
        Y                   = 150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -7840,
        Z                   = 0,
        Y                   = -4840,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -35300,
        Z                   = 0,
        Y                   = -3560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37180,
        Z                   = 0,
        Y                   = -1450,
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
        X                   = -83430,
        Z                   = 0,
        Y                   = -1170,
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
        X                   = -75400,
        Y                   = -2000,
        Z                   = -8100,
        Range               = -74400,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1FA4,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_1FA",          # 00, 0
        "Function_1_249",          # 01, 1
        "Function_2_457",          # 02, 2
        "Function_3_5D4",          # 03, 3
        "Function_4_5F8",          # 04, 4
        "Function_5_68E",          # 05, 5
        "Function_6_A9F",          # 06, 6
        "Function_7_FBE",          # 07, 7
        "Function_8_180A",         # 08, 8
        "Function_9_1972",         # 09, 9
        "Function_10_1DBF",        # 0A, 10
        "Function_11_219A",        # 0B, 11
        "Function_12_22D4",        # 0C, 12
        "Function_13_234F",        # 0D, 13
    )


    def Function_0_1FA(): pass

    label("Function_0_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_213")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_224")

    label("loc_213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_224")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_224")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_230"),
        (SWITCH_DEFAULT, "loc_248"),
    )


    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_245")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_245")

    Jump("loc_248")

    label("loc_248")

    Return()

    # Function_0_1FA end

    def Function_1_249(): pass

    label("Function_1_249")

    OP_16(0x2, 0xFA0, 0xFFFDB610, 0xFFFE0430, 0x230006)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_273")
    OP_B1("t0600_y")
    Jump("loc_285")

    label("loc_273")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_B1("t0600_n")

    label("loc_285")

    OP_1C(0x2, 0x0, 0xD)
    OP_1C(0x3, 0x0, 0xD)
    OP_1C(0x4, 0x0, 0xD)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_40E")
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_43(0xE, 0x0, 0x0, 0x4)

    label("loc_40E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")
    OP_6F(0x2, 100)
    OP_72(0x2, 0x10)
    OP_6F(0x3, 100)
    OP_72(0x3, 0x10)
    OP_6F(0x4, 100)
    OP_72(0x4, 0x10)

    label("loc_43E")

    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Return()

    # Function_1_249 end

    def Function_2_457(): pass

    label("Function_2_457")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5BE")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5BE")

    label("loc_495")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5BE")

    label("loc_4AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C7")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5BE")

    label("loc_4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5BE")

    label("loc_4E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5BE")

    label("loc_4F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5BE")

    label("loc_512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5BE")

    label("loc_52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5BE")

    label("loc_544")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5BE")

    label("loc_55D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_576")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5BE")

    label("loc_576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5BE")

    label("loc_58F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5BE")

    label("loc_5A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5BE")

    label("loc_5D3")

    Return()

    # Function_2_457 end

    def Function_3_5D4(): pass

    label("Function_3_5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_8D(0xFE, -28070, -8920, -16500, 6400, 3000)
    Jump("Function_3_5D4")

    label("loc_5F7")

    Return()

    # Function_3_5D4 end

    def Function_4_5F8(): pass

    label("Function_4_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68D")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62B")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_640")

    label("loc_62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_640")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_640")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_670")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_685")

    label("loc_670")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_685")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_685")

    Sleep(10)
    Jump("Function_4_5F8")

    label("loc_68D")

    Return()

    # Function_4_5F8 end

    def Function_5_68E(): pass

    label("Function_5_68E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_6F0")

    ChrTalk(    #0
        0xFE,
        (
            "大门的机能好像\x01",
            "还是没有恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "哎呀哎呀，又要这样\x01",
            "渡过一夜，\x01",
            "真是无法想象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B")

    label("loc_6F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(    #2
        0xFE,
        (
            "现在不管哪个关所\x01",
            "都处在很困扰的境地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "武器方面是个问题，\x01",
            "补给问题更是让人头疼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "搬运车和飞船都不能用了，\x01",
            "食品的运送现在非常麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7F9")

    ChrTalk(    #5
        0xFE,
        (
            "互不侵犯条约的签字仪式\x01",
            "好像顺利结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "身为王都关所的门卫，\x01",
            "我肩上的担子一下就轻了下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(    #7
        0xFE,
        (
            "昨天经过这里的游击士\x01",
            "刚才又回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "不过，不知为何…\x01",
            "看起来好像很疲倦的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "嗯，从王都那里往返一趟，\x01",
            "疲劳也是正常的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_96C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8EF")

    ChrTalk(    #10
        0xFE,
        (
            "今天早上看见了一位\x01",
            "打扮很奇特的神父呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "最近神父们还背着\x01",
            "护身用的武器啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_969")

    label("loc_8EF")


    ChrTalk(    #12
        0xFE,
        (
            "今天早上看见了一位\x01",
            "打扮很奇特的神父呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "背上还背着\x01",
            "弓箭一样的武器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "最近神父们还背着\x01",
            "护身用的武器啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_969")

    Jump("loc_A9B")

    label("loc_96C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_9DA")

    ChrTalk(    #15
        0xFE,
        (
            "昨天从关所来的游击士\x01",
            "今天早上向王都出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "多亏好好休息了一个晚上，\x01",
            "旅行者们都很有精神。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B")

    label("loc_9DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_A9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_A39")

    ChrTalk(    #17
        0xFE,
        (
            "被游击士护送的旅行商人\x01",
            "刚才已经到达了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "洛连特的雾有\x01",
            "那么厉害的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B")

    label("loc_A39")


    ChrTalk(    #19
        0xFE,
        (
            "明天要在艾尔贝离宫\x01",
            "进行互不侵犯条约的签字仪式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "所以通行时的审查也会\x01",
            "比平时更加严格哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9B")

    TalkEnd(0x8)
    Return()

    # Function_5_68E end

    def Function_6_A9F(): pass

    label("Function_6_A9F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B75")

    ChrTalk(    #21
        0xFE,
        (
            "飞船无法飞行\x01",
            "对王国军来说非常致命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "毕竟我们军队的主要战力\x01",
            "就是飞行舰队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "帝国也有飞行舰队，\x01",
            "但他们还是以地面部队为主力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "虽然也会受到一些影响，\x01",
            "不过显然不如我们严重。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_BC9")

    label("loc_B75")


    ChrTalk(    #25
        0xFE,
        (
            "飞船无法飞行\x01",
            "对王国军来说非常致命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "毕竟我们军队的主要战力\x01",
            "就是飞行舰队。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC9")

    Jump("loc_FBA")

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C4A")

    ChrTalk(    #27
        0xFE,
        (
            "不但关卡大门无法关闭，\x01",
            "连导力枪都无法使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "情况真是恶劣到极点呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "现在只能祈祷\x01",
            "别发生什么意外了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBA")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_C9F")

    ChrTalk(    #30
        0xFE,
        "雾终于散去了啊，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "签字仪式也顺利结束了。\x01",
            "真是个令人高兴的早晨啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBA")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D14")

    ChrTalk(    #32
        0xFE,
        (
            "听说威尔特桥的守备队\x01",
            "进入洛连特镇中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "每次一想到那种浓雾\x01",
            "就不由对大自然之力感到恐惧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_D14")


    ChrTalk(    #34
        0xFE,
        (
            "听说威尔特桥的守备队\x01",
            "进入洛连特镇中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "浓雾原来是\x01",
            "这么恐怖的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "大自然的力量\x01",
            "真是令人畏惧呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D88")

    Jump("loc_FBA")

    label("loc_D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DE5")

    ChrTalk(    #37
        0xFE,
        (
            "今天终于要进行\x01",
            "互不侵犯条约的签字仪式了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "这一天终于来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E65")

    label("loc_DE5")


    ChrTalk(    #39
        0xFE,
        (
            "今天终于要进行\x01",
            "互不侵犯条约的签字仪式了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "对王国来说，\x01",
            "这也是很有纪念意义的一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "很好！\x01",
            "我也要努力才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E65")

    Jump("loc_FBA")

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EE7")

    ChrTalk(    #42
        0xFE,
        (
            "现在王都中除了各国要人之外，\x01",
            "还有很多关联人员也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "身为士兵，我们也很希望\x01",
            "这次的活动能顺利结束。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBA")

    label("loc_EE7")


    ChrTalk(    #44
        0xFE,
        "明天就是条约的签字仪式了啊，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "现在王都中除了各国要人之外，\x01",
            "还有很多关联人员也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "十年前侵略王国的\x01",
            "埃雷波尼亚帝国，如今却\x01",
            "要和我们签署互不侵犯条约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "这样的话，引起各国关注\x01",
            "也是不奇怪的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FBA")

    TalkEnd(0x9)
    Return()

    # Function_6_A9F end

    def Function_7_FBE(): pass

    label("Function_7_FBE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1066")

    ChrTalk(    #48
        0xFE,
        (
            "听说哈肯大门那边\x01",
            "处于严格的警备状态…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "不知道帝国方面对这次的事件\x01",
            "有什么准备对策…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "如果只是签署互不侵犯条约的话，\x01",
            "我想也不会有什么事，可是…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1141")

    ChrTalk(    #51
        0xFE,
        (
            "从这里的城墙上可以很清楚地\x01",
            "看见那个浮游岛屿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "即使不刻意去注意\x01",
            "也非常显眼…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "总之让人很难不在意那个岛屿，\x01",
            "我没事的时候也经常眺望它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "嗯，不过在警备的时候\x01",
            "总是分散注意力可不好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_119D")

    label("loc_1141")


    ChrTalk(    #55
        0xFE,
        (
            "可是，那座岛……\x01",
            "究竟是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "看起来虽然很漂亮，\x01",
            "但不知为何总让人觉得不安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119D")

    Jump("loc_1806")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_12A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1217")

    ChrTalk(    #57
        0xFE,
        (
            "这里的警备工作\x01",
            "终于也恢复到普通的状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "国家典礼也好，异常气象也好，\x01",
            "应该都只是暂时的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_1217")


    ChrTalk(    #59
        0xFE,
        (
            "这里的警备工作\x01",
            "终于也恢复到普通的状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "可能的话，真希望什么也别发生了，\x01",
            "不管是国家典礼还是异常气象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "啊～累死了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_12A0")

    Jump("loc_1806")

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_13F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1337")

    ChrTalk(    #62
        0xFE,
        (
            "最近食堂的亚米丽\x01",
            "新做了一些东方料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "好吃虽然是好吃，\x01",
            "但总是卖光，真讨厌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "嗯～如果今天没意外的话\x01",
            "应该能吃到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F4")

    label("loc_1337")


    ChrTalk(    #65
        0xFE,
        (
            "马上就是接班的时间了吧……\x01",
            "今天的午饭吃什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "最近食堂的亚米丽\x01",
            "新做了一些东方料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "好吃虽然是好吃，\x01",
            "但总是卖光，真讨厌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "咕、咕噜……（吞口水）\x01",
            "今天该去哪呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_13F4")

    Jump("loc_1806")

    label("loc_13F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_14E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1451")

    ChrTalk(    #69
        0xFE,
        (
            "签字仪式结束后…\x01",
            "又是浓雾吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "真是让人一口气都不能松下来啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DE")

    label("loc_1451")


    ChrTalk(    #71
        0xFE,
        (
            "因签字仪式而实施的临时强化警备，\x01",
            "今天好不容易才结束…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "还没来得及松口气，\x01",
            "又到处浓雾弥漫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "呼～真是让人一分钟都不能休息啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14DE")

    Jump("loc_1806")

    label("loc_14E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_154B")

    ChrTalk(    #74
        0xFE,
        (
            "嗯，洛连特那边的状况\x01",
            "因为雾太浓很难确认。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "虽然还魔兽没有出现，\x01",
            "但还是要仔细巡查才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_15A0")

    ChrTalk(    #76
        0xFE,
        (
            "似乎将王都的受害情况\x01",
            "压制到了最低呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "真不愧是尤莉亚中尉她们啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1611")

    ChrTalk(    #78
        0xFE,
        "我、我在这里也看见了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "和奇怪的飞行物体战斗的\x01",
            "就是你们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "那、那究竟是什么东西啊！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_1611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_16B7")

    ChrTalk(    #81
        0xFE,
        (
            "……黑发的男孩吗？\x01",
            "没有来过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "如果来了的话应该在\x01",
            "南边的城墙上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "游客一般\x01",
            "都会去那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "应该是从南边的台阶下去，\x01",
            "然后从南门出去了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_16B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_172D")

    ChrTalk(    #85
        0xFE,
        (
            "虽然签字仪式已经临近了，\x01",
            "但我们的工作还是和平时一样，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "只是全力守卫格鲁纳门而已……\x01",
            "嗯，仅此而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_172D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_17CD")

    ChrTalk(    #87
        0xFE,
        (
            "政变之后，\x01",
            "部队进行了重编，\x01",
            "上层的首脑们好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "虽然这里是镇守王都的要道，\x01",
            "但大概是因为全部配备了精英人员。\x01",
            "似乎没有发生任何异常状况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_17CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1806")

    ChrTalk(    #89
        0xFE,
        "没有异常状况！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "呀，今天的天气也不错啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1806")

    TalkEnd(0xA)
    Return()

    # Function_7_FBE end

    def Function_8_180A(): pass

    label("Function_8_180A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_186D")

    ChrTalk(    #91
        0xFE,
        (
            "亚宁堡的防线自建国以来\x01",
            "从未被敌人突破过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "为了维护这荣耀\x01",
            "我也会死守在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196E")

    label("loc_186D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_196E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1906")

    ChrTalk(    #93
        0xFE,
        "啊，你们是游击士吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "我们格鲁纳门的守备队\x01",
            "也开始加强警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "在大门无法控制的状态下，\x01",
            "必须要加强警备，防患于未然。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_196E")

    label("loc_1906")


    ChrTalk(    #96
        0xFE,
        (
            "我们格鲁纳门的守备队\x01",
            "也开始加强警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "在大门无法控制的状态下，\x01",
            "必须要加强警备，防患于未然。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196E")

    TalkEnd(0xB)
    Return()

    # Function_8_180A end

    def Function_9_1972(): pass

    label("Function_9_1972")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1A95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A44")

    ChrTalk(    #98
        0xFE,
        (
            "空中浮岛的出现、\x01",
            "导力机能的停止……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "利贝尔王国内最近一直\x01",
            "发生不可思议的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "在这样下去的话，\x01",
            "就算女神降临也不觉得奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "……噢，失礼了。\x01",
            "这样说话太冒犯女神了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1A92")

    label("loc_1A44")


    ChrTalk(    #102
        0xFE,
        (
            "空中浮岛的出现、\x01",
            "导力机能的停止……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "总觉得像是神话中\x01",
            "的世界一样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A92")

    Jump("loc_1DBB")

    label("loc_1A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1C")

    ChrTalk(    #104
        0xFE,
        "欢迎来到格鲁纳门，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "进入警备状态之后\x01",
            "通行管理也比以前更严了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "可以自由通行的\x01",
            "只有游击士和军队的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1B78")

    label("loc_1B1C")


    ChrTalk(    #107
        0xFE,
        (
            "现在处于非常状况，\x01",
            "通行管理也比以前更严了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "可以自由通行的\x01",
            "只有游击士和军队的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B78")

    Jump("loc_1DBB")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1BF5")

    ChrTalk(    #109
        0xFE,
        (
            "听说在格兰赛尔\x01",
            "好像出了什么事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "和出现在周游道的那些特务兵\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "总有种不好的预感……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1C5F")

    ChrTalk(    #112
        0xFE,
        (
            "啊，话是那么说，\x01",
            "不过周游道现在已经被封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "要去格兰赛尔的话，\x01",
            "走庭园大道就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_1CCF")

    ChrTalk(    #114
        0xFE,
        "欢迎来到格鲁纳门！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "这么慌慌张张的，\x01",
            "是有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "要参观的话不用着急，\x01",
            "还有的是时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(    #117
        0xFE,
        "欢迎来到格鲁纳门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "马上就是条约的签字仪式了，\x01",
            "警备工作也要加强。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1D67")

    ChrTalk(    #119
        0xFE,
        "条约的签字仪式吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "希望不要有人\x01",
            "暗中捣乱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1DBB")

    ChrTalk(    #121
        0xFE,
        "欢迎来到格鲁纳门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "这里是格兰赛尔地区和\x01",
            "洛连特地区之间交接的关所。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBB")

    TalkEnd(0xC)
    Return()

    # Function_9_1972 end

    def Function_10_1DBF(): pass

    label("Function_10_1DBF")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1E12")

    ChrTalk(    #123
        0xFE,
        (
            "真是的，奇怪的事件\x01",
            "一直层出不穷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "以前的政变事件\x01",
            "就够受了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBA")

    ChrTalk(    #125
        0xFE,
        (
            "导力器瘫痪的时候\x01",
            "这里也发生了很大的骚乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "不但灯全都熄灭了，\x01",
            "连大门也关不上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "虽然通信器已经修好了，\x01",
            "但严峻的状况仍然没有得到好转。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1F36")

    label("loc_1EBA")


    ChrTalk(    #128
        0xFE,
        (
            "虽然通信器已经修好了，\x01",
            "但严峻的状况仍然没有得到好转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "虽然现在还没发生什么太严重的事情。\x01",
            "但无论如何也不能松懈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F36")

    Jump("loc_2196")

    label("loc_1F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1FA5")

    ChrTalk(    #130
        0xFE,
        "情报部就此解散了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "虽然让人松了口气，\x01",
            "但那飞走的巨大人形机器人…\x01",
            "究竟是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_200F")

    ChrTalk(    #132
        0xFE,
        (
            "结社……\x01",
            "到底是怎样的一群家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "我对那东西实在放不下心，\x01",
            "今后必须要继续加强警备啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_200F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_206F")

    ChrTalk(    #134
        0xFE,
        (
            "队长说要集合开会，\x01",
            "好像是有什么事情要说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "果然是那件事吗……\x01",
            "柏斯发生的事件\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(    #136
        0xFE,
        "听说离宫中安置了警备本部。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "自从卡西乌斯准将回到军队以后，\x01",
            "军队的办事效率迅速了很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2131")

    ChrTalk(    #138
        0xFE,
        "马上就是签字仪式了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "各界要人都会来到这里，\x01",
            "必须要加强警备才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_2131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(    #140
        0xFE,
        (
            "听说卢安和蔡斯好像都\x01",
            "发生了奇妙的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "格兰赛尔和城墙那面的\x01",
            "洛连特倒还是很安稳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2196")

    TalkEnd(0xD)
    Return()

    # Function_10_1DBF end

    def Function_11_219A(): pass

    label("Function_11_219A")

    EventBegin(0x0)
    OP_6D(-16830, 0, 1620, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(8000, 0)
    OP_6C(74000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -82890, 0, 20, 90)
    StopSound(0x7D00, 0x3D090, 0x0)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x2EE0)

    def lambda_2213():
        OP_6B(3250, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2213)

    def lambda_2223():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2223)

    def lambda_2233():
        OP_6D(-72030, 0, 20, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2233)
    Sleep(8000)
    OP_8E(0x101, 0xFFFEDED2, 0x0, 0xFFFFFFEC, 0x1388, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #142
        0x101,
        (
            "#1020F#5P已经是黄昏了……！\x02\x03",

            "#1015F亚宁堡的上面……\x01",
            "也就是城墙上了。\x02\x03",

            "#1002F必须要赶快过去……！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1637)
    EventEnd(0x0)
    Return()

    # Function_11_219A end

    def Function_12_22D4(): pass

    label("Function_12_22D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_234E")
    EventBegin(0x2)

    ChrTalk(    #143
        0x101,
        (
            "#1003F（我在做什么啊！）\x02\x03",

            "#1002F（约修亚……\x01",
            "  约修亚不是还在等着我吗！？）\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_234E")

    Return()

    # Function_12_22D4 end

    def Function_13_234F(): pass

    label("Function_13_234F")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_13_234F end

    SaveToFile()

Try(main)
