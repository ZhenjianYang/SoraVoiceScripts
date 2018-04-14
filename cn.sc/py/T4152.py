from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4152   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4152.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '士兵达登',                             # 9
        '比卡',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '王国军士兵',                           # 13
        '王都格兰赛尔·北街区',                 # 14
        '王都格兰赛尔·南街区',                 # 15
        '王都格兰赛尔·码头',                   # 16
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
        'ED6_DT07/CH01680 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
    )

    DeclNpc(
        X                   = -89010,
        Z                   = 250,
        Y                   = -1030,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -78290,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 180,
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
        X                   = -55400,
        Z                   = 0,
        Y                   = -3050,
        Direction           = 180,
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
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -76250,
        Z                   = -3500,
        Y                   = -30490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
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
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
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
        X                   = -117000,
        Z                   = 0,
        Y                   = -4090,
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
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_253",          # 02, 2
        "Function_3_277",          # 03, 3
        "Function_4_2FC",          # 04, 4
        "Function_5_389",          # 05, 5
        "Function_6_3C9",          # 06, 6
        "Function_7_3FF",          # 07, 7
        "Function_8_42D",          # 08, 8
        "Function_9_494",          # 09, 9
        "Function_10_4E2",         # 0A, 10
        "Function_11_4E6",         # 0B, 11
        "Function_12_4EA",         # 0C, 12
        "Function_13_4EE",         # 0D, 13
        "Function_14_9B0",         # 0E, 14
        "Function_15_BFC",         # 0F, 15
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Return()

    # Function_0_21A end

    def Function_1_21B(): pass

    label("Function_1_21B")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    OP_71(0xF, 0x4)
    OP_71(0xC, 0x10)
    OP_72(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_252")
    OP_1B(0x3, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xE)

    label("loc_252")

    Return()

    # Function_1_21B end

    def Function_2_253(): pass

    label("Function_2_253")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_2_253")

    label("loc_276")

    Return()

    # Function_2_253 end

    def Function_3_277(): pass

    label("Function_3_277")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FB")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_3_277")

    label("loc_2FB")

    Return()

    # Function_3_277 end

    def Function_4_2FC(): pass

    label("Function_4_2FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_388")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_4_2FC")

    label("loc_388")

    Return()

    # Function_4_2FC end

    def Function_5_389(): pass

    label("Function_5_389")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "这么晚了还去港口？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "千万小心脚下\x01",
            "别滑进湖里哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_389 end

    def Function_6_3C9(): pass

    label("Function_6_3C9")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "这么晚了啊……\x01",
            "回去时走夜路要小心才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_3C9 end

    def Function_7_3FF(): pass

    label("Function_7_3FF")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        (
            "刚才好像有白色的鸟\x01",
            "飞去西边了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_3FF end

    def Function_8_42D(): pass

    label("Function_8_42D")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "喂，那边的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "晚上出门倒不要紧，\x01",
            "不过可得多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "发生什么事就\x01",
            "大声叫我们吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_42D end

    def Function_9_494(): pass

    label("Function_9_494")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "这么晚了有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "有急事要坐船的话\x01",
            "还是天亮的时候再来吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_494 end

    def Function_10_4E2(): pass

    label("Function_10_4E2")

    SetPlaceName(0xB8)
    Return()

    # Function_10_4E2 end

    def Function_11_4E6(): pass

    label("Function_11_4E6")

    SetPlaceName(0xB7)
    Return()

    # Function_11_4E6 end

    def Function_12_4EA(): pass

    label("Function_12_4EA")

    SetPlaceName(0xAF)
    Return()

    # Function_12_4EA end

    def Function_13_4EE(): pass

    label("Function_13_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_758")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #9
        0x109,
        "#1063F这里是……地下水路吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #10
        0x101,
        "#1015F……不是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1063F可能性很低吧。\x02\x03",

            "……去其他地方找找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1002F明、明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_5A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62A")

    ChrTalk(    #13
        0x109,
        "#1063F这里是……地下水路吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #14
        0x101,
        "#1015F……不是吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #15
        0x109,
        (
            "#1063F可能性很低吧。\x02\x03",

            "……去其他地方找找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_62A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B3")

    ChrTalk(    #16
        0x103,
        "#0022F这里是……地下水路吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #17
        0x101,
        "#1015F……不是吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #18
        0x103,
        (
            "#0022F可能性很低啊。\x02\x03",

            "……去其他地方找找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_6B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737")

    ChrTalk(    #19
        0x106,
        "#050F这里是……地下水路吗。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #20
        0x101,
        "#1015F……不是吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #21
        0x106,
        (
            "#050F可能性很低啊。\x02\x03",

            "……去其他地方找找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_737")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_A2(0x0)
    Jump("loc_88C")

    label("loc_758")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79E")

    ChrTalk(    #22
        0x101,
        (
            "#1002F基库好像也没来……\x01",
            "最好去其他地方找找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_871")

    label("loc_79E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E6")

    ChrTalk(    #23
        0x109,
        (
            "#1063F要确认的话这里是最后了。\x01",
            "……先去其他地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_871")

    label("loc_7E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82D")

    ChrTalk(    #24
        0x103,
        (
            "#022F要确认的话这里是最后了。\x01",
            "……先去其他地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_871")

    label("loc_82D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_871")

    ChrTalk(    #25
        0x106,
        (
            "#050F要确认的话这里是最后了。\x01",
            "……先去其他地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_871")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_88C")

    Jump("loc_9AF")

    label("loc_88F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95A")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #26
        0x109,
        (
            "#1063F茶会的会场不在这里。\x01",
            "……赶快去码头吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #27
        0x101,
        "#1002F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_954")

    label("loc_8FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92C")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #28
        0x103,
        "#022F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_954")

    label("loc_92C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_954")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #29
        0x106,
        "#050F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_954")

    OP_A2(0x0)
    Jump("loc_994")

    label("loc_95A")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #30
        0x109,
        (
            "#1063F茶会的会场不在这里。\x01",
            "……赶快去码头吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_994")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_9AF")

    Return()

    # Function_13_4EE end

    def Function_14_9B0(): pass

    label("Function_14_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A83")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #31
        0x109,
        (
            "#1063F北街区之后再去也行吧。\x01",
            "先得去这边找找。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A28")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #32
        0x101,
        "#1002F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7D")

    label("loc_A28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A55")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #33
        0x103,
        "#022F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7D")

    label("loc_A55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7D")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #34
        0x106,
        "#050F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A7D")

    OP_A2(0x1)
    Jump("loc_ABD")

    label("loc_A83")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #35
        0x109,
        (
            "#1063F北街区之后再去也行吧。\x01",
            "先得去这边找找。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABD")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_BFB")

    label("loc_ADB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA6")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #36
        0x109,
        (
            "#1063F茶会的会场不是这儿。\x01",
            "……赶快去码头吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4B")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #37
        0x101,
        "#1002F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA0")

    label("loc_B4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #38
        0x103,
        "#022F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA0")

    label("loc_B78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA0")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #39
        0x106,
        "#050F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_BA0")

    OP_A2(0x1)
    Jump("loc_BE0")

    label("loc_BA6")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #40
        0x109,
        (
            "#1063F茶会的会场不是这儿。\x01",
            "……赶快去码头吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE0")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_BFB")

    Return()

    # Function_14_9B0 end

    def Function_15_BFC(): pass

    label("Function_15_BFC")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #41
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_BFC end

    SaveToFile()

Try(main)
