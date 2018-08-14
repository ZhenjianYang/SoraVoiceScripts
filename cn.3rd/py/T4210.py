from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4210   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '亲卫队队员',                           # 9
        '亲卫队队员',                           # 10
        '菲利普',                               # 11
        '杜南公爵',                             # 12
        '希尔丹夫人',                           # 13
        '茜亚',                                 # 14
        '卡兰大主教',                           # 15
        '临时',                                 # 16
        '目标用照相机',                         # 17
        '',                                     # 18
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
        'ED6_DT07/CH01320 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02470 ._CH',             # 02
        'ED6_DT27/CH03585 ._CH',             # 03
        'ED6_DT06/CH20127 ._CH',             # 04
        'ED6_DT06/CH20129 ._CH',             # 05
        'ED6_DT07/CH02460 ._CH',             # 06
        'ED6_DT07/CH02540 ._CH',             # 07
        'ED6_DT07/CH01400 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01320P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT27/CH03585P._CP',             # 03
        'ED6_DT06/CH20127P._CP',             # 04
        'ED6_DT06/CH20129P._CP',             # 05
        'ED6_DT07/CH02460P._CP',             # 06
        'ED6_DT07/CH02540P._CP',             # 07
        'ED6_DT07/CH01400P._CP',             # 08
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
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
        X                   = -5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
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
        Direction           = 0,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0xC8,
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
        "Function_0_212",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_258",          # 02, 2
        "Function_3_27C",          # 03, 3
        "Function_4_118D",         # 04, 4
        "Function_5_120E",         # 05, 5
        "Function_6_1256",         # 06, 6
        "Function_7_129E",         # 07, 7
        "Function_8_12FE",         # 08, 8
        "Function_9_1346",         # 09, 9
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_234")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_247")

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_247")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_247")

    Return()

    # Function_0_212 end

    def Function_1_248(): pass

    label("Function_1_248")

    OP_B1("t4210_n")
    OP_71(0x200, 0x0)
    ExitThread()
    Return()

    # Function_1_248 end

    def Function_2_258(): pass

    label("Function_2_258")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_8D(0xFE, -1790, 6330, 1580, 2190, 2000)
    Jump("Function_2_258")

    label("loc_27B")

    Return()

    # Function_2_258 end

    def Function_3_27C(): pass

    label("Function_3_27C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(18400, 2500, 5420, 0)
    OP_67(0, 8320, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(90000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 5040, 0, -6080, 0)
    SetChrPos(0x10E, 14140, 4500, 9980, 135)
    OP_43(0x10E, 0x3, 0x0, 0x4)

    def lambda_2FE():
        OP_6D(9800, 0, -5180, 11500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2FE)

    def lambda_316():
        OP_67(0, 4059, -10000, 11500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_316)

    def lambda_32E():
        OP_6B(3000, 11500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_32E)

    def lambda_33E():
        OP_6C(45000, 11500)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_33E)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #0 op#A op#5
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#6P#20A（升职吗…………）\x05\x02\x03",

            "#30A（这本来应该是\x01",
            "  值得高兴的事……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2400)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_404():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_404)
    Sleep(50)

    def lambda_417():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_417)
    Sleep(500)

    def lambda_42A():
        OP_8E(0xFE, 0x1C0C, 0x0, 0xFFFFE278, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_42A)
    Sleep(100)

    def lambda_44A():
        OP_8E(0xFE, 0x1CD4, 0x0, 0xFFFFE7C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_44A)
    WaitChrThread(0x11, 0x1)

    def lambda_46A():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_46A)
    WaitChrThread(0x10, 0x1)

    def lambda_47D():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_47D)
    WaitChrThread(0x10E, 0x3)
    OP_63(0x10E)
    Sleep(300)
    Fade(100)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #1
        0x10,
        "上尉，辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        "辛苦了！\x02",
    )

    Jump("loc_4EB")

    label("loc_4EB")

    CloseMessageWindow()
    Fade(120)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    Sleep(150)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    Sleep(280)

    ChrTalk(    #3
        0x11,
        "您今天休假吗？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x10E,
        "尤莉亚上尉",
        (
            "#172F#2P……啊，是的………………\x02\x03",

            "#170F你们的消息还真灵通啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        "不，没什么啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "是利昂从雷斯顿要塞\x01",
            "发来联络说的。\x02\x03",

            "好像是艾柯\x01",
            "直接向陛下请愿的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #7
        0x10E,
        "尤莉亚上尉",
        (
            "#173F#2P#3S请、请愿………！？#2S\x02\x03",

            "#176F（艾柯那家伙……\x01",
            "  说起来，那家伙好像也是\x01",
            "  一副欲言又止的表情……）\x02\x03",

            "（……可恶，\x01",
            "  那三个人凑在一起一定没好事……！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "唉，\x01",
            "我们也想给埃尔赛尤号的\x01",
            "修复工作帮忙啊。\x02",
        )
    )

    Jump("loc_713")

    label("loc_713")

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "不过听说现在去\x01",
            "已经赶不上了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "唉，真是在意啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#2P……不用担心。\x02\x03",

            "那三个人无论怎么说\x01",
            "都要留在雷斯顿要塞。\x02\x03",

            "#170F埃尔赛尤号的修复工作\x01",
            "交给格斯塔夫维修长去办了，\x01",
            "现在正在顺利进行之中。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #12
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#2P对了…………\x02\x03",

            "#178F殿下是不是\x01",
            "已经外出了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        "啊，是的。殿下她……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 17100, 1750, 4240, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 17500, 1750, 4240, 180)

    NpcTalk(    #14
        0x13,
        "男性的声音",
        (
            "#4P科洛蒂娅刚才\x01",
            "已经出发了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_908():
        OP_6D(12260, 0, -4620, 5500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_908)

    def lambda_920():
        OP_6C(36000, 5500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_920)
    OP_43(0x13, 0x3, 0x0, 0x5)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_986():

        label("loc_986")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_986")

    QueueWorkItem2(0x10E, 2, lambda_986)
    Sleep(100)

    def lambda_99C():

        label("loc_99C")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_99C")

    QueueWorkItem2(0x10, 2, lambda_99C)

    def lambda_9AD():

        label("loc_9AD")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_9AD")

    QueueWorkItem2(0x11, 2, lambda_9AD)
    Sleep(300)
    OP_43(0x12, 0x3, 0x0, 0x6)
    WaitChrThread(0x13, 0x3)
    OP_44(0x10E, 0x2)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    Sleep(500)

    ChrTalk(    #15
        0x13,
        (
            "#220F#2P今天预定要视察艾尔贝离宫。\x02\x03",

            "怎么，你没有听说吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x10E,
        "尤莉亚上尉",
        (
            "#170F杜南公爵大人……\x02\x03",

            "#176F不，我不是这个意思………………\x02\x03",

            "……我本来是想\x01",
            "如果可以的话，\x01",
            "打算陪同她一起前往的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x13,
        (
            "#220F#2P唔……担任护卫吗。\x02\x03",

            "说起来，\x01",
            "你好像从很久以前\x01",
            "就主动承担科洛蒂娅的护卫任务。\x02\x03",

            "明明早就不是\x01",
            "一介护卫的级别了嘛。\x02",
        )
    )

    Jump("loc_B59")

    label("loc_B59")

    CloseMessageWindow()

    NpcTalk(    #18
        0x10E,
        "尤莉亚上尉",
        "#175F是、是的…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x13,
        (
            "#225F#2P……反正有好几名\x01",
            "亲卫队员跟着她一起去。\x01",
            "不用担心啦。\x02\x03",

            "不会有事的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x10E,
        "尤莉亚上尉",
        (
            "#178F啊…………\x02\x03",

            "谢谢您。\x01",
            "公爵大人。\x02",
        )
    )

    Jump("loc_C33")

    label("loc_C33")

    CloseMessageWindow()

    ChrTalk(    #21
        0x13,
        (
            "#220F#2P走吧，菲利普。\x01",
            "还有一堆工作要处理呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C74():

        label("loc_C74")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_C74")

    QueueWorkItem2(0x10, 2, lambda_C74)

    def lambda_C85():

        label("loc_C85")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_C85")

    QueueWorkItem2(0x11, 2, lambda_C85)

    def lambda_C96():
        OP_8C(0xFE, 215, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_C96)
    OP_43(0x13, 0x3, 0x0, 0x7)
    Sleep(500)

    ChrTalk(    #22 op#A
        0x12,
        "#721F#25A啊，大人，请等一下……\x02",
    )

    CloseMessageWindow()

    def lambda_CDC():
        OP_8E(0xFE, 0x300C, 0x0, 0xFFFFE638, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CDC)
    WaitChrThread(0x12, 0x1)

    def lambda_CFC():
        OP_8E(0xFE, 0x2BC0, 0x0, 0xFFFFE638, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CFC)
    WaitChrThread(0x12, 0x1)
    Sleep(100)

    ChrTalk(    #23
        0x12,
        (
            "#720F#2P（……尤莉亚大人，\x01",
            "  请不要太消沉。）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x3)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    SetChrPos(0x13, -1020, 0, -11000, 0)

    ChrTalk(    #24
        0x13,
        "#224F#2P菲利普，你在磨蹭什么！\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #25
        0x12,
        "#721F#2P是、是。我马上来……\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x8)
    Sleep(2000)

    def lambda_DEB():
        OP_6D(10860, 0, -4920, 2500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_DEB)
    WaitChrThread(0x18, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #26
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#6P呼………………\x02\x03",

            "（又和殿下\x01",
            "  错过了吗……）\x02\x03",

            "#175F（…………没办法。\x01",
            "  殿下也是公务繁忙……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)

    ChrTalk(    #27
        0x10,
        (
            "#1P杜南公爵大人，\x01",
            "好像变了很多嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "是啊，最近一直在\x01",
            "行政区域努力工作呢。\x02\x03",

            "之前开始的补偿金发放工作\x01",
            "也是公爵大人的提案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1P唔，\x01",
            "我还以为他只会好吃懒做呢……\x02\x03",

            "说到底他还是\x01",
            "女王陛下的侄子啊……\x02",
        )
    )

    Jump("loc_FC4")

    label("loc_FC4")

    CloseMessageWindow()
    OP_63(0x10E)
    Sleep(500)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    OP_8C(0x10E, 270, 500)
    Sleep(300)

    NpcTalk(    #30
        0x10E,
        "尤莉亚上尉",
        (
            "#177F#2P我说你们，\x01",
            "还不赶快住嘴！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_102F():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_102F)

    def lambda_103D():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_103D)
    WaitChrThread(0x10, 0x2)
    Sleep(100)

    ChrTalk(    #31
        0x10,
        "#1P……是，非常抱歉！\x02",
    )


    ChrTalk(    #32
        0x11,
        "……是，非常抱歉！\x02",
    )

    OP_56(0x1)
    OP_59()

    NpcTalk(    #33
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#2P……今天因为休假，\x01",
            "我不会在城里留守。\x02\x03",

            "#170F这里就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "是，请放心吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "#1P请多保重！\x02",
    )

    CloseMessageWindow()

    def lambda_112C():

        label("loc_112C")

        TurnDirection(0xFE, 0x10E, 500)
        OP_48()
        Jump("loc_112C")

    QueueWorkItem2(0x10, 2, lambda_112C)

    def lambda_113D():

        label("loc_113D")

        TurnDirection(0xFE, 0x10E, 500)
        OP_48()
        Jump("loc_113D")

    QueueWorkItem2(0x11, 2, lambda_113D)
    OP_8C(0x10E, 180, 400)

    def lambda_1155():
        OP_8E(0xFE, 0x2580, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1155)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x3E8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_27C end

    def Function_4_118D(): pass

    label("Function_4_118D")


    def lambda_1193():
        OP_8E(0xFE, 0x4330, 0x8CA, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1193)
    WaitChrThread(0x10E, 0x1)

    def lambda_11B3():
        OP_8E(0xFE, 0x4330, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_11B3)
    WaitChrThread(0x10E, 0x1)

    def lambda_11D3():
        OP_8E(0xFE, 0x2BC0, 0x0, 0xFFFFE5FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_11D3)
    WaitChrThread(0x10E, 0x1)

    def lambda_11F3():
        OP_8E(0xFE, 0x2580, 0x0, 0xFFFFE5FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_11F3)
    WaitChrThread(0x10E, 0x1)
    Return()

    # Function_4_118D end

    def Function_5_120E(): pass

    label("Function_5_120E")


    def lambda_1214():
        OP_8E(0xFE, 0x42CC, 0x0, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1214)
    WaitChrThread(0x13, 0x1)

    def lambda_1234():
        OP_8E(0xFE, 0x2EE0, 0x0, 0xFFFFE890, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1234)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Return()

    # Function_5_120E end

    def Function_6_1256(): pass

    label("Function_6_1256")


    def lambda_125C():
        OP_8E(0xFE, 0x445C, 0x0, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_125C)
    WaitChrThread(0x12, 0x1)

    def lambda_127C():
        OP_8E(0xFE, 0x34BC, 0x0, 0xFFFFECDC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_127C)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 500)
    Return()

    # Function_6_1256 end

    def Function_7_129E(): pass

    label("Function_7_129E")

    OP_8C(0x13, 215, 500)

    def lambda_12AB():
        OP_8E(0xFE, 0x25F8, 0x0, 0xFFFFDCD8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_12AB)
    WaitChrThread(0x13, 0x1)

    def lambda_12CB():
        OP_6D(8900, 0, -5200, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_12CB)

    def lambda_12E3():
        OP_8E(0xFE, 0x14, 0x0, 0xFFFFDCD8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_12E3)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_7_129E end

    def Function_8_12FE(): pass

    label("Function_8_12FE")

    OP_8C(0x12, 215, 500)

    def lambda_130B():
        OP_8E(0xFE, 0x24F4, 0x0, 0xFFFFDCD8, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_130B)
    WaitChrThread(0x12, 0x1)

    def lambda_132B():
        OP_8E(0xFE, 0xFFFFFE34, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_132B)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_8_12FE end

    def Function_9_1346(): pass

    label("Function_9_1346")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1300, 0, -17300, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x10E, 240, 0, -18340, 0)
    SetChrChipByIndex(0x10E, 3)
    SetChrSubChip(0x10E, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 9150, 0, -10190, 225)
    SetChrPos(0x11, 8530, 0, -9330, 225)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #36
        0x10E,
        "尤莉亚上尉",
        "#175F呼、呼、呼…………\x02",
    )

    CloseMessageWindow()

    def lambda_1415():
        OP_8E(0xFE, 0x5FA, 0x0, 0xFFFFC037, 0x16A8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1415)
    Sleep(100)

    def lambda_1435():
        OP_8E(0xFE, 0x866, 0x0, 0xFFFFBCDA, 0x16A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1435)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #37
        0x11,
        "尤莉亚上尉！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #38
        0x10,
        (
            "城门已经\x01",
            "暂且关上了。\x02",
        )
    )

    Jump("loc_149A")

    label("loc_149A")

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "您没有受伤吧？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10E, 2)

    NpcTalk(    #40
        0x10E,
        "尤莉亚上尉",
        "#172F啊，是的……没什么事。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    Sleep(500)
    OP_8C(0x10E, 45, 400)
    Sleep(500)

    NpcTalk(    #41
        0x10E,
        "尤莉亚上尉",
        (
            "#178F不、不过，\x01",
            "这到底是…………？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        "哈、哈啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "看起来，\x01",
            "好像是尤莉亚上尉的支持者呢。\x02",
        )
    )

    Jump("loc_15A8")

    label("loc_15A8")

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "说起来，\x01",
            "今天早上王城也收到了很多慕名信……\x02",
        )
    )

    Jump("loc_15EC")

    label("loc_15EC")

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "和这个有什么关系吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    NpcTalk(    #46
        0x10E,
        "尤莉亚上尉",
        "#174F慕、慕名信…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "昨天某家杂志社刊登了\x01",
            "上尉的特集报道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "其中有很多描写您在\x01",
            "浮游都市的活跃表现的文章……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1400)

    ChrTalk(    #49
        0x10,
        "啊，我想起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "在上尉外出的时候，\x01",
            "有几名自称利贝尔通讯\x01",
            "记者的人前来拜访……\x02\x03",

            "说他们要刊登特集，\x01",
            "一定要来采访取材，\x01",
            "还说羡慕您在国民中的人气之类的……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x10E, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1700)

    NpcTalk(    #51
        0x10E,
        "尤莉亚上尉",
        (
            "#176F好、好了，别再说了……\x02\x03",

            "我大概想像得到…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10E, 180, 400)
    Sleep(500)

    NpcTalk(    #52
        0x10E,
        "尤莉亚上尉",
        (
            "#178F（杂志特集……\x01",
            "  慕名信…………）\x02\x03",

            "#176F（为、为什么会这样……）\x02\x03",

            "#176F（……我并不是\x01",
            "  这么伟大的人啊……）\x02\x03",

            "（说起来，\x01",
            "  刚才也受到了陛下的高度评价……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #53
        0x10E,
        "尤莉亚上尉",
        (
            "#175F（我明明只想\x01",
            "  保护殿下而已的………）\x02\x03",

            "（现在也没机会\x01",
            "  继续担当护卫了……）\x02\x03",

            "#175F（这也是…………\x01",
            "  ……没办法的事吗……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 220, 0, -6920, 0)
    SetChrPos(0x14, -180, 0, -5280, 180)
    SetChrPos(0x15, 820, 0, -4860, 180)

    def lambda_19F6():
        OP_6D(1420, 0, -4840, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_19F6)

    def lambda_1A0E():
        OP_67(0, 4780, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1A0E)

    def lambda_1A26():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1A26)
    WaitChrThread(0x18, 0x0)
    Sleep(300)

    ChrTalk(    #54
        0x14,
        (
            "#710F#1P您辛苦了，\x01",
            "卡兰大主教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x16,
        (
            "请转告陛下，\x01",
            "弥撒明天早上８点开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14,
        "#713F#1P是，我会转告的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 180, 400)

    def lambda_1AC8():
        OP_6D(1620, 0, -15900, 4000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1AC8)

    def lambda_1AE0():
        OP_8E(0xFE, 0xDC, 0x0, 0xFFFFC1D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1AE0)
    Sleep(200)

    def lambda_1B00():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFC838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B00)

    def lambda_1B1B():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFC9DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B1B)
    WaitChrThread(0x14, 0x1)
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #57
        0x14,
        (
            "#712F#1P哦，尤莉亚大人。\x01",
            "您在这里……\x02\x03",

            "做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_1BD2():

        label("loc_1BD2")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_1BD2")

    QueueWorkItem2(0x10E, 2, lambda_1BD2)
    Sleep(100)

    def lambda_1BE8():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1BE8)
    Sleep(50)

    def lambda_1BFB():

        label("loc_1BFB")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_1BFB")

    QueueWorkItem2(0x11, 2, lambda_1BFB)
    Sleep(300)

    NpcTalk(    #58
        0x10E,
        "尤莉亚上尉",
        (
            "#173F啊，不…………\x02\x03",

            "#176F原来是大主教。\x01",
            "失礼了。\x02",
        )
    )

    Jump("loc_1C66")

    label("loc_1C66")

    CloseMessageWindow()

    ChrTalk(    #59
        0x16,
        "#5P尤莉亚，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x16,
        (
            "#5P你很久都没有露面，\x01",
            "我一直在担心呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #61
        0x10E,
        "尤莉亚上尉",
        (
            "#178F十、十分抱歉。\x02\x03",

            "最近我都没有\x01",
            "去参加弥撒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x16,
        (
            "#5P哈哈，\x01",
            "我也知道你平时很忙。\x02",
        )
    )

    Jump("loc_1D40")

    label("loc_1D40")

    CloseMessageWindow()

    ChrTalk(    #63
        0x16,
        (
            "#5P不过，就算再怎么忙\x01",
            "也不要迷失了自我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        (
            "#5P最重要的东西\x01",
            "总是会陪伴在你身边的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x10E,
        "尤莉亚上尉",
        (
            "#170F是、是的……\x01",
            "谢谢您。\x02",
        )
    )

    Jump("loc_1DE6")

    label("loc_1DE6")

    CloseMessageWindow()

    ChrTalk(    #66
        0x16,
        (
            "#5P呵呵，\x01",
            "那么我这就告辞了。\x02",
        )
    )

    Jump("loc_1E18")

    label("loc_1E18")

    CloseMessageWindow()
    Fade(100)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    Sleep(300)
    SetChrPos(0x17, 2620, 0, -17500, 0)

    NpcTalk(    #67
        0x17,
        "亲卫队队员",
        "#2P您辛苦了！\x02",
    )


    ChrTalk(    #68
        0x11,
        "#1P您辛苦了！\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_1E89():
        OP_6D(1620, 0, -18000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1E89)

    def lambda_1EA1():
        OP_8E(0xFE, 0xDC, 0x0, 0xFFFFA2A4, 0x528, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1EA1)
    Sleep(200)

    def lambda_1EC1():
        OP_8F(0xFE, 0xFFFFFCF4, 0x0, 0xFFFFB85C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1EC1)
    WaitChrThread(0x10E, 0x1)

    def lambda_1EE1():

        label("loc_1EE1")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_1EE1")

    QueueWorkItem2(0x10, 2, lambda_1EE1)
    Sleep(300)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(700)
    OP_44(0x10E, 0x2)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    NpcTalk(    #69 op#A op#5
        0x10E,
        "尤莉亚上尉",
        (
            "#173F#30A（…………对了，\x01",
            "  有一个办法……）\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8E(0x10E, 0xFFFFFD1C, 0x0, 0xFFFFB5C8, 0x9C4, 0x0)
    Sleep(300)
    SetMapFlags(0x20)

    NpcTalk(    #70
        0x10E,
        "尤莉亚上尉",
        "#178F#5P大主教，请等一下！\x02",
    )

    OP_7C(0x0, 0x50, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x16, 0x10E, 400)

    def lambda_1FFF():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0xFFFFA8BC, 0x76C, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1FFF)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1346 end

    SaveToFile()

Try(main)
