from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4163   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4163.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '达维尔大使',                           # 9
        '奥利维特皇子',                         # 10
        '穆拉少校',                             # 11
        '雷克特书记官',                         # 12
        '目标用照相机',                         # 13
        '',                                     # 14
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT27/CH03713 ._CH',             # 02
        'ED6_DT26/CH20805 ._CH',             # 03
        'ED6_DT07/CH00033 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT27/CH03713P._CP',             # 02
        'ED6_DT26/CH20805P._CP',             # 03
        'ED6_DT07/CH00033P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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


    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = 76130,
        TriggerRange        = 1000,
        ActorX              = 4970,
        ActorZ              = 1000,
        ActorY              = 76130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54740,
        TriggerZ            = 0,
        TriggerY            = 65190,
        TriggerRange        = 1000,
        ActorX              = 54740,
        ActorZ              = 1000,
        ActorY              = 65190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_22E",          # 02, 2
        "Function_3_1146",         # 03, 3
        "Function_4_2593",         # 04, 4
        "Function_5_26B9",         # 05, 5
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1E2")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1E2")

    Return()

    # Function_0_1BA end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5")
    OP_6F(0x17, 0)
    Jump("loc_1FC")

    label("loc_1F5")

    OP_6F(0x17, 60)

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E")
    OP_6F(0x18, 0)
    Jump("loc_215")

    label("loc_20E")

    OP_6F(0x18, 60)

    label("loc_215")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D")
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()

    label("loc_22D")

    Return()

    # Function_1_1E3 end

    def Function_2_22E(): pass

    label("Function_2_22E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00#40W自从利贝尔方舟崩坏已经一个月……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00#40W当格兰赛尔城举办的庆祝会过后，\x01",
            "以艾丝蒂尔为首的伙伴们\x01",
            "纷纷离开王都的时候……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x00#40W帝国大使馆的办公室内，\x01",
            "出现了奥利维尔，也就是\x01",
            "奥利维特·莱泽·亚诺尔的身影。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(1000, 0, 75500, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -4460, 0, 78260, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, -4600, 200, 71920, 180)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4460, 200, 68060, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5440, 0, 73080, 180)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName("男子的声音")

    AnonymousTalk(    #3
        (
            "没、没想到你是……\x02\x03",

            "不、不对！\x01",
            "您是奥利维特皇子殿下……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0x54)
    Sleep(500)

    def lambda_478():
        OP_6D(-2500, 0, 72000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_478)

    def lambda_490():
        OP_67(0, 4950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_490)

    def lambda_4A8():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4A8)

    def lambda_4B8():
        OP_6B(3128, 4000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4B8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x14, 0x0)
    Sleep(500)

    ChrTalk(    #4
        0x11,
        (
            "#030F#5P呵呵，你不记得身为庶出的\x01",
            "我的相貌也是正常的。\x02\x03",

            "我几乎不怎么在宫廷里露面，\x01",
            "在社交界内也是无人知晓……\x02\x03",

            "#031F是个至少对自己的发迹\x01",
            "完全派不上用场的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#1102F#12P哈、哈哈……请您别开玩笑……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#035F#5P哈哈，不必这么紧张。\x02\x03",

            "#030F话说回来，\x01",
            "我还要好好感谢大使您才行。\x02\x03",

            "#031F『稍微也表现出点帝国人的样子』、\x01",
            "『不要沉溺于玩乐赶快回国工作去吧』之类的，\x01",
            "您给了我各种各样的忠告呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x10,
        "#1103F#12P#3S哇……！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #8
        0x10,
        "#1101F#12P那、那是因为……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "#272F#5P……皇子，适可而止吧。\x02\x03",

            "#276F不管怎么说，\x01",
            "大使也只是按照常理来处理而已。\x02\x03",

            "反过来说，隐藏身份的我们\x01",
            "就算被责怪也是理所应当的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "#1100F#12P穆、穆拉君。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#031F#5P呵呵，没错……\x01",
            "那我就不再追究了。\x02\x03",

            "#030F其实这一个多月，\x01",
            "你的工作的确很出色。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x10,
        "#1101F#12P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#035F#5P与国内保持紧密联络，\x01",
            "保障侨居在此的帝国人的安全，\x01",
            "以及协助国际定期船重新展开运营。\x02\x03",

            "此外对其它方面的各类案件\x01",
            "也进行了妥善的处理。\x02\x03",

            "#030F真是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#1102F#12P实、实在不敢当……\x02\x03",

            "#1100F殿下您才是辛苦了，\x01",
            "竟然去担任了那样危险的视察工作。\x02\x03",

            "看来这次的事件在国内\x01",
            "也引起了相当大的骚动。\x02\x03",

            "在向他们传达危机已平息的消息后，\x01",
            "大家似乎都已经放下心来……\x02\x03",

            "#1102F这些也全都是拜殿下\x01",
            "英明决断所赐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#035F#5P哈哈……\x01",
            "你就别给我戴高帽子了。\x02\x03",

            "#030F我不过是在自己力所能及的范围内\x01",
            "做了些理所应当的事情而已。\x02\x03",

            "而且还不仅仅是靠自己的力量，\x01",
            "而是利用了周边的状况。\x02\x03",

            "#031F这么来看的话，\x01",
            "朴实刚健的帝国人气质\x01",
            "还是与我有天壤之别吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#1102F#12P哈哈……\x01",
            "虽然我也明白这么说有些失礼，\x01",
            "但实际的确是如此呢。\x02\x03",

            "#1100F不过关于这次的事件，\x01",
            "正是殿下灵活的想法\x01",
            "将结果引导到了好的方向。\x02\x03",

            "今后的帝国……\x01",
            "恐怕正是需要\x01",
            "像殿下这样的人啊。\x02\x03",

            "#1102F……采用与宰相大人\x01",
            "不同的处事方法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        "#276F#5P大使……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#033F#5P哦，\x01",
            "我还一直以为你肯定是\x01",
            "『铁血宰相』大人的支持者呢……\x02\x03",

            "#030F果然你是因为出身贵族，\x01",
            "所以才反对宰相大人的改革路线吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1102F#12P哈哈，虽说是贵族，\x01",
            "也只不过是不值一提的男爵而已。\x02\x03",

            "其实我基本上还是支持\x01",
            "奥斯本大人的改革路线的。\x02\x03",

            "#1100F只不过……\x01",
            "看来利贝尔这个国家\x01",
            "让我中毒太深了。\x02\x03",

            "有时候，我也会对\x01",
            "宰相大人的铁腕政策感到恐惧。\x02\x03",

            "#1102F到底……\x01",
            "他会将埃雷波尼亚这旧帝国\x01",
            "带向何方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#032F#5P……原来如此。\x02\x03",

            "#035F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#1100F#12P……殿下？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#035F#5P没什么，最后能与你\x01",
            "进行这么有意义的谈话真是太好了。\x02\x03",

            "#030F如果今后你也能为各国的和平作出贡献\x01",
            "那是再好不过的事情。\x02\x03",

            "#031F我还希望你能尽量和爱尔莎大使合作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#1102F#12P哈哈……\x01",
            "这真是给我出了一道难题啊。\x02\x03",

            "#1100F的确，自从签订了停战条约以来，\x01",
            "克洛斯贝尔问题还是首次出现\x01",
            "能够取得具体进展的曙光。\x02\x03",

            "既然倡导者是利贝尔，\x01",
            "那么我的任务就会比预想中还重要……\x02\x03",

            "#1102F您就是这个意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#031F#5P呵呵，\x01",
            "看来我白担心一场了。\x02\x03",

            "#030F这样一来我回帝都时\x01",
            "就可以毫无牵挂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#1102F#12P请放心交给我吧。\x02\x03",

            "#1100F我也很期待今后\x01",
            "殿下能够更为活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1127():
        OP_6B(2940, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1127)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    Call(0, 3)
    Return()

    # Function_2_22E end

    def Function_3_1146(): pass

    label("Function_3_1146")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-41290, 0, 15350, 0)
    OP_67(0, 4350, -10000, 0)
    OP_6B(5360, 0)
    OP_6C(35000, 0)
    OP_6E(164, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -64260, 0, 6540, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -52700, 0, 13800, 0)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -50940, 0, 13800, 270)

    def lambda_11F5():
        OP_6D(-50290, 0, 15350, 5000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_11F5)

    def lambda_120D():
        OP_6B(5160, 5000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_120D)

    def lambda_121D():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_121D)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    ChrTalk(    #26
        0x11,
        (
            "#035F#6P呵呵……\x01",
            "利贝尔这地方真是可怕啊。\x02\x03",

            "没想到竟然能从帝国贵族口中\x01",
            "听到这样的话呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        (
            "#277F#11P是啊，\x01",
            "我还以为他是个更加顽固的人呢。\x02\x03",

            "#278F这个国家的空气\x01",
            "的确拥有能使人改变的力量呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#030F#6P呵呵，\x01",
            "这么说来，你展现出\x01",
            "温柔表情的场合也变多了呢。\x02\x03",

            "#031F看起来不也是\x01",
            "受到了相当的影响吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "#278F#11P哼……\x01",
            "虽然这并不是我本来的意愿。\x02\x03",

            "#270F话说回来，\x01",
            "你才是应当多学习一下\x01",
            "这个国家的品位和规范啊。\x02\x03",

            "#274F真是的，\x01",
            "你就只有『灵活』这一点在无限延伸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#035F#6P呵呵，那个可以说是\x01",
            "我唯一的武器啊。\x02\x03",

            "#032F哪怕只有一点点可能，\x01",
            "也要与那个『铁血宰相』对抗的武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x12,
        "#276F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #32
        0x11,
        "#032F#6P……计划有没有生变？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x12,
        (
            "#270F#11P到现在为止都很顺利。\x02\x03",

            "#272F宰相阁下在三天前\x01",
            "出发到东部各州进行视察去了。\x02\x03",

            "利用这个时间差，\x01",
            "你明天乘坐『埃尔赛尤号』回归帝都。\x02\x03",

            "各方面的铺垫也都准备好了。\x02\x03",

            "#277F你这次的凯旋\x01",
            "一定会造成相当轰动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "#035F#6P阻碍因素呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "#272F#11P情报局的第四科\x01",
            "似乎有一些活动的样子。\x02\x03",

            "#276F不过因为有『埃尔赛尤号』的出动，\x01",
            "他们也许会慎重行事……\x02\x03",

            "#277F而且更有可能的是，\x01",
            "说不定这次回国在他们眼中\x01",
            "只是放荡皇子不值一提的表演而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#034F#6P实际上也的确如此～\x02\x03",

            "#030F不过，就算是表演，\x01",
            "也是别无他法，只能就此开始了。\x02\x03",

            "#031F那何不让我尽情\x01",
            "华丽地舞蹈一番呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x12,
        "#278F#11P……是啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -45500, -500, 10100, 270)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1840():
        OP_6D(-47780, 0, 13150, 1500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1840)

    def lambda_1858():
        OP_67(0, 3750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1858)

    def lambda_1870():
        OP_6C(58000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1870)

    def lambda_1880():

        label("loc_1880")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_1880")

    QueueWorkItem2(0x11, 2, lambda_1880)
    Sleep(50)

    def lambda_1896():

        label("loc_1896")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_1896")

    QueueWorkItem2(0x12, 2, lambda_1896)
    WaitChrThread(0x14, 0x0)
    Sleep(500)

    NpcTalk(    #38
        0x13,
        "青年的声音",
        (
            "#5P——皇子殿下。\x01",
            "抱歉在深夜前来打扰。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x13,
        "青年的声音",
        (
            "#5P因为收到了帝都方面发来的联络，\x01",
            "现在可以向您报告吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#030F#6P是吗……\x01",
            "知道了，请进来吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x13,
        "青年的声音",
        "#5P……失礼了。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_70(0x4, 0x3C)
    OP_73(0x4)

    def lambda_19A5():
        OP_6D(-48660, 0, 14480, 3500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_19A5)

    def lambda_19BD():
        OP_6C(62000, 3500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_19BD)
    SetChrPos(0x13, -44500, 0, 10000, 270)

    def lambda_19DE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_19DE)

    def lambda_19F0():
        OP_8E(0xFE, 0xFFFF4868, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_19F0)
    Sleep(1000)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x4, 0x0)
    WaitChrThread(0x13, 0x1)

    def lambda_1A2E():

        label("loc_1A2E")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A2E")

    QueueWorkItem2(0x13, 2, lambda_1A2E)

    def lambda_1A3F():
        OP_8E(0xFE, 0xFFFF3D50, 0x0, 0x3070, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1A3F)
    WaitChrThread(0x13, 0x1)
    OP_44(0x13, 0x2)
    WaitChrThread(0x14, 0x2)

    ChrTalk(    #42
        0x11,
        (
            "#031F#6P哎呀，雷克特。\x02\x03",

            "#030F今天你都没出现，\x01",
            "我还以为发生什么事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x13,
        (
            "#1885F#11P那是因为从早上开始\x01",
            "我就一直在进行各种联络业务。\x02\x03",

            "#1880F明天您就要出发了，\x01",
            "如果我再不来打声招呼的话\x01",
            "就太不懂礼貌了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#035F#6P呵呵，不用介意。\x02\x03",

            "#037F不过……干脆这样吧。\x01",
            "难得你来一次，\x01",
            "不如我们三人就这样亲密到早上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12,
        (
            "#270F#5P那么书记官。\x01",
            "帝都的联络是什么内容呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x13,
        (
            "#1884F#11P那边已经接到了\x01",
            "皇子殿下传达的命令。\x02\x03",

            "#1887F不过，从王都到帝都\x01",
            "只需要不到半天时间，\x01",
            "大大出乎了他们的意料……\x02\x03",

            "现在他们似乎在慌忙准备着\x01",
            "明天的庆典。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x12,
        (
            "#278F#5P原来如此，不愧是『埃尔赛尤号』，\x01",
            "速度的确让人难以想象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "#034F#6P呜呜……\x02\x03",

            "#030F唉，那个暂且不说，\x01",
            "舞台至少是已经准备好了。\x02\x03",

            "#031F呵呵，\x01",
            "那就为明天准备一件\x01",
            "让大家大吃一惊的衣服吧。\x02\x03",

            "#037F比如一块白色的兜档布，\x01",
            "再加上闪闪发光的外套怎么样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#274F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x13,
        (
            "#1881F#11P哈哈，\x01",
            "这还真是颇具冲击力啊。\x02\x03",

            "如果我能够同行的话，\x01",
            "一定得亲眼参观一下才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        "#276F#5P书记官……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "#031F#6P呵，你这么年轻，\x01",
            "却大有前途呢。\x02\x03",

            "#030F怎么样，雷克特。\x01",
            "和我一起乘坐\x01",
            "『埃尔赛尤号』回帝都怎么样？\x02\x03",

            "你在王国的工作\x01",
            "也差不多都完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x13,
        (
            "#1885F#11P哈哈……\x01",
            "虽然我也很向往『埃尔赛尤号』，\x01",
            "不过下一件工作还在等着我呢。\x02\x03",

            "#1887F您的美意\x01",
            "我只有心领了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#035F#6P哎呀，那还真是遗憾。\x02\x03",

            "#030F那你就努力去做好\x01",
            "『下一件工作』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x13,
        (
            "#1885F#11P谢谢。\x01",
            "那我这就告辞了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x13, 90, 400)
    Sleep(300)

    def lambda_2058():
        OP_6D(-47780, 0, 13150, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2058)

    def lambda_2070():
        OP_6C(58000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2070)

    def lambda_2080():
        OP_8F(0xFE, 0xFFFF4868, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2080)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 90, 400)
    Sleep(500)
    OP_71(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(500)

    def lambda_20C8():
        OP_8E(0xFE, 0xFFFF4E44, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_20C8)

    def lambda_20E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_20E3)
    WaitChrThread(0x13, 0x1)
    Sleep(300)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x4, 0x0)
    Sleep(1000)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)
    OP_8C(0x12, 135, 0)

    def lambda_212C():
        OP_6D(-50290, 0, 15350, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_212C)

    def lambda_2144():
        OP_67(0, 4350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2144)

    def lambda_215C():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_215C)
    Sleep(1000)
    TurnDirection(0x11, 0x12, 400)
    WaitChrThread(0x14, 0x0)
    Sleep(500)
    TurnDirection(0x12, 0x11, 400)
    Sleep(300)

    ChrTalk(    #56
        0x12,
        (
            "#272F#11P二等书记官，\x01",
            "雷克特·亚兰德尔。\x02\x03",

            "#276F……他果然是宰相的手下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        (
            "#031F#6P八成是这样的。\x02\x03",

            "#030F他徒步通过哈肯大门\x01",
            "来到大使馆赴任是在一个月前。\x02\x03",

            "与我们乘坐\x01",
            "『埃尔赛尤号』前往浮游都市\x01",
            "正好是同一时段。\x02\x03",

            "#035F怎么想这也不应该是偶然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "#272F#11P……是啊。\x02\x03",

            "#276F目前能想到的情况大概也就是\x01",
            "他是情报局派来的人而已……\x02\x03",

            "……这样好吗？\x01",
            "留着这样的人不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "#035F#6P那是另外一回事。\x01",
            "我也想知道\x01",
            "宰相大人的态度。\x02\x03",

            "#030F如果让他通报给宰相大人的话，\x01",
            "迟早他们会有所行动的。\x02\x03",

            "#031F在东部各州的视察结束后……\x01",
            "大概会在两个星期之后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x12,
        (
            "#278F#11P唔，原来是这么打算的吗。\x02\x03",

            "#277F我知道了，\x01",
            "那么我也按照这种情况做准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "#031F#6P嗯，那就拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #62
        0x11,
        "#033F#6P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#273F#11P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x11,
        (
            "#030F#6P没什么……\x01",
            "只是看到月亮出来了而已。\x02\x03",

            "#031F这满月真是漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2540():
        OP_6D(-49620, 0, 17860, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2540)

    def lambda_2558():
        OP_6B(5060, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2558)

    def lambda_2568():
        OP_6C(28000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2568)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_44(0x14, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1146 end

    def Function_4_2593(): pass

    label("Function_4_2593")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2678")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x611, 1)"), scpexpr(EXPR_END)), "loc_2607")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #65
        "\x07\x00得到了\x1F\x11\x06\x07\x00。\x02",
    )

    Jump("loc_25EC")

    label("loc_25EC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BE)
    Jump("loc_2675")

    label("loc_2607")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "宝箱里装有\x1F\x11\x06\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x11\x06\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2656")

    label("loc_2656")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_2675")

    Jump("loc_26AB")

    label("loc_2678")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #67
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_26AB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_2593 end

    def Function_5_26B9(): pass

    label("Function_5_26B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_272D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #68
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_2712")

    label("loc_2712")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BF)
    Jump("loc_279B")

    label("loc_272D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #69
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_277C")

    label("loc_277C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_279B")

    Jump("loc_27D1")

    label("loc_279E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_27D1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_26B9 end

    SaveToFile()

Try(main)
