from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4221   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '奥利维特皇子',                         # 9
        '穆拉少校',                             # 10
        '奥斯本宰相',                           # 11
        '水壶',                                 # 12
        '红茶',                                 # 13
        '红茶',                                 # 14
        '目标用照相机',                         # 15
        '',                                     # 16
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
        'ED6_DT27/CH03260 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT27/CH03950 ._CH',             # 02
        'ED6_DT27/CH03263 ._CH',             # 03
        'ED6_DT26/CH20804 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03260P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT27/CH03950P._CP',             # 02
        'ED6_DT27/CH03263P._CP',             # 03
        'ED6_DT26/CH20804P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
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
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        "Function_0_1BA",          # 00, 0
        "Function_1_202",          # 01, 1
        "Function_2_20C",          # 02, 2
        "Function_3_1260",         # 03, 3
        "Function_4_22B8",         # 04, 4
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1E5")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_201")

    label("loc_1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_201")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_201")

    Return()

    # Function_0_1BA end

    def Function_1_202(): pass

    label("Function_1_202")

    OP_B1("t4221_n")
    Return()

    # Function_1_202 end

    def Function_2_20C(): pass

    label("Function_2_20C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 67000, 0, 7200, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 28000, 250, 53040, 90)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 30820, 300, 52900, 270)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x13, 29500, 300, 52600, 0)
    SetChrPos(0x14, 29900, 300, 53140, 0)
    SetChrPos(0x15, 28900, 300, 53140, 0)
    OP_6D(84260, 0, 8440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)

    def lambda_311():
        OP_6D(68220, 0, 8440, 8000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_311)

    def lambda_329():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_329)

    def lambda_339():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_339)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Sleep(500)

    def lambda_35D():
        OP_6D(67820, 0, 18440, 6000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_35D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x16, 0xFF)
    OP_6D(37490, 0, 59950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_3C1():
        OP_6D(31190, 0, 54740, 5000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_3C1)

    def lambda_3D9():
        OP_67(0, 5160, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3D9)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x12,
        (
            "#1485F#11P……呼。\x02\x03",

            "女王陛下不愧是\x01",
            "红茶的爱好者啊。\x02\x03",

            "香气、温度、味道……\x01",
            "每一项都无可挑剔。\x02\x03",

            "#1480F呵呵，就算我是喜好咖啡，\x01",
            "也希望能天天喝到这样的好茶啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#1551F#6P……虽然我也同意你的意见，\x01",
            "不过还是赶快进入正题吧。\x02\x03",

            "#1542F你到底想和我说什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x12,
        (
            "#1485F#11P呵呵……\x02\x03",

            "#1481F看来在利贝尔的这段时间\x01",
            "对殿下来说\x01",
            "还真是有非同一般的意义啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#1543F#6P……什么……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x12,
        (
            "#1480F#11P以前见面的时候，\x01",
            "您给我的印象就是\x01",
            "一个十分灵活聪明的人……\x02\x03",

            "不过现在的殿下\x01",
            "更添了几分坚强。\x02\x03",

            "#1485F想必陛下也会为此感到高兴吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#1545F#6P呵呵，这么说的话，\x01",
            "阁下才是一如既往的大胆呢。\x02\x03",

            "#1540F不，应该说是气势\x01",
            "比以前更有压迫感了呢。\x02\x03",

            "#1541F是因为不满足当前吞并的领土面积,\x01",
            "因而怀恨在心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        (
            "#1481F#11P呵呵，真是不客气啊。\x02\x03",

            "#1485F不过，如果可以的话\x01",
            "希望您使用『合并』这个词。\x02\x03",

            "自从『百日战役』以来，\x01",
            "帝国军队还从来没有过\x01",
            "侵略其它国家的行为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#1545F#6P的确如此。\x02\x03",

            "#1540F──至少在表面看来是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x12,
        "#1483F#11P……呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#1544F#6P被合并的小国和自治州\x01",
            "各自都存在着或多或少的问题。\x02\x03",

            "#1542F然后问题会逐渐激化，\x01",
            "随之而来的就是猎兵团的入侵，\x01",
            "使社会治安极度恶化……\x02\x03",

            "然后受到穷困的当地政府邀请，\x01",
            "帝国军队前往介入，\x01",
            "接着便不明不白地决定合并。\x02\x03",

            "#1551F这一过程简直如出一辙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12,
        (
            "#1480F#11P唔，\x01",
            "的确有这样的共通之处。\x02\x03",

            "#1485F但是这也是动荡的时代\x01",
            "所产生的必然吧。\x02\x03",

            "说到底，帝国军队也只不过是\x01",
            "为了祖国而尽可能采取措施\x01",
            "实现周边地区的安定而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#1540F#6P这一点的确非常出色。\x02\x03",

            "#1541F不过……\x01",
            "我还是有些在意情报局的人员\x01",
            "被过多地派往周边地区的情况呢。\x02\x03",

            "而且，被派去的时机\x01",
            "居然是在问题激化之前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        (
            "#1485F#11P呵呵，\x01",
            "我并不想知道您是从哪里\x01",
            "得到的这样的情报。\x02\x03",

            "#1481F这是为了贯彻危机管理的思想。\x02\x03",

            "正因为如此，\x01",
            "之前的数次事件\x01",
            "才能够防范于未然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#1544F#6P这是以周边地区的怨恨\x01",
            "以及遭受恐怖袭击的危险为代价的啊。\x02\x03",

            "#1542F老实说，\x01",
            "我现在还有些不敢相信\x01",
            "你会这样独自来访利贝尔。\x02\x03",

            "现在的埃雷波尼亚，\x01",
            "最容易成为恐怖袭击目标的\x01",
            "恐怕就是你了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        (
            "#1485F#11P呵呵，不敢当。\x02\x03",

            "#1480F不过，请放心。\x02\x03",

            "托优秀部下的福，\x01",
            "应付恐怖活动的对策万无一失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1543F#6P优秀部下……\x02\x01",

            "#1542F是说那个雷克特吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#1485F#11P呵呵，虽然他是个奇怪的人，\x01",
            "不过工作做得相当出色。\x02\x03",

            "从这次日程的调整到对恐怖分子的防范\x01",
            "都是他一手包办的。\x02\x03",

            "#1480F因此一会儿我也能够安心地\x01",
            "前往克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #17
        0x10,
        "#1543F#6P#3S什么……！？\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "#1480F#11P我接下来的预定是要与\x01",
            "克洛斯贝尔的代表进行机密会谈。\x02\x03",

            "最近因为共和国的资金流入，\x01",
            "感觉有些被对抗势力压制住的倾向。\x02\x03",

            "#1485F反正那里也是我早就想去的地方，\x01",
            "就趁此机会拜访一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1550F#6P怎、怎么可以……\x02\x03",

            "#1544F现在的克洛斯贝尔\x01",
            "正处于错综复杂的各国势力支配中！\x02\x03",

            "缓冲地带暂且不说，\x01",
            "那里正在成为恐怖组织\x01",
            "和犯罪组织的温床……\x02\x03",

            "#1542F就算是非正式访问，\x01",
            "帝国宰相前往那种地方也太……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12,
        (
            "#1481F#11P这么说的话，\x01",
            "殿下您不也是一样吗。\x02\x03",

            "登上那个浮游都市，\x01",
            "圆满完成视察任务\x01",
            "顺利回到地面。\x02\x03",

            "#1485F呵呵，\x01",
            "与您做的事情相比，\x01",
            "我去访问克洛斯贝尔如同儿戏一般。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#1542F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "#1480F#11P现在在国内\x01",
            "大家都把殿下当成英雄看待。\x02\x03",

            "殿下乘坐号称『洁白之翼』的\x01",
            "『埃尔赛尤号』回归帝都。\x02\x03",

            "与以『帝国时报社』为首的\x01",
            "各方面联络也万无一失……\x02\x03",

            "#1485F您所期待的华丽凯旋\x01",
            "一定会顺利进行吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#1549F#6P………哼………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        (
            "#1485F#11P呵呵，\x01",
            "您就尽量活用这次机会，\x01",
            "稳固自己的立足之地吧。\x02\x03",

            "#1481F殿下，\x01",
            "我对您可是抱有很大的期望啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1239():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1239)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_20C end

    def Function_3_1260(): pass

    label("Function_3_1260")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 67000, 0, 7200, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 28000, 250, 53040, 90)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 30820, 300, 52900, 270)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x13, 29500, 300, 52600, 0)
    SetChrPos(0x14, 29900, 300, 53140, 0)
    SetChrPos(0x15, 28900, 300, 53140, 0)
    OP_6D(31190, 0, 54740, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_1365():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1365)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Sleep(500)

    ChrTalk(    #25
        0x10,
        (
            "#1542F#6P……期望吗。\x02\x03",

            "#1545F哈哈………\x01",
            "这还真是出乎意料啊。\x02\x03",

            "#1540F我还以为你肯定只是\x01",
            "特地来找碴的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x12,
        (
            "#1483F#11P怎么会呢……\x01",
            "为什么会有这样的想法？\x02\x03",

            "#1481F我与殿下您\x01",
            "本来就是站在同一个立场上的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x10,
        "#1543F#6P什么……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrPos(0x12, 30820, 300, 53040, 270)
    OP_6D(37270, 0, 54090, 0)
    OP_67(0, 5370, -26010, 0)
    OP_6B(1800, 0)
    OP_6C(82000, 0)
    OP_6E(190, 0)

    def lambda_150D():
        OP_6B(1600, 36000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_150D)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #28
        0x12,
        (
            "#1484F#5P……殿下。\x01",
            "你本来应该是相当憎恨\x01",
            "埃雷波尼亚这个旧帝国的。\x02\x03",

            "憎恨这个由多数贵族所支配，\x01",
            "被愚蠢的陈规陋习\x01",
            "所束缚的旧体制。\x02\x03",

            "#1481F我说的没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#1542F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "#1480F#5P虽说我被大家尊称为\x01",
            "『铁血宰相』……\x02\x03",

            "但是我在帝国的立场\x01",
            "还并不够稳固。\x02\x03",

            "#1485F虽然我在帝都有很多支持者，\x01",
            "但在诸侯依旧有着深重影响的地方上\x01",
            "支持率还远远不够。\x02\x03",

            "就算是在公认很有影响力的帝国军中，\x01",
            "也只不过是七成的程度……\x02\x03",

            "剩下的都在诸侯支配之下，\x01",
            "如果再加上他们自己的私设军队，\x01",
            "恐怕形势就要完全逆转了。\x02\x03",

            "#1481F……我现在也只是处在\x01",
            "围绕帝国主导权的争夺\x01",
            "激战正酣的风头浪尖上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1551F#6P所以才在帝国全境铺设了铁路网，\x01",
            "为各地注入新鲜血液……\x02\x03",

            "并通过扩张领土\x01",
            "获得新的发言权吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        (
            "#1485F#5P呵呵，\x01",
            "您不愧是最了解我的人啊。\x02\x03",

            "#1482F我再说一次──\x01",
            "请协助我吧，殿下。\x02\x03",

            "如果得到您的协助，\x01",
            "我的改革就会如虎添翼。\x02\x03",

            "这样一来\x01",
            "腐败的贵族势力来不及\x01",
            "互相勾结就会土崩瓦解……\x02\x03",

            "#1485F──这也是您\x01",
            "最希望看到的事情吧。\x02",
        )
    )

    Jump("loc_1933")

    label("loc_1933")

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#1551F#6P…………………………………\x02\x03",

            "#1542F……宰相。\x01",
            "我只想问一句话。\x02\x03",

            "『结社』和你究竟有什么关系？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x12,
        (
            "#1485F#5P呵呵，您在说什么，\x01",
            "我完全不明白……\x02\x03",

            "#1481F不过，\x01",
            "为了改革而利用一切可利用的要素……\x02\x03",

            "这是我的政治理念。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#1541F#6P……我明白了。\x01",
            "我们的确很合得来。\x02\x03",

            "#1540F但正因为如此……\x01",
            "我拒绝你的邀请。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x12,
        "#1483F#5P哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#1551F#6P腐败的贵族势力\x01",
            "的确不合我的胃口……\x02\x03",

            "不，正如你所说的，\x01",
            "应该是十分憎恨他们吧。\x02\x03",

            "#1542F但是……比起这个来，\x01",
            "你的做法更让我感到可怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        "#1480F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1540F#6P恐怕你是要通过\x01",
            "制造某种幻想，\x01",
            "而让整个国家陷入一种狂热之中吧。\x02\x03",

            "在这种狂热之中，\x01",
            "旧势力的确没有生存空间。\x02\x03",

            "#1551F但是……只要齿轮开始转动\x01",
            "就无法再停下来了。\x02\x03",

            "它会把一切都卷入其中……\x01",
            "毫无界限地成长下去吧。\x02\x03",

            "#1542F……宰相。\x01",
            "你明白这一点吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x12,
        (
            "#1486F#5P哈哈，那是当然。\x02\x03",

            "#1481F──因为这只不过是\x01",
            "我改革的第一阶段。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x10,
        "#1549F#6P………哼……………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_44(0x16, 0xFF)
    OP_6D(31190, 0, 54740, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x12, 30820, 300, 52900, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #42
        0x12,
        (
            "#1485F#11P以后的事情……\x01",
            "如果殿下愿意和我携手的话，\x01",
            "请随时来告诉我。\x02\x03",

            "#1480F在您想通之前，\x01",
            "就请稳固自己的立足之地吧。\x02\x03",

            "……为此大概需要\x01",
            "先驯服那些你所厌恶的\x01",
            "贵族势力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#1545F#6P哼……\x01",
            "都被你看透了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_43(0x10, 0x3, 0x0, 0x4)
    Sleep(1200)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x12,
        (
            "#1485F#11P是正午的钟声……\x01",
            "船也该快到了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrPos(0x12, 30540, 0, 52900, 270)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(500)

    def lambda_1F76():
        OP_6D(31500, 0, 54300, 1500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1F76)

    def lambda_1F8E():
        OP_8E(0xFE, 0x774C, 0x0, 0xC8C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F8E)
    SetChrSubChip(0x10, 2)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 400)
    Sleep(500)

    ChrTalk(    #45
        0x12,
        (
            "#1480F#11P──那么，殿下。\x01",
            "我就先行一步了。\x02\x03",

            "#1485F两个星期之后……\x01",
            "我们在帝都再见吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x12, 90, 400)

    def lambda_2035():
        OP_6D(34750, 0, 54160, 3000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2035)

    def lambda_204D():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_204D)

    def lambda_205D():
        OP_8E(0xFE, 0x8818, 0x0, 0xC800, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_205D)
    Sleep(800)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x12, 0x1)

    def lambda_2094():
        OP_8E(0xFE, 0x87F0, 0x0, 0xC418, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2094)
    WaitChrThread(0x12, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_20BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_20BE)

    def lambda_20D0():
        OP_8E(0xFE, 0x87F0, 0x0, 0xBD74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20D0)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 34800, 0, 48500, 0)

    def lambda_2125():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2125)

    def lambda_2137():
        OP_8E(0xFE, 0x8746, 0x0, 0xC62A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2137)
    WaitChrThread(0x11, 0x1)

    def lambda_2157():
        OP_6D(30890, 0, 55120, 4000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2157)

    def lambda_216F():
        OP_8E(0xFE, 0x7CE2, 0x0, 0xD41C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_216F)
    WaitChrThread(0x11, 0x1)

    def lambda_218F():
        OP_8E(0xFE, 0x774C, 0x0, 0xD41C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_218F)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x10, 400)
    OP_63(0x10)
    Sleep(500)
    WaitChrThread(0x16, 0x0)

    ChrTalk(    #46
        0x11,
        (
            "#276F#5P谈话结束了吧。\x02\x03",

            "#270F……怎么了？\x01",
            "看你的表情这么疲劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#1544F#6P不，没事……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#1540F#6P我只是——\x01",
            "再次体会到了自己所面对的\x01",
            "是怎样的一个怪物而已。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2296():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2296)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1260 end

    def Function_4_22B8(): pass

    label("Function_4_22B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22CE")
    OP_22(0xB5, 0x0, 0x5A)
    Sleep(2500)
    Jump("Function_4_22B8")

    label("loc_22CE")

    Return()

    # Function_4_22B8 end

    SaveToFile()

Try(main)
