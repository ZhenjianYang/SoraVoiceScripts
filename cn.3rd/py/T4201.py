from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4201.x',
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
        '科洛蒂娅公主',                         # 9
        '基库',                                 # 10
        '红茶',                                 # 11
        '红茶',                                 # 12
        '茶器',                                 # 13
        '蛋糕',                                 # 14
        '蛋糕',                                 # 15
        '雷克特书记官',                         # 16
        '目标用摄影机',                         # 17
        '',                                     # 18
    )

    DeclEntryPoint(
        Unknown_00              = -2780,
        Unknown_04              = 12000,
        Unknown_08              = 63200,
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
        'ED6_DT27/CH03960 ._CH',             # 00
        'ED6_DT07/CH02323 ._CH',             # 01
        'ED6_DT26/CH20774 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT07/CH02093 ._CH',             # 04
        'ED6_DT07/CH02320 ._CH',             # 05
        'ED6_DT26/CH20254 ._CH',             # 06
        'ED6_DT26/CH20805 ._CH',             # 07
        'ED6_DT26/CH20806 ._CH',             # 08
        'ED6_DT26/CH20807 ._CH',             # 09
        'ED6_DT26/CH20773 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT27/CH03960P._CP',             # 00
        'ED6_DT07/CH02323P._CP',             # 01
        'ED6_DT26/CH20774P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT07/CH02093P._CP',             # 04
        'ED6_DT07/CH02320P._CP',             # 05
        'ED6_DT26/CH20254P._CP',             # 06
        'ED6_DT26/CH20805P._CP',             # 07
        'ED6_DT26/CH20806P._CP',             # 08
        'ED6_DT26/CH20807P._CP',             # 09
        'ED6_DT26/CH20773P._CP',             # 0A
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
        Unknown3            = 1638403,
        ChipIndex           = 0x3,
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
        Unknown3            = 1638403,
        ChipIndex           = 0x3,
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
        Unknown3            = 1703939,
        ChipIndex           = 0x3,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_292",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_2CB",          # 03, 3
        "Function_4_126E",         # 04, 4
        "Function_5_1370",         # 05, 5
        "Function_6_14C6",         # 06, 6
        "Function_7_155D",         # 07, 7
        "Function_8_267F",         # 08, 8
        "Function_9_315F",         # 09, 9
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_24A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_275")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_291")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_291")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_291")

    Return()

    # Function_0_222 end

    def Function_1_292(): pass

    label("Function_1_292")

    OP_B1("t4201_n")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    Return()

    # Function_1_292 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B5")

    label("loc_2CA")

    Return()

    # Function_2_2B5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x0C\x18――科洛蒂娅殿下，\x01",
            "我已下了一个决心。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x0C\x18我将继续支持即将成为女王的您。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x0C\x18为此我接受了\x01",
            "陛下授予我的重任。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x0C\x18……继续晋升的话，\x01",
            "见到您的机会\x01",
            "恐怕会愈发减少……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x0C\x18但我一定会成为辅佐您的力量。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x0C\x18请务必原谅\x01",
            "我这任性的决定。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(13000, 14000, 78580, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(90000, 0)
    OP_6E(280, 0)
    OP_1D(0x75)
    Sleep(2000)
    SetChrPos(0x10E, 14000, 14000, 78580, 270)

    def lambda_488():
        OP_8E(0xFE, 0x0, 0x36B0, 0x132E0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_488)

    def lambda_4A3():
        OP_6D(260, 14000, 78800, 6000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_4A3)

    def lambda_4BB():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4BB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10E, 0x1)
    Sleep(500)
    OP_8C(0x10E, 0, 400)
    Sleep(500)

    NpcTalk(    #6
        0x10E,
        "尤莉亚上尉",
        (
            "#176F要打扰工作中的陛下\x01",
            "实在有点过意不去……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_52F():
        OP_8E(0xFE, 0x0, 0x36B0, 0x138BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_52F)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 0, 16000, 92000, 180)
    SetChrPos(0x11, -4180, 18400, 86040, 180)

    NpcTalk(    #7
        0x10,
        "女孩的声音",
        "#100P哎呀，尤莉亚小姐……？\x02",
    )

    CloseMessageWindow()

    def lambda_5AE():
        OP_8E(0xFE, 0x0, 0x3E80, 0x15B44, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5AE)
    WaitChrThread(0x10E, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_5E5():
        OP_6D(720, 15500, 86740, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_5E5)

    def lambda_5FD():
        OP_6C(34000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5FD)

    def lambda_60D():
        OP_67(0, 3980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_60D)

    def lambda_625():
        OP_6B(3240, 2000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_625)
    WaitChrThread(0x18, 0x0)
    Sleep(500)

    ChrTalk(    #8
        0x11,
        "#311F#6P啾—☆\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x10, 0x1)

    NpcTalk(    #9
        0x10E,
        "尤莉亚上尉",
        (
            "#173F…………殿、殿下！？\x01",
            "还有基库…………\x02\x03",

            "为、为什么会在这里……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DD():
        OP_8E(0xFE, 0x0, 0x36B0, 0x14410, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6DD)

    def lambda_6F8():
        OP_6D(2250, 14000, 83190, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_6F8)

    def lambda_710():
        OP_6C(53000, 3000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_710)

    def lambda_720():
        OP_67(0, 4019, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_720)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #10
        0x10,
        (
            "#1872F#5P……啊，\x01",
            "是说视察艾尔贝离宫的事吗？\x02\x03",

            "#1815F呵呵，\x01",
            "今天来的市民似乎不太多，\x01",
            "所以就早些回来了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10E,
        "尤莉亚上尉",
        "#170F#12P是这样吗………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#1814F#5P嗯。\x01",
            "尤莉亚小姐，\x01",
            "我听说你今天休息………？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x10E,
        "尤莉亚上尉",
        (
            "#173F#12P嗯，是的…………\x02\x03",

            "#179F呵呵，\x01",
            "好久没有度过这么开心的休息日了。\x02\x03",

            "#171F机缘巧合，\x01",
            "遇到了十分珍贵的朋友……\x02\x03",

            "今天十分尽兴，\x01",
            "连时间都忘了。\x02\x03",

            "这都多亏了陛下\x01",
            "能够准予我休假呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#1818F#5P是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #15
        0x10,
        (
            "#1873F#5P……对了，尤莉亚小姐。\x02\x03",

            "#1872F感谢你\x01",
            "一直以来都支持着我。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #16
        0x10E,
        "尤莉亚上尉",
        "#173F#12P咦…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1819F#5P至今为止我都没发觉，\x01",
            "也没对你说过谢谢……\x02\x03",

            "回想起来，\x01",
            "尤莉亚小姐曾给予\x01",
            "失去双亲的我那么多教导。\x02\x03",

            "#1873F不管是防身术还是耿直的心胸……\x01",
            "在不知不觉中，\x01",
            "你教会了我许多。\x02\x03",

            "#1818F……我应该算是看着\x01",
            "尤莉亚小姐的背影长大的吧………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(    #18
        0x10,
        (
            "#1815F#5P对了对了，\x01",
            "连祖母大人也笑话我呢。\x02\x03",

            "说在一些很细小的地方…………\x01",
            "比如说走路的样子和言行举止，\x01",
            "我都和尤莉亚小姐一模一样……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #19
        0x10E,
        "尤莉亚上尉",
        "#173F#12P#40W…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x10,
        (
            "#1814F#5P……尤莉亚小姐？\x02\x03",

            "怎么了？\x02",
        )
    )

    Jump("loc_C57")

    label("loc_C57")

    CloseMessageWindow()
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #21
        0x10E,
        "尤莉亚上尉",
        (
            "#179F#12P不………………\x02\x03",

            "（我……………………\x01",
            "  一直都陪伴在殿下身旁。）\x02\x03",

            "（我的身影，就在殿下身旁。\x01",
            "  然而我只要一看不到殿下的身影\x01",
            "  就会感到不安、焦虑…………）\x02\x03",

            "#175F（我这个人，真是……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        "#1813F#5P……………………？？？\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_D7F():
        OP_6D(2250, 14000, 83890, 1500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_D7F)

    def lambda_D97():
        OP_6B(3140, 1500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D97)

    def lambda_DA7():
        OP_8E(0xFE, 0x0, 0x36B0, 0x13C54, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_DA7)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x10E, 0x1)
    Sleep(500)

    NpcTalk(    #23
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#12P………………科洛丝。\x02\x03",

            "#178F我今后，\x01",
            "可能无法一直呆在您身边。\x02\x03",

            "但是我已决定\x01",
            "亲手保护您，支持您。\x02\x03",

            "#179F作为臣下，作为挚友，\x01",
            "……更作为姐姐，\x01",
            "这就是我的希望。\x02\x03",

            "#170F……所以，\x01",
            "请您不要太勉强。\x02\x03",

            "有什么需要，\x01",
            "请务必要向我提出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1814F#5P尤莉亚小姐……………………\x02\x03",

            "#1873F……呵呵，当然了。\x02\x03",

            "说不定我还会\x01",
            "任性地向你撒娇……\x02\x03",

            "#1818F不过，\x01",
            "今后也请你多多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #25
        0x10E,
        "尤莉亚上尉",
        "#171F#12P………………是。\x02",
    )

    CloseMessageWindow()

    def lambda_FCA():
        OP_6B(3040, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_FCA)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0x18, 0xFF)
    OP_6D(10240, 18000, 100140, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(55000, 0)
    OP_6E(280, 0)
    SetChrPos(0x11, 9680, 18640, 99540, 270)
    SetChrFlags(0x10E, 0x4)
    SetChrPos(0x10E, 9680, 18000, 102240, 225)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -7540, 18000, 101460, 90)
    OP_43(0x10E, 0x3, 0x0, 0x5)
    OP_43(0x10, 0x3, 0x0, 0x4)

    def lambda_1076():
        OP_6B(3600, 30000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1076)
    FadeToBright(2000, 0)
    WaitChrThread(0x10E, 0x3)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    Sleep(2000)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x00#40W──这天下午，\x01",
            "两人一起悠闲地享用了下午茶。\x02\x03",

            "久违的休息日………\x02\x03",

            "这天的红茶香味\x01",
            "大概会永存于尤莉亚的心中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00Episode『尤莉亚大人的假日』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Call(6, 25)
    OP_C2(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124E")
    Sleep(1000)
    OP_28(0xD, 0x4, 0x10)
    OP_28(0xD, 0x4, 0x20)
    OP_3E(0x2D5, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x00得到了\x1F\xD5\x02\x07\x00。\x02",
    )

    Jump("loc_1217")

    label("loc_1217")

    CloseMessageWindow()
    AddMira(3000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00得到了\x07\x02３０００米拉\x07\x00。\x02",
    )

    Jump("loc_1242")

    label("loc_1242")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_124E")

    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1264")
    NewScene("ED6_DT21/U4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_126D")

    label("loc_1264")

    NewScene("ED6_DT21/U4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_126D")

    Return()

    # Function_3_2CB end

    def Function_4_126E(): pass

    label("Function_4_126E")


    def lambda_1274():
        OP_8E(0xFE, 0x1B1C, 0x4650, 0x18C54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1274)
    WaitChrThread(0x10, 0x1)

    def lambda_1294():
        OP_8E(0xFE, 0x1B1C, 0x4650, 0x18434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1294)
    WaitChrThread(0x10, 0x1)

    def lambda_12B4():
        OP_8E(0xFE, 0x1CD4, 0x4650, 0x18434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12B4)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 8460, 18560, 99880, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 9100, 18560, 98940, 0)
    Sleep(500)

    def lambda_130F():
        OP_8E(0xFE, 0x1CD4, 0x4650, 0x188D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_130F)
    WaitChrThread(0x10, 0x1)

    def lambda_132F():
        OP_8E(0xFE, 0x1F54, 0x4650, 0x188D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_132F)
    WaitChrThread(0x10, 0x1)
    Fade(250)
    SetChrPos(0x10, 8600, 18400, 100600, 180)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Return()

    # Function_4_126E end

    def Function_5_1370(): pass

    label("Function_5_1370")


    def lambda_1376():
        OP_8E(0xFE, 0x25D0, 0x4650, 0x18A24, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1376)
    WaitChrThread(0x10E, 0x1)
    OP_8C(0x10E, 225, 400)
    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 9140, 18520, 100160, 0)
    Sleep(500)
    OP_8C(0x10E, 90, 400)

    def lambda_13C4():
        OP_8E(0xFE, 0x29B8, 0x4650, 0x18A24, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_13C4)
    WaitChrThread(0x10E, 0x1)

    def lambda_13E4():
        OP_8E(0xFE, 0x29B8, 0x4650, 0x17AE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_13E4)
    WaitChrThread(0x10E, 0x1)

    def lambda_1404():
        OP_8E(0xFE, 0x1E00, 0x4650, 0x17AE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1404)
    WaitChrThread(0x10E, 0x1)

    def lambda_1424():
        OP_8E(0xFE, 0x1E00, 0x4650, 0x17F5C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1424)
    WaitChrThread(0x10E, 0x1)
    OP_8C(0x10E, 45, 400)
    Sleep(500)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8500, 18520, 98950, 0)
    Sleep(500)

    def lambda_146B():

        label("loc_146B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_146B")

    QueueWorkItem2(0x10E, 2, lambda_146B)
    WaitChrThread(0x10, 0x3)
    OP_44(0x10E, 0x2)

    def lambda_1485():
        OP_8E(0xFE, 0x1F54, 0x4650, 0x17E1C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1485)
    WaitChrThread(0x10E, 0x1)
    Fade(250)
    SetChrPos(0x10E, 9000, 18140, 98220, 0)
    SetChrChipByIndex(0x10E, 4)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(300)
    Return()

    # Function_5_1370 end

    def Function_6_14C6(): pass

    label("Function_6_14C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_155C")
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x10E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_62(0x10E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(400)
    OP_62(0x10E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1600)
    Jump("Function_6_14C6")

    label("loc_155C")

    Return()

    # Function_6_14C6 end

    def Function_7_155D(): pass

    label("Function_7_155D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(45500, 16000, 80800, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6D(27160, 16000, 77540, 0)
    OP_67(0, 8350, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 42720, 16000, 80320, 90)

    def lambda_1613():
        OP_6D(44170, 16000, 81200, 5000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1613)

    def lambda_162B():
        OP_67(0, 7500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_162B)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x17, 0x1)
    Fade(500)
    OP_6D(44170, 16000, 81200, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x17,
        "#1885F#6P………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, 59550, 16000, 80000, 270)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1719():
        OP_6D(49750, 16000, 81310, 1500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1719)

    def lambda_1731():
        OP_67(0, 6800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1731)
    Sleep(1000)
    OP_22(0x8C, 0x0, 0x64)
    ClearChrFlags(0x11, 0x1)
    OP_43(0x11, 0x0, 0x0, 0x2)

    def lambda_175F():
        OP_8E(0xFE, 0xAB54, 0x445C, 0x130B0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_175F)
    Sleep(1000)

    def lambda_177F():
        OP_6D(44170, 16000, 81200, 2500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_177F)

    def lambda_1797():
        OP_67(0, 7000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1797)
    WaitChrThread(0x11, 0x1)
    OP_97(0x11, 0xAB54, 0x137B8, 0x57E40, 0x1B58, 0x1)
    OP_97(0x11, 0xAB54, 0x137B8, 0x41EB0, 0x1388, 0x1)
    SetChrChipByIndex(0x11, 6)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 270, 400)
    OP_8F(0x11, 0xAAF0, 0x3E80, 0x13880, 0x7D0, 0x0)
    Fade(500)
    SetChrFlags(0x11, 0x1)
    OP_44(0x11, 0x0)
    SetChrPos(0x11, 43860, 16480, 80000, 270)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x11,
        "#311F#11P啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x17,
        (
            "#1881F#6P哟，好久不见。\x02\x03",

            "#1887F一点没变呢，小家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#310F#11P啾啾啾。\x02\x03",

            "啾～啾啾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x17,
        (
            "#1886F#6P是这样啊……\x01",
            "发生了许多事情呢。\x02\x03",

            "#1885F总之，你和你主人\x01",
            "都平安无事，这就最好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        "#311F#11P啾⊙\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 29720, 14000, 69740, 45)

    NpcTalk(    #36
        0x10,
        "女孩的声音",
        "#2P……学长。\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x17, 270, 400)

    def lambda_19A9():

        label("loc_19A9")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_19A9")

    QueueWorkItem2(0x17, 2, lambda_19A9)
    Fade(500)
    OP_6D(34340, 16000, 74200, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)

    def lambda_19FC():
        OP_8E(0xFE, 0x87A0, 0x3E80, 0x123F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19FC)

    def lambda_1A17():
        OP_6D(41740, 16000, 80750, 6500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1A17)
    WaitChrThread(0x10, 0x1)

    def lambda_1A34():
        OP_8E(0xFE, 0xA082, 0x3E80, 0x13420, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A34)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #37
        0x17,
        (
            "#1885F#11P科洛蒂娅殿下。\x01",
            "您好。\x02\x03",

            "#1880F请原谅在下擅自走动，\x01",
            "不过我只在这里参观而已。\x02\x03",

            "#1881F嗯，话说回来，\x01",
            "这里的风景可真好啊。\x02",
        )
    )

    Jump("loc_1AF5")

    label("loc_1AF5")

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "#1819F#6P学长……\x01",
            "这究竟是怎么回事？\x02\x03",

            "#1813F为什么学长你……\x01",
            "会在奥斯本宰相身边\x01",
            "为他效力呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x17,
        (
            "#1886F#11P哎呀……\x01",
            "您说的话在下完全不明白。\x02\x03",

            "#1880F是不是将在下与\x01",
            "另一个人混淆了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "#1817F#6P雷克特·亚兰德尔……\x02\x03",

            "两年前杰尼丝王立学院的注册学生，\x01",
            "前学生会长……\x02\x03",

            "#1812F学长，这不正是你吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x17,
        (
            "#1884F#11P非也，其实我的名字叫\x01",
            "雷克·特～亚兰德尔。\x02\x03",

            "#1882F因此您所说的应该是别人吧。\x02\x03",

            "#1881F称呼我为雷克，\x01",
            "亦或是特～亚兰德尔都可以。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #42
        0x10,
        (
            "#1812F#6P……\x01",
            "别再开玩笑了，学长！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #43
        0x10,
        (
            "#1816F#6P那样突然地提出退学申请，\x01",
            "无声无息的就消失了……！\x02\x03",

            "你知道雷欧学长和露西学姐，\x01",
            "还有乔儿和汉斯他们\x01",
            "有多担心你吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x17,
        "#1882F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1813F#6P连一向冷静的雷欧学长\x01",
            "也不禁大声怒吼！\x02\x03",

            "露西学姐\x01",
            "一脸泪容地苦笑道：\x01",
            "『雷克特就是这样的』！\x02\x03",

            "#1819F乔儿和汉斯，\x01",
            "当然还有我也……！\x02\x03",

            "为什么你……\x02\x03",

            "#1816F既然知道我在这城里，\x01",
            "而且已经在我面前现身，\x01",
            "为什么还要装聋作哑！？\x02",
        )
    )

    Jump("loc_1F2C")

    label("loc_1F2C")

    CloseMessageWindow()

    ChrTalk(    #46
        0x17,
        "#1885F#11P………呵呵……………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x17,
        "#1881F#4S#11P哇哈哈哈哈哈哈哈哈哈！#2S\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#1812F#6P雷克特学长……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x17,
        (
            "#1885F#11P抱歉抱歉。\x01",
            "别露出一副苦大仇深的表情嘛。\x02\x03",

            "#1887F不过呢，你呀。\x01",
            "还是那么固执呢。\x02\x03",

            "当上了王太女\x01",
            "却依然这么一板一眼，\x01",
            "与以前相比一点都没变啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x10,
        "#1872F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        (
            "#1885F#11P不过这我也就放心了。\x02\x03",

            "#1887F之前我还在担心\x01",
            "像你这样的女孩一旦成为了王太女\x01",
            "岂不是进退维谷……\x02\x03",

            "不过就从那些坊间的传闻来看，\x01",
            "你已经有所作为了不是吗？\x02\x03",

            "#1881F我退学之后的这段时间，\x01",
            "你似乎结下了很深厚的缘分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#1872F#6P学长……\x02\x03",

            "#1815F……嗯，托你的福。\x02\x03",

            "#1819F不过，最开始\x01",
            "让我发生转变的关键还是你，\x01",
            "雷克特学长。\x02\x03",

            "虽然你消失得那样突然，\x01",
            "让我没办法回报你……\x02\x03",

            "#1818F但我一直……\x01",
            "很感谢学长你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x17,
        (
            "#1885F#11P哦，那可真是我的荣幸呢。\x02\x03",

            "#1887F难道要回报我一个吻吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#1815F#6P这不行。\x02\x03",

            "#1818F虽然我很尊敬你，\x01",
            "但却谈不上恋爱的感情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x17,
        (
            "#1886F#11P真遗憾呀。\x02\x03",

            "#1885F学妹出落得如此迷人，\x01",
            "我都有些心动了……\x02\x03",

            "#1887F看来我呀，\x01",
            "是在自作多情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#1815F#6P呵呵，你又在开玩笑了。\x02\x03",

            "#1872F学长才是……\x01",
            "你现在这样正式的打扮\x01",
            "简直让人不敢相信自己的眼睛呢。\x02\x03",

            "以前你总是穿着皱皱巴巴的校服，\x01",
            "摆出一副吊儿郎当的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x17,
        (
            "#1884F#11P小傻瓜，那是流行呀。\x02\x03",

            "#1882F那种适度的松垮\x01",
            "也是经过严密的计算\x01",
            "而特地表现出来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1819F#6P……现在我算是相信\x01",
            "这话是真的了。\x02\x03",

            "在随心所欲享受校园生活，\x01",
            "到处肆意捣乱的同时，\x01",
            "学长依然像贤者一般充满理性和智慧。\x02\x03",

            "#1817F其理由……\x01",
            "我今天总算能够窥知一二了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x17,
        "#1882F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#1819F#6P我还要问一下……\x02\x03",

            "#1813F学长，为什么\x01",
            "你会在奥斯本宰相身边？\x02\x03",

            "从学院退学之后……\x01",
            "究竟，发生了什么？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_265D():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_265D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_155D end

    def Function_8_267F(): pass

    label("Function_8_267F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(41740, 16000, 80750, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    OP_43(0x11, 0x3, 0x0, 0x9)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 42720, 16000, 80320, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 43860, 16480, 80000, 270)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 41090, 16000, 78880, 45)

    def lambda_2735():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2735)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #61
        0x17,
        (
            "#1883F#11P哎呀……\x01",
            "定期船差不多要到了。\x02\x03",

            "#1885F那么，\x01",
            "我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#1814F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 135, 400)
    Sleep(300)

    ChrTalk(    #63
        0x17,
        (
            "#1881F#5P再见了，基库。\x02\x03",

            "#1887F下次我给你带点\x01",
            "帝国产的腊肠作为见面礼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x11,
        "#311F#11P啾㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1813F#6P等、等一下！\x02\x03",

            "又要……又要这样\x01",
            "不明不白地离开吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x17)
    Sleep(500)
    OP_44(0x11, 0x3)

    ChrTalk(    #66
        0x17,
        (
            "#1885F#5P对了，科洛丝。\x02\x03",

            "莫非你……\x01",
            "有喜欢的男生了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x10,
        "#1814F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 225, 400)
    Sleep(300)

    ChrTalk(    #68
        0x17,
        (
            "#1887F#11P哦，猜中了吗。\x02\x03",

            "#1881F哎呀～真好啊。\x01",
            "初恋这个东西。\x02\x03",

            "感觉就像心里有只小鹿在乱窜，\x01",
            "充满了甘甜与酸楚，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "#1812F#6P不、不要……\x01",
            "不要再开玩笑了！\x02\x03",

            "#1870F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #70
        0x10,
        (
            "#1815F#6P……嗯。\x01",
            "我是有了喜欢的男生。\x02\x03",

            "#1872F而且不久之前，\x01",
            "我就在这里被他拒绝了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x17,
        (
            "#1883F#11P什么，不会吧！？\x02\x03",

            "这样的偶然\x01",
            "就算是我也无法预料到的啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#1873F#6P呵呵，这就奇怪了。\x02\x03",

            "#1818F我原以为前辈你……\x01",
            "是什么都可以看穿的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x17,
        (
            "#1885F#11P唉，即便是本人\x01",
            "也并非全知全能。\x02\x03",

            "#1887F世间正因此而妙趣横生。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BEA():
        OP_6D(41200, 16000, 80200, 1200)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2BEA)

    def lambda_2C02():
        OP_8E(0xFE, 0xA280, 0x3E80, 0x135C4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2C02)
    Sleep(500)
    OP_8C(0x11, 225, 400)
    WaitChrThread(0x17, 0x1)
    Sleep(500)
    Fade(1000)

    def lambda_2C38():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_2C38)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x17, 0x1)
    OP_0D()
    Sleep(300)
    OP_99(0x10, 0x0, 0x6, 0x3E8)
    OP_99(0x10, 0x3, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #74
        0x10,
        "#1814F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x17,
        (
            "#1885F#11P……不错啊，科洛丝。\x02\x03",

            "唯有体会了恋爱的苦涩，\x01",
            "女人才能真正出类拔萃。\x02\x03",

            "#1887F又向着理想中的自我\x01",
            "迈进了一步，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#1870F#6P……学长………\x02\x03",

            "#1873F…………………………………\x02\x03",

            "#1819F学长……你自己呢？\x02\x03",

            "向着理想中的自我……\x01",
            "接近了吗？\x02\x03",

            "在那位宰相的身边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x17,
        "#1882F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x17, 0x8)
    SetChrFlags(0x17, 0x1)
    OP_0D()

    def lambda_2E40():
        OP_6D(41300, 16000, 80300, 1000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2E40)

    def lambda_2E58():
        OP_8F(0xFE, 0xA438, 0x3E80, 0x13718, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2E58)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #78
        0x17,
        (
            "#1885F#11P……我啊，\x01",
            "并没有什么理想中的自我。\x02\x03",

            "只是觉得有趣，\x01",
            "才跟随着那个大叔的。\x02\x03",

            "#1882F在进入王立学院之前就是如此了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#1814F#6P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_2F31():

        label("loc_2F31")

        TurnDirection(0xFE, 0x17, 500)
        OP_48()
        Jump("loc_2F31")

    QueueWorkItem2(0x10, 2, lambda_2F31)

    def lambda_2F42():
        OP_8E(0xFE, 0x9D94, 0x3E80, 0x13718, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F42)
    WaitChrThread(0x17, 0x1)

    def lambda_2F62():
        OP_6D(40700, 16000, 79700, 1300)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2F62)

    def lambda_2F7A():
        OP_8E(0xFE, 0x98E4, 0x3E80, 0x13268, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F7A)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #80
        0x17,
        (
            "#1886F#5P……皇子虽然也很有本事，\x01",
            "但和那个怪物一般的大叔相比，\x01",
            "还是相去甚远。\x02\x03",

            "#1885F好吧，\x01",
            "请转达我对他的忠告。\x02\x03",

            "#1887F不要在跳舞跳得累了的时候\x01",
            "被怪物吞掉。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(200)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 9)
    SetChrSubChip(0x17, 0)
    Sleep(200)
    SetChrSubChip(0x17, 1)
    Sleep(200)
    SetChrSubChip(0x17, 2)
    Sleep(400)

    def lambda_308A():
        OP_6D(37700, 16000, 76700, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_308A)

    def lambda_30A2():

        label("loc_30A2")

        OP_99(0xFE, 0x2, 0x9, 0x5DC)
        OP_48()
        Jump("loc_30A2")

    QueueWorkItem2(0x17, 2, lambda_30A2)

    def lambda_30B5():
        OP_8F(0xFE, 0x7814, 0x36B0, 0x11346, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_30B5)
    WaitChrThread(0x18, 0x0)
    Sleep(2000)

    def lambda_30DA():
        OP_6D(40000, 16000, 79000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_30DA)
    WaitChrThread(0x18, 0x0)
    OP_44(0x10, 0x2)
    Sleep(500)

    ChrTalk(    #81
        0x10,
        "#1813F#11P#40W……雷克特学长……\x02",
    )

    CloseMessageWindow()

    def lambda_312D():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_312D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_267F end

    def Function_9_315F(): pass

    label("Function_9_315F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3175")
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    Jump("Function_9_315F")

    label("loc_3175")

    Return()

    # Function_9_315F end

    SaveToFile()

Try(main)
