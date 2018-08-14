from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7003_4 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7003.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_13FD",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_47B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1A)
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_51(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_143")
    Jump("loc_185")

    label("loc_143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15F")
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_15F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B")
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_17B")

    OP_51(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185")

    OP_51(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7")

    ChrTalk(    #0
        0x1A,
        (
            "#074F只要离开这个庭院，\x01",
            "就无法返回了。\x02\x03",

            "#072F大概也没有能够\x01",
            "补充装备的地方吧。\x02\x03",

            "#070F趁现在做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1")

    ChrTalk(    #1
        0x1A,
        (
            "#073F啊啊，还有……\x02\x03",

            "#070F刚才始祖大人\x01",
            "似乎发现了新的领域。\x02\x03",

            "最好去问问她\x01",
            "详细情况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1")

    OP_A2(0xD)
    Jump("loc_470")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8")

    ChrTalk(    #2
        0x1A,
        (
            "#074F装备、道具的调配\x01",
            "以及导力盘的调整……\x01",
            "全都来自『庭院』的力量。\x02\x03",

            "#070F只要离开这里，\x01",
            "大概就无法享受这些恩惠了。\x02\x03",

            "趁现在做好万全的准备吧。\x02\x03",

            "#573F还有……刚才始祖大人\x01",
            "似乎发现了新的领域。\x02\x03",

            "#070F最好去问问她\x01",
            "详细的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_470")

    label("loc_3C8")


    ChrTalk(    #3
        0x1A,
        (
            "#074F装备、道具的调配\x01",
            "以及导力盘的调整……\x01",
            "全都来自『庭院』的力量。\x02\x03",

            "#070F只要离开这里，\x01",
            "大概就无法享受这些恩惠了。\x02\x03",

            "趁现在做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_470")

    SetChrSubChip(0x1A, 0)
    TalkEnd(0x1A)
    Jump("loc_13FC")

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #4
        0x1A,
        (
            "#074F………………………………\x02\x03",

            "呼，还是弄不清楚怎么回事。\x02\x03",

            "#072F如果一切的元凶都是『影之王』……\x01",
            "他到底是怎么打算的？\x02\x03",

            "#074F能够满足人们愿望的世界……\x01",
            "在这以上还能希望什么呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_675")

    label("loc_56B")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0x1A,
        (
            "#075F呼，费脑子的事\x01",
            "本来就不是我的任务。\x02\x03",

            "#070F如果有雾香在的话，\x01",
            "一定会得到不少帮助的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_610")

    ChrTalk(    #6
        0x101,
        "#1001F啊哈哈，没错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_644")

    ChrTalk(    #7
        0x102,
        "#1501F的确是这样呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_644")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_675")

    ChrTalk(    #8
        0x103,
        "#1536F呵呵，说的没错。\x02",
    )

    CloseMessageWindow()

    label("loc_675")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_13FC")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_B7D")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_717")
    Jump("loc_759")

    label("loc_717")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_733")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_759")

    label("loc_733")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_759")

    label("loc_74F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_759")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(    #9
        0x1A,
        (
            "#074F卡西乌斯大人的战斗能力\x01",
            "远远超过一般人……\x02\x03",

            "#072F但是，他强大的真正理由是\x01",
            "能够看穿事物本质。\x02\x03",

            "所以不管是作为游击士\x01",
            "还是军队的司令官，\x01",
            "都能够完全发挥其所有的力量。\x02\x03",

            "#573F简直是将『理』\x01",
            "臻至完美的人。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A8")

    ChrTalk(    #10
        0x102,
        "#1513F没错呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EA")

    label("loc_8A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(    #11
        0x10D,
        "#278F原来如此……可以说是不同次元的吗。\x02",
    )

    CloseMessageWindow()

    label("loc_8EA")

    Jump("loc_9F3")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 7)), scpexpr(EXPR_END)), "loc_998")

    ChrTalk(    #12
        0x1A,
        (
            "#074F瓦鲁特那家伙……\x01",
            "现在到底在哪里干什么呢。\x02\x03",

            "#070F不过似乎他也在\x01",
            "打听雾香的消息……\x02\x03",

            "#573F唉，如果有想说的话，\x01",
            "自己直接说不就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3")

    label("loc_998")


    ChrTalk(    #13
        0x1A,
        (
            "#572F是吗，瓦鲁特那家伙……\x02\x03",

            "#075F呼，\x01",
            "他现在到底在哪里干什么呢。\x02",
        )
    )

    Jump("loc_9F2")

    label("loc_9F2")

    CloseMessageWindow()

    label("loc_9F3")

    OP_A2(0xD)
    Jump("loc_B72")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69")

    ChrTalk(    #14
        0x1A,
        (
            "#074F要是我想到达那种境地，\x01",
            "需要花费多少功夫呢……\x02\x03",

            "#070F哎呀，还得进一步努力呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72")

    label("loc_A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFB")

    ChrTalk(    #15
        0x1A,
        (
            "#074F嗯，接下来就是\x01",
            "第四名『守护者』了吗……\x02\x03",

            "#070F……约修亚。\x01",
            "鼓足干劲冲吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1500F…………是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_B72")

    label("loc_AFB")


    ChrTalk(    #17
        0x1A,
        (
            "#070F嗯，接下来就是\x01",
            "第四名『守护者』了吗……\x02\x03",

            "#573F呼，都来到这里了，\x01",
            "就算再说什么\x01",
            "也是毫无用处的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B72")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_13FC")

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_EB2")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C14")
    Jump("loc_C56")

    label("loc_C14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C30")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C56")

    label("loc_C30")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C4C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C56")

    label("loc_C4C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C56")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 1)), scpexpr(EXPR_END)), "loc_D00")

    ChrTalk(    #18
        0x1A,
        (
            "#075F呼，唉…………\x02\x03",

            "我总有种回去之后一定会被\x01",
            "雾香那家伙大骂一顿的预感……\x01",
            "……是太过敏感了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB9")

    label("loc_D00")


    ChrTalk(    #19
        0x1A,
        (
            "#573F……你们和雾香战斗过了吗。\x02\x03",

            "#070F呵呵，她很强吧。\x02\x03",

            "一旦她拿起擅长的武器，\x01",
            "就比瓦鲁特更难对付。\x02\x03",

            "#075F就算不继承泰斗流的话，\x01",
            "估计也很难嫁得出去……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB9")

    OP_A2(0xD)
    Jump("loc_EA7")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 1)), scpexpr(EXPR_END)), "loc_E1A")

    ChrTalk(    #20
        0x1A,
        (
            "#074F雾香这个人\x01",
            "也是不肯认输的……\x02\x03",

            "#075F以后一定会伺机报复。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA7")

    label("loc_E1A")


    ChrTalk(    #21
        0x1A,
        (
            "#070F本来以为她这么长时间\x01",
            "都在专心担当协会的接待，\x02\x03",

            "战斗力应该会有所减弱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        "#1068F……唉，还真是不可小看啊。\x02",
    )

    CloseMessageWindow()

    label("loc_EA7")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_13FC")

    label("loc_EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_FE8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(    #23
        0x1A,
        (
            "#074F在帝国和共和国\x01",
            "都存在协会的设施。\x02\x03",

            "不过，竟然连卢·洛克尔的\x01",
            "训练场都再现得一模一样……\x02\x03",

            "#072F也许是故意选中那些\x01",
            "与我们关系密切的场所吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_FE2")

    label("loc_F72")


    ChrTalk(    #24
        0x1A,
        (
            "#572F列曼自治州\x01",
            "距离利贝尔相当遥远……\x02\x03",

            "#074F嗯，也许是故意选中那些\x01",
            "与我们关系密切的场所吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE2")

    TalkEnd(0xFE)
    Jump("loc_13FC")

    label("loc_FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_13FC")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #25
        0x1A,
        (
            "#070F说起来，约修亚……\x01",
            "我们好像很久都没见了呢。\x02\x03",

            "你好像去过克洛斯贝尔，\x01",
            "不想来卡尔瓦德参观一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1513F嗯，有机会的话\x01",
            "我一定会去的。\x02\x03",

            "#1503F不过，\x01",
            "现在我正和艾丝蒂尔在找人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1A,
        "#074F唔……好像发生了很多事呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #28
        0x102,
        (
            "#1504F说起来……\x01",
            "雪拉姐姐的信里面提到过，\x01",
            "雾香小姐已经回国去了吧。\x02\x03",

            "#1500F好像是受到了共和国政府的征召，\x01",
            "辞去了协会的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1079F雾香小姐，\x01",
            "是蔡斯支部的那位吗……\x02\x03",

            "#1078F哎……有这回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1A,
        (
            "#070F是啊……\x01",
            "她好像正忙于新的工作呢。\x02\x03",

            "#075F……以她的性格，\x01",
            "无论如何都不会偷懒的。\x02\x03",

            "她那么精明强干，\x01",
            "肯定已经让同事和部下佩服得五体投地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1509F哈哈……\x01",
            "真像雾香小姐的作风啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2661)
    Jump("loc_13F9")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1394")

    ChrTalk(    #32
        0x1A,
        (
            "#074F可是，没想到\x01",
            "这样的事也能发生于现实之中……\x02\x03",

            "#070F不过，\x01",
            "多亏了你们的努力，\x01",
            "已经弄清了一些事情。\x02\x03",

            "现在也只有以这些为线索\x01",
            "继续前进了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_13F9")

    label("loc_1394")


    ChrTalk(    #33
        0x1A,
        (
            "#070F多亏了你们的努力，\x01",
            "已经弄清了一些事情。\x02\x03",

            "现在也只有以这些为线索\x01",
            "继续前进了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F9")

    TalkEnd(0xFE)

    label("loc_13FC")

    Return()

    # Function_2_AC end

    def Function_3_13FD(): pass

    label("Function_3_13FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_1521")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A1")

    ChrTalk(    #34
        0x1F,
        (
            "#119F呵呵……\x01",
            "我也不能输给大家。\x02\x03",

            "#110F对现在的我来说，\x01",
            "有非完成不可的事情……\x02\x03",

            "差不多该和『影之王』\x01",
            "一决胜负了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_151B")

    label("loc_14A1")


    ChrTalk(    #35
        0x1F,
        (
            "#110F经过与『黑骑士』的战斗后……\x01",
            "所有的棋子应该都已经用完了。\x02\x03",

            "#115F差不多该和『影之王』\x01",
            "一决胜负了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151B")

    TalkEnd(0xFE)
    Jump("loc_25E1")

    label("loc_1521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_16C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FD")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #36
        0x1F,
        "#115F………………是你们啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #37
        0x1F,
        (
            "#110F我必须得\x01",
            "好好感谢你们才行。\x02\x03",

            "多亏了你们，\x01",
            "我才能够越过一道巨大的障碍。\x02\x03",

            "#111F……那么，继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0xA)
    TalkEnd(0xFE)
    Jump("loc_16C1")

    label("loc_15FD")

    TalkBegin(0xFE)

    ChrTalk(    #38
        0x1F,
        (
            "#115F……自从那次事件以来，\x01",
            "我一直踌躇不定。\x02\x03",

            "#116F也许是因为\x01",
            "我对准将的敬佩之心\x01",
            "导致我无法找到属于自己的答案。\x02\x03",

            "#110F不过，障碍已经越过了……\x01",
            "大家一起继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_16C1")

    Jump("loc_25E1")

    label("loc_16C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_1876")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 0)), scpexpr(EXPR_END)), "loc_175E")

    ChrTalk(    #39
        0x1F,
        (
            "#115F菲利普大人退役\x01",
            "应该是２０多年前的事了，\x01",
            "但现在他的功夫还那么厉害……\x02\x03",

            "#111F呵呵，很久没有如此振奋了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F5")

    label("loc_175E")


    ChrTalk(    #40
        0x1F,
        (
            "#110F在情报部的时候，\x01",
            "我也调查过菲利普大人的经历。\x02\x03",

            "拥有五种神技的『剑狐』……\x02\x03",

            "#119F他大展身手的时候，\x01",
            "已经是２０多年前了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F5")

    OP_A2(0xA)
    Jump("loc_1870")

    label("loc_17FB")


    ChrTalk(    #41
        0x1F,
        (
            "#115F菲利普大人很久之前\x01",
            "为了专心照顾杜南公爵阁下\x01",
            "而选择了退役……\x02\x03",

            "不过现在的身手依然不减当年呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1870")

    TalkEnd(0xFE)
    Jump("loc_25E1")

    label("loc_1876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_1A10")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1982")

    ChrTalk(    #42
        0x1F,
        (
            "#115F凯文神父……\x02\x03",

            "你的身体已经没事了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1060F嗯，没什么问题了。\x02\x03",

            "#1840F让你们这么担心，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x1F,
        (
            "#111F不，这样就好了。\x02\x03",

            "#110F因为你倒下的时候\x01",
            "我不在现场，\x01",
            "所以只是有点在意而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1A0A")

    label("loc_1982")


    ChrTalk(    #45
        0x1F,
        (
            "#115F呼，不过，\x01",
            "赛雷斯托大人也不知道那些蒙面人\x01",
            "是如何进到这里来的吗……\x02\x03",

            "现在就算我们怎么推测，\x01",
            "也不可能明白事实的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0A")

    TalkEnd(0xFE)
    Jump("loc_25E1")

    label("loc_1A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_1F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #46
        0x1F,
        (
            "#115F（…………没错，\x01",
            "  我还远没有成熟。）\x02\x03",

            "#116F（总是抱着\x01",
            "  这样的心态\x01",
            "  是不行的……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1015F上校，你怎么了？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E14")

    ChrTalk(    #48
        0x1F,
        "#110F……没什么，稍微想点事情。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x110,
        (
            "#260F呵呵，\x01",
            "你还在意着刚才的话吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1F,
        (
            "#111F哈哈，\x01",
            "玲的洞察力还真是惊人。\x02\x03",

            "#110F……怎么样，\x01",
            "不想来我们的公司吗？\x02\x03",

            "像你这样能看透人心思的人才\x01",
            "我们十分欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x110,
        (
            "#267F唔，这么说的话……\x02\x03",

            "#260F如果你愿意和玲再玩一次的话，\x01",
            "我就考虑考虑。\x02\x03",

            "#261F在格兰赛尔城的那次\x01",
            "最后没分出胜负呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA5")
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #52
        0x107,
        "#562F玲……\x02",
    )

    CloseMessageWindow()

    label("loc_1CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D36")

    ChrTalk(    #53
        0x105,
        (
            "#1165F（说、说起来\x01",
            "  在结社袭击王都的时候，\x01",
            "  他们两个曾经对决过呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1016F（啊……嗯，好像是……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DE0")

    label("loc_1D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D89")

    ChrTalk(    #55
        0x102,
        (
            "#1514F（对了，执行者袭击王都的时候，\x01",
            "  他们两个……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE0")

    label("loc_1D89")


    ChrTalk(    #56
        0x101,
        (
            "#1016F（说、说起来\x01",
            "  这两个人在结社袭击王都的时候\x01",
            "  曾经交过一次手呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE0")


    ChrTalk(    #57
        0x1F,
        (
            "#111F哈、哈哈哈……\x01",
            "拜托你手下留情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F01")

    label("loc_1E14")


    ChrTalk(    #58
        0x1F,
        (
            "#111F……没什么，稍微想点事情。\x02\x03",

            "#110F执行者Ｎｏ．ⅩⅤ，\x01",
            "『歼灭天使』玲……\x02\x03",

            "虽然以前也听说过传言，\x01",
            "不过洞察力还真非同寻常……\x02\x03",

            "#115F呼，\x01",
            "真希望她能加入我们公司啊。\x02",
        )
    )

    Jump("loc_1EDF")

    label("loc_1EDF")

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1016F啊哈哈…………\x02",
    )

    CloseMessageWindow()

    label("loc_1F01")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x266B)
    TalkEnd(0xFE)
    Jump("loc_1F8E")

    label("loc_1F0F")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #60
        0x1F,
        (
            "#115F（…………没错，\x01",
            "  我还远没有成熟。）\x02\x03",

            "#116F（这样的心，\x01",
            "  这样的心态\x01",
            "  是不行的……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1F8E")

    Jump("loc_25E1")

    label("loc_1F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B7")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #61
        0x1F,
        (
            "#115F……呼………………\x01",
            "的确到处都是奇妙的东西呢。\x02\x03",

            "……果然是异空间吗………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1011F那个，\x01",
            "上校你不相信吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #63
        0x1F,
        (
            "#110F艾丝蒂尔……\x02\x03",

            "#119F不好意思，\x01",
            "我还一直没有摸着头脑。\x02\x03",

            "要想找到有效的攻略法，\x01",
            "还需要一些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1016F攻、攻略法……\x02\x03",

            "不愧是上校，还能这么冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x1F,
        (
            "#495F哎呀，\x01",
            "都说我已经不是上校了。\x02\x03",

            "……我已经从军队中退伍了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1015F啊，说起来……\x02\x03",

            "好像是在经营一家\x01",
            "民间的调查公司对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x1F,
        (
            "#111F嗯，\x01",
            "虽然还算不上什么大公司……\x02\x03",

            "#110F现在只是在卢安\x01",
            "拥有一家小型的事务所。\x02\x03",

            "一切事务都由我和凯诺娜\x01",
            "两个人来处理。\x02",
        )
    )

    Jump("loc_2246")

    label("loc_2246")

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1004F咦…………？\x01",
            "那个凯诺娜上尉吗！？\x02\x03",

            "#1007F唔，\x01",
            "真是想象不出来……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x1F,
        (
            "#111F哈哈哈……\x01",
            "也许正如你所说的那样。\x02\x03",

            "#119F……不过，\x01",
            "她也已经有所改变了。\x02\x03",

            "现在总算能\x01",
            "无拘无束地悠闲一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1008F是吗……\x02\x03",

            "#1012F嗯，我觉得上校\x01",
            "给人的感觉也和以前不一样了。\x02\x03",

            "#1001F也许的确比较适合\x01",
            "开这样的民间公司吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x1F,
        "#111F呵呵，如果是这样就好了……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #72
        0x1F,
        (
            "#110F……不过这样一来\x01",
            "我们就更不能一直待在这里。\x02\x03",

            "要早点回去才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1006F…………嗯。\x02\x03",

            "#1018F那就请多关照了，上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x1F,
        "#495F（都说不是上校了……）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x266A)
    TalkEnd(0xFE)
    Jump("loc_25E1")

    label("loc_24B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257A")
    OP_A2(0xA)

    ChrTalk(    #75
        0x1F,
        (
            "#115F『影之国』……\x02\x03",

            "因为这种地方存在特定的『规则』，\x01",
            "所以一定是基于某种目的\x01",
            "而人为创造出来的。\x02\x03",

            "#110F如果能知道那个目的，\x01",
            "也许就能找到有效的攻略法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25DE")

    label("loc_257A")


    ChrTalk(    #76
        0x1F,
        (
            "#115F『影之国』的『规则』……\x02\x03",

            "如果能弄清楚这一点，\x01",
            "也许就能找到有效的攻略法……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DE")

    TalkEnd(0xFE)

    label("loc_25E1")

    Return()

    # Function_3_13FD end

    SaveToFile()

Try(main)
