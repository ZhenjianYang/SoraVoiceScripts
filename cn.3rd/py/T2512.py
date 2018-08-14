from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2512   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '罗基克',                               # 9
        '汉斯',                                 # 10
        '露西',                                 # 11
        '米丽亚老师',                           # 12
        '艾福托老师',                           # 13
        '塞尔玛',                               # 14
        '德尼斯',                               # 15
        '雅莉丝',                               # 16
        '米克',                                 # 17
        '目标用照相机',                         # 18
        '',                                     # 19
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
        'ED6_DT07/CH01080 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02690 ._CH',             # 02
        'ED6_DT07/CH01430 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01090 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01590 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01080P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02690P._CP',             # 02
        'ED6_DT07/CH01430P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01090P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01590P._CP',             # 07
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -120030,
        Z                   = 0,
        Y                   = 30750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 29010,
        Z                   = 0,
        Y                   = 28300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -61790,
        Z                   = 0,
        Y                   = -1780,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -29380,
        Z                   = 0,
        Y                   = 880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -60240,
        Z                   = 0,
        Y                   = 24290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -29120,
        Z                   = 0,
        Y                   = 24590,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_303",          # 01, 1
        "Function_2_30D",          # 02, 2
        "Function_3_48A",          # 03, 3
        "Function_4_4AE",          # 04, 4
        "Function_5_4D2",          # 05, 5
        "Function_6_4F6",          # 06, 6
        "Function_7_51A",          # 07, 7
        "Function_8_615",          # 08, 8
        "Function_9_7F7",          # 09, 9
        "Function_10_A4C",         # 0A, 10
        "Function_11_BF3",         # 0B, 11
        "Function_12_D40",         # 0C, 12
        "Function_13_F52",         # 0D, 13
        "Function_14_1032",        # 0E, 14
        "Function_15_1117",        # 0F, 15
        "Function_16_120D",        # 10, 16
        "Function_17_165C",        # 11, 17
        "Function_18_1ADC",        # 12, 18
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_27B")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1620, 0, -4100, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -720, 0, -4100, 270)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_2D2")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_28A")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_2D2")

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_29E")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_2D2")

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1480, 0, -2400, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    SetChrFlags(0x10, 0x10)

    label("loc_2C8")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_2D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_302")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_302")

    Return()

    # Function_0_22A end

    def Function_1_303(): pass

    label("Function_1_303")

    OP_B1("t2512_n")
    Return()

    # Function_1_303 end

    def Function_2_30D(): pass

    label("Function_2_30D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_474")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_474")

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_364")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_474")

    label("loc_364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_474")

    label("loc_37D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_474")

    label("loc_396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_474")

    label("loc_3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_474")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_474")

    label("loc_3E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_474")

    label("loc_3FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_474")

    label("loc_413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_474")

    label("loc_42C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_445")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_474")

    label("loc_445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_474")

    label("loc_45E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_474")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_489")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_474")

    label("loc_489")

    Return()

    # Function_2_30D end

    def Function_3_48A(): pass

    label("Function_3_48A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AD")
    OP_8D(0xFE, -1040, -3130, -430, -5120, 2000)
    Jump("Function_3_48A")

    label("loc_4AD")

    Return()

    # Function_3_48A end

    def Function_4_4AE(): pass

    label("Function_4_4AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D1")
    OP_8D(0xFE, 1840, -4950, 1050, -3130, 2000)
    Jump("Function_4_4AE")

    label("loc_4D1")

    Return()

    # Function_4_4AE end

    def Function_5_4D2(): pass

    label("Function_5_4D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F5")
    OP_8D(0xFE, -59450, 25230, -61220, 23390, 2000)
    Jump("Function_5_4D2")

    label("loc_4F5")

    Return()

    # Function_5_4D2 end

    def Function_6_4F6(): pass

    label("Function_6_4F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_519")
    OP_8D(0xFE, -30480, 23230, -28100, 25610, 1500)
    Jump("Function_6_4F6")

    label("loc_519")

    Return()

    # Function_6_4F6 end

    def Function_7_51A(): pass

    label("Function_7_51A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_END)), "loc_60D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_576")

    ChrTalk(    #0
        0xFE,
        "这次定期考试是关键了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "当然我可是\x01",
            "没打算认输的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60A")

    label("loc_576")


    ChrTalk(    #2
        0xFE,
        (
            "我打算向学长\x01",
            "借些优秀的参考书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "现在正让人家\x01",
            "帮忙找呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "……我也不打算\x01",
            "在考试上输给你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "你也要\x01",
            "努力加油啊！\x02",
        )
    )

    Jump("loc_606")

    label("loc_606")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_60A")

    Jump("loc_611")

    label("loc_60D")

    Call(0, 16)

    label("loc_611")

    TalkEnd(0xFE)
    Return()

    # Function_7_51A end

    def Function_8_615(): pass

    label("Function_8_615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_622")
    Jump("loc_7F3")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_62C")
    Jump("loc_7F3")

    label("loc_62C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_636")
    Jump("loc_7F3")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_697")

    ChrTalk(    #6
        0xFE,
        (
            "要想得高分，\x01",
            "就要提早准备呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "首先开始\x01",
            "做总结笔记吧。\x02",
        )
    )

    Jump("loc_693")

    label("loc_693")

    CloseMessageWindow()
    Jump("loc_712")

    label("loc_697")


    ChrTalk(    #8
        0xFE,
        "呵呵，很快就该定期考试了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "我也差不多要\x01",
            "开始备考复习了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "要想得高分，\x01",
            "现在就得开始准备才行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_712")

    Jump("loc_7F3")

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_7F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_774")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #11
        0xFE,
        "唔，哪本比较好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "这个可能\x01",
            "有点太难了啊……\x02",
        )
    )

    Jump("loc_770")

    label("loc_770")

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_774")


    ChrTalk(    #13
        0xFE,
        (
            "罗基克君\x01",
            "要我借他参考书，\x01",
            "我正在找适合他的呢。\x02",
        )
    )

    Jump("loc_7B5")

    label("loc_7B5")

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "看来他对学习也很认真。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "呵呵，我也很高兴啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7F3")

    TalkEnd(0xFE)
    Return()

    # Function_8_615 end

    def Function_9_7F7(): pass

    label("Function_9_7F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 4)), scpexpr(EXPR_END)), "loc_90F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_877")

    ChrTalk(    #16
        0x11,
        (
            "#730F我和露西学姐\x01",
            "再到这附近找找看。\x02\x03",

            "科洛丝，\x01",
            "你去乔儿那里露个面吧。\x02",
        )
    )

    Jump("loc_873")

    label("loc_873")

    CloseMessageWindow()
    Jump("loc_90C")

    label("loc_877")


    ChrTalk(    #17
        0x11,
        (
            "#730F看来雷克特同学\x01",
            "不在这附近的样子啊……\x02\x03",

            "#736F不，\x01",
            "说不定是假装不在藏起来了而已……\x02\x03",

            "#734F唉，真是麻烦的人啊。\x02",
        )
    )

    Jump("loc_908")

    label("loc_908")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_90C")

    Jump("loc_A20")

    label("loc_90F")


    ChrTalk(    #18
        0x11,
        (
            "#733F啊，科洛丝……\x02\x03",

            "#732F…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x105,
        "#044F嗯，汉斯君……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#735F不，没什么。\x02\x03",

            "#730F看来雷克特同学\x01",
            "好像不在这附近啊。\x02\x03",

            "科洛丝……对了，\x01",
            "你就先去\x01",
            "乔儿那里露个面吧。\x02",
        )
    )

    Jump("loc_A1C")

    label("loc_A1C")

    CloseMessageWindow()
    OP_A2(0x2F7C)

    label("loc_A20")

    Jump("loc_A48")

    label("loc_A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_A2D")
    Jump("loc_A48")

    label("loc_A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_A37")
    Jump("loc_A48")

    label("loc_A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_A41")
    Jump("loc_A48")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_A48")

    label("loc_A48")

    TalkEnd(0xFE)
    Return()

    # Function_9_7F7 end

    def Function_10_A4C(): pass

    label("Function_10_A4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_AA6")

    ChrTalk(    #21
        0xFE,
        "不过，还有课要上吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "莫非，\x01",
            "只有我一个人闲着？\x02",
        )
    )

    Jump("loc_AA2")

    label("loc_AA2")

    CloseMessageWindow()
    Jump("loc_AE7")

    label("loc_AA6")


    ChrTalk(    #23
        0xFE,
        "很快就是期待已久的长假了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "好～要干些什么呢～㈱\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_AE7")

    Jump("loc_BEF")

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_AF4")
    Jump("loc_BEF")

    label("loc_AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_AFE")
    Jump("loc_BEF")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_B08")
    Jump("loc_BEF")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B75")

    ChrTalk(    #25
        0xFE,
        (
            "露西同学\x01",
            "真是好漂亮啊～\x02",
        )
    )

    Jump("loc_B40")

    label("loc_B40")

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "我也想要\x01",
            "那样飘逸的长发啊……\x02",
        )
    )

    Jump("loc_B71")

    label("loc_B71")

    CloseMessageWindow()
    Jump("loc_BEF")

    label("loc_B75")


    ChrTalk(    #27
        0xFE,
        (
            "露西同学\x01",
            "真是好漂亮啊～\x02",
        )
    )

    Jump("loc_B9F")

    label("loc_B9F")

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "听说她是从北方\x01",
            "雷米菲利亚公国\x01",
            "留学来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "啊，真令人憧憬呀～㈱\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_BEF")

    TalkEnd(0xFE)
    Return()

    # Function_10_A4C end

    def Function_11_BF3(): pass

    label("Function_11_BF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C61")

    ChrTalk(    #30
        0xFE,
        (
            "……话先说在前头，\x01",
            "我可不是在偷懒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "只是现在\x01",
            "没心情改卷子啦！\x02",
        )
    )

    Jump("loc_C5D")

    label("loc_C5D")

    CloseMessageWindow()
    Jump("loc_D3C")

    label("loc_C61")


    ChrTalk(    #32
        0xFE,
        (
            "刚才我在职员室\x01",
            "批改试卷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "雷克特那笨蛋\x01",
            "竟然大摇大摆走进来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "『哟～米丽亚，在干什么呢？』\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "『这就开始改卷啦，真辛苦啊～☆』\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0xFE,
        "…………竟然给我说这种话！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_D3C")

    TalkEnd(0xFE)
    Return()

    # Function_11_BF3 end

    def Function_12_D40(): pass

    label("Function_12_D40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_F4E")
    OP_8C(0xFE, 270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_E26")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05艾福托老师闭着眼睛。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_DAE():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_DAE)

    ChrTalk(    #38
        0xFE,
        "恶、恶魔……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "快给我住口……！！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #40
        0x105,
        (
            "#047F（到底\x01",
            "  被说了什么呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xFE, 0x3)
    Jump("loc_F4E")

    label("loc_E26")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_E5A():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_E5A)

    ChrTalk(    #41
        0xFE,
        (
            "别、别说了，雷克特！\x01",
            "那才不是我！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        "#044F那、那个…………？\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(300)

    ChrTalk(    #43
        0xFE,
        "别、别吓唬我啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "我还以为是那家伙呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        (
            "#045F（艾福托老师……\x01",
            "  被学长捉弄了吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xFE, 0x3)
    OP_A2(0x5)

    label("loc_F4E")

    TalkEnd(0xFE)
    Return()

    # Function_12_D40 end

    def Function_13_F52(): pass

    label("Function_13_F52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_102E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_FC5")

    ChrTalk(    #46
        0xFE,
        (
            "虽然我父母一开始\x01",
            "是反对我入学的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "呵呵，\x01",
            "能够这样勤奋学习也很开心呢。\x02",
        )
    )

    Jump("loc_FC1")

    label("loc_FC1")

    CloseMessageWindow()
    Jump("loc_102E")

    label("loc_FC5")


    ChrTalk(    #48
        0xFE,
        (
            "好了，\x01",
            "差不多该预习明天的功课了。\x02",
        )
    )

    Jump("loc_FF6")

    label("loc_FF6")

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "呵呵，\x01",
            "能够这样勤奋学习也很开心呢。\x02",
        )
    )

    Jump("loc_102A")

    label("loc_102A")

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_102E")

    TalkEnd(0xFE)
    Return()

    # Function_13_F52 end

    def Function_14_1032(): pass

    label("Function_14_1032")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_108F")

    ChrTalk(    #50
        0x12,
        (
            "#1793F………不在呢。\x02\x03",

            "下次逮到他时\x01",
            "该怎么处置好呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1113")

    label("loc_108F")


    ChrTalk(    #51
        0x12,
        (
            "#1790F哎呀，科洛丝……\x02\x03",

            "#1790F找到雷克特了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#045F不，还没有……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        "#1795F是吗…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1113")

    TalkEnd(0xFE)
    Return()

    # Function_14_1032 end

    def Function_15_1117(): pass

    label("Function_15_1117")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1177")

    ChrTalk(    #54
        0xFE,
        (
            "为什么老师\x01",
            "会在那种地方转悠？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "难不成我之前\x01",
            "逃课被发现了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_1177")


    ChrTalk(    #56
        0xFE,
        (
            "我肚子饿了正准备去食堂，\x01",
            "却被堵在这儿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "刚才艾福托老师\x01",
            "就在宿舍前转来转去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "啊～\x01",
            "要是被发现了就肯定糟了啊～……\x02",
        )
    )

    Jump("loc_1205")

    label("loc_1205")

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1209")

    TalkEnd(0xFE)
    Return()

    # Function_15_1117 end

    def Function_16_120D(): pass

    label("Function_16_120D")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(700, 0, -2400, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 1480, 0, -3900, 0)
    SetChrSubChip(0x10, 0)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x10, 0x105, 400)
    Sleep(300)

    ChrTalk(    #59
        0x10,
        "#11P唔……你是………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#11P科洛丝·琳希同学。\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        (
            "#045F#6P嗯，那个……\x02\x03",

            "#542F老师让我\x01",
            "来发资料……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #62
        "\x07\x05把资料交给罗基克。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #63
        0x10,
        "#11P唔，这是今年的学分表……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 0, 500)
    Sleep(100)

    ChrTalk(    #64
        0x10,
        "#5P这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#5P一年中公共课的\x01",
            "比重很大啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#5P唔，体育有５个学分！？\x02\x03",

            "不……不可能………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        (
            "#542F#6P（…………唔。）\x02\x03",

            "（还是不要打扰他比较好。）\x02\x03",

            "#045F那么，我先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 600)

    def lambda_14B7():
        OP_8E(0xFE, 0x5C8, 0x0, 0xFFFFEA84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14B7)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10, 180, 600)

    ChrTalk(    #68
        0x10,
        "#11P等、等一下！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #69
        0x105,
        "#044F#6P咦……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Sleep(300)

    ChrTalk(    #70
        0x10,
        "#11P…………不，没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#11P根据资料来看，\x01",
            "定期考试应该在六个星期以后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#11P你也要\x01",
            "努力学习哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#11P疏忽、大意、不小心……\x01",
            "之类的借口可是行不通的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x105,
        (
            "#044F#6P是、是。\x02\x03",

            "#543F我会尽全力\x01",
            "认真复习的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F68)
    OP_8C(0x10, 0, 400)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_16_120D end

    def Function_17_165C(): pass

    label("Function_17_165C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-840, 0, -2820, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrPos(0x11, 1620, 0, -4100, 90)
    SetChrPos(0x12, -720, 0, -4100, 270)
    SetChrFlags(0x105, 0x8)

    def lambda_16E9():
        OP_6B(3100, 6000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_16E9)
    FadeToBright(1000, 0)
    OP_43(0x12, 0x3, 0x0, 0x12)
    Sleep(200)
    OP_8C(0x11, 45, 500)
    Sleep(800)
    OP_8C(0x11, 135, 500)
    Sleep(800)
    OP_8C(0x11, 45, 500)
    Sleep(800)
    OP_8C(0x11, 90, 500)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #75
        0x11,
        "#737F#5P（和露西学姐单独两个人……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #76
        0x11,
        "#738F#12P那个～露西学～姐～……\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0x3)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x12, 0x11, 400)
    Sleep(300)

    ChrTalk(    #77
        0x12,
        "#1790F#5P什么事，汉斯君。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "#739F#12P哎嘿～……没什么～……\x01",
            "就是说呢～…………\x02\x03",

            "#738F你觉得这个世界上\x01",
            "最重要的东西是什么呢～？\x02\x03",

            "果然，还是#200W爱#120W……#20W对吧㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x12,
        (
            "#1794F#5P嗯～……这个啊……\x02\x03",

            "最重要的东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #80
        0x12,
        "#1792F#5P#80W那是…………#20W暴力吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        "#731F#12P………………咦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #82
        0x12,
        (
            "#1793F#5P唉，不知怎么……\x02\x03",

            "我又手痒起来\x01",
            "想扁雷克特那家伙了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#735F#12P露西学姐……\x02\x03",

            "#737F（如果是我的话，扁我多少次都行！）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x8)
    OP_6D(0, -250, -7230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4B(0x11, 255)
    OP_4B(0x12, 255)
    SetChrPos(0x11, 1620, 0, -4100, 90)
    SetChrPos(0x12, -720, 0, -4100, 270)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_A2(0x2F70)
    EventEnd(0x0)
    Return()

    # Function_17_165C end

    def Function_18_1ADC(): pass

    label("Function_18_1ADC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B30")
    OP_8C(0x12, 225, 500)
    Sleep(800)
    OP_8C(0x12, 315, 500)
    Sleep(800)
    OP_8C(0x12, 270, 500)
    Sleep(1200)
    OP_8C(0x12, 315, 500)
    Sleep(800)
    OP_8C(0x12, 225, 500)
    Sleep(800)
    OP_8C(0x12, 270, 500)
    Sleep(1200)
    Jump("Function_18_1ADC")

    label("loc_1B30")

    Return()

    # Function_18_1ADC end

    SaveToFile()

Try(main)
