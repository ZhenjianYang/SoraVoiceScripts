from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4303.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60033",
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
        '凯文神父',                             # 9
        '尤莉亚上尉',                           # 10
        '幻想乐曲',                             # 11
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03580 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
        'ED6_DT27/CH03090P._CP',             # 02
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_123",          # 01, 1
        "Function_2_124",          # 02, 2
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    Event(0, 2)
    Return()

    # Function_0_11E end

    def Function_1_123(): pass

    label("Function_1_123")

    Return()

    # Function_1_123 end

    def Function_2_124(): pass

    label("Function_2_124")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x10A, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 800, 0, -15000, 0)
    SetChrPos(0x9, -800, 0, -16000, 0)
    SetChrFlags(0x8, 0x40)
    OP_6D(2460, 0, -21910, 0)
    OP_67(0, 10420, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A1(0xA, 0x9)
    SetChrPos(0xA, 4030, 0, 6430, 63)
    OP_72(0x9, 0x20)
    OP_72(0x9, 0x4)
    OP_72(0x9, 0x2)
    OP_6F(0x9, 843)
    OP_70(0x9, 0x34B)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)

    def lambda_227():
        OP_6D(1480, 0, 1000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_227)

    def lambda_23F():
        OP_67(0, 10420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23F)

    def lambda_257():
        OP_8E(0x9, 0xFFFFFCE0, 0x0, 0xFFFFFFF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_257)

    def lambda_272():
        OP_8E(0x8, 0x320, 0x0, 0x5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_272)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6B(3200, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        "#1063F#5P这可真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#6P#178F七耀教会对于如何\x01",
            "处置这东西也会略感为难吧。\x02\x03",

            "毕竟称得上是无畏级的\x01",
            "古代遗物吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#1067F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 265, 500)
    Sleep(500)

    ChrTalk(    #3
        0x8,
        (
            "#1060F#5P……可以\x01",
            "让我稍微检查一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 500)
    Sleep(400)

    ChrTalk(    #4
        0x9,
        (
            "#6P#178F当然。\x01",
            "陛下也给予了许可。\x02\x03",

            "希望能借助\x01",
            "你的智慧来帮助我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)
    OP_8C(0x8, 45, 500)

    def lambda_40B():
        OP_6D(3630, 0, 4360, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_40B)

    def lambda_423():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_423)

    def lambda_43B():
        OP_8E(0x8, 0x9CE, 0x0, 0xC6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43B)
    OP_8C(0x9, 37, 500)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 339, 1000)
    Sleep(1000)
    OP_8C(0x8, 48, 1000)
    Sleep(1000)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #5
        0x8,
        (
            "#1063F这就是报告书里的\x01",
            "『环之守护者』吗。\x02\x03",

            "和卡尔瓦德出土的\x01",
            "巨像感觉相似……\x02\x03",

            "#1067F嗯～真想亲眼确认\x01",
            "这东西活动的样子啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        "#1063F还有……\x02",
    )

    CloseMessageWindow()

    def lambda_51E():
        OP_8E(0x8, 0xFFFFFD3A, 0x0, 0x1ACC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51E)
    Sleep(1000)
    OP_8C(0x9, 0, 500)

    def lambda_545():
        OP_6D(390, 600, 19290, 6000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_545)

    def lambda_55D():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55D)

    def lambda_575():
        OP_6B(4200, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_575)
    WaitChrThread(0x101, 0x1)

    def lambda_58A():
        OP_8E(0x8, 0xF0, 0x258, 0x45EC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58A)
    Sleep(500)

    def lambda_5AA():
        OP_8E(0x9, 0xFFFFFDC6, 0x0, 0x2A4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5AA)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x9, 0x8, 500)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #7
        0x8,
        (
            "#1063F古代塞姆利亚文明末期……\x01",
            "１２００年前的东西是吧……\x02\x03",

            "虽然不清楚这个装置的机能，\x01",
            "但好像是整个遗迹的中枢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #8
        0x9,
        (
            "#5P#178F对古代遗物的分析……\x01",
            "以现代的技术来说几乎是不可能的。\x02\x03",

            "虽然同样由导力驱动，\x01",
            "但却是和导力器相异的机械体系……\x02\x03",

            "拉赛尔博士是这么说的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(500)

    ChrTalk(    #9
        0x8,
        (
            "#1060F#5P『女神为时过早的赠物』\x01",
            "——教会是这样定义的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 500)
    Sleep(500)

    ChrTalk(    #10
        0x8,
        "#1063F#5P那些东西……\x02",
    )

    CloseMessageWindow()

    def lambda_757():
        OP_8E(0x8, 0xFFFFE6BA, 0x0, 0x35A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_757)
    Sleep(1000)

    def lambda_777():
        OP_6D(-6050, 0, 13970, 3000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_777)

    def lambda_78F():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_78F)
    OP_8C(0x9, 225, 500)
    Sleep(1000)

    def lambda_7B3():
        OP_8E(0x9, 0xFFFFE8EA, 0x0, 0x285A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7B3)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #11
        0x8,
        (
            "#5P#1063F当使用了一种叫作『福音』的\x01",
            "漆黑的导力器之后……\x02\x03",

            "这些巨大的柱子\x01",
            "似乎就陷入地下了是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "#4P#178F#2P是的，大厅里的\x01",
            "四根柱子都陷进去了。\x02\x03",

            "但是，过了将近两个月，\x01",
            "还是没能找到当中的玄机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#5P#1065F被封印的『辉之环』……\x01",
            "还有被使用过的漆黑的『福音』……\x02\x03",

            "装置所说的第二结界和\x01",
            "设备塔的启动……\x02\x03",

            "#1067F原来如此……\x01",
            "我明白它们之间微妙的联系了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(    #14
        0x9,
        (
            "#4P#173F微妙的联系……\x02\x03",

            "那、那到底是怎么回事……！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(500)

    ChrTalk(    #15
        0x8,
        (
            "#5P#1060F呀～是某种\x01",
            "类似直觉的感觉啦。\x02\x03",

            "我想这地方\x01",
            "会不会就是『门』呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        "#4P#178F『门』……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#5P#1060F嗯嗯，是的。\x02\x03",

            "#1065F在通向女神至宝\x01",
            "的『路』上堵塞着巨大的『门』……\x02\x03",

            "想打开它的话，就需要\x01",
            "被称为『福音』的漆黑钥匙……\x02\x03",

            "#1063F这样想的话，这里没有\x01",
            "关键的『辉之环』也可以理解了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#4P#178F但、但要说是『路』的话，\x01",
            "这里已经是遗迹的最下层了。\x02\x03",

            "博士调查后也确定\x01",
            "这里不存在其它的区域……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#5P#1060F大概这条『路』不是\x01",
            "用通常的方法可以看到的吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(    #20
        (
            "\x07\x00是地下流动的七耀脉……\x01",
            "或是其它更不同的路径……\x02\x03",

            "或许在越过那里之后，\x01",
            "应该就能找到有关『环』的线索了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    Sleep(1000)
    OP_AD(0x2400A4, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_20(0xBB8)
    OP_AE(0xC8)
    Sleep(2000)
    OP_21()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_124 end

    SaveToFile()

Try(main)
