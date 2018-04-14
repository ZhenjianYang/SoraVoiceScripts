from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0410   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0410.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60015",
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
        '缇欧',                                 # 9
        '维鲁',                                 # 10
        '查儿',                                 # 11
        '弗兰兹',                               # 12
        '汉娜',                                 # 13
        '凯文神父',                             # 14
        '维鲁',                                 # 15
        '查儿',                                 # 16
        '弗兰兹',                               # 17
        '汉娜',                                 # 18
        '器皿',                                 # 19
        '器皿',                                 # 20
        '器皿',                                 # 21
        '器皿',                                 # 22
        '器皿',                                 # 23
        '沙拉',                                 # 24
        '面包',                                 # 25
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
        'ED6_DT26/CH20331 ._CH',             # 00
        'ED6_DT26/CH20336 ._CH',             # 01
        'ED6_DT27/CH03080 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT26/CH20313 ._CH',             # 04
        'ED6_DT26/CH20314 ._CH',             # 05
        'ED6_DT07/CH02480 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01070 ._CH',             # 08
        'ED6_DT07/CH01020 ._CH',             # 09
        'ED6_DT07/CH01030 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT26/CH20331P._CP',             # 00
        'ED6_DT26/CH20336P._CP',             # 01
        'ED6_DT27/CH03080P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT26/CH20313P._CP',             # 04
        'ED6_DT26/CH20314P._CP',             # 05
        'ED6_DT07/CH02480P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01070P._CP',             # 08
        'ED6_DT07/CH01020P._CP',             # 09
        'ED6_DT07/CH01030P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 35040,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1320,
        Z                   = 0,
        Y                   = 37500,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 80,
        Z                   = 0,
        Y                   = 32400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 35060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -76340,
        Z                   = 0,
        Y                   = 31640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 458753,
        ChipIndex           = 0x1,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -73490,
        Z                   = 0,
        Y                   = 31660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1507329,
        ChipIndex           = 0x1,
        NpcIndex            = 0x187,
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
        Unknown3            = 196611,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 196611,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 196611,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 196611,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 196611,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 458755,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1769475,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_472",          # 01, 1
        "Function_2_4C7",          # 02, 2
        "Function_3_644",          # 03, 3
        "Function_4_CDC",          # 04, 4
        "Function_5_141D",         # 05, 5
        "Function_6_1798",         # 06, 6
        "Function_7_1AFF",         # 07, 7
        "Function_8_1D1F",         # 08, 8
        "Function_9_1FFE",         # 09, 9
        "Function_10_26CE",        # 0A, 10
        "Function_11_2720",        # 0B, 11
        "Function_12_2772",        # 0C, 12
        "Function_13_27DA",        # 0D, 13
        "Function_14_282C",        # 0E, 14
        "Function_15_2893",        # 0F, 15
        "Function_16_28B4",        # 10, 16
        "Function_17_28FC",        # 11, 17
        "Function_18_3B46",        # 12, 18
        "Function_19_3B7F",        # 13, 19
        "Function_20_3BB8",        # 14, 20
        "Function_21_3D77",        # 15, 21
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    Jump("loc_3F9")

    label("loc_335")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    SetChrPos(0xD, -75610, 0, 2580, 270)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, -77060, 0, 3150, 180)
    SetChrPos(0xA, -73600, 0, 2980, 180)
    SetChrPos(0x9, -72950, 0, 2980, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0xA, 1)
    SetChrSubChip(0xA, 55)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 71)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 39)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42F")
    SetChrPos(0xB, -39020, 0, 33240, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 3820, 0, 24640, 155)
    Jump("loc_43B")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_43B")
    SetChrFlags(0xB, 0x80)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_455")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 20)
    Jump("loc_471")

    label("loc_455")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_471")
    Event(0, 9)

    label("loc_471")

    Return()

    # Function_0_322 end

    def Function_1_472(): pass

    label("Function_1_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_487")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_487")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A")
    Jump("loc_4C6")

    label("loc_49A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C6")
    OP_6F(0x5, 20)
    OP_6F(0x6, 20)
    OP_6F(0x7, 20)
    OP_6F(0x8, 20)

    label("loc_4C6")

    Return()

    # Function_1_472 end

    def Function_2_4C7(): pass

    label("Function_2_4C7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_62E")

    label("loc_4EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_62E")

    label("loc_505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_62E")

    label("loc_51E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_62E")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_62E")

    label("loc_550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_569")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_62E")

    label("loc_569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_582")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_62E")

    label("loc_582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_62E")

    label("loc_59B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_62E")

    label("loc_5B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_62E")

    label("loc_5CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_62E")

    label("loc_5E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_62E")

    label("loc_5FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_618")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_62E")

    label("loc_618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_62E")

    label("loc_643")

    Return()

    # Function_2_4C7 end

    def Function_3_644(): pass

    label("Function_3_644")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FA")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0xFE,
        (
            "喔！艾丝蒂尔，约修亚，\x01",
            "你们回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000F嗯！在协会\x01",
            "有些工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1040F好久不见了啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #3
        0xFE,
        (
            "啊啊，真的是好久好久了呢，\x01",
            "你们看起来很有精神嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "嗯……这样的话～\x01",
            "看来洛连特还有希望啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75F")

    ChrTalk(    #5
        0x103,
        "#021F呵呵，那样的话当然好……\x02",
    )

    CloseMessageWindow()

    label("loc_75F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BE")

    ChrTalk(    #6
        0x106,
        (
            "#555F真是位会说话的大叔啊。\x02\x03",

            "#051F算了，这些家伙确实\x01",
            "也比以前进步了不少……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FE")

    ChrTalk(    #7
        0x108,
        (
            "#071F哈哈，果然是家乡的人啊，\x01",
            "期待度很高啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_816")
    TurnDirection(0xFE, 0x108, 400)
    Jump("loc_843")

    label("loc_816")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E")
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_843")

    label("loc_82E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_843")
    TurnDirection(0xFE, 0x103, 400)

    label("loc_843")


    ChrTalk(    #8
        0xFE,
        "大家都处在困境中呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "期待当地的游击士\x01",
            "也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #10
        0xFE,
        (
            "虽然现在的状况\x01",
            "确实很辛苦，\x01",
            "但我们还是可以继续努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "农业类的工作，本来就是\x01",
            "靠手工作业来完成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015F确实呢，以前根本\x01",
            "就没有机械可以使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "只是没有定期船的话，\x01",
            "运送工作就没办法做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "盼望早日恢复原状的心情，\x01",
            "我们大家都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1006F嗯……\x02\x03",

            "虽然很困难，\x01",
            "但我们一定会努力的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1040F大叔也要加油啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "啊啊，交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20AA)
    Jump("loc_C62")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(    #18
        0xFE,
        (
            "导力式的燃炉无法使用了，\x01",
            "汉娜也很苦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "今天晚上只能像前人那样\x01",
            "用火炉来做料理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "话虽如此，但孩子们好像\x01",
            "反而很喜欢火炉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "到时大概还会像以前一样高兴地\x01",
            "围着火炉转个不停。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_B2B")

    label("loc_ACF")


    ChrTalk(    #22
        0xFE,
        (
            "导力式的燃炉无法使用了，\x01",
            "汉娜也很苦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "今天晚上只能像前人那样\x01",
            "用火炉来做料理了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2B")

    Jump("loc_C62")

    label("loc_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF6")

    ChrTalk(    #24
        0xFE,
        (
            "以手工作业的方式来完成\x01",
            "农场的工作倒是小事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "但没有定期船的话，\x01",
            "种出的蔬菜就没办法运走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "你们看看吧，\x01",
            "这么多农作物都堆在这！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "再这样下去的话，\x01",
            "岂不是全要烂在这里了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_C62")

    label("loc_BF6")


    ChrTalk(    #28
        0xFE,
        (
            "好不容易种出来的优质作物\x01",
            "却运不出去，真是深受打击啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "盼望早日恢复原状的心情，\x01",
            "我们大家都是一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62")

    Jump("loc_CD8")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 7)), scpexpr(EXPR_END)), "loc_CD4")

    ChrTalk(    #30
        0xFE,
        (
            "自从协会开始调查以后\x01",
            "雾更加严重了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "今天已经送货完毕了，\x01",
            "但明天开始就很令人担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD8")

    label("loc_CD4")

    Call(0, 5)

    label("loc_CD8")

    TalkEnd(0xB)
    Return()

    # Function_3_644 end

    def Function_4_CDC(): pass

    label("Function_4_CDC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_104D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1F")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #32
        0xFE,
        (
            "啊……\x01",
            "这不是艾丝蒂尔和约修亚吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1001F您好，汉娜阿姨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        "#1040F一切都还好吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #35
        0xFE,
        (
            "啊啊～我是还好啦，\x01",
            "但家里的事情可就不大好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "导力式的烹饪工具\x01",
            "全都没法用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "今天的早餐\x01",
            "只能吃凉的三明治。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "警备艇的人也来过，\x01",
            "总觉得对他们很不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1015F嗯、嗯，这样啊……\x02\x03",

            "不过只要是阿姨做的三明治，\x01",
            "就算是凉的肯定也很美味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#1040F我也有同感。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "哈哈，这么说真是\x01",
            "让我高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "等以后有空的话\x01",
            "再来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "到时候我会做好多好吃的\x01",
            "料理给你们吃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1001F嗯！非常期待！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        "#1040F到时一定再来麻烦您。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20AB)
    Jump("loc_104A")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_FC3")

    ChrTalk(    #46
        0xFE,
        (
            "维鲁和查儿\x01",
            "最近一直很热情地帮我做事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "看来孩子们也能感觉到\x01",
            "家里遇到困境了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "哈哈，看他们这么懂事，\x01",
            "就算导力器无法使用\x01",
            "也都不觉得烦恼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104A")

    label("loc_FC3")


    ChrTalk(    #49
        0xFE,
        (
            "导力式的烹饪工具\x01",
            "无法运转了，真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "没有导力器的话，很难做出\x01",
            "火候合适的料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "呼，今天只有用火炉来\x01",
            "烹饪料理了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104A")

    Jump("loc_1419")

    label("loc_104D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_13AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 7)), scpexpr(EXPR_END)), "loc_10CB")

    ChrTalk(    #52
        0xFE,
        (
            "年纪轻轻却\x01",
            "这么懂礼貌啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "但有的时候太客气\x01",
            "反而是失礼的行为呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "好了，别人的好意\x01",
            "接受就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A7")

    label("loc_10CB")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #55
        0xFE,
        (
            "艾丝蒂尔，雪拉小姐，\x01",
            "你们终于来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "最近一段时间\x01",
            "经常受你们的照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "这点小意思请收下，\x01",
            "是我们自制的茶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1008F这、这个……\x01",
            "我们不能收啊。\x02\x03",

            "帮助阿姨的是\x01",
            "凯文神父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "哈哈哈，给你们也是\x01",
            "一样的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "那位神父先生\x01",
            "也是不肯收。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1016F啊……\x01",
            "是、是啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "都不是外人了，\x01",
            "不用那么客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "别人的好意，接受就对了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #64
        0x103,
        (
            "#020F快收下吧。\x02\x03",

            "不然汉娜阿姨\x01",
            "会不高兴哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1015F啊，嗯……\x02\x03",

            "#1000F……那、那就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #66
        "\x07\x00得到了\x1F\x9F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x19F, 1)

    ChrTalk(    #67
        0xFE,
        (
            "疲劳的时候喝下它的话\x01",
            "就会精力十足的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1018F阿姨，谢谢啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #69
        0x103,
        "#021F呵呵，那就谢谢了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #70
        0xFE,
        "这点小意思不用放在心上的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "以后有空的话\x01",
            "还要再来玩啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A67)

    label("loc_13A7")

    Jump("loc_1419")

    label("loc_13AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 7)), scpexpr(EXPR_END)), "loc_1415")

    ChrTalk(    #72
        0xFE,
        (
            "我们出去送货的时候\x01",
            "雾还没这么厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "呼，这样的话就不能再让\x01",
            "孩子们跑出去玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1419")

    label("loc_1415")

    Call(0, 5)

    label("loc_1419")

    TalkEnd(0xC)
    Return()

    # Function_4_CDC end

    def Function_5_141D(): pass

    label("Function_5_141D")

    OP_4A(0xC, 255)
    OP_4A(0xB, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xB)"), scpexpr(EXPR_END)), "loc_14AE")

    ChrTalk(    #74
        0xB,
        "哎呀，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xC)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #75
        0xC,
        "艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xC,
        (
            "哎呀，真的是啊。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Jump("loc_1522")

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xC)"), scpexpr(EXPR_END)), "loc_1522")

    ChrTalk(    #77
        0xC,
        "啊，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xB)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #78
        0xB,
        (
            "喔，好久不见了，\x01",
            "身体还好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    label("loc_1522")


    ChrTalk(    #79
        0x101,
        "#1017F嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        "是从洛连特来的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "街道上起了大雾，\x01",
            "什么都看不清楚了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1015F嗯，其实我们就是\x01",
            "为了调查这雾而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        "那可辛苦你啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "艾丝蒂尔已经变成一位\x01",
            "很厉害的游击士了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #85
        0xC,
        (
            "这也是因为有优秀前辈\x01",
            "的指导吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 400)

    ChrTalk(    #86
        0x103,
        (
            "#021F呵呵，主要还是因为本人的努力啊。\x02\x03",

            "虽然在研修时确实费了不少力气，\x01",
            "但我并没教她什么重要的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #87
        0x101,
        (
            "#1008F才不是那样的呢。\x02\x03",

            "雪拉姐不管在什么时候\x01",
            "都一直指导着我… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        (
            "两个人都很了不起，\x01",
            "你们都做得很好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xB,
        (
            "今后也要继续加油啊，\x01",
            "我们会永远支持你们的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #90
        0x101,
        "#1006F谢谢！我会加油的⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        "嗯，也要小心啊。\x02",
    )

    CloseMessageWindow()

    def lambda_177D():
        OP_8C(0xC, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_177D)
    OP_8C(0xB, 180, 400)
    OP_4B(0xC, 255)
    OP_4B(0xB, 255)
    OP_A2(0x189F)
    Return()

    # Function_5_141D end

    def Function_6_1798(): pass

    label("Function_6_1798")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_19EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 6)), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(    #92
        0xD,
        (
            "#1068F不过，在这种状况下\x01",
            "去森林吗？\x02\x03",

            "本来就是很容易迷路的地方，\x01",
            "这下更加危险了。\x02\x03",

            "#1066F艾丝蒂尔，\x01",
            "你们一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E7")

    label("loc_1827")


    ChrTalk(    #93
        0xD,
        (
            "#1060F啊，艾丝蒂尔。\x02\x03",

            "好像已经向协会\x01",
            "报告完毕了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1002F缇欧她们怎么样了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #95
        0xD,
        (
            "#1060F放心。\x01",
            "大家都只是睡着了。\x02\x03",

            "调查进展得如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x103,
        (
            "#022F虽然还不能确定，\x01",
            "但发现了可疑的地方。\x02\x03",

            "接下来准备\x01",
            "前去探查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1015F神秘森林就是\x01",
            "东南部的大森林，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#1065F神秘森林……\x01",
            "利贝尔最大的森林地带啊。\x02\x03",

            "#1063F做好准备之后\x01",
            "再过去吧。\x02\x03",

            "那里视线很差，\x01",
            "要谨慎前进啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1006F凯文神父也是。\x01",
            "缇欧就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xD,
        "#1060F喔！放心交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x189E)

    label("loc_19E7")

    Jump("loc_1AFB")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A51")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #101
        0xD,
        (
            "#1060F这也是神父的工作之一啊。\x02\x03",

            "这里就交给我。\x01",
            "你们赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB1")

    label("loc_1A51")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #102
        0xD,
        (
            "#1064F怎么啦，艾丝蒂尔。\x01",
            "还没回协会吗？\x02\x03",

            "#1060F这里就交给我，\x01",
            "你们赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1AB1")

    Jump("loc_1AFB")

    label("loc_1AB4")


    ChrTalk(    #103
        0xD,
        (
            "#1060F这也是神父的工作之一啊。\x02\x03",

            "这里就交给我。\x01",
            "你们赶快回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFB")

    TalkEnd(0xD)
    Return()

    # Function_6_1798 end

    def Function_7_1AFF(): pass

    label("Function_7_1AFF")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE2")
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(1000)

    ChrTalk(    #104
        0xFE,
        (
            "啊！！约修亚哥哥！！\x01",
            "是来找我玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1040F呀啊！你还好吗？\x02\x03",

            "可是，抱歉。\x01",
            "现在还在工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "唉，真没意思…\x01",
            "还想和你一起玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        "#1049F哈哈，下次吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x20AD)
    Jump("loc_1D1B")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C1D")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #108
        0xFE,
        (
            "约修亚哥哥！\x01",
            "下次再来玩啊～～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDC")

    label("loc_1C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C96")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #109
        0xFE,
        "啊！约修亚还有艾丝蒂尔，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "我现在正在帮\x01",
            "爸爸干活，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "导力器不能用了，\x01",
            "有好多工作得做呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1CDC")

    label("loc_1C96")


    ChrTalk(    #112
        0xFE,
        (
            "我现在正在帮\x01",
            "爸爸干活，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "导力器不能用了，\x01",
            "有好多工作得做呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDC")

    Jump("loc_1D1B")

    label("loc_1CDF")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #114
        0xFE,
        (
            "约修亚哥哥！\x01",
            "下次再来玩啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "要再来玩哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1D1B")

    TalkEnd(0xE)
    Return()

    # Function_7_1AFF end

    def Function_8_1D1F(): pass

    label("Function_8_1D1F")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6F")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #116
        0xFE,
        "啊……约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#1040F呀，查儿。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "嗯、嗯……\x01",
            "查儿很有精神呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "现在也在帮妈妈\x01",
            "干活…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "不好好干活的话\x01",
            "可就不妙了… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#1040F是吗……\x01",
            "要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "啊，约修亚也\x01",
            "在做什么工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        (
            "#1040F嗯，是啊……\x02\x03",

            "不过，用不了不久\x01",
            "我就会再过来玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "嗯、嗯！！那我等你。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20AC)
    Jump("loc_1FFA")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1EBC")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #125
        0xFE,
        (
            "约修亚……\x01",
            "一定再来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "查儿会等你的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FBB")

    label("loc_1EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F69")

    ChrTalk(    #127
        0xFE,
        "啊，约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "那个，昨天\x01",
            "士兵先生来家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "查儿和妈妈给他们\x01",
            "做了三明治。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "士兵先生们… \x01",
            "很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "下、下次也想……\x01",
            "做给约修亚吃呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1FBB")

    label("loc_1F69")


    ChrTalk(    #132
        0xFE,
        (
            "查儿的三明治，\x01",
            "士兵先生们都很喜欢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "下、下次也想……\x01",
            "做给约修亚吃呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBB")

    Jump("loc_1FFA")

    label("loc_1FBE")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #134
        0xFE,
        (
            "约修亚……\x01",
            "一定再来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "查儿会等你的……\x02",
    )

    CloseMessageWindow()

    label("loc_1FFA")

    TalkEnd(0xF)
    Return()

    # Function_8_1D1F end

    def Function_9_1FFE(): pass

    label("Function_9_1FFE")

    EventBegin(0x0)
    SetChrPos(0x18, 400, 800, 27970, 0)
    SetChrPos(0x17, -910, 800, 27970, 0)
    SetChrPos(0x12, -1340, 800, 28000, 0)
    SetChrPos(0x13, -940, 800, 27500, 0)
    SetChrPos(0x14, 890, 800, 27500, 0)
    SetChrPos(0x15, -760, 800, 28500, 0)
    SetChrPos(0x16, 830, 800, 28500, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    OP_4A(0xC, 255)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xB, -2170, 0, 28020, 90)
    SetChrPos(0xA, -960, 200, 26970, 0)
    SetChrPos(0x9, 940, 200, 27000, 0)
    SetChrPos(0x8, 1730, 0, 31540, 270)
    SetChrPos(0xC, 1220, 0, 36190, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, -5790, 0, 24110, 90)
    SetChrPos(0x103, -5790, 0, 24110, 90)
    SetChrPos(0x107, -5790, 0, 24110, 90)
    SetChrPos(0x105, -5790, 0, 24110, 90)
    SetChrChipByIndex(0xB, 0)
    SetChrSubChip(0xB, 5)
    SetChrChipByIndex(0xA, 0)
    SetChrSubChip(0xA, 27)
    SetChrChipByIndex(0x9, 0)
    SetChrSubChip(0x9, 35)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 16)
    SetChrChipByIndex(0xC, 0)
    SetChrSubChip(0xC, 9)
    OP_6D(-5540, 0, 24290, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(500)

    def lambda_223B():
        OP_6D(-3970, 0, 25940, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_223B)
    OP_43(0x101, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x103, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0xC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #136
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    def lambda_22A2():
        OP_6D(-2470, 0, 27900, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22A2)

    def lambda_22BA():
        OP_8E(0xFE, 0xFFFFF808, 0x0, 0x68BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22BA)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #137
        0x101,
        "#1020F#6P弗兰兹叔叔！？\x02",
    )

    CloseMessageWindow()

    def lambda_22FC():
        OP_8C(0xFE, 100, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22FC)
    Sleep(500)

    ChrTalk(    #138
        0x101,
        "#1020F#5P查儿、维鲁！？\x02",
    )

    CloseMessageWindow()
    OP_43(0x103, 0x1, 0x0, 0xE)
    OP_43(0x107, 0x1, 0x0, 0x10)
    OP_43(0x105, 0x1, 0x0, 0xF)

    def lambda_2341():
        OP_6D(-40, 0, 31820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2341)
    OP_8E(0x101, 0xFFFFF380, 0x0, 0x69E6, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFFF3EE, 0x0, 0x749A, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFFF772, 0x0, 0x79B8, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFFFFBA, 0x0, 0x7DAA, 0x1388, 0x0)
    OP_8C(0x101, 90, 600)
    Sleep(500)
    OP_8C(0x101, 0, 600)
    Sleep(500)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #139
        0x101,
        (
            "#1020F#5P缇欧！\x01",
            "汉娜阿姨！！\x02\x03",

            "#1027F……骗人……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD1, 0x0, 0x50)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #140
        0x105,
        (
            "#049F#5P不妙……\x01",
            "都昏睡过去了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)
    Sleep(500)

    ChrTalk(    #141
        0x107,
        "#561F#6P嗯……这孩子也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1003F……呜…………\x02\x03",

            "#1027F又……\x01",
            "又没能赶上吗……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x105,
        "#043F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x107,
        "#063F姐、姐姐……\x02",
    )

    CloseMessageWindow()
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x103, 0x80)

    def lambda_24F0():
        OP_6D(320, 0, 28710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24F0)

    def lambda_2508():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2508)
    OP_8E(0x103, 0x410, 0x0, 0x5F5A, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(200)

    ChrTalk(    #145
        0x103,
        (
            "#522F#6P没办法啊……\x01",
            "又被对方逃走了。\x02\x03",

            "我们的行动\x01",
            "似乎完全都在她的掌握中呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_258A():

        label("loc_258A")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_258A")

    QueueWorkItem2(0x105, 1, lambda_258A)
    Sleep(100)

    def lambda_25A0():

        label("loc_25A0")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_25A0")

    QueueWorkItem2(0x107, 1, lambda_25A0)
    Sleep(400)

    ChrTalk(    #146
        0x105,
        "#042F#5P『黑衣女子』吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x103,
        "#022F#6P……嗯，没错的。\x02",
    )

    CloseMessageWindow()

    def lambda_25F2():
        OP_6D(-40, 0, 31820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25F2)
    OP_8E(0x103, 0xEEC, 0x0, 0x61A8, 0xBB8, 0x0)
    OP_8E(0x103, 0xEEC, 0x0, 0x7896, 0xBB8, 0x0)
    TurnDirection(0x103, 0x101, 400)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    OP_8C(0x105, 0, 400)
    OP_8C(0x107, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #148
        0x103,
        (
            "#022F#4P艾丝蒂尔……\x01",
            "先把大家都抬到床上吧。\x02\x03",

            "你来带路。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x7, 0x3E8)
    Sleep(500)

    ChrTalk(    #149
        0x101,
        "#1027F#5P啊……嗯……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    Call(0, 17)
    Return()

    # Function_9_1FFE end

    def Function_10_26CE(): pass

    label("Function_10_26CE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_26E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26E4)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF722, 0x0, 0x63D8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_26CE end

    def Function_11_2720(): pass

    label("Function_11_2720")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2736():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2736)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFFA92, 0x0, 0x5E4C, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_2720 end

    def Function_12_2772(): pass

    label("Function_12_2772")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2788():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2788)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x61BC, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_2772 end

    def Function_13_27DA(): pass

    label("Function_13_27DA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_27F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27F0)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF68C, 0x0, 0x5CE4, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_27DA end

    def Function_14_282C(): pass

    label("Function_14_282C")

    Sleep(1000)
    OP_8C(0xFE, 130, 400)
    OP_8E(0xFE, 0x41A, 0x0, 0x564A, 0xBB8, 0x0)
    OP_8C(0xFE, 220, 400)
    Sleep(500)
    OP_8C(0xFE, 130, 400)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_8E(0xFE, 0x3AC, 0x0, 0x4D30, 0xBB8, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x103, 0x80)
    Return()

    # Function_14_282C end

    def Function_15_2893(): pass

    label("Function_15_2893")

    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7D6, 0x0, 0x6A2C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_2893 end

    def Function_16_28B4(): pass

    label("Function_16_28B4")

    Sleep(1500)
    OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0x64F0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x68A6, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_28B4 end

    def Function_17_28FC(): pass

    label("Function_17_28FC")

    SetChrPos(0xB, -76340, 0, 31640, 180)
    SetChrPos(0xC, -73490, 0, 31660, 180)
    SetChrPos(0x8, -77060, 0, 3150, 180)
    SetChrPos(0xA, -73600, 0, 2980, 180)
    SetChrPos(0x9, -72950, 0, 2980, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -75750, 0, 2700, 270)
    SetChrPos(0x103, -74780, 0, 2600, 90)
    SetChrPos(0x105, -75080, 0, 31410, 270)
    SetChrPos(0x107, -74700, 0, 32159, 90)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xB, 1)
    SetChrSubChip(0xB, 7)
    SetChrChipByIndex(0xA, 1)
    SetChrSubChip(0xA, 55)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 71)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 39)
    SetChrChipByIndex(0xC, 1)
    SetChrSubChip(0xC, 23)
    OP_6F(0x5, 60)
    OP_6F(0x6, 60)
    OP_6F(0x7, 60)
    OP_6F(0x8, 60)
    OP_6D(-75020, 0, 33060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_1D(0x53)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    OP_6D(-76380, 0, 4030, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #150
        0x103,
        (
            "#025F总算都抬到床上了。\x02\x03",

            "#522F呼……\x01",
            "接下来该怎么做好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1027F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 500)
    Sleep(500)

    ChrTalk(    #152
        0x103,
        (
            "#022F艾丝蒂尔……\x02\x03",

            "我知道你很沮丧，\x01",
            "但现在必须赶快振作起来。\x02\x03",

            "不然的话，是没办法\x01",
            "让大家恢复清醒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1027F#5P……可是……\x01",
            "全都是因为我的不成熟才……\x02\x03",

            "我现在…还是连老爸的脚底都及不上……\x02\x03",

            "所以才会让缇欧她们\x01",
            "遭遇到这种事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x103,
        "#023F…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #155
        0x101,
        (
            "#1023F#5P迄今为止……\x01",
            "我虽然一直都在说些逞强的话……\x02\x03",

            "可是…\x01",
            "完全都只是在吹牛而已…\x02\x03",

            "这样下去的话…\x01",
            "还说什么追寻答案… \x02\x03",

            "#1027F我……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x103,
        (
            "#522F……………………………\x02\x03",

            "#026F……艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_2D3E():
        OP_6B(2900, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D3E)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 5)
    OP_0D()

    def lambda_2D5E():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D5E)
    Sleep(300)
    OP_22(0xA5, 0x0, 0x64)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    OP_99(0x103, 0x8, 0xE, 0x5DC)
    Sleep(500)

    ChrTalk(    #157
        0x101,
        "#1026F#5P啊……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x107, -67520, 0, -1240, 270)
    SetChrPos(0x105, -67520, 0, -1240, 270)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #158
        0x105,
        "#5P雪拉扎德！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x107,
        "#1P姐、姐姐！？\x02",
    )

    CloseMessageWindow()
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0x13)
    Sleep(1000)

    ChrTalk(    #160
        0x103,
        (
            "#022F……不成熟的不只是你。\x02\x03",

            "即使是我。\x01",
            "不也一样完全比不上老师吗。\x01",
            "但我从没气馁过，一直在努力提高自己。\x02\x03",

            "阿加特也是，金先生也是，\x01",
            "连卡西乌斯老师，也是一样…\x02\x03",

            "大家都会因自己的无力而痛苦懊恼，\x01",
            "但同时也都会继续拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1026F#5P老、老爸也……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x103,
        (
            "#522F你还记得吧？\x02\x03",

            "莱娜阿姨去世的时候，\x01",
            "老师并没能及时赶到… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1026F#5P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        (
            "#022F可是老师……\x01",
            "最终还是摆脱了失去莱娜阿姨的阴影，\x01",
            "步向了游击士的道路。\x02\x03",

            "并一直努力坚持，\x01",
            "守护着自己珍视的人。\x02\x03",

            "如今老师回归到了军队，\x01",
            "但他这种信念也不会有丝毫改变。\x02\x03",

            "#026F艾丝蒂尔……\x01",
            "你又该怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1003F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x103,
        (
            "#022F其实这并不难思考。\x02\x03",

            "只要明白自己内心\x01",
            "深处的真实想法就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1003F#5P………………………………\x02\x03",

            "答案…我现在还无法找到，但是…\x02\x03",

            "#1026F即使如此……我也会继续前进。\x02\x03",

            "为了保护最重要的人……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #168
        0x101,
        (
            "#1005F#5P虽然自己的力量还远远不够，\x01",
            "但我不会就这么放弃的！\x02",
        )
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        (
            "#524F呵呵……\x01",
            "你终于明白过来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #170
        0x101,
        (
            "#1025F#5P对不起，雪拉姐……\x02\x03",

            "我这个妹妹……\x01",
            "总是给你添麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        (
            "#027F呵呵，\x01",
            "那也是姐姐的义务啊。\x02\x03",

            "而且越是添麻烦的孩子\x01",
            "也就越可爱，对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#1015F#5P呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x107,
        "#061F嘻嘻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x105,
        "#041F#6P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #175
        0x101,
        (
            "#1008F#5P啊……抱、抱歉。\x02\x03",

            "让、让大家担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x107,
        (
            "#560F嗯，虽然吓了一跳，不过……\x02\x03",

            "姐姐和雪拉姐的关系\x01",
            "还真是好的没得说呢。\x02\x03",

            "#067F嘿嘿嘿……\x01",
            "我都有点嫉妒了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x105,
        (
            "#048F#6P呵呵，看到了这么感动的场面，\x01",
            "我也很满足呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#1013F#5P好、好了啦……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #179
        0x101,
        (
            "#1015F#5P那么，雪拉姐，咱们现在该怎么做？\x02\x03",

            "虽然应该马上回协会报告，\x01",
            "但是不能扔下缇欧她们不管…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#522F是啊……\x02\x03",

            "看来只能是你我之中的一个人\x01",
            "留在这里了… \x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, -68520, 0, -1240, 270)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #181
        0xD,
        "青年的声音",
        "#1P没有那个必要啦。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3511():

        label("loc_3511")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_3511")

    QueueWorkItem2(0x101, 1, lambda_3511)

    def lambda_3522():

        label("loc_3522")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_3522")

    QueueWorkItem2(0x103, 1, lambda_3522)

    def lambda_3533():

        label("loc_3533")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_3533")

    QueueWorkItem2(0x105, 1, lambda_3533)

    def lambda_3544():

        label("loc_3544")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_3544")

    QueueWorkItem2(0x107, 1, lambda_3544)

    def lambda_3555():
        OP_6D(-75100, 0, 2370, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3555)
    OP_4A(0xD, 255)
    ClearChrFlags(0xD, 0x80)

    def lambda_3576():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3576)
    OP_8E(0xD, 0xFFFEEE90, 0x0, 0xFFFFFBF0, 0x9C4, 0x0)
    OP_8E(0xD, 0xFFFEE526, 0x0, 0xB4, 0x9C4, 0x0)
    TurnDirection(0xD, 0x101, 400)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #182
        0x105,
        "#044F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x107,
        "#064F#5P呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x103,
        "#023F呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xD,
        (
            "#1062F#6P耶～大家好啊。\x01",
            "我是七耀教会的凯文。\x02\x03",

            "上次在王都分别后还没过多久嘛，\x01",
            "没想到这么快就又见面了呢。\x02\x03",

            "#1061F果然是女神的引导啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1020F#5P什、什么……\x02\x03",

            "为什么凯文先生会突然\x01",
            "出现在这里啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xD,
        (
            "#1066F#6P啊～说来也是很简单的啦。\x02\x03",

            "昨天夜里，迪拜恩教区长\x01",
            "将昏睡事件的报告\x01",
            "发到了王都的大圣堂。\x02\x03",

            "#1065F所以身为『星杯骑士』的我\x01",
            "就跑过来确认一下情况啦。\x02\x03",

            "穿过浓雾密布的街道，\x01",
            "今天早上好不容易才抵达洛连特。\x02\x03",

            "#1062F然后跑到协会就听说\x01",
            "你们现在因为工作\x01",
            "跑到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1007F#5P啊～好啦好啦。\x01",
            "事情的大概我明白了。\x02\x03",

            "#1019F说来说去，这根本就不算是什么\x01",
            "女神的引导嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xD,
        "#1066F#6P啊哈哈～～被揭穿了吗～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x103,
        (
            "#020F不过，凯文神父，\x02\x03",

            "你刚才说的『没有那个必要』\x01",
            "是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xD,
        (
            "#1060F#6P啊，就是说大姐你和艾丝蒂尔\x01",
            "没有必要留在这里了。\x02\x03",

            "这里交给我就好，\x01",
            "你们两个一起回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1004F#5P哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x105,
        "#542F#5P那、那样好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xD,
        (
            "#1071F#6P这也是神父的工作啊。\x02\x03",

            "我好歹也算是略通医术，\x01",
            "放心交给我就好了啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x107,
        (
            "#560F#5P那个……\x01",
            "真是谢谢了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x103,
        (
            "#021F呵呵，那么我们就\x01",
            "恭敬不如从命了。\x02\x03",

            "#020F各位！我们这就回洛连特！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        (
            "#1025F#5P嗯！\x02\x03",

            "凯文……\x01",
            "缇欧…就拜托你了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xD,
        (
            "#1060F#6P噢！\x01",
            "没问题，放心走吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6D(-73890, 0, 410, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrPos(0x0, -73890, 0, 410, 90)
    SetChrPos(0x1, -73890, 0, 410, 90)
    SetChrPos(0x2, -73890, 0, 410, 90)
    SetChrPos(0x3, -73890, 0, 410, 90)
    OP_69(0x0, 0x0)
    SetChrPos(0xD, -75610, 0, 2580, 270)
    OP_4B(0xD, 255)
    OP_A2(0x1822)
    OP_A2(0x0)
    OP_28(0x91, 0x1, 0x8)
    OP_28(0x91, 0x1, 0x10)
    OP_28(0x91, 0x1, 0x20)
    Sleep(500)
    OP_21()
    OP_1D(0xF)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_28FC end

    def Function_18_3B46(): pass

    label("Function_18_3B46")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3B57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B57)
    OP_8E(0xFE, 0xFFFED9DC, 0x0, 0x262, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_3B46 end

    def Function_19_3B7F(): pass

    label("Function_19_3B7F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3B90():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B90)
    OP_8E(0xFE, 0xFFFEDFC2, 0x0, 0xDC, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_3B7F end

    def Function_20_3BB8(): pass

    label("Function_20_3BB8")

    EventBegin(0x0)
    OP_4A(0xD, 255)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xD, -74400, 0, 300, 315)
    SetChrPos(0xB, -75940, 0, 930, 135)
    SetChrPos(0xC, -75950, 0, 180, 135)
    SetChrPos(0xA, -75640, 0, 1920, 135)
    SetChrPos(0x9, -74730, 0, 2000, 135)
    SetChrPos(0x8, -75270, 0, 2740, 135)
    SetChrChipByIndex(0xB, 9)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xA, 8)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0xC, 10)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(-72650, 0, 450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_3CCB():
        OP_6D(-75540, 0, 1480, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3CCB)
    FadeToBright(2000, 0)
    OP_62(0xD, 0x0, 2100, 0x26, 0x27, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_8C(0xD, 270, 400)
    Sleep(200)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_8C(0xD, 0, 400)
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_43(0x9, 0x1, 0x0, 0x15)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_63(0xD)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3BB8 end

    def Function_21_3D77(): pass

    label("Function_21_3D77")

    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(1000)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_8C(0xD, 270, 400)
    Return()

    # Function_21_3D77 end

    SaveToFile()

Try(main)
