from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1410   ._SN',
        MapName             = 'Bose',
        Location            = 'C1410.x',
        MapIndex            = 62,
        MapDefaultBGM       = "ed60015",
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
        '维姆拉',                               # 9
        '龙谷',                                 # 10
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = 33900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 3410,
        Z                   = 0,
        Y                   = 36700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 4500,
        TriggerZ            = 0,
        TriggerY            = 39460,
        TriggerRange        = 1500,
        ActorX              = 5070,
        ActorZ              = 500,
        ActorY              = 39610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_146",          # 01, 1
        "Function_2_147",          # 02, 2
        "Function_3_15D",          # 03, 3
        "Function_4_B59",          # 04, 4
        "Function_5_DB5",          # 05, 5
        "Function_6_1FAB",         # 06, 6
        "Function_7_2035",         # 07, 7
        "Function_8_20DC",         # 08, 8
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_134")
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x8, 0, 0)
    Jump("loc_145")

    label("loc_134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145")
    SetChrFlags(0x8, 0x80)

    label("loc_145")

    Return()

    # Function_0_11E end

    def Function_1_146(): pass

    label("Function_1_146")

    Return()

    # Function_1_146 end

    def Function_2_147(): pass

    label("Function_2_147")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_147")

    label("loc_15C")

    Return()

    # Function_2_147 end

    def Function_3_15D(): pass

    label("Function_3_15D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1D1")
    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "迄今为止发生的异变和\x01",
            "巨龙事件也许有什么关系也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "接下来大概还会有\x01",
            "什么事情发生吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_B58")

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2AB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255")

    ChrTalk(    #2
        0xFE,
        "嗯……是你们吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "真是难得，\x01",
            "今天刚来了位客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "好像是龙的研究者，\x01",
            "为了调查古代龙的住处而来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2A5")

    label("loc_255")


    ChrTalk(    #5
        0xFE,
        (
            "真是难得，\x01",
            "今天刚来了位客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "真是的……\x01",
            "这种时候竟然还有这种心情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5")

    TalkEnd(0xFE)
    Jump("loc_B58")

    label("loc_2AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_82D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 1)), scpexpr(EXPR_END)), "loc_36E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315")

    ChrTalk(    #7
        0xFE,
        (
            "看来已经顺利\x01",
            "把巨龙降服了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "身为居住在峡谷的人，\x01",
            "我也要感谢你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B")

    label("loc_315")


    ChrTalk(    #9
        0xFE,
        (
            "大家吃了这顿火锅以后\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "这一仗下来，你们肯定也\x01",
            "疲惫不堪了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B")

    Jump("loc_827")

    label("loc_36E")


    ChrTalk(    #11
        0xFE,
        "嗯，是你们吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "看来已经顺利\x01",
            "把巨龙降服了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "身为居住在峡谷的人，\x01",
            "我也要感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006F这全都是靠维姆拉先生\x01",
            "的帮助啊。\x02\x03",

            "如果只有我们几个的话，\x01",
            "真的是什么也做不了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46B")

    ChrTalk(    #15
        0x106,
        (
            "#051F啊啊，正是如此。\x01",
            "该说谢谢的应该是我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50E")

    label("loc_46B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D")

    ChrTalk(    #16
        0x103,
        "#020F是啊，多谢您的协助了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_50E")

    label("loc_49D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CF")

    ChrTalk(    #17
        0x108,
        "#070F没错，谢谢您的协助啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_50E")

    label("loc_4CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50E")

    ChrTalk(    #18
        0x104,
        (
            "#031F呼～真服了你们。\x02\x03",

            "『谢谢您的协助了。』\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #19
        0xFE,
        (
            "为了说这句话\x01",
            "还特意跑来一趟吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "你们还真是有闲心……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1016F啊…也、也不只是为了\x01",
            "那个才来了啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "算了，你们就在这里随意休息吧，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "要是肚子饿了的话\x01",
            "那里有火锅料理可以吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1004F哎，那是给我们吃的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "嗯，虽然吃下这个\x01",
            "需要有相当的觉悟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "但对你们这些时常要面对战斗的\x01",
            "游击士来说，应该还是很有用的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "好了，试试看吧。\x01",
            "趁这个机会尝一尝。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #28
        "\x06\x07\x02黑暗火锅·觉悟\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EA")
    OP_31(0x0, 0x2, 0x1)
    OP_31(0x0, 0x5, 0x0)

    label("loc_6EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FD")
    OP_31(0x1, 0x5, 0xC8)

    label("loc_6FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_710")
    OP_31(0x2, 0x5, 0xC8)

    label("loc_710")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_723")
    OP_31(0x3, 0x5, 0xC8)

    label("loc_723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_736")
    OP_31(0x4, 0x5, 0xC8)

    label("loc_736")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_749")
    OP_31(0x5, 0x5, 0xC8)

    label("loc_749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75C")
    OP_31(0x6, 0x5, 0xC8)

    label("loc_75C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76F")
    OP_31(0x7, 0x5, 0xC8)

    label("loc_76F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_782")
    OP_31(0x8, 0x5, 0xC8)

    label("loc_782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x8)"), scpexpr(EXPR_END)), "loc_79C")
    Jump("loc_7CA")

    label("loc_79C")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x06\x07\x02黑暗火锅·觉悟\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_7CA")

    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #30
        0xFE,
        (
            "喔……\x01",
            "平安回来了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "有需要的话就再来吧，\x01",
            "随时欢迎你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A51)
    OP_A2(0x0)

    label("loc_827")

    TalkEnd(0xFE)
    Jump("loc_B58")

    label("loc_82D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_END)), "loc_8BF")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_886")

    ChrTalk(    #32
        0xFE,
        (
            "岩山的空洞中\x01",
            "有很多危险的魔兽，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "请不要逞强，小心地前进吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B9")

    label("loc_886")


    ChrTalk(    #34
        0xFE,
        "嗯……回来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "在这里好好\x01",
            "休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    TalkEnd(0xFE)
    Jump("loc_B58")

    label("loc_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 5)), scpexpr(EXPR_END)), "loc_8CD")
    Call(0, 5)
    Jump("loc_B58")

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_9AC")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(    #36
        0xFE,
        (
            "虽然不知道你们要做什么，\x01",
            "不过居然会来到这个地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "这个屋子里的东西\x01",
            "你们可以随意使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A6")

    label("loc_944")


    ChrTalk(    #38
        0xFE,
        (
            "虽然不知道你们要做什么，\x01",
            "不过居然会来到这个地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "这个屋子里的东西\x01",
            "你们可以随意使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A6")

    TalkEnd(0xFE)
    Jump("loc_B58")

    label("loc_9AC")

    TalkBegin(0xFE)

    ChrTalk(    #40
        0xFE,
        "嗯……你们是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1011F啊，我们是\x01",
            "游击士协会的人…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #42
        0xFE,
        "啊～，好像没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #43
        0xFE,
        (
            "那个红毛小鬼和我\x01",
            "以前就认识了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x106,
        (
            "#053F哼，不要一口\x01",
            "一个小鬼。\x02\x03",

            "#051F好久不见啦，\x01",
            "维姆拉大叔。\x02\x03",

            "你身体还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "呵呵，我可不想\x01",
            "输给你们年轻人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "虽然不知道你们要做什么，\x01",
            "不过居然会来到这个地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "这个屋子里的东西\x01",
            "你们可以随意使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1018F啊……嗯，谢谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        "#051F不好意思，真是帮大忙了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A80)
    OP_A2(0x0)
    TalkEnd(0xFE)

    label("loc_B58")

    Return()

    # Function_3_15D end

    def Function_4_B59(): pass

    label("Function_4_B59")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2F")

    ChrTalk(    #50
        0xFE,
        (
            "身为一名研究者，\x01",
            "我对古代龙的住处也很有兴趣……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "但那个地方好像很危险，\x01",
            "维姆拉先生不让我去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "迄今为止，去那里的人\x01",
            "几乎全都是游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "看来确实不是我这种人\x01",
            "应该去的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C89")

    label("loc_C2F")


    ChrTalk(    #54
        0xFE,
        (
            "去过古代龙住处的人\x01",
            "几乎全都是游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "从这点可以清楚了解到\x01",
            "那里的危险程度呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C89")

    Jump("loc_DB1")

    label("loc_C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D51")

    ChrTalk(    #56
        0xFE,
        (
            "啊，你好。\x01",
            "我是古代生物的研究者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "听到古代龙住处的传闻之后\x01",
            "特意赶到这里，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "那、那里的危险程度似乎\x01",
            "远超乎我的预料呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "我、我只是稍微\x01",
            "来看看情况而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_DB1")

    label("loc_D51")


    ChrTalk(    #60
        0xFE,
        (
            "听到古代龙住处的传闻之后\x01",
            "特意赶到这里，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "非常危险呢。\x01",
            "连、连一步都不敢踏出去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB1")

    TalkEnd(0x9)
    Return()

    # Function_4_B59 end

    def Function_5_DB5(): pass

    label("Function_5_DB5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DCC")
    Call(0, 6)
    Call(0, 8)

    label("loc_DCC")

    Fade(1000)
    OP_6D(3740, 0, 36060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 4260, 0, 35660, 225)
    SetChrPos(0x106, 3350, 0, 36130, 180)
    SetChrPos(0x107, 2660, 0, 36470, 180)
    SetChrPos(0xF9, 3440, 0, 37310, 180)
    OP_4A(0x8, 255)
    OP_0D()
    TurnDirection(0xF9, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在后篇见过维姆拉】\x01",        # 0
            "【◇在后篇没见过维姆拉】\x01",      # 1
            "【◇什么也没有变更】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EF2"),
        (1, "loc_EF8"),
        (SWITCH_DEFAULT, "loc_EFE"),
    )


    label("loc_EF2")

    OP_A2(0x1A80)
    Jump("loc_EFE")

    label("loc_EF8")

    OP_A3(0x1A80)
    Jump("loc_EFE")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_FCF")

    ChrTalk(    #62
        0x106,
        (
            "#051F哟。\x01",
            "维姆拉大叔。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(700)

    ChrTalk(    #63
        0x8,
        (
            "阿加特……\x01",
            "还有小姐们也来了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1011F#5P您好啊，维姆拉大叔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        "#560F#5P那个，打扰您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "嗯，多次来这种\x01",
            "偏僻荒凉的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "有什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1120")

    label("loc_FCF")

    OP_8C(0x8, 0, 400)
    Sleep(700)

    ChrTalk(    #68
        0x8,
        "嗯……你们是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x107,
        "#560F#5P那个，打扰您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1011F#5P嗯，我们是\x01",
            "游击士协会的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        "啊啊，就是那样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "那个红毛小鬼和我\x01",
            "以前就认识了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#053F哼，不要一口\x01",
            "一个小鬼。\x02\x03",

            "#051F好久不见啦，\x01",
            "维姆拉大叔。\x02\x03",

            "你身体还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "呵呵，我可不想\x01",
            "输给你们年轻人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "那么，有什么事吗？\x01",
            "你们似乎是为什么事情而来的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1120")


    ChrTalk(    #76
        0x101,
        "#1002F#5P嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        (
            "\x07\x05将柏斯地区出现龙的事件\x01",
            "说明给了维姆拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #78
        0x8,
        "呼……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "怪不得前一阵子\x01",
            "外边那么乱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#051F喂，大叔。\x02\x03",

            "记得你之前曾经说过，\x01",
            "你到过西北部去吧？\x02\x03",

            "现在想请你告诉我们\x01",
            "那边的路怎么走。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #81
        0x8,
        "……我拒绝\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D3")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1311")

    label("loc_12D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FA")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1311")

    label("loc_12FA")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1311")

    Sleep(1000)

    ChrTalk(    #82
        0x101,
        "#1004F#5P哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        (
            "#055F慢着！！\x01",
            "为什么想都不想就直接拒绝！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "……我只有一个问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "你们，找到龙之后\x01",
            "准备怎么做？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1015F#5P嗯、嗯嗯……\x02\x03",

            "它好像是被某些恶人操控了… \x01",
            "可能的话，我们也不想杀死它……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x106,
        (
            "#552F但如果将『福音』破坏\x01",
            "也不能让它清醒的话，就没办法了。\x02\x03",

            "毕竟世界上没那么多完美结局啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        "哎呀呀呀……说得真轻松啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "听你们的口气，\x01",
            "似乎将龙同你们打倒过的魔兽\x01",
            "混为一谈了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        "那实在是太天真了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "龙可是在『大崩坏』之前\x01",
            "就存在的神兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1015F#5P『大崩坏』之前……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #93
        0x101,
        "#1020F#5P#3S哎哎！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #94
        0x107,
        (
            "#065F#5P那、那就是说\x01",
            "在1200年前就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x106,
        (
            "#051F哈哈，那不太可能吧。\x02\x03",

            "虽然能看出来它是个老家伙，\x01",
            "但再怎么老也不可能……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_164C")

    ChrTalk(    #96
        0x103,
        (
            "#025F#5P不，那是有可能的。\x02\x03",

            "#022F虽然仅限于有龙之传承\x01",
            "的国家……\x02\x03",

            "但确实有『龙是不老不死的』\x01",
            "这种说法一直在流传着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F1")

    label("loc_164C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16DF")

    ChrTalk(    #97
        0x105,
        (
            "#043F#5P不，那是有可能的。\x02\x03",

            "龙的目击记录，在９００年前的\x01",
            "利贝尔建国时期就已经有了。\x02\x03",

            "听说和现在不同，\x01",
            "当时出现得相当频繁呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F1")

    label("loc_16DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1772")

    ChrTalk(    #98
        0x104,
        (
            "#035F#5P不，那是有可能的。\x02\x03",

            "#032F根据七耀教会的传说，\x01",
            "龙是守护空之女神\x01",
            "的圣兽。\x02\x03",

            "这种存在，或许不是\x01",
            "以我们的常识可以解释的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F1")

    label("loc_1772")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F1")

    ChrTalk(    #99
        0x108,
        (
            "#074F#5P不，那是有可能的。\x02\x03",

            "#072F在东方，有很多人将龙\x01",
            "视作神兽崇拜。\x02\x03",

            "还是不要用一般人的常识来\x01",
            "论断比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F1")

    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x106,
        "#055F……真的吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1007F#5P的、的确不要把它\x01",
            "和普通的魔兽相提并论比较好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "想将这样的家伙消灭？\x01",
            "你们这种举动根本和自杀没区别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "好了，总之这件事就交给\x01",
            "军队去处理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "虽然军队那群家伙也不怎么靠得住，\x01",
            "但如果有那个男人在的话，也许…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1004F#5P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "……不管怎么说，我可不愿意\x01",
            "看着你们这些小家伙去白白送死。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        "抱歉，我不能帮忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1026F#5P但，但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#053F…………………………………\x02\x03",

            "#555F……喂，大叔。\x02\x03",

            "你的好意我们心领了，\x01",
            "但你不觉得有点离题了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        "……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x106,
        (
            "#050F我们遇到过\x01",
            "棘手的敌人\x01",
            "不是一次两次了。\x02\x03",

            "像之前的情报部，\x01",
            "还有古代的人形兵器…\x02\x03",

            "#053F每一个也都是\x01",
            "强大到令人绝望的对手。\x02\x03",

            "但我们最终也都是克服重重困难\x01",
            "合力战胜他们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        (
            "#051F这次的龙也是一样！\x02\x03",

            "虽然它确实是前所未有的强敌，\x01",
            "但我们也从没打算过去白白送死。\x02\x03",

            "#053F所以……拜托了。\x02\x03",

            "无论如何请帮帮我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #114
        0x101,
        "#1025F#2P阿加特……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)
    Sleep(300)

    ChrTalk(    #115
        0x107,
        "#560F#6P阿加特哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "你什么时候变得\x01",
            "这么能言善道了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "话都说到这个份上了，\x01",
            "看来不帮你们也是不成的啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x106,
        "#052F！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #120
        0x101,
        "#1004F#5P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        "#067F#5P谢、谢谢您了！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "哪里……\x01",
            "没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "我有些准备工作要做，\x01",
            "所以要先走一步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "我会在西部最里侧等你们，\x01",
            "跟过来就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1015F#5P跟上来？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x106,
        (
            "#555F喂！你直接把西北边的路\x01",
            "告诉我们不就好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "光是口头说说的话，\x01",
            "大概你们也一样找不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "总之你们到了峡谷西侧之后\x01",
            "一直往深处走就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        "我等着你们！\x02",
    )

    CloseMessageWindow()

    def lambda_1DB0():

        label("loc_1DB0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1DB0")

    QueueWorkItem2(0x101, 1, lambda_1DB0)

    def lambda_1DC1():

        label("loc_1DC1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1DC1")

    QueueWorkItem2(0x106, 1, lambda_1DC1)

    def lambda_1DD2():

        label("loc_1DD2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1DD2")

    QueueWorkItem2(0x107, 1, lambda_1DD2)

    def lambda_1DE3():

        label("loc_1DE3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1DE3")

    QueueWorkItem2(0xF9, 1, lambda_1DE3)

    def lambda_1DF4():
        OP_6D(2020, 0, 36590, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DF4)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xCC6, 0x0, 0x8886, 0xBB8, 0x0)
    OP_8E(0x8, 0x500, 0x0, 0x8DA4, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFEE26, 0x0, 0x8C50, 0xBB8, 0x0)

    def lambda_1E4D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E4D)
    OP_8E(0x8, 0xFFFFEA8E, 0x0, 0x8C0A, 0xBB8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #130
        0x101,
        "#1020F#2P等、等一下……！\x02",
    )

    CloseMessageWindow()
    OP_6D(3740, 0, 36060, 1500)

    ChrTalk(    #131
        0x106,
        (
            "#551F#5P……没办法。\x02\x03",

            "#050F就照大叔说的\x01",
            "跟过去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F#2P是、是啊……\x02\x03",

            "#1002F嗯，是峡谷西侧\x01",
            "最深处的地方对吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F3E():
        OP_8C(0x107, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1F3E)

    def lambda_1F4C():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1F4C)
    OP_8C(0x106, 90, 400)
    Sleep(500)

    ChrTalk(    #133
        0x106,
        (
            "#051F#6P啊啊。\x02\x03",

            "这里的地形比较复杂，\x01",
            "小心别迷路啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A26)
    OP_28(0x96, 0x1, 0x40)
    OP_28(0x96, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_DB5 end

    def Function_6_1FAB(): pass

    label("Function_6_1FAB")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2028"),
        (1, "loc_202E"),
        (SWITCH_DEFAULT, "loc_2034"),
    )


    label("loc_2028")

    OP_A2(0x1200)
    Jump("loc_2034")

    label("loc_202E")

    OP_A2(0x1201)
    Jump("loc_2034")

    label("loc_2034")

    Return()

    # Function_6_1FAB end

    def Function_7_2035(): pass

    label("Function_7_2035")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C0")
    SoundLoad(13)
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_20C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_20DA")

    Return()

    # Function_7_2035 end

    def Function_8_20DC(): pass

    label("Function_8_20DC")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_8_20DC end

    SaveToFile()

Try(main)
