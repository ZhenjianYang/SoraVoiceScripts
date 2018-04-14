from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0135   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0135.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60084",
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
        '托露塔',                               # 9
        '伊莉莎',                               # 10
        '德瑟鲁',                               # 11
        '福克纳',                               # 12
        '矿工提恩特',                           # 13
        '矿工彭兹',                             # 14
        '佩特洛夫船长',                         # 15
        '乘务员诺拉',                           # 16
        '潘杜老人',                             # 17
        '索斯摩夫',                             # 18
        '安敦',                                 # 19
        '利库斯',                               # 20
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
        'ED6_DT26/CH20330 ._CH',             # 00
        'ED6_DT07/CH02490 ._CH',             # 01
        'ED6_DT07/CH01280 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT26/CH20312 ._CH',             # 04
        'ED6_DT07/CH01503 ._CH',             # 05
        'ED6_DT07/CH01500 ._CH',             # 06
        'ED6_DT07/CH01443 ._CH',             # 07
        'ED6_DT07/CH01540 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01450 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01140 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT26/CH20330P._CP',             # 00
        'ED6_DT07/CH02490P._CP',             # 01
        'ED6_DT07/CH01280P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT26/CH20312P._CP',             # 04
        'ED6_DT07/CH01503P._CP',             # 05
        'ED6_DT07/CH01500P._CP',             # 06
        'ED6_DT07/CH01443P._CP',             # 07
        'ED6_DT07/CH01540P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01450P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01140P._CP',             # 0C
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 36450,
        Z                   = 0,
        Y                   = 126300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 39320,
        Z                   = 220,
        Y                   = 70940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 36640,
        Z                   = 0,
        Y                   = 72850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39470,
        Z                   = 1620,
        Y                   = 77070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 41000,
        Z                   = 1500,
        Y                   = 79500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 37050,
        Z                   = 0,
        Y                   = 75490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 41530,
        Z                   = 0,
        Y                   = 67550,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 44910,
        Z                   = 0,
        Y                   = 71790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 43750,
        Z                   = 0,
        Y                   = 73360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )


    DeclActor(
        TriggerX            = 35580,
        TriggerZ            = 0,
        TriggerY            = 74990,
        TriggerRange        = 800,
        ActorX              = 34500,
        ActorZ              = 1500,
        ActorY              = 75200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_32F",          # 01, 1
        "Function_2_33E",          # 02, 2
        "Function_3_4BB",          # 03, 3
        "Function_4_4C0",          # 04, 4
        "Function_5_782",          # 05, 5
        "Function_6_9C7",          # 06, 6
        "Function_7_A21",          # 07, 7
        "Function_8_B44",          # 08, 8
        "Function_9_C97",          # 09, 9
        "Function_10_FD5",         # 0A, 10
        "Function_11_104D",        # 0B, 11
        "Function_12_13DA",        # 0C, 12
        "Function_13_148A",        # 0D, 13
        "Function_14_1570",        # 0E, 14
        "Function_15_1673",        # 0F, 15
        "Function_16_1753",        # 10, 16
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2D0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 15)
    Jump("loc_32E")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_311")
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 2)
    SetChrPos(0x8, 88620, 0, 79000, 270)
    SetChrPos(0x9, 87090, 0, 79170, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_311")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_321")
    SetChrFlags(0x11, 0x80)

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E")
    SetChrFlags(0x10, 0x10)

    label("loc_32E")

    Return()

    # Function_0_2B6 end

    def Function_1_32F(): pass

    label("Function_1_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_33D")
    OP_6F(0x0, 10)

    label("loc_33D")

    Return()

    # Function_1_32F end

    def Function_2_33E(): pass

    label("Function_2_33E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4A5")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4A5")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4A5")

    label("loc_395")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4A5")

    label("loc_3AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4A5")

    label("loc_3C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4A5")

    label("loc_3E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4A5")

    label("loc_3F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4A5")

    label("loc_412")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4A5")

    label("loc_42B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_444")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4A5")

    label("loc_444")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4A5")

    label("loc_45D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4A5")

    label("loc_476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4A5")

    label("loc_48F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A5")

    label("loc_4BA")

    Return()

    # Function_2_33E end

    def Function_3_4BB(): pass

    label("Function_3_4BB")

    Call(0, 4)
    Return()

    # Function_3_4BB end

    def Function_4_4C0(): pass

    label("Function_4_4C0")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                  # 0
            "买东西\x01",                                # 1
            "招牌菜『三蛋黄杂烩粥』　1600米拉\x01",      # 2
            "离开\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x4)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_542")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_61B")
    SubMira(1600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x02三蛋黄杂烩粥\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x7D0)
    OP_31(0x1, 0xFD, 0x7D0)
    OP_31(0x2, 0xFD, 0x7D0)
    OP_31(0x3, 0xFD, 0x7D0)
    OP_31(0x4, 0xFD, 0x7D0)
    OP_31(0x5, 0xFD, 0x7D0)
    OP_31(0x6, 0xFD, 0x7D0)
    OP_31(0x7, 0xFD, 0x7D0)
    OP_31(0x8, 0xFD, 0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_5E1")
    Jump("loc_60D")

    label("loc_5E1")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x02三蛋黄杂烩粥\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_60D")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_641")

    label("loc_61B")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_641")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_653")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66D")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_66D")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_77E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6E1")

    ChrTalk(    #3
        0xB,
        (
            "夫人昏睡不起，\x01",
            "可老板还是像平常一样地工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "不过和平时相比，\x01",
            "精神还是差很多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E")

    label("loc_6E1")


    ChrTalk(    #5
        0xB,
        (
            "夫人昏睡不起，\x01",
            "可老板还是像平常一样地工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "不过和平时相比，\x01",
            "精神还是差很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "伊莉莎也为了照顾夫人\x01",
            "一直待在二楼……\x01",
            "现在就得靠我努力了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_77E")

    TalkEnd(0xB)
    Return()

    # Function_4_4C0 end

    def Function_5_782(): pass

    label("Function_5_782")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_9C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 4)), scpexpr(EXPR_END)), "loc_80D")

    ChrTalk(    #8
        0xFE,
        (
            "在这么消沉的夜晚，\x01",
            "酒馆可不能关门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "因为大家都怀抱着不安\x01",
            "聚集在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "抱歉，托露塔就\x01",
            "就拜托你们照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C3")

    label("loc_80D")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 3)), scpexpr(EXPR_END)), "loc_853")

    ChrTalk(    #11
        0xFE,
        "哟，是艾丝蒂尔你们啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_87E")

    label("loc_853")


    ChrTalk(    #12
        0xFE,
        (
            "哟，艾丝蒂尔和雪拉扎德。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87E")


    ChrTalk(    #13
        0x101,
        "#1003F德瑟鲁大叔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "抱歉，托露塔就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "我也想过今晚\x01",
            "要不要关门……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "不过在这么消沉的夜晚，\x01",
            "大家都想来喝上一杯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "作为城里唯一的酒馆，\x01",
            "自然不能关门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1010F这样啊……\x02\x03",

            "#1002F嗯……明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#020F如果发现了什么\x01",
            "我们会再来通知的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #20
        0xFE,
        "……嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "就靠你们了，游击士。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1894)

    label("loc_9C3")

    TalkEnd(0xA)
    Return()

    # Function_5_782 end

    def Function_6_9C7(): pass

    label("Function_6_9C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D6")
    Call(0, 16)
    Jump("loc_A20")

    label("loc_9D6")

    TalkBegin(0x9)

    ChrTalk(    #22
        0x9,
        (
            "艾丝蒂尔～\x01",
            "妈妈就拜托了\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "我已经不要紧了，\x01",
            "请你们努力调查。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_A20")

    Return()

    # Function_6_9C7 end

    def Function_7_A21(): pass

    label("Function_7_A21")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A8B")

    ChrTalk(    #24
        0xFE,
        (
            "今天的雾……\x01",
            "我以前从没见过这么厉害的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "如果明天也不天晴，\x01",
            "真不想去工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B40")

    label("loc_A8B")


    ChrTalk(    #26
        0xFE,
        (
            "嘎嘎嘎嘎…\x01",
            "…包子…虽然很好吃……嘎嘎\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "啪咕啪啪咕啪…\x01",
            "今…今天…的雾…雾真的…咕咕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "咯咯咯咯咯咯咯咯…\x01",
            "如…如果明天…也不晴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "…………嗝。\x01",
            "真不想去工作啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B40")

    TalkEnd(0xC)
    Return()

    # Function_7_A21 end

    def Function_8_B44(): pass

    label("Function_8_B44")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B9D")

    ChrTalk(    #30
        0xFE,
        (
            "也没必要翘班\x01",
            "过来吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "真希望他能把这股子劲用在工作上。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_B9D")


    ChrTalk(    #32
        0xFE,
        (
            "提恩特那家伙……\x01",
            "今天又迟到了很久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "他的理由是在雾中迷路了，不过\x01",
            "真正的原因肯定是去吃东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "那家伙的贪吃\x01",
            "可是有名的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "这样在工作中溜出矿山\x01",
            "跑到这里来吃饭的那股劲儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "要是用在工作中的话，\x01",
            "他的作用起码是现在的十倍。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_C93")

    TalkEnd(0xD)
    Return()

    # Function_8_B44 end

    def Function_9_C97(): pass

    label("Function_9_C97")

    TalkBegin(0xE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CBC")
    SetChrSubChip(0xFE, 2)
    Jump("loc_CD7")

    label("loc_CBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD2")
    SetChrSubChip(0xFE, 2)
    Jump("loc_CD7")

    label("loc_CD2")

    SetChrSubChip(0xFE, 1)

    label("loc_CD7")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_DEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D4C")

    ChrTalk(    #37
        0xFE,
        (
            "虽然对不起乘客，\x01",
            "不过天气不好也没有办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "现在最多也就是祈求\x01",
            "雾赶快散去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE7")

    label("loc_D4C")


    ChrTalk(    #39
        0xFE,
        (
            "哟，这不是\x01",
            "游击士们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "我们这些乘务员今天\x01",
            "也都停留在洛连特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "总之在天气恢复之前，\x01",
            "只能保持这个状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "总之现在只能\x01",
            "祈求女神了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_DE7")

    Jump("loc_FCC")

    label("loc_DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_E67")

    ChrTalk(    #43
        0xFE,
        (
            "怎么？这回是\x01",
            "来找索斯摩夫的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "那家伙刚才\x01",
            "回了飞船坪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "他这人有点古怪，\x01",
            "一定待在一些奇怪的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCC")

    label("loc_E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_ED3")

    ChrTalk(    #46
        0xFE,
        "你们在找库因特吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "那家伙很早就\x01",
            "吃完饭出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "哼，肯定又是翘班\x01",
            "在街上闲逛吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCC")

    label("loc_ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F31")

    ChrTalk(    #49
        0xFE,
        (
            "虽然对不起乘客，\x01",
            "不过天气不好也没有办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "现在最多也就是祈求\x01",
            "雾赶快散去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCC")

    label("loc_F31")


    ChrTalk(    #51
        0xFE,
        (
            "哟，这不是\x01",
            "游击士们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "我们这些乘务员今天\x01",
            "也都停留在洛连特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "总之在天气恢复之前，\x01",
            "只能保持这个状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "总之现在只能\x01",
            "祈求女神了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_FCC")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xE)
    Return()

    # Function_9_C97 end

    def Function_10_FD5(): pass

    label("Function_10_FD5")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1008")

    ChrTalk(    #55
        0xFE,
        (
            "呼，到底什么时候\x01",
            "出发呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1049")

    label("loc_1008")


    ChrTalk(    #56
        0xFE,
        (
            "呼，到底什么时候\x01",
            "出发呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "我实在是\x01",
            "等得受不了了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1049")

    TalkEnd(0xF)
    Return()

    # Function_10_FD5 end

    def Function_11_104D(): pass

    label("Function_11_104D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_13D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_END)), "loc_13A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 0)), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #58
        0xFE,
        (
            "那时候我要是在钟楼\x01",
            "就不会让小家伙上去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "偏偏在那种时候离开，\x01",
            "我真生自己的气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A3")

    label("loc_10C4")

    ClearChrFlags(0xFE, 0x10)

    ChrTalk(    #60
        0xFE,
        "鲁克那小家伙还好吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "真希望他没事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1002F……目前看来还可以。\x02\x03",

            "虽然没有醒，\x01",
            "不过只是睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #63
        0xFE,
        (
            "哟，这不是卡西乌斯的\x01",
            "调皮女儿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "是吗……\x01",
            "你去看过小家伙了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1000F嗯，协会正在调查。\x02\x03",

            "是潘杜爷爷您把\x01",
            "鲁克送回家的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "唉，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "他在钟楼上\x01",
            "昏倒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#020F当时有没有\x01",
            "发生什么奇怪的事？\x02\x03",

            "就算是些细微的小事\x01",
            "也请告诉我们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #69
        0xFE,
        "唔，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "我当时满脑子都在想\x01",
            "鲁克的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "很遗憾，其他的事\x01",
            "都记不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1015F是吗……\x01",
            "嗯，人在那时都会那样的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #73
        0xFE,
        "抱歉，帮不了你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020F不，能确认到没发生\x01",
            "什么特别的事已经很好了。\x02\x03",

            "感谢您的合作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1016F可别喝太多哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "嗯，这我知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "那么就这样。\x01",
            "你们也要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1898)

    label("loc_13A3")

    Jump("loc_13D6")

    label("loc_13A6")


    ChrTalk(    #78
        0xFE,
        "鲁克那小家伙还好吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "真希望他没事……\x02",
    )

    CloseMessageWindow()

    label("loc_13D6")

    TalkEnd(0x10)
    Return()

    # Function_11_104D end

    def Function_12_13DA(): pass

    label("Function_12_13DA")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1427")

    ChrTalk(    #80
        0xFE,
        "呼……吃饱了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "肚子也胀起来了，\x01",
            "得赶紧回去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1486")

    label("loc_1427")


    ChrTalk(    #82
        0xFE,
        "呼……吃饱了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "好久没吃过这么\x01",
            "象样的晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "肚子也胀起来了，\x01",
            "得赶紧回去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1486")

    TalkEnd(0x11)
    Return()

    # Function_12_13DA end

    def Function_13_148A(): pass

    label("Function_13_148A")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_156C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_14E4")

    ChrTalk(    #85
        0xFE,
        (
            "明天起得收集那位\x01",
            "小姐的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "嗯，想要认识她\x01",
            "首先要有努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156C")

    label("loc_14E4")


    ChrTalk(    #87
        0xFE,
        "啊，金发的小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "真想不到会有\x01",
            "那么动人的女性……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "偶然发生在乡间的\x01",
            "冲动的相遇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "这已经是女神的引导\x01",
            "和命令了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_156C")

    TalkEnd(0x12)
    Return()

    # Function_13_148A end

    def Function_14_1570(): pass

    label("Function_14_1570")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_166F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_15CC")

    ChrTalk(    #91
        0xFE,
        (
            "我那个同伴\x01",
            "好像对谁一见钟情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "不过他经常这样，\x01",
            "也不用介意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166F")

    label("loc_15CC")


    ChrTalk(    #93
        0xFE,
        (
            "总觉得我那个同伴……\x01",
            "好像对谁一见钟情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "今晚他又要\x01",
            "张口闭口提那个女人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "不过他经常这样，\x01",
            "也不用介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "忽冷忽热的……\x01",
            "安敦就是这样的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_166F")

    TalkEnd(0x13)
    Return()

    # Function_14_1570 end

    def Function_15_1673(): pass

    label("Function_15_1673")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_6F(0x0, 10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 2)
    SetChrPos(0x8, 88620, 0, 79000, 270)
    SetChrPos(0x9, 87090, 0, 79170, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(82660, 0, 80340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(86990, 0, 80450, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0112   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1673 end

    def Function_16_1753(): pass

    label("Function_16_1753")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, 86750, 0, 80570, 180)
    SetChrPos(0x103, 87440, 0, 80930, 180)
    SetChrPos(0xF8, 85880, 0, 80850, 135)
    SetChrPos(0xF9, 85060, 0, 80750, 135)
    OP_8C(0x9, 0, 0)
    OP_6D(86420, 0, 80630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1879")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没和伊莉莎再会】\x01",      # 0
            "【◇已和伊莉莎再会】\x01",      # 1
            "【◇不变更】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_186D"),
        (1, "loc_1873"),
        (SWITCH_DEFAULT, "loc_1879"),
    )


    label("loc_186D")

    OP_A3(0x1882)
    Jump("loc_1879")

    label("loc_1873")

    OP_A2(0x1882)
    Jump("loc_1879")

    label("loc_1879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")

    ChrTalk(    #97
        0xFE,
        "#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1008F嗯……\x01",
            "好久不见，伊莉莎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#6P哇，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "#6P太好了～\x01",
            "看来训练顺利结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "#6P担心死我了～\x01",
            "你总算是回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1016F对不起，\x01",
            "这么晚才来跟你见面。\x02\x03",

            "#1015F先不说这个了……\x01",
            "阿姨的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19CB")

    label("loc_1971")


    ChrTalk(    #103
        0xFE,
        (
            "#6P啊，艾丝蒂尔，\x01",
            "还有雪拉扎德小姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1025F晚上好，伊莉莎。\x02\x03",

            "阿姨的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CB")


    ChrTalk(    #105
        0xFE,
        (
            "#6P唔～看上去只是在\x01",
            "安稳地睡觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "#6P不管是摇她还是叫她，\x01",
            "她一点反应都没有～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "#6P教区长先生虽然说\x01",
            "不必担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1003F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        (
            "#020F#2P我们是受市长先生的委托\x01",
            "来调查此事件的。\x02\x03",

            "能不能请你配合一下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "#6P啊，好，当然没问题～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#6P请随便问吧～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1015F那么……\x02\x03",

            "#1002F首先，阿姨是在\x01",
            "何时何地昏倒在地的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "#6P啊，嗯……～？\x01",
            "时间是傍晚的５点左右吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "#6P我和妈妈在外面的阳台上\x01",
            "收拾椅子什么的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x103,
        "#023F#2P阳台上的椅子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "#6P嗯，这种雾天\x01",
            "不是很潮湿吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "#6P好不容易糊好了一楼的墙壁，\x01",
            "想想二楼的椅子也该收拾一下～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        "#026F#2P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "#6P在收拾的过程中\x01",
            "爸爸叫我下楼去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "#6P再回来时妈妈已经\x01",
            "靠在椅子上睡着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1002F是这样啊……\x01",
            "阿姨睡着时你不在场？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "#6P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "#6P然后我怎么叫她\x01",
            "她也不醒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "#6P我就赶紧叫来爸爸\x01",
            "把她背到了二楼的床上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#6P然后……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1025F伊莉莎……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)
    OP_8F(0x101, 0x15414, 0x0, 0x13718, 0x3E8, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    Sleep(500)
    OP_99(0x9, 0x1, 0x2, 0x3E8)
    Sleep(1000)

    ChrTalk(    #128
        0xFE,
        "#6P呵呵，对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "#6P看到艾丝蒂尔你们来了\x01",
            "总算松了一口气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1012F#5P嗯……我知道。\x02\x03",

            "不会有事的，不要勉强自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#6P嗯……\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x2, 0x0, 0x3E8)
    Sleep(500)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_8F(0x101, 0x153D8, 0x0, 0x1386C, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #132
        0xFE,
        "#6P谢谢～我已经没事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "#6P还有没有什么其他要问的吗～？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x40)

    ChrTalk(    #134
        0x101,
        (
            "#1007F#5P唔…让我想想。\x02\x03",

            "#1015F雪拉姐，你呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        (
            "#026F#2P是啊……\x02\x03",

            "#022F在你妈妈昏睡前后\x01",
            "有没有发生过什么怪事？\x02\x03",

            "比如有陌生人来过之类的，\x01",
            "或者听到怪异的声音？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "#6P陌生人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "#6P说起来，我被爸爸\x01",
            "叫下楼的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "#6P我看到有个女人\x01",
            "从钟楼走出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#023F#2P女人……\x01",
            "是洛连特的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "#6P不，虽然她站在雾中，\x01",
            "看不清脸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "#6P不过她的服饰设计得很不可思议，\x01",
            "我觉得像是旅行者～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1004F#5P设计得不可思议……\x01",
            "哪里不可思议？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "#6P唔，像是舒适的\x01",
            "黑色礼服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "#6P不过雾那么浓，\x01",
            "具体细节实在看不清～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1006F#5P是吗……\x01",
            "不过这可能是重要的目击情报，\x02\x03",

            "得去向爱娜姐报告一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        (
            "#026F#2P嗯……是啊。\x02\x03",

            "#020F谢谢你，伊莉莎。\x01",
            "告诉了我们这么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "#6P啊，哪里哪里～\x01",
            "你们工作辛苦了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1006F#5P阿姨的事\x01",
            "就交给我们吧。\x02\x03",

            "我们一定会找出\x01",
            "办法让她醒过来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "#6P嗯……\x01",
            "谢谢你～艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(82980, 0, 80630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 82980, 0, 80630, 270)
    SetChrPos(0x103, 82980, 0, 80630, 270)
    SetChrPos(0xF8, 82980, 0, 80630, 270)
    SetChrPos(0xF9, 82980, 0, 80630, 270)
    OP_8C(0x9, 90, 0)
    OP_4B(0x9, 255)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_A2(0x1814)
    OP_28(0x90, 0x2, 0x8)
    OP_28(0x90, 0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2298")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_2298")

    label("loc_2298")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_16_1753 end

    SaveToFile()

Try(main)
