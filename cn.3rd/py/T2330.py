from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2330   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2330.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2330   ._SN',
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
        '雷克斯',                               # 9
        '卡拉',                                 # 10
        '',                                     # 11
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_144",          # 02, 2
        "Function_3_149",          # 03, 3
        "Function_4_4D3",          # 04, 4
        "Function_5_4D8",          # 05, 5
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Return()

    # Function_0_142 end

    def Function_1_143(): pass

    label("Function_1_143")

    Return()

    # Function_1_143 end

    def Function_2_144(): pass

    label("Function_2_144")

    Call(0, 3)
    Return()

    # Function_2_144 end

    def Function_3_149(): pass

    label("Function_3_149")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17B")

    ChrTalk(    #0
        0x10,
        "玩的时候注意别受伤哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E1")

    label("loc_17B")


    ChrTalk(    #1
        0x10,
        "咦？　波利呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "在和克拉姆他们一块玩吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "虽然有精神是好事，\x01",
            "但要注意别受伤哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1E1")

    Jump("loc_4CF")

    label("loc_1E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_2F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_238")

    ChrTalk(    #4
        0x10,
        "一会儿得去看看才行呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "好东西是不是\x01",
            "都已经卖掉了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF")

    label("loc_238")


    ChrTalk(    #6
        0x10,
        "咦，你们好像很开心呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "是不是在义卖会\x01",
            "找到什么好东西了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x14E,
        "#1711F这是秘密——！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14F,
        "#1732F是秘密——！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "啊哈哈，\x01",
            "看来一会儿得去看看才行呢。\x02",
        )
    )

    Jump("loc_2EB")

    label("loc_2EB")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2EF")

    Jump("loc_4CF")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_4C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 1)), scpexpr(EXPR_END)), "loc_3FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_347")

    ChrTalk(    #11
        0x10,
        (
            "卢西亚应该也在义卖会帮忙吧。\x01",
            "如果有空的话就去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F7")

    label("loc_347")


    ChrTalk(    #12
        0x10,
        (
            "你知道吗？\x01",
            "今天开始要举办义卖会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "虽然『义卖会』听起来挺土的，\x01",
            "不过村子里还真有节日的气氛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "卢西亚应该也去义卖会帮忙了吧。\x01",
            "如果有空的话就去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3F7")

    Jump("loc_4C5")

    label("loc_3FA")


    ChrTalk(    #15
        0x10,
        (
            "哎呀，\x01",
            "这不是玛丽和波利吗。\x02",
        )
    )

    Jump("loc_425")

    label("loc_425")

    CloseMessageWindow()

    ChrTalk(    #16
        0x14E,
        (
            "#1718F啊，雷克斯先生，\x01",
            "您好～。\x02",
        )
    )

    Jump("loc_458")

    label("loc_458")

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "谢谢你经常\x01",
            "陪我家的卢西亚玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14F,
        "#1732F不客气～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "哈哈，\x01",
            "你们还是那么精神呢。\x02",
        )
    )

    Jump("loc_4C1")

    label("loc_4C1")

    CloseMessageWindow()
    OP_A2(0x2F41)

    label("loc_4C5")

    Jump("loc_4CF")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_4CF")

    label("loc_4CF")

    TalkEnd(0x10)
    Return()

    # Function_3_149 end

    def Function_4_4D3(): pass

    label("Function_4_4D3")

    Call(0, 5)
    Return()

    # Function_4_4D3 end

    def Function_5_4D8(): pass

    label("Function_5_4D8")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 2)), scpexpr(EXPR_END)), "loc_592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_51F")

    ChrTalk(    #20
        0x11,
        (
            "天黑之前要回去哦。\x02\x03",

            "老师会担心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F")

    label("loc_51F")


    ChrTalk(    #21
        0x11,
        (
            "回去太晚\x01",
            "特蕾莎老师就会担心的。\x02",
        )
    )

    Jump("loc_551")

    label("loc_551")

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "玩得差不多了就要早点回去哦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        "#1713F……好。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_58F")

    Jump("loc_644")

    label("loc_592")


    ChrTalk(    #24
        0x11,
        (
            "哎呀？　玛丽就你一个人？\x02\x03",

            "……波利呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x14E,
        (
            "#1713F那、那个，\x01",
            "和克拉姆他们在一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "是吗，玩的时候要小心哦。\x02\x03",

            "别太靠近悬崖边上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x14E,
        "#1712F……是、是！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F42)

    label("loc_644")

    Jump("loc_800")

    label("loc_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_69E")

    ChrTalk(    #28
        0x11,
        "下次要再来和卢西亚玩哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "那孩子\x01",
            "也非常开心呢。\x02",
        )
    )

    Jump("loc_69A")

    label("loc_69A")

    CloseMessageWindow()
    Jump("loc_72D")

    label("loc_69E")


    ChrTalk(    #30
        0x11,
        "哎呀？　好像很开心呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        "发生什么好事情了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x14E,
        "#1711F没什么——！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14F,
        "#1732F没什么啦——！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "呵呵，异口同声啊～。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_72D")

    Jump("loc_800")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(    #35
        0x11,
        "卢西亚也很喜欢参加活动呢～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "这点到底是像谁呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6")

    label("loc_77F")


    ChrTalk(    #37
        0x11,
        (
            "哎呀，玛丽和波利，\x01",
            "欢迎光临！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "要找卢西亚的话，\x01",
            "她在义卖会帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        "那孩子也很喜欢参加活动呢～。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7F6")

    Jump("loc_800")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_800")

    label("loc_800")

    TalkEnd(0x11)
    Return()

    # Function_5_4D8 end

    SaveToFile()

Try(main)
