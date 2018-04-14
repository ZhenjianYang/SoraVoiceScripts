from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4400   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4400.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '拉利',                                 # 9
        '游客',                                 # 10
        '游客',                                 # 11
        '游客',                                 # 12
        '港口工人',                             # 13
        '港口工人',                             # 14
        '港口工人',                             # 15
        '作业员',                               # 16
        '作业员',                               # 17
        '港口工人',                             # 18
        '王都格兰赛尔·西街区',                 # 19
        '王都格兰赛尔·码头北',                 # 20
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
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01530 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT06/CH20159 ._CH',             # 06
        'ED6_DT07/CH01450 ._CH',             # 07
        'ED6_DT07/CH01550 ._CH',             # 08
        'ED6_DT07/CH01500 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01530P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT06/CH20159P._CP',             # 06
        'ED6_DT07/CH01450P._CP',             # 07
        'ED6_DT07/CH01550P._CP',             # 08
        'ED6_DT07/CH01500P._CP',             # 09
    )

    DeclNpc(
        X                   = -8750,
        Z                   = 0,
        Y                   = -3530,
        Direction           = 268,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 22130,
        Z                   = 0,
        Y                   = -5230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24260,
        Z                   = 0,
        Y                   = -5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 23230,
        Z                   = 0,
        Y                   = -5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 13390,
        Z                   = 0,
        Y                   = 2850,
        Direction           = 90,
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
        X                   = 14890,
        Z                   = 0,
        Y                   = 2850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -22680,
        Z                   = 0,
        Y                   = -15490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -18690,
        Z                   = 0,
        Y                   = 6110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -17670,
        Z                   = 0,
        Y                   = 7510,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -15960,
        Z                   = 0,
        Y                   = 25420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 60310,
        Z                   = 0,
        Y                   = -1230,
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
        X                   = -9950,
        Z                   = 0,
        Y                   = 71270,
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


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_2BD",          # 01, 1
        "Function_2_322",          # 02, 2
        "Function_3_49F",          # 03, 3
        "Function_4_4C8",          # 04, 4
        "Function_5_A79",          # 05, 5
        "Function_6_B6E",          # 06, 6
        "Function_7_C52",          # 07, 7
        "Function_8_D25",          # 08, 8
        "Function_9_E72",          # 09, 9
        "Function_10_F86",         # 0A, 10
        "Function_11_10FD",        # 0B, 11
        "Function_12_1275",        # 0C, 12
        "Function_13_1374",        # 0D, 13
        "Function_14_14E3",        # 0E, 14
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2AD")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x10, -14520, 0, -5650, 262)

    label("loc_2AD")

    Jump("loc_2BC")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2BC")
    SetChrFlags(0x10, 0x10)

    label("loc_2BC")

    Return()

    # Function_0_27A end

    def Function_1_2BD(): pass

    label("Function_1_2BD")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F4")
    OP_B1("t4400_y")
    Jump("loc_2FD")

    label("loc_2F4")

    OP_B1("t4400_n")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_317")
    OP_72(0xC, 0x4)

    label("loc_317")

    OP_71(0xB, 0x4)
    OP_1C(0x3, 0x0, 0xE)
    Return()

    # Function_1_2BD end

    def Function_2_322(): pass

    label("Function_2_322")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_489")

    label("loc_347")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_489")

    label("loc_360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_489")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_489")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_489")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_489")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_489")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_489")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_489")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_489")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_489")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_489")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_489")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_489")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_489")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_489")

    label("loc_49E")

    Return()

    # Function_2_322 end

    def Function_3_49F(): pass

    label("Function_3_49F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C7")
    OP_8D(0xFE, -8750, -2900, -6330, -5850, 1500)
    Sleep(2000)
    Jump("Function_3_49F")

    label("loc_4C7")

    Return()

    # Function_3_49F end

    def Function_4_4C8(): pass

    label("Function_4_4C8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_588")

    ChrTalk(    #0
        0xFE,
        (
            "搬，搬运车无法开动\x01",
            "就得用手搬运行李了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "但、但是要搬运的行李\x01",
            "都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "工作能偷懒真幸运，\x01",
            "现在可不是说这种话的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我，我的工资\x01",
            "和三餐怎么办啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588")

    Jump("loc_A75")

    label("loc_58B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_69B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5CB")

    ChrTalk(    #4
        0xFE,
        (
            "呼，当天不是夜班\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_698")

    label("loc_5CB")


    ChrTalk(    #5
        0xFE,
        (
            "事务所被袭击\x01",
            "丹克和菲利奥\x01",
            "似乎都很惨的样子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "他、他们又没做坏事\x01",
            "不觉得很可怜吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "我、我当天\x01",
            "不在事务所真是太好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "虽、虽然也有过\x01",
            "一点点这种念头，\x01",
            "但那实在太过分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "没错吧？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_698")

    Jump("loc_A75")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_705")

    ChrTalk(    #10
        0xFE,
        (
            "我，我在这里工作\x01",
            "只是吃点粗茶淡饭的\x01",
            "无力的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "但、但是勉强\x01",
            "也算幸福的生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E3")

    label("loc_705")


    ChrTalk(    #12
        0xFE,
        (
            "在找穿白裙子的女孩……？\x01",
            "难、难道是什么事件吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "我，我在这里工作\x01",
            "只是吃点粗茶淡饭的\x01",
            "无力的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "但、但是勉强\x01",
            "也算幸福的生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "这个，偶然\x01",
            "也会想和\x01",
            "女孩子约会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "但、但那种事\x01",
            "怎么可能说出口嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7E3")

    Jump("loc_A75")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(    #17
        0xFE,
        "反而……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "变得很、很成熟的样子\x01",
            "真让人憧憬啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2")

    label("loc_832")


    ChrTalk(    #19
        0xFE,
        (
            "今、今天我\x01",
            "也要努力工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "这、这种日子\x01",
            "反而更让人想\x01",
            "努力工作啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "但、但是我\x01",
            "也没喝过酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "抱，抱歉……\x01",
            "只是想说说看而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8C2")

    Jump("loc_A75")

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_952")

    ChrTalk(    #23
        0xFE,
        (
            "你、你可别说出去，我本来\x01",
            "想在飞船公社工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "但、但是，不觉得很过分吗？\x01",
            "那里竞争太激烈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "我，我实在\x01",
            "太没胆了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A75")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9AD")

    ChrTalk(    #26
        0xFE,
        (
            "本、本来想摆摆\x01",
            "前辈的架子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "但对人生的前辈\x01",
            "怎么可能那样做呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A75")

    label("loc_9AD")


    ChrTalk(    #28
        0xFE,
        (
            "我、我在这里工作\x01",
            "已经快两年了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "最近有了后辈\x01",
            "稍、稍微有点迷惑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "因、因为……又比我年纪大，\x01",
            "还结了婚的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "本、本来想摆摆\x01",
            "前辈的架子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "但对人生的前辈\x01",
            "怎么可能那样做呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A75")

    TalkEnd(0x8)
    Return()

    # Function_4_4C8 end

    def Function_5_A79(): pass

    label("Function_5_A79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B")
    Jump("loc_B6A")

    label("loc_A8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_AA1")
    Jump("loc_B6A")

    label("loc_AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_ADC")

    ChrTalk(    #33
        0xFE,
        (
            "啊哈哈……\x01",
            "和这些孩子们在一起就不会无聊了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6A")

    label("loc_ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B00")

    ChrTalk(    #34
        0xFE,
        "好了，该回去了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B6A")

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_B49")

    ChrTalk(    #35
        0xFE,
        (
            "只是带到港口来\x01",
            "竟然都这么高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "这么轻松真是得救了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B6A")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_B6A")

    ChrTalk(    #37
        0xFE,
        "啊～真是漂亮的湖啊。\x02",
    )

    CloseMessageWindow()

    label("loc_B6A")

    TalkEnd(0xFE)
    Return()

    # Function_5_A79 end

    def Function_6_B6E(): pass

    label("Function_6_B6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B80")
    Jump("loc_C4E")

    label("loc_B80")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_B96")
    Jump("loc_C4E")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_BC3")

    ChrTalk(    #38
        0xFE,
        (
            "都说啦～！\x01",
            "这里不是海是湖！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4E")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BEE")

    ChrTalk(    #39
        0xFE,
        (
            "咦～我\x01",
            "觉得还是肉好啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4E")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_C31")

    ChrTalk(    #40
        0xFE,
        (
            "与其看鱼\x01",
            "我更想看海鸥啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "啊，但是这里是湖吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4E")

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_C4E")

    ChrTalk(    #42
        0xFE,
        "我喜欢这个地方。\x02",
    )

    CloseMessageWindow()

    label("loc_C4E")

    TalkEnd(0xFE)
    Return()

    # Function_6_B6E end

    def Function_7_C52(): pass

    label("Function_7_C52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C64")
    Jump("loc_D21")

    label("loc_C64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C7A")
    Jump("loc_D21")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_CAD")

    ChrTalk(    #43
        0xFE,
        (
            "大～海～啊，好～宽阔，\x01",
            "好～大～啊⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D21")

    label("loc_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDE")

    ChrTalk(    #44
        0xFE,
        (
            "今天晚饭吃什么呢。\x01",
            "我想吃鱼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D21")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_D00")

    ChrTalk(    #45
        0xFE,
        "对了对了，有鱼吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D21")

    label("loc_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_D21")

    ChrTalk(    #46
        0xFE,
        "我是第一次来港口哦。\x02",
    )

    CloseMessageWindow()

    label("loc_D21")

    TalkEnd(0xFE)
    Return()

    # Function_7_C52 end

    def Function_8_D25(): pass

    label("Function_8_D25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(    #47
        0xFE,
        (
            "到底什么时候\x01",
            "船才能动呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6E")

    label("loc_D58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_D6E")
    Jump("loc_E6E")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_DBF")

    ChrTalk(    #48
        0xFE,
        "这是卢安市长已经确定的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "这样港口的营业\x01",
            "也马上就恢复正常了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6E")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFC")

    ChrTalk(    #50
        0xFE,
        (
            "好了，工作已经结束了。\x01",
            "请大家去喝一杯吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6E")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E28")

    ChrTalk(    #51
        0xFE,
        (
            "嗯，不要急,\x01",
            "先做能做的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6E")

    label("loc_E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E6E")

    ChrTalk(    #52
        0xFE,
        (
            "差不多该是把仓库\x01",
            "整理整齐的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "以后还会很忙哦。\x02",
    )

    CloseMessageWindow()

    label("loc_E6E")

    TalkEnd(0xFE)
    Return()

    # Function_8_D25 end

    def Function_9_E72(): pass

    label("Function_9_E72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA4")

    ChrTalk(    #54
        0xFE,
        "呼，身体变迟钝真是没办法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_EA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_EBA")
    Jump("loc_F82")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_EEF")

    ChrTalk(    #55
        0xFE,
        (
            "市长选举，真希望\x01",
            "波尔多斯氏能获胜……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #56
        0xFE,
        (
            "最近大概是太忙了\x01",
            "总觉得时间过得好快……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_F54")

    ChrTalk(    #57
        0xFE,
        "呼，从哪个仓库开始整理呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_F82")

    ChrTalk(    #58
        0xFE,
        (
            "闲着当然不好\x01",
            "太忙也是个问题啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F82")

    TalkEnd(0xFE)
    Return()

    # Function_9_E72 end

    def Function_10_F86(): pass

    label("Function_10_F86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE2")

    ChrTalk(    #59
        0xFE,
        (
            "不能工作，\x01",
            "只能钓钓鱼等着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "你怎样？\x01",
            "垂下钓线就会冷静下来啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F9")

    label("loc_FE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_FF8")
    Jump("loc_10F9")

    label("loc_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1058")

    ChrTalk(    #61
        0xFE,
        (
            "刚才，给了我鱼竿的人\x01",
            "来过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "虽然不太清楚\x01",
            "但好像是叫钓公师团的团体的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F9")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1087")

    ChrTalk(    #63
        0xFE,
        (
            "现在这时候\x01",
            "正是钓鱼的时候！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F9")

    label("loc_1087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(    #64
        0xFE,
        (
            "工作的间歇\x01",
            "能钓鱼也不坏。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F9")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_10F9")

    ChrTalk(    #65
        0xFE,
        (
            "不认识的人\x01",
            "硬把钓竿塞给了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "机会难得，\x01",
            "想试着钓钓看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F9")

    TalkEnd(0xFE)
    Return()

    # Function_10_F86 end

    def Function_11_10FD(): pass

    label("Function_11_10FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114A")

    ChrTalk(    #67
        0xFE,
        (
            "……真是的，导力器不能使用\x01",
            "我们搞技术的就没法工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1271")

    label("loc_114A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1160")
    Jump("loc_1271")

    label("loc_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_11B4")

    ChrTalk(    #68
        0xFE,
        (
            "技术不外传\x01",
            "是我的信念……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "但如果对方是女孩子\x01",
            "忍不住就会教了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1271")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FB")

    ChrTalk(    #70
        0xFE,
        "嘿嘿，是，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "哈，不行不行\x01",
            "要严厉要严厉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1271")

    label("loc_11FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1247")

    ChrTalk(    #72
        0xFE,
        (
            "呵呵，人被称赞\x01",
            "心情就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "但是，对后辈\x01",
            "还是要严厉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1271")

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1271")

    ChrTalk(    #74
        0xFE,
        (
            "技术是自然\x01",
            "就能学到的东西……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1271")

    TalkEnd(0xFE)
    Return()

    # Function_11_10FD end

    def Function_12_1275(): pass

    label("Function_12_1275")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(    #75
        0xFE,
        (
            "哎～怎么\x01",
            "不动啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "好孩子，快动啦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1370")

    label("loc_12B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12CA")
    Jump("loc_1370")

    label("loc_12CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_12F7")

    ChrTalk(    #77
        0xFE,
        (
            "前辈，那里的回路\x01",
            "该怎么办啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1370")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(    #78
        0xFE,
        (
            "好厉害啊～\x01",
            "好崇拜你～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1370")

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1344")

    ChrTalk(    #79
        0xFE,
        "哇～好出色的手法～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1370")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(    #80
        0xFE,
        (
            "哇～前辈的技术\x01",
            "我真是望尘莫及。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1370")

    TalkEnd(0xFE)
    Return()

    # Function_12_1275 end

    def Function_13_1374(): pass

    label("Function_13_1374")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CA")

    ChrTalk(    #81
        0xFE,
        (
            "每天都来单位\x01",
            "却一直不能工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "今后，\x01",
            "到底会变成怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF")

    label("loc_13CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_13E0")
    Jump("loc_14DF")

    label("loc_13E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1423")

    ChrTalk(    #83
        0xFE,
        "呼哇～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "……啊糟糕。\x01",
            "疏忽大意是受伤的根源。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF")

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1454")

    ChrTalk(    #85
        0xFE,
        (
            "呜～肚子好饿～\x01",
            "今天吃什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_14B6")

    ChrTalk(    #86
        0xFE,
        (
            "好，这个结束了\x01",
            "就去休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "对我们来说身体就是本钱嘛。\x01",
            "休息也是很好的工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF")

    label("loc_14B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_14DF")

    ChrTalk(    #88
        0xFE,
        "这里是仓库街的管理事务所哦。\x02",
    )

    CloseMessageWindow()

    label("loc_14DF")

    TalkEnd(0xFE)
    Return()

    # Function_13_1374 end

    def Function_14_14E3(): pass

    label("Function_14_14E3")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_14_14E3 end

    SaveToFile()

Try(main)
