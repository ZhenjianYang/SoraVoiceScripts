from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E1210   ._SN',
        MapName             = 'event',
        Location            = 'E1210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '随从骑士玛卡斯',                       # 9
        '随从骑士塞萨尔',                       # 10
        '瑟尔纳特总长',                         # 11
        '随从骑士',                             # 12
        '随从骑士',                             # 13
        '随从骑士',                             # 14
        '',                                     # 15
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
        'ED6_DT26/CH20610 ._CH',             # 00
        'ED6_DT26/CH20744 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20610P._CP',             # 00
        'ED6_DT26/CH20744P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_19A",          # 01, 1
        "Function_2_1D8",          # 02, 2
        "Function_3_186E",         # 03, 3
        "Function_4_18C7",         # 04, 4
        "Function_5_2ACB",         # 05, 5
        "Function_6_2B18",         # 06, 6
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_18B")
    OP_A3(0x2505)
    Event(0, 4)
    Jump("loc_199")

    label("loc_18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_199")
    OP_A3(0x2504)
    Event(0, 2)

    label("loc_199")

    Return()

    # Function_0_17A end

    def Function_1_19A(): pass

    label("Function_1_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B3")

    OP_22(0x7A, 0x1, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7")
    OP_23(0x1C3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x7A)

    label("loc_1D7")

    Return()

    # Function_1_19A end

    def Function_2_1D8(): pass

    label("Function_2_1D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -160, 200, 6650, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -3150, 200, 6970, 315)
    SetChrPos(0x109, -210, 1500, -4500, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(4150, 0, 6650, 0)
    OP_67(0, 4870, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)

    def lambda_26F():

        label("loc_26F")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_26F")

    QueueWorkItem2(0x109, 3, lambda_26F)
    OP_76(0xFF, 0x7, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(500)

    def lambda_2C1():
        OP_6D(-30, 1500, 5630, 3500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2C1)

    def lambda_2D9():
        OP_67(0, 6180, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D9)

    def lambda_2F1():
        OP_6B(2600, 3500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2F1)

    def lambda_301():
        OP_6E(325, 3500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_301)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x0)
    SetChrSubChip(0x11, 1)
    Sleep(100)
    SetChrSubChip(0x10, 1)
    Sleep(150)

    ChrTalk(    #0
        0x11,
        (
            "#5P#100P格拉汉姆大人。\x01",
            "今天辛苦您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#5P#100P您辛苦了。\x02\x03",

            "这次的行动\x01",
            "做得十分干净利落。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F嗯，比平时要轻松，\x01",
            "真是让我松了一口气。\x02\x03",

            "#1066F唉～～\x01",
            "如果时间允许的话，\x01",
            "还能和有闲阶级的女士风花雪月一场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        "#5P#100P又说那样的话了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#5P#100P做事太过招摇的话，\x01",
            "可是会被总长盯上的哦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F是、是。\x01",
            "你们也太不懂开玩笑了。\x02\x03",

            "真不明白，\x01",
            "为什么你们两个会被分派到\x01",
            "像我这样随便的家伙身边。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#5P#100P呵呵……\x01",
            "毕竟，\x01",
            "您好歹也是个『守护骑士』啊。\x02\x03",

            "包括这部\x01",
            "『梅尔卡瓦』在内，\x01",
            "总不能没有相应的后援吧。\x02",
        )
    )

    Jump("loc_5B4")

    label("loc_5B4")

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#5P#100P随从骑士的人数\x01",
            "也比核定的数目要少很多了。\x02\x03",

            "要不，干脆趁这个机会\x01",
            "申请增加一些人手如何？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #8
        0x109,
        "凯文·格拉汉姆",
        (
            "#1068F要是那样做的话，\x01",
            "一个人行动时就更麻烦了啊。\x02\x03",

            "#1066F请容我回绝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#5P#100P真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#5P#100P您要是能让我们多做点活儿，\x01",
            "我们也会比较放心啊……\x02\x03",

            "半年前那件事也是，\x01",
            "除了帮忙搬运『盐之桩』之外，\x01",
            "我们什么忙也没帮上。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x109,
        "凯文·格拉汉姆",
        (
            "#1065F说到那玩意，\x01",
            "光是搬运也已经是很重大的任务啦……\x02\x03",

            "#1072F（要是随便行动，\x01",
            "  让那家伙警戒起来\x01",
            "  可就糟了啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "#5P#100P哎……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F不，没什么。\x02\x03",

            "#1060F——按照预定计划，\x01",
            "就这样回亚尔特利亚吧。\x02\x03",

            "明天……不，已经是今天了吗。\x01",
            "争取午后就能到达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#5P明白。\x02",
    )

    Jump("loc_8B0")

    label("loc_8B0")

    CloseMessageWindow()
    LoadEffect(0x0, "map\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4400, 1150, 6600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x11, 0)
    Sleep(50)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    Sleep(1000)

    NpcTalk(    #15
        0x109,
        "凯文·格拉汉姆",
        "#1063F从哪里来的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#5P亚尔特利亚——\x02\x03",

            "从瑟尔纳特总长那里\x01",
            "直接发来的联络。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x109,
        "凯文·格拉汉姆",
        (
            "#1064F哎，真的？\x02\x03",

            "#1068F（在这种时候，\x01",
            "  那个人发联络过来，\x01",
            "  肯定没什么好事啊……）\x02\x03",

            "#1060F没办法……接通吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 1)
    Sleep(150)

    ChrTalk(    #18
        0x11,
        "#5P#100P了解。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0)
    Sleep(150)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)

    def lambda_ABD():
        OP_6D(1250, 2000, 3510, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_ABD)

    def lambda_AD5():
        OP_67(0, 5340, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AD5)

    def lambda_AED():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_AED)

    def lambda_AFD():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_AFD)

    def lambda_B0D():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B0D)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    Sleep(300)
    OP_22(0x127, 0x0, 0x64)

    def lambda_B39():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B39)
    OP_73(0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0x0, 0x6, 0x1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #19
        (
            "\x07\x05哟，凯文。\x01",
            "辛苦了。\x02\x03",

            "情况如何？\x02",
        )
    )

    Jump("loc_BC1")

    label("loc_BC1")

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #20
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F#6P#100P啊啊，很顺利。\x02\x03",

            "猎物是『愚者挂坠』。\x02\x03",

            "虽然我感到了『蛇』的气息，\x01",
            "但恐怕只是他们可以随意割掉的尾巴而已。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #21
        (
            "\x07\x05是吗……\x01",
            "大致上和预计的一样。\x02\x03",

            "辛苦了。\x01",
            "回来后好好休息——\x01",
            "虽然我是想这么说。\x02",
        )
    )

    Jump("loc_CF2")

    label("loc_CF2")

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #22
        0x109,
        "凯文·格拉汉姆",
        "#1068F#6P#100P（果然来了……）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #23
        "\x07\x05哦？怎么了？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #24
        0x109,
        "凯文·格拉汉姆",
        (
            "#1061F#6P#100P没什么、没什么。\x01",
            "请继续。 \x02",
        )
    )

    Jump("loc_DB0")

    label("loc_DB0")

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #25
        (
            "\x07\x05嗯，虽然你刚刚完成任务，\x01",
            "现在就这么说有点对不住……\x02\x03",

            "不过……\x01",
            "有件事想拜托你。\x02",
        )
    )

    Jump("loc_E35")

    label("loc_E35")

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #26
        0x109,
        "凯文·格拉汉姆",
        (
            "#1065F#6P#100P唔……\x02\x03",

            "#1063F……和『异端』有关吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #27
        (
            "\x07\x05不，只是『回收物品』而已。\x02\x03",

            "那东西目前应该被暂时保管在\x01",
            "格兰赛尔大圣堂的地下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #28
        0x109,
        "凯文·格拉汉姆",
        (
            "#1063F#6P#100P格兰赛尔……！\x02\x03",

            "原来如此，\x01",
            "可能跟『环』有关吗……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #29
        (
            "\x07\x05可能性很高吧。\x02\x03",

            "怎样，能帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #30
        0x109,
        "凯文·格拉汉姆",
        (
            "#1065F#6P#100P……明白。\x02\x03",

            "#1060F这边还有护送的任务，\x01",
            "我就让『梅尔卡瓦』\x01",
            "直接回亚尔特利亚去吧。\x02\x03",

            "格兰赛尔我一个人去就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #31
        (
            "\x07\x05嗯，拜托你了。\x02\x03",

            "对了，关于这件事，\x01",
            "我还派了一个新的随从骑士过去。\x02\x03",

            "对你的新手下\x01",
            "可要好好关照哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    NpcTalk(    #32
        0x109,
        "凯文·格拉汉姆",
        (
            "#1064F#6P#100P等……\x01",
            "等一下！\x02\x03",

            "新手下……\x01",
            "怎么又这么突然就……！\x02",
        )
    )

    Jump("loc_11AB")

    label("loc_11AB")

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #33
        (
            "\x07\x05呵呵，\x01",
            "女神安排的机缘总是很唐突的。\x02\x03",

            "那个随从骑士的训练成绩很优秀，\x01",
            "应该不会拖你的后腿的。\x02\x03",

            "那么，祝你一路顺风。\x02",
        )
    )

    Jump("loc_1256")

    label("loc_1256")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0x0, 0x6, 0x0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #34
        0x109,
        "凯文·格拉汉姆",
        "#1064F#6P#100P………………（无语）\x02",
    )

    CloseMessageWindow()

    def lambda_12C4():
        OP_6D(-30, 1500, 5630, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_12C4)

    def lambda_12DC():
        OP_67(0, 6180, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12DC)

    def lambda_12F4():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_12F4)

    def lambda_1304():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1304)

    def lambda_1314():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1314)
    WaitChrThread(0x10, 0x0)
    SetChrSubChip(0x11, 1)
    Sleep(100)
    SetChrSubChip(0x10, 1)
    Sleep(150)

    ChrTalk(    #35
        0x11,
        (
            "#5P#100P哈哈……\x01",
            "那个，怎么说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#5P#100P不、不是挺好的嘛。\x01",
            "有新人要来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    NpcTalk(    #37
        0x109,
        "凯文·格拉汉姆",
        (
            "#1068F这算什么好事啊！\x02\x03",

            "#1067F唉，\x01",
            "那家伙还真是老样子……\x02\x03",

            "真想不明白，\x01",
            "她怎么能当上那小说的原型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "#5P#100P啊啊……\x01",
            "是那部《红耀石》对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#5P#100P咦，这样好吗？\x02\x03",

            "这样不是会把我们『骑士团』的存在\x01",
            "暴露给世间所知道……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #40
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F那么戏剧性的内容\x01",
            "反而会成为很好的障眼法。\x02\x03",

            "女主角最终还死掉了，\x01",
            "也可以适当地扰乱敌人的情报。\x02\x03",

            "#1068F……若是认得本人的话，\x01",
            "马上就会知道她根本不是\x01",
            "那种可以如此简单死掉的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        "#5P#100P哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "#5P#100P唉，算了。\x01",
            "对别人的评价就先到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #43
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F总之……\x01",
            "事情就是这样。\x02\x03",

            "这次的后续工作\x01",
            "就完全交给你们了。\x02\x03",

            "金钱的流向也清查一下为妙，\x01",
            "感觉他应该还有其它的隐藏账户。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#5P#100P原来如此……\x01",
            "一切包在我们身上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#5P#100P那我们这就\x01",
            "返回亚尔特利亚……\x02\x03",

            "您准备怎么办？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #46
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F嗯……\x01",
            "就找个合适的自治州降落吧。\x02\x03",

            "#1060F可以的话，\x01",
            "尽可能在有国际定期船出入的城市附近。\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #47
        0x10,
        "#5P#100P收到。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x10, 0)
    Sleep(150)

    ChrTalk(    #48
        0x10,
        (
            "#5P#100P哎呀……\x01",
            "差不多要天亮了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 2)
    Sleep(100)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_1D8 end

    def Function_3_186E(): pass

    label("Function_3_186E")


    def lambda_1874():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1874)
    OP_8F(0xFE, 0xFFFFFF74, 0x5DC, 0xFFFFFC5E, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_8F(0xFE, 0xFFFFFCE0, 0x7D0, 0x5AA, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFCAE, 0x7D0, 0xAE6, 0x7D0, 0x0)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_186E end

    def Function_4_18C7(): pass

    label("Function_4_18C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -160, 200, 6650, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -3150, 200, 6970, 315)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2920, 200, 6830, 45)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -100, 2200, 2400, 0)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    OP_43(0x12, 0x0, 0x0, 0x5)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_6F(0x0, 30)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_74(0x0, 0x6, 0x3)

    def lambda_1981():

        label("loc_1981")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_1981")

    QueueWorkItem2(0x13, 3, lambda_1981)
    OP_76(0x2, 0x0, 0x1, 0xFFFFFFFD, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x1, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFC, 0x0, 0x0, 0x0)
    OP_6D(4300, 0, 6750, 0)
    OP_67(0, 4870, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #49
        (
            "\x07\x00——原来如此。\x01",
            "我已经了解了大致的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_1D(0x76)
    FadeToBright(2000, 0)
    OP_6B(3090, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x12,
        (
            "#1824F#6P关于你打听的人物，\x01",
            "已经确认完毕了。\x02\x03",

            "奥利维特皇子。\x01",
            "穆拉·范德尔。\x02\x03",

            "金·瓦赛克。\x01",
            "乔丝特·卡普亚。\x02\x03",

            "艾丝蒂尔·布莱特。\x01",
            "约修亚·布莱特。\x02\x03",

            "#1820F──以上６人\x01",
            "已经确认平安归还。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #51
        (
            "\x07\x05是吗……那我就放心了。\x02\x03",

            "利贝尔国内的人\x01",
            "我已经确认过了……\x02\x03",

            "剩下的只有『蛇』的两个人，\x01",
            "不过，那边也不需要确认吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #52
        0x12,
        (
            "#1825F#6P呵呵，真有你的。\x02\x03",

            "#1822F不过……事发这么突然，\x01",
            "还真是难以置信啊。\x02\x03",

            "『影之国』──\x01",
            "至宝所留下的负面遗产吗。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #53
        (
            "\x07\x05嗯嗯……\x02\x03",

            "……不过，详细情况\x01",
            "等回去了之后再报告吧。\x02\x03",

            "善后处理似乎\x01",
            "也需要花点时间。\x02",
        )
    )

    Jump("loc_1D2E")

    label("loc_1D2E")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #54
        0x12,
        "#1825F#6P啊啊，那就拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0x0)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #55
        0x12,
        (
            "#1826F#6P……话说回来，\x01",
            "你给人的感觉好像不太一样了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #56
        "\x07\x05咦……\x02",
    )

    Jump("loc_1E17")

    label("loc_1E17")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #57
        0x12,
        (
            "#1825F#6P要是以前的你，\x01",
            "对相关人等的安危\x01",
            "可不至于这么关心。\x02\x03",

            "不……\x01",
            "应该说是刻意压抑自己的关心吧。\x02\x03",

            "#1820F看来在那什么『影之国』里\x01",
            "经历了不少事吧？\x02",
        )
    )

    Jump("loc_1ED0")

    label("loc_1ED0")

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #58
        (
            "\x07\x05哈哈……\x01",
            "说起经历还真是多到让人厌烦啊。\x02\x03",

            "包括这些在内，\x01",
            "都等我回去再报告吧。\x02\x03",

            "……我个人也有些事\x01",
            "想和总长谈谈。\x02",
        )
    )

    Jump("loc_1F7B")

    label("loc_1F7B")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #59
        0x12,
        (
            "#1823F#6P怎么，真是意味深长啊。\x02\x03",

            "#1825F不过，\x01",
            "能和莉丝一起平安归来比什么都好。\x02\x03",

            "#1821F等你们回来了，\x01",
            "我们三个一起去喝酒吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #60
        (
            "\x07\x05哈哈，真让人期待呢。\x02\x03",

            "……对了总长。\x01",
            "有件事想打听一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #61
        0x12,
        "#1820F#6P是什么？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #62
        (
            "\x07\x05嗯，那个……\x02\x03",

            "『守护骑士』的诨名\x01",
            "以后还能不能改啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x12, 0x96, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2114():
        OP_99(0xFE, 0x6, 0x9, 0x708)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2114)
    Sleep(500)

    ChrTalk(    #63
        0x12,
        "#1823F#6P…………啊……………？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #64
        (
            "\x07\x05其实除了『异端制裁』之外，\x01",
            "我还有些其它的事情想做……\x02\x03",

            "当然我依然会好好完成\x01",
            "守护骑士的任务的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x12, 0xFFFFFFCE, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)

    ChrTalk(    #65
        0x12,
        "#1825F#6P#40W……呼呼呼……哈哈哈……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(4300, 0, 6900, 0)
    ClearChrFlags(0x12, 0x800)
    ClearChrFlags(0x12, 0x1)
    SetChrPos(0x12, -250, 2000, 2600, 45)
    SetChrSubChip(0x12, 16)
    OP_0D()
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_44(0x13, 0x3)

    ChrTalk(    #66
        0x12,
        "#1827F#6P#4S哈哈哈哈哈哈哈哈哈哈！\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()

    def lambda_23A6():

        label("loc_23A6")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_23A6")

    QueueWorkItem2(0x13, 3, lambda_23A6)
    OP_62(0x13, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetChrSubChip(0x14, 1)
    Sleep(100)
    SetChrSubChip(0x13, 1)
    Sleep(150)

    ChrTalk(    #67
        0x14,
        "#2P总、总长……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #68
        (
            "\x07\x05唉……\x01",
            "果然是不行啊？\x02",
        )
    )

    Jump("loc_2467")

    label("loc_2467")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #69
        0x12,
        (
            "#1825F#6P呵呵呵……\x01",
            "守护骑士竟想改变\x01",
            "自己曾经取好的『诨名』吗。\x02\x03",

            "这在骑士团千年历史中\x01",
            "也是相当稀奇的事啊。\x02\x03",

            "#1821F……不过，并非没有先例。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #70
        "\x07\x05那么……\x02",
    )

    Jump("loc_256A")

    label("loc_256A")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #71
        0x12,
        (
            "#1826F#6P呵呵，\x01",
            "在下次见面之前，\x01",
            "你就想个更响亮的诨名吧。\x02\x03",

            "要是没想出来，\x01",
            "作为惩罚就让我来给你随便起个怪名字好了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #72
        (
            "\x07\x05怎么能这样，\x01",
            "这又不是什么惩罚游戏。\x02\x03",

            "算了，\x01",
            "我会努力想个酷一点的名字的。\x02\x03",

            "像『苍之流星』啦，\x01",
            "『黑色箭矢』什么的。\x02",
        )
    )

    Jump("loc_269C")

    label("loc_269C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Sleep(300)
    OP_62(0x13, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0xFFFFFF6A, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0xFFFFFE98, 2200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    OP_63(0x13)
    OP_63(0x14)
    OP_63(0x15)
    Sleep(500)
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #73
        "\x07\x05那、那个……我说错了什么话吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Sleep(300)

    ChrTalk(    #74
        0x12,
        (
            "#1824F#6P……凯文·格拉汉姆。\x02\x03",

            "#1821F作为你的原教官\x01",
            "我只给你一个忠告。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("凯文的声音")

    AnonymousTalk(    #75
        "\x07\x05哦……\x02",
    )

    Jump("loc_2844")

    label("loc_2844")

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_284D():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_284D)

    def lambda_285D():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_285D)
    FadeToDark(2000, 0, -1)
    OP_24(0x7A, 0x3C)
    Sleep(200)
    OP_24(0x7A, 0x32)
    Sleep(200)
    OP_24(0x7A, 0x28)
    Sleep(200)
    OP_24(0x7A, 0x1E)
    Sleep(200)
    OP_24(0x7A, 0x14)
    Sleep(200)
    OP_24(0x7A, 0xA)
    Sleep(200)
    OP_23(0x7A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    WaitChrThread(0xEE, 0x2)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #76
        (
            "\x07\x00如果你不想\x01",
            "今后丢更多丑的话……\x02\x03",

            "就不要说胡话了。\x01",
            "还是和莉丝商量一下再决定吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x1388)
    OP_21()
    Sleep(3000)
    OP_1D(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0x0, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS477._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x96, 0x78, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS478._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x7, 0, -320000, 7000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(2000)
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(3000)
    OP_56(0x2)
    OP_C6(0x0, 0x3, 16777215, 2500, 0)
    OP_C6(0x1, 0x3, 16777215, 3000, 0)
    Sleep(4000)
    OP_A2(0x2C27)
    OP_A2(0x2582)
    OP_C4(0x0, 0x10)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2502)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05保存通关数据吗？\x18\x02",
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_2A86")

    label("loc_2A86")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9F")
    OP_DC(0x0, 0x3)
    ShowSaveMenu()
    EventBegin(0x4)

    label("loc_2A9F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    FadeToDark(0, 0, -1)
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    Sleep(3000)
    OP_B4(0x1)
    Return()

    # Function_4_18C7 end

    def Function_5_2ACB(): pass

    label("Function_5_2ACB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B17")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Jump("Function_5_2ACB")

    label("loc_2B17")

    Return()

    # Function_5_2ACB end

    def Function_6_2B18(): pass

    label("Function_6_2B18")

    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    Return()

    # Function_6_2B18 end

    SaveToFile()

Try(main)
