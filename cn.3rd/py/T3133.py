from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3133   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '提妲',                                 # 9
        '阿加特',                               # 10
        '拉赛尔博士',                           # 11
        '艾莉卡',                               # 12
        '丹',                                   # 13
        '玛多克工房长',                         # 14
        '物体对象',                             # 15
        '咖啡',                                 # 16
        '咖啡',                                 # 17
        '咖啡',                                 # 18
        '咖啡',                                 # 19
        '水壶',                                 # 20
        '导力装甲',                             # 21
        '晚饭',                                 # 22
        '晚饭',                                 # 23
        '晚饭',                                 # 24
        '餐具',                                 # 25
        '餐具',                                 # 26
        '餐具',                                 # 27
        '餐具',                                 # 28
        '目标用照相机',                         # 29
        '',                                     # 30
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00060 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH02020 ._CH',             # 02
        'ED6_DT07/CH00061 ._CH',             # 03
        'ED6_DT07/CH00063 ._CH',             # 04
        'ED6_DT07/CH02023 ._CH',             # 05
        'ED6_DT27/CH03970 ._CH',             # 06
        'ED6_DT27/CH03980 ._CH',             # 07
        'ED6_DT26/CH20696 ._CH',             # 08
        'ED6_DT26/CH20697 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT07/CH02620 ._CH',             # 0C
        'ED6_DT27/CH04220 ._CH',             # 0D
        'ED6_DT26/CH20205 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH02020P._CP',             # 02
        'ED6_DT07/CH00061P._CP',             # 03
        'ED6_DT07/CH00063P._CP',             # 04
        'ED6_DT07/CH02023P._CP',             # 05
        'ED6_DT27/CH03970P._CP',             # 06
        'ED6_DT27/CH03980P._CP',             # 07
        'ED6_DT26/CH20696P._CP',             # 08
        'ED6_DT26/CH20697P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT07/CH02620P._CP',             # 0C
        'ED6_DT27/CH04220P._CP',             # 0D
        'ED6_DT26/CH20205P._CP',             # 0E
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 1179658,
        ChipIndex           = 0xA,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1703947,
        ChipIndex           = 0xB,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 393227,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 131083,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 458763,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_3C2",          # 00, 0
        "Function_1_420",          # 01, 1
        "Function_2_421",          # 02, 2
        "Function_3_16B6",         # 03, 3
        "Function_4_1749",         # 04, 4
        "Function_5_17BC",         # 05, 5
        "Function_6_18EC",         # 06, 6
        "Function_7_1974",         # 07, 7
        "Function_8_1A3B",         # 08, 8
        "Function_9_1DCC",         # 09, 9
        "Function_10_1E35",        # 0A, 10
        "Function_11_24B9",        # 0B, 11
        "Function_12_2566",        # 0C, 12
        "Function_13_2765",        # 0D, 13
        "Function_14_278F",        # 0E, 14
    )


    def Function_0_3C2(): pass

    label("Function_0_3C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3E4")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_3F7")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3F7")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_3F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_41F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_41F")

    Return()

    # Function_0_3C2 end

    def Function_1_420(): pass

    label("Function_1_420")

    Return()

    # Function_1_420 end

    def Function_2_421(): pass

    label("Function_2_421")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-580, 0, 1360, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x107, -2460, -500, -5500, 0)
    SetChrPos(0x12, -2460, -500, -5500, 0)
    SetChrPos(0x13, -1560, -500, -5500, 0)
    SetChrPos(0x14, -1560, -500, -5500, 0)
    OP_9F(0x107, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)

    def lambda_4FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4FE)

    def lambda_510():
        OP_8E(0xFE, 0xFFFFF9E8, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_510)
    Sleep(500)

    def lambda_530():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_530)

    def lambda_542():
        OP_8E(0xFE, 0xFFFFF664, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_542)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #0
        0x13,
        (
            "#1451F#11P呼，\x01",
            "果然还是自己家好啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x3, 0x0, 0x3)
    Sleep(300)
    OP_43(0x12, 0x3, 0x0, 0x4)
    Sleep(100)
    Sleep(500)

    def lambda_5AF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5AF)

    def lambda_5C1():
        OP_8E(0xFE, 0xFFFFF9E8, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5C1)
    Sleep(500)

    def lambda_5E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5E1)

    def lambda_5F3():
        OP_8E(0xFE, 0xFFFFF664, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5F3)
    WaitChrThread(0x107, 0x1)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x13, 0x3)

    ChrTalk(    #1
        0x13,
        (
            "#1450F#5P丹，麻烦你泡杯咖啡。\x01",
            "多放点牛奶哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x14,
        (
            "#1460F#11P是是。\x01",
            "砂糖要三块对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#560F#6P啊，我也来帮忙吧。\x02",
    )

    CloseMessageWindow()

    def lambda_6AB():
        OP_6D(420, 0, 2360, 5500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6AB)
    OP_43(0x14, 0x3, 0x0, 0x5)
    Sleep(300)
    OP_43(0x107, 0x3, 0x0, 0x6)
    WaitChrThread(0x24, 0x3)
    WaitChrThread(0x107, 0x3)
    Sleep(300)

    ChrTalk(    #4
        0x12,
        (
            "#104F#6P这种喝法还真是不正宗啊。\x02\x03",

            "只有黑咖啡才叫咖啡啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x13,
        (
            "#1457F#11P哼，\x01",
            "头脑顽固的老人就是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        (
            "#100F#6P不正宗就是不正宗，\x01",
            "有什么不对？\x02\x03",

            "#100F而且，\x01",
            "还要放三块砂糖。\x02\x03",

            "#104F唉～\x01",
            "真可悲啊……\x02",
        )
    )

    Jump("loc_7DE")

    label("loc_7DE")

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        "#1459F#11P真让人火大…………\x02",
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(300)
    OP_82(0x0, 0x0)
    Sleep(500)
    OP_8C(0x14, 225, 400)
    Sleep(100)

    def lambda_82C():
        OP_8E(0xFE, 0xFFFFFEE8, 0x0, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_82C)
    Sleep(100)
    OP_8C(0x107, 225, 400)
    Sleep(100)

    def lambda_858():
        OP_8E(0xFE, 0xFFFFFB82, 0x0, 0xBD6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_858)
    Sleep(100)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 180, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 180, 400)
    OP_82(0x1, 0x2)

    ChrTalk(    #8
        0x14,
        (
            "#1461F#5P好了好了，艾莉卡。\x01",
            "你要的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#061F#5P来，趁热喝哦。\x02",
    )

    CloseMessageWindow()
    Fade(350)
    OP_22(0x82, 0x0, 0x64)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -900, 800, 1400, 0)
    Sleep(200)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -1660, 800, 1400, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #10
        0x13,
        "#1832F#11P啧，暂时休战吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        "#101F#6P好～不客气了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x13,
        "#1457F#2P嗞嗞～…………！\x02",
    )


    ChrTalk(    #13
        0x12,
        "#104F#3P嗞嗞～…………！\x02",
    )

    OP_56(0x1)
    OP_59()
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 9)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x107, -2300, 200, 500, 90)
    SetChrPos(0x12, -2300, 200, 1800, 90)
    SetChrPos(0x13, 340, 200, 1610, 270)
    SetChrPos(0x14, 310, 200, 450, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x17, -1700, 800, 150, 0)
    SetChrPos(0x18, -1660, 800, 1400, 0)
    SetChrPos(0x19, -900, 800, 1400, 0)
    SetChrPos(0x1A, -900, 800, 150, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #14
        0x13,
        (
            "#1458F#11P呼…………\x02\x03",

            "#1450F好了。\x02\x03",

            "阿尔巴特·拉赛尔。\x01",
            "……礼物呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x12,
        (
            "#103F#6P礼物？\x02\x03",

            "为什么会是\x01",
            "轮到我来准备礼物啊？\x02\x03",

            "尽情享受外国旅行的\x01",
            "难道不是你们吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x13,
        (
            "#1459F#11P嗯…………\x02\x03",

            "…………都已经跟尤莉亚小姐\x01",
            "一起乘过埃尔赛尤号了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x13,
        (
            "#1830F#2P#3S至少要拿点尤莉亚小姐的照片啊手帕啊\x01",
            "#4S制服的扣子什么的吧！！#2S\x02",
        )
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#065F#6P制、制服的扣子……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "#1461F#2P哈哈，\x01",
            "尤莉亚小姐还在士官学校的时候\x01",
            "艾莉卡就是她的拥护者了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12,
        (
            "#104F#6P艾莉卡啊，\x01",
            "有空说这些无聊话，\x01",
            "不如去读读论文。\x02\x03",

            "真是的，你就是总这样才……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x13,
        "#1457F#11P……刚才，你侮辱尤莉亚大人了？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 6)
    SetChrSubChip(0x13, 0)

    def lambda_D9A():
        OP_96(0xFE, 0x172, 0x0, 0x9E2, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D9A)
    WaitChrThread(0x13, 0x1)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #22
        0x12,
        (
            "#101F#6P谁知道呢～我不明白你在说什么。\x02\x03",

            "我和尤莉亚上尉\x01",
            "在埃尔赛尤号上可是\x01",
            "经常一起喝茶的好朋友哦。\x02\x03",

            "#104F嗯，\x01",
            "她确实有不少优点……\x02",
        )
    )

    Jump("loc_E63")

    label("loc_E63")

    CloseMessageWindow()

    def lambda_E6A():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x9E2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E6A)
    WaitChrThread(0x13, 0x1)
    SetChrSubChip(0x107, 1)
    OP_8C(0x13, 180, 800)

    def lambda_E96():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBD6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E96)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)

    def lambda_EC0():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_EC0)

    def lambda_ECE():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x8FC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_ECE)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #23
        0x13,
        (
            "#1830F#5P这个臭老头……\x02\x03",

            "我非堵上你这张\x01",
            "不知好歹的嘴不可……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)

    def lambda_F51():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_F51)

    def lambda_F6B():
        OP_95(0xFE, 0x0, 0x12C, 0x0, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F6B)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    ClearChrFlags(0x12, 0x20)

    ChrTalk(    #24
        0x12,
        (
            "#101F#12P怎么样，羡慕吧？\x01",
            "羡慕吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x8)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)

    def lambda_FF1():
        OP_96(0xFE, 0xFFFFF542, 0x0, 0xFFFFFC7C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_FF1)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    def lambda_1019():
        OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0xFFFFFC7C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1019)
    WaitChrThread(0x107, 0x1)

    def lambda_1039():
        OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1039)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 600)
    Sleep(300)

    ChrTalk(    #25
        0x107,
        (
            "#62F真是的，你们两个！\x01",
            "没说两句就吵起来……\x02\x03",

            "…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_A3(0x1)
    OP_A2(0x0)
    OP_A6(0x1)
    ClearChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 310, 0, -300, 180)
    OP_22(0x1A, 0x0, 0x64)
    OP_0D()

    def lambda_10FB():
        OP_8E(0xFE, 0x136, 0x0, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_10FB)
    WaitChrThread(0x14, 0x1)

    def lambda_111B():
        OP_8E(0xFE, 0xFFFFF344, 0x0, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_111B)
    WaitChrThread(0x14, 0x1)

    def lambda_113B():
        OP_8E(0xFE, 0xFFFFF344, 0x0, 0x62C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_113B)
    WaitChrThread(0x14, 0x1)
    Sleep(300)

    ChrTalk(    #26
        0x14,
        (
            "#1463F#12P……提妲？\x02\x03",

            "怎么了？\x02",
        )
    )

    Jump("loc_1197")

    label("loc_1197")

    CloseMessageWindow()
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #27
        0x107,
        (
            "#066F不，没什么……\x02\x03",

            "上次像这样看到\x01",
            "妈妈和爷爷斗嘴，\x01",
            "已经是很久以前了……\x02\x03",

            "#067F嘿、嘿嘿……\x01",
            "感觉真是久违了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 90, 300)
    Sleep(300)

    ChrTalk(    #28
        0x14,
        "#1461F#6P嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)
    TurnDirection(0x14, 0x107, 400)
    Sleep(300)

    ChrTalk(    #29
        0x14,
        (
            "#1460F#12P提妲，\x01",
            "稍后一起去买东西吧。\x02\x03",

            "今天的晚饭我来做。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x14, 400)
    Sleep(300)

    ChrTalk(    #30
        0x107,
        (
            "#064F#5P咦，真的……？\x02\x03",

            "#066F……爸爸做的饭\x01",
            "也好久没吃了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x14,
        (
            "#1460F#12P目前暂时\x01",
            "也没有什么工作……\x02\x03",

            "从今天开始，\x01",
            "我就做一段时间的饭吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x107, 90, 400)
    Sleep(800)
    TurnDirection(0x107, 0x14, 400)
    Sleep(300)

    ChrTalk(    #32
        0x107,
        (
            "#560F#5P嗯、嗯……\x02\x03",

            "#67F那、那\x01",
            "我也来帮忙吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14,
        (
            "#1461F#12P哈哈……\x01",
            "多多关照啦，提妲。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1422():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1422)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x24, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x12, 0xFF)
    OP_6D(420, 0, 2360, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 9)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x107, -2300, 200, 500, 90)
    SetChrPos(0x12, -2300, 200, 1800, 90)
    SetChrPos(0x13, 340, 200, 1610, 270)
    SetChrPos(0x14, 310, 200, 450, 270)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x20, -1700, 800, 150, 0)
    SetChrPos(0x21, -1700, 800, 1400, 0)
    SetChrPos(0x22, -700, 800, 1400, 0)
    SetChrPos(0x23, -700, 800, 150, 0)
    SetChrPos(0x1D, -1100, 800, 850, 0)
    SetChrPos(0x1E, -1070, 800, 1720, 0)
    SetChrPos(0x1F, -1110, 800, 30, 0)
    Sleep(500)

    def lambda_15BE():
        OP_6B(2800, 14000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_15BE)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x107, 0x3, 0x0, 0x9)
    Sleep(2000)
    Sleep(300)
    FadeToDark(300, 0, -106)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x07\x00#40W那天的晚饭，\x01",
            "真是无比的丰盛。\x02\x03",

            "提妲被久别重逢的家人所包围，\x01",
            "度过了一段幸福时光。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00#40W而晚餐后……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_44(0x107, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_421 end

    def Function_3_16B6(): pass

    label("Function_3_16B6")


    def lambda_16BC():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_16BC)
    WaitChrThread(0x13, 0x1)

    def lambda_16DC():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_16DC)
    WaitChrThread(0x13, 0x1)

    def lambda_16FC():
        OP_8E(0xFE, 0x4F6, 0x0, 0x582, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_16FC)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 400)
    Sleep(300)
    Fade(500)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x13, 340, 200, 1610, 270)
    OP_0D()
    Return()

    # Function_3_16B6 end

    def Function_4_1749(): pass

    label("Function_4_1749")


    def lambda_174F():
        OP_8E(0xFE, 0xFFFFF2FE, 0x0, 0xFFFFF9D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_174F)
    WaitChrThread(0x12, 0x1)

    def lambda_176F():
        OP_8E(0xFE, 0xFFFFF2FE, 0x0, 0x582, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_176F)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 90, 400)
    Sleep(300)
    Fade(500)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -2300, 200, 1800, 90)
    OP_0D()
    Return()

    # Function_4_1749 end

    def Function_5_17BC(): pass

    label("Function_5_17BC")


    def lambda_17C2():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_17C2)
    WaitChrThread(0x14, 0x1)

    def lambda_17E2():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_17E2)
    WaitChrThread(0x14, 0x1)

    def lambda_1802():
        OP_8E(0xFE, 0x4F6, 0x0, 0x1086, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1802)
    WaitChrThread(0x14, 0x1)

    def lambda_1822():
        OP_8E(0xFE, 0x6C2, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1822)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 0, 400)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)
    LoadEffect(0x0, "map\\mp068_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 1870, 200, 5600, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x3C)
    Sleep(2000)
    LoadEffect(0x1, "map\\onsen00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1320, 1800, 5600, 0, 0, 0, 300, 200, 300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_17BC end

    def Function_6_18EC(): pass

    label("Function_6_18EC")


    def lambda_18F2():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_18F2)
    WaitChrThread(0x107, 0x1)

    def lambda_1912():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1912)
    WaitChrThread(0x107, 0x1)

    def lambda_1932():
        OP_8E(0xFE, 0x4F6, 0x0, 0x1086, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1932)
    WaitChrThread(0x107, 0x1)

    def lambda_1952():
        OP_8E(0xFE, 0x2B2, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1952)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 400)
    Return()

    # Function_6_18EC end

    def Function_7_1974(): pass

    label("Function_7_1974")


    ChrTalk(    #36
        0x13,
        (
            "#1451F#2P呼，\x01",
            "果然还是自己的家好啊～\x02\x03",

            "#1450F丹，麻烦你泡杯咖啡。\x01",
            "多放点牛奶哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #37
        0x14,
        (
            "#1460F#4P是是。\x01",
            "砂糖要三块对吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #38
        0x107,
        "#560F#4P啊，我也来帮忙吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Return()

    # Function_7_1974 end

    def Function_8_1A3B(): pass

    label("Function_8_1A3B")

    ClearChrFlags(0x12, 0x4)

    def lambda_1A46():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1A46)

    def lambda_1A64():
        OP_8F(0xFE, 0xFFFFF79A, 0x0, 0xE60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1A64)
    WaitChrThread(0x13, 0x1)

    label("loc_1A7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B52")

    def lambda_1A8D():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBA4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1A8D)
    WaitChrThread(0x13, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_1AB2():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1AB2)

    def lambda_1ACC():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xE60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1ACC)
    WaitChrThread(0x13, 0x1)

    def lambda_1AEC():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1AEC)
    WaitChrThread(0x12, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_1B11():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1B11)

    def lambda_1B2B():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x8FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B2B)
    WaitChrThread(0x12, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B4F")
    Jump("loc_1B52")

    label("loc_1B4F")

    Jump("loc_1A7E")

    label("loc_1B52")


    def lambda_1B58():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBA4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1B58)
    WaitChrThread(0x13, 0x1)

    def lambda_1B78():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1B78)

    def lambda_1B92():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1B92)
    Sleep(1000)

    def lambda_1BB1():
        OP_6D(-140, 0, 3800, 5000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1BB1)

    def lambda_1BC9():
        OP_67(0, 4700, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1BC9)

    def lambda_1BE1():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xF8C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1BE1)

    def lambda_1BFC():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1BFC)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(1000)
    OP_44(0x13, 0x2)
    OP_44(0x12, 0x2)

    def lambda_1C2E():

        label("loc_1C2E")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_1C2E")

    QueueWorkItem2(0x13, 0, lambda_1C2E)

    def lambda_1C3F():

        label("loc_1C3F")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_1C3F")

    QueueWorkItem2(0x12, 0, lambda_1C3F)
    OP_A2(0x1)

    label("loc_1C4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DCB")

    def lambda_1C5C():
        OP_8F(0xFE, 0xFFFFFD44, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C5C)

    def lambda_1C77():
        OP_8F(0xFE, 0x1F4, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1C77)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_1C9C():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xCE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C9C)

    def lambda_1CB7():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xF8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1CB7)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_1CDC():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1CDC)

    def lambda_1CF6():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1CF6)
    Sleep(1000)

    def lambda_1D15():
        OP_8F(0xFE, 0xFFFFFD44, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D15)

    def lambda_1D30():
        OP_8F(0xFE, 0x1F4, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1D30)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_1D55():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xCE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D55)

    def lambda_1D70():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xF8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1D70)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_1D95():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1D95)

    def lambda_1DAF():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1DAF)
    Sleep(1000)
    Jump("loc_1C4D")

    label("loc_1DCB")

    Return()

    # Function_8_1A3B end

    def Function_9_1DCC(): pass

    label("Function_9_1DCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E34")
    OP_62(0x107, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_62(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_62(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_62(0x14, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    Jump("Function_9_1DCC")

    label("loc_1E34")

    Return()

    # Function_9_1DCC end

    def Function_10_1E35(): pass

    label("Function_10_1E35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-3220, 0, -1000, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 1660, 0, 4750, 0)
    SetChrPos(0x107, -2870, 4000, 5150, 270)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x107, 14)
    SetChrSubChip(0x107, 0)

    def lambda_1EC0():
        OP_6D(-3220, 0, 2300, 4000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1EC0)
    FadeToBright(2000, 0)

    def lambda_1EE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1EE1)

    def lambda_1EF3():
        OP_8E(0xFE, 0xFFFFE890, 0x7D0, 0x141E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1EF3)
    WaitChrThread(0x107, 0x1)

    def lambda_1F13():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x334, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1F13)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    Sleep(500)

    ChrTalk(    #39
        0x107,
        (
            "#1271F#6P呜～……睡过头了……\x02\x03",

            "早上好～爷爷……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #40
        0x14,
        "男性的声音",
        "#6P早啊，提妲。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_1FC5():
        OP_6D(2380, 0, 6080, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1FC5)

    def lambda_1FDD():
        OP_6B(2960, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1FDD)

    def lambda_1FED():
        OP_67(0, 4560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_1FED)

    def lambda_2005():
        OP_8E(0xFE, 0xFFFFEE3A, 0x0, 0x334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2005)
    WaitChrThread(0x107, 0x1)

    def lambda_2025():
        OP_8E(0xFE, 0xFFFFFD80, 0x0, 0x1284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2025)
    WaitChrThread(0x107, 0x1)

    def lambda_2045():
        OP_8E(0xFE, 0xA0, 0x0, 0x1284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2045)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #41
        0x107,
        "#1264F#6P……咦，爸爸？\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #42
        0x107,
        (
            "#1267F#6P啊，对了。\x02\x03",

            "爸爸和妈妈\x01",
            "都回来啦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x107, 300)
    Sleep(300)

    ChrTalk(    #43
        0x14,
        "#1461F#11P哈哈，看来你睡得很好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        (
            "#1272F#6P嗯、嗯……\x02\x03",

            "对不起，\x01",
            "我完全忘了……\x02",
        )
    )

    Jump("loc_216B")

    label("loc_216B")

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x107,
        (
            "#1262F#6P啊……对、对了！\x02\x03",

            "昨天的事！\x01",
            "你说过今天告诉我的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x14,
        (
            "#1460F#11P没问题，我记着呢。\x02\x03",

            "不过呢，\x01",
            "你大概还是\x01",
            "直接问那两个人比较好吧。\x02",
        )
    )

    Jump("loc_223F")

    label("loc_223F")

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        "#1264F#6P妈妈和爷爷？\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x107, 180, 500)
    Sleep(600)
    OP_8C(0x107, 225, 500)
    Sleep(600)
    OP_8C(0x107, 180, 500)
    Sleep(300)

    ChrTalk(    #48
        0x14,
        (
            "#1460F#11P他们俩好像\x01",
            "谈了一整夜哦。\x02\x03",

            "而且一大早\x01",
            "就赶去中央工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#1262F#5P好、好……！\x02",
    )

    CloseMessageWindow()

    def lambda_2309():

        label("loc_2309")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_2309")

    QueueWorkItem2(0x14, 2, lambda_2309)

    def lambda_231A():
        OP_8E(0xFE, 0xA0, 0x0, 0xE9C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_231A)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #50
        0x14,
        "#1463F#5P啊啊，提妲……\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x107, 0x14, 500)
    Sleep(500)

    ChrTalk(    #51
        0x14,
        (
            "#1460F#5P在此之前\x01",
            "要先吃早饭哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #52
        0x107,
        (
            "#1273F啊，忘得一干二净……\x02\x03",

            "而且还没洗脸，\x01",
            "还要梳头发……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x14,
        (
            "#1460F#5P那么，\x01",
            "稍后再吃早饭吧。\x02\x03",

            "……我帮你保一下温。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x107,
        "#1267F嗯、嗯！！\x02",
    )

    CloseMessageWindow()
    OP_44(0x14, 0xFF)
    OP_43(0x107, 0x3, 0x0, 0xB)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1E35 end

    def Function_11_24B9(): pass

    label("Function_11_24B9")

    SetChrFlags(0x107, 0x1000)
    OP_8C(0x107, 270, 600)

    def lambda_24CB():
        OP_8E(0xFE, 0xFFFFF8E4, 0x0, 0xE9C, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_24CB)
    WaitChrThread(0x107, 0x1)

    def lambda_24EB():
        OP_8E(0xFE, 0xFFFFED72, 0x0, 0x334, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_24EB)
    WaitChrThread(0x107, 0x1)

    def lambda_250B():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x334, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_250B)
    WaitChrThread(0x107, 0x1)

    def lambda_252B():
        OP_8E(0xFE, 0xFFFFE890, 0x7D0, 0x141E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_252B)
    WaitChrThread(0x107, 0x1)

    def lambda_254B():
        OP_8E(0xFE, 0xFFFFF4CA, 0xFA0, 0x141E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_254B)
    WaitChrThread(0x107, 0x1)
    Return()

    # Function_11_24B9 end

    def Function_12_2566(): pass

    label("Function_12_2566")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 32860, -1000, 4940, 90)
    SetChrPos(0x11, 32659, -1000, 2600, 180)
    LoadEffect(0x1, "monster\\ms31000.eff")
    OP_6D(25620, -1000, 4400, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)

    def lambda_2621():
        OP_6D(34020, -880, 5070, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2621)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x2, 0x10, 0, 800, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x11, 0, 800, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)

    def lambda_26C6():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_26C6)

    def lambda_26D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_26D6)

    def lambda_26E8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_26E8)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0xD)
    OP_43(0x11, 0x0, 0x0, 0xE)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4122   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2566 end

    def Function_13_2765(): pass

    label("Function_13_2765")

    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_13_2765 end

    def Function_14_278F(): pass

    label("Function_14_278F")

    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 600)
    OP_8C(0xFE, 270, 600)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    Return()

    # Function_14_278F end

    SaveToFile()

Try(main)
