from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0122   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0122.x',
        MapIndex            = 4,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0122   ._SN',
            'ED6_DT21/T0122_1 ._SN',
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
        '佛莱迪',                               # 9
        '梅尔达斯',                             # 10
        '埃尔格',                               # 11
        '斯蒂娜',                               # 12
        '乘务员库因特',                         # 13
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH01290 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH01290P._CP',             # 04
    )

    DeclNpc(
        X                   = -38180,
        Z                   = 0,
        Y                   = -500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -36560,
        Z                   = 0,
        Y                   = 1550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36680,
        Z                   = 0,
        Y                   = 73750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -86130,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -42050,
        Z                   = 0,
        Y                   = -4160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = -38537,
        TriggerZ            = 0,
        TriggerY            = -1845,
        TriggerRange        = 400,
        ActorX              = -38180,
        ActorZ              = 1500,
        ActorY              = -497,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36170,
        TriggerZ            = 0,
        TriggerY            = 71651,
        TriggerRange        = 1000,
        ActorX              = -36678,
        ActorZ              = 1500,
        ActorY              = 73751,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1BB",          # 01, 1
        "Function_2_1BC",          # 02, 2
        "Function_3_1C1",          # 03, 3
        "Function_4_1C6",          # 04, 4
        "Function_5_70D",          # 05, 5
        "Function_6_F1C",          # 06, 6
        "Function_7_179D",         # 07, 7
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Return()

    # Function_0_1BA end

    def Function_1_1BB(): pass

    label("Function_1_1BB")

    Return()

    # Function_1_1BB end

    def Function_2_1BC(): pass

    label("Function_2_1BC")

    Call(0, 4)
    Return()

    # Function_2_1BC end

    def Function_3_1C1(): pass

    label("Function_3_1C1")

    Call(0, 5)
    Return()

    # Function_3_1C1 end

    def Function_4_1C6(): pass

    label("Function_4_1C6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_207")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6")
    OP_A9(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207")
    TalkEnd(0x8)
    Return()

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_709")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 3)), scpexpr(EXPR_END)), "loc_306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_258")

    ChrTalk(    #0
        0x8,
        (
            "那么，巡逻就拜托了。\x01",
            "有什么事的话我们会联系协会的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303")

    label("loc_258")


    ChrTalk(    #1
        0x8,
        (
            "老爸对新型导力器\x01",
            "看来很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "最近他就像那样，一个人\x01",
            "进行调整之类的练习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "如果在导力器方面有什么问题，\x01",
            "可以随时来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "那么，就有劳\x01",
            "你们巡逻了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_303")

    Jump("loc_709")

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_548")
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #5
        0x8,
        "呀，艾丝蒂尔和雪拉扎德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "好久不见呢。\x01",
            "你们看起来精神很不错，太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 2)), scpexpr(EXPR_END)), "loc_3E0")

    ChrTalk(    #7
        0x101,
        (
            "#1006F嗯，佛莱迪先生也是。\x02\x03",

            "蔡斯的研修，\x01",
            "看来圆满结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "啊啊，真是受益匪浅。\x02",
    )

    CloseMessageWindow()
    Jump("loc_506")

    label("loc_3E0")


    ChrTalk(    #9
        0x101,
        "#1000F晚上好，佛莱迪先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#027F你看来\x01",
            "气色不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #11
        0x8,
        (
            "嗯，我最近\x01",
            "刚从蔡斯回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "因为中央工房的新型引擎\x01",
            "开始开发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1004F咦，佛莱迪先生\x01",
            "也去了蔡斯！？\x02\x03",

            "#1015F嗯……刚好错过，\x01",
            "没能遇见真有点遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "#020F看来我们和你没有缘分啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "哈哈，可能算是错过了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_506")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #16
        0x8,
        (
            "对了，这么晚\x01",
            "还在到处走动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "是不是在巡逻？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    Jump("loc_589")

    label("loc_548")


    ChrTalk(    #18
        0x8,
        (
            "呀，艾丝蒂尔你们啊。\x01",
            "这么晚了真不容易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "是不是在巡逻？\x02",
    )

    CloseMessageWindow()

    label("loc_589")


    ChrTalk(    #20
        0x101,
        (
            "#1015F嗯……\x01",
            "嗯，算是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020F我们在巡视市内的各处\x01",
            "兼调查雾的事。\x02\x03",

            "这附近\x01",
            "没什么异常吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "嗯，没什么特别的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #23
        0x8,
        (
            "……是吧，老爸，\x01",
            "没什么异常吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #24
        0x9,
        "#3P嗯，很安静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1011F是吗……\x02\x03",

            "#1006F……嗯，那就好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    OP_8C(0x9, 90, 400)
    OP_4B(0x9, 255)

    ChrTalk(    #26
        0x103,
        (
            "#026F打扰你们了。\x02\x03",

            "#020F那我们继续\x01",
            "去巡视了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #27
        0x8,
        "啊啊，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "有什么事的话，\x01",
            "我会马上通知协会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188B)

    label("loc_709")

    TalkEnd(0x8)
    Return()

    # Function_4_1C6 end

    def Function_5_70D(): pass

    label("Function_5_70D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_END)), "loc_753")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_742")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_739")
    OP_A9(0x8)
    Jump("loc_73B")

    label("loc_739")

    OP_A9(0x1)

    label("loc_73B")

    TalkEnd(0xA)
    Return()

    label("loc_742")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_753")
    TalkEnd(0xA)
    Return()

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_END)), "loc_8C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_888")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7B7")

    ChrTalk(    #29
        0xA,
        (
            "看来这次的雾\x01",
            "用常识无法解释。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "艾丝蒂尔你们\x01",
            "巡逻要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_885")

    label("loc_7B7")


    ChrTalk(    #31
        0xA,
        (
            "哦，是艾丝蒂尔你们啊。\x01",
            "巡逻辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "到了晚上雾还是\x01",
            "没有变化呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "本来在夜风的吹拂下…\x01",
            "第二天早上就会是个大晴天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "……看来这次的雾\x01",
            "用常识无法解释。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "我们这些市民也该\x01",
            "提高警戒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_885")

    Jump("loc_8C5")

    label("loc_888")


    ChrTalk(    #36
        0xA,
        "鲁克他们确实令人担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "艾丝蒂尔你们\x01",
            "巡逻要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C5")

    Jump("loc_F18")

    label("loc_8C8")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #38
        0xA,
        "哦，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "好久不见啦。\x01",
            "从你去了训练场以后头一次见吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1000F埃尔格先生，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        "啊啊，终于回来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "雪拉扎德也在一起，\x01",
            "是不是又在执行协会的什么任务啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#026F嗯，我们正在\x01",
            "城里巡逻。\x02\x03",

            "#022F你们可能已经听说了，\x01",
            "发生了一些让人有点在意的事件。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #44
        0xA,
        "嗯，我也是刚听说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "确实挺令人担心的……\x01",
            "有你们巡逻真是太好了，\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #46
        0xA,
        (
            "真是的，才这么一会儿不见，\x01",
            "艾丝蒂尔你也成长了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "当年你那么讨厌考试，\x01",
            "在研修中发牢骚，真令人怀念啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #48
        0x101,
        "#1008F我、我说埃尔格先生……\x02",
    )

    CloseMessageWindow()

    def lambda_B0C():
        TurnDirection(0x0, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B0C)

    def lambda_B1A():
        TurnDirection(0x1, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B1A)

    def lambda_B28():
        TurnDirection(0x2, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B28)
    TurnDirection(0x3, 0x101, 400)
    Sleep(400)

    ChrTalk(    #49
        0x103,
        (
            "#021F哎呀，有什么好隐瞒的。\x02\x03",

            "考试确实是很惨，\x01",
            "但实技不是学的很好吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC8")

    ChrTalk(    #50
        0x106,
        (
            "#051F哈哈，果然是这样吗。\x02\x03",

            "真像你的风格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C")

    label("loc_BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFE")

    ChrTalk(    #51
        0x107,
        (
            "#560F嘿嘿……\x02\x03",

            "哎～姐姐真是的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C")

    label("loc_BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3B")

    ChrTalk(    #52
        0x104,
        (
            "#031F呵，感觉\x01",
            "真像是艾丝蒂尔的过去啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C")

    label("loc_C3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(    #53
        0x108,
        (
            "#070F哈哈，别害羞嘛。\x02\x03",

            "人有缺点才显得可爱嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9D")

    ChrTalk(    #54
        0x105,
        "#041F嘻嘻……\x02",
    )

    CloseMessageWindow()

    label("loc_C9D")


    ChrTalk(    #55
        0xA,
        "呀，抱歉抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "老爱说过去的事，\x01",
            "大概是因为上了年纪啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "话说回来，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "关于约修亚\x01",
            "有什么消息吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D1F():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D1F)

    def lambda_D2D():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D2D)

    def lambda_D3B():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D3B)
    TurnDirection(0x3, 0xA, 400)
    Sleep(400)

    ChrTalk(    #59
        0x101,
        (
            "#1003F嗯、嗯……\x02\x03",

            "#1007F调查了不少，\x01",
            "但没什么发现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        (
            "是吗……\x01",
            "果然没那么简单吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "听卡西乌斯说起的时候，\x01",
            "担心的不得了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "这样看来……艾丝蒂尔。\x01",
            "你是没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "但是，觉得难过的时候\x01",
            "随时都可以来这里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "不介意的话，我和斯蒂娜\x01",
            "都可以听你倾诉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1025F埃尔格先生……\x02\x03",

            "#1000F……嗯，谢谢。\x01",
            "我一定会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        "啊啊，常来逛逛吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        "那么，小心巡逻。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "我们这边如果有什么异常\x01",
            "也会马上联络协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        "#020F嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x1)

    label("loc_F18")

    TalkEnd(0xA)
    Return()

    # Function_5_70D end

    def Function_6_F1C(): pass

    label("Function_6_F1C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 6)), scpexpr(EXPR_END)), "loc_126D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 7)), scpexpr(EXPR_END)), "loc_F92")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #70
        0xFE,
        (
            "虽然很担心这次的事，不过\x01",
            "艾丝蒂尔你也要小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "听我说，一定\x01",
            "不能勉强自己。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_F92")

    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FE4")

    ChrTalk(    #72
        0xFE,
        "对了，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "你这么晚在干什么呢？\x01",
            "有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1029")

    label("loc_FE4")


    ChrTalk(    #74
        0xFE,
        (
            "哎呀，是艾丝蒂尔～～\x01",
            "还有雪拉也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "你这么晚在干什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_1029")


    ChrTalk(    #76
        0x101,
        (
            "#1015F嗯，我们在\x01",
            "城里巡逻一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x103,
        (
            "#020F协会为了以防万一，\x01",
            "也提高警惕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "发生了的那些事\x01",
            "阿姨也听说了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "醒不过来的鲁克他们\x01",
            "真令人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "艾丝蒂尔，你们\x01",
            "你们也要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "听我说，\x01",
            "一定不能勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1013F真、真是的……\x02\x03",

            "阿姨你每次\x01",
            "都把我当小孩子看。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117C")

    ChrTalk(    #83
        0x107,
        (
            "#061F嘿嘿……\x01",
            "就像我妈妈一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1218")

    label("loc_117C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AD")

    ChrTalk(    #84
        0x105,
        (
            "#045F呵呵……\x01",
            "你真是幸运。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1218")

    label("loc_11AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E3")

    ChrTalk(    #85
        0x104,
        "#031F呵呵，就像母亲一般的感觉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1218")

    label("loc_11E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1218")

    ChrTalk(    #86
        0x106,
        "#051F哈哈，看来这就叫一物降一物。\x02",
    )

    CloseMessageWindow()

    label("loc_1218")


    ChrTalk(    #87
        0x103,
        (
            "#020F嗯，不过阿姨\x01",
            "没说错。\x02\x03",

            "我们也\x01",
            "小心一点为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188F)

    label("loc_126A")

    Jump("loc_1799")

    label("loc_126D")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #89
        0xFE,
        "哎呀…………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #90
        0xFE,
        (
            "呀～怎么办呀。\x01",
            "这不是艾丝蒂尔吗！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #91
        0xFE,
        (
            "哎呀哎呀，仔细一看…\x01",
            "连雪拉也在一起呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1008F嘿嘿，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        "#021F呵呵，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "真是的～真是好久不见哦！\x01",
            "阿姨都急死了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #95
        0xFE,
        (
            "昨天就听到传闻，\x01",
            "但去碰你却一直没碰上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1016F啊哈哈，对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#027F不过，艾丝蒂尔\x01",
            "也有很多事情啦。\x02\x03",

            "就原谅她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "没问题，这点事\x01",
            "阿姨还是明白的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "听说约修亚的事时…\x01",
            "还有点担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "嗯，看来艾丝蒂尔\x01",
            "也很努力的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1016F嗯、嗯……算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "那，别提了，\x01",
            "艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "（盯……………………\x01",
            "　……………………………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015F什、什么？\x01",
            "突然盯着我看。\x02\x03",

            "我、我刷了牙，\x01",
            "脸也洗了才来的呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#3S真是的，多漂亮呀！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #106
        0x101,
        "#1004F哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "怎么回事，穿这裙子！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "有种活跃女孩子的感觉哦～～\x01",
            "很适合你哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1008F嘿嘿……是、是吗。\x02\x03",

            "这个，是雪拉姐\x01",
            "在王都给我买的。\x02\x03",

            "作为当上正游击士的祝贺哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "哦～到底是雪拉。\x01",
            "很有品味嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x103,
        (
            "#021F呵呵，阿姨\x01",
            "喜欢就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "注意仪容\x01",
            "可是有心思的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "嗯嗯，即使成为正游击士\x01",
            "看来也能做得很出色呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "以前那么邋遢的艾丝蒂尔\x01",
            "打扮得这么有模有样的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "呜呜……\x01",
            "阿、阿姨都快流眼泪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1008F哈，哈哈……\x02\x03",

            "#1013F（没，没想到\x01",
            "  穿条裙子她都会哭啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#025F（要是看到艾丝蒂尔穿婚纱\x01",
            "那还不得昏倒了啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188E)
    OP_A2(0x2)

    label("loc_1799")

    TalkEnd(0xB)
    Return()

    # Function_6_F1C end

    def Function_7_179D(): pass

    label("Function_7_179D")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_17FA")

    ChrTalk(    #118
        0xFE,
        "呼哼哼哼～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "嘿嘿，难得\x01",
            "到了城里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "不去购物\x01",
            "真是损失太大了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C8")

    label("loc_17FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_186A")

    ChrTalk(    #121
        0xFE,
        (
            "索斯摩夫说他在工作中\x01",
            "看到了一只猫哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "总之，详细情况可以去问他本人。\x01",
            "他应该还在飞船坪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C8")

    label("loc_186A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_187C")
    Call(1, 0)
    Jump("loc_18C8")

    label("loc_187C")


    ChrTalk(    #123
        0xFE,
        "哼哼哼哼～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "嘿嘿，难得\x01",
            "到了城里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "不去购物\x01",
            "真是损失太大了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C8")

    TalkEnd(0xC)
    Return()

    # Function_7_179D end

    SaveToFile()

Try(main)
