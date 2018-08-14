from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4143   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4143.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '目标用照相机',                         # 9
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
        "Function_0_CA",           # 00, 0
        "Function_1_107",          # 01, 1
        "Function_2_108",          # 02, 2
        "Function_3_F8F",          # 03, 3
        "Function_4_1021",         # 04, 4
        "Function_5_1027",         # 05, 5
        "Function_6_1093",         # 06, 6
        "Function_7_111B",         # 07, 7
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_F5")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_106")

    label("loc_F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_106")

    Return()

    # Function_0_CA end

    def Function_1_107(): pass

    label("Function_1_107")

    Return()

    # Function_1_107 end

    def Function_2_108(): pass

    label("Function_2_108")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, 540, -250, -3300, 180)
    SetChrPos(0x151, -540, -250, -3100, 180)
    OP_6D(760, -250, -5360, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    def lambda_179():
        OP_6D(1760, -250, -1360, 4000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_179)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    OP_63(0x103)
    OP_63(0x151)
    Sleep(500)

    ChrTalk(    #0
        0x103,
        (
            "#1642F#2P嘁，数量丝毫不减……\x02\x03",

            "#1647F如果不赶快\x01",
            "去协会的话……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x151,
        (
            "#1654F……没办法了。\x01",
            "今晚就在这里休息吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25E():
        TurnDirection(0xFE, 0x151, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_25E)
    Sleep(100)

    def lambda_271():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_271)
    Sleep(300)

    ChrTalk(    #2
        0x103,
        (
            "#1642F#2P只是这些人的话\x01",
            "突破还是没问题的。\x02\x03",

            "只要见缝插针就可以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x151,
        (
            "#1652F不行哦，别太勉强了。\x01",
            "该休息的时候就得休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#1647F#2P（嗯…………\x01",
            "  倒是也有道理……）\x02\x03",

            "#1646F（不、不行不行。\x01",
            "  不能冲动行事……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x151, 0x3, 0x0, 0x3)
    OP_8C(0x103, 180, 400)
    Sleep(300)
    OP_43(0x103, 0x3, 0x0, 0x4)

    ChrTalk(    #5
        0x103,
        (
            "#1646F#2P他们早晚\x01",
            "会闯到这里来。\x02\x03",

            "#1642F还是不要冒险了，\x01",
            "到协会去避难吧。\x01",
            "肯定比这里要安全。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x103, 0x3)
    OP_8C(0x103, 270, 400)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_439():
        OP_6D(400, 2500, 1060, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_439)

    def lambda_451():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_451)
    Sleep(1000)
    OP_8C(0x103, 0, 400)
    WaitChrThread(0x10, 0x0)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x151, 0x3)

    ChrTalk(    #6
        0x103,
        (
            "#1644F啊，喂！\x01",
            "不要擅自行动！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x103, 0x3, 0x0, 0x6)
    Sleep(1000)
    OP_43(0x151, 0x3, 0x0, 0x5)

    def lambda_4D1():
        OP_6D(1220, 4000, 5340, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4D1)
    WaitChrThread(0x151, 0x3)

    ChrTalk(    #7
        0x151,
        (
            "#1650F在二层休息吧。\x02\x03",

            "万一他们闯进来了，\x01",
            "也比较容易逃跑。\x02\x03",

            "……就在这里吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x3)

    ChrTalk(    #8
        0x103,
        (
            "#1642F#1P给我等一下啊。\x02\x03",

            "#1642F这可是为了\x01",
            "你的安全着想……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(    #9
        0x151,
        (
            "#1654F那些黑衣人\x01",
            "在大半夜里\x01",
            "也一本正经地在巡逻。\x02\x03",

            "所以我觉得\x01",
            "不太可能让我们找到机会。\x02\x03",

            "#1650F既然好不容易到了这里……\x01",
            "今晚就好好休息，\x01",
            "明天再努力好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#1646F#1P……………………………………\x02\x03",

            "#1648F………………努什么力呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x151,
        "#1653F咦？\x02",
    )

    CloseMessageWindow()

    def lambda_6D5():

        label("loc_6D5")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_6D5")

    QueueWorkItem2(0x151, 2, lambda_6D5)

    def lambda_6E6():
        OP_8E(0xFE, 0xFFFFFFC4, 0xFA0, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E6)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(300)

    ChrTalk(    #12
        0x103,
        (
            "#1646F#3P你啊，\x01",
            "一定还隐瞒了什么吧。\x02\x03",

            "你说你是第一次来王都。\x01",
            "可是你对这里的地形却很清楚。\x02\x03",

            "而且对于黑衣人的行动\x01",
            "也是相当了解的样子。\x02\x03",

            "#1648F……到底出于什么目的？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sleep(500)
    OP_44(0x151, 0x2)
    OP_8C(0x103, 135, 400)

    def lambda_7EB():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0x9B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7EB)
    WaitChrThread(0x103, 0x1)

    def lambda_80B():
        OP_8E(0xFE, 0x7F8, 0xFA0, 0x9B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_80B)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #13
        0x103,
        (
            "#1646F好像并不只是单纯地\x01",
            "想从黑衣人眼皮下逃走。\x02\x03",

            "还特意提出了\x01",
            "『想要参观王都』这样的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 500)
    Sleep(300)

    ChrTalk(    #14
        0x103,
        "#1648F你究竟是在打什么主意？\x02",
    )

    CloseMessageWindow()

    def lambda_8D3():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0x9B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D3)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    def lambda_8F8():
        OP_6D(2120, 4000, 3940, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8F8)

    def lambda_910():
        OP_6B(2700, 1500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_910)

    def lambda_920():
        OP_6C(50000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_920)
    OP_8C(0x103, 0, 400)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #15
        0x103,
        "#1648F#4P……答案呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x151,
        "#1656F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#1646F#4P…………委托以信用为第一。\x02\x03",

            "情况都不说清楚，\x01",
            "是无法让人接受委托的。\x02\x03",

            "#1642F所谓遗产之类的，\x01",
            "其实只是谎言对吧？\x02\x03",

            "从逃跑的时候……\x01",
            "不，从你刚来协会的时候\x01",
            "我就觉得有点不对劲。\x02\x03",

            "#1648F……说啊。\x01",
            "为什么要撒谎……？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)

    ChrTalk(    #18
        0x151,
        (
            "#1654F#5P这、这个…………\x02\x03",

            "遗产继承是真的……\x02\x03",

            "#1652F我、我…………\x01",
            "我想去格兰赛尔王城。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(200)
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #19
        0x151,
        (
            "#1652F#5P…………我是遗产继承人\x01",
            "这件事是千真万确的。\x02\x03",

            "但是，正式的继承手续\x01",
            "还没有办好。\x02\x03",

            "#1654F继承手续必须\x01",
            "要去格兰赛尔城的\x01",
            "行政区域提出办理才行…………\x02\x03",

            "但是那边的黑衣人相当多，\x01",
            "防守得很严密。\x02\x03",

            "#1656F因为继承的手续\x01",
            "我的亲戚们都知道……\x02\x03",

            "所以就……\x01",
            "……不让我接近王城………\x02\x03",

            "………………………………\x02\x03",

            "#1652F但是，我一定要一步一步接近才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x103,
        (
            "#1648F#4P……嗯………………\x02\x03",

            "好吧。\x01",
            "我暂且相信你。\x02\x03",

            "#1646F……为什么直到现在\x01",
            "才告诉我呢？\x02",
        )
    )

    Jump("loc_D3E")

    label("loc_D3E")

    CloseMessageWindow()

    ChrTalk(    #21
        0x151,
        (
            "#1656F#5P这………………\x02\x03",

            "#1655F这、这是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        (
            "#1646F#4P如果对我全盘托出，\x01",
            "那么我肯定会被金钱迷惑……\x02\x03",

            "只要正式手续还没有办好，\x01",
            "就有无数的机会。\x02\x03",

            "#1642F你认为我会\x01",
            "对遗产见财起意？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)

    ChrTalk(    #23
        0x103,
        (
            "#1644F#4P#3S你认为我就是\x01",
            "那样的人！？#2S\x02",
        )
    )

    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)

    ChrTalk(    #24
        0x151,
        "#1652F#3S#5P不、不是！！#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    Sleep(500)

    ChrTalk(    #25
        0x151,
        (
            "#1652F#5P……不是的。\x02\x03",

            "自从祖父过世之后\x01",
            "我就一直一个人生活。\x02\x03",

            "#1654F可是遗书公布之后，\x01",
            "就有许多人蜂拥而来。\x02\x03",

            "#1656F……就是像你说的那种\x01",
            "觊觎遗产的人。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F6D():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F6D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4152   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_2_108 end

    def Function_3_F8F(): pass

    label("Function_3_F8F")

    Sleep(1000)
    OP_8C(0x151, 0, 400)
    Sleep(300)

    def lambda_FA6():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_FA6)
    WaitChrThread(0x151, 0x1)

    def lambda_FC6():
        OP_8E(0xFE, 0xFFFFF164, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_FC6)
    WaitChrThread(0x151, 0x1)

    def lambda_FE6():
        OP_8E(0xFE, 0xFFFFF164, 0x7D0, 0x12C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_FE6)
    WaitChrThread(0x151, 0x1)

    def lambda_1006():
        OP_8E(0xFE, 0xFFFFFDA8, 0xFA0, 0x12C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1006)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_3_F8F end

    def Function_4_1021(): pass

    label("Function_4_1021")

    Sleep(5000)
    Return()

    # Function_4_1021 end

    def Function_5_1027(): pass

    label("Function_5_1027")

    OP_8C(0x151, 0, 400)
    Sleep(500)
    OP_8C(0x151, 180, 400)
    Sleep(500)
    OP_8C(0x151, 90, 400)
    Sleep(200)

    def lambda_1051():
        OP_8E(0xFE, 0x208, 0xFA0, 0x13B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1051)
    WaitChrThread(0x151, 0x1)

    def lambda_1071():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1071)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 180, 400)
    Return()

    # Function_5_1027 end

    def Function_6_1093(): pass

    label("Function_6_1093")


    def lambda_1099():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1099)
    WaitChrThread(0x103, 0x1)

    def lambda_10B9():
        OP_8E(0xFE, 0xFFFFF164, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10B9)
    WaitChrThread(0x103, 0x1)

    def lambda_10D9():
        OP_8E(0xFE, 0xFFFFF164, 0x7D0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10D9)
    WaitChrThread(0x103, 0x1)

    def lambda_10F9():
        OP_8E(0xFE, 0xFFFFFFC4, 0xFA0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10F9)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 180, 400)
    Return()

    # Function_6_1093 end

    def Function_7_111B(): pass

    label("Function_7_111B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2120, 4000, 3940, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x103, 1000, 4000, 2480, 0)
    SetChrPos(0x151, 1000, 4000, 3540, 180)

    def lambda_118C():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_118C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #26
        0x151,
        (
            "#1652F#5P为此我才委托了\x01",
            "值得信赖的人。\x02\x03",

            "我怎么可能\x01",
            "不相信你呢。\x02\x03",

            "#1656F……只不过………………\x02\x03",

            "#1655F参观王都的话是在撒谎。\x01",
            "……请原谅我的谎言。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x103)

    ChrTalk(    #27
        0x103,
        (
            "#1645F呼……………………\x01",
            "……………………没话可说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x151,
        "#1656F#5P………………嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        (
            "#1642F为什么\x01",
            "不一开始就说出来嘛。\x02\x03",

            "如果知道是这样的情况，\x01",
            "我们这边就会采取正式的护卫工作。\x02\x03",

            "只要藏在协会里面\x01",
            "就是最安全的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x151,
        (
            "#1653F#5P啊…………唔…………\x02\x03",

            "………………………………\x02\x03",

            "#1656F我还是……\x01",
            "……有些害怕……\x02\x03",

            "那天，我看到了。\x02\x03",

            "蜂拥而来的\x01",
            "那些人的眼睛……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x151, 0, 400)
    Sleep(300)

    def lambda_1437():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0x11BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1437)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #31
        0x151,
        (
            "#1654F#5P当宣读遗书的时候，\x01",
            "好多人的眼神瞬间就变了。\x02\x03",

            "那种疯狂，那种杀意……\x02\x03",

            "简直无法形容……\x01",
            "难以说清道明的感觉……\x02\x03",

            "并且转眼之间\x01",
            "就被掩饰得不留痕迹……\x02\x03",

            "但那种深藏着的眼神\x01",
            "是绝对抹消不了的。\x02\x03",

            "#1656F…………那一定是\x01",
            "人的本性。\x02\x03",

            "无论是谁，都会在某个地方\x01",
            "………………潜藏着残酷的一面。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #32
        0x151,
        (
            "#1654F#5P……这样的人，我害怕。\x02\x03",

            "所以我并不是\x01",
            "不相信游击士。\x02\x03",

            "#1656F而是，而是……\x02\x03",

            "……害怕………\x02\x03",

            "#1654F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x151, 180, 500)
    Sleep(300)

    ChrTalk(    #33
        0x151,
        (
            "#1652F#5P对、对不起！\x02\x03",

            "#1656F果然没有意义呢……\x01",
            "这样的委托……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        "#1646F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x151,
        (
            "#1656F#5P这、这个……\x02\x03",

            "#1655F雪拉扎德小姐，在您那么忙的时候\x01",
            "还把您卷入到这样的麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36 op#A
        0x151,
        "#1655F#5P#20A这个委托就…………\x02",
    )

    Sleep(2000)

    ChrTalk(    #37 op#A
        0x103,
        "#1646F#7A……我啊。\x02",
    )

    OP_59()

    ChrTalk(    #38
        0x151,
        "#1653F#5P………………咦？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)
    Sleep(300)

    ChrTalk(    #39
        0x103,
        (
            "#1646F我可是一个不管什么样的任务\x01",
            "都不会应付了事的人。\x02\x03",

            "……别把我看扁了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x151)
    Sleep(500)

    def lambda_185D():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_185D)
    WaitChrThread(0x151, 0x1)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 180, 400)
    Sleep(1000)

    def lambda_18A5():

        label("loc_18A5")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_18A5")

    QueueWorkItem2(0x151, 2, lambda_18A5)

    def lambda_18B6():
        OP_8F(0xFE, 0x794, 0xFA0, 0x9B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_18B6)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x103, 275, 400)
    Sleep(800)

    def lambda_18E2():
        OP_8F(0xFE, 0x3E8, 0xFA0, 0xDD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_18E2)
    WaitChrThread(0x151, 0x1)

    def lambda_1902():
        OP_8F(0xFE, 0xFFFFFFC4, 0xFA0, 0x9B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1902)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x103, 95, 400)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_63(0x103)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        "\x18\x07\x0C应该道歉的，其实是我。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #41
        "\x18\x07\x0C我想正大光明地挺起胸膛生活。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x18\x07\x0C这种心情并不是一时心血来潮，\x01",
            "而且之前我一直都在拼尽全力。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #43
        "\x18\x07\x0C不过还是有一些不一样。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x18\x07\x0C我………再次感受到了。\x01",
            "我想正大光明地挺起胸膛生活。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x18\x07\x0C……所以，这个任务\x01",
            "我会坚持到最后，圆满完成。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x2507)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_111B end

    SaveToFile()

Try(main)
