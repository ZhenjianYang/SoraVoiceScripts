from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C3100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3100_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_4EF",          # 01, 1
        "Function_2_633",          # 02, 2
        "Function_3_1459",         # 03, 3
        "Function_4_1AC4",         # 04, 4
        "Function_5_1AE7",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -70, 0, -5570, 0)
    SetChrPos(0xF7, 880, 150, -6000, 0)
    SetChrPos(0xF8, -320, 200, -7040, 0)
    SetChrPos(0xF9, 1170, 210, -7190, 0)
    OP_6D(570, 0, -3460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        (
            "这是王国军的根据地\x01",
            "雷斯顿水上要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "民间人士\x01",
            "请勿进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F#3P那个，我们\x01",
            "是看了公告板而来的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F6")

    ChrTalk(    #3
        0x106,
        (
            "#050F#2P应该会有\x01",
            "和特别训练相关的工作。\x02\x03",

            "你没从上级那里听说吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B")

    label("loc_1F6")


    ChrTalk(    #4
        0x103,
        (
            "#020F#2P应该会有\x01",
            "和特别训练相关的工作。\x02\x03",

            "你没从上级那里听说吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B")


    ChrTalk(    #5
        0xFE,
        "哦，那件事情啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "刚刚，司令部\x01",
            "有通知下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "不是王国军的成员却要参与训练，\x01",
            "实在是辛苦各位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1015F#3P没什么，这也是工作嘛。\x02\x03",

            "#1006F那么，\x01",
            "能不能帮我们向负责人传达一下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "哦，这倒没什么问题，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "你们几位已经\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1011F#3P什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "不，因为训练已经开始\x01",
            "很长时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "进入要塞后一定会立即\x01",
            "要求你们参加模拟战斗训练的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "因此，装备的变更等等\x01",
            "还是事先在这里处理完比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1000F#3P啊，原来如此。\x02\x03",

            "这样的话，\x01",
            "稍微需要一点时间准备呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_46E")

    ChrTalk(    #16
        0x106,
        (
            "#050F#2P确实需要准备准备……\x02\x03",

            "抱歉，能不能稍等一下？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8")

    label("loc_46E")


    ChrTalk(    #17
        0x103,
        (
            "#020F#2P确实需要准备准备……\x02\x03",

            "抱歉，能不能稍等一下？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8")


    ChrTalk(    #18
        0xFE,
        "没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "那么，准备好之后\x01",
            "再跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    OP_28(0x6D, 0x1, 0x1)
    OP_28(0x6D, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_4EF(): pass

    label("Function_1_4EF")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -70, 0, -5570, 0)
    SetChrPos(0xF7, 880, 150, -6000, 0)
    SetChrPos(0xF8, -320, 200, -7040, 0)
    SetChrPos(0xF9, 1170, 210, -7190, 0)
    OP_6D(570, 0, -3460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #20
        0xFE,
        "哟，准备好了吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    OP_28(0x6D, 0x1, 0x2)
    OP_28(0x6D, 0x4, 0x8)
    Call(1, 2)
    Jump("loc_632")

    label("loc_5F5")


    ChrTalk(    #21
        0xFE,
        "哎呀，还没好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "不抓紧一点\x01",
            "训练要结束了哦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x9, 255)

    label("loc_632")

    Return()

    # Function_1_4EF end

    def Function_2_633(): pass

    label("Function_2_633")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, -690, 0, 7060, 180)
    SetChrPos(0xD, 870, 0, 7440, 180)
    SetChrPos(0xE, -1090, 0, 8810, 180)
    SetChrPos(0xF, -290, 0, 8810, 180)
    SetChrPos(0x10, 510, 0, 8810, 180)
    SetChrPos(0x11, 1300, 0, 8810, 180)

    ChrTalk(    #23
        0xFE,
        (
            "好，那我去\x01",
            "向队长传达……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #24
        0xFE,
        (
            "看来不必了……\x01",
            "他自己出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1004F#3P咦……！？\x02",
    )

    CloseMessageWindow()
    OP_70(0x0, 0x1C2)
    Sleep(1000)
    Fade(1000)
    OP_6D(-240, 9150, -5410, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, 0, 0, -3780, 0)
    SetChrPos(0x101, -540, 0, -5810, 0)
    SetChrPos(0xF7, 660, 0, -5820, 0)
    SetChrPos(0xF8, -670, 220, -7420, 0)
    SetChrPos(0xF9, 820, 230, -7580, 0)
    OP_0D()
    OP_43(0x9, 0x1, 0x1, 0x4)

    def lambda_7E9():
        OP_67(0, 6930, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E9)

    def lambda_801():
        OP_6D(0, 0, -4270, 8000)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_801)

    def lambda_819():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_819)
    Sleep(2000)

    def lambda_82E():

        label("loc_82E")

        TurnDirection(0x101, 0xB, 400)
        OP_48()
        Jump("loc_82E")

    QueueWorkItem2(0x101, 1, lambda_82E)

    def lambda_83F():

        label("loc_83F")

        TurnDirection(0xF7, 0xB, 400)
        OP_48()
        Jump("loc_83F")

    QueueWorkItem2(0xF7, 1, lambda_83F)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)

    def lambda_87A():
        OP_8E(0xB, 0xFFFFFD4E, 0x0, 0xFFFFF088, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_87A)

    def lambda_895():
        OP_8E(0xD, 0x366, 0x0, 0xFFFFF204, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_895)

    def lambda_8B0():
        OP_8E(0x10, 0x1FE, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8B0)
    Sleep(35)

    def lambda_8D0():
        OP_8E(0xE, 0xFFFFFBBE, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8D0)
    Sleep(25)

    def lambda_8F0():
        OP_8E(0xF, 0xFFFFFEDE, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8F0)

    def lambda_90B():
        OP_8E(0x11, 0x514, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_90B)
    OP_44(0xFE, 0x1)
    WaitChrThread(0xB, 0x1)
    OP_44(0xB, 0x0)
    OP_4A(0xB, 0)
    WaitChrThread(0xD, 0x1)
    OP_44(0xD, 0x0)
    OP_4A(0xD, 0)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0x0)
    OP_4A(0x10, 0)
    WaitChrThread(0xE, 0x1)
    OP_44(0xE, 0x0)
    OP_4A(0xE, 0)
    WaitChrThread(0xF, 0x1)
    OP_44(0xF, 0x0)
    OP_4A(0xF, 0)
    OP_44(0x11, 0x0)
    OP_4A(0x11, 0)
    WaitChrThread(0xF8, 0x0)
    OP_73(0x0)
    OP_44(0xF7, 0x1)
    OP_44(0x101, 0x1)

    ChrTalk(    #26
        0x101,
        "#1004F啊……希德少校！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C4")

    ChrTalk(    #27
        0x106,
        "#052F真是好久不见了。\x02",
    )

    CloseMessageWindow()

    label("loc_9C4")


    NpcTalk(    #28
        0xB,
        "希德",
        (
            "#701F哈哈，好久不见。\x02\x03",

            "拉赛尔博士绑架事件的事情\x01",
            "给你们添了不少麻烦。\x02\x03",

            "一直想如果有机会的话\x01",
            "要好好地向你们道歉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1016F啊哈哈，没关系啦。\x01",
            "你不是也放我们逃跑了吗。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #30
        0xB,
        "希德",
        (
            "#703F是吗……\x01",
            "你们能这么想我真是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1006F对了，我们今天\x01",
            "是看了公告板而来的。\x02\x03",

            "好像是在进行\x01",
            "特别训练吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #32
        0xB,
        "希德",
        (
            "#701F嗯，本来只是像往常一样的\x01",
            "定期训练……\x02\x03",

            "不过，摩尔根将军马上\x01",
            "就要来视察这里了。\x02\x03",

            "为了鼓舞士气，\x01",
            "我紧急变更了训练内容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F原来如此，可以理解。\x02\x03",

            "要是被那个大嗓门喝斥下来\x01",
            "那可真不好受啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF4")

    ChrTalk(    #34
        0x103,
        "#021F呵呵，的确如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C0B")

    label("loc_BF4")


    ChrTalk(    #35
        0x105,
        "#041F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C0B")


    NpcTalk(    #36
        0xB,
        "希德",
        (
            "#703F本来这工作属于\x01",
            "卡西乌斯准将的管辖范围……\x02\x03",

            "不过很不凑巧，他刚好不在。\x01",
            "所以就由我暂时负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1011F哦，这样啊。\x02\x03",

            "#1015F是吗……\x01",
            "老爸他平时也在这里……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0xB,
        "希德",
        (
            "#701F这次他很快就会回来的。\x02\x03",

            "如果你们在蔡斯逗留一段时间的话，\x01",
            "我想应该有机会遇见他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1017F啊，嗯……也是。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 225, 400)

    ChrTalk(    #40
        0xD,
        "希德中校，时间已经……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)

    NpcTalk(    #41
        0xB,
        "希德",
        (
            "#700F哦，聊过头了。\x02\x03",

            "#703F那么，贝尔克副队长。\x01",
            "接下来的说明就由你负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1015F咦，中校……！？\x02\x03",

            "我记得以前\x01",
            "好像是希德少校吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #43
        0xB,
        (
            "#702F嗯、嗯……\x02\x03",

            "其实有任免命令下达，\x01",
            "我晋升为中校了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1011F噢～原来是这样啊。\x02\x03",

            "#1001F恭喜你，希德中校！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB9")

    ChrTalk(    #45
        0x106,
        (
            "#051F哈哈，这不是很好吗。\x02\x03",

            "像你这样优秀的人\x01",
            "应该要得到嘉奖才对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB9")


    ChrTalk(    #46
        0xB,
        (
            "#701F那个……谢谢了。\x02\x03",

            "我只是履行了身为士官的义务而已，\x01",
            "你们这么说，真有点不太好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1006F你看看，又来了～\x01",
            "你真是太谦虚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        "嗯，说得一点也没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        (
            "中校你应该再\x01",
            "自豪一些……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)

    ChrTalk(    #50
        0xB,
        (
            "#700F贝尔克副队长……\x01",
            "你忘记了自己的职责吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        "……失礼了。\x02",
    )

    CloseMessageWindow()

    def lambda_FCC():
        OP_8C(0xD, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FCC)
    Sleep(250)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #52
        0xD,
        (
            "那么，我就赶快\x01",
            "说明委托的内容吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1051")

    ChrTalk(    #53
        0x106,
        (
            "#050F委托内容就是参加训练吧。\x02\x03",

            "那具体应该做点什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108A")

    label("loc_1051")


    ChrTalk(    #54
        0x103,
        (
            "#020F委托内容就是参加训练吧。\x02\x03",

            "具体应该做点什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108A")


    ChrTalk(    #55
        0xD,
        (
            "希望你们参加模拟战斗，\x01",
            "对手就是士兵们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "战斗预定为二连战，\x01",
            "中间没有休息时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "不把握好节奏的话，\x01",
            "就有可能成为苦战。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1015F没有休息的连战啊……\x01",
            "这、这好像有点难度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        "确实不容易……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "你们的任务是通过战斗\x01",
            "为士兵们做出示范。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "所以希望你们不要手下留情，\x01",
            "要以必胜的信念进行战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002F……明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_11FE")

    ChrTalk(    #63
        0x106,
        "#051F这不用你提醒。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1217")

    label("loc_11FE")


    ChrTalk(    #64
        0x103,
        "#525F这不用你提醒。\x02",
    )

    CloseMessageWindow()

    label("loc_1217")


    ChrTalk(    #65
        0xB,
        (
            "#701F哈哈，真是值得信赖。\x02\x03",

            "那么，带诸位游击士\x01",
            "去训练场吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        "是，了解！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        "#700F待会儿训练场见。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)

    def lambda_128F():
        TurnDirection(0x101, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_128F)

    def lambda_129D():
        OP_8C(0xE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_129D)
    OP_8C(0xF, 0, 400)
    WaitChrThread(0xE, 0x1)

    def lambda_12B7():
        OP_8E(0xB, 0xFFFFFD4E, 0x0, 0x1B94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12B7)
    Sleep(20)

    def lambda_12D7():
        OP_8E(0xE, 0xFFFFFBBE, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_12D7)
    Sleep(30)

    def lambda_12F7():
        OP_8E(0xF, 0xFFFFFEDE, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_12F7)
    Sleep(2000)
    OP_8E(0xD, 0x366, 0x0, 0xFFFFF038, 0x7D0, 0x0)

    ChrTalk(    #68
        0xD,
        (
            "那么就由我来带路。\x01",
            "跟我来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)

    def lambda_1353():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1353)
    OP_8C(0x11, 0, 400)
    OP_44(0x10, 0x1)

    def lambda_136C():
        OP_8E(0xD, 0x366, 0x0, 0x1D10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_136C)
    Sleep(30)

    def lambda_138C():
        OP_8E(0x10, 0x1FE, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_138C)
    Sleep(20)

    def lambda_13AC():
        OP_8E(0x11, 0x514, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_13AC)
    Sleep(1000)

    def lambda_13CC():
        OP_8E(0x101, 0xFFFFFDE4, 0x0, 0x169E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CC)
    Sleep(150)

    def lambda_13EC():
        OP_8E(0xF7, 0x294, 0x0, 0x169E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_13EC)
    Sleep(250)

    def lambda_140C():
        OP_8E(0xF8, 0xFFFFFD62, 0x0, 0x1C02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_140C)

    def lambda_1427():
        OP_8E(0xF9, 0x334, 0x0, 0x1C02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1427)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C3101   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_633 end

    def Function_3_1459(): pass

    label("Function_3_1459")

    EventBegin(0x0)
    OP_6D(500, 80, -3600, 0)
    OP_67(0, 8080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -70, 0, -5570, 0)
    SetChrPos(0xF7, 880, 150, -6000, 0)
    SetChrPos(0xF8, -320, 200, -7040, 0)
    SetChrPos(0xF9, 1170, 210, -7190, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, -540, 0, -3960, 180)
    SetChrPos(0xD, 820, 0, -3580, 180)
    SetChrPos(0xE, -1300, 0, -2190, 180)
    SetChrPos(0xF, -400, 0, -2190, 180)
    SetChrPos(0x10, 400, 0, -2190, 180)
    SetChrPos(0x11, 1300, 0, -2190, 180)
    SetChrPos(0x9, 2440, 0, -4250, 180)
    OP_4A(0x9, 255)
    OP_6F(0x0, 450)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1609")

    ChrTalk(    #69
        0xB,
        (
            "#701F#1P──诸位游击士。\x01",
            "让你们今天特意过来真不好意思。\x02\x03",

            "今后也许还会\x01",
            "请你们进行协助。\x02\x03",

            "到时候\x01",
            "也请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6D, 0x1, 0x80)
    OP_28(0x6D, 0x4, 0x10)
    Jump("loc_16BD")

    label("loc_1609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_16BD")

    ChrTalk(    #70
        0xB,
        (
            "#703F#1P──诸位游击士。\x01",
            "让你们今天特意过来真不好意思。\x02\x03",

            "很遗憾，\x01",
            "训练成果并不是很好……\x02\x03",

            "#701F今后也许还会\x01",
            "请你们进行协助。\x02\x03",

            "到时候\x01",
            "也请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6D, 0x1, 0x100)
    OP_28(0x6D, 0x4, 0x80)
    OP_28(0x6D, 0x4, 0x40)

    label("loc_16BD")


    ChrTalk(    #71
        0x101,
        "#1006F#3P嗯，我们才要请你们多多关照呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1742")

    ChrTalk(    #72
        0x106,
        (
            "#050F#2P我们也希望尽可能地\x01",
            "和军方多合作。\x02\x03",

            "有需要的话请随时\x01",
            "与协会联络。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1790")

    label("loc_1742")


    ChrTalk(    #73
        0x103,
        (
            "#020F#2P我们也希望尽可能地\x01",
            "和军方多合作。\x02\x03",

            "有需要的话请随时\x01",
            "与协会联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_196D")

    ChrTalk(    #74
        0xB,
        (
            "#701F#1P就拜托你们了。\x02\x03",

            "那么最后──\x01",
            "我要把这个交给诸位。\x02\x03",

            "──贝尔克副队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        "是！\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0xD, 0x0, 0x3E8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #76
        "\x07\x00得到了\x1F\x46\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x146, 1)
    Sleep(500)
    OP_94(0x1, 0xD, 0xB4, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #77
        0xB,
        (
            "#701F#1P虽是微不足道的东西，\x01",
            "就当成对你们协助训练的谢礼吧。\x02\x03",

            "请你们有效地利用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1001F#3P谢谢你，希德中校。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1907")

    ChrTalk(    #79
        0x106,
        "#051F#2P不好意思了，真是好东西。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_1907")


    ChrTalk(    #80
        0x103,
        "#021F#2P呵呵，真是好东西。\x02",
    )

    CloseMessageWindow()

    label("loc_1927")


    ChrTalk(    #81
        0xB,
        (
            "#701F#1P那我就先告辞了。\x02\x03",

            "我衷心期待着与诸位\x01",
            "再度相会的日子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1997")

    label("loc_196D")


    ChrTalk(    #82
        0xB,
        (
            "#701F#1P承蒙夸奖。\x02\x03",

            "那我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1997")


    def lambda_199D():
        OP_8C(0xE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_199D)

    def lambda_19AB():
        OP_8C(0xF, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_19AB)

    def lambda_19B9():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19B9)

    def lambda_19C7():
        OP_8C(0x11, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19C7)
    WaitChrThread(0x11, 0x1)

    def lambda_19DA():
        OP_8C(0xB, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19DA)
    Sleep(250)
    OP_8C(0xD, 180, 400)
    WaitChrThread(0xB, 0x1)

    def lambda_19F9():
        OP_8E(0xB, 0xFFFFFDE4, 0x0, 0x1B94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19F9)

    def lambda_1A14():
        OP_8E(0xD, 0x334, 0x0, 0x1D10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A14)

    def lambda_1A2F():
        OP_8E(0xE, 0xFFFFFAEC, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1A2F)

    def lambda_1A4A():
        OP_8E(0xF, 0xFFFFFE70, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1A4A)

    def lambda_1A65():
        OP_8E(0x10, 0x190, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A65)

    def lambda_1A80():
        OP_8E(0x11, 0x514, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A80)
    Sleep(1000)
    OP_70(0x0, 0x0)
    Sleep(350)
    OP_43(0x9, 0x1, 0x1, 0x5)
    OP_73(0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_A2(0x1)
    EventEnd(0x0)
    OP_4B(0x9, 255)
    Return()

    # Function_3_1459 end

    def Function_4_1AC4(): pass

    label("Function_4_1AC4")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x992, 0x0, 0xFFFFF13C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_4_1AC4 end

    def Function_5_1AE7(): pass

    label("Function_5_1AE7")

    OP_8C(0xFE, 270, 400)
    OP_8E(0x9, 0x0, 0x0, 0xFFFFF13C, 0x7D0, 0x0)
    OP_8E(0x9, 0x0, 0x0, 0xFFFFF362, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    Return()

    # Function_5_1AE7 end

    SaveToFile()

Try(main)
