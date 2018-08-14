from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4144   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4144.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '艾莉卡博士',                           # 9
        '希德中校',                             # 10
        '雷克鲁斯方石',                         # 11
        '雷克鲁斯方石',                         # 12
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
        'ED6_DT27/CH03970 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT26/CH20607 ._CH',             # 02
        'ED6_DT26/CH20622 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03970P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT26/CH20607P._CP',             # 02
        'ED6_DT26/CH20622P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_17D",          # 01, 1
        "Function_2_17E",          # 02, 2
        "Function_3_91E",          # 03, 3
        "Function_4_2F9B",         # 04, 4
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_169")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_17C")

    label("loc_169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_17C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_17C")

    Return()

    # Function_0_14A end

    def Function_1_17D(): pass

    label("Function_1_17D")

    Return()

    # Function_1_17D end

    def Function_2_17E(): pass

    label("Function_2_17E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x109, -280, 0, 310, 0)
    SetChrPos(0x11, 460, 0, -2310, 0)
    SetChrPos(0x10, -780, 0, -1580, 0)
    OP_6D(-1630, -1000, 27520, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(44000, 0)
    OP_6E(354, 0)

    def lambda_20F():
        OP_6B(7650, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20F)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C8(0x200, 0x46, "C_PLAC31._CH", 0x0, 0x3E8)

    def lambda_23E():
        OP_8E(0xFE, 0xFFFFFFBA, 0xFFFFFC18, 0x4722, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23E)
    Sleep(50)

    def lambda_25E():
        OP_8E(0xFE, 0xFFFFFD30, 0xFFFFFC18, 0x3FAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_25E)
    Sleep(100)

    def lambda_27E():
        OP_8E(0xFE, 0x262, 0xFFFFFC18, 0x3F34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_27E)
    WaitChrThread(0x109, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_6D(1280, -1000, 18410, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(226, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10,
        "#1459F#6P这、这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        (
            "#703F#4P令人惊讶……\x02\x03",

            "#701F没想到大圣堂地下\x01",
            "还会有这样的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)

    ChrTalk(    #2
        0x109,
        (
            "#1060F#5P简而言之，\x01",
            "此处是根据利贝尔王家\x01",
            "和七耀教会的盟约而建造的。\x02\x03",

            "#1065F修建这里的目的只有一个……\x02\x03",

            "#1063F抑制古代遗物的力量和机能，\x01",
            "防止其向外扩散。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#1457F#6P……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#701F#4P也就是与你们星杯骑士团的\x01",
            "使命有着直接关系的地方对吧。\x02\x03",

            "这么说来，在利贝尔之外也有\x01",
            "与此处相类似的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1075F#5P嗯，的确如此。\x02\x03",

            "#1060F我等将此地\x01",
            "称为『始源之地』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#1458F#6P『始源之地』……\x01",
            "实在是意味深长啊。\x02\x03",

            "#1456F归根究底，这里所参照的原型\x01",
            "还是在亚尔特利亚吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        "#1064F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#1450F#6P哎呀，猜中了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        (
            "#1066F#5P不……怎么说呢。\x02\x03",

            "我只是在想，真不愧是\x01",
            "拉赛尔博士的女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#1457F#6P请不要将我和\x01",
            "那个秃子相提并论。\x02\x03",

            "#1456F基础理论姑且不论，\x01",
            "应用工学方面我可是技高一筹。\x02\x03",

            "『卡佩尔』和『埃尔赛尤』的\x01",
            "基本系统可是\x01",
            "由我担任主设计的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1060F#5P哦～原来如此啊。\x02\x03",

            "#1064F……哦哦，\x01",
            "话题扯远了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    def lambda_74C():
        OP_6D(1480, -1000, 24030, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_74C)

    def lambda_764():
        OP_67(0, 5460, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_764)

    def lambda_77C():
        OP_6B(3850, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_77C)

    def lambda_78C():
        OP_6E(254, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_78C)
    WaitChrThread(0x10, 0x0)
    Sleep(800)

    def lambda_7A6():
        OP_6D(1840, -1000, 29250, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A6)

    def lambda_7BE():
        OP_67(0, 4570, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7BE)

    def lambda_7D6():
        OP_6B(3790, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7D6)

    def lambda_7E6():
        OP_6E(229, 4000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7E6)

    def lambda_7F6():
        OP_8E(0xFE, 0xFFFFFF10, 0xFFFFFC18, 0x6914, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F6)
    Sleep(150)

    def lambda_816():
        OP_8E(0xFE, 0xFFFFFC04, 0xFFFFFC18, 0x6194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_816)
    Sleep(300)

    def lambda_836():
        OP_8E(0xFE, 0x1C2, 0xFFFFFC18, 0x6252, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_836)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #12
        0x109,
        "#1063F#6P──这，就是那件东西吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#703F#4P嗯，没错──\x02\x03",

            "#700F三天前从浮游都市\x01",
            "沉没地点打捞上来的\x01",
            "类似古代遗物的东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0xBB8)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_17E end

    def Function_3_91E(): pass

    label("Function_3_91E")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x109, -240, -1000, 26900, 0)
    SetChrPos(0x11, 450, -1000, 25170, 0)
    SetChrPos(0x10, -1020, -1000, 24980, 0)
    OP_DB(0x0, 0xE)
    OP_DC(0x2, 0xFF)
    OP_DC(0x1, 0x0, 0x8)
    OP_DC(0x1, 0x0, 0xE)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    Call(6, 9)
    ClearChrFlags(0x10F, 0x80)
    SetChrPos(0x10F, 240, -1000, 15420, 0)
    OP_A2(0x25D5)
    OP_6D(1930, -1000, 30500, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(4000, 0)
    OP_6B(3800, 0)
    OP_6C(45000, 0)
    OP_6E(229, 0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6P原来如此……\x01",
            "大致情况我已明白了。\x02\x03",

            "#1067F……可是这个东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1457F#6P嗯，如你所见。\x02\x03",

            "这个物体的\x01",
            "导力反应已经消失了。\x02\x03",

            "#1452F知道这意味着什么吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACE():
        OP_6D(1200, -1000, 27440, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ACE)

    def lambda_AE6():
        OP_67(0, 4650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AE6)

    def lambda_AFE():
        OP_6B(4000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AFE)

    def lambda_B0E():
        OP_6E(229, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B0E)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #16
        0x109,
        (
            "#1065F#5P失去了导力的古代遗物，\x01",
            "根据盟约而言是不在交还范围内的……\x02\x03",

            "#1060F原来如此，\x01",
            "我明白博士等我来的理由了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1456F#6P哼哼。\x01",
            "这样就不用我多费口舌了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#703F#4P实际上，导力反应是在\x01",
            "将要送到这个大圣堂之前才消失的。\x02\x03",

            "虽然暂时是存放在了这里，\x01",
            "但在没有正式达成交还意见之前，\x01",
            "所有权的归属问题并不明确。\x02\x03",

            "#700F那么……\x01",
            "这种情况下究竟应该怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1067F#5P……唔……\x01",
            "真是击中我的软肋了。\x02\x03",

            "#1063F作为利贝尔的代表，\x01",
            "你们是想得到此物的所有权吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#701F#4P此次为了见证,\x01",
            "我才随同一起来到了这里。\x02\x03",

            "也就是说提出这个主张的\x01",
            "正是艾莉卡博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#1450F#6P原本就是由中央工房在\x01",
            "沉没遗迹打捞的过程中发现的物品。\x02\x03",

            "理所当然具有这样的权利不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1065F#5P……失效的古代遗物\x01",
            "就完全成为了黑匣子。\x02\x03",

            "不管采用何种手段\x01",
            "也不可能进行分析的。\x02\x03",

            "#1840F即便如此也要将其保留吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#1450F#6P嗯，没错。\x02\x03",

            "#1457F请你设身处地的想一想。\x01",
            "这可是在那样的事件后留下的呢。\x02\x03",

            "我当时虽然没能亲身经历，\x01",
            "但我们的常识或多或少\x01",
            "已经被一样东西彻底颠覆了──\x02\x03",

            "#1452F──七耀教会历经千年\x01",
            "极尽所能掩盖的真相。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x109,
        "#1063F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#1453F#6P名为『噬身之蛇』的\x01",
            "不明身份的结社也是一样。\x02\x03",

            "越是听到关于他们的事情，\x01",
            "就越觉得他们的技术简直不可想象。\x02\x03",

            "#1457F真相究竟是怎样的，\x01",
            "又有什么样的事情会发生……\x02\x03",

            "包括我在内的大多数人\x01",
            "已不能再对其不闻不问了。\x02\x03",

            "#1459F正因如此，有了这样的线索\x01",
            "当然想要竭尽所能地进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1067F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #27
        0x11,
        (
            "#701F#2P博士，到此为止吧。\x02\x03",

            "对他个人进行追问\x01",
            "也不能解决问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "#1457F#6P……也是。\x02",
    )

    CloseMessageWindow()

    def lambda_11B9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_11B9)
    Sleep(400)

    ChrTalk(    #29
        0x10,
        (
            "#1450F#6P总之……\x01",
            "我们已经将事情说明了。\x02\x03",

            "这个古代遗物──\x01",
            "不，仅仅是个金属块。\x02\x03",

            "是交给我们，还是不交？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1067F#5P#40W………这………………\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    NpcTalk(    #31
        0x10F,
        "少女的声音",
        (
            "#1P『不盈一握之迷惘\x01",
            "  由此孕育出邪念──』\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1317():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1317)
    Sleep(100)
    OP_8C(0x11, 180, 400)
    OP_1D(0xB7)
    Fade(1000)
    OP_6D(0, -1000, 223790, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(180000, 0)
    OP_6E(294, 0)
    SetChrPos(0x10F, 0, -1000, 212020, 0)
    SetChrChipByIndex(0x10F, 2)
    SetChrSubChip(0x10F, 0)
    SetChrPos(0x109, -90, -1000, 227080, 180)
    SetChrPos(0x11, 610, -1000, 225560, 180)
    SetChrPos(0x10, -760, -1000, 225640, 180)

    def lambda_13C3():
        OP_6D(0, -1000, 211000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13C3)

    def lambda_13DB():
        OP_67(0, 3600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13DB)

    def lambda_13F3():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_13F3)

    def lambda_1403():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1403)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #32
        0x11,
        "#702F#5P！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "#1454F#5P这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1079F#5P（咦………………）\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #35
        0x10F,
        "身着修女服的少女",
        (
            "#1446F#5P『爬过旷野，翻越山丘，\x01",
            "  播撒灾厄于长空…………』\x02\x03",

            "──圣典第二节，\x01",
            "《被解放的灾厄》如是说……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)
    Sleep(200)
    SetChrSubChip(0x10F, 1)
    Sleep(200)
    SetChrSubChip(0x10F, 2)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_6D(1650, -1000, 210300, 0)
    OP_67(0, 4080, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(134000, 0)
    OP_6E(299, 0)

    def lambda_1586():
        OP_8E(0xFE, 0xFFFFFFE2, 0xFFFFFC18, 0x3645C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1586)

    def lambda_15A1():
        OP_6D(1430, -1000, 222830, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15A1)

    def lambda_15B9():
        OP_67(0, 4350, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15B9)

    def lambda_15D1():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15D1)

    def lambda_15E1():
        OP_6E(320, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_15E1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    NpcTalk(    #36
        0x10F,
        "身着修女服的少女",
        (
            "#1440F#11P格拉汉姆阁下，我迟来了一步。\x02\x03",

            "七耀教会星杯骑士团所属\x01",
            "随从骑士莉丝·亚尔珍特。\x02\x03",

            "以后还请您多加指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        "#1064F#5P#6P………………………（目瞪口呆）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "#1452F#6P……又突然出现了个怪人。\x02\x03",

            "#1454F等、等一下，你……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #39
        0x10F,
        "#1444F#11P…………怎么了？\x02",
    )

    CloseMessageWindow()
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xBB8)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #40
        0x10,
        (
            "#1830F#6P唔……\x01",
            "骗不了我的！\x02\x03",

            "就算你这个样子\x01",
            "也不要想蒙骗我!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        "#1802F#11P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "#1457F#6P可、可怕的星杯骑士团……\x02\x03",

            "竟然派了这样的少女来\x01",
            "想要挫我方的锐气……\x02\x03",

            "#1834F不、不过！\x01",
            "我也有坚强的后盾哟！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #43
        0x10,
        "#1455F#6P#4S好好看看这个吧！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)
    OP_AD(0x240102, 0x96, 0x78, 0x1F4)
    Sleep(1500)
    OP_8C(0x11, 270, 400)
    SetMessageWindowPos(100, 60, -1, -1)
    SetChrName("希德中校")

    AnonymousTalk(    #44
        "\x07\x00#702F博士，这是……\x02",
    )

    Jump("loc_1920")

    label("loc_1920")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(70, 300, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(    #45
        "\x07\x00#1064F提妲的照片？\x02",
    )

    Jump("loc_1960")

    label("loc_1960")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("莉丝修女")

    AnonymousTalk(    #46
        "\x07\x00#1442F…………真可爱。\x02",
    )

    Jump("loc_19A4")

    label("loc_19A4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x10,
        (
            "#1834F#6P你刚才说了真可爱吧！？\x01",
            "你说了真可爱对吧！？\x02\x03",

            "#1831F对吧，对吧！\x01",
            "这娇小玲珑的脸蛋\x01",
            "真是太让人喜欢了！\x02\x03",

            "嗯～果然没错，\x01",
            "可爱之人必然知晓可爱之处所在！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 90, 600)
    Sleep(400)
    OP_8C(0x10, 0, 600)
    Sleep(400)
    OP_8C(0x10, 90, 600)
    OP_8C(0x10, 180, 600)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#1457F#6P咳咳，因此……\x02\x03",

            "#1452F不论你有多么可爱，\x01",
            "对于已经有了免疫力的我\x01",
            "是无效的，明白吗?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10F,
        (
            "#1802F#11P请问……\x01",
            "刚才您所说的话\x01",
            "我不太明白。\x02\x03",

            "可爱……\x01",
            "说的是我吗？\x02",
        )
    )

    Jump("loc_1BF1")

    label("loc_1BF1")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #50
        0x10,
        "#1451F#6P#4S那是当然！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #51
        0x10,
        (
            "#1831F#6P清冷秀美\x01",
            "却透着童稚的姣好容颜！\x02\x03",

            "将出浴少女般\x01",
            "柔嫩欲滴的玉体轻裹\x01",
            "的修女装！\x02\x03",

            "哇，这是何等的杀伤力呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        "#1805F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x10,
        (
            "#1836F#6P呼……\x01",
            "这样不对吧～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        (
            "#1446F#11P……格拉汉姆阁下。\x01",
            "请问这两位是？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D72():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D72)
    Sleep(100)

    ChrTalk(    #55
        0x109,
        (
            "#1064F#6P啊、啊啊……\x02\x03",

            "#1065F他们是中央工房的\x01",
            "艾莉卡·拉赛尔博士和\x01",
            "王国军的希德中校。\x02\x03",

            "#1063F不过，你为什么\x01",
            "称呼我格拉汉姆阁下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10F,
        (
            "#1440F#11P原来如此……\x01",
            "是遗物发现者的代表。\x02\x03",

            "#1446F……辛苦你们了。\x01",
            "接下来的事情就交给我们吧。\x02\x03",

            "还请你们将其归还。\x01",
            "（点头）\x02",
        )
    )

    Jump("loc_1EBD")

    label("loc_1EBD")

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "#1454F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        "#702F#5P什么……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #59
        0x109,
        (
            "#1064F#6P等、等等！\x01",
            "怎么能擅自就这样决定了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10F,
        (
            "#1446F#11P……只是为格拉汉姆阁下\x01",
            "省去一些不必要的工夫。\x02\x03",

            "#1443F即便已经完全失效，\x01",
            "却终究是和『七至宝』相关的遗物……\x02\x03",

            "怎么能轻易\x01",
            "交给普通人呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        "#1063F#6P这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#1458F#6P呼，哼哼～\x01",
            "真是伶牙俐齿啊。\x02\x03",

            "#1456F不过很可惜，\x01",
            "没有了盟约作为绝对的标准，\x01",
            "你们也就没有法律依据了对吧？\x02\x03",

            "是打算要无理取闹吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10F,
        (
            "#1447F#11P……说到没有法律依据\x01",
            "你们不也一样吗。\x02\x03",

            "#1448F如果以盟约为绝对标准，\x01",
            "那么失效的古代遗物\x01",
            "是谁也不能据为己有的。\x02\x03",

            "只能弃之不管。\x01",
            "除此之外，别无他法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#1459F#6P也就是说……\x01",
            "你们不但是要将其夺走\x01",
            "而且还不许我们有半点怨言？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10F,
        "#1446F#11P的确如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "#1457F#6P哼，很好……\x02",
    )

    CloseMessageWindow()

    def lambda_220A():
        OP_6D(1430, -1000, 223800, 800)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_220A)

    def lambda_2222():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2222)
    Sleep(100)
    OP_8C(0x11, 315, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #67
        0x10,
        (
            "#1455F#11P凯文·格拉汉姆！\x01",
            "你看该怎么办吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10F,
        "#1443F#11P……该怎么办？\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #69
        0x109,
        (
            "#1064F#6P我、我吗！？\x01",
            "怎么突然就把矛头指向了我……\x02\x03",

            "#1068F……说实话\x01",
            "我是非常希望将其回收。\x02\x03",

            "#1066F可是，在利贝尔\x01",
            "我得到了许多的协助。\x01",
            "不留情面的话也有些过意不去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#703F#5P呼，从双方的角度而言\x01",
            "都缺少了决定性的东西。\x02\x03",

            "#701F这可就麻烦了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x109,
        (
            "#1068F#6P我说中校……\x01",
            "你怎么一副事不关己的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x0)
    OP_22(0x15F, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x109,
        "#1064F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10F,
        "#1444F#11P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_C4(0x1, 0x400)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 180, 400)

    ChrTalk(    #74
        0x11,
        "#702F#5P怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "#1452F#6P你们俩……\x01",
            "为什么突然瞠目结舌了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        "#1067F#6P为、为什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10F,
        (
            "#1443F#11P……刚才的，\x01",
            "难道没有听到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#1459F#6P到底\x01",
            "听到了什么啊──\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 0, 400)
    Sleep(300)

    ChrTalk(    #79
        0x10,
        "#1454F#11P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_260B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_260B)
    Sleep(100)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #80
        0x10F,
        "#1444F#11P啊……\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xB8)
    LoadEffect(0x0, "map\\mp256_00.eff")
    LoadEffect(0x1, "map\\mp252_01.eff")
    LoadEffect(0x2, "map\\mp256_01.eff")
    OP_22(0x146, 0x1, 0x32)
    PlayEffect(0x2, 0x0, 0xFF, 0, 400, 230000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0, 400, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_E5(0x0, 0xA, 0x0, 262144)
    OP_E5(0x0, 0xA, 0x1, 262144)
    OP_E5(0x0, 0xA, 0x2, 262144)
    OP_E5(0x0, 0xA, 0x3, 262144)
    OP_E5(0x0, 0xA, 0x4, 262144)
    OP_E5(0x0, 0xA, 0x5, 262144)
    OP_E5(0x0, 0xA, 0x6, 262144)
    OP_E5(0x0, 0xA, 0x7, 262144)
    OP_E5(0x0, 0xA, 0x8, 262144)
    OP_E5(0x0, 0xA, 0x9, 262144)
    OP_E5(0x0, 0xA, 0xA, 262144)
    OP_E5(0x0, 0xB, 0x0, 262144)
    OP_E5(0x0, 0xB, 0x1, 262144)
    OP_E5(0x0, 0xB, 0x2, 262144)
    OP_E5(0x0, 0xB, 0x3, 262144)
    OP_E5(0x0, 0xB, 0x4, 262144)
    OP_E5(0x0, 0xB, 0x5, 262144)
    OP_E5(0x0, 0xB, 0x6, 262144)
    OP_E5(0x0, 0xB, 0x7, 262144)
    OP_E5(0x0, 0xB, 0x8, 262144)
    OP_E5(0x0, 0xB, 0x9, 262144)
    OP_E5(0x0, 0xB, 0xA, 262144)
    OP_E5(0x2, 0xA, 0x0, 700)
    OP_E5(0x2, 0xA, 0x1, 700)
    OP_E5(0x2, 0xA, 0x2, 700)
    OP_E5(0x2, 0xA, 0x3, 700)
    OP_E5(0x2, 0xA, 0x4, 700)
    OP_E5(0x2, 0xA, 0x5, 700)
    OP_E5(0x2, 0xA, 0x6, 700)
    OP_E5(0x2, 0xA, 0x7, 700)
    OP_E5(0x2, 0xA, 0x8, 700)
    OP_E5(0x2, 0xA, 0xA, 700)
    OP_E5(0x2, 0xB, 0x0, 700)
    OP_E5(0x2, 0xB, 0x1, 700)
    OP_E5(0x2, 0xB, 0x2, 700)
    OP_E5(0x2, 0xB, 0x3, 700)
    OP_E5(0x2, 0xB, 0x4, 700)
    OP_E5(0x2, 0xB, 0x5, 700)
    OP_E5(0x2, 0xB, 0x6, 700)
    OP_E5(0x2, 0xB, 0x7, 700)
    OP_E5(0x2, 0xB, 0x8, 700)
    OP_E5(0x2, 0xB, 0xA, 700)
    Sleep(1000)
    Fade(1000)
    OP_6D(-130, -1000, 30000, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(3870, 0)
    OP_6C(0, 0)
    OP_6E(208, 0)
    SetChrPos(0x109, -60, -1000, 25760, 0)
    SetChrPos(0x11, 670, -1000, 24300, 0)
    SetChrPos(0x10, -780, -1000, 23650, 0)
    SetChrPos(0x10F, -60, -1000, 20930, 0)

    def lambda_28C8():
        OP_6D(0, -1650, 32000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28C8)

    def lambda_28E0():
        OP_67(0, 7700, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28E0)

    def lambda_28F8():
        OP_6B(3080, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_28F8)

    def lambda_2908():
        OP_6E(176, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2908)
    Sleep(500)
    OP_B0(0xA, 0xF)
    OP_B0(0xB, 0xF)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x69)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x69)
    WaitChrThread(0x109, 0x0)
    OP_73(0xA)
    OP_73(0xB)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(1000)
    OP_B0(0xA, 0xF)
    OP_B0(0xB, 0xF)
    OP_6F(0xA, 105)
    OP_70(0xA, 0xB4)
    OP_6F(0xB, 105)
    OP_70(0xB, 0xB4)

    def lambda_2982():
        OP_6D(0, -1050, 34120, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2982)

    def lambda_299A():
        OP_67(0, 4700, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_299A)

    def lambda_29B2():
        OP_6B(2350, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_29B2)
    OP_73(0xA)
    OP_73(0xB)
    OP_71(0x200A, 0x0)
    ExitThread()
    OP_71(0x200B, 0x0)
    ExitThread()
    OP_6F(0xA, 181)
    OP_70(0xA, 0x12C)
    OP_6F(0xB, 181)
    OP_70(0xB, 0x12C)
    Sleep(300)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 1000, 230000, 30)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 1000, 30000, 30)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(300)
    OP_22(0xC9, 0x0, 0x64)
    PlayEffect(0x1, 0x2, 0x12, 0, 0, 0, 30, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x13, 0, 0, 0, 30, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #81
        0x11,
        "#702F#5P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#1455F#5P难、难以置信……\x02\x03",

            "导力反应明明已经\x01",
            "完全消失了的啊！？\x02\x03",

            "可是为什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10F,
        (
            "#1443F#5P………………………………\x02\x03",

            "#1446F……一锤定音了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x109,
        "#1065F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-2130, -1000, 28840, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(315000, 0)
    OP_6E(225, 0)
    OP_0D()

    def lambda_2BF5():
        OP_6D(-2050, -1000, 31170, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BF5)

    def lambda_2C0D():
        OP_8E(0xFE, 0x0, 0xFFFFFC18, 0x6DBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C0D)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #85
        0x109,
        (
            "#1063F#6P立方体的古代遗物……\x02\x03",

            "至今为止从未出现\x01",
            "也从未听说过的种类。\x02\x03",

            "那就将其命名为\x01",
            "『方石』吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_6F(0xA, 301)
    OP_70(0xA, 0x12D)
    OP_6F(0xB, 301)
    OP_70(0xB, 0x12D)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_22(0x8F, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x20)

    def lambda_2D34():
        OP_6D(-1950, -1000, 30670, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2D34)
    OP_0D()
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240105, 0xBE, 0x82, 0x1F4)
    Sleep(1500)
    OP_56(0x2)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1000)
    Sleep(1000)
    Fade(1000)
    OP_82(0x1, 0x2)
    OP_23(0xC9)
    OP_E5(0x2, 0xA, 0x0, 0)
    OP_E5(0x2, 0xA, 0x1, 0)
    OP_E5(0x2, 0xA, 0x2, 0)
    OP_E5(0x2, 0xA, 0x3, 0)
    OP_E5(0x2, 0xA, 0x4, 0)
    OP_E5(0x2, 0xA, 0x5, 0)
    OP_E5(0x2, 0xA, 0x6, 0)
    OP_E5(0x2, 0xA, 0x7, 0)
    OP_E5(0x2, 0xA, 0x8, 0)
    OP_E5(0x2, 0xA, 0xA, 0)
    OP_E5(0x2, 0xB, 0x0, 0)
    OP_E5(0x2, 0xB, 0x1, 0)
    OP_E5(0x2, 0xB, 0x2, 0)
    OP_E5(0x2, 0xB, 0x3, 0)
    OP_E5(0x2, 0xB, 0x4, 0)
    OP_E5(0x2, 0xB, 0x5, 0)
    OP_E5(0x2, 0xB, 0x6, 0)
    OP_E5(0x2, 0xB, 0x7, 0)
    OP_E5(0x2, 0xB, 0x8, 0)
    OP_E5(0x2, 0xB, 0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #86
        0x10,
        "#1454F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1065F#5P……………………………\x02",
    )

    CloseMessageWindow()

    def lambda_2E81():
        OP_6D(-2050, -1000, 28810, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2E81)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #88
        0x109,
        (
            "#1075F#11P希德中校……\x01",
            "艾莉卡·拉赛尔博士。\x02\x03",

            "谨遵盟约，以星杯骑士团\x01",
            "凯文·格拉汉姆之名\x01",
            "将该古代遗物予以回收。\x02\x03",

            "#1060F对两位以及与之相关的人员\x01",
            "致以诚挚的感谢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F63():
        OP_6B(4200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F63)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    OP_3E(0x328, 1)
    OP_44(0x109, 0x0)
    OP_A2(0x2505)
    Sleep(3000)
    NewScene("ED6_DT21/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_3_91E end

    def Function_4_2F9B(): pass

    label("Function_4_2F9B")

    OP_24(0x146, 0x28)
    Sleep(200)
    OP_24(0x146, 0x1E)
    Sleep(200)
    OP_24(0x146, 0x14)
    Sleep(200)
    OP_24(0x146, 0xA)
    Sleep(200)
    OP_24(0x146, 0x0)
    OP_23(0x146)
    Return()

    # Function_4_2F9B end

    SaveToFile()

Try(main)
