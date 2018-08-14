from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '夏伊',                                 # 9
        '史帕德',                               # 10
        '塞森',                                 # 11
        '多姆',                                 # 12
        '',                                     # 13
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01680 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01680P._CP',             # 04
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 129840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_21E",          # 02, 2
        "Function_3_242",          # 03, 3
        "Function_4_247",          # 04, 4
        "Function_5_3E9",          # 05, 5
        "Function_6_3EE",          # 06, 6
        "Function_7_52E",          # 07, 7
        "Function_8_533",          # 08, 8
        "Function_9_6D8",          # 09, 9
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1D4")
    Jump("loc_1EF")

    label("loc_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1DE")
    Jump("loc_1EF")

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_1EF")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1EF")

    label("loc_1EF")

    Return()

    # Function_0_1BE end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_B1("t4120_n")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_21D")

    Return()

    # Function_1_1F0 end

    def Function_2_21E(): pass

    label("Function_2_21E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_241")
    OP_8D(0xFE, 1470, 131290, -1690, 128210, 2000)
    Jump("Function_2_21E")

    label("loc_241")

    Return()

    # Function_2_21E end

    def Function_3_242(): pass

    label("Function_3_242")

    Call(0, 4)
    Return()

    # Function_3_242 end

    def Function_4_247(): pass

    label("Function_4_247")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_254")
    Jump("loc_3E5")

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_323")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B8")

    ChrTalk(    #0
        0x12,
        "多姆那家伙在三楼呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        (
            "他正在经营独一无二的商店。\x01",
            "乐意的话就去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_320")

    label("loc_2B8")


    ChrTalk(    #2
        0x12,
        "多姆那家伙手很巧嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "连坏掉的导力器之类的东西\x01",
            "也能马上修好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x12,
        "嗯，那可是才能啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_320")

    Jump("loc_3E5")

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_32D")
    Jump("loc_3E5")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_3E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_389")

    ChrTalk(    #5
        0x12,
        "多姆那家伙在三楼呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        (
            "他正在经营有趣的商店，\x01",
            "请务必去看看哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5")

    label("loc_389")


    ChrTalk(    #7
        0x12,
        "我和儿时玩伴多姆开始开店了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x12,
        (
            "多姆的技术加上我的经营能力，\x01",
            "一定会很顺利的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3E5")

    TalkEnd(0x12)
    Return()

    # Function_4_247 end

    def Function_5_3E9(): pass

    label("Function_5_3E9")

    Call(0, 6)
    Return()

    # Function_5_3E9 end

    def Function_6_3EE(): pass

    label("Function_6_3EE")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_3FB")
    Jump("loc_52A")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_455")

    ChrTalk(    #9
        0x10,
        "我们还是新婚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "呵呵，我丈夫虽然不爱说话，\x01",
            "但这不是很酷吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486")

    label("loc_455")


    ChrTalk(    #11
        0x10,
        "啦啦啦、啦～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "啊，欢迎光临～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_486")

    Jump("loc_52A")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_493")
    Jump("loc_52A")

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_52A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4F1")

    ChrTalk(    #13
        0x10,
        (
            "那个人啊，就知道写进货单，\x01",
            "从来不会做买卖……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "只有靠我努力了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_52A")

    label("loc_4F1")


    ChrTalk(    #15
        0x10,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "请进，\x01",
            "慢慢看哦。\x02",
        )
    )

    Jump("loc_526")

    label("loc_526")

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_52A")

    TalkEnd(0x10)
    Return()

    # Function_6_3EE end

    def Function_7_52E(): pass

    label("Function_7_52E")

    Call(0, 8)
    Return()

    # Function_7_52E end

    def Function_8_533(): pass

    label("Function_8_533")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_540")
    Jump("loc_6D4")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_5FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5AB")

    ChrTalk(    #17
        0x13,
        (
            "要是没有塞森，\x01",
            "这家店是绝对开不起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x13,
        (
            "我要感谢\x01",
            "那家伙才行呢。\x02",
        )
    )

    Jump("loc_5A7")

    label("loc_5A7")

    CloseMessageWindow()
    Jump("loc_5F8")

    label("loc_5AB")


    ChrTalk(    #19
        0x13,
        (
            "这家店是塞森\x01",
            "说要开的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x13,
        (
            "他说『与顾客们\x01",
            "多交流交流也不错』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5F8")

    Jump("loc_6D4")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_605")
    Jump("loc_6D4")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_6D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_661")

    ChrTalk(    #21
        0x13,
        "我、我不擅长接待客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        (
            "只要能摆弄导力器，\x01",
            "就觉得很幸福了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4")

    label("loc_661")


    ChrTalk(    #23
        0x13,
        "欢、欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        (
            "那个……\x01",
            "这里是修理窗口。\x02",
        )
    )

    Jump("loc_6A3")

    label("loc_6A3")

    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        (
            "可以帮您修理\x01",
            "损坏的导力器之类的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_6D4")

    TalkEnd(0x13)
    Return()

    # Function_8_533 end

    def Function_9_6D8(): pass

    label("Function_9_6D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_6E5")
    Jump("loc_7FC")

    label("loc_6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_764")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_71D")

    ChrTalk(    #26
        0xFE,
        (
            "……虽然觉得\x01",
            "有点对不起妻子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761")

    label("loc_71D")


    ChrTalk(    #27
        0xFE,
        "我把店都交给妻子打理了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "才刚刚结婚，\x01",
            "这样好吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_761")

    Jump("loc_7FC")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_76E")
    Jump("loc_7FC")

    label("loc_76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7B3")

    ChrTalk(    #29
        0xFE,
        "……我妻子在柜台边。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "请到那边看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FC")

    label("loc_7B3")


    ChrTalk(    #31
        0xFE,
        "……欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "商店在楼上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "……我妻子在柜台边。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_7FC")

    TalkEnd(0xFE)
    Return()

    # Function_9_6D8 end

    SaveToFile()

Try(main)
