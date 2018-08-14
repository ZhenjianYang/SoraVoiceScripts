from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1603   ._SN',
        MapName             = 'Bose',
        Location            = 'C1603.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        '阿加特',                               # 9
        '目标用照相机',                         # 10
        '',                                     # 11
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
        'ED6_DT06/CH20053 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH00150 ._CH',             # 02
        'ED6_DT06/CH20137 ._CH',             # 03
        'ED6_DT07/CH00154 ._CH',             # 04
        'ED6_DT07/CH00151 ._CH',             # 05
        'ED6_DT07/CH00450 ._CH',             # 06
        'ED6_DT07/CH00460 ._CH',             # 07
        'ED6_DT07/CH00470 ._CH',             # 08
        'ED6_DT07/CH00454 ._CH',             # 09
        'ED6_DT07/CH00464 ._CH',             # 0A
        'ED6_DT07/CH00474 ._CH',             # 0B
        'ED6_DT07/CH00451 ._CH',             # 0C
        'ED6_DT07/CH00461 ._CH',             # 0D
        'ED6_DT07/CH00471 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT06/CH20053P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH00150P._CP',             # 02
        'ED6_DT06/CH20137P._CP',             # 03
        'ED6_DT07/CH00154P._CP',             # 04
        'ED6_DT07/CH00151P._CP',             # 05
        'ED6_DT07/CH00450P._CP',             # 06
        'ED6_DT07/CH00460P._CP',             # 07
        'ED6_DT07/CH00470P._CP',             # 08
        'ED6_DT07/CH00454P._CP',             # 09
        'ED6_DT07/CH00464P._CP',             # 0A
        'ED6_DT07/CH00474P._CP',             # 0B
        'ED6_DT07/CH00451P._CP',             # 0C
        'ED6_DT07/CH00461P._CP',             # 0D
        'ED6_DT07/CH00471P._CP',             # 0E
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_162",          # 00, 0
        "Function_1_178",          # 01, 1
        "Function_2_18B",          # 02, 2
        "Function_3_AAA",          # 03, 3
        "Function_4_1CC4",         # 04, 4
    )


    def Function_0_162(): pass

    label("Function_0_162")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_177")

    Return()

    # Function_0_162 end

    def Function_1_178(): pass

    label("Function_1_178")

    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_72(0x203, 0x0)
    ExitThread()
    Return()

    # Function_1_178 end

    def Function_2_18B(): pass

    label("Function_2_18B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2260, 0, -14860, 0)
    OP_67(0, 3660, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2600, 0, -31760, 30)
    SetChrPos(0x111, 2600, 0, -21000, 30)
    SetChrPos(0x113, 4260, 0, -21340, 30)
    SetChrPos(0x112, 940, 0, -20660, 30)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x111,
        (
            "#1743F#6P哦……\x01",
            "这地方又宽敞了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x112,
        (
            "#1750F#6P感觉好像很特别嘛。\x02\x03",

            "难道这就是洞窟最深处？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x113,
        "#1764F#6P不过，什么也没感觉到啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x111,
        "#1742F#6P难道，还有其它路吗？\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(500)
    OP_22(0x7B, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #4
        0x10,
        "男子的声音",
        (
            "#2P干得不错嘛。\x01",
            "这里就是目的地。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_3A2():
        OP_8C(0xFE, 200, 500)
        ExitThread()

    QueueWorkItem(0x111, 2, lambda_3A2)
    Sleep(50)

    def lambda_3B5():
        OP_8C(0xFE, 200, 500)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_3B5)
    Sleep(50)

    def lambda_3C8():
        OP_8C(0xFE, 200, 500)
        ExitThread()

    QueueWorkItem(0x113, 2, lambda_3C8)
    Sleep(300)

    ChrTalk(    #5
        0x111,
        "#1743F#11P……啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x112,
        "#1753F#11P……哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x113,
        "#1767F#11P啧，身后吗……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(4000, 0, -29800, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x10, 4000, 0, -32259, 0)
    SetChrPos(0x111, 4000, 0, -22880, 180)
    SetChrPos(0x112, 2500, 0, -22980, 180)
    SetChrPos(0x113, 5500, 0, -22980, 180)

    def lambda_4C7():
        OP_8E(0xFE, 0xFA0, 0x0, 0xFFFF900C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4C7)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #8
        0x10,
        (
            "#051F#5P嘿，之前的过程\x01",
            "我全部看到了。\x02\x03",

            "#053F没想到途中\x01",
            "居然会分道扬镳啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #9
        0x111,
        (
            "#1747F#6P那、那还不是因为\x01",
            "大哥选了这种地方！\x02\x03",

            "#1749F要是在更轻松的地方，\x01",
            "怎么会变成那样嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#051F#5P嘿，\x01",
            "所以我才选了这里啊。\x02\x03",

            "#053F陷入困难的时候，\x01",
            "你们会有怎样的行动……\x02\x03",

            "#050F我就是要看看这个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x112,
        "#1753F#6P哦～是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x113,
        (
            "#1763F#6P哼，\x01",
            "说得倒是轻松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#053F#5P……我承认你们\x01",
            "在战斗上的本事。\x02\x03",

            "这方面的水准已经在\x01",
            "一般准游击士以上了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x111,
        "#1743F#6P我们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x112,
        "#1753F#6P在一般准游击士以上……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x113,
        "#1762F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#551F#5P单纯说战斗实力而已。\x02\x03",

            "#051F但是，单靠这个是无法\x01",
            "胜任游击士的工作的。\x02\x03",

            "在这个意义上，\x01",
            "这次你们表现得不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x113,
        (
            "#1763F#6P哼，\x01",
            "尽想些无聊的招数。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#053F#5P不过，\x01",
            "仅仅依此来判断还远远不够。\x02\x03",

            "你们几个，\x01",
            "是否能当上\x01",
            "真正的游击士……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)

    def lambda_914():
        OP_6B(3800, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_914)

    def lambda_924():
        OP_6D(4000, 0, -29300, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_924)
    OP_22(0x1F9, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_21()
    OP_1D(0xC4)
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "#054F#5P最后还要问问\x01",
            "这把『重剑』！\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #21
        0x111,
        (
            "#1749F#6P唉……\x01",
            "果然到头来还是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x111, 6)
    SetChrSubChip(0x111, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x112,
        "#1756F#6P嗯，算是意料之中吧。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x112, 7)
    SetChrSubChip(0x112, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x113,
        (
            "#1761F#6P……啊啊，\x01",
            "那就展示我们所有的实力吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x113, 8)
    SetChrSubChip(0x113, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x10,
        "#051F#5P那好，上吧！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Battle(0x3A4, 0x0, 0x0, 0x0, 0xFF)
    OP_20(0x0)
    Call(0, 3)
    Return()

    # Function_2_18B end

    def Function_3_AAA(): pass

    label("Function_3_AAA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2600, 0, -27040, 0)
    OP_67(0, 4460, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 3)
    SetChrPos(0x10, 4000, 0, -27500, 0)
    SetChrPos(0x111, 4000, 0, -24100, 180)
    SetChrPos(0x112, 3000, 0, -24000, 180)
    SetChrPos(0x113, 5000, 0, -24200, 180)

    def lambda_B6A():
        OP_6B(3400, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B6A)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x111,
        "#1743F#12P成、成功了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x112,
        "#1753F#12P终、终于把大哥……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x113,
        "#1762F#6P真的……打倒了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#053F#5P原来如此……\x01",
            "你们已经有这种本事了啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10, 0x3, 0x1, 0x1F4)
    Fade(500)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #29
        0x111,
        "#1749F#12P喂，这不是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x112,
        "#1755F#12P这不是没事吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x113,
        "#1764F#6P哼……我就知道是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "#051F#5P嘿，\x01",
            "别这么失望嘛。\x02\x03",

            "你们已经能让我单膝跪地了。\x01",
            "自信点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#053F#5P……不过，\x01",
            "这下就知道你们现在的实力了。\x02\x03",

            "#051F我这就来\x01",
            "总结一下考试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x111,
        "#1742F#12P总结……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x112,
        "#1753F#12P就是发表考试结果？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x113,
        "#1763F#6P终于到这个时候了吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #37
        0x10,
        "#050F#5P首先是迪恩……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x111,
        "#1743F#12P从、从我开始？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#051F#5P你的判断力\x01",
            "似乎是你的长处。\x02\x03",

            "#053F不过，还是有点胆小……\x01",
            "或者说感觉太过慎重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x111,
        "#1745F#12P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#050F#5P接着是雷斯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x112,
        "#1752F#12P在！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#053F#5P看来你的\x01",
            "直觉很优秀。\x02\x03",

            "#555F不过，行动有点轻率，\x01",
            "这个值得注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x112,
        "#1755F#12P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#050F#5P最后是洛克……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x113,
        "#1764F#6P哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "#053F#5P你性格好强，\x01",
            "行动力值得肯定……\x02\x03",

            "但还欠缺冷静的判断。\x02\x03",

            "#051F你这个样子，\x01",
            "有几条命都不够用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x113,
        "#1763F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#551F#5P让我直说的话，\x01",
            "你们都还不够格。\x02\x03",

            "#555F说实话……\x01",
            "看着都觉得危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x111,
        "#1749F#12P虽然不甘心……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x112,
        "#1754F#12P不过感觉正中要害。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x113,
        "#1764F#6P哼，还是得重来吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#053F#5P……以上是对你们\x01",
            "个人的评价。\x02\x03",

            "#051F不过，你们三个聚在一起，\x01",
            "就要重新评价了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x112, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x113, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #54
        0x111,
        "#1743F#12P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x112,
        "#1753F#12P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x113,
        "#1762F#6P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#051F#5P看过你们最后和魔兽的战斗……\x01",
            "我终于可以放心了。\x02\x03",

            "嗯，三个人一起合作的话\x01",
            "总是比一个人要强的。\x02\x03",

            "#053F因此……\x01",
            "有条件的算你们合格吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #58
        0x112,
        "#1750F#12P合、合格……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x111,
        "#1743F#12P但、但是条件是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#053F#5P啊，那就是你们要\x01",
            "经常三个人一起共事。\x02\x03",

            "#050F这样吧……\x01",
            "至少在成为正游击士以前。\x02\x03",

            "我也会跟嘉恩说好，\x01",
            "让他这样安排工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x113,
        "#1762F#6P三人一起……共事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#053F#5P是啊，三个人一起积累经验，\x01",
            "暂且好好培养心态。\x02\x03",

            "#051F这样总有一天\x01",
            "能够独挑大梁的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x113,
        "#1761F#6P哦，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x111,
        (
            "#1749F#12P虽然觉得\x01",
            "有点可怜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x112,
        "#1751F#12P不过，比不合格好多了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#053F#5P哼，\x01",
            "总之好好努力吧。\x02\x03",

            "#051F好了……\x01",
            "你们擅长的武器是甩棍对吧。\x02\x03",

            "就当作庆祝合格的贺礼。\x01",
            "去柏斯的武器店，\x01",
            "我给你们买把新的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x111,
        "#1747F#12P庆、庆祝合格……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x112,
        "#1753F#12P大、大哥为我们？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x113,
        "#1764F#6P哼，真恶心。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x10,
        (
            "#551F#5P我都说了，你们几个……\x01",
            "到底以为我是什么人啊。\x02\x03",

            "#555F不准再说我是\x01",
            "无血无泪的鬼怪或恶魔了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x113,
        "#1761F#6P唉，说得好听。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x112,
        (
            "#1756F#12P不过，确实……\x01",
            "对那个小姑娘多温柔啊。\x02\x03",

            "#1751F是叫小提妲吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x10,
        "#057F#5P#4S啊……？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #74
        0x111,
        (
            "#1745F#6P（喂、喂，雷斯！\x01",
            "  这个是禁句啊……！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x112,
        "#1753F#11P（对、对了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#053F#5P……我算明白你们的想法了。\x02\x03",

            "#051F稍微给点好脸色看\x01",
            "就拿我当傻瓜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x113,
        (
            "#1764F#6P唉……\x01",
            "没办法了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #78
        0x10,
        (
            "#054F#5P现在开始给我\x01",
            "马拉松跑到洞口去！\x02\x03",

            "稍微慢一点\x01",
            "就用重剑砍了你们！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x111, 0x113, 400)
    Sleep(300)

    ChrTalk(    #79
        0x111,
        (
            "#1747F#11P喂，洛克……\x01",
            "论持久力你第一！\x02\x03",

            "别让大哥追上，\x01",
            "拜托你领头了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x113, 0x111, 400)
    Sleep(300)

    ChrTalk(    #80
        0x113,
        (
            "#1761F#6P嘿……\x01",
            "不用你说，我也正打算这样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x112,
        "#1751F唉～到头来果然还是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        "#054F#5P喂，还不快跑！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x111, 180, 0)
    OP_8C(0x112, 180, 0)
    OP_8C(0x113, 180, 0)
    Sleep(300)

    ChrTalk(    #83
        0x111,
        "#1743F#5P是、是！\x02",
    )


    ChrTalk(    #84
        0x112,
        "#1752F#4P哇、哇！\x02",
    )


    ChrTalk(    #85
        0x113,
        "#1762F#3P哦、哦！\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_1B57():

        label("loc_1B57")

        TurnDirection(0xFE, 0x111, 500)
        OP_48()
        Jump("loc_1B57")

    QueueWorkItem2(0x10, 2, lambda_1B57)
    OP_62(0x113, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x113, 0x3, 0x0, 0x4)
    Sleep(100)
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x111, 0x3, 0x0, 0x4)
    Sleep(100)
    OP_62(0x112, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x112, 0x3, 0x0, 0x4)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x113, 0xFF)
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x10, 0xFF)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x00Episode『重剑流特训法』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB7")
    Sleep(1000)
    OP_28(0xC, 0x4, 0x10)
    OP_28(0xC, 0x4, 0x20)
    OP_3E(0x148, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #87
        "\x07\x00得到了\x1F\x48\x01\x07\x00。\x02",
    )

    Jump("loc_1C82")

    label("loc_1C82")

    CloseMessageWindow()
    AddMira(100)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #88
        "\x07\x00得到了\x07\x02１００米拉\x07\x00。\x02",
    )

    Jump("loc_1CAB")

    label("loc_1CAB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1CB7")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5513   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_AAA end

    def Function_4_1CC4(): pass

    label("Function_4_1CC4")

    OP_8C(0xFE, 90, 500)

    def lambda_1CD1():
        OP_8E(0xFE, 0x1770, 0x0, 0xFFFFA114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CD1)
    WaitChrThread(0xFE, 0x1)

    def lambda_1CF1():
        OP_8E(0xFE, 0x1770, 0x0, 0xFFFF667C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CF1)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_1CC4 end

    SaveToFile()

Try(main)
