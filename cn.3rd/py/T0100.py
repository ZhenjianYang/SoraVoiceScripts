from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100   ._SN',
        MapName             = 'rolent',
        Location            = 'T0100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '斯蒂娜',                               # 9
        '伊莉莎',                               # 10
        '克劳斯市长',                           # 11
        '目标用照相机',                         # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH02730 ._CH',             # 01
        'ED6_DT07/CH02350 ._CH',             # 02
        'ED6_DT26/CH20789 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH02730P._CP',             # 01
        'ED6_DT07/CH02350P._CP',             # 02
        'ED6_DT26/CH20789P._CP',             # 03
    )

    DeclNpc(
        X                   = -86130,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
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
        X                   = 82247,
        Z                   = 0,
        Y                   = 2548,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_1A7",          # 01, 1
        "Function_2_1C6",          # 02, 2
        "Function_3_27E",          # 03, 3
        "Function_4_BDD",          # 04, 4
        "Function_5_1E1B",         # 05, 5
        "Function_6_1E74",         # 06, 6
        "Function_7_1ECD",         # 07, 7
        "Function_8_1F33",         # 08, 8
        "Function_9_1FC0",         # 09, 9
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_175")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_1A6")

    label("loc_175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_194")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_1A6")

    label("loc_194")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1A6")

    Return()

    # Function_0_14A end

    def Function_1_1A7(): pass

    label("Function_1_1A7")

    OP_B1("T0100_n")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5")
    OP_71(0x42F, 0x0)
    ExitThread()
    OP_82(0x89, 0x0)

    label("loc_1C5")

    Return()

    # Function_1_1A7 end

    def Function_2_1C6(): pass

    label("Function_2_1C6")

    EventBegin(0x0)
    SetChrPos(0x0, 46140, 0, 20660, 270)
    OP_6D(39440, 250, 23160, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_21C():
        OP_6B(3850, 9000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21C)

    def lambda_22C():
        OP_6D(39440, 250, 23160, 9000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22C)

    def lambda_244():
        OP_6C(306000, 9000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_244)
    OP_77(0xFF, 0x92, 0x59, 0x0, 0xFA0)
    Sleep(4000)
    Sleep(2000)
    OP_77(0x40, 0x4C, 0xAA, 0x0, 0xBB8)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0101   ._SN", 100, 1, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_1C6 end

    def Function_3_27E(): pass

    label("Function_3_27E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00#40W翌日──\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_6D(49000, 0, 10440, 0)
    OP_67(0, 3280, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearParty()
    AddParty(0x54, 0xEE, 0xFF)
    SetChrPos(0x155, 49000, 0, -6000, 0)
    OP_1D(0xC0)

    def lambda_31D():
        OP_6D(49000, 0, 17020, 5000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_31D)

    def lambda_335():
        OP_67(0, 3780, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_335)
    FadeToBright(2000, 0)
    Sleep(1500)

    def lambda_35B():
        OP_8E(0xFE, 0xBF68, 0x0, 0x3BD8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_35B)
    WaitChrThread(0x155, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x155,
        (
            "#296F………………约修亚……\x02\x03",

            "居然连『灰银超大螳螂』\x01",
            "和『双海马』\x01",
            "都不能满足你……\x02\x03",

            "#292F不愧是我弟弟，\x01",
            "品味还真是高啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x155, 180, 400)
    Sleep(500)

    ChrTalk(    #2
        0x155,
        (
            "#290F#5P哼哼，\x01",
            "不过今天一定会让你满足的。\x02\x03",

            "#294F#3S……用『传说中的虫』！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(53920, 0, 19930, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(39000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 54450, 250, 18980, 270)
    OP_70(0x9, 0x1E)
    OP_73(0x9)

    def lambda_4EA():
        OP_8E(0xFE, 0xCAA8, 0x0, 0x4A24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EA)
    Sleep(1000)
    OP_72(0x9, 0x8)
    ExitThread()
    OP_6F(0x9, 30)
    OP_70(0x9, 0x0)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x155, 400)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_550():
        OP_6D(49180, 0, 17760, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_550)

    def lambda_568():
        OP_67(0, 4090, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_568)

    def lambda_580():
        OP_6C(347000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_580)

    def lambda_590():
        OP_8E(0xFE, 0xC364, 0x0, 0x4218, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_590)

    ChrTalk(    #3
        0x10,
        "#11P哎呀，这不是艾丝蒂尔吗！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x155, 0x10, 400)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #4
        0x10,
        (
            "#11P怎么了，\x01",
            "像个门神似的站在那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#11P今天也要去抓虫吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x155,
        (
            "#290F#6P嘿嘿，\x01",
            "今天的我可是大不相同了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        "#11P哎呀哎呀，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x155,
        (
            "#291F#6P嗯，没错。\x02\x03",

            "今天我要做特制的糖浆\x01",
            "把虫都引诱过来。\x02\x03",

            "只要用这种糖浆，\x01",
            "就会有很厉害的虫跑出来～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#11P哟，那可真是厉害呢～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "#11P……………………话说回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#11P艾丝蒂尔。\x01",
            "你已经１１岁啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#11P也该要有点\x01",
            "女孩的样子才行吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x155,
        (
            "#296F#6P但是，\x01",
            "不穿这衣服活动不方便嘛！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F2():

        label("loc_7F2")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_7F2")

    QueueWorkItem2(0x10, 2, lambda_7F2)

    def lambda_803():
        OP_8E(0xFE, 0xBF68, 0x0, 0x9218, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_803)

    ChrTalk(    #14 op#A
        0x155,
        "#291F#6P#10A拜拜——！\x02",
    )

    Sleep(1500)

    ChrTalk(    #15
        0x10,
        "#6P啊，艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x155, 0x1)
    Sleep(1000)

    ChrTalk(    #16
        0x10,
        "#6P唉，还是老样子……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(50100, 0, 41020, 0)
    OP_67(0, 6390, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(72000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, 49730, 0, 29510, 0)
    Sleep(1000)

    def lambda_8EA():
        OP_8E(0xFE, 0xC242, 0x0, 0x9FC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_8EA)
    WaitChrThread(0x155, 0x1)
    OP_8C(0x155, 300, 400)
    Sleep(300)

    ChrTalk(    #17
        0x155,
        (
            "#296F唔，\x01",
            "首先要收集糖浆的材料。\x02\x03",

            "#290F『巨龙咖啡豆』\x01",
            "可以拜托伊莉莎分给我……\x02\x03",

            "『新鲜牛奶』和『新鲜鸡蛋』\x01",
            "就去找缇欧要吧！\x02",
        )
    )

    Jump("loc_9AB")

    label("loc_9AB")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "先去找伊莉莎\x01",                            # 0
            "先去找缇欧\x01",                              # 1
            "保险起见，先去看看有没有新品运动鞋\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    SetMapFlags(0x2000000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB2")

    ChrTalk(    #18
        0x155,
        (
            "#291F好，\x01",
            "先去找伊莉莎吧。\x02\x03",

            "#290F伊莉莎……\x01",
            "还在帮店里做事吗？\x02",
        )
    )

    Jump("loc_A84")

    label("loc_A84")

    CloseMessageWindow()

    def lambda_A8B():
        OP_8E(0xFE, 0x8F7A, 0x0, 0x9FC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_A8B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 4)
    Jump("loc_BDC")

    label("loc_AB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B43")

    ChrTalk(    #19
        0x155,
        (
            "#290F新鲜的材料，\x01",
            "还是要找缇欧才行呢。\x02\x03",

            "#291F好，去农场吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B14():
        OP_8E(0xFE, 0x8F7A, 0x0, 0x9FC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_B14)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BDC")

    label("loc_B43")


    ChrTalk(    #20
        0x155,
        (
            "#296F嗯……保险起见……\x02\x03",

            "#291F先去看看\x01",
            "有没有新品运动鞋进货吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_BB3():
        OP_8E(0xFE, 0xC242, 0x0, 0x7346, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_BB3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T0121   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_BDC")

    Return()

    # Function_3_27E end

    def Function_4_BDD(): pass

    label("Function_4_BDD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 29540, 0, 46220, 0)
    OP_44(0x155, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_C5B")
    OP_6D(26620, 0, 45190, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, 22320, 0, 38470, 90)
    Jump("loc_CA9")

    label("loc_C5B")

    OP_6D(31120, 0, 46190, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, 41170, 0, 43630, 270)

    label("loc_CA9")


    def lambda_CAF():
        OP_6B(3090, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_CAF)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_1581")

    ChrTalk(    #21
        0x155,
        "#291F#2P伊莉莎～！！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_CF2():
        OP_6D(28900, 0, 46160, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_CF2)

    def lambda_D0A():
        OP_67(0, 7150, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D0A)

    def lambda_D22():
        OP_6C(317000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D22)

    def lambda_D32():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_D32)
    OP_43(0x155, 0x3, 0x0, 0x6)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D65():

        label("loc_D65")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_D65")

    QueueWorkItem2(0x11, 2, lambda_D65)
    WaitChrThread(0x155, 0x3)
    OP_44(0x11, 0x2)
    Sleep(300)

    ChrTalk(    #22
        0x11,
        "#11P啊，艾丝蒂尔～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#11P嘿嘿……昨天的约修亚，\x01",
            "真是好帅哦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#11P真希望\x01",
            "他能再吹口琴给我们听啊～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x155,
        (
            "#296F#6P这个嘛…………\x02\x03",

            "约修亚那家伙，\x01",
            "在那之后一句话都没说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "#11P咦！？　……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x155,
        (
            "#295F#6P嗯～………………\x02\x03",

            "是不是我拿了口琴\x01",
            "随便乱吹，\x01",
            "惹他不高兴了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x11,
        "#11P唉，艾丝蒂尔真是的……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #29
        0x11,
        "#11P……我说啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#11P虽然约修亚\x01",
            "什么也不肯告诉你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#11P但那一定是因为\x01",
            "他有过什么痛苦的经历哦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        "#11P所以啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x155,
        "#290F#6P…………嗯，我知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "#11P咦…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x155,
        (
            "#295F#6P约修亚一直在烦恼呢。\x01",
            "经常带着一副痛苦的表情。\x02\x03",

            "#295F……但是，\x01",
            "我大概帮不上他的忙。\x02\x03",

            "所以……………………\x02\x03",

            "#290F…………现在只能\x01",
            "让他打起精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#11P艾丝蒂尔…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)
    Sleep(500)

    ChrTalk(    #37
        0x155,
        (
            "#291F#6P……好，\x01",
            "那就给我『巨龙咖啡豆』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#11P咦，泡咖啡的那个？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#11P干嘛突然要这个～？\x01",
            "你要拿来干什么呀～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x155,
        "#290F#6P……保密。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x11,
        (
            "#11P每次艾丝蒂尔这样来要东西的时候，\x01",
            "绝对是有什么企图的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#11P唉，算了。\x01",
            "你等一下哦～。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x8)

    def lambda_127E():

        label("loc_127E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_127E")

    QueueWorkItem2(0x155, 2, lambda_127E)
    WaitChrThread(0x11, 0x3)
    OP_44(0x155, 0x2)
    Sleep(300)

    ChrTalk(    #43
        0x11,
        "#11P给，『巨龙咖啡豆』。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #44
        "\x07\x00得到了\x07\x02『巨龙咖啡豆』\x07\x00。\x02",
    )

    Jump("loc_12FA")

    label("loc_12FA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F61)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_1569")

    ChrTalk(    #45
        0x155,
        (
            "#290F#6P嗯，材料好像齐了。\x02\x03",

            "#292F好～，这样就…………\x02\x03",

            "……接下来……就去神秘森林\x01",
            "…………把那种虫给…………！\x02\x03",

            "#291F哼哼哼……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x11,
        (
            "#11P艾、艾丝蒂尔？\x01",
            "你在打什么鬼主意～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x155,
        (
            "#291F#6P待会儿也会给伊莉莎看的！\x02\x03",

            "#290F…………不过说不定\x01",
            "你会吓到晕倒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        "#11P…………那、那就免了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x155,
        "#291F#6P待会儿见～！\x02",
    )

    CloseMessageWindow()

    def lambda_14B6():

        label("loc_14B6")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_14B6")

    QueueWorkItem2(0x11, 2, lambda_14B6)

    def lambda_14C7():
        OP_8E(0xFE, 0x7F08, 0x0, 0xA334, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_14C7)
    WaitChrThread(0x155, 0x1)

    def lambda_14E7():
        OP_8E(0xFE, 0xB90A, 0x0, 0xA334, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_14E7)
    WaitChrThread(0x155, 0x1)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #50
        0x11,
        (
            "#5P不过……\x01",
            "还真有点想看。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_154D():
        OP_6B(2660, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_154D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 9)
    Jump("loc_157E")

    label("loc_1569")


    ChrTalk(    #51
        0x155,
        "#290F◆没有。\x02",
    )

    CloseMessageWindow()

    label("loc_157E")

    Jump("loc_1E1A")

    label("loc_1581")


    ChrTalk(    #52
        0x155,
        "#290F#1P伊莉莎～！！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_15A9():
        OP_6D(29570, 0, 47050, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_15A9)

    def lambda_15C1():
        OP_67(0, 7150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_15C1)

    def lambda_15D9():
        OP_6C(317000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_15D9)

    def lambda_15E9():
        OP_6B(2760, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_15E9)
    OP_43(0x155, 0x3, 0x0, 0x5)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_161C():

        label("loc_161C")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_161C")

    QueueWorkItem2(0x11, 2, lambda_161C)
    WaitChrThread(0x155, 0x3)
    OP_44(0x11, 0x2)
    Sleep(300)

    ChrTalk(    #53
        0x11,
        "#5P啊，艾丝蒂尔～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#5P嘿嘿……昨天的约修亚，\x01",
            "真是好帅哦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        (
            "#5P真希望\x01",
            "他能再吹口琴给我们听啊～……\x02",
        )
    )

    Jump("loc_16C5")

    label("loc_16C5")

    CloseMessageWindow()

    ChrTalk(    #56
        0x155,
        (
            "#296F#12P这个嘛…………\x02\x03",

            "约修亚那家伙，\x01",
            "在那之后一句话都没说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#5P咦！？　……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x155,
        (
            "#295F#12P嗯～………………\x02\x03",

            "是不是我拿了口琴\x01",
            "随便乱吹，\x01",
            "惹他不高兴了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x11,
        "#5P唉，艾丝蒂尔真是的……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #60
        0x11,
        "#5P……我说啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        (
            "#5P虽然约修亚\x01",
            "什么也不肯告诉你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        (
            "#5P但那一定是因为\x01",
            "他有过什么痛苦的经历哦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#5P所以啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x155,
        "#290F#12P…………嗯，我知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x11,
        "#5P咦…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x155,
        (
            "#295F#12P约修亚一直在烦恼呢。\x01",
            "经常带着一副痛苦的表情。\x02\x03",

            "#295F……但是，\x01",
            "我大概帮不上他的忙。\x02\x03",

            "所以……………………\x02\x03",

            "#290F…………现在只能\x01",
            "让他打起精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#5P艾丝蒂尔…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)
    Sleep(500)

    ChrTalk(    #68
        0x155,
        (
            "#291F#12P……好，\x01",
            "那就给我『巨龙咖啡豆』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        "#5P咦，泡咖啡的那个？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#5P干嘛突然要这个～？\x01",
            "你要拿来干什么呀～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x155,
        "#290F#12P……保密。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x11,
        (
            "#5P每次艾丝蒂尔这样来要东西的时候，\x01",
            "绝对是有什么企图的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#5P唉，算了。\x01",
            "你等一下哦～。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x7)

    def lambda_1B35():

        label("loc_1B35")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B35")

    QueueWorkItem2(0x155, 2, lambda_1B35)

    def lambda_1B46():
        OP_8F(0xFE, 0x7918, 0x0, 0xB0B8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1B46)
    WaitChrThread(0x155, 0x1)
    WaitChrThread(0x11, 0x3)
    OP_44(0x155, 0x2)
    Sleep(300)

    ChrTalk(    #74
        0x11,
        "#11P给，『巨龙咖啡豆』。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #75
        "\x07\x00得到了\x07\x02『巨龙咖啡豆』\x07\x00。\x02",
    )

    Jump("loc_1BD1")

    label("loc_1BD1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F61)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(    #76
        0x155,
        "#290F◆没有。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E1A")

    label("loc_1C08")


    ChrTalk(    #77
        0x155,
        (
            "#291F#6P好，接下来轮到缇欧了！\x02\x03",

            "#291F去找她要\x01",
            "『新鲜牛奶』和『新鲜鸡蛋』吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "#11P……我说艾丝蒂尔，\x01",
            "你在打什么鬼主意～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x155,
        (
            "#291F#6P哼哼…………\x01",
            "待会儿也会给伊莉莎看的！\x02\x03",

            "#290F…………不过说不定\x01",
            "你会吓到晕倒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x11,
        "#11P…………那、那就免了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x155,
        "#291F#6P待会儿见～！\x02",
    )

    CloseMessageWindow()

    def lambda_1D59():

        label("loc_1D59")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_1D59")

    QueueWorkItem2(0x11, 2, lambda_1D59)

    def lambda_1D6A():
        OP_8E(0xFE, 0x7918, 0x0, 0xA7E4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1D6A)
    WaitChrThread(0x155, 0x1)

    def lambda_1D8A():
        OP_8E(0xFE, 0x27A6, 0x0, 0xA7E4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1D8A)
    WaitChrThread(0x155, 0x1)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #82
        0x11,
        (
            "不过……\x01",
            "还真有点想看。\x02",
        )
    )

    Jump("loc_1DF2")

    label("loc_1DF2")

    CloseMessageWindow()

    def lambda_1DF9():
        OP_6B(2660, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1DF9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1E1A")

    Return()

    # Function_4_BDD end

    def Function_5_1E1B(): pass

    label("Function_5_1E1B")

    SetChrPos(0x155, 41930, 0, 42750, 270)

    def lambda_1E32():
        OP_8E(0xFE, 0x828C, 0x0, 0xA6FE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1E32)
    WaitChrThread(0x155, 0x1)

    def lambda_1E52():
        OP_8E(0xFE, 0x7954, 0x0, 0xB4A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1E52)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x11, 500)
    Return()

    # Function_5_1E1B end

    def Function_6_1E74(): pass

    label("Function_6_1E74")

    SetChrPos(0x155, 16329, 0, 41520, 90)

    def lambda_1E8B():
        OP_8E(0xFE, 0x7364, 0x0, 0xA230, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1E8B)
    WaitChrThread(0x155, 0x1)

    def lambda_1EAB():
        OP_8E(0xFE, 0x7364, 0x0, 0xAD98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1EAB)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x11, 500)
    Return()

    # Function_6_1E74 end

    def Function_7_1ECD(): pass

    label("Function_7_1ECD")


    def lambda_1ED3():
        OP_8E(0xFE, 0x7918, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1ED3)
    WaitChrThread(0x11, 0x1)

    def lambda_1EF3():
        OP_8E(0xFE, 0x7918, 0x1F4, 0xC81E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1EF3)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)

    def lambda_1F18():
        OP_8E(0xFE, 0x7918, 0x0, 0xB748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F18)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_7_1ECD end

    def Function_8_1F33(): pass

    label("Function_8_1F33")


    def lambda_1F39():
        OP_8E(0xFE, 0x7918, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F39)
    WaitChrThread(0x11, 0x1)

    def lambda_1F59():
        OP_8E(0xFE, 0x7918, 0x1F4, 0xC81E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F59)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)

    def lambda_1F7E():
        OP_8E(0xFE, 0x7918, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F7E)
    WaitChrThread(0x11, 0x1)

    def lambda_1F9E():
        OP_8E(0xFE, 0x7364, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F9E)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x155, 500)
    Return()

    # Function_8_1F33 end

    def Function_9_1FC0(): pass

    label("Function_9_1FC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x155, 32640, 0, 41530, 90)
    OP_6D(32640, 0, 41530, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_6A(0x155)

    def lambda_2023():
        OP_8E(0xFE, 0xD14C, 0x0, 0xA23A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2023)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x155, 0x1)
    Sleep(500)
    OP_6A(0xFF)
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)

    def lambda_206F():
        OP_8C(0xFE, 350, 200)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_206F)

    def lambda_207D():
        OP_6D(56000, 6000, 48460, 4000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_207D)

    def lambda_2095():
        OP_67(0, 4560, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2095)

    def lambda_20AD():
        OP_6C(35000, 4000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_20AD)

    def lambda_20BD():
        OP_6B(3440, 4000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_20BD)
    WaitChrThread(0x13, 0x0)
    Sleep(300)
    SetChrFlags(0x155, 0x4)
    SetChrPos(0x155, 53580, 3000, 41530, 350)

    ChrTalk(    #83
        0x155,
        (
            "#296F#5P………………………………\x02\x03",

            "稍微绕个路吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x155, 0x4)
    Fade(2000)
    OP_6D(55030, 0, 49600, 0)
    OP_67(0, 8730, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(119000, 0)
    OP_6E(243, 0)
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetChrPos(0x155, 51000, 0, 46100, 0)

    def lambda_219E():
        OP_8E(0xFE, 0xC738, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_219E)
    WaitChrThread(0x155, 0x1)

    def lambda_21BE():
        OP_8E(0xFE, 0xCD14, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_21BE)
    WaitChrThread(0x155, 0x1)
    OP_8C(0x155, 180, 400)
    Sleep(2000)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59400, 0, 46000, 180)

    def lambda_2200():
        OP_8E(0xFE, 0xE808, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2200)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 400)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #84
        0x12,
        (
            "#600F哦…………？\x02\x03",

            "这不是艾丝蒂尔吗。\x01",
            "怎么了？\x02",
        )
    )

    Jump("loc_2285")

    label("loc_2285")

    CloseMessageWindow()

    def lambda_228C():
        OP_8E(0xFE, 0xD41C, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_228C)
    OP_63(0x155)
    Sleep(200)
    TurnDirection(0x155, 0x12, 500)
    OP_62(0x155, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #85
        0x155,
        "#293F#12P啊，市长爷爷。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    OP_8C(0x155, 180, 400)
    Sleep(100)
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #86
        0x12,
        (
            "#602F#5P…………啊啊，那个钟楼啊。\x02\x03",

            "上个月修复工程已经完毕了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x155,
        "#296F#6P嗯，我知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        (
            "#600F#5P汇集了全洛连特的工匠。\x01",
            "这是大家智慧的结晶啊。\x02\x03",

            "建筑材料也尽量使用\x01",
            "和原来一样的东西。\x02\x03",

            "你看，\x01",
            "和以前没多大变化吧？\x02",
        )
    )

    Jump("loc_241B")

    label("loc_241B")

    CloseMessageWindow()

    ChrTalk(    #89
        0x155,
        (
            "#295F#6P………………嗯……\x02\x03",

            "虽然……\x01",
            "……我不太记得了……\x02",
        )
    )

    Jump("loc_2474")

    label("loc_2474")

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        (
            "#603F#5P………………………………\x02\x03",

            "#600F每当我看到这个钟楼，\x01",
            "就会变得精神十足。\x02\x03",

            "能感觉到洛连特的人民……\x02\x03",

            "不，是我至今为止\x01",
            "遇到的所有人，\x01",
            "都在支持这个城市……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x155,
        "#296F#6P………………嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        (
            "#603F#5P所以我……\x01",
            "觉得这里是非常宝贵的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x155,
        "#296F#6P………………嗯。\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x155)

    ChrTalk(    #94
        0x155,
        "#292F#6P…………好……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x155, 290, 500)

    ChrTalk(    #95
        0x155,
        (
            "#294F#5P等着吧，约修亚！！\x02\x03",

            "今天一定要抓到\x01",
            "『传说中的虫』！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2656():

        label("loc_2656")

        TurnDirection(0xFE, 0x155, 500)
        OP_48()
        Jump("loc_2656")

    QueueWorkItem2(0x12, 2, lambda_2656)

    ChrTalk(    #96
        0x12,
        (
            "#604F#5P……哦！？\x02\x03",

            "呃，艾丝蒂尔……？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x155,
        "#291F#5P#3SＧｏ—Ｇｏ—！！\x02",
    )

    CloseMessageWindow()

    def lambda_26CB():
        OP_8E(0xFE, 0xC8F0, 0x0, 0xC544, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_26CB)
    WaitChrThread(0x155, 0x1)

    def lambda_26EB():
        OP_8E(0xFE, 0xC8F0, 0x0, 0x9178, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_26EB)
    WaitChrThread(0x155, 0x1)
    Sleep(1000)

    ChrTalk(    #98
        0x12,
        "#600F#5P……哎…………？？？\x02",
    )

    CloseMessageWindow()

    def lambda_2739():
        OP_6B(3300, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2739)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x13, 0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/C0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1FC0 end

    SaveToFile()

Try(main)
