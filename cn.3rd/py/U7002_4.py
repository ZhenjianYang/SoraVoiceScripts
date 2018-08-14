from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7002_4 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7002.x',
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
        "Function_3_B9C",          # 03, 3
        "Function_4_14F3",         # 04, 4
        "Function_5_1C9B",         # 05, 5
        "Function_6_2385",         # 06, 6
        "Function_7_2BE6",         # 07, 7
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2F7")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 6)), scpexpr(EXPR_END)), "loc_181")

    ChrTalk(    #0
        0x15,
        (
            "#216F怎、怎么回事啊，\x01",
            "那个老伯…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1300)

    ChrTalk(    #1
        0x15,
        "#214F#3S…………太奇怪了！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1061F奇怪……\x02\x03",

            "#1066F能再想想其它的\x01",
            "形容方法吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_211")

    label("loc_181")


    ChrTalk(    #3
        0x15,
        (
            "#215F因为是再现出来的人格，\x01",
            "所以管家老伯就变成了敌人……？\x02\x03",

            "……………………………………\x02\x03",

            "#413F我已经完全不明白了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211")

    OP_A2(0x5)
    Jump("loc_2F1")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 6)), scpexpr(EXPR_END)), "loc_29A")

    ChrTalk(    #4
        0x15,
        (
            "#216F呼，平时看起来\x01",
            "一本正经的老伯……#3880W \x01",
            "#20W竟然会这么强……\x02\x03",

            "#214F#3S………果然是很奇怪啊！#2S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1")

    label("loc_29A")


    ChrTalk(    #5
        0x15,
        (
            "#413F我已经完全不明白了……\x02\x03",

            "#215F我们大家……\x01",
            "真的能平安回去吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1")

    TalkEnd(0xFE)
    Jump("loc_B9B")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_5E1")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38E")
    Jump("loc_3D0")

    label("loc_38E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D0")

    label("loc_3AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D0")

    label("loc_3C6")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D0")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B8")

    ChrTalk(    #6
        0x15,
        (
            "#215F真、真的可以吗……\x01",
            "竟然把利贝尔\x01",
            "下任的女王殿下封印起来……\x02\x03",

            "#416F这个『影之王』，\x01",
            "被抓到之后一定会被判极刑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#1165F哈、哈哈…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_566")

    label("loc_4B8")


    ChrTalk(    #8
        0x15,
        (
            "#215F嗯，这位公主应该是\x01",
            "利贝尔下任的女王殿下吧。\x02\x03",

            "真、真的可以吗……\x01",
            "竟然把这样的人封印起来……\x02\x03",

            "#416F这个『影之王』，\x01",
            "被抓到之后一定会被判极刑的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566")

    OP_A2(0x5)
    Jump("loc_5D6")

    label("loc_56C")


    ChrTalk(    #9
        0x15,
        (
            "#416F虽然这话由我来说\x01",
            "有些奇怪……\x02\x03",

            "#212F这个『影之王』，\x01",
            "被抓到之后一定会被判极刑的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D6")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_B9B")

    label("loc_5E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_710")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7")

    ChrTalk(    #10
        0x15,
        (
            "#210F嗯嗯，\x01",
            "反正已经被卷入这么奇怪的事，\x01",
            "那就只好这么做了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_653")
    TurnDirection(0x15, 0x102, 400)
    Jump("loc_65A")

    label("loc_653")

    TurnDirection(0x15, 0x16, 400)

    label("loc_65A")

    Sleep(300)

    ChrTalk(    #11
        0x15,
        (
            "#211F约修亚，等会儿一起去\x01",
            "那个奇怪的王都逛逛吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1840F真会见机行事啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_70A")

    label("loc_6C7")


    ChrTalk(    #13
        0x15,
        (
            "#211F嗯嗯，反正已经被卷进来了，\x01",
            "那就要和约修亚在一起！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A")

    TalkEnd(0xFE)
    Jump("loc_B9B")

    label("loc_710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")
    TalkBegin(0xFE)

    ChrTalk(    #14
        0x15,
        (
            "#214F这、这里是怎么回事！\x02\x03",

            "#215F怎么会飘浮在空间里……\x01",
            "而且还有这么多书……\x02\x03",

            "#214F要是掉下去的话\x01",
            "该怎么办啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1065F（唔，\x01",
            "  果然很不冷静呢。）\x02\x03",

            "#1071F……我说，那个…………\x02\x03",

            "#1062F对了，\x01",
            "你之前说过正在\x01",
            "克洛斯贝尔附近吧……\x02\x03",

            "#1066F现在开的运输公司，\x01",
            "也提供国际快递服务吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x109, 400)

    ChrTalk(    #16
        0x15,
        (
            "#215F……哎，是啊………………\x02\x03",

            "#212F当、当然了。\x01",
            "我们原本就是帝国出身。\x02\x03",

            "卡普亚特急便，\x01",
            "可是活跃于大陆各地的。\x02\x03",

            "#210F克洛斯贝尔已经算很近了。\x02\x03",

            "最近还去过\x01",
            "列曼自治州附近呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AE")

    ChrTalk(    #17
        0x107,
        (
            "#064F哎，到那么远……？\x02\x03",

            "#067F真厉害……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EE")

    label("loc_9AE")


    ChrTalk(    #18
        0x109,
        (
            "#1064F哎，是、是这样啊……\x02\x03",

            "那不是很厉害嘛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE")


    ChrTalk(    #19
        0x15,
        (
            "#210F嘿嘿，\x01",
            "可别小看山猫号哦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7B")

    ChrTalk(    #20
        0x10D,
        (
            "#272F……记得努力赚钱，\x01",
            "早点还清借款。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x10D, 500)
    Sleep(1000)
    Jump("loc_ACC")

    label("loc_A7B")


    ChrTalk(    #21
        0x14,
        (
            "#272F……记得努力赚钱，\x01",
            "早点还清借款。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1000)

    label("loc_ACC")


    ChrTalk(    #22
        0x15,
        (
            "#214F不、不用你说\x01",
            "我也是这么打算的！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x265A)
    TalkEnd(0xFE)
    Jump("loc_B9B")

    label("loc_B08")

    TalkBegin(0xFE)

    ChrTalk(    #23
        0x15,
        (
            "#215F……话说回来，\x01",
            "这里真是个奇怪的地方……\x02\x03",

            "怎么会飘浮在空间里……\x01",
            "而且还有这么多书……\x02\x03",

            "#413F哥哥们不要紧吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_B9B")

    Return()

    # Function_2_AC end

    def Function_3_B9C(): pass

    label("Function_3_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D38")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3B")
    Jump("loc_C7D")

    label("loc_C3B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C57")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7D")

    label("loc_C57")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C73")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7D")

    label("loc_C73")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #24
        0x13,
        (
            "#170F…………不管怎么说，\x01",
            "殿下平安无事比什么都好。\x02\x03",

            "#175F不过，也许还有\x01",
            "其他的人被抓了起来。\x02\x03",

            "#176F我们必须赶快行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_EB6")

    label("loc_D38")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC8")
    Jump("loc_E0A")

    label("loc_DC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DE4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E0A")

    label("loc_DE4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E00")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E0A")

    label("loc_E00")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E0A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #25
        0x13,
        (
            "#176F说起来，\x01",
            "那个王都原来是伪造的啊……\x02\x03",

            "#178F不过，这下就明白了。\x02\x03",

            "那个叫『影之王』的\x01",
            "就是所有事情的元凶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB6")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_14F2")

    label("loc_EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_113E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F58")
    Jump("loc_F9A")

    label("loc_F58")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F74")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F9A")

    label("loc_F74")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F90")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F9A")

    label("loc_F90")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B3")

    ChrTalk(    #26
        0x13,
        (
            "#176F……话说回来，\x01",
            "这里净是些弄不懂的事。\x02\x03",

            "#175F这个异空间也好，\x01",
            "真正的恶魔也好，\x01",
            "还有那副景象的王都…………\x02\x03",

            "到处都有『魔物』在徘徊，\x01",
            "还出现了实体化的亡灵……\x02\x03",

            "#176F……现在也只好\x01",
            "继续搜索了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1133")

    label("loc_10B3")


    ChrTalk(    #27
        0x13,
        (
            "#175F虽然想快点把\x01",
            "城门前的封印解开，\x01",
            "好确认陛下和殿下是否平安……\x02\x03",

            "……不过现在还是\x01",
            "踏踏实实地继续搜索吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1133")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_14F2")

    label("loc_113E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 7)), scpexpr(EXPR_END)), "loc_11EC")
    TalkBegin(0xFE)

    ChrTalk(    #28
        0x13,
        (
            "#178F可是……\x01",
            "这里到底是什么地方……\x02\x03",

            "听说四轮之塔里存在着\x01",
            "被称为『里塔』的异空间……\x02\x03",

            "#176F不，仔细想想\x01",
            "这也不是能够解释的事情……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_14F2")

    label("loc_11EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_14F2")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #29
        0x13,
        (
            "#176F王都变成那个样子……\x02\x03",

            "#175F陛下和殿下都平安无事吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1060F那个，尤莉亚小姐。\x01",
            "你的心情我十分明白……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0x13, 0x109, 400)

    ChrTalk(    #31
        0x13,
        (
            "#170F哎、哎呀，各位……\x02\x03",

            "#176F……对不起，\x01",
            "我有点混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1065F没什么，\x01",
            "这也是没有办法的事。\x02\x03",

            "#1068F就连我\x01",
            "也是一头雾水呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10D,
        (
            "#276F……上尉，这对我来说\x01",
            "也是完全无法理解的事态……\x02\x03",

            "#270F只能够说，现在出现了\x01",
            "不明身份的『敌人』。\x02\x03",

            "正因为我们还没掌握状况，\x01",
            "所以更应该谨慎行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        "#175F是、是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        (
            "#1440F以后也许又会\x01",
            "遇到什么强敌。\x02\x03",

            "#1446F你在这里好好做准备\x01",
            "也是在给大家帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x13,
        (
            "#176F…………明白了。\x02\x03",

            "#170F看来这个据点是安全的。\x02\x03",

            "所以我会尽可能地\x01",
            "做好探索的准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2637)
    TalkEnd(0xFE)

    label("loc_14F2")

    Return()

    # Function_3_B9C end

    def Function_4_14F3(): pass

    label("Function_4_14F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_1C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_END)), "loc_183E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A8")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    TurnDirection(0xFE, 0xEE, 0)
    Sleep(300)

    ChrTalk(    #37
        0x1F,
        (
            "#113F哎呀……\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        "#1078F嗯，是这样的……\x02",
    )

    CloseMessageWindow()
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0xEE, -67750, 4120, -15480, 296)
    SetChrPos(0xEF, -66720, 4120, -14920, 281)
    SetChrPos(0xF0, -67510, 4120, -17140, 301)
    SetChrPos(0xF1, -66430, 4120, -16400, 321)
    OP_6D(-67750, 4120, -15480, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    TurnDirection(0xFE, 0xEE, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #39
        (
            "\x07\x05凯文把红耀石石碑上\x01",
            "记述的语句向理查德作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_1681")

    label("loc_1681")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #40
        0x1F,
        (
            "#113F『剑圣的继承者』……我吗？\x02\x03",

            "#116F可、可是……\x02\x03",

            "#115F……啊，也罢。\x01",
            "先不说是否有继承的资格，\x01",
            "看来这里只有我符合这个条件。\x02\x03",

            "#110F我没有问题。\x01",
            "随时都可以加入你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x109,
        "#1077F嗯，那就拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B17)
    Sleep(300)
    EventEnd(0x0)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_67(0, 3620, -10000, 1000)
    Jump("loc_183B")

    label("loc_17A8")

    TalkBegin(0xFE)

    ChrTalk(    #42
        0x1F,
        (
            "#116F虽然我不认为\x01",
            "自己有那样的资格……\x02\x03",

            "#115F不过现在可不是\x01",
            "感情用事的时候。\x02\x03",

            "#110F……你们随时都可以\x01",
            "加我做同伴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_183B")

    Jump("loc_1C9A")

    label("loc_183E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDC")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-68630, 4120, -16430, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(180000, 0)
    OP_6E(403, 0)
    SetChrPos(0xEE, -67570, 4120, -15720, 315)
    SetChrPos(0xEF, -66080, 4120, -15490, 315)
    SetChrPos(0xF0, -67810, 4120, -17260, 315)
    SetChrPos(0xF1, -66170, 4120, -17290, 315)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1932")

    ChrTalk(    #43
        0x10A,
        (
            "#814F#5P唔，上校………\x01",
            "在做居合斩的练习吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BB")

    label("loc_1932")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1982")

    ChrTalk(    #44
        0x101,
        (
            "#1011F#5P哎，上校………？\x01",
            "……你在干什么…………？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BB")

    label("loc_1982")


    ChrTalk(    #45
        0x109,
        (
            "#1064F#5P理查德上校……\x01",
            "……好厉害的剑气……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BB")


    ChrTalk(    #46
        0x1F,
        (
            "#119F#12P…………不，\x01",
            "这世上另有很多强者……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 15)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #47
        0x1F,
        (
            "#115F#12P尚未达到极致，\x01",
            "也无法狠心舍弃……\x02\x03",

            "我的剑，\x01",
            "只不过是半调子罢了。\x02\x03",

            "#110F……只是像这样\x01",
            "一边修养着心神，\x01",
            "一边等待心境拨云见日的一天。\x02",
        )
    )

    Jump("loc_1AC0")

    label("loc_1AC0")

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        "#1063F#5P是、是这样吗……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 40)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-66850, 4120, -16340, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -66850, 4120, -16340, 315)
    SetChrPos(0x1, -66850, 4120, -16340, 315)
    SetChrPos(0x2, -66850, 4120, -16340, 315)
    SetChrPos(0x3, -66850, 4120, -16340, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    OP_A2(0xB)
    Jump("loc_1C89")

    label("loc_1BDC")


    ChrTalk(    #49
        0x1F,
        (
            "#115F我的剑，\x01",
            "只不过是半调子罢了……\x02\x03",

            "所以一边像这样修养心神，\x01",
            "一边等待自己心境\x01",
            "拨云见日的一天。\x02\x03",

            "#110F……虽然不明白为什么，\x01",
            "但这样就能冷静下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C89")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C9A")

    Return()

    # Function_4_14F3 end

    def Function_5_1C9B(): pass

    label("Function_5_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_1EA6")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D32")
    Jump("loc_1D74")

    label("loc_1D32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D4E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D74")

    label("loc_1D4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D6A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D74")

    label("loc_1D6A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D74")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E32")

    ChrTalk(    #50
        0x14,
        (
            "#272F………『影之王』……\x02\x03",

            "从他的手法来看\x01",
            "绝不是个简单的角色……\x02\x03",

            "#276F要找出敌人的身份，\x01",
            "现在的线索真是太少了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1E9B")

    label("loc_1E32")


    ChrTalk(    #51
        0x14,
        (
            "#276F我很在意出现在\x01",
            "格兰赛尔城的女性幽灵。\x02\x03",

            "似乎已经在凯文先生面前\x01",
            "出现过好几次了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2384")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_20B7")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F3D")
    Jump("loc_1F7F")

    label("loc_1F3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F59")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F7F")

    label("loc_1F59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F75")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F7F")

    label("loc_1F75")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F7F")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205B")

    ChrTalk(    #52
        0x14,
        (
            "#272F这个异空间……\x01",
            "被叫做『影之国』吗。\x02\x03",

            "虽然不清楚到底搞什么鬼，\x01",
            "反正都是那个『王』\x01",
            "搞的花招吧……\x02\x03",

            "#270F把那家伙斩了，\x01",
            "就能从这里出去了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_20AC")

    label("loc_205B")


    ChrTalk(    #53
        0x14,
        (
            "#270F敌人就是用来打败的。\x02\x03",

            "#276F……不过，\x01",
            "也许没这么简单……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AC")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2384")

    label("loc_20B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F3")

    ChrTalk(    #54
        0x109,
        (
            "#1078F……哎呀，\x01",
            "看到穆拉先生你的出现，\x01",
            "真是让我松了一口气呀。\x02\x03",

            "#1077F总觉得心里更有底了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10E,
        (
            "#170F嗯，说实话我也在担心\x01",
            "只靠我们几个不知该怎么办才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14,
        (
            "#270F……不，我自己也对\x01",
            "现在的状况感到不安。\x02\x03",

            "不过既然已经\x01",
            "有『敌人』出现，\x01",
            "那就不能置之不管。\x02\x03",

            "#276F而且那个家伙\x01",
            "很有可能也被卷了进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10E,
        (
            "#172F……啊………………\x02\x03",

            "#178F的、的确…………\x02\x03",

            "这种情况，\x01",
            "如果是敌人设下的陷阱的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x14,
        (
            "#272F……继续搜索的话\x01",
            "事情就会明朗吧。\x02\x03",

            "如果要用到我的力量，\x01",
            "请随时叫上我。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2638)
    Jump("loc_2381")

    label("loc_22F3")


    ChrTalk(    #59
        0x14,
        (
            "#276F虽然不清楚所谓的『敌人』\x01",
            "到底是什么来头……\x02\x03",

            "#272F但是不能这样\x01",
            "放任不管。\x02\x03",

            "如果要用到我的力量，\x01",
            "请随时叫上我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2381")

    TalkEnd(0xFE)

    label("loc_2384")

    Return()

    # Function_5_1C9B end

    def Function_6_2385(): pass

    label("Function_6_2385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_284C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F2")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0)
    Sleep(300)

    ChrTalk(    #60
        0x20,
        (
            "#263F晚上好，是个不错的夜晚呢。\x02\x03",

            "#260F虽说看不到月亮很遗憾，\x01",
            "但星星也很漂亮呀。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AE")

    ChrTalk(    #61
        0x102,
        "#1503F玲………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x20,
        (
            "#1300F……约修亚，\x01",
            "你不用说什么。\x02\x03",

            "玲从一开始\x01",
            "就明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        "#1505F……是吗………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_24AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2597")

    ChrTalk(    #64
        0x101,
        "#1003F那个，玲………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x20,
        (
            "#1300F……莱维…………\x02\x03",

            "他教会了我很多东西，\x01",
            "但只有『真相』没有教给我。\x02\x03",

            "#268F他说『玲的真相\x01",
            "要玲自己找出来』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1025F……是这样啊…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_2597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CA")

    ChrTalk(    #67
        0x107,
        "#063F那个，玲…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_25EF")

    label("loc_25CA")


    ChrTalk(    #68
        0x109,
        "#1840F我说，玲…………？\x02",
    )

    CloseMessageWindow()

    label("loc_25EF")


    ChrTalk(    #69
        0x20,
        "#261F嘻嘻…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x0, 400)
    Sleep(300)

    ChrTalk(    #70
        0x20,
        (
            "#260F玲在想……\x02\x03",

            "难得有这么多爱热闹的人\x01",
            "聚集在一起。\x02\x03",

            "#265F不如一起去那个黑色的\x01",
            "古罗力亚斯玩捉迷藏吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D1")

    ChrTalk(    #71
        0x101,
        (
            "#1016F哈哈，\x01",
            "这个有点……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E4")

    label("loc_26D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2777")

    ChrTalk(    #72
        0x10F,
        (
            "#1446F……玲应该是我们当中\x01",
            "对那艘飞艇最熟悉的……\x02\x03",

            "#1440F……不太公平呢。\x01",
            "加点规则吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        "#1061F哈哈，你还真感兴趣……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E4")

    label("loc_2777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C1")
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #74
        0x107,
        "#065F哇、哇啊…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E4")

    label("loc_27C1")


    ChrTalk(    #75
        0x109,
        "#1066F还、还是算了……\x02",
    )

    CloseMessageWindow()

    label("loc_27E4")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2655)
    TalkEnd(0xFE)
    Jump("loc_2849")

    label("loc_27F2")

    TalkBegin(0xFE)

    ChrTalk(    #76
        0x20,
        (
            "#260F嘻嘻，好美丽的星空啊。\x02\x03",

            "#261F要是有月亮的话\x01",
            "就更漂亮了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_2849")

    Jump("loc_2BE5")

    label("loc_284C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_2BE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2905")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_288F")
    TurnDirection(0xFE, 0x101, 0)
    Jump("loc_2896")

    label("loc_288F")

    TurnDirection(0xFE, 0x102, 0)

    label("loc_2896")


    ChrTalk(    #77
        0x20,
        (
            "#260F艾丝蒂尔和约修亚\x01",
            "每天都在一起练习吧。\x02\x03",

            "#263F嘻嘻，艾丝蒂尔\x01",
            "有没有稍微变强了一些呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298C")

    label("loc_2905")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #78
        0x20,
        (
            "#267F呼……\x02\x03",

            "……艾丝蒂尔和约修亚\x01",
            "每天都在一起练习吧。\x02\x03",

            "#263F嘻嘻，艾丝蒂尔\x01",
            "有没有稍微变强了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F3")

    ChrTalk(    #79
        0x101,
        (
            "#1017F啊，算是吧。\x02\x01",

            "#1008F只有……一点点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x20,
        "#267F唔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A40")

    label("loc_29F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A40")

    ChrTalk(    #81
        0x102,
        "#1501F嗯，虽然只有一点点。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x20,
        "#267F唔……\x02",
    )

    CloseMessageWindow()

    label("loc_2A40")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x7)
    TalkEnd(0xFE)
    Jump("loc_2BE5")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B18")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A6E")
    TurnDirection(0xFE, 0x101, 0)

    label("loc_2A6E")


    ChrTalk(    #83
        0x20,
        (
            "#267F艾丝蒂尔每天\x01",
            "都在和约修亚一起练习吧。\x02\x03",

            "#261F嘻嘻……\x01",
            "以后让玲也来指导一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B12")

    ChrTalk(    #84
        0x101,
        (
            "#1016F啊、啊哈哈……\x01",
            "请手下留情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B12")

    TalkEnd(0xFE)
    Jump("loc_2BE5")

    label("loc_2B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 0)), scpexpr(EXPR_END)), "loc_2BA6")
    TalkBegin(0xFE)

    ChrTalk(    #85
        0x20,
        (
            "#266F……呼，\x01",
            "那三个人也真是的……\x02\x03",

            "要是和玲再稍微\x01",
            "多玩一会儿就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x109,
        "#1068F哎呀，饶了我吧……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2BE5")

    label("loc_2BA6")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #87
        0x20,
        "#1300F……………………………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_2BE5")

    Return()

    # Function_6_2385 end

    def Function_7_2BE6(): pass

    label("Function_7_2BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2DA8")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D01")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C89")

    ChrTalk(    #88
        0x1A,
        (
            "#070F……阿加特，准备好了。\x02\x03",

            "想要练习的话\x01",
            "随时可以找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x106,
        (
            "#051F不好意思……\x01",
            "一会儿一定过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFB")

    label("loc_2C89")


    ChrTalk(    #90
        0x1A,
        (
            "#573F虽然这个空间\x01",
            "到底是什么东西\x01",
            "还没有弄清楚……\x02\x03",

            "#070F不过这里\x01",
            "新鲜的空气确实\x01",
            "很能提起精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFB")

    OP_A2(0xE)
    Jump("loc_2D9D")

    label("loc_2D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D4F")

    ChrTalk(    #91
        0x1A,
        (
            "#074F嘶……………\x02\x03",

            "哈啊啊啊………………！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D9D")

    label("loc_2D4F")


    ChrTalk(    #92
        0x1A,
        (
            "#573F阿加特，你该认真一点了吧。\x02\x03",

            "#070F这种程度可打不倒我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9D")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_2DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_2EE0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5B")

    ChrTalk(    #93
        0x1A,
        (
            "#074F经过我对始祖小姐\x01",
            "所说的话的深思熟虑……\x02\x03",

            "我认为现在\x01",
            "我们是被拉入了\x01",
            "某个高位世界。\x02\x03",

            "#070F唔，打比方说\x01",
            "就像仙界之类的地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2EDA")

    label("loc_2E5B")


    ChrTalk(    #94
        0x1A,
        (
            "#074F虽然不清楚详细情况，\x01",
            "不过我觉得我们好像\x01",
            "来到了某个高位世界。\x02\x03",

            "#070F唔，打比方说\x01",
            "就像仙界之类的地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDA")

    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_2FF7")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F90")

    ChrTalk(    #95
        0x1A,
        (
            "#074F唔，如果把我们\x01",
            "卷进来的这个空间\x01",
            "真的能够受到意念影响的话……\x02\x03",

            "#072F『影之王』所设下的\x01",
            "后面的战斗试炼，\x01",
            "一定会要求强大的精神力。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2FF1")

    label("loc_2F90")


    ChrTalk(    #96
        0x1A,
        (
            "#074F以后的战斗，\x01",
            "一定会要求强大的精神力。\x02\x03",

            "恐怕『王』也做好了\x01",
            "这样的准备……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF1")

    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_2FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_3152")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F3")

    ChrTalk(    #97
        0x1A,
        (
            "#573F不过，上校的出现\x01",
            "有点超出我的意料。\x02\x03",

            "#070F这么说，有可能\x01",
            "卡西乌斯大人也会……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x1A,
        (
            "#073F不，等一下……\x02\x03",

            "#074F在共和国的我\x01",
            "既然都被卷入了进来，\x01",
            "那家伙也有可能……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_314C")

    label("loc_30F3")


    ChrTalk(    #99
        0x1A,
        "#572F……………………唔。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #100
        "\x07\x05看起来金正在担心地考虑什么事情。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_314C")

    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_3152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 3)), scpexpr(EXPR_END)), "loc_336C")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31E9")
    Jump("loc_322B")

    label("loc_31E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3205")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322B")

    label("loc_3205")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3221")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322B")

    label("loc_3221")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_322B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3306")

    ChrTalk(    #101
        0x1A,
        (
            "#074F看来『影之王』\x01",
            "确实是个不明身份的人……\x02\x03",

            "#070F不过那个『女性幽灵』\x01",
            "好像是我们的同伴呢。\x02\x03",

            "有这么多厉害的人聚在一起。\x01",
            "我们一定会有胜算的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3361")

    label("loc_3306")


    ChrTalk(    #102
        0x1A,
        (
            "#074F虽说『影之王』\x01",
            "是个不明身份的人……\x02\x03",

            "#070F不过我们一定会有胜算的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3361")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_336C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_370B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3403")
    Jump("loc_3445")

    label("loc_3403")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_341F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3445")

    label("loc_341F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_343B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3445")

    label("loc_343B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3445")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #103
        0x101,
        (
            "#1000F……哦，对了，金大哥。\x02\x03",

            "#1015F那个……\x01",
            "听说雾香小姐已经辞去了\x01",
            "协会接待员的职务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x1A,
        (
            "#573F哈哈……是啊。\x02\x03",

            "#070F其实她受到了\x01",
            "某个机构的征召……\x01",
            "虽然她也烦恼了一阵……\x02\x03",

            "……不过这也算是个好机会。\x01",
            "所以就回共和国去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1010F是吗…………\x02\x03",

            "#1006F这样的话\x01",
            "就没办法了。\x02\x03",

            "#1007F一想到没有\x01",
            "雾香小姐的蔡斯支部，\x01",
            "就会感到很寂寞啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x1A,
        (
            "#071F哈哈，你在说什么呢。\x02\x03",

            "#070F你们现在不是正在\x01",
            "各地巡回修行吗。\x02\x03",

            "那直接去共和国\x01",
            "见她不就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1008F啊，对啊。\x02\x03",

            "#1006F嗯，这样的话……\x02\x03",

            "离开这个世界以后\x01",
            "我们就去那里玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x1A,
        "#071F哦，那我们期待着。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2653)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_370B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_3914")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37A2")
    Jump("loc_37E4")

    label("loc_37A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37BE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37E4")

    label("loc_37BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37DA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37E4")

    label("loc_37DA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37E4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AE")

    ChrTalk(    #109
        0x1A,
        (
            "#074F在这『影之国』里\x01",
            "会出现不能用常识\x01",
            "理解的『魔物』……\x02\x03",

            "在下面的星层里\x01",
            "也许会有更加\x01",
            "超出想象的东西存在。\x02\x03",

            "#070F要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3909")

    label("loc_38AE")


    ChrTalk(    #110
        0x1A,
        (
            "#070F我也是第一次与\x01",
            "『魔物』作对手。\x02\x03",

            "必须看清敌人的特性\x01",
            "作出对应才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3909")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_3914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 2)), scpexpr(EXPR_END)), "loc_3A86")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39AB")
    Jump("loc_39ED")

    label("loc_39AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39C7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39ED")

    label("loc_39C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39E3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39ED")

    label("loc_39E3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39ED")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #111
        0x1A,
        (
            "#070F说起来，这里树的香味\x01",
            "和静静的瀑布声……\x02\x03",

            "唔，\x01",
            "让我想起了以前修行的时候……\x02",
        )
    )

    Jump("loc_3A7A")

    label("loc_3A7A")

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3F07")

    label("loc_3A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_3F07")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CC2")
    OP_51(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B33")
    Jump("loc_3B75")

    label("loc_3B33")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B4F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B75")

    label("loc_3B4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B6B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B75")

    label("loc_3B6B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B75")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #112
        0x1A,
        (
            "#074F是吗，你把头发剪了啊……\x02\x03",

            "#070F我听说你是在\x01",
            "戏团的时候留起长发的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        (
            "#1520F嗯………………\x02\x03",

            "不过，发生了这么多事……\x02\x03",

            "#1521F……想稍微转换一下心情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x1A,
        (
            "#573F…………是吗。\x02\x03",

            "#070F不过这也很适合你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x103,
        "#1527F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EF7")

    label("loc_3CC2")

    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D52")
    Jump("loc_3D94")

    label("loc_3D52")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D6E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D94")

    label("loc_3D6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D8A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D94")

    label("loc_3D8A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D94")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #116
        0x1A,
        (
            "#074F对了，\x01",
            "雪拉扎德好像把头发剪了啊……\x02\x03",

            "我听说她是在\x01",
            "戏团的时候留起长发的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#1500F好像是这样的。\x02\x03",

            "#1514F不过在上次的事件里，\x01",
            "雪拉姐姐也经历了很多事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x1A,
        (
            "#074F唔，的确……\x02\x03",

            "#070F不过，一定没问题的。\x01",
            "她的坚强是素有定评的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1501F嗯，我也这么觉得。\x02",
    )

    CloseMessageWindow()

    label("loc_3EF7")

    OP_A2(0x2652)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_3F07")

    Return()

    # Function_7_2BE6 end

    SaveToFile()

Try(main)