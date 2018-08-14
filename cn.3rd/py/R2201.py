from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2201   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2201.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
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
        '费瑟尔',                               # 9
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
        Unknown_3A              = 101,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01200 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01200P._CP',             # 00
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
        "Function_1_EF",           # 01, 1
        "Function_2_F0",           # 02, 2
        "Function_3_119",          # 03, 3
        "Function_4_5CF",          # 04, 4
        "Function_5_9EB",          # 05, 5
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    OP_B1("R2201_1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_EE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_EE")

    Return()

    # Function_0_D2 end

    def Function_1_EF(): pass

    label("Function_1_EF")

    Return()

    # Function_1_EF end

    def Function_2_F0(): pass

    label("Function_2_F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1E, 0x4, 0x8)
    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_F0 end

    def Function_3_119(): pass

    label("Function_3_119")

    OP_72(0x0, 0x0)
    ExitThread()
    OP_72(0x1, 0x0)
    ExitThread()
    OP_72(0x2, 0x0)
    ExitThread()
    OP_72(0x3, 0x0)
    ExitThread()
    OP_72(0x4, 0x0)
    ExitThread()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 65099, -6000, -25940, 294)
    SetChrPos(0x10, 63790, -6000, -24800, 146)
    OP_6D(64629, -6000, -25100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_77(0xCC, 0x8E, 0x5A, 0x0, 0x0)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0 op#A op#5
        "\x07\x00#15A～最终章　亚瑟利亚湾的决斗～\x05\x02",
    )

    CloseMessageWindow()
    Sleep(3000)
    OP_56(0x0)
    Sleep(1000)
    OP_23(0x1C8)
    OP_75(0xFF, 0x11, 0x5)
    OP_75(0xFF, 0x12, 0x5)
    OP_75(0xFF, 0x1A, 0x5)
    OP_75(0xFF, 0x1B, 0x5)
    FadeToBright(3000, 0)
    OP_1E()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, 80)
    Sleep(2000)

    AnonymousTalk(    #1
        (
            "\x07\x00卢安地区梅威海道，亚瑟利亚湾沿岸――\x02\x01",

            "　\x01",
            "诺琪所说的对决之时很快就到来了。\x02\x01",

            "　\x01",
            "这次相遇是偶然还是必然呢――\x02\x01",

            "某天艾丝蒂尔在海道旁的海滨漫步，\x01",
            "这时一艘小型帆船靠近了她。\x02",
        )
    )

    Jump("loc_307")

    label("loc_307")

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x00小船一靠岸，\x01",
            "船上就出现了一个人的身影――\x02\x01",

            "　\x01",
            "――背向大海而立，穿着晚礼服的绅士。\x02\x01",

            "　\x01",
            "这毫无疑问就是『钓公师团』的团长――\x02\x01",

            "被称为『钓鱼男爵』，有『太公望』之称号的\x01",
            "费瑟尔其人。\x02",
        )
    )

    Jump("loc_3CD")

    label("loc_3CD")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x1C8, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_75(0xFF, 0x11, 0x3)
    OP_75(0xFF, 0x12, 0x3)
    OP_75(0xFF, 0x1A, 0x3)
    OP_75(0xFF, 0x1B, 0x3)
    Sleep(4000)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x10,
        "！！！\x02",
    )

    Jump("loc_44F")

    label("loc_44F")

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "那、那钓钩与钓竿是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F你、你是，团长先生？\x01",
            "我是……\x02",
        )
    )

    Jump("loc_4AE")

    label("loc_4AE")

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "不用再说了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "我一直\x01",
            "在等待这一刻……！！\x02",
        )
    )

    Jump("loc_4F8")

    label("loc_4F8")

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "就是现在！\x01",
            "我要向你挑战爆钓十五回合决胜赛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1016F十、十五回合……\x02\x03",

            "这下可要拖很长时间了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "来吧，决一胜负！！\x02",
    )

    CloseMessageWindow()
    OP_23(0x1C8)
    Sleep(300)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_20(0xBB8)
    OP_21()
    Return()

    # Function_3_119 end

    def Function_4_5CF(): pass

    label("Function_4_5CF")

    OP_1D(0xC0)
    OP_AD(0x240139, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EA")
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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_652"),
        (1, "loc_67C"),
        (2, "loc_9A8"),
        (SWITCH_DEFAULT, "loc_9E7"),
    )


    label("loc_652")

    OP_AE(0x1F4)
    Sleep(1000)
    Call(0, 5)
    OP_1D(0xC0)
    OP_AD(0x240139, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E7")

    label("loc_67C")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "  艾丝蒂尔和费瑟尔将进行一对一的钓鱼对决。\x01",
            "  游戏是１５次对战的回合制，由玩家和\x01",
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

    Jump("loc_839")

    label("loc_839")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
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

    Jump("loc_999")

    label("loc_999")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_9E7")

    label("loc_9A8")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_9DB")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_9E4")

    label("loc_9DB")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_9E4")

    Jump("loc_9E7")

    label("loc_9E7")

    Jump("loc_5E8")

    label("loc_9EA")

    Return()

    # Function_4_5CF end

    def Function_5_9EB(): pass

    label("Function_5_9EB")

    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(58740, -6720, -62720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 60130, -6720, -62280, 243)
    SetChrPos(0x10, 64900, -6760, -69120, 243)
    OP_48()
    OP_3E(0x24F, 1)
    OP_3E(0x252, 1)
    OP_3E(0x253, 1)
    OP_3E(0x3DB, 10)
    OP_3E(0x3DC, 10)
    OP_22(0x1C8, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x1B, 0x2, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xE1, 0xFFFFF45C, 0xFFFFF448, 0x72C4)"), scpexpr(EXPR_END)), "loc_AC8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD2")

    label("loc_AC8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD2")

    EventBegin(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 65099, -6000, -25940, 294)
    SetChrPos(0x10, 63790, -6000, -24800, 146)
    OP_6D(64629, -6000, -25100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    Sleep(3000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_B53"),
        (0, "loc_CA6"),
        (SWITCH_DEFAULT, "loc_CA9"),
    )


    label("loc_B53")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #13
        0x101,
        "#1007F输、输了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "哇哈哈！　\x01",
            "果然本人才是最强的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "如果想再挑战，\x01",
            "本人随时都奉陪。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_23(0x1C8)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_C6D"),
        (0, "loc_C97"),
        (SWITCH_DEFAULT, "loc_CA6"),
    )


    label("loc_C6D")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_C88")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_C91")

    label("loc_C88")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_C91")

    Jump("loc_CA6")

    label("loc_C97")

    OP_D6(0x1)
    OP_D6(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_CA6")

    Jump("loc_CA9")

    label("loc_CA9")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #17
        0x10,
        "没想到，竟然如此厉害……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "……唔，\x01",
            "这就是所谓时代的潮流吗。\x02",
        )
    )

    Jump("loc_D16")

    label("loc_D16")

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "好吧，请收下这个吧。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFB54, 0xFFFFE890, 0xFFFF9DAE, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05从费瑟尔手中接过了闪耀着彩虹色的鱼线。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x10, 0xF92E, 0xFFFFE890, 0xFFFF9F20, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #21
        0x101,
        (
            "#1008F哇，好漂亮的鱼线哦……\x01",
            "真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "……嗯。\x01",
            "这下三种钓具\x01",
            "终于全部收集到一起了呢。\x02",
        )
    )

    Jump("loc_E43")

    label("loc_E43")

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "你……\x01",
            "是叫做艾丝蒂尔对吧？\x02",
        )
    )

    Jump("loc_E74")

    label("loc_E74")

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1011F是、是的，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "……本人已经有所觉悟了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "从今天开始\x01",
            "你就是钓公师团的团长了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1004F咦……？\x02\x03",

            "#1005F呃，你说什么～！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "而本人嘛……\x01",
            "今后会成为名誉会长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "从现在开始就是年轻人的时代了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "为了普及和发展垂钓文化，\x01",
            "所有的事情都拜托给你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1004F等、等一下……\x01",
            "我、我可不干哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_23(0x1C8)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    Sleep(1500)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x00此后，两人之间进行了长达一小时的交涉――\x02\x01",

            "　\x01",
            "以团长实在是任重道远为由，\x01",
            "姑且以认定艾丝蒂尔为名誉团员的形式告终。\x02\x01",

            "　\x01",
            "而这一连串比试的故事\x01",
            "瞬间传遍了钓鱼爱好者们之间――\x02\x01",

            "在此以后，他们都这样称呼艾丝蒂尔。\x02",
        )
    )

    Jump("loc_1120")

    label("loc_1120")

    CloseMessageWindow()

    AnonymousTalk(    #34
        (
            "\x07\x00称霸爆钓比赛之王――\x02\x01",

            "　　　　　　　　亦称为『爆钓王』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C4(0x1, 0x800)
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00Episode『爆钓传说艾丝蒂尔』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1251")
    Sleep(3000)
    OP_28(0x1E, 0x4, 0x20)
    OP_28(0x1E, 0x4, 0x10)
    OP_3E(0x12C, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x00得到了\x1F\x2C\x01\x07\x00。\x02",
    )

    Jump("loc_121A")

    label("loc_121A")

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_1245")

    label("loc_1245")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1251")

    Sleep(2000)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_126C")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1275")

    label("loc_126C")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1275")

    Return()

    # Function_5_9EB end

    SaveToFile()

Try(main)
