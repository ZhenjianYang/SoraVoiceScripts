from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3310   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3310.x',
        MapIndex            = 1,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '士兵布拉姆',                           # 9
        '士兵赫宁',                             # 10
        '派斯队长',                             # 11
        '格温副队长',                           # 12
        '伦法',                                 # 13
        '布鲁诺',                               # 14
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 5990,
        Z                   = 0,
        Y                   = 9340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 7230,
        TriggerZ            = 0,
        TriggerY            = 9350,
        TriggerRange        = 400,
        ActorX              = 6990,
        ActorZ              = 1500,
        ActorY              = 11450,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 7160,
        TriggerRange        = 400,
        ActorX              = -51810,
        ActorZ              = 1500,
        ActorY              = 6820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_23E",          # 01, 1
        "Function_2_23F",          # 02, 2
        "Function_3_246",          # 03, 3
        "Function_4_2EF",          # 04, 4
        "Function_5_A74",          # 05, 5
        "Function_6_A79",          # 06, 6
        "Function_7_1194",         # 07, 7
        "Function_8_1199",         # 08, 8
        "Function_9_11A0",         # 09, 9
        "Function_10_11A5",        # 0A, 10
        "Function_11_1C95",        # 0B, 11
        "Function_12_232A",        # 0C, 12
        "Function_13_2FC0",        # 0D, 13
        "Function_14_32AD",        # 0E, 14
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 3860, 0, 68230, 108)

    label("loc_200")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -51810, 0, 6820, 97)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6990, 0, 11450, 189)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D")
    ClearChrFlags(0xD, 0x80)

    label("loc_23D")

    Return()

    # Function_0_1E2 end

    def Function_1_23E(): pass

    label("Function_1_23E")

    Return()

    # Function_1_23E end

    def Function_2_23F(): pass

    label("Function_2_23F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_2_23F end

    def Function_3_246(): pass

    label("Function_3_246")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_296")

    ChrTalk(    #0
        0xFE,
        (
            "圣海姆门也\x01",
            "好像有地震啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "幸好没有\x01",
            "出现人员伤亡。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB")

    label("loc_296")


    ChrTalk(    #2
        0xFE,
        (
            "听说连圣海姆门那里\x01",
            "之前也出现过地震呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "地震如此频繁，\x01",
            "实在是不正常啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2EB")

    TalkEnd(0xD)
    Return()

    # Function_3_246 end

    def Function_4_2EF(): pass

    label("Function_4_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300")
    Call(0, 12)
    Return()

    label("loc_300")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35E")

    ChrTalk(    #4
        0x9,
        (
            "不管怎样，\x01",
            "没有地震就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "这样的话又可以恢复到\x01",
            "安稳的生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B4")

    label("loc_35E")


    ChrTalk(    #6
        0x9,
        "地震好像已经平息了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "中央工房都已经正式声明了，\x01",
            "那就肯定可以放心了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3B4")

    Jump("loc_A70")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_410")

    ChrTalk(    #8
        0x9,
        (
            "紧急联络\x01",
            "好像发来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "到底是什么事呢，\x01",
            "又想知道又不想知道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455")

    label("loc_410")


    ChrTalk(    #10
        0x9,
        (
            "队长的紧急联络\x01",
            "好像发来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "这、这次\x01",
            "又出了什么事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_455")

    Jump("loc_A70")

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_56B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4BA")

    ChrTalk(    #12
        0x9,
        (
            "我看到的那个可疑男子也好，\x01",
            "地震继续发生也好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        "好像是发生了什么事啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_568")

    label("loc_4BA")


    ChrTalk(    #14
        0x9,
        (
            "呼，不得了了啊。\x01",
            "连圣海姆门也发生地震了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "这样看来的话\x01",
            "地震绝对不是偶然啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "我看到的那个可疑男子也好，\x01",
            "地震继续发生也好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "好像是发生了什么事啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_568")

    Jump("loc_A70")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_END)), "loc_5B5")

    ChrTalk(    #18
        0xFE,
        (
            "能把话说出来\x01",
            "就痛快多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "一会队长那里\x01",
            "也拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A70")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_9C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 5)), scpexpr(EXPR_END)), "loc_611")

    ChrTalk(    #20
        0xFE,
        (
            "对地震的印象太过深刻，\x01",
            "其他的事情都给忘了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "没帮上忙，真抱歉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_611")


    ChrTalk(    #22
        0xFE,
        "嗯，怎么了？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_67C")

    ChrTalk(    #23
        0x106,
        (
            "#050F我们是游击士协会的。\x02\x03",

            "有关３天前的地震，\x01",
            "想向你询问一些事情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_6D1")

    label("loc_67C")


    ChrTalk(    #24
        0x103,
        (
            "#020F我们是游击士协会的人哦。\x02\x03",

            "有关３天前的地震，\x01",
            "有些事想向你打听一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_6D1")


    ChrTalk(    #25
        0xFE,
        (
            "啊啊，那个吗……\x01",
            "真是吓了一跳啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "这还是第一次遇到地震，\x01",
            "当时都不知道发生了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "嗯，你们是来\x01",
            "调查受害状况的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1015F啊，不是的。\x02\x03",

            "嗯…其实是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05询问对方是否在地震前后\x01",
            "发现了什么奇怪的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #30
        0xFE,
        "啊～奇怪的事情……吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "要是那么说的话，\x01",
            "当然是发生地震最奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F啊～不，那当然\x01",
            "没错，不过……\x02\x03",

            "除了地震之外\x01",
            "还有没有别的奇异现象发生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "抱歉，不记得有什么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "对地震的印象太强，\x01",
            "之后的事情全都忘记了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1007F啊……是、是吗…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_931")

    ChrTalk(    #36
        0x106,
        (
            "#053F这样的话，\x01",
            "再问下去也问不出什么了。\x02\x03",

            "#051F打扰啦，\x01",
            "您继续工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_986")

    label("loc_931")


    ChrTalk(    #37
        0x103,
        (
            "#026F那样的话，\x01",
            "再问下去也没用了啊。\x02\x03",

            "#027F真是打扰您了，\x01",
            "请继续工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_986")


    ChrTalk(    #38
        0xFE,
        "啊啊，不好意思啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "那，如果有事\x01",
            "再来问吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x140D)

    label("loc_9BE")

    Jump("loc_A70")

    label("loc_9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A13")

    ChrTalk(    #40
        0xFE,
        (
            "通行手续的话\x01",
            "就去对面的建筑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "和那里的队长说一下\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A70")

    label("loc_A13")


    ChrTalk(    #42
        0xFE,
        "哟，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "通行手续的话\x01",
            "就去对面的建筑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "和那里的队长说一下\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A70")

    TalkEnd(0x9)
    Return()

    # Function_4_2EF end

    def Function_5_A74(): pass

    label("Function_5_A74")

    Call(0, 6)
    Return()

    # Function_5_A74 end

    def Function_6_A79(): pass

    label("Function_6_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A86")
    Call(0, 11)
    Return()

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9F")
    Call(0, 13)
    Return()

    label("loc_A9F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 1)), scpexpr(EXPR_END)), "loc_B1B")

    ChrTalk(    #45
        0xA,
        (
            "士兵们对关不上的大门\x01",
            "感到很不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "但对比一下哈肯大门那里的情况，\x01",
            "这里简直就是轻松的乐园了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C15")

    label("loc_B1B")


    ChrTalk(    #47
        0xA,
        (
            "士兵们对关不上的大门\x01",
            "感到很不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        (
            "但对比一下哈肯大门那里的情况，\x01",
            "这里简直就是轻松的乐园了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "根本就没有必要\x01",
            "那么紧张嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "喔，你们也看看小说\x01",
            "放松一下吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x00得到了\x1F\x46\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x246, 1)
    OP_A2(0x10C1)

    label("loc_C15")

    Jump("loc_1190")

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF3")

    ChrTalk(    #52
        0xA,
        "呀，各位游击士，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "多亏了那些发生器，\x01",
            "通信总算恢复了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "虽然人数不多，但要塞那边\x01",
            "派来了增援的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "马上派他们去亚尔摩村\x01",
            "进行巡逻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "那里离蔡斯比较远，\x01",
            "居民们也更加不安呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_D82")

    label("loc_CF3")


    ChrTalk(    #57
        0xA,
        (
            "增援的士兵们已经被\x01",
            "派遣到亚尔摩村了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "那里离蔡斯比较远，\x01",
            "居民也会更加不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "如果能看到我们王国军过去守卫，\x01",
            "多少也能踏实一些吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D82")

    Jump("loc_1190")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DF2")

    ChrTalk(    #60
        0xA,
        (
            "我们这边也要面对签字仪式，\x01",
            "警备不能松懈下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "算了，反正这里永远也\x01",
            "都是这么清闲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E90")

    label("loc_DF2")


    ChrTalk(    #62
        0xA,
        (
            "地震的事件\x01",
            "总算是解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "虽然还有一些奇怪的事情没搞清楚，\x01",
            "不过之后的调查交给协会就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "我们这边也要面对签字仪式，\x01",
            "警备不能松懈下来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E90")

    Jump("loc_1190")

    label("loc_E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EEC")

    ChrTalk(    #65
        0xA,
        (
            "不过要塞那边\x01",
            "好像有准将在吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "既然如此的话\x01",
            "就完全不必担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F81")

    label("loc_EEC")


    ChrTalk(    #67
        0xA,
        (
            "听说雷斯顿要塞那里\x01",
            "也遭到地震的侵袭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "刚刚才接到那边\x01",
            "的联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "不过要塞那里\x01",
            "好像有准将在吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "既然如此的话\x01",
            "就完全不必担心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F81")

    Jump("loc_1190")

    label("loc_F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_107E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(    #71
        0xA,
        (
            "听说圣海姆门那里\x01",
            "的受害情况并不严重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        (
            "不过再这样下去的话\x01",
            "实在是让人很不安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_FED")


    ChrTalk(    #73
        0xA,
        (
            "呀，各位游击士。\x01",
            "这一阵子真是很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "听说圣海姆门那里\x01",
            "的受害情况并不严重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "嗯，即使如此，\x01",
            "再这么下去的话也让人放心不下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_107B")

    Jump("loc_1190")

    label("loc_107E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(    #76
        0xA,
        (
            "虽然不知道他是否和地震有关联，\x01",
            "不过还是很在意那个奇怪的男子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "我也要把情况\x01",
            "报告给雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "报告给协会的工作\x01",
            "就拜托你们各位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1190")

    label("loc_111B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 3)), scpexpr(EXPR_END)), "loc_1190")

    ChrTalk(    #79
        0xA,
        (
            "我没有接到什么\x01",
            "可疑人物和事件的报告……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "但也许部下们\x01",
            "有什么发现吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        "可以的话你们去问问他们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1190")

    TalkEnd(0xA)
    Return()

    # Function_6_A79 end

    def Function_7_1194(): pass

    label("Function_7_1194")

    Call(0, 8)
    Return()

    # Function_7_1194 end

    def Function_8_1199(): pass

    label("Function_8_1199")

    TalkBegin(0xB)
    TalkEnd(0xB)
    Return()

    # Function_8_1199 end

    def Function_9_11A0(): pass

    label("Function_9_11A0")

    Call(0, 10)
    Return()

    # Function_9_11A0 end

    def Function_10_11A5(): pass

    label("Function_10_11A5")

    TalkBegin(0xC)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "休息\x01",        # 2
            "离开\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120B")
    OP_0D()
    OP_A9(0xAB)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_120B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1224")
    OP_0D()
    OP_A9(0xAA)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_1224")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1235")
    TalkEnd(0xC)
    Return()

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(    #82
        0xC,
        (
            "队长一边吃饭\x01",
            "一边发呆出神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "想想的话，应该是哈肯大门\x01",
            "发生了什么事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "这些事情真是\x01",
            "不愿意去想啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_12FD")

    label("loc_12BD")


    ChrTalk(    #85
        0xC,
        (
            "哈肯大门\x01",
            "发生了什么事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        (
            "这些事情真是\x01",
            "不愿意去想啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FD")

    Jump("loc_1C91")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(    #87
        0xC,
        "啊～不是发呆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "看一下就知道了，\x01",
            "大门现在敞开着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xC,
        (
            "现在可以从共和国那边\x01",
            "自由出入了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_13D1")

    label("loc_1379")


    ChrTalk(    #90
        0xC,
        (
            "想想的话，其实国境线这种东西\x01",
            "本来就是人为划定的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        (
            "不然根本就没有\x01",
            "这些东西的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D1")

    Jump("loc_1C91")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_169D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1524")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_145B")

    ChrTalk(    #92
        0xC,
        (
            "雷斯顿要塞那里好像\x01",
            "发生了地震啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        (
            "难道是发动政变的那些家伙\x01",
            "仍然贼心不死吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E1")

    label("loc_145B")


    ChrTalk(    #94
        0xC,
        (
            "雷斯顿要塞那里好像\x01",
            "发生了地震啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xC,
        (
            "竟然还专门挑选军用设施，\x01",
            "还真是过分啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "难道是发动政变的那些家伙\x01",
            "仍然贼心不死吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_14E1")

    Jump("loc_1521")

    label("loc_14E4")


    ChrTalk(    #97
        0xC,
        "呼～今天没东西吃了吗，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "才来晚了一会，\x01",
            "真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1521")

    Jump("loc_169A")

    label("loc_1524")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156C")
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xC)

    ChrTalk(    #99
        0xC,
        "啊啊！这位客人是！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C2")

    label("loc_156C")


    ChrTalk(    #100
        0xC,
        "嗯……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x108, 500)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xC)

    ChrTalk(    #101
        0xC,
        "啊啊！站在那里的不就是！？\x02",
    )

    CloseMessageWindow()

    label("loc_15C2")


    ChrTalk(    #102
        0x108,
        (
            "#071F哈哈，好久不见了啊。\x02\x03",

            "正好到这附近办事，\x01",
            "顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        "要、要吃些东西吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x108,
        (
            "#070F不了，现在没有\x01",
            "空闲，\x02\x03",

            "不能待太久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        (
            "是、是吗…\x01",
            "没办法，以后有机会的话一定再来啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x108,
        "#070F喔！没问题！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1640)
    OP_A2(0x2)

    label("loc_169A")

    Jump("loc_1C91")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1710")

    ChrTalk(    #107
        0xC,
        (
            "那个大块头的客人\x01",
            "看起来好像也是共和国的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        (
            "我也是出身于那里，\x01",
            "看一眼他的服装就知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1710")


    ChrTalk(    #109
        0xC,
        (
            "忘了具体是哪天了，\x01",
            "来了一位身材巨大的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xC,
        (
            "那位客人的食量就如同\x01",
            "他的外表一样惊人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xC,
        (
            "店里的食物全都\x01",
            "被他吃光了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        (
            "哈哈哈。\x01",
            "那个客人后来就没再来过。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1431)
    OP_A2(0x3)

    label("loc_17BC")

    Jump("loc_1C91")

    label("loc_17BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1892")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1847")

    ChrTalk(    #113
        0xC,
        (
            "这里的客人本来\x01",
            "就很少了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "地震的事情要是再传开\x01",
            "生意就更要进入冰点了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "哈哈哈～\x01",
            "看来我也该去冬眠了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188F")

    label("loc_1847")


    ChrTalk(    #116
        0xC,
        (
            "不知为什么，队长他们\x01",
            "的脸色都不太好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        "还有什么问题吗～？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_188F")

    Jump("loc_1C91")

    label("loc_1892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_1BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7A")
    OP_A2(0x3)
    OP_A2(0x140F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18BB")
    OP_28(0x85, 0x1, 0x800)
    Jump("loc_18BB")

    label("loc_18BB")


    ChrTalk(    #118
        0xC,
        (
            "啊，欢迎光临～\x01",
            "这里是间没有任何特色的酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1000F啊～可以稍微打扰一下吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #120
        0xC,
        "好，什么事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1011F啊，我们是\x01",
            "游击士协会的人。\x02\x03",

            "希望您能配合我们\x01",
            "做个调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "啊，当然可以。\x01",
            "反正现在一个客人也没有。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #123
        (
            "\x07\x05询问对方是否在地震前后\x01",
            "发现了什么奇怪的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #124
        0xC,
        (
            "啊～除了地震之外就没有\x01",
            "什么奇怪的事情发生了～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        (
            "地震刚来的时候\x01",
            "大家都很吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#044F那地震前后\x01",
            "也没有奇怪的事情发生吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 400)

    ChrTalk(    #127
        0xC,
        (
            "嗯…奇怪的事情…\x01",
            "实在是想不起来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "哈，最奇怪的事情也就是\x01",
            "我一直留在店里没出去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        "#1015F啊，是这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #130
        0x105,
        (
            "#043F……看来是没有什么\x01",
            "值得注意的情报啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        "不能帮上你忙十分抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1016F哪里，不用介意。\x02\x03",

            "#1000F谢谢您的配合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_1B7A")


    ChrTalk(    #133
        0xC,
        (
            "我觉得，\x01",
            "没什么太奇怪的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        (
            "无论发生什么，\x01",
            "我一直都会在店里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC4")

    Jump("loc_1C91")

    label("loc_1BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3D")
    OP_A2(0x3)

    ChrTalk(    #135
        0xC,
        "恭候各位的光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xC,
        (
            "如你们所见，\x01",
            "这里是家没有任何特色的酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xC,
        (
            "嘿，有需要的话\x01",
            "就多来坐坐吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C91")

    label("loc_1C3D")


    ChrTalk(    #138
        0xC,
        (
            "啊，欢迎光临～\x01",
            "这里是间没有任何特色的酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xC,
        (
            "嘿，有需要的话\x01",
            "就多来坐坐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C91")

    TalkEnd(0xC)
    Return()

    # Function_10_11A5 end

    def Function_11_1C95(): pass

    label("Function_11_1C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA6")
    Call(0, 14)

    label("loc_1CA6")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, -49720, 0, 6390, 270)
    SetChrPos(0xF7, -49720, 0, 7460, 270)
    SetChrPos(0x104, -48400, 0, 7020, 270)
    SetChrPos(0x105, -49010, 0, 5660, 270)
    OP_6D(-50310, 0, 6810, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #140
        0xA,
        "#6P啊，你们是游击士吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xA,
        (
            "#6P协会通知过我们，\x01",
            "这次是来调查『地震』的事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1004F啊，是啊……\x02\x03",

            "#1016F真不愧是雾香姐，\x01",
            "安排得这么周到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "#6P哈哈，我们平时也是多次\x01",
            "承蒙她的帮助呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        (
            "#6P你们的调查工作\x01",
            "我一定会全力配合的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E73")

    ChrTalk(    #145
        0x106,
        (
            "#051F那可谢谢了。\x02\x03",

            "那可以先把地震的发生情况\x01",
            "详细地说给我们听吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1E73")


    ChrTalk(    #146
        0x103,
        (
            "#020F那就谢谢啦。\x02\x03",

            "那可以先把地震的发生情况\x01",
            "详细说给我们听听吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB9")


    ChrTalk(    #147
        0xA,
        "#6P这个啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "#6P地震的发生时间\x01",
            "大概是３天前的下午５点左右。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        (
            "#6P震动并不算太强烈，\x01",
            "而且只持续了１０秒而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        (
            "#6P但这里以前从没发生过地震，\x01",
            "所以在军中还是引起了不小的骚动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        "#6P之后，当天夜里──\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xA,
        (
            "#6P在我们和雷斯顿要塞进行定期联络时，\x01",
            "发现了一个奇妙的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x105,
        (
            "#043F是不是其他的地方\x01",
            "完全没有发生地震？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        "#6P啊，正是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#6P不但雷斯顿要塞没有发生地震，\x01",
            "连圣海姆门那边也没有任何震动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "#6P蔡斯市和亚尔摩村\x01",
            "也都一样没有发生任何地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1002F原来如此……\x02\x03",

            "对了，今天蔡斯市发生地震了，\x01",
            "您听说了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        "#6P啊，这个已经听说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "#6P只是这次我们这边\x01",
            "完全没有任何摇晃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x104,
        (
            "#035F#2P范围极端狭小，\x01",
            "而且场所会转移的局部地震吗……\x02\x03",

            "#030F果然是非常诡异啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21EF")

    ChrTalk(    #161
        0x106,
        (
            "#053F地震的情况我们已经了解了。\x02\x03",

            "#050F除此之外还有没有发生过\x01",
            "什么不正常的事件？\x02\x03",

            "比如看见过奇怪的人之类的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2264")

    label("loc_21EF")


    ChrTalk(    #162
        0x103,
        (
            "#026F地震的情况我们已经了解啦。\x02\x03",

            "#022F除此以外还有什么\x01",
            "值得注意的事情发生吗？\x02\x03",

            "比如目击到什么可疑人物之类的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2264")


    ChrTalk(    #163
        0xA,
        (
            "#6P嗯……\x01",
            "我没有收到什么重要的报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "#6P不过也许我的部下们\x01",
            "有什么发现吧，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        "#6P你们自己去问问就可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1006F嗯，多谢您了。\x02\x03",

            "我们这就去向\x01",
            "士兵们打听一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x140C)
    OP_28(0x85, 0x1, 0x40)
    OP_28(0x85, 0x1, 0x80)
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_11_1C95 end

    def Function_12_232A(): pass

    label("Function_12_232A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_233B")
    Call(0, 14)

    label("loc_233B")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x105, 6250, 0, 69020, 270)
    SetChrPos(0x101, 5250, 0, 68630, 270)
    SetChrPos(0xF7, 5320, 0, 67540, 270)
    SetChrPos(0x104, 6400, 0, 67950, 270)
    OP_6D(4490, 0, 68450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 5)), scpexpr(EXPR_END)), "loc_2423")

    ChrTalk(    #167
        0x9,
        "#5P啊，还有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1002F#2P嗯，我们从布拉姆\x01",
            "那里听到了一些情报……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_258B")

    label("loc_2423")


    ChrTalk(    #169
        0x9,
        "#5P嗯，有什么事？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_248E")

    ChrTalk(    #170
        0x106,
        (
            "#051F我们是游击士协会的人。\x02\x03",

            "有关３天前的地震，\x01",
            "想向你询问一些事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DA")

    label("loc_248E")


    ChrTalk(    #171
        0x103,
        (
            "#020F我们是游击士协会的人。\x02\x03",

            "有关３天前的地震，\x01",
            "有些事想向你打听一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DA")


    ChrTalk(    #172
        0x9,
        (
            "#5P啊啊，那个吗……\x01",
            "真是吓了一跳啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x9,
        (
            "#5P地震还是第一次遇到，\x01",
            "当时都不知道发生了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        "#5P嗯，还想问什么吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1002F#2P嗯，我们从布拉姆\x01",
            "那里听到了一些情报……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #176
        (
            "\x07\x05把门卫布拉姆所说的话\x01",
            "告诉赫宁。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #177
        0x9,
        "#5P啊，是那件事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "#5P嗯，我确实是那么\x01",
            "问过他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x105,
        (
            "#040F就是『有没有人\x01",
            "通过大门？』对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        "#5P嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        (
            "#5P在４天前……\x01",
            "也就是地震发生的前一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#5P我值班结束，正要回休息所的时候，\x01",
            "忽然看到从街道那边走来一名奇怪的男子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1004F#2P奇怪的男子……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x104,
        (
            "#030F#6P是不是一个戴着面具，\x01",
            "身穿白衣的男子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        "#5P面、面具？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#5P就算是奇怪\x01",
            "也不会奇怪到那种程度啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        (
            "#5P是个身穿黑色外套，\x01",
            "个子很高的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        "#5P而且还戴着黑色的眼镜。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2839")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在蔡斯看过瓦鲁特的情报】\x01",          # 0
            "【◇没有在蔡斯看过瓦鲁特的情报】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2824"),
        (1, "loc_282A"),
        (SWITCH_DEFAULT, "loc_2830"),
    )


    label("loc_2824")

    OP_A2(0x1480)
    Jump("loc_2830")

    label("loc_282A")

    OP_A3(0x1480)
    Jump("loc_2830")

    label("loc_2830")

    FadeToBright(300, 0)

    label("loc_2839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_END)), "loc_290F")

    ChrTalk(    #189
        0x101,
        (
            "#1004F#2P黑色的眼镜……\x02\x03",

            "那个好像是叫做\x01",
            "墨镜是吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x85, 0x1, 0x200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_28CA")

    ChrTalk(    #190
        0x106,
        (
            "#555F啊啊……\x02\x03",

            "那种东西很稀有，\x01",
            "看来和之前听说的是同一个人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290C")

    label("loc_28CA")


    ChrTalk(    #191
        0x103,
        (
            "#022F嗯……\x02\x03",

            "这种东西很少见，\x01",
            "看来和之前听说的是同一个人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290C")

    Jump("loc_2BE2")

    label("loc_290F")


    ChrTalk(    #192
        0x101,
        (
            "#1015F#2P黑色的眼镜……\x02\x03",

            "是指镜架是\x01",
            "黑颜色的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x9,
        "#5P不、不是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x9,
        (
            "#5P镜片的部分\x01",
            "也是纯黑的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1004F#2P那、那样的话\x01",
            "岂不是看不见前边了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x85, 0x1, 0x400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A34")

    ChrTalk(    #196
        0x106,
        (
            "#555F那个东西…\x01",
            "大概就是所谓的『墨镜』了。\x02\x03",

            "据说那东西可以\x01",
            "挡住强烈的日光照射。\x02\x03",

            "而且还不会影响\x01",
            "前方的视线。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACC")

    label("loc_2A34")


    ChrTalk(    #197
        0x103,
        (
            "#020F那大概就是传闻中一种\x01",
            "叫做墨镜的眼镜了吧。\x02\x03",

            "据说那东西\x01",
            "有着抵挡太阳光的功效，\x02\x03",

            "虽然戴上那个后视线多少会受一些影响，\x01",
            "但看清楚前方还是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACC")


    ChrTalk(    #198
        0x104,
        (
            "#035F#6P我也听说过那个，\x01",
            "不过可不是随便就能搞到的东西啊。\x02\x03",

            "#030F在帝都的黑街上倒是看见\x01",
            "黑道的头目们戴过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1007F#2P真、真是听起来就危险的东西呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #200
        0x101,
        (
            "#1019F#5P可话说回来，你为什么会\x01",
            "认识那些危险的人物呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x104,
        (
            "#031F#6P哼哼……\x01",
            "常言道『蛇走蛇道，鬼走鬼道』嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE2")


    ChrTalk(    #202
        0x9,
        (
            "#5P啊，原来那个奇怪的黑眼镜\x01",
            "叫做墨镜啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #203
        0x9,
        (
            "#5P我继续说刚才的话，就在我要进休息所时，\x01",
            "忽然看见那家伙从街道那边走来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x9,
        (
            "#5P一般来说，途经这里的人\x01",
            "都会进这酒馆里休息一下，所以我\x01",
            "以为他很快就会进来，就先进去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x105,
        (
            "#043F可是……\x01",
            "那个人就再没出现，对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        "#5P啊啊，正是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#5P然后我就去问布拉姆，\x01",
            "结果他也说没有人通过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "#5P那家伙虽然经常偷懒打磕睡，\x01",
            "但毕竟不至于连有人通过大门\x01",
            "都察觉不到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x104,
        (
            "#030F#6P嗯，但也有可能是他\x01",
            "直接去了兵舍那边吧？\x02\x03",

            "也许他是有事找队长呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        (
            "#5P我当时感到很蹊跷，\x01",
            "就去问过了队长和副队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x9,
        (
            "#5P但他们都说那一段时间内\x01",
            "没人来访过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "#5P可这样的话，我看见的那个男人\x01",
            "到底是来干什么的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x9,
        (
            "#5P每次一想起这件事\x01",
            "我的头脑就一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1002F#2P嗯…确实是个很奇怪的家伙呢。\x02\x03",

            "我们就把这件事\x01",
            "报告给雾香姐吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F30")

    ChrTalk(    #215
        0x106,
        (
            "#053F啊……\x01",
            "就那么办吧。\x02\x03",

            "#051F多谢您提供的情报啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F67")

    label("loc_2F30")


    ChrTalk(    #216
        0x103,
        (
            "#020F嗯……\x01",
            "就这么办吧。\x02\x03",

            "#021F感谢您提供的情报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F67")


    ChrTalk(    #217
        0x9,
        "#5P哪里哪里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x9,
        (
            "#5P你们来问这些，\x01",
            "我也松了口气呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1411)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FB9")
    OP_28(0x85, 0x1, 0x800)
    Jump("loc_2FB9")

    label("loc_2FB9")

    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_12_232A end

    def Function_13_2FC0(): pass

    label("Function_13_2FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FD1")
    Call(0, 14)

    label("loc_2FD1")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, -49720, 0, 6390, 270)
    SetChrPos(0xF7, -49720, 0, 7460, 270)
    SetChrPos(0x104, -48400, 0, 7020, 270)
    SetChrPos(0x105, -49010, 0, 5660, 270)
    OP_6D(-50310, 0, 6810, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #219
        0xA,
        (
            "#6P啊，是你们啊。\x01",
            "从部下那里打探到了什么有用的情报吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#1002F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #221
        (
            "\x07\x05把有关墨镜男子的目击情报\x01",
            "报告给了队长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #222
        0xA,
        (
            "#6P嗯…赫宁那小子，\x01",
            "看见了那样的男子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        (
            "#6P虽然还不知道他是否和地震\x01",
            "有关系，不过确实是个很可疑的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xA,
        (
            "#6P那我们这边也\x01",
            "报告给雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3214")

    ChrTalk(    #225
        0x106,
        "#050F啊，那就拜托啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #226
        0x106,
        (
            "#051F那么……\x01",
            "这里的调查就算是告一段落了，\x02\x03",

            "这就回蔡斯\x01",
            "向雾香报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327D")

    label("loc_3214")


    ChrTalk(    #227
        0x103,
        "#020F嗯，拜托您了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #228
        0x103,
        (
            "#526F那么……\x01",
            "这里的调查算是完成了。\x02\x03",

            "我们这就回蔡斯\x01",
            "向雾香报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327D")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #229
        0x101,
        "#1006F#4P嗯！了解。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    OP_A2(0x1412)
    OP_28(0x85, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_13_2FC0 end

    def Function_14_32AD(): pass

    label("Function_14_32AD")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_3327"),
        (1, "loc_332D"),
        (SWITCH_DEFAULT, "loc_3333"),
    )


    label("loc_3327")

    OP_A2(0x1200)
    Jump("loc_3333")

    label("loc_332D")

    OP_A2(0x1201)
    Jump("loc_3333")

    label("loc_3333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3341")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3345")

    label("loc_3341")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3345")

    Return()

    # Function_14_32AD end

    SaveToFile()

Try(main)
