from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1500   ._SN',
        MapName             = 'Bose',
        Location            = 'T1500.x',
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
        '罗伊德',                               # 9
        '',                                     # 10
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
        'ED6_DT07/CH01020 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
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


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_E6",           # 01, 1
        "Function_2_F0",           # 02, 2
        "Function_3_113",          # 03, 3
        "Function_4_802",          # 04, 4
        "Function_5_C31",          # 05, 5
        "Function_6_1357",         # 06, 6
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_E5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_E5")

    Return()

    # Function_0_D2 end

    def Function_1_E6(): pass

    label("Function_1_E6")

    OP_B1("T1500_n")
    Return()

    # Function_1_E6 end

    def Function_2_F0(): pass

    label("Function_2_F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_10A")
    Call(0, 6)

    label("loc_10A")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_F0 end

    def Function_3_113(): pass

    label("Function_3_113")

    OP_1D(0x14)
    OP_C4(0x1, 0x800)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 2190, -2000, 42760, 180)
    SetChrPos(0x10, 2280, -2000, 41180, 0)
    OP_6D(2190, -1800, 41900, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_77(0xCE, 0x98, 0x58, 0x0, 0x0)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00热爱『垂钓』的活泼女孩，艾丝蒂尔·布莱特――\x02\x01",

            "　\x01",
            "以及将本部设在王都、\x01",
            "无比喜爱『垂钓』的组织，『钓公师团』――\x02\x01",

            "　\x01",
            "『物以类聚』――\x02\x01",

            "这就是两者间的奇妙因缘所产生的故事。\x02",
        )
    )

    Jump("loc_27A")

    label("loc_27A")

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1 op#A op#5
        "\x07\x00#15A～第１章　始于川蝉亭～\x05\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_21()
    OP_56(0x0)
    Sleep(1000)
    OP_1D(0xF)
    OP_75(0xFF, 0x3, 0x5)
    OP_75(0xFF, 0x4, 0x5)
    OP_72(0x802, 0x0)
    ExitThread()
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, 80)
    Sleep(2000)

    AnonymousTalk(    #2
        (
            "\x07\x00瓦雷利亚湖沿岸的休憩之所『川蝉亭』――\x02\x01",

            "正游击士艾丝蒂尔在休假期间到访了此地。\x02\x01",

            "　\x01",
            "难得的休闲时光――\x02\x01",

            "艾丝蒂尔借来了旅店的钓具，\x01",
            "走出栈桥，尽情享受垂钓的乐趣。\x02\x01",

            "那天的鱼神奇地接连上钩，\x01",
            "她的篮子里不一会儿就满了。\x02",
        )
    )

    Jump("loc_3CF")

    label("loc_3CF")

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x07\x00同一时刻，来此旅店进行一日游的\x01",
            "『钓公师团』成员罗伊德则叹气不已。\x02\x01",

            "　\x01",
            "一来到这里，他便将小船驶进湖区，\x01",
            "在船上享受垂钓――\x02\x01",

            "但是很不走运，连一条鱼也没钓上来。\x02",
        )
    )

    Jump("loc_47B")

    label("loc_47B")

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x07\x00意气消沉回到旅店的罗伊德――\x02\x01",

            "眼帘中映入了艾丝蒂尔正为大丰收而雀跃不已的身影。\x02\x01",

            "　\x01",
            "这立刻挑起了他的好胜心――\x02\x01",

            "使得他坐立不安，\x01",
            "随即向艾丝蒂尔提出了一种『比试』。\x02",
        )
    )

    Jump("loc_52E")

    label("loc_52E")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x1CC, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_75(0xFF, 0x3, 0x1)
    OP_75(0xFF, 0x4, 0x1)
    OP_71(0x802, 0x0)
    ExitThread()
    Sleep(4000)

    ChrTalk(    #5
        0x10,
        (
            "……就这样，\x01",
            "现在我要向你挑战\x01",
            "爆钓五回合决胜赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1004F爆、爆钓五回合决胜赛～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        "是的，『爆钓比赛』――\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "钓鱼之人赌上骄傲与名誉，\x01",
            "也就是所谓的『决斗』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "而钓公师团的成员\x01",
            "一旦说出这话，\x01",
            "就决不能退缩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "来吧，现在就以自己\x01",
            "最好的钓具为赌注决一胜负吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1019F……真、真是莫名其妙呢。\x02\x03",

            "#1015F而且要以钓具为赌注的话，\x01",
            "我现在手上拿的\x01",
            "可全部是从旅馆借来的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "那样的话，\x01",
            "你什么都不赌也行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "这是我的坚持――\x01",
            "这场比试，你无论如何都得接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F啊哈哈……\x01",
            "看来没有选择余地呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_20(0x3E8)
    OP_C4(0x0, 0x10)
    OP_23(0x1CC)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Sleep(1000)
    Return()

    # Function_3_113 end

    def Function_4_802(): pass

    label("Function_4_802")

    FadeToDark(0, 0, -1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xC0)
    OP_AD(0x240137, 0x0, 0x0, 0x1F4)

    label("loc_825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C30")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_89A"),
        (1, "loc_8C4"),
        (2, "loc_BEE"),
        (SWITCH_DEFAULT, "loc_C2D"),
    )


    label("loc_89A")

    OP_AE(0x1F4)
    Sleep(1000)
    Call(0, 5)
    OP_1D(0xC0)
    OP_AD(0x240137, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2D")

    label("loc_8C4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　艾丝蒂尔与罗伊德将进行一对一的垂钓对决。\x01",
            "  游戏是５次对战的回合制，由玩家和\x01",
            "  对战对手交替行动来进行。\x01",
            "　\x01",
            "  轮到自己的回合时，首先选择要使用的钓竿和鱼饵。\x01",
            "　（※能够使用的鱼饵因钓竿而异。）\x01",
            "　\x01",
            "  选择鱼饵后，即开始钓鱼游戏。\x01",
            "　鱼上钩时，将显示[ ！]标志，\x01",
            "  请迅速按下决定按钮，把鱼钓上来。\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_A7F")

    label("loc_A7F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "  能钓到的鱼根据鱼饵的种类而变化，\x01",
            "  而且钓到的鱼也可能用作鱼饵。\x01",
            "　\x01",
            "  钓到的鱼各自有设定分数，\x01",
            "  最后获得分数多的一方获胜。\x01",
            "　\x01",
            "  此外，大鱼可能会逃走，\x01",
            "  请不要放弃多试几次。\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_BDF")

    label("loc_BDF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_C2D")

    label("loc_BEE")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_C21")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_C2A")

    label("loc_C21")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_C2A")

    Jump("loc_C2D")

    label("loc_C2D")

    Jump("loc_825")

    label("loc_C30")

    Return()

    # Function_4_802 end

    def Function_5_C31(): pass

    label("Function_5_C31")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2710, -2000, 30940, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -2960, -2000, 32500, 180)
    SetChrPos(0x10, -10780, -2000, 32560, 180)
    OP_48()
    OP_3E(0x24F, 1)
    OP_3E(0x250, 1)
    OP_3E(0x253, 1)
    OP_3E(0x3D4, 3)
    OP_3E(0x3D5, 3)
    OP_3E(0x3D7, 3)
    OP_22(0x1CC, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x1B, 0x0, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)"), scpexpr(EXPR_END)), "loc_D0E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D18")

    label("loc_D0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D18")

    EventBegin(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 2190, -2000, 42760, 180)
    SetChrPos(0x10, 2280, -2000, 41180, 0)
    OP_6D(2190, -1800, 41900, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(3000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_D99"),
        (0, "loc_F20"),
        (SWITCH_DEFAULT, "loc_F23"),
    )


    label("loc_D99")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #17
        0x101,
        "#1003F输、输掉了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "呼，总算保住了面子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "这下今晚总算能睡个好觉了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1009F唔～虽然不知道为什么，\x01",
            "但总觉得超级不甘心啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_23(0x1CC)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x18\x07\x05再度挑战小游戏吗？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【 再挑战 】\x01",      # 0
            "【回到门前】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_EEA"),
        (0, "loc_F11"),
        (SWITCH_DEFAULT, "loc_F20"),
    )


    label("loc_EEA")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_F05")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_F0E")

    label("loc_F05")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_F0E")

    Jump("loc_F20")

    label("loc_F11")

    OP_D6(0x1)
    OP_D6(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_F20")

    Jump("loc_F23")

    label("loc_F23")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #22
        0x101,
        "#1018F太好了，赢啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "唔，输了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "不过，这是场精彩的比赛。\x01",
            "即使输了也毫无怨言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "来，收下这个吧。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0x8D4, 0xFFFFF830, 0xA30C, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05罗伊德交出了银色的钓钩。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x10, 0x8E8, 0xFFFFF830, 0xA0DC, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #27
        0x101,
        (
            "#1004F……这、这个是\x01",
            "银耀石做的钓钩？\x02\x03",

            "这么贵重的东西\x01",
            "我可不能收啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "是我向你挑战……\x01",
            "并且失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "难道说，\x01",
            "你还要让我背负更大的耻辱吗？\x02",
        )
    )

    Jump("loc_1105")

    label("loc_1105")

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "来吧，别客气，\x01",
            "收下就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1008F嗯、嗯～……\x01",
            "既然你都这么说了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_23(0x1CC)
    OP_20(0xBB8)
    OP_21()
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x07\x05就这样，\x01",
            "艾丝蒂尔接受了罗伊德的银色钓钩。\x02",
        )
    )

    Jump("loc_11BF")

    label("loc_11BF")

    CloseMessageWindow()

    AnonymousTalk(    #33
        (
            "\x07\x05但她对前方等待着的\x01",
            "奇异的命运一无所知……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1292")
    Sleep(3000)
    OP_28(0x1C, 0x4, 0x10)
    OP_28(0x1C, 0x4, 0x20)
    OP_28(0x1D, 0x4, 0x2)
    OP_3E(0x3A6, 20)
    OP_3E(0x3AA, 20)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x00得到了\x07\x02鱼贝系列\x07\x00。\x02",
    )

    Jump("loc_125B")

    label("loc_125B")

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #35
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_1286")

    label("loc_1286")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1292")

    Sleep(2000)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x18\x07\x05继续进行第二章吗？\x02",
    )

    Sleep(1000)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【 进入第二章 】\x01",      # 0
            "【  回到门前  】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1325"),
        (1, "loc_1334"),
        (SWITCH_DEFAULT, "loc_1356"),
    )


    label("loc_1325")

    OP_A2(0x2504)
    NewScene("ED6_DT21/C4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1356")

    label("loc_1334")

    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_134A")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1353")

    label("loc_134A")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1353")

    Jump("loc_1356")

    label("loc_1356")

    Return()

    # Function_5_C31 end

    def Function_6_1357(): pass

    label("Function_6_1357")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x18\x07\x05爆钓传说艾丝蒂尔\x02",
    )

    OP_CC(0x0, 0x0, 0xFFFF, 0xA0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_13E8")
    OP_CC(0x1, 0x0, "【  回到门前  】")
    OP_CC(0x1, 0x0, "【 从最初开始 】")
    OP_CC(0x1, 0x0, "【从第二章开始】")

    label("loc_13E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1406")
    OP_CC(0x1, 0x0, "【从最终章开始】")

    label("loc_1406")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_56(0x0)
    OP_5F(0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1438"),
        (1, "loc_145F"),
        (2, "loc_1472"),
        (3, "loc_1486"),
        (SWITCH_DEFAULT, "loc_149A"),
    )


    label("loc_1438")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1453")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_145C")

    label("loc_1453")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_145C")

    Jump("loc_149A")

    label("loc_145F")

    OP_20(0x3E8)
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_149A")

    label("loc_1472")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_149A")

    label("loc_1486")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_149A")

    label("loc_149A")

    Jump("loc_1361")

    label("loc_149D")

    Return()

    # Function_6_1357 end

    SaveToFile()

Try(main)
