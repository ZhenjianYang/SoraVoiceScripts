from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'U7001_5 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0303.x',
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
        "Function_3_B1",           # 03, 3
        "Function_4_274",          # 04, 4
        "Function_5_8E1",          # 05, 5
        "Function_6_1004",         # 06, 6
        "Function_7_1C5D",         # 07, 7
        "Function_8_2054",         # 08, 8
        "Function_9_376C",         # 09, 9
        "Function_10_3DF5",        # 0A, 10
        "Function_11_4757",        # 0B, 11
        "Function_12_5A99",        # 0C, 12
        "Function_13_5D6E",        # 0D, 13
        "Function_14_5F44",        # 0E, 14
        "Function_15_608F",        # 0F, 15
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

    Call(5, 3)
    Return()

    # Function_2_AC end

    def Function_3_B1(): pass

    label("Function_3_B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_152")
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")

    ChrTalk(    #0
        0x11,
        "#1065F……呼………呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1448F（睡得好香…………）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_147")

    label("loc_11E")


    ChrTalk(    #2
        0x11,
        "#1065F……呼………呼…………\x02",
    )

    CloseMessageWindow()

    label("loc_147")

    ClearChrFlags(0x11, 0x10)
    TalkEnd(0x11)
    Jump("loc_273")

    label("loc_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_210")
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC")

    ChrTalk(    #3
        0x11,
        "#40W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1000F嗯，看来平静多了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1447F…………嗯。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_205")

    label("loc_1DC")


    ChrTalk(    #6
        0x11,
        "#40W………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_205")

    ClearChrFlags(0x11, 0x10)
    TalkEnd(0x11)
    Jump("loc_273")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_273")
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x11)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05好像睡着了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #8
        0x10F,
        "#1445F………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    TalkEnd(0x11)

    label("loc_273")

    Return()

    # Function_3_B1 end

    def Function_4_274(): pass

    label("Function_4_274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F5")

    ChrTalk(    #9
        0x12,
        "#1446F……有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1067F不，不………\x02\x03",

            "#1077F没什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD")

    label("loc_2F5")


    ChrTalk(    #11
        0x12,
        (
            "#1805F（终于进了骑士团，\x01",
            "  经受了那样刻苦的修行………）\x02\x03",

            "（好不容易\x01",
            "  当上了随从骑士……）\x02\x03",

            "#1445F（可是………………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1067F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3AD")

    OP_A2(0x1)
    Jump("loc_410")

    label("loc_3B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E5")

    ChrTalk(    #13
        0x12,
        "#1446F……有什么事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_410")

    label("loc_3E5")


    ChrTalk(    #14
        0x12,
        "#1445F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_410")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_8E0")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_6FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_475")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #15
        0x12,
        "#1445F…………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6FC")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #16
        0x12,
        (
            "#1446F凯文以前就是那样子。\x02\x03",

            "不仅任性，而且总是\x01",
            "旁若无人自言自语……\x02\x03",

            "#1443F……虽然喜欢胡乱逞强，\x01",
            "实际上却很不中用。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A9")

    ChrTalk(    #17
        0x103,
        (
            "#1523F哦，这位就是\x01",
            "传说中的那位修女吗……\x02\x03",

            "#1522F不过……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x109, 400)

    ChrTalk(    #18
        0x103,
        (
            "#1527F好像在生\x01",
            "凯文先生的气呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E7")

    label("loc_5A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E7")

    ChrTalk(    #19
        0x10A,
        "#811F（生气的样子也很可爱呢……㈱）\x02",
    )

    CloseMessageWindow()

    label("loc_5E7")


    ChrTalk(    #20
        0x109,
        (
            "#1068F（哈哈…………\x01",
            "  感觉没办法靠近呀……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x1)
    TalkEnd(0xFE)
    Jump("loc_6FC")

    label("loc_62F")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #21
        0x12,
        (
            "#1446F凯文以前就是那样子。\x02\x03",

            "不仅任性，而且总是\x01",
            "旁若无人自言自语……\x02\x03",

            "#1443F……虽然喜欢胡乱逞强，\x01",
            "实际上却很不中用。\x02\x03",

            "#1805F……我不知道。\x01",
            "随你怎么样好了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_6FC")

    Jump("loc_8E0")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_740")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #22
        0x12,
        "#1445F…………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_8E0")

    label("loc_740")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(    #23
        0x12,
        (
            "#1446F…………凯文。\x01",
            "你继续瞒混也可以。\x02\x03",

            "只要你自己满足的话……\x02\x03",

            "#1445F不过………………\x02\x03",

            "#1446F从此以后就别跟我说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        "#1067F………………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2634)
    Jump("loc_8D8")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(    #25
        0x12,
        (
            "#1446F…………………………\x02\x03",

            "别跟我说话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1068F（……糟糕，\x01",
            "  好像还在气头上………）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8D8")

    label("loc_89C")


    ChrTalk(    #27
        0x12,
        (
            "#1446F…………………………\x02\x03",

            "别跟我说话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D8")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_8E0")

    Return()

    # Function_4_274 end

    def Function_5_8E1(): pass

    label("Function_5_8E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_A45")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BF")

    ChrTalk(    #28
        0x10,
        (
            "#1505F我也向赛雷斯托小姐\x01",
            "提出了一些疑问……\x02\x03",

            "#1503F她对『利贝尔方舟』相关的记忆\x01",
            "一点也没保留下来。\x02\x03",

            "#1503F似乎是因为她自己只是作为『影』的存在，\x01",
            "而没有被赋予不必要的情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_A3F")

    label("loc_9BF")


    ChrTalk(    #29
        0x10,
        (
            "#1505F她好像没有被赋予\x01",
            "不必要的情报。\x02\x03",

            "#1503F……从防止将情报泄露给『环』这点来考虑，\x01",
            "也许这样是十分妥当的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F")

    TalkEnd(0xFE)
    Jump("loc_1003")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_B9D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")

    ChrTalk(    #30
        0x10,
        (
            "#1503F理查德先生的解放，\x01",
            "似乎是至今为止没有过的形式……\x02\x03",

            "但这个应该也是\x01",
            "被『规则』所限定好的。\x02\x03",

            "#1505F组成这个世界的\x01",
            "所谓『规则』……\x02\x03",

            "我有一种再稍微深入点\x01",
            "就能够掌握它的感觉……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_B97")

    label("loc_B31")


    ChrTalk(    #31
        0x10,
        (
            "#1505F组成这个世界的\x01",
            "所谓『规则』……\x02\x03",

            "我有一种再稍微深入点\x01",
            "就能够掌握它的感觉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B97")

    TalkEnd(0xFE)
    Jump("loc_1003")

    label("loc_B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_1003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")
    TalkBegin(0xFE)

    ChrTalk(    #32
        0x101,
        (
            "#1000F……约修亚，\x01",
            "凯文先生的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#1500F嗯，现在已经睡着了。\x02\x03",

            "#1503F不过看起来\x01",
            "好像总是在做恶梦…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1004F哎………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        "#1802F…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D86")

    ChrTalk(    #36
        0x10,
        (
            "#1503F总之就是精神上的负担\x01",
            "对肉体造成了影响。\x02\x03",

            "#1505F现在只能\x01",
            "让他好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1003F是吗…………\x02\x03",

            "#1002F约修亚，\x01",
            "这里还得拜托你照顾一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        "#1446F……拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "#1501F嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F10")

    label("loc_D86")

    OP_4A(0x17, 255)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x17, 0x0, 0)

    ChrTalk(    #40
        0x17,
        (
            "#1165F啊，你们不用担心。\x02\x03",

            "从症状来看，\x01",
            "只是有点发烧罢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#1503F总之就是精神上的负担\x01",
            "对肉体造成了影响。\x02\x03",

            "#1505F现在只能\x01",
            "让他好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1003F是吗…………\x02\x03",

            "#1002F约修亚，科洛丝，\x01",
            "这里还得拜托你们照顾一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10F,
        "#1446F……拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x17,
        "#1167F嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#1501F交给我们吧。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F10")

    TalkEnd(0xFE)
    OP_A2(0x2659)
    Jump("loc_1003")

    label("loc_F19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA5")
    OP_A2(0x3)

    ChrTalk(    #46
        0x10,
        (
            "#1505F精神上的负担，\x01",
            "还是不要使用药物\x01",
            "勉强让他恢复比较好。\x02\x03",

            "#1500F就让他好好休息一下，\x01",
            "等他自然恢复吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_FA5")


    ChrTalk(    #47
        0x10,
        (
            "#1503F凯文先生现在的问题是\x01",
            "精神上的负担。\x02\x03",

            "我想只有让他好好休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1000")

    TalkEnd(0xFE)

    label("loc_1003")

    Return()

    # Function_5_8E1 end

    def Function_6_1004(): pass

    label("Function_6_1004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_1363")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_109B")
    Jump("loc_10DD")

    label("loc_109B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10B7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10DD")

    label("loc_10B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10D3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10DD")

    label("loc_10D3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10DD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E6")

    ChrTalk(    #48
        0x1C,
        (
            "#1527F……太过勉强可不行哦。\x02\x03",

            "#1535F『第六星层』的大致情况\x01",
            "我们已经掌握了，\x01",
            "接下来就想想怎么解决它吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F7")

    ChrTalk(    #49
        0x109,
        (
            "#1068F虽然说得没错……\x02\x03",

            "#1840F边酗酒边思考，\x01",
            "真符合大姐的作风啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C4")

    label("loc_11F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122F")

    ChrTalk(    #50
        0x102,
        "#1508F……虽然说得不错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1252")

    label("loc_122F")


    ChrTalk(    #51
        0x109,
        "#1840F虽然说得不错……\x02",
    )

    CloseMessageWindow()

    label("loc_1252")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128C")

    ChrTalk(    #52
        0x101,
        "#1019F雪拉姐，这酒瓶是什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_12C4")

    label("loc_128C")


    ChrTalk(    #53
        0x109,
        (
            "#1066F边酗酒边思考，\x01",
            "真符合大姐的作风啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C4")

    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x5)
    Jump("loc_1358")

    label("loc_12E6")


    ChrTalk(    #54
        0x1C,
        (
            "#1520F关于所谓的『试炼』\x01",
            "我们大致已经弄明白了。\x02\x03",

            "#1535F……接下来就仔细想想\x01",
            "怎么来把它解决吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1358")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1C5C")

    label("loc_1363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_1992")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A2")

    ChrTalk(    #55
        0x1C,
        (
            "#1526F那个始祖大人所说的话，\x01",
            "虽然没什么不明白的地方……\x02\x03",

            "#1522F可是为什么\x01",
            "这里会有书呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 47, 400)
    Sleep(300)

    ChrTalk(    #56
        0x1C,
        (
            "#1532F而且有这么多。\x01",
            "唉，真是搞不懂……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x1C,
        "#1523F啊，找到本奇怪的书！\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (8, "loc_14AD"),
        (14, "loc_14F1"),
        (0, "loc_1518"),
        (1, "loc_1539"),
        (4, "loc_155E"),
        (6, "loc_1594"),
        (5, "loc_15D3"),
        (7, "loc_15F3"),
        (3, "loc_1619"),
        (10, "loc_1655"),
        (9, "loc_1699"),
        (13, "loc_16D0"),
        (12, "loc_1716"),
        (11, "loc_173A"),
        (15, "loc_175E"),
        (SWITCH_DEFAULT, "loc_17A6"),
    )


    label("loc_14AD")


    ChrTalk(    #58
        0x109,
        (
            "#1064F哎…………！？\x02\x03",

            "#1063F是、是什么………？\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_14F1")


    ChrTalk(    #59
        0x10F,
        "#1444F……………………？\x02",
    )

    Jump("loc_17A6")

    label("loc_1518")


    ChrTalk(    #60
        0x101,
        "#1004F这…………？\x02",
    )

    Jump("loc_17A6")

    label("loc_1539")


    ChrTalk(    #61
        0x102,
        "#1504F嗯………………？\x02",
    )

    Jump("loc_17A6")

    label("loc_155E")


    ChrTalk(    #62
        0x105,
        (
            "#1164F哎…………\x02\x03",

            "奇怪的书……？\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_1594")


    ChrTalk(    #63
        0x107,
        (
            "#064F那个那个…………\x02\x03",

            "奇怪的书……是吗？\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_15D3")


    ChrTalk(    #64
        0x106,
        "#555F嗯…………？\x02",
    )

    Jump("loc_17A6")

    label("loc_15F3")


    ChrTalk(    #65
        0x108,
        "#073F奇怪的书…………？\x02",
    )

    Jump("loc_17A6")

    label("loc_1619")


    ChrTalk(    #66
        0x104,
        (
            "#1543F哦…………？\x02\x03",

            "#1542F那是什么啊。\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_1655")


    ChrTalk(    #67
        0x10B,
        (
            "#213F哎…………！？\x02\x03",

            "#216F怎、怎么了，突然……\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_1699")


    ChrTalk(    #68
        0x10A,
        (
            "#814F嗯…………？\x02\x03",

            "……奇怪的书？\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_16D0")


    ChrTalk(    #69
        0x10E,
        (
            "#172F奇怪的书…………？\x02\x03",

            "#178F……那是…………？\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_1716")


    ChrTalk(    #70
        0x10D,
        "#270F唔………………？\x02",
    )

    Jump("loc_17A6")

    label("loc_173A")


    ChrTalk(    #71
        0x10C,
        "#113F嗯………………？\x02",
    )

    Jump("loc_17A6")

    label("loc_175E")


    ChrTalk(    #72
        0x110,
        (
            "#264F……哎呀，是什么啊。\x02\x03",

            "#261F嘻嘻，让玲也看看！\x02",
        )
    )

    Jump("loc_17A6")

    label("loc_17A6")

    CloseMessageWindow()

    ChrTalk(    #73
        0x1C,
        (
            "#1526F#60W基尔巴特·斯坦因著…#1200W…#20W\x01",
            "───《肉体改造论》。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x29, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #74
        0x1C,
        (
            "#1525F唔……\x01",
            "这书架真的是让人难以理解啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x1, 0x1)
    OP_A2(0x265F)
    Jump("loc_198C")

    label("loc_18A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1932")

    ChrTalk(    #75
        0x1C,
        (
            "#1532F可是，\x01",
            "为什么会有这样的书呢。\x02\x03",

            "而且还有一些\x01",
            "很奇怪的书……\x02\x03",

            "#1525F我可不认为会有谁\x01",
            "把这个放进来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_198C")

    label("loc_1932")


    ChrTalk(    #76
        0x1C,
        (
            "#1532F为什么会有\x01",
            "这样的书呢。\x02\x03",

            "我不认为那个始祖大人\x01",
            "会把这书放进来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198C")

    TalkEnd(0xFE)
    Jump("loc_1C5C")

    label("loc_1992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_1A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FF")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #77
        0x1C,
        (
            "#1526F……嗯，没关系吧。\x02\x03",

            "看来他平时也有相当的锻炼。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x5)
    TalkEnd(0xFE)
    Jump("loc_1A6D")

    label("loc_19FF")

    TalkBegin(0xFE)

    ChrTalk(    #78
        0x1C,
        (
            "#1520F看来他平时也有相当的锻炼，\x01",
            "应该没关系的。\x02\x03",

            "#1535F我来照看他，\x01",
            "你们不用担心了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1A6D")

    Jump("loc_1C5C")

    label("loc_1A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_1C5C")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFD")

    ChrTalk(    #79
        0x1C,
        (
            "#1520F哦，这么说你和凯文先生\x01",
            "是从小就熟识了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        "#1802F嗯，是的。算是吧…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_1AFD")


    ChrTalk(    #81
        0x1C,
        (
            "#1525F你这个家伙真是的……\x02\x03",

            "#1522F对初次见面的人做什么呢。\x02\x03",

            "至少献上首圣歌吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#1504F喂……这是问题所在吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1B8F")

    OP_A2(0x5)
    Jump("loc_1C54")

    label("loc_1B95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C1A")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #83
        0x1C,
        (
            "#1526F虽然我认识的人之中\x01",
            "也有一位奇怪的修女……\x02\x03",

            "#1522F不过这孩子还真是有过之而无不及……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1C1A")


    ChrTalk(    #84
        0x1C,
        (
            "#1525F对方可是修女，\x01",
            "你也应该稍微有所顾忌吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C54")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1C5C")

    Return()

    # Function_6_1004 end

    def Function_7_1C5D(): pass

    label("Function_7_1C5D")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FBD")
    Sleep(500)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1F4)
    OP_21()
    OP_1D(0x0)

    ChrTalk(    #85
        0x19,
        "#1545F欢迎来到在下的独奏会！\x02\x03",
    )

    CloseMessageWindow()

    ChrTalk(    #86 op#A op#5
        0x19,
        "#1540F#30A看好！华丽的演出时间到了⊙\x05\x02",
    )

    CloseMessageWindow()
    Sleep(2500)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    EventBegin(0x1)

    ChrTalk(    #87 op#A op#5
        0x19,
        "#1545F#10A#0W……………………\x05\x02",
    )

    Sleep(1500)
    OP_4B(0x12, 255)
    CloseMessageWindow()
    Sleep(6270)

    ChrTalk(    #88 op#A op#5
        0x19,
        "#1545F#100A#0W滑过天边 星之轨迹……\x05\x02",
    )

    Sleep(6600)

    ChrTalk(    #89 op#A op#5
        0x19,
        "#1545F#100A#0W彷如路标 引导向你……\x05\x02",
    )

    Sleep(6200)

    ChrTalk(    #90 op#A op#5
        0x19,
        "#1545F#100A#0W急切的思念 满溢胸怀……\x05\x02",
    )

    Sleep(5600)

    ChrTalk(    #91 op#A op#5
        0x19,
        "#1545F#100A#0W月亮也嘲笑 这份痛苦……\x05\x02",
    )

    Sleep(7000)

    ChrTalk(    #92 op#A op#5
        0x19,
        "#1545F#100A#0W若无法实现 这份空想……\x05\x02",
    )

    Sleep(7000)

    ChrTalk(    #93 op#A op#5
        0x19,
        "#1545F#100A#0W至少请留下 一道浅伤……\x05\x02",
    )

    Sleep(9500)

    ChrTalk(    #94 op#A op#5
        0x19,
        "#1545F#100A#0W最初之吻 最后之吻……\x05\x02",
    )

    Sleep(8500)

    ChrTalk(    #95 op#A op#5
        0x19,
        "#1545F#100A#0W你的泪滴 化作琥珀……\x05\x02",
    )

    Sleep(8800)

    ChrTalk(    #96 op#A op#5
        0x19,
        "#1545F#100A#0W这份爱意 永远封存……\x05\x02",
    )

    Sleep(10800)
    CloseMessageWindow()
    Sleep(5500)
    EventEnd(0x1)
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F18")

    ChrTalk(    #97 op#A op#5
        0x10B,
        "#216F#20W#21A真的唱了呢……\x05\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_1F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F5A")

    ChrTalk(    #98 op#A op#5
        0x103,
        (
            "#1525F#20W#39A唉，\x01",
            "没想到真的唱了。\x05\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F93")

    label("loc_1F5A")


    ChrTalk(    #99 op#A op#5
        0x102,
        (
            "#1505F#20W#31A……奥利维尔，\x01",
            "你是认真的吗。\x05\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F93")


    ChrTalk(    #100 op#A op#5
        0x19,
        "#1547F#30A⊙～～\x05\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Sleep(1500)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_2051")

    label("loc_1FBD")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    EventBegin(0x1)

    ChrTalk(    #101 op#A op#5
        0x19,
        (
            "#1545F#70W#20A若无法实现 这份空想……\x01",
            "至少请留下 一道浅伤……\x05\x02\x03",

            "最初之吻 最后之吻……\x01",
            "你的泪滴 化作琥珀……\x01",
            "这份爱意 永远封存……\x05\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)

    label("loc_2051")

    OP_1D(0x49)
    Return()

    # Function_7_1C5D end

    def Function_8_2054(): pass

    label("Function_8_2054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_2396")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C5")

    ChrTalk(    #102
        0x17,
        (
            "#1167F由『辉之环』所\x01",
            "构建的『影之国』……\x02\x03",

            "#1169F看来这对『利贝尔方舟』\x01",
            "上的人们好像也是\x01",
            "出乎预料的事情呢。\x02\x03",

            "#1162F他们将都市全体的管理\x01",
            "交给『环』，原本是打算想把\x01",
            "利贝尔方舟变成一个『真正的乐园』。\x02\x03",

            "不过，『环』违背了\x01",
            "都市设计者的初衷，\x01",
            "制造了另一个被称作『影之国』的世界。\x02\x03",

            "#1169F这是人们\x01",
            "所期望的吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2390")

    label("loc_21C5")


    ChrTalk(    #103
        0x17,
        (
            "#1167F呼，\x01",
            "我想再更详细地调查一下……\x02\x03",

            "#1165F解读当时的人们\x01",
            "所做记录的片断\x01",
            "还需要花点时间……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2277")

    ChrTalk(    #104
        0x101,
        (
            "#1015F科洛丝，\x01",
            "不用太过追根究底吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2390")

    label("loc_2277")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BA")

    ChrTalk(    #105
        0x102,
        (
            "#1501F科洛丝，\x01",
            "你还是稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2390")

    label("loc_22BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22FC")

    ChrTalk(    #106
        0x10E,
        (
            "#176F……殿下，\x01",
            "请您适当休息一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2390")

    label("loc_22FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_235E")

    ChrTalk(    #107
        0x10B,
        (
            "#215F我、我说……\x01",
            "稍微休息一下吧？\x02\x03",

            "#210F你累倒的话就麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2390")

    label("loc_235E")


    ChrTalk(    #108
        0x109,
        (
            "#1066F哈哈，殿下……\x01",
            "请不要太勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2390")

    TalkEnd(0xFE)
    Jump("loc_376B")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_2553")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2497")

    ChrTalk(    #109
        0x17,
        (
            "#1160F刚才我从始祖大人\x01",
            "那里听说了……\x02\x03",

            "这个世界似乎有\x01",
            "吸取情报空间的性质。\x02\x03",

            "#1383F这些书所积累的情报\x01",
            "是受到我们的存在和意志影响\x01",
            "而显现出来的……\x02\x03",

            "#1382F大概就是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x109,
        "#1066F这、这样啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_254D")

    label("loc_2497")


    ChrTalk(    #111
        0x17,
        (
            "#1167F在各地放置的『门』\x01",
            "也许也是以同样的原理\x01",
            "进行运作的。\x02\x03",

            "由于我们的存在\x01",
            "而显现的情报空间……\x02\x03",

            "#1160F也许是『影之王』创造\x01",
            "这个世界的时候\x01",
            "所遗留下来的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254D")

    TalkEnd(0xFE)
    Jump("loc_376B")

    label("loc_2553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D02")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x0, 400)
    Sleep(300)

    ChrTalk(    #112
        0x17,
        "#1164F啊，各位……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2608")

    ChrTalk(    #113
        0x102,
        (
            "#1500F科洛丝，\x01",
            "在这里收集情报吗。\x02\x03",

            "#1501F有什么发现吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_2608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(    #114
        0x101,
        (
            "#1011F科洛丝，\x01",
            "你在这里调查吗。\x02\x03",

            "#1006F发现什么了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_2662")


    ChrTalk(    #115
        0x109,
        (
            "#1060F啊，殿下。\x01",
            "你又到这里来了吗。\x02\x03",

            "#1066F怎么样，\x01",
            "有什么发现吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B8")


    ChrTalk(    #116
        0x17,
        (
            "#1165F是、是啊……\x02\x03",

            "这里的书\x01",
            "看起来并不是\x01",
            "按顺序排列的……\x02\x03",

            "#1160F但是这个书架好像\x01",
            "也有着某种独特的『规则』，\x01",
            "看来需要掌握一些要领。\x02\x03",

            "比如说，想象你想读的书，\x01",
            "就能把书『叫到』附近的书架……\x02",
        )
    )

    Jump("loc_27A2")

    label("loc_27A2")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284B")

    ChrTalk(    #117
        0x101,
        (
            "#1004F竟、竟然能办到这样的事……\x02\x03",

            "#1015F啊……对了，因为这里是\x01",
            "能够用意念影响的世界……\x02\x03",

            "唔，有很强意念的话\x01",
            "就能创造出书来？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_284B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28EF")

    ChrTalk(    #118
        0x102,
        (
            "#1504F竟然能办到这样的事吗……\x02\x03",

            "#1503F……对了，这里是能够\x01",
            "用意念影响的世界……\x02\x03",

            "#1501F用自己强烈的意念\x01",
            "把书叫过来对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_28EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E8")

    ChrTalk(    #119
        0x10E,
        (
            "#173F能、能够这样做吗……\x02\x03",

            "#176F不过，赛雷斯托大人说过\x01",
            "这里是可以被意念影响的世界……\x02\x03",

            "的确，有这样的阅览方法的话，\x01",
            "这个过于高大的书架也能说的通了。\x02\x03",

            "#170F也就是说……能用强烈的意念\x01",
            "把书叫过来是吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_29E8")


    ChrTalk(    #120
        0x109,
        (
            "#1064F这、这是什么把戏……\x02\x03",

            "#1068F唉，不过在这个世界里\x01",
            "的确是可能做到的……\x02\x03",

            "#1066F用强烈的意念\x01",
            "把书叫过来……是吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A77")


    ChrTalk(    #121
        0x17,
        (
            "#1160F不，\x01",
            "只用单纯的意念好像不行。\x02\x03",

            "#1165F唔，该怎么说呢……\x01",
            "我也不是很清楚……\x02\x03",

            "大概是对着书架呼唤……\x01",
            "那样的感觉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B78")

    ChrTalk(    #122
        0x10E,
        (
            "#173F这、这样的方法……\x02\x03",

            "#179F……说起来，\x01",
            "殿下无论学什么\x01",
            "都能很快领会……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2B78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD8")

    ChrTalk(    #123
        0x102,
        (
            "#1504F真不愧是科洛丝……\x02\x03",

            "#1501F看来我大概是\x01",
            "没办法掌握了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2BD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C3B")

    ChrTalk(    #124
        0x101,
        (
            "#1007F唔…………\x01",
            "真不愧是科洛丝……\x02\x03",

            "竟然能精通\x01",
            "这样的技巧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2C3B")


    ChrTalk(    #125
        0x109,
        (
            "#1066F真、真厉害啊。\x02\x03",

            "#1068F估计我是怎么也\x01",
            "精通不了的啦，\x01",
            "书架的情报收集就拜托你了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")


    ChrTalk(    #126
        0x17,
        (
            "#1165F啊、啊哈哈…………\x02\x03",

            "我也只是偶尔\x01",
            "能够成功一次而已……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x265B)
    TalkEnd(0xFE)
    Jump("loc_2E13")

    label("loc_2D02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9E")

    ChrTalk(    #127
        0x17,
        (
            "#1160F想要阅览这里的书，\x01",
            "看来也需要一些要领……\x02\x03",

            "也许在什么地方\x01",
            "能找到有用的资料。\x02\x03",

            "#1382F我会尽可能的收集情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2E10")

    label("loc_2D9E")


    ChrTalk(    #128
        0x17,
        (
            "#1160F想要阅览这里的书，\x01",
            "看来也需要一些要领……\x02\x03",

            "也许会找到有用的资料，\x01",
            "我会尽可能的收集情报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E10")

    TalkEnd(0xFE)

    label("loc_2E13")

    Jump("loc_376B")

    label("loc_2E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_END)), "loc_2FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F82")
    TalkBegin(0xFE)

    ChrTalk(    #129
        0x17,
        (
            "#1162F各位……\x01",
            "情况我已经从始祖大人那里听说了。\x02\x03",

            "看来要继续前进\x01",
            "似乎需要我的力量对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x109,
        (
            "#1066F哦……\x01",
            "既然你知道就好办了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x17,
        (
            "#1167F嗯，我已经做好准备了。\x02\x03",

            "#1162F打算继续前进的话，\x01",
            "随时都可以加我做同伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x109,
        (
            "#1075F明白了。\x02\x03",

            "#1060F做好准备之后，\x01",
            "就回第六星层继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B04)
    TalkEnd(0xFE)
    Jump("loc_2FF4")

    label("loc_2F82")

    TalkBegin(0xFE)

    ChrTalk(    #133
        0x17,
        (
            "#1167F看来要继续前进\x01",
            "似乎需要我的力量。\x02\x03",

            "#1162F我已经做好准备了，\x01",
            "随时都可以加我做同伴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_2FF4")

    Jump("loc_3104")

    label("loc_2FF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3092")

    ChrTalk(    #134
        0x17,
        (
            "#1160F这里好像有\x01",
            "各种各样的书。\x02\x03",

            "#1160F不过它们好像\x01",
            "不是按顺序排列的。\x02\x03",

            "#1167F这里大概也存在着\x01",
            "某种『规则』……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3101")

    label("loc_3092")


    ChrTalk(    #135
        0x17,
        (
            "#1160F这里的书\x01",
            "好像不是\x01",
            "按顺序排列的。\x02\x03",

            "#1167F……大概也存在着\x01",
            "某种『规则』……\x02",
        )
    )

    Jump("loc_3100")

    label("loc_3100")

    CloseMessageWindow()

    label("loc_3101")

    TalkEnd(0xFE)

    label("loc_3104")

    Jump("loc_376B")

    label("loc_3107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_376B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A9")

    ChrTalk(    #136
        0x101,
        (
            "#1000F……科洛丝，\x01",
            "凯文先生的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x17,
        (
            "#1164F啊，嗯。\x02\x03",

            "#1160F现在应该\x01",
            "睡得很安稳了。\x02\x03",

            "#1169F刚才那会儿\x01",
            "他好像一直在\x01",
            "做恶梦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1004F哎………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x10F,
        "#1802F…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3357")
    OP_4A(0x10, 255)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(    #140
        0x10,
        (
            "#1503F总之就是精神上的负担\x01",
            "对肉体造成了影响。\x02\x03",

            "#1505F现在只能\x01",
            "让他好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1003F是吗…………\x02\x03",

            "#1002F约修亚，科洛丝，\x01",
            "这里还得拜托你们照顾一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x10F,
        "#1446F……拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x17,
        "#1167F嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x10,
        "#1501F交给我们吧。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 255)
    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34A3")

    label("loc_3357")


    ChrTalk(    #145
        0x17,
        (
            "#1169F『圣痕』的力量…………\x02\x03",

            "我想这和约修亚的症状一样，\x01",
            "是精神上的负担\x01",
            "对肉体造成了影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#1503F嗯，是啊…………\x02\x03",

            "现在只有让他\x01",
            "好好的休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#1003F是吗…………\x02\x03",

            "#1002F对不起，科洛丝。\x01",
            "这里还得拜托你照顾一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x10F,
        "#1446F……拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x17,
        "#1167F嗯。\x02",
    )

    CloseMessageWindow()

    label("loc_34A3")

    OP_A2(0x2659)
    Jump("loc_3768")

    label("loc_34A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3697")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3611")

    ChrTalk(    #150
        0x17,
        (
            "#1164F……说起来，\x01",
            "乔丝特的家务事\x01",
            "做得非常好呢。\x02\x03",

            "没想到她的手这么巧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CE")

    ChrTalk(    #151
        0x102,
        (
            "#1509F嗯，至少\x01",
            "比艾丝蒂尔要厉害哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1019F呜………………\x02\x03",

            "#1022F好、好像一直成长在\x01",
            "都是男人的家庭里，\x01",
            "所以已经习惯这个样子了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360E")

    label("loc_35CE")


    ChrTalk(    #153
        0x101,
        (
            "#1019F呜………………\x02\x03",

            "是、是、是这样吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360E")

    Jump("loc_3691")

    label("loc_3611")


    ChrTalk(    #154
        0x17,
        (
            "#1165F凯文先生的事\x01",
            "你们就不用太担心了。\x02\x03",

            "我对照顾病人\x01",
            "还是有些心得的。\x02\x03",

            "#1160F各位请继续\x01",
            "前进探索吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3691")

    OP_A2(0x7)
    Jump("loc_3768")

    label("loc_3697")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370E")

    ChrTalk(    #155
        0x17,
        (
            "#1160F虽然曾经从\x01",
            "艾丝蒂尔那里听说过……\x02\x03",

            "#1161F呵呵，乔丝特的家务事\x01",
            "做得非常好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3768")

    label("loc_370E")


    ChrTalk(    #156
        0x17,
        (
            "#1160F凯文先生的事\x01",
            "你们就不用太担心了。\x02\x03",

            "我对照顾病人\x01",
            "还是有些心得的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3768")

    TalkEnd(0xFE)

    label("loc_376B")

    Return()

    # Function_8_2054 end

    def Function_9_376C(): pass

    label("Function_9_376C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_3875")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3815")

    ChrTalk(    #157
        0x13,
        (
            "#065F凯、凯文哥哥小时候\x01",
            "是那样的孩子啊……\x02\x03",

            "#562F莉丝姐姐，真是辛苦你了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x109,
        "#1068F（糟了，不会相信了吧……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_386A")

    label("loc_3815")


    ChrTalk(    #159
        0x13,
        (
            "#065F真、真是有点\x01",
            "不敢相信……\x02\x03",

            "凯文哥哥小时候\x01",
            "是那样的孩子啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_386A")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_3DF4")

    label("loc_3875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_399B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392D")

    ChrTalk(    #160
        0x13,
        (
            "#063F那个那个，莉丝姐姐，\x01",
            "……请打起精神来！\x02\x03",

            "虽、虽然不知道\x01",
            "到底是怎么回事……\x02\x03",

            "#562F凯文哥哥\x01",
            "一定是把莉丝姐姐\x01",
            "看得非常重要……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3990")

    label("loc_392D")


    ChrTalk(    #161
        0x13,
        (
            "#063F唔，吵架的理由\x01",
            "我虽然不清楚……\x02\x03",

            "可是，还是去好好谈谈，\x01",
            "尽快和好比较好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3990")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_3DF4")

    label("loc_399B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 3)), scpexpr(EXPR_END)), "loc_3ACB")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A6D")

    ChrTalk(    #162
        0x13,
        (
            "#063F哎，莉丝姐姐\x01",
            "和凯文哥哥吵架了…………\x01",
            "……是这样吗……？\x02\x03",

            "这么没有精神……\x02\x03",

            "#562F怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x109,
        (
            "#1068F（哎呀……\x01",
            "  好强烈的罪恶感……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3AC0")

    label("loc_3A6D")


    ChrTalk(    #164
        0x13,
        (
            "#063F但是莉丝姐姐\x01",
            "看起来很没精神……\x02\x03",

            "#562F到底怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC0")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_3DF4")

    label("loc_3ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_3DF4")
    SetChrFlags(0x13, 0x10)
    TalkBegin(0x13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AEF")
    OP_4A(0x13, 255)
    Jump("loc_3AF7")

    label("loc_3AEF")

    OP_4A(0x13, 255)
    OP_4A(0x16, 255)

    label("loc_3AF7")


    ChrTalk(    #165
        0x13,
        (
            "#063F那个，莉丝姐姐\x01",
            "哪里不舒服吗……？\x02\x03",

            "要、要不\x01",
            "我帮你拿药过来……\x02",
        )
    )

    Jump("loc_3B59")

    label("loc_3B59")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C73")

    ChrTalk(    #166
        0x10B,
        (
            "#214F笨、笨蛋。\x01",
            "那是在生气……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x13, 0x10B, 400)

    ChrTalk(    #167
        0x13,
        "#064F哎………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10B,
        (
            "#416F……因为那个冒牌神父\x01",
            "好像说了什么\x01",
            "不该说的话。\x02\x03",

            "结果把她给激怒了，\x01",
            "所以她才闷闷不乐的。\x02\x03",

            "#212F还是不要去打扰她比较好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D7B")

    label("loc_3C73")


    ChrTalk(    #169
        0x16,
        (
            "#214F笨、笨蛋。\x01",
            "那是在生气……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x13, 0x16, 400)

    ChrTalk(    #170
        0x13,
        "#064F哎………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x16,
        (
            "#416F……因为那个冒牌神父\x01",
            "好像说了什么\x01",
            "不该说的话。\x02\x03",

            "结果把她给激怒了，\x01",
            "所以她才闷闷不乐的。\x02\x03",

            "#212F还是不要去打扰她比较好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7B")

    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #172
        0x13,
        (
            "#065F唔………\x02\x03",

            "但、但是…………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DDA")
    OP_4B(0x13, 255)
    Jump("loc_3DE2")

    label("loc_3DDA")

    OP_4B(0x13, 255)
    OP_4B(0x16, 255)

    label("loc_3DE2")

    OP_8C(0x13, 45, 0)
    OP_A2(0x2633)
    ClearChrFlags(0x13, 0x10)
    TalkEnd(0x13)

    label("loc_3DF4")

    Return()

    # Function_9_376C end

    def Function_10_3DF5(): pass

    label("Function_10_3DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_4524")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F74")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EA2")
    Jump("loc_3EE4")

    label("loc_3EA2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EBE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE4")

    label("loc_3EBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EDA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE4")

    label("loc_3EDA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #173
        0x1B,
        (
            "#816F嗯，莉丝看起来\x01",
            "好像有点精神了。\x02\x03",

            "#819F呵呵，\x01",
            "果然聊一聊还是有好处的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_40E9")

    label("loc_3F74")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4004")
    Jump("loc_4046")

    label("loc_4004")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4020")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4046")

    label("loc_4020")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_403C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4046")

    label("loc_403C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4046")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 1)

    ChrTalk(    #174
        0x1B,
        (
            "#818F然后，我就和艾丝蒂尔\x01",
            "一起急忙到现场去了……\x02\x03",

            "#810F啊，艾丝蒂尔\x01",
            "是我游击士的后辈……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 1)

    label("loc_40E9")

    OP_A2(0x9)
    Jump("loc_4521")

    label("loc_40EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_418D")
    Jump("loc_41CF")

    label("loc_418D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41A9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41CF")

    label("loc_41A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41C5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41CF")

    label("loc_41C5")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41CF")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #175
        0x1B,
        (
            "#810F……对了，阿加特前辈\x01",
            "已经出去了吗？\x02\x03",

            "#1311F我本来还想趁\x01",
            "前辈不在的时候\x01",
            "偷袭提妲……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42EE")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #176
        0x1B,
        (
            "#1317F啊，阿加特前辈……！？\x02\x03",

            "哇哇，糟了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x106,
        "#057F喂，你说什么胡话呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4373")

    label("loc_42EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4373")

    ChrTalk(    #178
        0x106,
        "#057F喂，你说什么胡话呢……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #179
        0x1B,
        (
            "#1317F哇哇…………\x01",
            "前辈怎么会在这里……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4373")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4521")

    label("loc_437E")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_440E")
    Jump("loc_4450")

    label("loc_440E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_442A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4450")

    label("loc_442A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4446")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4450")

    label("loc_4446")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4450")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 1)

    ChrTalk(    #180
        0x1B,
        (
            "#1316F正好那时\x01",
            "浮游都市崩塌了，\x01",
            "大家都乱成一团……\x02\x03",

            "#1317F所以就没办法\x01",
            "去买东西了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x109,
        "#1840F（……什么啊，完全跑题了吧？）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 1)

    label("loc_4521")

    Jump("loc_4756")

    label("loc_4524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_4756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x12, 255)

    ChrTalk(    #182
        0x1B,
        (
            "#818F可、可是\x01",
            "听你这么说……\x02\x03",

            "你不是非常担心\x01",
            "凯文先生的事，\x01",
            "结果晕倒了下来吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x12, 0xFE, 400)
    Sleep(200)

    ChrTalk(    #183
        0x12,
        "#1441F才、才没这样的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x1B,
        "#819F哦～，真的吗～？\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x102,
        (
            "#1505F（亚妮拉丝……\x01",
            "  这么快就混熟了吗。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)
    OP_8C(0x12, 71, 0)
    OP_A2(0x265C)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4756")

    label("loc_467F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F6")
    TalkBegin(0xFE)

    ChrTalk(    #186
        0x1B,
        (
            "#810F嘿嘿，\x01",
            "她就是莉丝吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #187
        0x1B,
        "#1311F真可爱…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_4753")

    label("loc_46F6")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #188
        0x1B,
        (
            "#818F莉丝啊，\x01",
            "你真不坦率……\x02\x03",

            "#816F好，\x01",
            "就让姐姐我……\x02",
        )
    )

    Jump("loc_474D")

    label("loc_474D")

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_4753")

    TalkEnd(0xFE)

    label("loc_4756")

    Return()

    # Function_10_3DF5 end

    def Function_11_4757(): pass

    label("Function_11_4757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_4817")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B7")

    ChrTalk(    #189
        0x16,
        (
            "#214F……喂，振作点！\x02\x03",

            "再装死的话就不管你了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_480C")

    label("loc_47B7")


    ChrTalk(    #190
        0x16,
        (
            "#212F喂，好好准备呀。\x02\x03",

            "#214F你要躺到什么时候。\x01",
            "……不管你了哦！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_480C")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5A98")

    label("loc_4817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_4A97")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4883")

    ChrTalk(    #191
        0x105,
        (
            "#1164F那个，乔丝特？\x02\x03",

            "#1163F……怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4913")

    label("loc_4883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48CE")

    ChrTalk(    #192
        0x101,
        (
            "#1015F我说，乔丝特……？\x02\x03",

            "……怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4913")

    label("loc_48CE")


    ChrTalk(    #193
        0x109,
        (
            "#1064F……乔丝特？\x02\x03",

            "#1060F怎么了，\x01",
            "好像没精神啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4913")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #194
        0x16,
        (
            "#417F没、没什么……！\x02\x03",

            "#417F只是在想，我们真的\x01",
            "能回到原来的世界去吗……\x02\x03",

            "#416F…………只是这个而已！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E0")

    label("loc_499C")


    ChrTalk(    #195
        0x16,
        (
            "#212F哥哥他们还等着我呢。\x02\x03",

            "#214F……要赶紧回去！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E0")

    OP_A2(0x8)
    Jump("loc_4A8C")

    label("loc_49E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A48")

    ChrTalk(    #196
        0x16,
        (
            "#413F认识的星座一个也没有啊……\x02\x03",

            "#417F……我们……\x01",
            "真的能回去吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8C")

    label("loc_4A48")


    ChrTalk(    #197
        0x16,
        (
            "#212F哥哥他们还等着我呢。\x02\x03",

            "#214F……要赶紧回去！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8C")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5A98")

    label("loc_4A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_4B96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B39")
    TalkBegin(0xFE)

    ChrTalk(    #198
        0x16,
        (
            "#215F…………唉……\x01",
            "来到了一个奇怪的地方……\x02\x03",

            "……………………………………\x02\x03",

            "#413F从今以后\x01",
            "我们该怎么办呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    TalkEnd(0xFE)
    Jump("loc_4B93")

    label("loc_4B39")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #199
        0x16,
        (
            "#215F……………………………………\x02\x03",

            "#413F唉………………\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_4B93")

    Jump("loc_5A98")

    label("loc_4B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_4D30")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD2")

    ChrTalk(    #200
        0x16,
        (
            "#215F……真是一个\x01",
            "搞不懂的世界啊……\x02\x03",

            "那个女人的话\x01",
            "原来是真的啊……\x02\x03",

            "#413F……算了。\x01",
            "我还是去给公主帮帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CCC")

    ChrTalk(    #201
        0x105,
        (
            "#1165F啊，对不起，乔丝特。\x02\x03",

            "让你做这些工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x16,
        (
            "#213F啊，没事，请别在放心上。\x02\x03",

            "#210F反正我也没什么事做。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CCC")

    OP_A2(0x8)
    Jump("loc_4D2A")

    label("loc_4CD2")


    ChrTalk(    #203
        0x16,
        (
            "#215F唉，尽是些\x01",
            "我搞不懂的事。\x02\x03",

            "#413F……什么时候\x01",
            "才能回去呢…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2A")

    TalkEnd(0xFE)
    Jump("loc_5A98")

    label("loc_4D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_4E01")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D9D")

    ChrTalk(    #204
        0x16,
        (
            "#416F嗯，大致好多了。\x02\x03",

            "#210F虽然还有点发烧，\x01",
            "不过已经没有大碍了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_4DFB")

    label("loc_4D9D")


    ChrTalk(    #205
        0x16,
        (
            "#210F差不多可以\x01",
            "带我去搜索了吧。\x02\x03",

            "#211F这个神父的情况\x01",
            "也已经平静了不少……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DFB")

    TalkEnd(0xFE)
    Jump("loc_5A98")

    label("loc_4E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_5099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF3")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #206
        0x16,
        (
            "#216F别、别用这副打扮\x01",
            "接近约修亚啊！\x02\x03",

            "#214F胸、胸部太大，\x01",
            "都露出来了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x1C, 255)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #207
        0x1C,
        "#1523F嗯………………？？\x02",
    )

    CloseMessageWindow()
    OP_4B(0x1C, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4FE7")

    label("loc_4EF3")

    TalkBegin(0xFE)

    ChrTalk(    #208
        0x16,
        (
            "#210F嗯，\x01",
            "现在他好像睡得很香。\x02\x03",

            "也不怎么\x01",
            "做恶梦了……\x02\x03",

            "#211F接下来就等\x01",
            "烧退下去了。\x02",
        )
    )

    Jump("loc_4F75")

    label("loc_4F75")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FE4")

    ChrTalk(    #209
        0x105,
        (
            "#1161F乔丝特，\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x16,
        (
            "#213F嗯，好的。\x02\x03",

            "#211F嘿嘿，交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE4")

    TalkEnd(0xFE)

    label("loc_4FE7")

    OP_A2(0x8)
    Jump("loc_5096")

    label("loc_4FED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5056")

    ChrTalk(    #211
        0x16,
        (
            "#216F可、可恶！！\x02\x03",

            "那个胸部也太犯规了吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5093")

    label("loc_5056")


    ChrTalk(    #212
        0x16,
        (
            "#210F这里就交给我吧。\x02\x03",

            "我已经习惯这样了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5093")

    TalkEnd(0xFE)

    label("loc_5096")

    Jump("loc_5A98")

    label("loc_5099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_53CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #213
        0x16,
        (
            "#210F嗯，这样就可以了。\x02\x03",

            "之后只要注意\x01",
            "别让身体着凉……\x02\x03",

            "#211F要不要准备些热粥\x01",
            "让他醒过来的时候喝呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1019F（唔…………）\x02\x03",

            "（乔丝特这家伙\x01",
            "  意外的能干呀……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51BC")

    ChrTalk(    #215
        0x105,
        (
            "#1161F（呵呵，\x01",
            "  她非常会做家务呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_523C")

    ChrTalk(    #216
        0x102,
        (
            "#1500F（说起来，\x01",
            "  空贼团的家务事\x01",
            "  也都是她一手包办呢……）\x02\x03",

            "#1509F（各种家务好像都很擅长。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_523C")


    ChrTalk(    #217
        0x101,
        "#1019F（哼…………！）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_53CB")

    label("loc_526D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52CD")

    ChrTalk(    #218
        0x16,
        (
            "#210F神父没什么问题哦。\x02\x03",

            "因为我一直在照看他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_52CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5325")

    ChrTalk(    #219
        0x16,
        (
            "#210F神父没什么问题哦。\x02\x03",

            "因为我和公主一直在照看他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_5325")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5385")

    ChrTalk(    #220
        0x16,
        (
            "#210F神父没什么问题哦。\x02\x03",

            "#211F因为我和约修亚\x01",
            "一直在照看他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_5385")


    ChrTalk(    #221
        0x16,
        (
            "#210F神父没什么问题哦。\x02\x03",

            "因为我们一直在照看他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C8")

    TalkEnd(0xFE)

    label("loc_53CB")

    Jump("loc_5A98")

    label("loc_53CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_55F8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548B")

    ChrTalk(    #222
        0x16,
        (
            "#212F唔、唔……\x02\x03",

            "那种打扮弹起鲁特琴来\x01",
            "好像还很帅的样子…………\x02\x03",

            "也许是真的皇子大人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x109,
        "#1068F哎呀，都说就是皇子了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_54EF")

    label("loc_548B")


    ChrTalk(    #224
        0x16,
        (
            "#413F呼，修女也终于\x01",
            "稍微冷静下来了。\x02\x03",

            "#215F一般很老实的人\x01",
            "生气起来还真是可怕……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54EF")

    OP_A2(0x8)
    Jump("loc_55F2")

    label("loc_54F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5561")

    ChrTalk(    #225
        0x16,
        (
            "#215F虽然是个奇怪的家伙，\x01",
            "但也算是很帅啦。\x02\x03",

            "#212F也许是真的皇子大人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55F2")

    label("loc_5561")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #226
        0x16,
        (
            "#212F……冒牌神父，\x01",
            "之后要道歉哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x109,
        (
            "#1840F那、那个暂且不提……\x02\x03",

            "#1066F那个『冒牌神父』的称号\x01",
            "能不能改改了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55F2")

    TalkEnd(0xFE)
    Jump("loc_5A98")

    label("loc_55F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_5705")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A5")

    ChrTalk(    #228
        0x16,
        (
            "#213F哇……\x01",
            "这么过分的事情。\x02\x03",

            "#212F那个神父竟然是\x01",
            "这样的坏孩子呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x109,
        (
            "#1068F（莉丝那家伙，\x01",
            "  在说什么夸张的话……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_56FA")

    label("loc_56A5")


    ChrTalk(    #230
        0x16,
        (
            "#210F总、总之别放在心上啦。\x02\x03",

            "#211F也许只是\x01",
            "你们互相误会了…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FA")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5A98")

    label("loc_5705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_587B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57FB")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    TurnDirection(0xFE, 0x109, 800)

    ChrTalk(    #231
        0x16,
        (
            "#214F啊，冒牌神父！！\x02\x03",

            "#212F修女很生气哦。\x02\x03",

            "虽然不知道发生了什么，\x01",
            "不过你还是去道个歉吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x109,
        (
            "#1068F（哈哈……\x01",
            "  好像连道歉也不接受呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5878")

    label("loc_57FB")

    TalkBegin(0xFE)

    ChrTalk(    #233
        0x16,
        (
            "#212F……修女好像\x01",
            "非常生气哦。\x02\x03",

            "冒牌神父，\x01",
            "你是不是说了很过分的话？\x02\x03",

            "#214F好好地去道个歉吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_5878")

    Jump("loc_5A98")

    label("loc_587B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_5A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5946")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_593F")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #234
        0x16,
        (
            "#416F（真是……\x01",
            "  虽然不知道发生了什么，\x01",
            "  不过反正是你的错吧？）\x02\x03",

            "#212F（好好地去反省一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x109,
        "#1841F（……真丢脸。）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_5943")

    label("loc_593F")

    Call(5, 9)

    label("loc_5943")

    Jump("loc_5A98")

    label("loc_5946")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F7")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #236
        0x16,
        (
            "#214F（喂，这里就交给我们，\x01",
            "  你快点回去搜索吧。）\x02\x03",

            "（有你在的话\x01",
            "  只会更加别扭吧？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x109,
        (
            "#1067F（是、是呀……\x01",
            "  拜托你了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_5A95")

    label("loc_59F7")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #238
        0x16,
        (
            "#416F（真是……\x01",
            "  虽然不知道发生了什么，\x01",
            "  不过反正是你的错吧？）\x02\x03",

            "#212F（好好地去反省一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x109,
        "#1841F（……真丢脸。）\x02",
    )

    CloseMessageWindow()

    label("loc_5A95")

    TalkEnd(0xFE)

    label("loc_5A98")

    Return()

    # Function_11_4757 end

    def Function_12_5A99(): pass

    label("Function_12_5A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_5C74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B39")
    TalkBegin(0xFE)

    ChrTalk(    #240
        0x14,
        (
            "#178F好像古代的人们对『影之国』\x01",
            "了解的也不是很详细。\x02\x03",

            "#176F这里是『辉之环』\x01",
            "擅自创造出来的世界。\x01",
            "也难怪会这样……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    TalkEnd(0xFE)
    Jump("loc_5C71")

    label("loc_5B39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BA4")
    TalkBegin(0xFE)

    ChrTalk(    #241
        0x14,
        (
            "#170F殿下，\x01",
            "这里就交给我来吧……\x02\x03",

            "请您也\x01",
            "适当休息一下。\x02",
        )
    )

    Jump("loc_5B9D")

    label("loc_5B9D")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_5C71")

    label("loc_5BA4")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x17, 255)
    TurnDirection(0xFE, 0x17, 400)
    Sleep(300)

    ChrTalk(    #242
        0x14,
        (
            "#178F……可是殿下，\x01",
            "您差不多该休息一下了吧。\x02\x03",

            "#176F这里我会\x01",
            "尽量来处理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x17,
        (
            "#1165F哈哈………\x01",
            "是、是啊。\x02\x03",

            "#1382F嗯……让我再稍微……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_5C71")

    Jump("loc_5D6D")

    label("loc_5C74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D11")
    OP_A2(0xA)

    ChrTalk(    #244
        0x14,
        (
            "#176F真不明白为什么\x01",
            "这里会有书架……\x02\x03",

            "#178F貌似古今东西\x01",
            "所有的书这里都有。\x02\x03",

            "也许会有什么关于\x01",
            "这个异空间的线索呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6A")

    label("loc_5D11")


    ChrTalk(    #245
        0x14,
        (
            "#172F……不过怎么会\x01",
            "堆得这么高！？\x02\x03",

            "很明显用手\x01",
            "根本就够不到啊…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D6A")

    TalkEnd(0xFE)

    label("loc_5D6D")

    Return()

    # Function_12_5A99 end

    def Function_13_5D6E(): pass

    label("Function_13_5D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E43")
    TalkBegin(0xFE)

    ChrTalk(    #246
        0x1F,
        (
            "#115F我…………\x01",
            "我觉得自己会到这里\x01",
            "并不是偶然。\x02\x03",

            "#110F不管是谁的意思，\x01",
            "我的确在这里得到了难以得到的东西。\x02\x03",

            "#111F……那么，从现在开始\x01",
            "我会尽力去做好\x01",
            "当前所能办到的事。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_A2(0xE)
    Jump("loc_5F43")

    label("loc_5E43")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #247
        0x1F,
        (
            "#112F嗯，这个书架\x01",
            "真是太棒了……\x02\x03",

            "#115F竟然能找到\x01",
            "这么多资料……\x02\x03",

            "……在回去之前\x01",
            "要尽可能的记住。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F01")

    ChrTalk(    #248
        0x101,
        "#1016F（好认真啊，上校……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3B")

    label("loc_5F01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F3B")

    ChrTalk(    #249
        0x110,
        "#269F（嘻嘻，真是个有趣的人。）\x02",
    )

    CloseMessageWindow()

    label("loc_5F3B")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_5F43")

    Return()

    # Function_13_5D6E end

    def Function_14_5F44(): pass

    label("Function_14_5F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6010")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #250
        0x15,
        (
            "#270F《弗拉蒙贵族年鉴》……\x01",
            "《无名男子　第４卷》……\x02\x03",

            "《奥雷德秘境探访》……\x01",
            "《帝国时报社旧刊合集》……\x02\x03",

            "#272F嗯………………\x01",
            "好像不能作为参考啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0xF)
    TalkEnd(0xFE)
    Jump("loc_608E")

    label("loc_6010")

    TalkBegin(0xFE)

    ChrTalk(    #251
        0x15,
        (
            "#276F要是能找到关于\x01",
            "『敌人』的情报的话，\x01",
            "就能想出相应对策了……\x02\x03",

            "……好像没有什么\x01",
            "可以参考的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_608E")

    Return()

    # Function_14_5F44 end

    def Function_15_608F(): pass

    label("Function_15_608F")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6144")
    OP_A2(0xC)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(200)

    ChrTalk(    #252
        0x21,
        (
            "#1228F呼呼…………\x02\x03",

            "#1224F呜呜……\x01",
            "别和我说话……\x02\x03",

            "我已经一点也不想动了。\x02\x03",

            "#1227F别……别管我………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6246")

    label("loc_6144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E7")
    OP_A2(0xD)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(200)

    ChrTalk(    #253
        0x21,
        (
            "#1225F我、我都说\x01",
            "别和我说话啦！\x02\x03",

            "#1224F可、可恶……\x01",
            "你们是来嘲笑我的吗？\x02\x01",

            "#1227F是来嘲笑我的吧！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6246")

    label("loc_61E7")

    OP_A3(0xC)
    OP_A3(0xD)

    ChrTalk(    #254
        0x21,
        (
            "#1228F都、都说了别管我……\x02\x03",

            "想笑的话\x01",
            "随便去笑就行了吧！？\x02",
        )
    )

    Jump("loc_6245")

    label("loc_6245")

    CloseMessageWindow()

    label("loc_6246")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Return()

    # Function_15_608F end

    SaveToFile()

Try(main)
