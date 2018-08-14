from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4404   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4404.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '异形的男人',                           # 9
        '基尔巴特',                             # 10
        'Ｇ－阿帕奇',                           # 11
        '来福枪',                               # 12
        '',                                     # 13
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
        'ED6_DT07/CH02420 ._CH',             # 00
        'ED6_DT27/CH03750 ._CH',             # 01
        'ED6_DT27/CH04750 ._CH',             # 02
        'ED6_DT27/CH04751 ._CH',             # 03
        'ED6_DT27/CH04753 ._CH',             # 04
        'ED6_DT26/CH20632 ._CH',             # 05
        'ED6_DT26/CH20501 ._CH',             # 06
        'ED6_DT27/CH04150 ._CH',             # 07
        'ED6_DT27/CH04151 ._CH',             # 08
        'ED6_DT27/CH04152 ._CH',             # 09
        'ED6_DT27/CH04153 ._CH',             # 0A
        'ED6_DT27/CH04154 ._CH',             # 0B
        'ED6_DT26/CH20611 ._CH',             # 0C
        'ED6_DT26/CH20451 ._CH',             # 0D
        'ED6_DT29/CH14970 ._CH',             # 0E
        'ED6_DT27/CH04080 ._CH',             # 0F
        'ED6_DT26/CH20622 ._CH',             # 10
        'ED6_DT27/CH03440 ._CH',             # 11
        'ED6_DT26/CH20617 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02420P._CP',             # 00
        'ED6_DT27/CH03750P._CP',             # 01
        'ED6_DT27/CH04750P._CP',             # 02
        'ED6_DT27/CH04751P._CP',             # 03
        'ED6_DT27/CH04753P._CP',             # 04
        'ED6_DT26/CH20632P._CP',             # 05
        'ED6_DT26/CH20501P._CP',             # 06
        'ED6_DT27/CH04150P._CP',             # 07
        'ED6_DT27/CH04151P._CP',             # 08
        'ED6_DT27/CH04152P._CP',             # 09
        'ED6_DT27/CH04153P._CP',             # 0A
        'ED6_DT27/CH04154P._CP',             # 0B
        'ED6_DT26/CH20611P._CP',             # 0C
        'ED6_DT26/CH20451P._CP',             # 0D
        'ED6_DT29/CH14970P._CP',             # 0E
        'ED6_DT27/CH04080P._CP',             # 0F
        'ED6_DT26/CH20622P._CP',             # 10
        'ED6_DT27/CH03440P._CP',             # 11
        'ED6_DT26/CH20617P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x185,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_1FE",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_1918",         # 03, 3
        "Function_4_1BAC",         # 04, 4
        "Function_5_1BFB",         # 05, 5
        "Function_6_1C96",         # 06, 6
        "Function_7_1CDC",         # 07, 7
        "Function_8_1D19",         # 08, 8
        "Function_9_2D8C",         # 09, 9
        "Function_10_2DE5",        # 0A, 10
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1E1")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_1FD")

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1FD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1FD")

    Return()

    # Function_0_1C2 end

    def Function_1_1FE(): pass

    label("Function_1_1FE")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_1FE end

    def Function_2_204(): pass

    label("Function_2_204")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "battle\\damage0.eff")
    LoadEffect(0x1, "map\\mpsibuk.eff")
    LoadEffect(0x2, "map\\mp255_00.eff")
    SetChrPos(0x109, 3620, 0, 66530, 0)
    SetChrPos(0x10F, 3620, 0, 66530, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-78990, 1750, 13960, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(332000, 0)
    OP_6D(1820, 0, -960, 0)
    OP_67(0, 10300, -10000, 0)
    OP_6B(3580, 0)
    OP_6C(45000, 0)
    OP_6E(506, 0)

    def lambda_2F9():
        OP_6D(430, 0, 28700, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2F9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_6D(300, 0, 25910, 0)
    OP_67(0, 8340, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(371, 0)
    OP_0D()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -90, 0, 13540, 0)

    def lambda_379():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0x6234, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_379)
    WaitChrThread(0x11, 0x0)
    Sleep(200)
    OP_8C(0x11, 270, 600)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x11, 0, 800)
    OP_8C(0x11, 90, 800)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3E1():
        OP_8E(0xFE, 0x3912, 0x0, 0x62F2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3E1)
    WaitChrThread(0x11, 0x0)
    Fade(1000)
    SetChrPos(0x11, 6940, 0, 73790, 90)

    def lambda_417():
        OP_8E(0xFE, 0x53B6, 0x0, 0x124A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_417)
    OP_6D(20900, 0, 74140, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2750, 0)
    OP_6B(3380, 0)
    OP_6C(224000, 0)
    OP_6E(298, 0)

    def lambda_478():
        OP_6B(2750, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_478)
    WaitChrThread(0x11, 0x0)
    Sleep(200)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x11, 135, 600)
    Sleep(500)
    OP_8C(0x11, 45, 600)
    Sleep(300)
    OP_8C(0x11, 90, 600)
    Sleep(500)

    ChrTalk(    #0
        0x11,
        (
            "#674F#5P哼……\x01",
            "到哪里去了……！？\x02\x03",

            "我明明看到他们\x01",
            "往这边跑了啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x109, 9080, 0, 74240, 90)
    SetChrPos(0x10F, 8830, 0, 75680, 90)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    NpcTalk(    #1
        0x109,
        "凯文的声音",
        (
            "#3P怎么……\x01",
            "原来是这位小哥啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x11,
        "#672F#5P什……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)

    def lambda_5C8():
        OP_6D(18500, 0, 73760, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_5C8)

    def lambda_5E0():
        OP_67(0, 5180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5E0)

    def lambda_5F8():
        OP_6B(2930, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5F8)

    def lambda_608():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_608)

    def lambda_618():
        OP_6E(295, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_618)

    def lambda_628():
        OP_8E(0xFE, 0x4038, 0x0, 0x12200, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_628)
    Sleep(500)

    def lambda_648():
        OP_8E(0xFE, 0x3F6F, 0x0, 0x127A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_648)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_67A():
        OP_8F(0xFE, 0x5960, 0x0, 0x12480, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_67A)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #3
        0x11,
        (
            "#676F不、不可能……\x02\x03",

            "我完美的跟踪术\x01",
            "竟然会被别人发现！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1840F#5P完美……\x01",
            "哈哈，你还真是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1443F……他是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1075F#5P算是『蛇』的爪牙吧。\x02\x03",

            "#1060F不过说到底也只是\x01",
            "他们无数尾巴中的小小杂鱼而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        "#1446F……看起来的确是这样呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #8
        0x11,
        (
            "#674F竟敢说我是杂鱼！\x02\x03",

            "还有那边的小丫头！\x02\x03",

            "『的确是这样』\x01",
            "是什么意思啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        (
            "#1805F#40W………………………………#20W\x02\x03",

            "#1447F……不管怎么看，\x01",
            "都是杂鱼啊。\x02\x03",

            "气势汹汹却总做无用功，\x01",
            "到头来只能自取灭亡……\x02\x03",

            "#1448F而且还不接受教训。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x11,
        "#676F什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1066F#5P唉，你还是这么敏锐啊。\x02\x03",

            "明明是第一次见面，\x01",
            "却把对方都看透了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1446F这个人的性情\x01",
            "实在太容易辨别了……\x02\x03",

            "从骨子里透出一股\x01",
            "小人的气息呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #13
        0x11,
        (
            "#674F你……\x02\x03",

            "#673F……哼哼哼，好吧。\x02\x03",

            "#675F既然你这么说了，\x01",
            "那就做好觉悟吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(20700, 0, 73950, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(135000, 0)
    OP_6E(305, 0)
    OP_0D()
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0x11, 90, 2000)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 0, 2000)
    OP_8C(0x11, 270, 2000)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1063F哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15 op#A op#5
        0x10F,
        "#1441F#6P#8A……………………\x05\x02",
    )

    Fade(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(800)

    def lambda_B7D():
        OP_6D(22470, 0, 73750, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B7D)

    def lambda_B95():
        OP_6B(2400, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B95)
    OP_43(0x10F, 0x0, 0x0, 0x3)
    Sleep(2000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x10F, 0x0)

    def lambda_BD2():
        OP_6D(20800, 0, 73500, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_BD2)

    def lambda_BEA():
        OP_67(0, 4950, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BEA)

    def lambda_C02():
        OP_6B(2910, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C02)

    def lambda_C12():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_C12)

    def lambda_C22():
        OP_6E(298, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C22)
    WaitChrThread(0x13, 0x0)
    Sleep(300)

    ChrTalk(    #16
        0x109,
        (
            "#1065F#4P『法剑』……\x02\x03",

            "#1067F……那是你擅长的武器吗。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    def lambda_C9F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C9F)
    Sleep(700)

    ChrTalk(    #17
        0x10F,
        (
            "#1445F#5P……就和凯文选择弩枪一样，\x01",
            "我也选择了与自己\x01",
            "相应的武器。\x02\x03",

            "#1806F只是这样而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1840F#4P……是吗………\x02\x03",

            "#1065F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_D6F():
        OP_6D(24720, 0, 73600, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_D6F)

    def lambda_D87():
        OP_67(0, 5560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D87)

    def lambda_D9F():
        OP_6B(2680, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_D9F)

    def lambda_DAF():
        OP_6C(135000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_DAF)

    def lambda_DBF():
        OP_6E(307, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_DBF)

    def lambda_DCF():
        OP_8E(0xFE, 0x58C0, 0x0, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DCF)
    Sleep(1000)
    OP_8C(0x10F, 90, 400)
    WaitChrThread(0x10, 0x0)
    OP_44(0x11, 0x1)
    Sleep(500)
    Fade(250)
    SetChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 25400, 0, 74910, 270)
    OP_0D()
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #19
        0x11,
        "#1224F#5P怎、怎么可能……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #20
        0x11,
        (
            "#1224F#5P刚、刚才那是什么……\x01",
            "我怎么什么都没看清楚……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x109,
        (
            "#1075F#4P『法剑』……\x01",
            "#1060F是星杯骑士团流传的武器呢。\x02\x03",

            "它的刀刃可分为若干节，\x01",
            "中间用铁链加以连接，\x01",
            "因此能够伸缩自如。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "#1222F#5P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1065F#4P那么，\x01",
            "是不是该告诉我们了。\x02\x03",

            "#1063F为什么被指名通缉的你\x01",
            "会出现在格兰赛尔呢？\x02\x03",

            "──你对这边的情况\x01",
            "了解多少？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#1220F#5P哼、哼……\x01",
            "谁会告诉你这些——\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1026():
        OP_8E(0xFE, 0x57E4, 0x0, 0x124F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1026)

    def lambda_1041():
        OP_6D(25720, 0, 73600, 900)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1041)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #25
        0x11,
        "#1224F#5P哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        (
            "#1801F#6P……真是死鸭子嘴硬啊。\x02\x03",

            "还不赶快交代。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1066F#4P对了对了，我的同伴\x01",
            "一旦肚子饿了心情就会很糟糕。\x02\x03",

            "劝你还是老老实实说吧，\x01",
            "以免再遭罪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#1224F#5P呜……呜呜呜……\x02\x03",

            "#1225F──既然这样的话！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)

    def lambda_11B1():
        OP_6D(25800, 0, 73600, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11B1)

    def lambda_11C9():
        OP_6B(2500, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11C9)

    def lambda_11D9():
        OP_96(0xFE, 0x6662, 0x0, 0x124D0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_11D9)
    SetChrChipByIndex(0x11, 13)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_43(0x11, 0x0, 0x0, 0x6)

    ChrTalk(    #29
        0x11,
        (
            "#1227F#5P请饶了我吧！\x02\x03",

            "我今天真是倒大霉了，\x01",
            "不小心迫降到这种地方！\x02\x03",

            "然后偶然发现了你们，\x01",
            "只不过是跟着过来而已！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x11, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x7)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x10F,
        (
            "#1446F#6P……订正。\x02\x03",

            "#1440F从某种意义上来说，\x01",
            "他也不是个普通人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1068F#4P我同意……\x02\x03",

            "#1063F……那么，\x01",
            "到底是怎么回事？\x02\x03",

            "既然说是迫降，\x01",
            "也就是说这附近有\x01",
            "『结社』的飞艇咯？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0x0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #32
        0x11,
        (
            "#1224F#5P不、不是的！\x02\x03",

            "我说的『迫降』\x01",
            "指的不是飞艇──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    PlayEffect(0x2, 0x0, 0xFF, 32130, -2000, 74350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xE3, 0x0, 0x64)
    OP_22(0x10B, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_20(0x7D0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x109, 20630, 0, 74330, 90)
    SetChrPos(0x10F, 20030, 0, 75290, 90)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x800)

    def lambda_1515():
        OP_96(0xFE, 0x6590, 0x0, 0x12430, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1515)
    OP_22(0xA3, 0x0, 0x64)
    OP_6D(26900, 0, 74700, 0)
    OP_67(0, 3600, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(90000, 0)
    OP_6E(350, 0)

    def lambda_1575():
        OP_6B(2620, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1575)
    OP_0D()

    ChrTalk(    #33 op#A op#5
        0x11,
        "#1221F#25A#3S#5P──而是这个！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(1300)
    Fade(500)
    OP_1D(0x97)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_15DC():
        OP_6D(24630, 1000, 74700, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15DC)

    def lambda_15F4():
        OP_67(0, 2860, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15F4)

    def lambda_160C():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_160C)
    OP_23(0xE3)
    OP_23(0x10B)
    OP_22(0xDC, 0x0, 0x64)
    OP_22(0x5C, 0x0, 0x64)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 33130, -2000, 74500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32130, -5000, 74700, 270)

    def lambda_1684():

        label("loc_1684")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1684")

    QueueWorkItem2(0x12, 3, lambda_1684)

    def lambda_1697():
        OP_8F(0xFE, 0x7D82, 0x578, 0x123CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1697)

    def lambda_16B2():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_16B2)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)

    def lambda_16E1():
        OP_96(0xFE, 0x4704, 0x0, 0x126EC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_16E1)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)

    def lambda_1713():
        OP_96(0xFE, 0x4ABA, 0x0, 0x12110, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1713)
    WaitChrThread(0x10F, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #34
        0x109,
        "#1069F#12P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        "#1449F#6P人形兵器……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 600)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_179D():
        OP_96(0xFE, 0x5C6C, 0x0, 0x11D50, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_179D)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x11, 0x0)

    def lambda_17CF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_17CF)
    Sleep(300)
    SetChrFlags(0x13, 0x80)
    OP_8C(0x11, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)

    def lambda_1801():
        OP_96(0xFE, 0x65EA, 0x0, 0x123CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1801)
    WaitChrThread(0x11, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #36
        0x11,
        "#1221F#5P#3S哇哈哈，形势逆转了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #37
        0x11,
        (
            "#1226F#5P快！\x01",
            "『Ｇ－阿帕奇』啊！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #38
        0x11,
        (
            "#1225F#5P#3S用你那强大的力量\x01",
            "把这些家伙打得满地找牙吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 8)
    Return()

    # Function_2_204 end

    def Function_3_1918(): pass

    label("Function_3_1918")

    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_1930():
        OP_8E(0xFE, 0x4A10, 0x0, 0x12660, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1930)
    Sleep(50)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    WaitChrThread(0xFE, 0x1)

    def lambda_195F():
        OP_96(0xFE, 0x51C2, 0x0, 0x124D0, 0x4B0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_195F)
    Sleep(100)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)

    def lambda_1A3C():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A3C)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)

    def lambda_1A5B():
        OP_7C(0x64, 0x0, 0x1388, 0xC8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A5B)
    PlayEffect(0x0, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x11, 0x0, 0x0, 0x5)
    Sleep(100)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 3)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_3_1918 end

    def Function_4_1BAC(): pass

    label("Function_4_1BAC")

    SetChrFlags(0x13, 0x800)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 22880, 0, 74880, 0)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1BD8():
        OP_96(0xFE, 0x5CD0, 0x0, 0x11AE4, 0xBB8, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1BD8)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA, 0x0, 0x64)
    Return()

    # Function_4_1BAC end

    def Function_5_1BFB(): pass

    label("Function_5_1BFB")


    ChrTalk(    #39 op#A op#5
        0x11,
        "#1227F#5P#20A哇！\x05\x02",
    )

    OP_43(0x13, 0x0, 0x0, 0x4)
    OP_22(0x50, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)

    def lambda_1C35():
        OP_96(0xFE, 0x5F0A, 0x0, 0x124B2, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C35)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 0)

    def lambda_1C6C():
        OP_96(0xFE, 0x61A8, 0x0, 0x1249E, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C6C)
    WaitChrThread(0xFE, 0x1)
    Sleep(1000)
    OP_43(0xFE, 0x1, 0x0, 0x7)
    Return()

    # Function_5_1BFB end

    def Function_6_1C96(): pass

    label("Function_6_1C96")

    OP_22(0x218, 0x0, 0x64)
    OP_99(0x11, 0x0, 0x6, 0x5DC)
    Sleep(1000)

    label("loc_1CA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CDB")
    OP_99(0x11, 0x6, 0x2, 0x5DC)
    OP_22(0x218, 0x0, 0x64)
    OP_99(0x11, 0x2, 0x6, 0x5DC)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CD8")
    Jump("loc_1CDB")

    label("loc_1CD8")

    Jump("loc_1CA9")

    label("loc_1CDB")

    Return()

    # Function_6_1C96 end

    def Function_7_1CDC(): pass

    label("Function_7_1CDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D18")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_7_1CDC")

    label("loc_1D18")

    Return()

    # Function_7_1CDC end

    def Function_8_1D19(): pass

    label("Function_8_1D19")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    ClearChrFlags(0x109, 0x80)
    SetChrPos(0x109, 20950, 0, 74370, 90)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x10F, 0x80)
    SetChrPos(0x10F, 20920, 0, 76000, 90)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 25400, 0, 74870, 270)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 25000, -300, 74870, 270)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32130, 1500, 74350, 270)

    def lambda_1DDA():

        label("loc_1DDA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1DDA")

    QueueWorkItem2(0x12, 3, lambda_1DDA)

    def lambda_1DED():

        label("loc_1DED")

        OP_9E(0xFE, 0xA, 0xA, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1DED")

    QueueWorkItem2(0x12, 2, lambda_1DED)
    OP_6D(30350, 1150, 74660, 0)
    OP_67(0, 5330, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(122000, 0)
    OP_6E(445, 0)
    LoadEffect(0x1, "map\\mpsibuk.eff")
    LoadEffect(0x2, "monster\\ms30109a.eff")
    LoadEffect(0x3, "map\\mpsmk0.eff")
    LoadEffect(0x4, "map\\mp252_01.eff")
    LoadEffect(0x5, "map\\mp252_05.eff")
    OP_22(0x143, 0x0, 0x64)
    PlayEffect(0x2, 0x0, 0x12, 0, 0, 0, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_23(0x143)

    def lambda_1F27():
        OP_6B(1600, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1F27)

    def lambda_1F37():
        OP_8F(0xFE, 0x7D82, 0xFFFFC568, 0x1226E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1F37)
    Sleep(1500)
    OP_22(0xDC, 0x0, 0x64)

    def lambda_1F5C():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1F5C)
    PlayEffect(0x1, 0x2, 0xFF, 32130, -1500, 74750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    ChrTalk(    #40
        0x11,
        "#1224F#5P#3S怎、怎么可能！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x2)
    Sleep(300)

    def lambda_1FEA():
        OP_6D(24460, 0, 73600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FEA)

    def lambda_2002():
        OP_67(0, 4910, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2002)

    def lambda_201A():
        OP_6B(2150, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_201A)

    def lambda_202A():
        OP_6C(122000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_202A)

    def lambda_203A():
        OP_6E(421, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_203A)
    Sleep(1000)
    SetChrSubChip(0x11, 1)
    Sleep(300)
    WaitChrThread(0x109, 0x0)
    SetChrFlags(0x12, 0x80)

    ChrTalk(    #41
        0x11,
        (
            "#1225F#5P你、你们……\x01",
            "竟然把我珍贵的专用机体给！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1065F没想到你还隐藏着\x01",
            "这么一手……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #43
        0x109,
        (
            "#1060F#11P话说回来，莉丝。\x01",
            "你的身手不错嘛？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #44
        0x10F,
        (
            "#1446F#6P只是修行之身而已。\x02\x03",

            "#1445F………还远远及不上\x01",
            "姐姐。\x02",
        )
    )

    Jump("loc_21B0")

    label("loc_21B0")

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1840F#11P…………是吗……………\x02\x03",

            "#1075F哈哈……\x01",
            "这么说我不也一样吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10F,
        (
            "#1802F#6P………………………………\x02\x03",

            "#1445F……凯文……那个………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        "#1067F#11P接下来──\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    def lambda_2290():
        OP_8E(0xFE, 0x59BA, 0x0, 0x124A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2290)
    Sleep(300)
    Fade(500)
    OP_6D(22650, 0, 73560, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(224000, 0)
    OP_6E(421, 0)
    OP_8C(0x10F, 90, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0x109,
        (
            "#1060F#5P看来你的牌也出光了，\x01",
            "那我们就来个了断吧。\x02\x03",

            "如果你老老实实的话，\x01",
            "我可以网开一面，\x01",
            "就把你交给士兵吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10F,
        "#1802F#2P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #50
        0x11,
        (
            "#1222F#6P你、你打算把我\x01",
            "交给王国军队吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1075F#5P如果你愿意的话，\x01",
            "我还可以把你一起带回\x01",
            "亚尔特利亚法典国。\x02\x03",

            "#1073F──不过在那种情况下，\x01",
            "你的小命可就得不到保障了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(300)

    ChrTalk(    #52
        0x11,
        "#1224F#6P哇……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_20(0x7D0)
    OP_22(0x15F, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x109,
        "#1063F#5P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1443F#2P又、又来了……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_C4(0x1, 0x400)
    OP_0D()
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x11,
        (
            "#1224F#6P那……\x01",
            "……刚才那是什么……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 1)
    Sleep(800)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x4, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)

    ChrTalk(    #56
        0x109,
        (
            "#1067F#5P又是这东西……\x01",
            "它到底是什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        "#1802F#2P好像对什么起了反应……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #58
        0x11,
        (
            "#1224F#6P那、那是什么……\x01",
            "你们到底想干什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x109,
        (
            "#1068F#5P啊，这和小哥你没有关系，\x01",
            "保持沉默就可以了。\x02\x03",

            "#1067F可是……\x01",
            "从刚才开始到底──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男子的声音")

    AnonymousTalk(    #60
        "\x07\x05呵呵……开始了吗。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xB0)
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    SetChrPos(0x10, 17660, 6700, 68260, 0)
    SetChrChipByIndex(0x10, 18)
    SetChrSubChip(0x10, 10)

    def lambda_27FA():
        OP_6D(19500, 6050, 66800, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_27FA)

    def lambda_2812():
        OP_67(0, 4850, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2812)

    def lambda_282A():
        OP_6B(3020, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_282A)

    def lambda_283A():
        OP_6C(143000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_283A)

    def lambda_284A():
        OP_6E(300, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_284A)
    Sleep(2000)
    OP_99(0x10, 0xA, 0xC, 0x5DC)
    SetChrSubChip(0x10, 6)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #61
        0x11,
        "#1224F#2P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x109,
        "#1069F#2P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10F,
        "#1441F#2P……什么时候……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #64
        0x10,
        (
            "\x07\x05#1591F#5P久违了。\x01",
            "凯文·格拉汉姆──\x02\x03",

            "背负着深重罪孽的『圣痕』，\x01",
            "在看不见方向的黑暗中徘徊赎罪的人啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x109,
        (
            "#1079F#2P！？\x02\x03",

            "#1063F你、你到底是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrPos(0x109, 22930, 0, 74580, 0)
    SetChrPos(0x10F, 21140, 0, 75820, 180)
    SetChrPos(0x11, 26360, 0, 75020, 180)
    SetChrPos(0x13, 26360, -200, 74420, 270)
    PlayEffect(0x4, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x109, 180, 0)
    Fade(500)
    OP_6D(21190, 4180, 72060, 0)
    OP_67(0, 6950, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(327000, 0)
    OP_6E(344, 0)
    OP_0D()
    SetChrFlags(0x10, 0x2)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)

    def lambda_2A90():
        OP_6D(21820, 0, 75340, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2A90)
    WaitChrThread(0xEE, 0x0)
    PlayEffect(0x4, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x147, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 135, 400)
    Sleep(300)
    PlayEffect(0x5, 0x2, 0xFF, 22490, 1000, 74230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToDark(14000, 16777215, -1)

    def lambda_2B8B():
        OP_6B(4500, 16000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2B8B)
    OP_43(0x11, 0x0, 0x0, 0xA)
    Sleep(1000)

    ChrTalk(    #66 op#A op#5
        0x11,
        "#1227F#5P#22A哇哇……！？\x05\x02",
    )

    Sleep(1540)

    ChrTalk(    #67 op#A op#5
        0x109,
        "#1070F#5P#10A呜……！？\x05\x02",
    )

    Sleep(1300)

    ChrTalk(    #68 op#A op#5
        0x10F,
        "#1449F#5P#10A……凯文……！\x05\x02",
    )

    Sleep(1800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("异形的男人")

    AnonymousTalk(    #69 op#A op#5
        (
            "\x07\x05#1591F#4P#48A『王』已复活，\x01",
            "昏暗的炼狱之门即将开启……\x05\x02",
        )
    )

    Sleep(4800)
    OP_56(0x0)
    Sleep(500)
    OP_44(0x11, 0x0)
    SetChrName("异形的男人")

    AnonymousTalk(    #70 op#A op#5
        (
            "\x07\x05#1591F#4P#46A来吧！\x01",
            "各位供品！迷茫的人们啊！\x05\x02",
        )
    )

    Sleep(4600)
    OP_56(0x0)
    Sleep(500)
    SetChrName("异形的男人")

    AnonymousTalk(    #71 op#A op#5
        (
            "\x07\x05#1591F#4P#48A在无尽的永劫火焰中\x01",
            "燃烧殆尽吧！\x07\x00\x05\x02",
        )
    )

    Sleep(4800)
    OP_56(0x0)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    OP_0D()
    OP_44(0x109, 0x2)
    Sleep(1000)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_6D(0, -100000, 0, 0)
    OP_20(0x1388)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_21()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7004   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_1D19 end

    def Function_9_2D8C(): pass

    label("Function_9_2D8C")

    OP_24(0xC9, 0x5A)
    Sleep(250)
    OP_24(0xC9, 0x50)
    Sleep(250)
    OP_24(0xC9, 0x46)
    Sleep(250)
    OP_24(0xC9, 0x3C)
    Sleep(250)
    OP_24(0xC9, 0x32)
    Sleep(250)
    OP_24(0xC9, 0x28)
    Sleep(250)
    OP_24(0xC9, 0x1E)
    Sleep(250)
    OP_24(0xC9, 0x14)
    Sleep(250)
    OP_24(0xC9, 0xA)
    Sleep(250)
    OP_24(0xC9, 0x0)
    OP_23(0xC9)
    Return()

    # Function_9_2D8C end

    def Function_10_2DE5(): pass

    label("Function_10_2DE5")

    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    Return()

    # Function_10_2DE5 end

    SaveToFile()

Try(main)
