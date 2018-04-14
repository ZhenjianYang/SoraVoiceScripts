from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0133_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0133_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
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
        "Function_1_3E9",          # 01, 1
        "Function_2_77C",          # 02, 2
        "Function_3_9F2",          # 03, 3
        "Function_4_1544",         # 04, 4
        "Function_5_1A48",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    ChrTalk(    #0
        0x101,
        "#1001F您好啊，潘杜爷爷。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        "#020F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1015F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05诉说了在寻找拉欧老人\x01",
            "所说的炖煮料理食谱的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #6
        0x101,
        (
            "#1011F潘杜爷爷和拉欧爷爷\x01",
            "的年龄似乎很接近啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#020F有关那个料理，\x01",
            "您知道些什么吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #8
        0xFE,
        (
            "嗯，年轻的时候\x01",
            "好像确实吃过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "不过我和那老小子不同，\x01",
            "对食物没有太大兴趣，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "直说好了，\x01",
            "已经完全没印象了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1016F啊，是那样啊。\x02\x03",

            "嗯，这可该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7")

    ChrTalk(    #12
        0x106,
        "#053F……白跑了一趟啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_333")

    label("loc_2A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D5")

    ChrTalk(    #13
        0x108,
        "#070F嗯，白跑了一趟啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_333")

    label("loc_2D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_306")

    ChrTalk(    #14
        0x104,
        (
            "#031F哈哈哈。\x01",
            "白跑了一趟呢\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333")

    label("loc_306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_333")

    ChrTalk(    #15
        0x105,
        "#045F看来……没有收获呢。\x02",
    )

    CloseMessageWindow()

    label("loc_333")


    ChrTalk(    #16
        0xFE,
        (
            "嗯，抱歉啊。\x01",
            "没帮上你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#525F您不用在意。\x01",
            "我们再去找别人打听就好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #18
        0xFE,
        (
            "那么你们就找城里的老婆婆\x01",
            "们多问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "在我们那个年代，\x01",
            "几乎谁都会做呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_28(0x75, 0x1, 0x100)
    Return()

    # Function_0_AA end

    def Function_1_3E9(): pass

    label("Function_1_3E9")

    EventBegin(0x0)
    Call(1, 5)

    ChrTalk(    #20
        0x24,
        "女神啊，拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x24,
        (
            "让我顺利接近那位\x01",
            "美丽的姐姐吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1015F#2P…………………………\x02\x03",

            "呼……\x01",
            "请问现在方便吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x24,
        "嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x24)

    ChrTalk(    #24
        0x24,
        "啊……难道！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x24,
        "你们……是协会的人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006F#2P嗯，正是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#020F我们看了委托，\x01",
            "您就是安敦先生吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x24,
        (
            "啊啊，请多关照，\x01",
            "我就是王都来的安敦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x24,
        (
            "虽然才刚见面，\x01",
            "不过委托很急，我就直说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x24,
        (
            "不是太困难的工作，\x01",
            "请你们一定要接受啊。\x02",
        )
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_612")

    ChrTalk(    #31
        0x101,
        (
            "#1000F#2P好，您说吧。\x02\x03",

            "究竟是什么事？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_779")

    label("loc_612")


    ChrTalk(    #32
        0x101,
        (
            "#1015F#2P啊，抱歉。\x02\x03",

            "马上开始的话\x01",
            "恐怕还不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x24,
        (
            "啊，果然…\x01",
            "我就知道会被拒绝。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x24, 180, 400)

    ChrTalk(    #34
        0x24,
        (
            "谁也不会听\x01",
            "我说话啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x24,
        (
            "以前也是……\x01",
            "以后也是。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x101,
        "#1016F#2P不、不用那么大反应啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#020F并没有拒绝啊，\x01",
            "不要误会。\x02\x03",

            "等我们有空时会回来，\x01",
            "请稍等一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x24,
        "说好话谁都会，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x24,
        (
            "算了，我等你们，\x01",
            "虽然也不抱什么希望。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x76, 0x1, 0x8000)

    label("loc_779")

    EventEnd(0x0)
    Return()

    # Function_1_3E9 end

    def Function_2_77C(): pass

    label("Function_2_77C")

    EventBegin(0x0)
    Call(1, 5)

    ChrTalk(    #40
        0x24,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x24,
        (
            "难道…\x01",
            "你们是游击士协会的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1002F#2P嗯……正是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x24,
        (
            "是吗……\x01",
            "你们回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x24,
        (
            "那么，愿意帮助我\x01",
            "这个不幸的人吗？\x02",
        )
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_927")

    ChrTalk(    #45
        0x101,
        "#1006F#2P嗯，好的。\x02",
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x24)

    ChrTalk(    #46
        0x24,
        "噢噢！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)

    ChrTalk(    #47
        0x24,
        (
            "呵，真的\x01",
            "你们愿意接受吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1016F#2P我、我们没有必要\x01",
            "对你说谎啊！！\x02\x03",

            "#1011F到底是什么委托啊？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_9EF")

    label("loc_927")


    ChrTalk(    #49
        0x101,
        (
            "#1007F#2P抱歉……\x01",
            "我们还有别的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x24,
        "呼～是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x24,
        (
            "果然，你们也是\x01",
            "无情的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1019F#2P……说什么啊。\x02\x03",

            "#1022F总之，等我们有空时\x01",
            "就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x24,
        (
            "算了，我等你们，\x01",
            "虽然也不抱什么希望。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EF")

    EventEnd(0x0)
    Return()

    # Function_2_77C end

    def Function_3_9F2(): pass

    label("Function_3_9F2")


    ChrTalk(    #54
        0x24,
        "嗯，其实…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x24,
        (
            "我希望你们替我\x01",
            "收集药的材料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x24,
        (
            "嗯……～？\x01",
            "这就是材料一览。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "\x07\x05魔兽甲壳　　　×５个\x01",
            "魔兽羽翼　　　×５个\x01",
            "魔兽之种　　　×５个\x01",
            "珍珠草　　　　×１条\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #58
        0x103,
        (
            "#025F魔兽的掉落物\x01",
            "倒还好说…\x02\x03",

            "……不过『珍珠草』\x01",
            "好像是鱼的一种吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x24,
        "嗯，是种很少见的鱼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x24,
        (
            "我想做的药材\x01",
            "需要那种鱼的肝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x24,
        (
            "听说在水草多的浅河中\x01",
            "可以钓到它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1015F#2P是吗……水草多的浅水河……\x02\x03",

            "#1006F#2P……好，记录完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x24,
        "啊，记录完毕？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x24,
        "……那么，接下来就拜托了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x24, 180, 400)

    ChrTalk(    #65
        0x101,
        "#1004F#2P啊、啊！？这就完了啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#022F请等一下！\x01",
            "我还有话要问。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)

    ChrTalk(    #67
        0x24,
        (
            "啊？什么？\x01",
            "已经说明的很清楚了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#027F你刚才\x01",
            "说是为了做药……\x02\x03",

            "究竟是什么药？\x01",
            "为什么目的而做？\x02\x03",

            "请把药的名称和使用目的\x01",
            "告诉我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x24,
        (
            "为、为什么非要\x01",
            "说那种事不可啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D64")

    ChrTalk(    #70
        0x106,
        (
            "#050F我们有义务\x01",
            "防止犯罪事件的发生。\x02\x03",

            "药品因使用方法的不同，\x01",
            "也可以用于毒品等途径呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71")

    label("loc_D64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC0")

    ChrTalk(    #71
        0x108,
        (
            "#070F并不是怀疑你，\x01",
            "但毕竟药是有危险的，\x02\x03",

            "请你配合一下，\x01",
            "告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71")

    label("loc_DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E16")

    ChrTalk(    #72
        0x104,
        (
            "#030F不管什么药\x01",
            "也都存在危险，\x02\x03",

            "为了防患于未然，\x01",
            "必须要问清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71")

    label("loc_E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E71")

    ChrTalk(    #73
        0x105,
        (
            "#040F不管是什么药，\x01",
            "用得不对也都有风险，\x02\x03",

            "保险起见，\x01",
            "我们必须确认一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E71")


    ChrTalk(    #74
        0x103,
        (
            "#020F嗯，就是那样了。\x02\x03",

            "所以请您\x01",
            "告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x24,
        (
            "呼，是吗。\x01",
            "算了，其实也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x24,
        (
            "我想做得药就是——\x01",
            "『千杯不醉的秘药』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x24,
        (
            "服下这种药之后，\x01",
            "不管怎么喝酒\x01",
            "也绝对不会醉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x24,
        (
            "这是教区长告诉我的，\x01",
            "所以绝对可信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1011F#2P嘿～好厉害的药啊。\x02\x03",

            "怎么喝酒也都\x01",
            "不会醉…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB7")

    ChrTalk(    #80
        0x104,
        "#032F哟哟……我很有兴趣啊。\x02",
    )

    CloseMessageWindow()

    label("loc_FB7")


    ChrTalk(    #81
        0x103,
        (
            "#023F什么啊。\x01",
            "好无聊的药。\x02\x03",

            "怎么喝也都不会醉，\x01",
            "那不就失去了喝酒的意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1015F#2P呼～雪拉姐的\x01",
            "喝酒方式也是不对的啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1073")

    ChrTalk(    #83
        0x107,
        (
            "#064F可是可是～你为什么\x01",
            "要做那种药呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_1073")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AA")

    ChrTalk(    #84
        0x105,
        (
            "#040F不过，为什么\x01",
            "要做那种药呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_10AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E3")

    ChrTalk(    #85
        0x108,
        (
            "#070F不过，你为什么\x01",
            "要做那种药呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_10E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1117")

    ChrTalk(    #86
        0x104,
        (
            "#030F不过，你为何\x01",
            "要做那种药呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(    #87
        0x106,
        (
            "#050F是想用在无法拒绝\x01",
            "的酒宴中吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F2")

    label("loc_1150")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #88
        0x104,
        (
            "#030F难道是有无法拒绝\x01",
            "的酒会吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F2")

    label("loc_1187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BE")

    ChrTalk(    #89
        0x108,
        (
            "#070F是因为有无法拒绝\x01",
            "的酒席吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F2")

    label("loc_11BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F2")

    ChrTalk(    #90
        0x105,
        (
            "#040F是因为有无法拒绝\x01",
            "的酒席吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F2")


    ChrTalk(    #91
        0x24,
        (
            "要说成无法拒绝的酒会倒是\x01",
            "不太准确…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x24,
        (
            "不过…确实也是场\x01",
            "无可避免的酒会啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x24,
        (
            "呼，所以无论如何\x01",
            "也需要那种药。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A3")

    ChrTalk(    #94
        0x104,
        (
            "#035F呼～那种心情……\x01",
            "我也深有体会啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A3")


    ChrTalk(    #95
        0x101,
        (
            "#1020F#2P但、但别喝太多，\x01",
            "不行吗？\x02\x03",

            "#1007F呼，还是适度\x01",
            "饮酒比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x103,
        "#025F呼，这话说得没错……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1344")
    TurnDirection(0x106, 0x103, 400)

    ChrTalk(    #97
        0x106,
        "#551F但是不该由你来说吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_1344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137E")
    TurnDirection(0x108, 0x103, 400)

    ChrTalk(    #98
        0x108,
        (
            "#073F喂喂……\x01",
            "你在说那个吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_137E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D5")
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #99
        0x104,
        (
            "#034F雪、雪拉……\x01",
            "你竟然说喝酒要适量……\x02\x03",

            "（真是不自觉啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D5")


    ChrTalk(    #100
        0x24,
        (
            "……委托的理由\x01",
            "你们现在都明白了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1414")
    OP_8C(0x106, 135, 400)
    Jump("loc_1441")

    label("loc_1414")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142C")
    OP_8C(0x108, 135, 400)
    Jump("loc_1441")

    label("loc_142C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1441")
    OP_8C(0x104, 135, 400)

    label("loc_1441")


    ChrTalk(    #101
        0x101,
        "#1002F#2P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x103,
        (
            "#020F……算可以了。\x02\x03",

            "那么，等材料收集完毕之后\x01",
            "我们会回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x24,
        "啊啊，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x24,
        (
            "那就交给你们了。\x01",
            "这可是关系到我将来的大事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1011F#2P？？？\x02\x03",

            "#1016F虽、虽然不懂……\x01",
            "不过我们会努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    OP_28(0x76, 0x4, 0x4)
    OP_28(0x76, 0x4, 0x8)
    OP_28(0x76, 0x1, 0x1)
    OP_28(0x76, 0x1, 0x2)
    OP_28(0x76, 0x1, 0x4)
    OP_8C(0x24, 180, 400)
    Return()

    # Function_3_9F2 end

    def Function_4_1544(): pass

    label("Function_4_1544")

    EventBegin(0x0)
    Call(1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_15E4")

    ChrTalk(    #106
        0x101,
        (
            "#1000F#2P那个～安敦先生，\x02\x03",

            "能再打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x24,
        "嗯……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)

    ChrTalk(    #108
        0x24,
        (
            "啊，游击士，\x01",
            "你们回来了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x24,
        (
            "啊，难道说…\x01",
            "药的材料都找到了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1658")

    label("loc_15E4")


    ChrTalk(    #110
        0x101,
        (
            "#1018F#2P哟！安敦先生，\x02\x03",

            "打扰一下可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x24,
        "嗯……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)

    ChrTalk(    #112
        0x24,
        "啊，各位游击士，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x24,
        "药的材料都找到了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1658")

    OP_61(0x101)

    ChrTalk(    #114
        0x101,
        "#1006F#2P嗯，确认一下吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #115
        "\x07\x05将材料拿给安敦看。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3AB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3BA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16FF")
    OP_28(0x76, 0x1, 0x1000)
    OP_3F(0x3A4, 5)
    OP_3F(0x39F, 5)
    OP_3F(0x3AB, 5)
    OP_3F(0x3BA, 1)

    label("loc_16FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A6")

    ChrTalk(    #116
        0x24,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x24,
        (
            "不好意思，\x01",
            "好像还没收集全啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#1004F#2P啊？是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x24,
        "啊啊，再确认一下笔记吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x24,
        (
            "那么，等材料收集完毕之后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x24, 180, 400)
    Jump("loc_1A45")

    label("loc_17A6")


    ChrTalk(    #121
        0x24,
        (
            "噢噢！！！\x01",
            "全部都收集到了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x24,
        (
            "太好了！\x01",
            "太感谢了！各位游击士！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x24,
        (
            "很好！！\x01",
            "那么马上去调制药吧！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x101,
        (
            "#1004F#2P啊……？\x02\x03",

            "我、我们也一起去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x24,
        (
            "啊啊，是你们帮我收集到材料的啊，\x01",
            "一定要一起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x24,
        (
            "来见证我\x01",
            "感动的瞬间吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1007F#2P虽、虽然完全\x01",
            "不明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        (
            "#020F嗯，没关系吧。\x02\x03",

            "不过都到了委托的最后环节，\x01",
            "还是去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_194E")

    ChrTalk(    #129
        0x106,
        "#051F啊啊，没有拒绝的理由啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19DE")

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197C")

    ChrTalk(    #130
        0x104,
        "#030F嗯，没理由拒绝啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19DE")

    label("loc_197C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AC")

    ChrTalk(    #131
        0x108,
        "#070F嗯，没有理由拒绝啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19DE")

    label("loc_19AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DE")

    ChrTalk(    #132
        0x105,
        (
            "#040F啊啊～也没有理由\x01",
            "拒绝啊…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DE")


    ChrTalk(    #133
        0x24,
        "很好，决定了！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x24,
        (
            "那么！！这就去找教区长吧！！\x01",
            "Ｌｅｔ＇ｓ　ｇｏ！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x76, 0x1, 0x2000)
    NewScene("ED6_DT21/T0130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A45")

    EventEnd(0x0)
    Return()

    # Function_4_1544 end

    def Function_5_1A48(): pass

    label("Function_5_1A48")

    Fade(1000)
    OP_4A(0x24, 255)
    SetChrPos(0x101, 54300, 10300, 45000, 135)
    SetChrPos(0x103, 53830, 10300, 46000, 135)
    SetChrPos(0xF8, 53300, 10300, 45070, 135)
    SetChrPos(0xF9, 52830, 10300, 46040, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC4")
    SetChrPos(0xF9, 53300, 10300, 45070, 135)
    SetChrPos(0xF8, 52830, 10300, 46040, 135)

    label("loc_1AC4")

    OP_6D(54840, 10300, 44060, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    OP_0D()
    Return()

    # Function_5_1A48 end

    SaveToFile()

Try(main)
