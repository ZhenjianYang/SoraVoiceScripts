from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2410   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2410.x',
        MapIndex            = 1,
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
        '水壶',                                 # 9
        '红茶',                                 # 10
        '红茶',                                 # 11
        '红茶',                                 # 12
        '红茶',                                 # 13
        '特蕾莎院长',                           # 14
        '达尼艾尔',                             # 15
        '玛丽',                                 # 16
        '克拉姆',                               # 17
        '波利',                                 # 18
        '乔儿',                                 # 19
        '水壶',                                 # 20
        '目标用照相机',                         # 21
        '',                                     # 22
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02590 ._CH',             # 03
        'ED6_DT07/CH02500 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT06/CH20021 ._CH',             # 09
        'ED6_DT07/CH02573 ._CH',             # 0A
        'ED6_DT07/CH02390 ._CH',             # 0B
        'ED6_DT07/CH02393 ._CH',             # 0C
        'ED6_DT06/CH20094 ._CH',             # 0D
        'ED6_DT06/CH20095 ._CH',             # 0E
        'ED6_DT06/CH20096 ._CH',             # 0F
        'ED6_DT06/CH20097 ._CH',             # 10
        'ED6_DT26/CH20784 ._CH',             # 11
        'ED6_DT26/CH20278 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02590P._CP',             # 03
        'ED6_DT07/CH02500P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT06/CH20021P._CP',             # 09
        'ED6_DT07/CH02573P._CP',             # 0A
        'ED6_DT07/CH02390P._CP',             # 0B
        'ED6_DT07/CH02393P._CP',             # 0C
        'ED6_DT06/CH20094P._CP',             # 0D
        'ED6_DT06/CH20095P._CP',             # 0E
        'ED6_DT06/CH20096P._CP',             # 0F
        'ED6_DT06/CH20097P._CP',             # 10
        'ED6_DT26/CH20784P._CP',             # 11
        'ED6_DT26/CH20278P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703944,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 14600,
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
        X                   = 35100,
        Z                   = 0,
        Y                   = 2300,
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
        X                   = 35300,
        Z                   = 0,
        Y                   = -35300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 32500,
        Z                   = 0,
        Y                   = -34400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 65554,
        ChipIndex           = 0x12,
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
        "Function_0_2E2",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_30C",          # 02, 2
        "Function_3_322",          # 03, 3
        "Function_4_1771",         # 04, 4
        "Function_5_17DB",         # 05, 5
        "Function_6_1817",         # 06, 6
        "Function_7_185F",         # 07, 7
        "Function_8_18A7",         # 08, 8
        "Function_9_1925",         # 09, 9
        "Function_10_194D",        # 0A, 10
        "Function_11_19AE",        # 0B, 11
        "Function_12_1A2E",        # 0C, 12
        "Function_13_2DBF",        # 0D, 13
        "Function_14_2DEF",        # 0E, 14
        "Function_15_2E1D",        # 0F, 15
        "Function_16_2E52",        # 10, 16
        "Function_17_2EA7",        # 11, 17
    )


    def Function_0_2E2(): pass

    label("Function_0_2E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_301")
    SetMapFlags(0x10000000)
    Event(0, 12)
    Jump("loc_30A")

    label("loc_301")

    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_30A")

    Return()

    # Function_0_2E2 end

    def Function_1_30B(): pass

    label("Function_1_30B")

    Return()

    # Function_1_30B end

    def Function_2_30C(): pass

    label("Function_2_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_30C")

    label("loc_321")

    Return()

    # Function_2_30C end

    def Function_3_322(): pass

    label("Function_3_322")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-560, 0, 3500, 0)
    OP_67(0, 3800, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(30000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x105, -1400, 0, -3500, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -1580, 0, 4620, 270)
    SetChrPos(0x18, -1200, 0, -3500, 180)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -4260, 600, 6460, 0)
    SetChrPos(0x12, -4260, 600, 5460, 0)
    SetChrPos(0x13, -3560, 600, 5460, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)

    def lambda_41F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_41F)

    def lambda_431():
        OP_8E(0xFE, 0xFFFFFC54, 0x0, 0xA50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_431)
    Sleep(1000)

    def lambda_451():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_451)

    def lambda_463():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_463)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)

    ChrTalk(    #0
        0x105,
        "#044F#12P………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0x1)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x15, 0x18, 400)
    Sleep(300)

    ChrTalk(    #1
        0x15,
        (
            "#752F#5P哎呀克拉姆，\x01",
            "你跑到哪儿去了？\x02\x03",

            "大家早就……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    def lambda_541():

        label("loc_541")

        TurnDirection(0xFE, 0x105, 600)
        OP_48()
        Jump("loc_541")

    QueueWorkItem2(0x18, 2, lambda_541)
    Sleep(600)

    def lambda_557():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0x9EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_557)
    Sleep(100)

    def lambda_577():
        OP_8F(0xFE, 0x50, 0x0, 0x8C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_577)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    ChrTalk(    #2
        0x15,
        (
            "#753F#5P哎呀？　你是……\x02\x03",

            "#751F难道是科洛丝？\x02\x03",

            "都长这么大了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#049F#12P#40W…………特蕾莎……老师……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_62F():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_62F)
    Sleep(1000)

    ChrTalk(    #4 op#A op#5
        0x105,
        "#043F#12P#30A老师、老师……！\x05\x02",
    )

    Sleep(500)
    OP_21()
    OP_1D(0xB2)
    Sleep(500)

    def lambda_685():
        OP_6B(2960, 800)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_685)

    def lambda_695():
        OP_8F(0xFE, 0xFFFFFAB0, 0x0, 0x870, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695)
    Sleep(580)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)

    def lambda_6CE():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0xA50, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6CE)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #5
        0x105,
        (
            "#049F#12P老、老师，那个……\x01",
            "……我、我…………\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x105, 0x2, 0x0, 0x4)
    Sleep(2000)

    ChrTalk(    #6
        0x15,
        (
            "#751F#5P哎呀哎呀，\x01",
            "爱哭的样子还是没变呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0x2)

    ChrTalk(    #7
        0x105,
        "#047F#12P因、因为…………！\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0xFFFFFFCE, 2000, 0x18, 0x1B, 0x12C, 0x0)
    OP_43(0x105, 0x2, 0x0, 0x4)
    Sleep(2000)

    ChrTalk(    #8
        0x18,
        (
            "#774F#11P咦…………？？\x02\x03",

            "怎、怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)
    OP_44(0x105, 0x2)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)

    def lambda_819():
        OP_6B(3060, 1000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_819)

    def lambda_829():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0x564, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_829)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        (
            "#045F#12P啊、啊哈哈……\x02\x03",

            "#540F对、对不起。\x01",
            "我失态了。\x02\x03",

            "我实在太高兴，忍不住……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x15,
        (
            "#750F#5P……科洛丝…………\x02\x03",

            "#751F呵呵，欢迎回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        (
            "#048F#12P是！\x01",
            "……呜………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x15,
        (
            "#751F#5P哎呀哎呀。\x01",
            "真是一点都没变呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x18, 380)
    Sleep(300)

    ChrTalk(    #13
        0x15,
        (
            "#750F#1P克拉姆也回来啦。\x02\x03",

            "以后可不能随便跑出去了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #14
        0x18,
        (
            "#772F#11P我、我只是\x01",
            "去找东西而已啦！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x105, 300, 500)
    Sleep(600)
    OP_8C(0x105, 30, 500)
    Sleep(600)
    OP_8C(0x105, 345, 500)
    Sleep(500)

    ChrTalk(    #15
        0x105,
        (
            "#542F#12P对了，特蕾莎老师。\x01",
            "约瑟夫叔叔在哪里……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x105, 380)
    Sleep(500)

    ChrTalk(    #16
        0x15,
        (
            "#754F#5P…………………………\x02\x03",

            "……是吗，\x01",
            "科洛丝还不知道啊……\x02\x03",

            "#757F我丈夫……\x01",
            "他已经过世了。\x02\x03",

            "已经过去四年了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#044F#12P……………………\x02\x03",

            "#40W…………咦………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x15,
        (
            "#754F#5P去卢安买东西的时候\x01",
            "遇上了事故……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(300)

    def lambda_B8C():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B8C)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #19
        0x105,
        (
            "#043F#40W#12P…………………………\x02\x03",

            "#049F……对……对不起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x15,
        "#750F#5P……为什么要道歉？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#542F#12P#40W我……我……\x01",
            "……什么也不知道………\x02\x03",

            "只会胡乱耍性子……\x01",
            "明明最喜欢这里了……\x02\x03",

            "#043F却总坚持着不来……\x01",
            "……只顾自己钻牛角尖……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #22
        0x105,
        (
            "#049F#40W要是能早点……#500W　\x01",
            "#15W#3S要是能早点回来……！！#2S\x02",
        )
    )

    Sleep(800)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_9E(0x105, 0x7, 0x0, 0xC8, 0x7D0)
    Sleep(800)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x19, 500, 2000, 14700, 180)
    SetChrPos(0x17, 500, 2000, 14700, 180)
    SetChrPos(0x16, 1000, 2000, 14700, 180)

    NpcTalk(    #23
        0x19,
        "小孩子的声音",
        "#4P啊哈哈！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x17,
        "小孩子的声音",
        "#4P说什么呢～！\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #25
        0x105,
        "#044F#12P#40W……咦………………？\x02",
    )

    CloseMessageWindow()
    OP_44(0x18, 0x2)

    def lambda_E2A():

        label("loc_E2A")

        TurnDirection(0xFE, 0x17, 500)
        OP_48()
        Jump("loc_E2A")

    QueueWorkItem2(0x18, 2, lambda_E2A)
    Sleep(100)

    def lambda_E40():

        label("loc_E40")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_E40")

    QueueWorkItem2(0x15, 2, lambda_E40)

    def lambda_E51():
        OP_67(0, 3600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_E51)

    def lambda_E69():
        OP_8E(0xFE, 0x190, 0x0, 0x1B58, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E69)
    Sleep(600)
    OP_43(0x19, 0x3, 0x0, 0x6)
    Sleep(600)
    OP_43(0x16, 0x3, 0x0, 0x7)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x19, 0x1)
    WaitChrThread(0x16, 0x1)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #26
        0x17,
        "女孩子",
        (
            "#1714F啊，克拉姆！\x02\x03",

            "#1715F你到哪里去了啦，真是的。\x02",
        )
    )

    Jump("loc_F16")

    label("loc_F16")

    CloseMessageWindow()

    def lambda_F1D():
        OP_8E(0xFE, 0xC8, 0x0, 0x1068, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_F1D)
    Sleep(300)
    OP_43(0x19, 0x3, 0x0, 0x8)
    Sleep(300)

    def lambda_F49():
        OP_8E(0xFE, 0x4B0, 0x0, 0xE60, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_F49)
    WaitChrThread(0x16, 0x1)
    TurnDirection(0x16, 0x18, 500)
    WaitChrThread(0x19, 0x3)

    NpcTalk(    #27
        0x19,
        "年幼的女孩子",
        (
            "#1733F#6P啊～…………\x02\x03",

            "姐姐，\x01",
            "你为什么哭呢～？\x02",
        )
    )

    Jump("loc_FC6")

    label("loc_FC6")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #28
        0x105,
        "#043F#11P嗯、嗯……呃……？\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0x2)
    OP_44(0x18, 0x2)
    OP_44(0x15, 0x2)
    TurnDirection(0x15, 0x105, 400)
    Sleep(300)

    ChrTalk(    #29
        0x15,
        (
            "#751F#5P呵呵，\x01",
            "这些是我现在正在照顾的孩子们。\x02\x03",

            "#750F来，大家都来打个招呼吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("孩子们")

    AnonymousTalk(    #30
        "\x07\x00#4S好——！#2S\x02",
    )

    Jump("loc_10B7")

    label("loc_10B7")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_10DB():
        OP_6D(710, 0, 3690, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_10DB)

    def lambda_10F3():
        OP_6B(2960, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_10F3)

    def lambda_1103():
        OP_6C(38000, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1103)

    def lambda_1113():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1113)

    def lambda_1121():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1121)
    OP_43(0x16, 0x3, 0x0, 0x9)
    Sleep(300)
    OP_8C(0x18, 225, 400)
    Sleep(800)
    OP_8C(0x19, 45, 400)
    Sleep(800)
    WaitChrThread(0x16, 0x3)

    NpcTalk(    #31
        0x17,
        "女孩子",
        "#1718F#5P我是玛丽～！\x02",
    )

    Jump("loc_1190")

    label("loc_1190")

    CloseMessageWindow()
    OP_8C(0x19, 90, 400)
    Sleep(300)

    NpcTalk(    #32
        0x19,
        "年幼的女孩子",
        "#1730F#6P？？　哎～？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #33
        0x16,
        "男孩",
        "#1721F#11P你好～，大姐姐！\x02",
    )

    Jump("loc_11FD")

    label("loc_11FD")

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 500)
    Sleep(300)

    ChrTalk(    #34
        0x18,
        (
            "#772F#11P喂，波利。\x01",
            "什么叫『哎～』啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        "#044F#12P#40W……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x15,
        (
            "#750F#5P科洛丝？\x02\x03",

            "玛西亚孤儿院，\x01",
            "一直都在这里哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#542F#12P#40W……………啊………………\x02\x03",

            "#041F#20W………是……………！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1310():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1310)

    ChrTalk(    #38
        0x15,
        (
            "#750F#5P现在时间也刚刚好，\x01",
            "我们来喝茶吧。\x02\x03",

            "#751F科洛丝，要来帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#048F#12P……好的………！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 0, 500)
    OP_43(0x15, 0x3, 0x0, 0xA)
    Sleep(500)

    def lambda_13AF():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x8AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13AF)
    Sleep(400)

    def lambda_13CF():

        label("loc_13CF")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13CF")

    QueueWorkItem2(0x17, 2, lambda_13CF)

    def lambda_13E0():

        label("loc_13E0")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13E0")

    QueueWorkItem2(0x18, 2, lambda_13E0)

    def lambda_13F1():

        label("loc_13F1")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13F1")

    QueueWorkItem2(0x16, 2, lambda_13F1)

    def lambda_1402():

        label("loc_1402")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_1402")

    QueueWorkItem2(0x19, 2, lambda_1402)

    def lambda_1413():
        OP_8F(0xFE, 0xFFFFF574, 0x0, 0x500, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1413)
    Sleep(200)

    def lambda_1433():
        OP_8F(0xFE, 0xFFFFF678, 0x0, 0xA00, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1433)
    Sleep(200)

    def lambda_1453():
        OP_8F(0xFE, 0xFFFFFC68, 0x0, 0xA3C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1453)
    Sleep(200)

    def lambda_1473():
        OP_8F(0xFE, 0xFFFFFBF0, 0x0, 0x654, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1473)
    WaitChrThread(0x105, 0x1)
    OP_43(0x105, 0x3, 0x0, 0xB)
    Sleep(500)
    OP_8C(0x105, 90, 500)
    Sleep(1000)
    OP_8C(0x105, 280, 500)
    Sleep(1000)
    FadeToDark(2000, 0, 120)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x18\x07\x0C#40W自从那天以后，\x01",
            "一有空就去孤儿院转转成了我每天的必修课。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #41
        "\x18\x07\x0C#40W果然，我或许并没有改变。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x18\x07\x0C#40W依然软弱的我，怀抱着对温暖空间的憧憬。\x01",
            "被怀念的老师和可爱的孩子们的温暖所包围。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #43
        "\x18\x07\x0C#40W我就在这里，与欢声笑语在一起直到内心满足。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x18\x07\x0C#40W幼年时的温馨\x01",
            "是不知双亲的我唯一的回忆……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x18\x07\x0C#40W这样的回忆和孤儿院一起\x01",
            "一如既往的留在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x18\x07\x0C#40W所以我安心了……\x01",
            "能够继续欺骗自己了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #47
        "\x18\x07\x0C#40W是的，我的心………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #48
        "\x18\x07\x0C#40W――并没有那么美丽。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_20(0xFA0)
    OP_21()
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x00#40W――一个月后。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_322 end

    def Function_4_1771(): pass

    label("Function_4_1771")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17DA")

    def lambda_1780():
        OP_9E(0xFE, 0x5, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1780)
    Sleep(1800)

    def lambda_179F():
        OP_9E(0xFE, 0x9, 0x0, 0x4B0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_179F)
    Sleep(5000)

    def lambda_17BE():
        OP_9E(0xFE, 0x7, 0x0, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_17BE)
    Sleep(3400)
    Jump("Function_4_1771")

    label("loc_17DA")

    Return()

    # Function_4_1771 end

    def Function_5_17DB(): pass

    label("Function_5_17DB")


    def lambda_17E1():
        OP_8F(0xFE, 0xFFFFF9C0, 0x0, 0xC58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_17E1)
    WaitChrThread(0x17, 0x1)

    def lambda_1801():
        OP_8F(0xFE, 0xFFFFF678, 0x0, 0xA00, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1801)
    Return()

    # Function_5_17DB end

    def Function_6_1817(): pass

    label("Function_6_1817")


    def lambda_181D():
        OP_8E(0xFE, 0x1F4, 0x0, 0x2864, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_181D)
    WaitChrThread(0x19, 0x1)

    def lambda_183D():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x1F04, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_183D)
    WaitChrThread(0x19, 0x1)
    OP_8C(0x19, 180, 600)
    Return()

    # Function_6_1817 end

    def Function_7_185F(): pass

    label("Function_7_185F")


    def lambda_1865():
        OP_8E(0xFE, 0x3E8, 0x0, 0x25A8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1865)
    WaitChrThread(0x16, 0x1)

    def lambda_1885():
        OP_8E(0xFE, 0x528, 0x0, 0x1F04, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1885)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 180, 600)
    Return()

    # Function_7_185F end

    def Function_8_18A7(): pass

    label("Function_8_18A7")


    def lambda_18AD():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0x1950, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_18AD)
    WaitChrThread(0x19, 0x1)

    def lambda_18CD():
        OP_8E(0xFE, 0xFFFFF678, 0x0, 0xA28, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_18CD)
    WaitChrThread(0x19, 0x1)

    def lambda_18ED():

        label("loc_18ED")

        TurnDirection(0xFE, 0x19, 500)
        OP_48()
        Jump("loc_18ED")

    QueueWorkItem2(0x105, 2, lambda_18ED)

    def lambda_18FE():
        OP_8E(0xFE, 0xFFFFF678, 0x0, 0x3D4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_18FE)
    WaitChrThread(0x19, 0x1)
    TurnDirection(0x19, 0x105, 500)
    Sleep(300)
    Return()

    # Function_8_18A7 end

    def Function_9_1925(): pass

    label("Function_9_1925")


    def lambda_192B():
        OP_8E(0xFE, 0x1D6, 0x0, 0x596, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_192B)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 270, 600)
    Return()

    # Function_9_1925 end

    def Function_10_194D(): pass

    label("Function_10_194D")


    def lambda_1953():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x2508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1953)
    WaitChrThread(0x15, 0x1)

    def lambda_1973():
        OP_8E(0xFE, 0xFFFFF1A0, 0x0, 0x2508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1973)
    WaitChrThread(0x15, 0x1)

    def lambda_1993():
        OP_8E(0xFE, 0xFFFFF1A0, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1993)
    WaitChrThread(0x15, 0x1)
    Return()

    # Function_10_194D end

    def Function_11_19AE(): pass

    label("Function_11_19AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A2D")
    OP_62(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x16, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_11_19AE")

    label("loc_1A2D")

    Return()

    # Function_11_19AE end

    def Function_12_1A2E(): pass

    label("Function_12_1A2E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-720, 0, 8640, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -2720, 0, 8260, 200)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, -2500, 240, 6020, 270)
    SetChrChipByIndex(0x1A, 12)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x105,
        (
            "#542F#5P稍微等等哦。\x01",
            "我这就泡茶。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 320, 500)
    OP_43(0x105, 0x0, 0x0, 0x11)
    Sleep(500)
    SetChrSubChip(0x1A, 2)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    SetChrSubChip(0x1A, 1)
    Sleep(600)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    SetChrSubChip(0x1A, 2)
    Sleep(1200)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    OP_22(0xA4, 0x0, 0x64)
    Fade(250)
    SetChrPos(0x1A, -1580, 0, 6020, 270)
    ClearChrFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)
    Sleep(500)

    def lambda_1B7D():
        OP_6D(-1740, 0, 14180, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_1B7D)

    def lambda_1B95():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0x2468, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1B95)
    WaitChrThread(0x1A, 0x1)

    def lambda_1BB5():
        OP_8E(0xFE, 0xFFFFF434, 0x0, 0x2468, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BB5)
    WaitChrThread(0x1A, 0x1)

    def lambda_1BD5():
        OP_8E(0xFE, 0xFFFFF434, 0x0, 0x30AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BD5)
    WaitChrThread(0x1A, 0x1)
    Sleep(500)

    ChrTalk(    #51
        0x1A,
        (
            "#1892F#12P那个、那个……\x02\x03",

            "#645F对、对不起，科洛丝。\x02\x03",

            "我说话真是不经大脑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#543F#5P不，没关系的。\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #53
        0x105,
        (
            "#049F#5P……乔儿同学，我啊……\x02\x03",

            "#542F自幼就父母双亡了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x1A,
        "#643F#12P咦……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x1A, 400)
    Sleep(300)

    ChrTalk(    #55
        0x105,
        (
            "#542F#5P…………所以呢。\x02\x03",

            "#543F或许是在那些孩子身上，\x01",
            "我看到了自己的影子。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_6D(-2440, 240, 8340, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, -5260, 240, 7300, 90)
    SetChrChipByIndex(0x105, 7)
    SetChrSubChip(0x105, 0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, -2500, 240, 7300, 270)
    SetChrChipByIndex(0x1A, 12)
    SetChrSubChip(0x1A, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, -3540, 600, 7080, 0)
    SetChrPos(0x12, -4480, 600, 7080, 0)
    SetChrPos(0x10, -4100, 650, 6600, 0)
    Sleep(1200)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x105,
        (
            "#543F#6P没有父母\x01",
            "并不一定是不幸。\x02\x03",

            "只是因为这理由\x01",
            "就认定这个人的一生是不幸的，\x01",
            "我讨厌这种想法。\x02\x03",

            "我一直是这么想的。\x02\x03",

            "#049F不想被别人说\x01",
            "自己『很可怜』。\x02\x03",

            "……我不想被人这样说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x1A,
        (
            "#1892F#11P那、那个……\x02\x03",

            "科洛丝，\x01",
            "关于那件事……\x02",
        )
    )

    Jump("loc_1F75")

    label("loc_1F75")

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        (
            "#047F#6P不，乔儿同学。\x01",
            "让我说到最后吧。\x02\x03",

            "#042F我其实…………\x01",
            "并不是为这里的孩子着想\x01",
            "而生气的。\x02\x03",

            "我那时候，是为自己而生气。\x02\x03",

            "然后对『优等生』、『献身』什么的，\x01",
            "对这些词感到愤怒。\x02\x03",

            "#049F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x1A,
        "#643F#11P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x105,
        (
            "#049F#6P#40W这是伪善，对吧……\x02\x03",

            "这样的心情被乔儿同学\x01",
            "给一语道破……\x02\x03",

            "而我又不愿意承认……\x02\x03",

            "#047F然后终于，\x01",
            "忍不住发火了。\x02\x03",

            "…………真的很对不起。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #61
        0x1A,
        (
            "#1892F#11P哎……\x02\x03",

            "#1893F不、不～科洛丝……\x01",
            "#3S真～的很对不起！！#2S\x02\x03",

            "我、我完全\x01",
            "不是这个意思……\x02\x03",

            "而且，我完全\x01",
            "不了解科洛丝的情况…………\x02\x03",

            "我绝对不是\x01",
            "想说你伪善的。\x01",
            "真～的很抱歉！！\x02\x03",

            "#1892F本来我是想\x01",
            "早点来道歉的……\x01",
            "…………那、那个……\x02\x03",

            "却不知道该怎么\x01",
            "说出口才好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        "#543F#6P……………嗯………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x1A,
        (
            "#647F#11P还有，\x01",
            "我也收回说孩子们可怜的话。\x02\x03",

            "#1890F我明明从来\x01",
            "没有来过这里……\x02\x03",

            "明明根本不知道\x01",
            "孤儿院的孩子是什么样……\x02\x03",

            "#1893F就随便那样乱说，\x01",
            "真是对不起！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #64
        0x105,
        (
            "#543F#6P……对了，乔儿同学。\x02\x03",

            "#542F你要不要去\x01",
            "看看孩子们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x1A,
        "#643F#11P咦……！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6F(0x2, 10)
    OP_6F(0x3, 20)
    OP_6F(0x4, 15)
    OP_6F(0x5, 15)
    OP_6D(36900, 0, -32900, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    SetChrFlags(0x19, 0x2)
    SetChrPos(0x18, 37940, 1500, -36940, 225)
    SetChrPos(0x16, 37940, 200, -36940, 225)
    SetChrPos(0x17, 37960, 1500, -32830, 225)
    SetChrPos(0x19, 37960, 200, -32830, 225)
    SetChrChipByIndex(0x18, 13)
    SetChrSubChip(0x18, 0)
    SetChrChipByIndex(0x16, 14)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x17, 15)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x19, 16)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x105, 0x4)
    SetChrPos(0x105, 34000, 0, -30160, 180)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    ClearChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 34000, 0, -30160, 180)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_25A5():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF7900, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_25A5)
    Sleep(800)
    OP_43(0x105, 0x3, 0x0, 0x10)
    WaitChrThread(0x1A, 0x1)
    Sleep(500)
    OP_8C(0x1A, 270, 500)
    Sleep(1000)
    OP_8C(0x1A, 90, 500)

    ChrTalk(    #66
        0x1A,
        (
            "#643F#6P哦～……\x01",
            "是双层床啊。\x02\x03",

            "#640F真不错啊～……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_262F():
        OP_6D(37810, 0, -33430, 2500)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_262F)
    OP_43(0x105, 0x0, 0x0, 0xF)

    def lambda_264E():
        OP_8E(0xFE, 0x9088, 0x0, 0xFFFF7900, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_264E)
    WaitChrThread(0x1A, 0x1)
    OP_8C(0x1A, 180, 600)
    Sleep(1000)
    OP_8C(0x1A, 10, 600)
    Sleep(500)
    WaitChrThread(0x105, 0x0)
    WaitChrThread(0x1C, 0x0)

    ChrTalk(    #67
        0x19,
        "啊嚏……！\x02",
    )

    OP_9E(0x19, 0xA, 0xA, 0xC8, 0x7D0)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #68
        0x1A,
        "#641F#12P啊哈哈，好可爱！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8F(0x1A, 0x909C, 0x0, 0xFFFF7A2C, 0x3E8, 0x0)
    Sleep(300)
    OP_22(0x186, 0x0, 0x64)
    Fade(500)
    OP_70(0x3, 0xF)
    OP_73(0x3)
    OP_0D()
    Sleep(300)
    OP_8F(0x1A, 0x9088, 0x0, 0xFFFF7900, 0x3E8, 0x0)
    Sleep(300)

    def lambda_2736():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2736)
    Sleep(100)
    OP_8C(0x105, 90, 400)
    Sleep(500)

    ChrTalk(    #69
        0x1A,
        "#649F#11P真是可爱的睡相啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1A)
    Sleep(500)

    ChrTalk(    #70
        0x1A,
        (
            "#1890F#11P哈哈，\x01",
            "在不知情的情况下伤害了他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x105,
        (
            "#047F#6P嗯……我也要说声抱歉。\x02\x03",

            "#049F那个时候我明明知道\x01",
            "乔儿同学不是故意的……\x02\x03",

            "却擅自生起气来……\x01",
            "朝你乱发脾气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x1A,
        (
            "#644F#11P没、没关系啦，这点小事。\x01",
            "本来就是我不对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        (
            "#543F#6P呵呵……但是呢。\x02\x03",

            "因为这次的事情，\x01",
            "我似乎也整理好了心情。\x02\x03",

            "现在能感觉到\x01",
            "不可思议的平静。\x02\x03",

            "#542F……因为我果然还是认为\x01",
            "这里是最重要的地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #74
        0x105,
        (
            "#045F#6P其实，\x01",
            "我有点睡眠不足……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x1A,
        (
            "#643F#11P咦，科洛丝也是？\x02\x03",

            "#645F我、我昨天\x01",
            "也完全没睡着……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x1A)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #76
        0x1A,
        "#649F#11P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x105,
        "#041F#6P呵呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x1A,
        (
            "#640F#11P那么……\x02\x03",

            "#648F差不多该走了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x105,
        "#048F#6P嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2ABE():
        OP_6D(36900, 0, -32900, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2ABE)
    OP_43(0x105, 0x0, 0x0, 0xD)
    OP_43(0x1A, 0x0, 0x0, 0xE)
    WaitChrThread(0x105, 0x0)
    OP_71(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_2B00():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF8A30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B00)
    WaitChrThread(0x1A, 0x0)

    def lambda_2B20():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF8A30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2B20)
    WaitChrThread(0x1A, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 20)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    Sleep(1000)

    ChrTalk(    #80
        0x1A,
        "#644F#12P啊，对了，科洛丝……\x02",
    )

    CloseMessageWindow()

    def lambda_2B88():
        OP_6B(3800, 20000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_2B88)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #81
        (
            "\x07\x0C#40W从以前开始\x01",
            "我就一直想说了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #82
        (
            "\x07\x0C#40W你就直接叫我名字，\x01",
            "别加『同学』了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #83
        (
            "\x07\x0C#40W我都一直\x01",
            "直接称呼你名字的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x0C#40W嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(2000)
    Fade(2000)
    OP_44(0x1C, 0xFF)
    OP_6D(-720, 0, 13700, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(65000, 0)
    OP_6E(280, 0)

    def lambda_2CC3():
        OP_6D(-600, 0, 3640, 20000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2CC3)

    def lambda_2CDB():
        OP_6C(25000, 20000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2CDB)
    Sleep(4000)
    SetChrName("")

    AnonymousTalk(    #85
        (
            "\x07\x0C#40W那，乔儿，\x01",
            "今天真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x0C#40W呜呜…………！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x0C#40W被你当面这么叫\x01",
            "还真是难为情……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #88
        "\x07\x0C#40W嘻嘻……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1A2E end

    def Function_13_2DBF(): pass

    label("Function_13_2DBF")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x848A, 0x0, 0xFFFF796E, 0x5DC, 0x0)
    OP_8E(0xFE, 0x8412, 0x0, 0xFFFF7FD6, 0x5DC, 0x0)
    Return()

    # Function_13_2DBF end

    def Function_14_2DEF(): pass

    label("Function_14_2DEF")

    Sleep(1000)
    OP_8E(0xFE, 0x848A, 0x0, 0xFFFF796E, 0x5DC, 0x0)
    OP_8E(0xFE, 0x83F4, 0x0, 0xFFFF7B8A, 0x5DC, 0x0)
    Return()

    # Function_14_2DEF end

    def Function_15_2E1D(): pass

    label("Function_15_2E1D")

    Sleep(1000)
    OP_8E(0xFE, 0x858E, 0x0, 0xFFFF7AE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8BD8, 0x0, 0xFFFF78C4, 0x7D0, 0x0)
    OP_8C(0x105, 45, 400)
    Return()

    # Function_15_2E1D end

    def Function_16_2E52(): pass

    label("Function_16_2E52")


    def lambda_2E58():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF8080, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E58)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    Sleep(300)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 20)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    Sleep(300)
    OP_8C(0x105, 180, 400)
    Return()

    # Function_16_2E52 end

    def Function_17_2EA7(): pass

    label("Function_17_2EA7")


    def lambda_2EAD():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0x3854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EAD)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -2990, 300, 15280, 0)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)
    LoadEffect(0x0, "map\\mp068_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -2990, 500, 15280, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x3C)
    Sleep(3000)
    LoadEffect(0x1, "map\\onsen00.eff")
    PlayEffect(0x1, 0x1, 0xFF, -3100, 1300, 15430, 0, 0, 0, 100, 200, 100, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_17_2EA7 end

    SaveToFile()

Try(main)
