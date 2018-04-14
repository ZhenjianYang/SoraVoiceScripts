from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5406   ._SN',
        MapName             = 'Other',
        Location            = 'C5406.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '小丑肯帕雷拉',                         # 9
        '亡命装甲兵',                           # 10
        '强化猎兵',                             # 11
        '强化猎兵',                             # 12
        '强化猎兵',                             # 13
        '强化猎兵',                             # 14
        '强化猎兵',                             # 15
        '强化猎兵',                             # 16
        '强化猎兵',                             # 17
        '强化猎兵',                             # 18
        '强化猎兵',                             # 19
        '强化猎兵',                             # 20
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
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT27/CH04010 ._CH',             # 01
        'ED6_DT29/CH12390 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT29/CH12390 ._CH',             # 04
        'ED6_DT27/CH04620 ._CH',             # 05
        'ED6_DT27/CH04621 ._CH',             # 06
        'ED6_DT27/CH04622 ._CH',             # 07
        'ED6_DT26/CH20298 ._CH',             # 08
        'ED6_DT27/CH04000 ._CH',             # 09
        'ED6_DT27/CH04011 ._CH',             # 0A
        'ED6_DT27/CH04001 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT27/CH04010P._CP',             # 01
        'ED6_DT29/CH12390P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT29/CH12390P._CP',             # 04
        'ED6_DT27/CH04620P._CP',             # 05
        'ED6_DT27/CH04621P._CP',             # 06
        'ED6_DT27/CH04622P._CP',             # 07
        'ED6_DT26/CH20298P._CP',             # 08
        'ED6_DT27/CH04000P._CP',             # 09
        'ED6_DT27/CH04011P._CP',             # 0A
        'ED6_DT27/CH04001P._CP',             # 0B
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 1130,
        Y                   = 3000,
        Z                   = -178880,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = -2550,
        Y                   = -2000,
        Z                   = 7130,
        Range               = 4630,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x1252,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_2CA",          # 00, 0
        "Function_1_2FC",          # 01, 1
        "Function_2_378",          # 02, 2
        "Function_3_4F5",          # 03, 3
        "Function_4_510",          # 04, 4
        "Function_5_124E",         # 05, 5
        "Function_6_132A",         # 06, 6
        "Function_7_19F0",         # 07, 7
        "Function_8_1A38",         # 08, 8
        "Function_9_1BD0",         # 09, 9
        "Function_10_1C41",        # 0A, 10
        "Function_11_1C7E",        # 0B, 11
        "Function_12_1FFD",        # 0C, 12
        "Function_13_2017",        # 0D, 13
        "Function_14_22F8",        # 0E, 14
        "Function_15_233F",        # 0F, 15
        "Function_16_238B",        # 10, 16
        "Function_17_23D2",        # 11, 17
        "Function_18_2402",        # 12, 18
        "Function_19_2432",        # 13, 19
        "Function_20_2474",        # 14, 20
        "Function_21_24BB",        # 15, 21
        "Function_22_24EB",        # 16, 22
        "Function_23_251B",        # 17, 23
        "Function_24_254B",        # 18, 24
        "Function_25_2591",        # 19, 25
        "Function_26_25DC",        # 1A, 26
        "Function_27_2627",        # 1B, 27
        "Function_28_2672",        # 1C, 28
        "Function_29_26A9",        # 1D, 29
        "Function_30_26DB",        # 1E, 30
        "Function_31_2712",        # 1F, 31
        "Function_32_2749",        # 20, 32
        "Function_33_2780",        # 21, 33
        "Function_34_27B7",        # 22, 34
        "Function_35_2959",        # 23, 35
    )


    def Function_0_2CA(): pass

    label("Function_0_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)
    Jump("loc_2FB")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2FB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 34)

    label("loc_2FB")

    Return()

    # Function_0_2CA end

    def Function_1_2FC(): pass

    label("Function_1_2FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_354")
    OP_72(0x0, 0x8)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_72(0x1, 0x8)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x4)
    Jump("loc_377")

    label("loc_354")

    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_71(0x8, 0x4)

    label("loc_377")

    Return()

    # Function_1_2FC end

    def Function_2_378(): pass

    label("Function_2_378")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4DF")

    label("loc_39D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4DF")

    label("loc_3B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4DF")

    label("loc_3CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4DF")

    label("loc_3E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4DF")

    label("loc_401")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4DF")

    label("loc_41A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_433")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4DF")

    label("loc_433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4DF")

    label("loc_44C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4DF")

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4DF")

    label("loc_47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4DF")

    label("loc_497")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4DF")

    label("loc_4B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4DF")

    label("loc_4C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4DF")

    label("loc_4F4")

    Return()

    # Function_2_378 end

    def Function_3_4F5(): pass

    label("Function_3_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_507")
    Return()

    label("loc_507")

    Call(0, 4)
    Call(0, 6)
    Return()

    # Function_3_4F5 end

    def Function_4_510(): pass

    label("Function_4_510")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(1070, -1000, 4640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 1240, -1000, 20540, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 1880, -1000, 4290, 0)
    SetChrPos(0x102, 370, -1000, 4390, 0)
    OP_0D()

    NpcTalk(    #0
        0x8,
        "少年的声音",
        (
            "#4P嘻嘻……\x01",
            "动作好慢啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5F4():
        OP_6D(1780, -1000, 9150, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F4)

    def lambda_60C():
        OP_67(0, 6240, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60C)

    def lambda_624():
        OP_6B(2800, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_624)

    def lambda_634():
        OP_6E(323, 3500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_634)
    OP_8E(0x8, 0x500, 0xFFFFFC18, 0x2EE0, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #1
        0x101,
        "#1020F#4P你、你是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1032F#6P……肯帕雷拉吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#854F#5P真是无情啊，约修亚。\x02\x03",

            "只顾着和莱维叙旧，\x01",
            "却连个招呼都不和我打？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1035F#6P没想到你会\x01",
            "留在飞船上……\x02\x03",

            "#1030F看穿我的行动了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#851F#5P啊哈哈，别小看人啊，\x01",
            "至少我也担任着监视『计划』的任务呢。\x02\x03",

            "和其他人相比，\x01",
            "关注的事情自然多了些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#1032F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#850F#5P呵呵，话说回来……\x02\x03",

            "五年不见，\x01",
            "你倒是变了不少呢。\x02\x03",

            "似乎变得更有男人味了嘛～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1031F#6P倒是你……\x01",
            "完全都没有变化啊。\x02\x03",

            "外表还是和以前一模一样，\x01",
            "好像完全都没有长大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#851F#5P哼哼哼～那是因为\x01",
            "我每天都很注意皮肤的保养哦。\x02\x03",

            "#854F你好像也经常穿女装，\x01",
            "要不要我介绍点好的化妆品？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1030F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1022F#4P啊～真是的！急死人了。\x02\x03",

            "#1005F你既然埋伏在这里，\x01",
            "就是想跟我们打一架对吧！？\x02\x03",

            "那还等什么！赶快放马过来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#851F啊哈哈，好有气势的女孩子呀～\x02\x03",

            "#850F早就听说你是约修亚的女朋友，\x01",
            "我还一直在猜想会是怎样的女孩……\x02\x03",

            "看来还挺般配的嘛？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1013F#4P女、女朋友……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#854F哟，难道说女朋友不是你，\x01",
            "而是那个空贼女孩吗？\x02\x03",

            "#851F你好受欢迎呀，约修亚㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1019F#4P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1035F#6P……玩笑\x01",
            "就到此为止吧。\x02\x03",

            "虽然我很好奇你为何\x01",
            "连乔丝特的事都知道……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 1)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x102,
        (
            "#1030F#6P你的战斗力\x01",
            "应该和我不相上下。\x02\x03",

            "即使这样，也一定要分个高下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#851F#5P啊哈哈，没那个意思啦。\x02\x03",

            "#850F刚才也说了，\x01",
            "我只是负责观察『计划』而已。\x02\x03",

            "并没有捕捉你们\x01",
            "的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1032F#6P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1015F#4P哼～是这样吗。\x02\x03",

            "那你为什么还要\x01",
            "埋伏在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#853F#5P哼哼～那当然\x01",
            "是为了问候你们二位一下了。\x02\x03",

            "#854F不过，就这样直接说再见\x01",
            "未免也太缺乏艺术性了。\x02\x03",

            "我只是想给你们的逃亡演出\x01",
            "增加一点高潮情节而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_CCA():
        OP_6D(1800, -1000, 11000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CCA)

    def lambda_CE2():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE2)
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x1, 0x2, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    OP_1F(0x5A, 0x3E8)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_1F(0x64, 0x3E8)

    def lambda_DAD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DAD)
    Sleep(50)

    def lambda_DC0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC0)
    LoadEffect(0x1, "map\\\\mp003_00.eff")
    OP_6D(1160, -1000, 2460, 1500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1390, -1000, -1260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1050, -1000, 420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E6C():
        OP_96(0xFE, 0xFFFFFDE4, 0xFFFFFC18, 0x141E, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E6C)
    Sleep(100)

    def lambda_E8F():
        OP_96(0xFE, 0xBA4, 0xFFFFFC18, 0x1310, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E8F)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1420, -1000, 2270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1100, -1000, 3760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1600, -1000, 5220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 1050, -1000, 6410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)

    def lambda_FD5():
        OP_6D(6550, 890, 5910, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD5)

    def lambda_FED():
        OP_67(0, 3790, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FED)

    def lambda_1005():
        OP_6B(4030, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1005)

    def lambda_1015():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1015)

    def lambda_1025():
        OP_6E(271, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1025)
    SetChrPos(0x9, 7200, 3370, -17760, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_104B():

        label("loc_104B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_104B")

    QueueWorkItem2(0x9, 3, lambda_104B)

    def lambda_105E():

        label("loc_105E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_105E")

    QueueWorkItem2(0x101, 0, lambda_105E)

    def lambda_106F():

        label("loc_106F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_106F")

    QueueWorkItem2(0x102, 0, lambda_106F)
    OP_43(0x9, 0x0, 0x0, 0x5)
    Sleep(3000)

    def lambda_108C():
        OP_8C(0xFE, 270, 100)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_108C)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x102, 10)
    OP_44(0x102, 0x0)
    OP_8E(0x102, 0x988, 0xFFFFFC18, 0x19A0, 0xFA0, 0x0)
    OP_8C(0x102, 90, 400)
    SetChrChipByIndex(0x102, 1)
    WaitChrThread(0x9, 0x0)
    OP_44(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x101,
        "#1020F#4P什、什、什！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1034F#6P高机动飞行人形兵器——\x01",
            "『亡命装甲兵』！\x02\x03",

            "已经开始量产了吗！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(7630, -1000, 9550, 0)
    OP_67(0, 3790, -10000, 0)
    OP_6B(4630, 0)
    OP_6C(42000, 0)
    OP_6E(271, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x8,
        (
            "#853F#5P历尽艰辛才重逢的两人，\x01",
            "又被新的障碍阻住了去路。\x02\x03",

            "#854F啊啊～少年和少女的命运将会如何呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_11F9():
        OP_8F(0xFE, 0x198C, 0x12C, 0x161C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11F9)

    def lambda_1214():
        OP_6B(3270, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1214)
    WaitChrThread(0x101, 0x2)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x429, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1248"),
        (SWITCH_DEFAULT, "loc_124D"),
    )


    label("loc_1248")

    OP_B4(0x0)
    Jump("loc_124D")

    label("loc_124D")

    Return()

    # Function_4_510 end

    def Function_5_124E(): pass

    label("Function_5_124E")


    def lambda_1254():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1254)
    Sleep(300)

    def lambda_1274():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1274)
    Sleep(300)

    def lambda_1294():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1294)
    Sleep(300)

    def lambda_12B4():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12B4)
    Sleep(300)

    def lambda_12D4():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12D4)
    Sleep(300)

    def lambda_12F4():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12F4)
    Sleep(300)

    def lambda_1314():
        OP_8F(0xFE, 0x2D14, 0x384, 0x161C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1314)
    Return()

    # Function_5_124E end

    def Function_6_132A(): pass

    label("Function_6_132A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2600D2, 0x2600D7, 0xC)
    OP_44(0x9, 0x2)
    OP_44(0x8, 0x0)
    SetChrPos(0x8, 1280, -1000, 12000, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 11540, 900, 5660, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 2110, -1000, 3460, 90)
    SetChrPos(0x102, 950, -1000, 4990, 90)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 1)
    SetChrSubChip(0x102, 0)
    OP_6D(6550, -400, 6000, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(57000, 0)
    OP_6E(365, 0)
    LoadEffect(0x2, "battle\\btbomb00.eff")
    LoadEffect(0x3, "map\\mp090_00.eff")
    OP_43(0x9, 0x3, 0x0, 0x8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x9, 0x3)
    Sleep(300)

    ChrTalk(    #25
        0x8,
        "#2P啊哈哈，挺有一手嘛。\x02",
    )

    CloseMessageWindow()

    def lambda_144E():
        OP_6D(2270, -1000, 8930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_144E)

    def lambda_1466():
        OP_67(0, 6740, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1466)

    def lambda_147E():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_147E)

    def lambda_148E():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_148E)

    def lambda_149E():
        OP_6E(365, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_149E)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x8,
        (
            "#851F#5P约修亚也就罢了，\x01",
            "没想到这位小姐的实力也很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)

    def lambda_14FC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14FC)
    Sleep(100)
    OP_8C(0x102, 0, 400)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0x87A, 0xFFFFFC18, 0x125C, 0x1388, 0x0)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #27
        0x101,
        (
            "#1005F#4P你、你这个人～……\x01",
            "恶作剧也要有个限度啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#853F#5P别生气～别生气。\x02\x03",

            "#850F好了，演出结束，\x01",
            "小丑该退场了吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x2, "map\\\\mp055_00.eff")
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_15FC():
        OP_6D(1800, -1000, 10200, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15FC)

    def lambda_1614():
        OP_6B(2300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1614)
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x1, 0x2, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x2, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        "#1020F#4P！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #30
        0x8,
        (
            "#854F#5P哈哈哈……\x01",
            "那么两位。\x02\x03",

            "在不久的将来再见吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    SetChrFlags(0x8, 0x80)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x7)
    Sleep(1500)

    def lambda_1726():
        OP_6D(2550, -1000, 7750, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1726)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #31
        0x101,
        "#1020F#2P消、消失了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1035F#6P这是幻术的一种。\x01",
            "不必介意。\x02\x03",

            "#1030F现在必须赶快──\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 990, -1000, -17770, 0)

    NpcTalk(    #33
        0x8,
        "男人的声音",
        (
            "#1S#1P喂！\x01",
            "他们真的跑到这里了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_1824():
        OP_6D(1020, -1000, -10820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1824)

    def lambda_183C():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_183C)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(100)

    def lambda_1859():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1859)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x101, 0x3)

    NpcTalk(    #34
        0x8,
        "男人的声音",
        "#1S#1P啊啊……没错！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x2B)
    Sleep(500)
    Fade(500)
    OP_6D(1210, -1000, 5170, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(3090, 0)
    OP_6C(60000, 0)
    OP_6E(311, 0)
    OP_0D()
    TurnDirection(0x102, 0x101, 600)
    Sleep(400)

    ChrTalk(    #35
        0x102,
        "#1036F#6P艾丝蒂尔，赶快！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 600)
    Sleep(400)

    ChrTalk(    #36
        0x101,
        "#1002F#2P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    def lambda_1938():
        OP_6D(12680, -910, 27340, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1938)

    def lambda_1950():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1950)

    def lambda_1968():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1968)

    def lambda_1978():
        OP_6E(375, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1978)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0xA)
    WaitChrThread(0x102, 0x3)
    Sleep(300)
    OP_8E(0x101, 0x2EFE, 0xFFFFFC72, 0x67CA, 0x1388, 0x0)
    SetChrFlags(0x101, 0x80)
    OP_72(0x0, 0x20)
    OP_22(0xFD, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x77)
    OP_73(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_132A end

    def Function_7_19F0(): pass

    label("Function_7_19F0")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_7_19F0 end

    def Function_8_1A38(): pass

    label("Function_8_1A38")


    def lambda_1A3E():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A3E)

    def lambda_1A58():
        OP_8F(0xFE, 0x2D14, 0xFFFFF060, 0x161C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1A58)
    PlayEffect(0x2, 0xFF, 0x9, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0x9, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0xFF, 0x9, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0x9, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0x9, 500, 200, 100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x9, 0x0)
    PlayEffect(0x3, 0xFF, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    Return()

    # Function_8_1A38 end

    def Function_9_1BD0(): pass

    label("Function_9_1BD0")

    OP_8E(0xFE, 0x258, 0xFFFFFC18, 0x3A70, 0x1770, 0x0)
    OP_8E(0xFE, 0x2EFE, 0xFFFFFC18, 0x3EDA, 0x1770, 0x0)
    OP_8E(0xFE, 0x2E86, 0xFFFFFB82, 0x61DA, 0x1770, 0x0)
    OP_72(0x0, 0x20)
    OP_22(0xFD, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_8E(0xFE, 0x2EFE, 0xFFFFFC72, 0x67CA, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_1BD0 end

    def Function_10_1C41(): pass

    label("Function_10_1C41")

    OP_8E(0xFE, 0x726, 0xFFFFFC18, 0x3A02, 0x1770, 0x0)
    OP_8E(0xFE, 0x2EFE, 0xFFFFFC18, 0x3EDA, 0x1770, 0x0)
    OP_8E(0xFE, 0x2E5E, 0xFFFFFB82, 0x5CD0, 0x1770, 0x0)
    Return()

    # Function_10_1C41 end

    def Function_11_1C7E(): pass

    label("Function_11_1C7E")

    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(12550, -1000, 29240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x4, 0x4)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 140)
    OP_70(0x0, 0x2EE)
    OP_43(0x8, 0x1, 0x0, 0xC)
    FadeToBright(1000, 0)
    OP_0D()
    LoadEffect(0x1, "map\\\\mp003_00.eff")
    LoadEffect(0x4, "monster\\\\msc0555.eff")
    SetChrPos(0xA, 2200, -1000, 5060, 0)
    SetChrPos(0xB, 2200, -1000, 5060, 0)
    SetChrPos(0xC, 2200, -1000, 5060, 0)
    SetChrPos(0xD, 2200, -1000, 5060, 0)
    SetChrPos(0xE, 2200, -1000, 5060, 0)
    SetChrPos(0xF, 310, -1000, 4040, 0)
    SetChrPos(0x10, 310, -1000, 4040, 0)
    SetChrPos(0x11, 310, -1000, 4040, 0)
    SetChrPos(0x12, 310, -1000, 4040, 0)
    SetChrPos(0x13, 310, -1000, 4040, 0)

    def lambda_1DD0():
        OP_6D(9470, -1150, 23720, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DD0)

    def lambda_1DE8():
        OP_67(0, 4190, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DE8)

    def lambda_1E00():
        OP_6E(360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1E00)
    Sleep(1500)
    OP_43(0xA, 0x1, 0x0, 0xE)
    OP_43(0xF, 0x1, 0x0, 0x13)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xF)
    OP_43(0x10, 0x1, 0x0, 0x14)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x10)
    OP_43(0x11, 0x1, 0x0, 0x15)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x11)
    OP_43(0x12, 0x1, 0x0, 0x16)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x12)
    OP_43(0x13, 0x1, 0x0, 0x17)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)

    ChrTalk(    #37
        0xF,
        "#5P可、可恶……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "#5P发射！\x01",
            "绝对不能让他们逃走！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EB9():
        OP_6D(9390, -1000, 24480, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EB9)

    def lambda_1ED1():
        OP_67(0, 6620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ED1)

    def lambda_1EE9():
        OP_6E(338, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1EE9)
    OP_43(0xA, 0x1, 0x0, 0x18)
    OP_43(0xF, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0xB, 0x1, 0x0, 0x19)
    OP_43(0x10, 0x1, 0x0, 0x1E)
    Sleep(100)
    OP_43(0xC, 0x1, 0x0, 0x1A)
    OP_43(0x11, 0x1, 0x0, 0x1F)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x1B)
    OP_43(0x12, 0x1, 0x0, 0x20)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    OP_43(0x13, 0x1, 0x0, 0x21)
    WaitChrThread(0x101, 0x3)
    Sleep(2000)
    OP_73(0x0)
    OP_6F(0x0, 750)
    OP_70(0x0, 0x348)
    OP_22(0x136, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    OP_6F(0x0, 840)
    OP_70(0x0, 0x3D4)
    OP_22(0x136, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_44(0xA, 0x1)
    Sleep(100)
    OP_44(0xB, 0x1)
    Sleep(100)
    OP_44(0xC, 0x1)
    Sleep(100)
    OP_44(0xD, 0x1)
    Sleep(100)
    OP_44(0xE, 0x1)
    Sleep(100)
    OP_44(0xF, 0x1)
    Sleep(100)
    OP_44(0x10, 0x1)
    Sleep(100)
    OP_44(0x11, 0x1)
    Sleep(100)
    OP_44(0x12, 0x1)
    Sleep(100)
    OP_44(0x13, 0x1)
    OP_73(0x0)
    OP_0D()
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1C7E end

    def Function_12_1FFD(): pass

    label("Function_12_1FFD")

    Sleep(500)
    OP_22(0x133, 0x0, 0x64)
    Sleep(4500)
    OP_22(0x133, 0x0, 0x64)
    Sleep(5000)
    Return()

    # Function_12_1FFD end

    def Function_13_2017(): pass

    label("Function_13_2017")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)

    label("loc_2021")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F7")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C3")
    Sleep(400)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 9790, -1300, 27370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_22F4")

    label("loc_20C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2150")
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 9870, -1200, 29300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_22F4")

    label("loc_2150")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DD")
    Sleep(600)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 9840, 2500, 27360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_22F4")

    label("loc_21DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226A")
    Sleep(700)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 10850, 2500, 25410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_22F4")

    label("loc_226A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F4")
    Sleep(800)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 10920, -1150, 25380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_22F4")

    Jump("loc_2021")

    label("loc_22F7")

    Return()

    # Function_13_2017 end

    def Function_14_22F8(): pass

    label("Function_14_22F8")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x97E, 0xFFFFFC18, 0x3C6E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_14_22F8 end

    def Function_15_233F(): pass

    label("Function_15_233F")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xBC2, 0xFFFFFC18, 0x3778, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_15_233F end

    def Function_16_238B(): pass

    label("Function_16_238B")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x794, 0xFFFFFC18, 0x3200, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_16_238B end

    def Function_17_23D2(): pass

    label("Function_17_23D2")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x88E, 0xFFFFFC18, 0x2BFC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_17_23D2 end

    def Function_18_2402(): pass

    label("Function_18_2402")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x6D6, 0xFFFFFC18, 0x251C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_2402 end

    def Function_19_2432(): pass

    label("Function_19_2432")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x2E4, 0xFFFFFC18, 0x3B06, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_19_2432 end

    def Function_20_2474(): pass

    label("Function_20_2474")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x136, 0xFFFFFC18, 0x34A8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_20_2474 end

    def Function_21_24BB(): pass

    label("Function_21_24BB")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFFFFDE4, 0xFFFFFC18, 0x2E22, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_21_24BB end

    def Function_22_24EB(): pass

    label("Function_22_24EB")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFA, 0xFFFFFC18, 0x2A08, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_24EB end

    def Function_23_251B(): pass

    label("Function_23_251B")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFFFFF56, 0xFFFFFC18, 0x2440, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_251B end

    def Function_24_254B(): pass

    label("Function_24_254B")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x2378, 0xFFFFFC18, 0x3F48, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    OP_43(0xA, 0x1, 0x0, 0xD)
    Return()

    # Function_24_254B end

    def Function_25_2591(): pass

    label("Function_25_2591")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x1EE6, 0xFFFFFC18, 0x4132, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Return()

    # Function_25_2591 end

    def Function_26_25DC(): pass

    label("Function_26_25DC")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x19A0, 0xFFFFFC18, 0x4236, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 0, 400)
    OP_43(0xC, 0x1, 0x0, 0xD)
    Return()

    # Function_26_25DC end

    def Function_27_2627(): pass

    label("Function_27_2627")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFA, 0xFFFFFC18, 0x3ECF, 0x1388, 0x0)
    OP_8E(0xFE, 0x1284, 0xFFFFFC18, 0x3FB5, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0xD, 0x1, 0x0, 0xD)
    Return()

    # Function_27_2627 end

    def Function_28_2672(): pass

    label("Function_28_2672")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xE4C, 0xFFFFFC18, 0x41F0, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0xE, 0x1, 0x0, 0xD)
    Return()

    # Function_28_2672 end

    def Function_29_26A9(): pass

    label("Function_29_26A9")

    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x8CA, 0xFFFFFC18, 0x54D8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0xF, 0x1, 0x0, 0xD)
    Return()

    # Function_29_26A9 end

    def Function_30_26DB(): pass

    label("Function_30_26DB")

    Sleep(50)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x74E, 0xFFFFFC18, 0x4F9C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x10, 0x1, 0x0, 0xD)
    Return()

    # Function_30_26DB end

    def Function_31_2712(): pass

    label("Function_31_2712")

    Sleep(70)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xB18, 0xFFFFFC18, 0x4E02, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x11, 0x1, 0x0, 0xD)
    Return()

    # Function_31_2712 end

    def Function_32_2749(): pass

    label("Function_32_2749")

    Sleep(100)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x726, 0xFFFFFC18, 0x46B4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x12, 0x1, 0x0, 0xD)
    Return()

    # Function_32_2749 end

    def Function_33_2780(): pass

    label("Function_33_2780")

    Sleep(120)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xB68, 0xFFFFFC18, 0x4614, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 45, 400)
    OP_43(0x13, 0x1, 0x0, 0xD)
    Return()

    # Function_33_2780 end

    def Function_34_27B7(): pass

    label("Function_34_27B7")

    EventBegin(0x0)
    OP_72(0x0, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 980)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xA, 9080, -1000, 16200, 0)
    SetChrPos(0xB, 7910, -1000, 16690, 0)
    SetChrPos(0xC, 6560, -1000, 16950, 0)
    SetChrPos(0xD, 4740, -1000, 16309, 45)
    SetChrPos(0xE, 3660, -1000, 16880, 45)
    SetChrPos(0xF, 2250, -1000, 21720, 45)
    SetChrPos(0x10, 1870, -1000, 20380, 45)
    SetChrPos(0x11, 2840, -1000, 19970, 45)
    SetChrPos(0x12, 1830, -1000, 18100, 45)
    SetChrPos(0x13, 2920, -1000, 17940, 45)
    OP_6D(6900, -1000, 20600, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(45000, 0)
    OP_6E(248, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #39
        0xF,
        (
            "#5P唔……\x01",
            "别想就这么逃跑！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        "#5P我们也乘飞艇出动！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_27B7 end

    def Function_35_2959(): pass

    label("Function_35_2959")

    Return()

    # Function_35_2959 end

    SaveToFile()

Try(main)
