from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2110   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '米拉诺',                               # 9
        '秘书凯诺娜',                           # 10
        '诺曼市长',                             # 11
        '资料１',                               # 12
        '资料２',                               # 13
        '资料２',                               # 14
        '信',                                   # 15
        '目标用照相机',                         # 16
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
        'ED6_DT07/CH01230 ._CH',             # 00
        'ED6_DT26/CH20797 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01233 ._CH',             # 03
        'ED6_DT26/CH20679 ._CH',             # 04
        'ED6_DT06/CH20021 ._CH',             # 05
        'ED6_DT26/CH20798 ._CH',             # 06
        'ED6_DT26/CH20278 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01230P._CP',             # 00
        'ED6_DT26/CH20797P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01233P._CP',             # 03
        'ED6_DT26/CH20679P._CP',             # 04
        'ED6_DT06/CH20021P._CP',             # 05
        'ED6_DT26/CH20798P._CP',             # 06
        'ED6_DT26/CH20278P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1F6,
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
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1F6,
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
        Unknown3            = 131079,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1F6,
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
        Unknown3            = 1114117,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1F6,
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
        "Function_0_1EA",          # 00, 0
        "Function_1_24E",          # 01, 1
        "Function_2_27A",          # 02, 2
        "Function_3_290",          # 03, 3
        "Function_4_2B4",          # 04, 4
        "Function_5_2D8",          # 05, 5
        "Function_6_1550",         # 06, 6
        "Function_7_15B1",         # 07, 7
        "Function_8_15F2",         # 08, 8
        "Function_9_165A",         # 09, 9
        "Function_10_16A2",        # 0A, 10
        "Function_11_170A",        # 0B, 11
        "Function_12_1737",        # 0C, 12
        "Function_13_17C5",        # 0D, 13
        "Function_14_1813",        # 0E, 14
        "Function_15_1879",        # 0F, 15
        "Function_16_1DB5",        # 10, 16
        "Function_17_1E0E",        # 11, 17
        "Function_18_1E45",        # 12, 18
        "Function_19_2856",        # 13, 19
        "Function_20_28E3",        # 14, 20
        "Function_21_29DD",        # 15, 21
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_218")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_24D")

    label("loc_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_23A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_24D")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_24D")

    Return()

    # Function_0_1EA end

    def Function_1_24E(): pass

    label("Function_1_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_270")
    OP_A3(0x0)
    OP_B1("T2110_1")
    Jump("loc_279")

    label("loc_270")

    OP_B1("T2110_0")

    label("loc_279")

    Return()

    # Function_1_24E end

    def Function_2_27A(): pass

    label("Function_2_27A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_27A")

    label("loc_28F")

    Return()

    # Function_2_27A end

    def Function_3_290(): pass

    label("Function_3_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_8D(0xFE, -6630, 65280, -3270, 67330, 1000)
    Jump("Function_3_290")

    label("loc_2B3")

    Return()

    # Function_3_290 end

    def Function_4_2B4(): pass

    label("Function_4_2B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_8D(0xFE, -2620, 970, 1167, -2110, 3000)
    Jump("Function_4_2B4")

    label("loc_2D7")

    Return()

    # Function_4_2B4 end

    def Function_5_2D8(): pass

    label("Function_5_2D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-34700, 0, 70780, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(328000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -26820, 140, 63060, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -25760, 0, 68260, 180)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, -26680, 200, 66900, 180)
    SetChrChipByIndex(0x10C, 4)
    SetChrSubChip(0x10C, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -27060, 540, 64580, 0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_3AA():
        OP_6D(-28500, 0, 67500, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3AA)

    def lambda_3C2():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #0
        0x10,
        (
            "#6P原来如此啊，\x01",
            "是这样吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#6P竟然把销售渠道\x01",
            "弄得那样清楚明了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#6P这下很快就能打入帝都市场了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x10C,
        "理查德所长",
        (
            "#11P#1850F因为您委托的内容是\x01",
            "查明帝国导力器的\x01",
            "交易现状……\x02\x03",

            "就以当地的专卖店\x01",
            "为中心展开了调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "#6P嗯，收集得非常齐全呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#6P话虽如此……\x01",
            "问题在于利贝尔的货源啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#6P国际定期航班\x01",
            "被博尔德那大叔所控制……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10C,
        "理查德所长",
        (
            "#11P#1855F是啊，\x01",
            "国际定期航班载货量的４０％\x01",
            "都是博尔德家的优先合约。\x02\x03",

            "#1850F不过，最近除了定期航班以外\x01",
            "也有个体运输业者……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x10C, 1)
    Sleep(400)
    OP_8C(0x11, 0, 400)

    def lambda_62D():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x10C5C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_62D)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)
    OP_8C(0x11, 135, 400)

    def lambda_659():
        OP_8E(0xFE, 0xFFFF9EBC, 0x0, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_659)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x10C, 0)

    def lambda_67E():
        OP_8E(0xFE, 0xFFFF9EBC, 0x0, 0xFC1C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_67E)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 225, 400)
    Sleep(300)

    ChrTalk(    #8
        0x11,
        (
            "#1862F呵呵，\x01",
            "这个是附加资料呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x12, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x15, 0x800)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -26220, -50, 64450, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #9
        0x10,
        "#6P哦，准备得很充分嘛。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x10C,
        "理查德所长",
        (
            "#11P#1851F哈哈，\x01",
            "因为这次的调查时间延长了一点。\x02\x03",

            "这算是那部分的附赠。\x01",
            "请一起拿去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#6P你还是那么有先见之明啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#6P怎么样，要不要跳槽来我们这里？\x01",
            "薪水很高哦～！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x10C,
        "理查德所长",
        (
            "#11P#1850F承蒙米拉诺小姐\x01",
            "如此夸奖……\x02\x03",

            "#1859F但是，\x01",
            "我想唯利是图的商业世界\x01",
            "并不适合我。\x02\x03",

            "因为我生性谨慎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#6P啊哈哈，你真会开玩笑。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#6P也罢。\x01",
            "你慢慢考虑就是了。\x02",
        )
    )

    Jump("loc_8DD")

    label("loc_8DD")

    CloseMessageWindow()
    OP_59()
    Fade(500)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, -26820, 0, 63660, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(    #16
        0x11,
        "#1862F辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x6)
    Sleep(600)
    OP_43(0x11, 0x3, 0x0, 0x7)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10C, 65535)
    SetChrSubChip(0x10C, 0)
    ClearChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, -26680, 0, 66240, 180)
    Sleep(250)

    def lambda_982():

        label("loc_982")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_982")

    QueueWorkItem2(0x10C, 2, lambda_982)
    Sleep(2700)
    OP_44(0x10C, 0x2)

    def lambda_99C():
        OP_8E(0xFE, 0xFFFF932C, 0x0, 0x102C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_99C)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 315, 400)
    WaitChrThread(0x10, 0x3)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #17
        0x10,
        "啊，这么说来所长先生……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 135, 400)
    Sleep(300)

    ChrTalk(    #18
        0x10,
        "下次调查也要拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "虽然我让西蒙去做了，\x01",
            "但总觉得不大放心。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x10C,
        "理查德所长",
        (
            "#1850F#6P嗯嗯，没问题。\x02\x03",

            "还是国外市场的调查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "对对……\x02",
    )

    Jump("loc_AD1")

    label("loc_AD1")

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x10, 225, 400)
    Sleep(300)

    ChrTalk(    #22
        0x10,
        "哦，这个东西不错嘛。\x02",
    )

    CloseMessageWindow()

    def lambda_B1C():
        OP_6D(-36660, 0, 66240, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_B1C)

    def lambda_B34():
        OP_67(0, 4500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B34)

    def lambda_B4C():
        OP_6C(306000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_B4C)

    def lambda_B5C():
        OP_6B(3340, 4000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_B5C)
    OP_43(0x10, 0x3, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x11, 0x3, 0x0, 0xA)
    Sleep(200)
    OP_43(0x10C, 0x3, 0x0, 0x9)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x11, 0x3)
    WaitChrThread(0x10C, 0x3)

    ChrTalk(    #23
        0x10,
        "#5P…………是这里。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x10C,
        "理查德所长",
        "#1853F奥雷德自治州……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        "#1864F#2P啊，要在那么小的地方……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#5P就是因为地方小，\x01",
            "才能获得市场占有率嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#5P那里也有国际定期船，\x01",
            "而且还没有任何人出手呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x10C,
        "理查德所长",
        (
            "#1859F原来如此，\x01",
            "要查明市场规模的可能性……\x01",
            "……是这样吧。\x02\x03",

            "#1850F调查的目标\x01",
            "仅限于导力器市场吗？\x01",
            "还是市场全体……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#5P要全体的调查。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 400)
    Sleep(300)

    ChrTalk(    #30
        0x10,
        "#5P……怎么样，能办到吗？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0x10C,
        "理查德所长",
        (
            "#1850F交给我们吧。\x02\x03",

            "我先联络一下\x01",
            "附近的常驻人员好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        "#5P好，就这么定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#5P下周我还会再来的，\x01",
            "详细情况到时候再说吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E20():
        OP_6D(-35190, 0, 67100, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_E20)

    def lambda_E38():

        label("loc_E38")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_E38")

    QueueWorkItem2(0x10C, 2, lambda_E38)

    def lambda_E49():

        label("loc_E49")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_E49")

    QueueWorkItem2(0x11, 2, lambda_E49)

    def lambda_E5A():
        OP_8E(0xFE, 0xFFFF7D88, 0x0, 0x10360, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E5A)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    ChrTalk(    #34
        0x10,
        "#11P…………回见啦！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #35
        0x10C,
        "理查德所长",
        "#1850F#5P恭候光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#1862F#5P路上小心。\x02",
    )

    CloseMessageWindow()

    def lambda_EF2():
        OP_6D(-33510, 0, 68790, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_EF2)

    def lambda_F0A():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10360, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F0A)
    WaitChrThread(0x10, 0x1)

    def lambda_F2A():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10B6C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F2A)
    WaitChrThread(0x10, 0x1)

    def lambda_F4A():
        OP_8E(0xFE, 0xFFFF7D38, 0xFFFFF830, 0x10B6C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F4A)
    WaitChrThread(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_44(0x10C, 0x2)
    OP_44(0x11, 0x2)
    Sleep(1000)
    OP_8C(0x10C, 215, 400)

    def lambda_F83():
        OP_6D(-36660, 0, 66240, 2500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_F83)

    def lambda_F9B():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0xFC07, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_F9B)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 215, 400)
    WaitChrThread(0x17, 0x0)
    Sleep(300)

    NpcTalk(    #37
        0x10C,
        "理查德所长",
        (
            "#1855F#6P奥雷德自治州吗……\x01",
            "……有点偏内陆啊。\x02\x03",

            "#1850F记得那边应该是\x01",
            "雷因兹兄弟负责的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #38
        0x11,
        "#1860F#11P嗯嗯，稍后我会联络他们的。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x10C,
        "理查德所长",
        "#1850F#6P拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #40
        0x10C,
        "理查德所长",
        (
            "#1859F#6P呵呵，\x01",
            "真不愧是柏斯商人啊。\x02\x03",

            "米拉诺小姐的委托\x01",
            "很具有前瞻性，而且挺有趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        (
            "#1861F#11P虽然和所长相比\x01",
            "还有很大差距。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #42
        0x10C,
        "理查德所长",
        "#1851F#6P哈哈，你太抬举我了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x11, 400)
    Sleep(300)

    NpcTalk(    #43
        0x10C,
        "理查德所长",
        "#1850F#6P……凯诺娜，请下一位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#1862F#11P明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_1208():

        label("loc_1208")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1208")

    QueueWorkItem2(0x10C, 2, lambda_1208)
    OP_8C(0x11, 90, 400)

    def lambda_1220():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1220)
    WaitChrThread(0x11, 0x1)
    OP_44(0x10C, 0x2)
    OP_43(0x10C, 0x3, 0x0, 0xB)

    def lambda_124B():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10C5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_124B)
    WaitChrThread(0x11, 0x1)

    def lambda_126B():
        OP_8E(0xFE, 0xFFFF7D88, 0xFFFFF830, 0x10C5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_126B)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)

    def lambda_1290():
        OP_6D(-34360, 0, 68540, 3500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1290)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -33400, -2000, 68460, 90)

    def lambda_12BE():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0x10C5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12BE)
    Sleep(600)

    def lambda_12DE():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10B6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_12DE)
    Sleep(1000)
    OP_43(0x10C, 0x3, 0x0, 0xE)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 215, 400)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 215, 400)
    WaitChrThread(0x10C, 0x3)

    ChrTalk(    #45
        0x12,
        (
            "#11P哎呀，所长先生，\x01",
            "一直给你添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#11P这次又有点关于\x01",
            "市里财政的事想和你商量……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #47
        0x10C,
        "理查德所长",
        (
            "#1851F#5P好的，乐意效劳。\x02\x03",

            "请坐下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13D2():
        OP_6D(-28500, 0, 67500, 5000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_13D2)

    def lambda_13EA():
        OP_67(0, 5480, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_13EA)

    def lambda_1402():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1402)

    def lambda_1412():
        OP_6B(3260, 5000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_1412)

    def lambda_1422():

        label("loc_1422")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1422")

    QueueWorkItem2(0x10C, 2, lambda_1422)
    OP_8C(0x11, 270, 500)
    OP_8C(0x12, 90, 400)
    Sleep(500)
    SetChrFlags(0x11, 0x4)

    def lambda_144B():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0xF424, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_144B)
    Sleep(700)
    OP_43(0x12, 0x3, 0x0, 0xC)
    Sleep(800)
    OP_44(0x10C, 0x2)
    OP_43(0x10C, 0x3, 0x0, 0xD)
    WaitChrThread(0x11, 0x1)

    def lambda_1487():

        label("loc_1487")

        TurnDirection(0xFE, 0x12, 600)
        OP_48()
        Jump("loc_1487")

    QueueWorkItem2(0x11, 2, lambda_1487)
    WaitChrThread(0x12, 0x3)
    OP_44(0x11, 0x2)

    def lambda_14A1():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0x10AA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14A1)
    WaitChrThread(0x11, 0x1)

    def lambda_14C1():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x10AA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14C1)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 180, 500)
    WaitChrThread(0x10C, 0x3)

    NpcTalk(    #48
        0x10C,
        "理查德所长",
        (
            "#1850F#11P那么，\x01",
            "今天有什么事……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1528():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1528)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2D8 end

    def Function_6_1550(): pass

    label("Function_6_1550")


    def lambda_1556():
        OP_8E(0xFE, 0xFFFF905C, 0x0, 0xF8AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1556)
    WaitChrThread(0x10, 0x1)

    def lambda_1576():
        OP_8E(0xFE, 0xFFFF905C, 0x0, 0x10B6C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1576)
    WaitChrThread(0x10, 0x1)

    def lambda_1596():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10B6C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1596)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_6_1550 end

    def Function_7_15B1(): pass

    label("Function_7_15B1")


    def lambda_15B7():
        OP_8E(0xFE, 0xFFFF9EBC, 0x0, 0x10B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15B7)
    WaitChrThread(0x11, 0x1)

    def lambda_15D7():
        OP_8E(0xFE, 0xFFFF923C, 0x0, 0x10B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15D7)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_7_15B1 end

    def Function_8_15F2(): pass

    label("Function_8_15F2")


    def lambda_15F8():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10360, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15F8)
    WaitChrThread(0x10, 0x1)

    def lambda_1618():
        OP_8E(0xFE, 0xFFFF7D88, 0x0, 0x10360, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1618)
    WaitChrThread(0x10, 0x1)

    def lambda_1638():
        OP_8E(0xFE, 0xFFFF75B8, 0x0, 0xFB90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1638)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 215, 400)
    Return()

    # Function_8_15F2 end

    def Function_9_165A(): pass

    label("Function_9_165A")


    def lambda_1660():
        OP_8E(0xFE, 0xFFFF7BBC, 0x0, 0x102C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1660)
    WaitChrThread(0x10C, 0x1)

    def lambda_1680():
        OP_8E(0xFE, 0xFFFF7BBC, 0x0, 0xFC07, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1680)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 270, 400)
    Return()

    # Function_9_165A end

    def Function_10_16A2(): pass

    label("Function_10_16A2")


    def lambda_16A8():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10B30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_16A8)
    WaitChrThread(0x11, 0x1)

    def lambda_16C8():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_16C8)
    WaitChrThread(0x11, 0x1)

    def lambda_16E8():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_16E8)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 180, 400)
    Return()

    # Function_10_16A2 end

    def Function_11_170A(): pass

    label("Function_11_170A")

    SetChrFlags(0x10C, 0x4)

    def lambda_1715():
        OP_8E(0xFE, 0xFFFF770C, 0x0, 0xF99C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1715)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 120, 400)
    Return()

    # Function_11_170A end

    def Function_12_1737(): pass

    label("Function_12_1737")

    SetChrFlags(0x12, 0x4)

    def lambda_1742():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0x10748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1742)
    WaitChrThread(0x12, 0x1)

    def lambda_1762():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0xF8AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1762)
    WaitChrThread(0x12, 0x1)

    def lambda_1782():
        OP_8E(0xFE, 0xFFFF973C, 0x0, 0xF8AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1782)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 0, 400)
    Fade(250)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -26820, 140, 63060, 0)
    OP_0D()
    Return()

    # Function_12_1737 end

    def Function_13_17C5(): pass

    label("Function_13_17C5")


    def lambda_17CB():
        OP_8E(0xFE, 0xFFFF97C8, 0x0, 0x102C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_17CB)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 180, 400)
    Fade(250)
    SetChrChipByIndex(0x10C, 4)
    SetChrSubChip(0x10C, 0)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, -26680, 200, 66900, 180)
    OP_0D()
    Return()

    # Function_13_17C5 end

    def Function_14_1813(): pass

    label("Function_14_1813")

    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x10C, 45, 500)
    Sleep(500)

    def lambda_1837():
        OP_8E(0xFE, 0xFFFF7C34, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1837)
    WaitChrThread(0x10C, 0x1)

    def lambda_1857():
        OP_8E(0xFE, 0xFFFF8314, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1857)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 45, 500)
    Return()

    # Function_14_1813 end

    def Function_15_1879(): pass

    label("Function_15_1879")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-5980, 0, 65300, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10C, -4880, -500, 60500, 0)
    SetChrPos(0x11, -4880, -500, 60500, 0)
    OP_9F(0x10C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -7600, 500, 64400, 0)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_192E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_192E)

    def lambda_1940():
        OP_8E(0xFE, 0xFFFFECF0, 0x0, 0xFAEF, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1940)
    Sleep(1100)

    def lambda_1960():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1960)
    OP_43(0x11, 0x3, 0x0, 0x11)
    WaitChrThread(0x10C, 0x1)
    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_8C(0x10C, 270, 400)
    Sleep(300)

    NpcTalk(    #49
        0x10C,
        "理查德所长",
        "#1853F#11P嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_19CB():
        OP_6D(-7800, 0, 65300, 2000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_19CB)

    def lambda_19E3():
        OP_8E(0xFE, 0xFFFFE638, 0x0, 0xFAEF, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_19E3)
    WaitChrThread(0x10C, 0x1)
    Sleep(500)
    Fade(500)
    OP_22(0x12, 0x0, 0x50)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    Sleep(500)

    NpcTalk(    #50
        0x10C,
        "理查德所长",
        "#1852F#5P（………这封信是……………）\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    TurnDirection(0x11, 0x10C, 400)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    def lambda_1A99():
        OP_8E(0xFE, 0xFFFFE6D8, 0x0, 0xF690, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A99)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #51
        0x11,
        (
            "#1864F#6P…………所长？\x02\x03",

            "您怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #52
        0x10C,
        "理查德所长",
        (
            "#1855F#11P……………………没什么……\x02\x03",

            "#1850F好像又有一封\x01",
            "错送到这里来的\x01",
            "寄给市长的邮件。\x02\x03",

            "这家事务所\x01",
            "本来是他的家，\x01",
            "也难怪会这样……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 135, 400)
    Sleep(300)

    NpcTalk(    #53
        0x10C,
        "理查德所长",
        "#1850F#5P唉，我给他送去吧。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x168, 0x3C, 0x64)

    def lambda_1BF7():

        label("loc_1BF7")

        TurnDirection(0xFE, 0x10C, 500)
        OP_48()
        Jump("loc_1BF7")

    QueueWorkItem2(0x11, 2, lambda_1BF7)

    def lambda_1C08():
        OP_8F(0xFE, 0xFFFFEBE2, 0x0, 0xF672, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1C08)
    WaitChrThread(0x10C, 0x1)

    def lambda_1C28():
        OP_8E(0xFE, 0xFFFFECF0, 0x0, 0xF384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1C28)
    Sleep(300)

    ChrTalk(    #54
        0x11,
        (
            "#1864F#5P咦，现在吗？\x02\x03",

            "但是，外面都快下雨了……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10C, 0x1)

    NpcTalk(    #55
        0x10C,
        "理查德所长",
        (
            "#1859F#11P没什么，就在附近嘛。\x01",
            "就算下起来也不用担心的。\x02\x03",

            "#1850F定期联络那边就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        "#1864F#5P是、是……\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1D30():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_1D30)

    def lambda_1D42():
        OP_8E(0xFE, 0xFFFFECF0, 0xFFFFFE0C, 0xEC54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1D42)
    WaitChrThread(0x10C, 0x1)
    OP_44(0x11, 0x2)

    def lambda_1D66():
        OP_8C(0x11, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1D66)
    OP_22(0x7, 0x0, 0x64)
    OP_20(0xFA0)

    def lambda_1D7E():
        OP_6D(-7800, 0, 62300, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1D7E)
    OP_43(0x17, 0x3, 0x0, 0x10)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    WaitChrThread(0x17, 0x3)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1879 end

    def Function_16_1DB5(): pass

    label("Function_16_1DB5")

    OP_24(0x168, 0x5A)
    Sleep(100)
    OP_24(0x168, 0x50)
    Sleep(100)
    OP_24(0x168, 0x46)
    Sleep(100)
    OP_24(0x168, 0x3C)
    Sleep(100)
    OP_24(0x168, 0x32)
    Sleep(100)
    OP_24(0x168, 0x28)
    Sleep(100)
    OP_24(0x168, 0x1E)
    Sleep(100)
    OP_24(0x168, 0x14)
    Sleep(100)
    OP_24(0x168, 0xA)
    Sleep(100)
    OP_24(0x168, 0x0)
    OP_23(0x168)
    Return()

    # Function_16_1DB5 end

    def Function_17_1E0E(): pass

    label("Function_17_1E0E")


    def lambda_1E14():
        OP_8E(0xFE, 0xFFFFECF0, 0x0, 0xF438, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E14)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_8C(0x11, 180, 500)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_17_1E0E end

    def Function_18_1E45(): pass

    label("Function_18_1E45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x100000)
    OP_24(0x1C9, 0x3C)
    OP_6D(-5860, 0, 66040, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_6D(-8560, 0, 69400, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10C, -5460, -500, 60500, 0)
    OP_9F(0x10C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -4500, -500, 60500, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F17():
        OP_6D(-5860, 0, 66040, 3500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1F17)

    def lambda_1F2F():
        OP_6C(335000, 3500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1F2F)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1F57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_1F57)

    def lambda_1F69():
        OP_8E(0xFE, 0xFFFFEAAC, 0x0, 0xF67C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1F69)
    Sleep(800)

    def lambda_1F89():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1F89)

    def lambda_1F9B():
        OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xF5A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F9B)
    Sleep(700)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)

    NpcTalk(    #57
        0x10C,
        "理查德所长",
        (
            "#1859F#5P哎呀哎呀，\x01",
            "浑身都湿透了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 90, 400)
    Sleep(300)

    NpcTalk(    #58
        0x10C,
        "理查德所长",
        "#1850F#5P凯诺娜，没事吧？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #59
        0x11,
        (
            "#1861F#4P嗯嗯，\x01",
            "我一点事也没有。\x02\x03",

            "#1860F这让我想起\x01",
            "士官学校时代的\x01",
            "生存训练了。\x02\x03",

            "倒是所长，\x01",
            "您还是请赶快换衣服吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x10C,
        "理查德所长",
        (
            "#1850F#5P啊，我也没事。\x02\x03",

            "生存训练\x01",
            "我可是挺擅长的呢。\x02",
        )
    )

    Jump("loc_2131")

    label("loc_2131")

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "#1864F#4P我、我不是这个意思，可是……\x02",
    )

    CloseMessageWindow()
    OP_22(0xC3, 0x1, 0x32)
    Sleep(800)
    OP_62(0x10C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    def lambda_21A7():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_21A7)
    OP_8C(0x11, 0, 500)
    Sleep(500)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x32)
    Sleep(500)
    OP_22(0x2BB, 0x1, 0x32)
    Sleep(2200)

    NpcTalk(    #62
        0x10C,
        "理查德所长",
        "#1852F#5P……是暗号通信呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#1860F#6P在定期报告里，\x01",
            "迪兰斯说有些情报值得注意。\x02\x03",

            "说不定是收到相关情报了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #64
        0x10C,
        "理查德所长",
        (
            "#1850F#5P原来如此……\x02\x03",

            "#1855F……这么说来，\x01",
            "是共和国方面发生了什么事吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22D2():
        OP_8E(0xFE, 0xFFFFEAAC, 0x7D0, 0x11364, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_22D2)
    Sleep(400)

    def lambda_22F2():
        OP_8E(0xFE, 0xFFFFEE6C, 0x7D0, 0x11364, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22F2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10C, 0xFF)
    OP_44(0x11, 0xFF)
    OP_6D(-35000, 0, 67900, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    LoadEffect(0x0, "map\\mp001_00.eff")
    LoadEffect(0x1, "map\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -35480, 2120, 67780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10C, -33500, -2000, 69060, 90)
    SetChrPos(0x11, -33500, -2000, 69060, 90)
    OP_24(0x2BB, 0x3C)
    Sleep(200)
    OP_24(0x2BB, 0x46)
    OP_43(0x10C, 0x3, 0x0, 0x13)
    OP_43(0x11, 0x3, 0x0, 0x14)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10C, 0x3)
    OP_23(0x2BB)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -35480, 2120, 67780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    NpcTalk(    #65
        0x10C,
        "理查德所长",
        (
            "#1850F#20W……啊啊，是我。\x02\x03",

            "#1499F#20W都说别叫我上校了……\x02\x03",

            "#1855F#20W…………啊啊…………\x02\x03",

            "#20W……啊啊…………\x01",
            "……………啊啊…………\x02\x03",

            "#20W东方人街吗…………\x02\x03",

            "#20W那里还没有\x01",
            "设置情报所呢……\x02\x03",

            "#1850F#20W……啊啊，知道了。\x01",
            "我们这边也会调查看看。\x02\x03",

            "#20W嗯，你也不要鲁莽行事哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)
    WaitChrThread(0x11, 0x3)
    Sleep(500)
    OP_8C(0x10C, 180, 400)
    Sleep(300)

    def lambda_25C8():
        OP_6D(-35000, 0, 66900, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_25C8)
    OP_43(0x10C, 0x1, 0x0, 0x15)

    def lambda_25E7():

        label("loc_25E7")

        TurnDirection(0xFE, 0x10C, 400)
        OP_48()
        Jump("loc_25E7")

    QueueWorkItem2(0x11, 2, lambda_25E7)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #66
        0x11,
        "#1864F有什么情况吗……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10C, 0x1)
    OP_44(0x11, 0x2)
    Sleep(300)

    NpcTalk(    #67
        0x10C,
        "理查德所长",
        (
            "#1852F#5P东方人街\x01",
            "似乎又有猎兵团入驻了。\x02\x03",

            "猎兵团『赤色星座』。\x01",
            "是个相当庞大的组织。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 225, 400)
    Sleep(100)

    def lambda_26AE():
        OP_6D(-35920, 0, 65780, 2500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_26AE)

    def lambda_26C6():
        OP_8E(0xFE, 0xFFFF79A0, 0x0, 0xFF50, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_26C6)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    OP_8C(0x11, 225, 400)
    Sleep(300)

    ChrTalk(    #68
        0x11,
        (
            "#1863F#12P最近一阵子，\x01",
            "活动似乎变得频繁了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0x10C,
        "理查德所长",
        (
            "#1855F#5P至少会有使黑社会势力\x01",
            "抗争激化的可能性。\x02\x03",

            "光使用旧情报部的情报网\x01",
            "似乎无法掌握情况……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #70
        0x10C,
        "理查德所长",
        (
            "#1850F#5P唔…………\x02\x03",

            "#1859F………………看来\x01",
            "我还是去一趟比较好。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2829():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2829)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1E45 end

    def Function_19_2856(): pass

    label("Function_19_2856")


    def lambda_285C():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_285C)
    WaitChrThread(0x10C, 0x1)

    def lambda_287C():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_287C)
    WaitChrThread(0x10C, 0x1)

    def lambda_289C():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_289C)
    WaitChrThread(0x10C, 0x1)

    def lambda_28BC():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0x1093C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_28BC)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 270, 400)
    Sleep(500)
    Return()

    # Function_19_2856 end

    def Function_20_28E3(): pass

    label("Function_20_28E3")

    Sleep(1000)

    def lambda_28EE():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_28EE)
    WaitChrThread(0x11, 0x1)

    def lambda_290E():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_290E)
    WaitChrThread(0x11, 0x1)

    def lambda_292E():
        OP_8E(0xFE, 0xFFFF8364, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_292E)
    WaitChrThread(0x11, 0x1)

    def lambda_294E():
        OP_8E(0xFE, 0xFFFF8364, 0x0, 0x103C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_294E)
    WaitChrThread(0x11, 0x1)
    Sleep(2500)
    OP_8C(0x11, 180, 500)

    def lambda_297A():
        OP_8E(0xFE, 0xFFFF8261, 0x0, 0xFBF4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_297A)
    WaitChrThread(0x11, 0x1)
    Fade(250)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -32180, 700, 63400, 0)
    OP_0D()
    Sleep(1800)
    OP_8C(0x11, 0, 500)

    def lambda_29C2():
        OP_8E(0xFE, 0xFFFF8364, 0x0, 0x103C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_29C2)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_20_28E3 end

    def Function_21_29DD(): pass

    label("Function_21_29DD")


    def lambda_29E3():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0xFBF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_29E3)
    WaitChrThread(0x10C, 0x2)
    OP_8C(0x10C, 225, 400)
    Return()

    # Function_21_29DD end

    SaveToFile()

Try(main)
