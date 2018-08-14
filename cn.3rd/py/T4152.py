from ED63RDScenarioHelper import *

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
        '黑衣人',                               # 9
        '黑衣人',                               # 10
        '目标用照相机',                         # 11
        '王都格兰赛尔·北街区',                 # 12
        '王都格兰赛尔·南街区',                 # 13
        '王都格兰赛尔·码头',                   # 14
        '',                                     # 15
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
        'ED6_DT27/CH03460 ._CH',             # 02
        'ED6_DT26/CH20608 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT27/CH03460P._CP',             # 02
        'ED6_DT26/CH20608P._CP',             # 03
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 18,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_26B",          # 02, 2
        "Function_3_28F",          # 03, 3
        "Function_4_314",          # 04, 4
        "Function_5_3A1",          # 05, 5
        "Function_6_185C",         # 06, 6
        "Function_7_1878",         # 07, 7
        "Function_8_18D4",         # 08, 8
        "Function_9_1907",         # 09, 9
        "Function_10_197C",        # 0A, 10
        "Function_11_19B1",        # 0B, 11
        "Function_12_19E8",        # 0C, 12
        "Function_13_1BB0",        # 0D, 13
        "Function_14_1BF1",        # 0E, 14
        "Function_15_1C32",        # 0F, 15
        "Function_16_2060",        # 10, 16
        "Function_17_2064",        # 11, 17
        "Function_18_2068",        # 12, 18
        "Function_19_206C",        # 13, 19
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_215")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_22F")

    label("loc_215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_24B")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_24B")

    Return()

    # Function_0_1EA end

    def Function_1_24C(): pass

    label("Function_1_24C")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    OP_71(0x100C, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    Return()

    # Function_1_24C end

    def Function_2_26B(): pass

    label("Function_2_26B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28E")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_2_26B")

    label("loc_28E")

    Return()

    # Function_2_26B end

    def Function_3_28F(): pass

    label("Function_3_28F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
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
    Jump("Function_3_28F")

    label("loc_313")

    Return()

    # Function_3_28F end

    def Function_4_314(): pass

    label("Function_4_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
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
    Jump("Function_4_314")

    label("loc_3A0")

    Return()

    # Function_4_314 end

    def Function_5_3A1(): pass

    label("Function_5_3A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -78640, 1750, 14010, 180)
    SetChrPos(0x10F, -78960, 1750, 14190, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-71540, 9350, 9960, 0)
    OP_67(0, 7060, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(309000, 0)
    OP_6E(310, 0)

    def lambda_428():
        OP_6D(-74440, 8750, 4160, 5500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_428)

    def lambda_440():
        OP_67(0, 6730, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_440)

    def lambda_458():
        OP_6B(4570, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_458)

    def lambda_468():
        OP_6C(333000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_468)

    def lambda_478():
        OP_6E(303, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_478)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(-79260, 1750, 13830, 0)
    OP_67(0, 6190, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(332000, 0)
    OP_6E(323, 0)

    def lambda_4DE():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4DE)
    OP_0D()
    Sleep(500)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_72(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_73(0xC)
    OP_43(0x109, 0x0, 0x0, 0x8)
    Sleep(800)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    Sleep(1000)

    def lambda_529():
        OP_6D(-80200, 0, 1610, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_529)

    def lambda_541():
        OP_67(0, 5590, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_541)

    def lambda_559():
        OP_6B(2690, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_559)

    def lambda_569():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_569)

    def lambda_579():
        OP_6E(295, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_579)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x3)

    ChrTalk(    #0
        0x109,
        (
            "#1068F呼～……\x01",
            "比预想的多花了不少时间啊。\x02\x03",

            "没想到会被艾莉卡博士\x01",
            "逼到这种地步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1440F#5P……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1078F不过啊，最后那句话\x01",
            "可真是让我想都想不到。\x02\x03",

            "『想要把这个拿走的话，\x01",
            "  就得把这个女孩留下来\x01",
            "  作为交换条件！』……\x02\x03",

            "#1077F哈哈……\x01",
            "她又不是亚妮拉丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1444F#5P亚妮拉丝……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1078F哦，抱歉。\x01",
            "是我在利贝尔认识的一个人。\x02\x03",

            "是个当游击士的女孩，\x01",
            "和莉丝差不多是\x01",
            "一样的年纪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1446F#5P……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1062F哈哈……那个……\x01",
            "#40W………………………………\x02\x03",

            "#1068F#20W喂……莉丝？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        "#1440F#5P……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1840F难道……\x01",
            "你生气了？\x02\x03",

            "是不是因为我一直\x01",
            "都没有和你取得联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1446F#5P──格拉汉姆阁下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        "#1064F#3S是、是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1446F#5P……就如同您\x01",
            "在这五年中担任\x01",
            "守护骑士的要职一样……\x02\x03",

            "我在这五年间\x01",
            "也有了很大的变化。\x02\x03",

            "#1443F现在的我是名星杯随从骑士。\x02\x03",

            "只是为了支持您、\x01",
            "保护您而被派来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1063F………莉丝…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#5P……所以不用再做\x01",
            "不必要的担心了。\x02\x03",

            "不然的话……\x01",
            "我这样的一身着装\x01",
            "就毫无意义了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1067F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        (
            "#1448F#5P……不是要乘坐国际定期船的\x01",
            "最后一班吗？\x02\x03",

            "我们快点到\x01",
            "飞艇坪那边去吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_A88():
        OP_6D(-76280, 0, 180, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A88)

    def lambda_AA0():
        OP_67(0, 6380, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AA0)

    def lambda_AB8():
        OP_6B(2390, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AB8)

    def lambda_AC8():
        OP_6C(69000, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_AC8)

    def lambda_AD8():
        OP_6E(326, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_AD8)

    def lambda_AE8():

        label("loc_AE8")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_AE8")

    QueueWorkItem2(0x109, 0, lambda_AE8)
    OP_43(0x10F, 0x0, 0x0, 0xA)
    Sleep(300)
    Sleep(800)

    ChrTalk(    #16 op#A op#5
        0x109,
        "#1079F#6P#12A啊，喂……\x05\x02",
    )

    WaitChrThread(0x10F, 0x0)
    OP_44(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #17
        0x109,
        "#1079F#6P……刚才的是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1440F#5P………………………………\x02\x03",

            "#1446F您听错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        "#1064F#6P嘿……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 315, 400)
    Sleep(300)

    ChrTalk(    #20
        0x10F,
        (
            "#1447F#2P格拉汉姆阁下。\x01",
            "您是不是太累了？\x02\x03",

            "竟然会听到\x01",
            "一些本不存在的声音。\x02\x03",

            "#1448F上船之后还是\x01",
            "立刻坐下来休息一下──\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #21
        0x10F,
        (
            "#1800F#2P……稍微\x01",
            "休息一下为好。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x109, 0x0, 0x0, 0x7)

    ChrTalk(    #22
        0x109,
        "#1840F#6P呼……\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x0)
    OP_43(0x109, 0x0, 0x0, 0x6)
    Sleep(500)

    ChrTalk(    #23
        0x109,
        (
            "#1061F#6P#3S哈哈哈哈哈哈哈哈！\x01",
            "竟然会『咕噜噜』地叫起来！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(100)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x2)
    OP_0D()
    Sleep(200)

    ChrTalk(    #24
        0x109,
        (
            "#1066F#6P#2S你呀，一点都没变嘛！\x02\x03",

            "还是老样子，\x01",
            "总是肚子饿得咕咕叫～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10F, 0x2)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 8)
    OP_99(0x10F, 0x8, 0xC, 0x5DC)
    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_99(0x10F, 0xA, 0xC, 0x5DC)
    Sleep(500)

    ChrTalk(    #25
        0x10F,
        (
            "#1445F#2P这、这仅仅是\x01",
            "一种生理现象。\x02\x03",

            "无法对其进行控制\x01",
            "也是我修行不足的证明……\x02\x03",

            "我为此感到非常惭愧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1840F#6P修行不足……\x01",
            "哈哈，不是这样的问题吧。\x02\x03",

            "#1071F对啦～就是要这样\x01",
            "才符合莉丝的风格嘛。\x02\x03",

            "每次都偷偷溜进厨房偷吃，\x01",
            "然后被大骂一通……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x10F, 0xC, 0xD, 0x5DC)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)

    ChrTalk(    #27
        0x10F,
        "#1800F#2P……够了！\x02",
    )

    CloseMessageWindow()

    def lambda_F9E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_F9E)
    Sleep(300)

    def lambda_FB1():
        OP_6D(-74700, 0, -1800, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_FB1)

    def lambda_FC9():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_FC9)
    OP_43(0x109, 0x0, 0x0, 0xB)

    ChrTalk(    #28 op#A op#5
        0x109,
        "#1078F#2P#15A啊，等等嘛！\x05\x02",
    )

    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    OP_8F(0x10F, 0xFFFED7D4, 0x0, 0xFFFFF7CC, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x1)
    Sleep(500)

    ChrTalk(    #29
        0x10F,
        (
            "#1443F#6P……讨厌。\x01",
            "走开。\x02",
        )
    )

    Jump("loc_105C")

    label("loc_105C")

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1840F#2P对不起，我道歉。\x02\x03",

            "因为太怀念了，\x01",
            "所以才开这样的玩笑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6P……没关系。\x01",
            "没有必要为此道歉。\x02\x03",

            "你要道的歉\x01",
            "远远不止\x01",
            "这一点而已。\x02",
        )
    )

    Jump("loc_1118")

    label("loc_1118")

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1066F#2P哎呀，开始起劲了。\x02\x03",

            "我想拜托你一件事……\x01",
            "不要再那样了，好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10F,
        "#1802F#6P……哪样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1840F#2P你这种恭敬的语气。\x02\x03",

            "对其他人暂且不提，\x01",
            "这么跟我说话总觉得很不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        "#1445F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1840F#2P也不要再叫我\x01",
            "格拉汉姆阁下了。\x02\x03",

            "直接叫我名字就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        (
            "#1446F#6P如果我要说──\x01",
            "『我拒绝』呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        (
            "#1075F#2P那我就继续恳求下去。\x02\x03",

            "#1060F如果你不回答『是』的话，\x01",
            "我会一直跪在你面前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        "#1445F#6P……果然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        (
            "#1066F#2P对嘛，你也知道我的性格，\x01",
            "所谓江山易改，本性难移。\x02\x03",

            "这种孽缘，\x01",
            "可不是这么说断就断的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        (
            "#1802F#6P………………………………\x02\x03",

            "#1445F#40W……明明从……\x01",
            "…………却还…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        "#1079F#2P嗯？你说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10F,
        (
            "#1446F#6P……没什么。\x02\x03",

            "#1443F算了。\x01",
            "既然这是命令──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x109,
        (
            "#1071F#2P不不。\x01",
            "不是命令，只是请求。\x02\x03",

            "#1062F你可别把这个\x01",
            "给搞错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        (
            "#1441F#6P哼……\x02\x03",

            "#1446F#40W………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #46
        0x10F,
        (
            "#1801F#6P……凯文。\x01",
            "你还是那样任性。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x109,
        (
            "#1840F#2P……！\x02\x03",

            "#1066F哈哈……\x01",
            "对对，正是！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10F,
        (
            "#1800F#6P我把话说在前面，\x01",
            "虽然我可以改变称呼的方式……\x02\x03",

            "但你是守护骑士，\x01",
            "而我是随从骑士的关系没有改变。\x02\x03",

            "#1443F你可别把这个给搞错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1075F#2P嗯……是嘛。\x02\x03",

            "#1840F想要回到从前那种关系……\x01",
            "我想也是无法做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1445F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1075F#2P那么……\x01",
            "我还有一个提议。\x02\x03",

            "#1060F离最后一班定期船出发还有一些时间，\x01",
            "先去东街区的百货店一趟如何？\x02\x03",

            "去买一些面包之类的东西，\x01",
            "也好在船上填填肚子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        (
            "#1442F#6P……这个我赞成。\x02\x03",

            "#1447F把没卖完的食物\x01",
            "全部都买下来好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x109,
        (
            "#1068F#2P你不至于\x01",
            "饥饿到这种程度吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_182E():
        OP_6B(2000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_182E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_3A1 end

    def Function_6_185C(): pass

    label("Function_6_185C")

    OP_99(0x109, 0x3, 0x5, 0x5DC)
    OP_99(0x109, 0x3, 0x5, 0x5DC)
    OP_99(0x109, 0x3, 0x5, 0x5DC)
    Return()

    # Function_6_185C end

    def Function_7_1878(): pass

    label("Function_7_1878")

    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)

    label("loc_1887")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18D3")
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    Sleep(1500)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    Sleep(2000)
    Jump("loc_1887")

    label("loc_18D3")

    Return()

    # Function_7_1878 end

    def Function_8_18D4(): pass

    label("Function_8_18D4")


    def lambda_18DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18DA)
    OP_8E(0xFE, 0xFFFECEB0, 0x0, 0x1E0, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_18D4 end

    def Function_9_1907(): pass

    label("Function_9_1907")


    def lambda_190D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_190D)
    OP_8F(0xFE, 0xFFFECB86, 0x6D6, 0x2FB2, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(100)
    OP_6F(0xC, 59)
    OP_70(0xC, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8F(0xFE, 0xFFFEC726, 0x0, 0x19A, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_1907 end

    def Function_10_197C(): pass

    label("Function_10_197C")

    OP_8C(0xFE, 135, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFECC9E, 0x0, 0xFFFFFE48, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFED522, 0x0, 0xFFFFFC90, 0x7D0, 0x0)
    Return()

    # Function_10_197C end

    def Function_11_19B1(): pass

    label("Function_11_19B1")

    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0xFFFED40A, 0x0, 0xFFFFF54C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFEDD4C, 0x0, 0xFFFFF736, 0x1388, 0x0)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_11_19B1 end

    def Function_12_19E8(): pass

    label("Function_12_19E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    OP_6D(-74240, -3500, -14080, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(310000, 0)
    OP_6E(320, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, -73100, -3500, -15300, 0)
    SetChrPos(0x151, -72100, -3500, -15300, 0)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    SetChrPos(0x10, -57040, -3500, -17320, 270)
    SetChrPos(0x11, -73800, -3500, -23360, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1AAD():
        OP_8E(0xFE, 0xFFFEF1B0, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AAD)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0xD)
    Sleep(2000)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    def lambda_1B3A():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1B3A)
    Sleep(100)

    def lambda_1B4D():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1B4D)
    Sleep(100)

    def lambda_1B60():
        OP_8E(0xFE, 0xFFFF2CE8, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1B60)
    Sleep(100)
    OP_43(0x11, 0x3, 0x0, 0xE)
    Sleep(3000)

    def lambda_1B8C():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1B8C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4143   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_19E8 end

    def Function_13_1BB0(): pass

    label("Function_13_1BB0")


    def lambda_1BB6():
        OP_8E(0xFE, 0xFFFEDFB8, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BB6)
    WaitChrThread(0x11, 0x1)

    def lambda_1BD6():
        OP_8E(0xFE, 0xFFFEEC10, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BD6)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_13_1BB0 end

    def Function_14_1BF1(): pass

    label("Function_14_1BF1")


    def lambda_1BF7():
        OP_8E(0xFE, 0xFFFEDFB8, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BF7)
    WaitChrThread(0x11, 0x1)

    def lambda_1C17():
        OP_8E(0xFE, 0xFFFEDFB8, 0xFFFFF254, 0xFFFFA4C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C17)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_14_1BF1 end

    def Function_15_1C32(): pass

    label("Function_15_1C32")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x151, 0x8)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -54500, 0, -5600, 270)
    SetChrPos(0x11, -89160, 0, -2500, 90)
    OP_6D(-74700, -3500, -10220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(640, 0)

    def lambda_1CC3():
        OP_8E(0xFE, 0xFFFEA1EC, 0x0, 0xFFFFEA20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1CC3)

    def lambda_1CDE():
        OP_6D(-76600, -4500, -8320, 21000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1CDE)

    def lambda_1CF6():
        OP_67(0, 6500, -10000, 21000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1CF6)
    FadeToBright(3000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #54
        (
            "\x07\x00自从那些人住在\x01",
            "我和祖父生活的家里……\x02\x03",

            "就不断发生有人被从楼上推下去了，\x01",
            "或者食物里面有奇怪的药味之类的事情……\x02",
        )
    )

    Jump("loc_1DA8")

    label("loc_1DA8")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #55
        "\x07\x00真的是各种各样的事…………\x02",
    )

    Jump("loc_1DDD")

    label("loc_1DDD")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #56
        (
            "\x07\x00虽然我是法定的亲戚，\x01",
            "但还尚未成年……\x02",
        )
    )

    Jump("loc_1E1D")

    label("loc_1E1D")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #57
        (
            "\x07\x00……开始还勉强和他们能谈谈，\x01",
            "后来就不得不离开家了。\x02\x03",

            "在谁也找不到的街道上\x01",
            "四处徘徊着。\x02",
        )
    )

    Jump("loc_1E95")

    label("loc_1E95")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #58
        (
            "\x07\x00……可是，如果这样下去，\x01",
            "他们就会以下落不明为由说我已经死亡。\x02",
        )
    )

    Jump("loc_1EED")

    label("loc_1EED")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #59
        (
            "\x07\x00而且就算我回到家里，\x01",
            "也会被监禁在某个地方\x01",
            "然后被申报为下落不明。\x02",
        )
    )

    Jump("loc_1F48")

    label("loc_1F48")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #60
        (
            "\x07\x00然后遗书就会因此被算作无效，\x01",
            "那些亲戚就可以分割遗产了。\x02",
        )
    )

    Jump("loc_1F9A")

    label("loc_1F9A")

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_1FA3():
        OP_8E(0xFE, 0xFFFF3E2C, 0x0, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FA3)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #61
        (
            "\x07\x00……我不愿就这样不明不白。\x02\x03",

            "所以我回到了王都。\x02",
        )
    )

    Jump("loc_200A")

    label("loc_200A")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("爱娜")

    AnonymousTalk(    #62
        "\x07\x00我一定要正式继承遗产。\x02",
    )

    Jump("loc_203B")

    label("loc_203B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4143   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1C32 end

    def Function_16_2060(): pass

    label("Function_16_2060")

    SetPlaceName(0xB8)
    Return()

    # Function_16_2060 end

    def Function_17_2064(): pass

    label("Function_17_2064")

    SetPlaceName(0xB7)
    Return()

    # Function_17_2064 end

    def Function_18_2068(): pass

    label("Function_18_2068")

    SetPlaceName(0xAF)
    Return()

    # Function_18_2068 end

    def Function_19_206C(): pass

    label("Function_19_206C")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #63
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_206C end

    SaveToFile()

Try(main)
