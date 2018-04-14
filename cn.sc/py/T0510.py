from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0510   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0510.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
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
        '戴恩副队长',                           # 9
        '阿斯顿队长',                           # 10
        '阿维因队长',                           # 11
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
    )

    DeclNpc(
        X                   = 26800,
        Z                   = 0,
        Y                   = 29900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 29800,
        Z                   = 0,
        Y                   = -73400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 29800,
        Z                   = 0,
        Y                   = -73400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = 28250,
        TriggerZ            = 0,
        TriggerY            = 29800,
        TriggerRange        = 500,
        ActorX              = 26800,
        ActorZ              = 1500,
        ActorY              = 29900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28310,
        TriggerZ            = 0,
        TriggerY            = -73420,
        TriggerRange        = 500,
        ActorX              = 29850,
        ActorZ              = 1500,
        ActorY              = -73420,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20640,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 1000,
        ActorX              = 20640,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_1A7",          # 01, 1
        "Function_2_1FD",          # 02, 2
        "Function_3_213",          # 03, 3
        "Function_4_218",          # 04, 4
        "Function_5_693",          # 05, 5
        "Function_6_6AB",          # 06, 6
        "Function_7_1251",         # 07, 7
        "Function_8_138C",         # 08, 8
    )


    def Function_0_186(): pass

    label("Function_0_186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_190")
    Jump("loc_1A6")

    label("loc_190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_1A6")

    Return()

    # Function_0_186 end

    def Function_1_1A7(): pass

    label("Function_1_1A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_1FC")

    Return()

    # Function_1_1A7 end

    def Function_2_1FD(): pass

    label("Function_2_1FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_212")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1FD")

    label("loc_212")

    Return()

    # Function_2_1FD end

    def Function_3_213(): pass

    label("Function_3_213")

    Call(0, 4)
    Return()

    # Function_3_213 end

    def Function_4_218(): pass

    label("Function_4_218")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3")

    ChrTalk(    #0
        0x8,
        (
            "哈肯大门那边的情况\x01",
            "好像相当紧迫啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "间接性地进行联络，\x01",
            "一直都是那么紧张戒备中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "虽然刚刚签署完互不侵犯条约，\x01",
            "但不管什么时候也不能对帝国掉以轻心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_32D")

    label("loc_2D3")


    ChrTalk(    #3
        0x8,
        (
            "哈肯大门那边的情况\x01",
            "好像相当紧迫啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "间接性地进行联络，\x01",
            "一直都是那么紧张戒备中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D")

    Jump("loc_68F")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8")

    ChrTalk(    #5
        0x8,
        (
            "喔，是各位游击士啊。\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "现在路灯都熄灭了，\x01",
            "到处也都很危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "旅行时要\x01",
            "小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3E8")

    label("loc_3A8")


    ChrTalk(    #8
        0x8,
        (
            "现在路灯都熄灭了，\x01",
            "到处也都很危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "旅行时要\x01",
            "小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E8")

    Jump("loc_68F")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_456")

    ChrTalk(    #10
        0x8,
        (
            "虽然不知道具体过程，\x01",
            "但龙的骚乱似乎已经平息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "呼，不管怎样，\x01",
            "总算是个好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C8")

    label("loc_456")


    ChrTalk(    #12
        0x8,
        (
            "虽然不知道具体过程，\x01",
            "但龙的骚乱似乎平息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "好久没有收到\x01",
            "新消息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "最后总算是\x01",
            "把事情解决了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4C8")

    Jump("loc_68F")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_5A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_528")

    ChrTalk(    #15
        0x8,
        (
            "听说连飞行舰队\x01",
            "也无法将龙捕获。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "果然没有卡西乌斯准将\x01",
            "还是不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A2")

    label("loc_528")


    ChrTalk(    #17
        0x8,
        (
            "为了捕获飞龙，竟然连\x01",
            "飞行舰队都出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "而且居然这样\x01",
            "也无法把龙抓住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "果然没有卡西乌斯准将\x01",
            "还是不行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5A2")

    Jump("loc_68F")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_68F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_600")

    ChrTalk(    #20
        0x8,
        (
            "前几天大雾的时候\x01",
            "真是辛苦得要死。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "虽然只是雾，\x01",
            "但也不能轻视啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68F")

    label("loc_600")


    ChrTalk(    #22
        0x8,
        (
            "前几天大雾的时候\x01",
            "真是辛苦得要死。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "洛连特的警备\x01",
            "一直人手不足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "已经向哈肯大门\x01",
            "请求支援了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "虽然只是雾，\x01",
            "但也不能轻视啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_68F")

    TalkEnd(0x8)
    Return()

    # Function_4_218 end

    def Function_5_693(): pass

    label("Function_5_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A6")
    Call(0, 7)
    Jump("loc_6AA")

    label("loc_6A6")

    Call(0, 6)

    label("loc_6AA")

    Return()

    # Function_5_693 end

    def Function_6_6AB(): pass

    label("Function_6_6AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_726")

    ChrTalk(    #26
        0x9,
        (
            "呀！艾丝蒂尔和约修亚，\x01",
            "连雪拉扎德也在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "前一阵子的大雾事件\x01",
            "真是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76B")

    label("loc_726")


    ChrTalk(    #28
        0x9,
        "呀！艾丝蒂尔和约修亚，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "前一阵子的大雾事件\x01",
            "真是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B")


    ChrTalk(    #30
        0x9,
        (
            "今天又在\x01",
            "执行任务吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1000F啊，嗯。\x01",
            "正是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1040F这边的情况怎么样？\x02\x03",

            "现在看起来，关所的大门\x01",
            "一直开着…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #33
        0x9,
        (
            "那大门是导力式的，\x01",
            "现在连开关都成了问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "为了不阻碍交通，\x01",
            "只能一直开着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1007F是吗……\x01",
            "那也只能如此了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D1")

    ChrTalk(    #36
        0x103,
        (
            "#022F辛苦了，\x01",
            "警备工作就拜托您了。\x02\x03",

            "现在也许还有些不老实的家伙\x01",
            "正在蠢蠢欲动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)
    Jump("loc_99E")

    label("loc_8D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_934")

    ChrTalk(    #37
        0x106,
        (
            "#057F辛苦了，\x01",
            "警备工作就拜托您了。\x02\x03",

            "那些可恶的白痴至今\x01",
            "仍在蠢蠢欲动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    Jump("loc_99E")

    label("loc_934")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99E")

    ChrTalk(    #38
        0x108,
        (
            "#072F辛苦您了，\x01",
            "警备工作就拜托了。\x02\x03",

            "在这种情况下，\x01",
            "还不知道潜伏了什么样的角色。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x108, 400)

    label("loc_99E")


    ChrTalk(    #39
        0x9,
        (
            "嗯，上边也做出了\x01",
            "这样的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "虽然是很麻烦的工作，\x01",
            "但为了保证这里的安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "也只能拼命\x01",
            "努力了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1042F拜托您了。\x02\x03",

            "我们也会尽全力来\x01",
            "结束这种事态的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #43
        0x9,
        (
            "如果没有你们的努力，\x01",
            "想解决这次的事件根本不可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "我也拜托你们加油了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20AE)
    Jump("loc_CDF")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B4B")

    ChrTalk(    #45
        0x9,
        (
            "我们王国军警备队\x01",
            "也在努力进行关所的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "不过，你们游击士\x01",
            "是可以自由通行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "如果没有你们的努力，\x01",
            "想解决这次的事件根本不可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C49")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEF")

    ChrTalk(    #48
        0x9,
        (
            "听说有警备艇\x01",
            "迫降在了米尔西街道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "这要是平时的话，雷斯顿要塞\x01",
            "马上就会派出救援部队…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "但现在根本\x01",
            "做不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "救援工作\x01",
            "只能暂时放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_C49")

    label("loc_BEF")


    ChrTalk(    #52
        0x9,
        (
            "虽然对不起警备艇的各位，\x01",
            "但现在也没办法救援啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "救援队现在的移动\x01",
            "能力极其有限。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C49")

    Jump("loc_CDF")

    label("loc_C4C")


    ChrTalk(    #54
        0x9,
        (
            "我们王国军警备队\x01",
            "也在努力进行关所的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "不过，你们游击士\x01",
            "是可以自由通行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "如果没有你们的努力，\x01",
            "想解决这次的事件根本不可能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDF")

    Jump("loc_124D")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 1)), scpexpr(EXPR_END)), "loc_D4D")

    ChrTalk(    #57
        0x9,
        (
            "接下来也要靠你们\x01",
            "游击士的努力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "我们双方携手努力的话，\x01",
            "一定可以让王国和平的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_D4D")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #59
        0x9,
        (
            "啊，艾丝蒂尔，\x01",
            "还有雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "这次也多谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "鲁克那小家伙\x01",
            "也恢复了意识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1017F嘿嘿，哪里的话，\x02\x03",

            "多亏阿斯顿先生\x01",
            "帮忙保护城镇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "哈哈，这些话我会\x01",
            "转告给部下们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "接下来也要靠你们\x01",
            "游击士的努力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "我们双方携手努力的话，\x01",
            "一定可以让王国和平的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1006F嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        "#020F我们也拜托您了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A69)

    label("loc_EBB")

    Jump("loc_124D")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_124D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 7)), scpexpr(EXPR_END)), "loc_F38")

    ChrTalk(    #68
        0x9,
        (
            "定期船都停航了，\x01",
            "看来雾很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "我们军队\x01",
            "也会思索对策的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "总之现在大家\x01",
            "要携手度过难关。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124D")

    label("loc_F38")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #71
        0x9,
        (
            "啊，艾丝蒂尔\x01",
            "好久不见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1001F好久不见了，阿斯顿先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "协会有工作吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "现在要办通行手续的话\x01",
            "要花些时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F啊，没关系，\x01",
            "今天并不准备通行……\x02\x03",

            "#1011F办理手续需要花一些时间？\x01",
            "难道是出了什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "那倒没有，只是受空贼艇抢夺\x01",
            "事件的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "所以上面下达了\x01",
            "强化警备的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1004F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        (
            "#022F原来如此……\x01",
            "军队也加强警备了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #80
        0x9,
        "其实只是个形式而已。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "比起那个，\x01",
            "我更在意洛连特的雾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "定期船都停航了，\x01",
            "似乎浓得很不寻常啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1002F嗯，其实我们\x01",
            "也在调查这阵大雾。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #84
        0x9,
        (
            "原来如此，因为这个\x01",
            "才来这里的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "要是有什么情况，\x01",
            "就和军队也进行一下联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "这种时候\x01",
            "才能体现出合作关系的重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        "#020F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "那么，调查的事情\x01",
            "就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1006F嗯，先这么说啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1887)

    label("loc_124D")

    TalkEnd(0x9)
    Return()

    # Function_6_6AB end

    def Function_7_1251(): pass

    label("Function_7_1251")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_1388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(    #90
        0xA,
        (
            "在阿斯顿队长回来之前\x01",
            "这里就由我们守备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "任务很艰巨，\x01",
            "所以一定要认真对待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1388")

    label("loc_12BD")


    ChrTalk(    #92
        0xA,
        (
            "我们是从哈肯大门那边调派来这里\x01",
            "暂时代替阿斯顿队长进行警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "在洛连特的警备结束前\x01",
            "这里就交给我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "在大雾中发生了什么事呢？\x01",
            "真是让人不解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "现在还不能放松警备，\x01",
            "要多提醒部下才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1388")

    TalkEnd(0xA)
    Return()

    # Function_7_1251 end

    def Function_8_138C(): pass

    label("Function_8_138C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DF")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05好像是导力停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_159D")

    label("loc_13DF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #97
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1582")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x32)
    OP_73(0x1)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_159C")

    Return()

    label("loc_159D")

    Return()

    # Function_8_138C end

    SaveToFile()

Try(main)
