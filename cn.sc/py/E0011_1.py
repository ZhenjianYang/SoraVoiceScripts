from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'E0011_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0011_1 ._SN',
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
        "Function_1_7C2",          # 01, 1
        "Function_2_CFB",          # 02, 2
        "Function_3_1923",         # 03, 3
        "Function_4_226B",         # 04, 4
        "Function_5_32C6",         # 05, 5
        "Function_6_3A68",         # 06, 6
        "Function_7_3A7A",         # 07, 7
        "Function_8_4453",         # 08, 8
        "Function_9_48DD",         # 09, 9
        "Function_10_4C57",        # 0A, 10
        "Function_11_5167",        # 0B, 11
        "Function_12_54C1",        # 0C, 12
        "Function_13_59D0",        # 0D, 13
        "Function_14_5DDC",        # 0E, 14
        "Function_15_65B9",        # 0F, 15
        "Function_16_67D9",        # 10, 16
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3")
    Call(0, 57)

    label("loc_C3")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116310, 0, 3680, 0)
    OP_67(0, 6750, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 115700, 0, 3700, 90)
    SetChrSubChip(0x8, 1)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "#052F艾丝蒂尔……怎么了？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25D")

    ChrTalk(    #1
        0x101,
        (
            "#1016F#6P啊，没什么。\x01",
            "跟平常一样在船内散步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#051F是吗……\x02\x03",

            "嘿，你每次都是这样，\x01",
            "永远都逛不够啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1019F#6P这有什么关系。\x02\x03",

            "距离抵达柏斯\x01",
            "还有不少时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#051F也对，足够用来\x01",
            "睡一觉了。\x02\x03",

            "#552F不过，接下来是柏斯啊……\x02\x03",

            "继卢安、蔡斯和王都之后\x01",
            "又会发生什么事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_425")

    label("loc_25D")


    ChrTalk(    #5
        0x101,
        (
            "#1016F#6P啊，没什么。\x02\x03",

            "一搭上飞船\x01",
            "就想在船内散步了。\x02\x03",

            "光是坐在座位上\x01",
            "总感觉平静不下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#051F哈哈，还真是像你呢。\x02\x03",

            "#556F不过……\x01",
            "……真辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004F#6P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#051F就是关于到目前为止\x01",
            "『结社』所引发的事件。\x02\x03",

            "让你接连不断地跑遍\x01",
            "卢安、蔡斯和王都不是吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1025F#6P啊，嗯……\x02\x03",

            "阿加特你们才是，\x01",
            "为了调查情报部的余党\x01",
            "而奔走各地吧？\x02\x03",

            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#051F还好，我们只是\x01",
            "跑跑腿而已。\x02\x03",

            "#552F不过，接下来是柏斯啊……\x02\x03",

            "不知道又会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425")


    ChrTalk(    #11
        0x101,
        (
            "#1015F#6P嗯……\x02\x03",

            "最好不要发生什么事，\x01",
            "不过这似乎不大可能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#053F嗯嗯……\x02\x03",

            "#050F总之到了柏斯之后\x01",
            "就开始调查空贼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1020F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#052F……你在惊讶什么？\x02\x03",

            "也不能排除他们是\x01",
            "结社爪牙的可能性吧。\x02\x03",

            "这可是你说的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1008F#6P啊，嗯，是啊……\x02\x03",

            "#1013F但、但是我仔细想过后\x01",
            "又觉得那种可能性看来很低。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "#050F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1016F#6P那、那个，因为我\x01",
            "和他们交手好几次了。\x02\x03",

            "感觉他们不像是结社爪牙\x01",
            "那样的坏人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#053F……反正也没关系。\x02\x03",

            "#051F详细情况等到了柏斯\x01",
            "就能从卢格兰老爷子那里得知了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1007F#6P嗯……说得也是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1807)
    SetChrSubChip(0x8, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_7C1")

    label("loc_669")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_73B")

    label("loc_6F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_715")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73B")

    label("loc_715")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_731")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73B")

    label("loc_731")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73B")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #20
        0x8,
        (
            "#053F空贼艇的抢夺事件吗……\x02\x03",

            "#051F详细情况等到了柏斯\x01",
            "就能从卢格兰老爷子那里得知了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)

    label("loc_7C1")

    Return()

    # Function_0_AA end

    def Function_1_7C2(): pass

    label("Function_1_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBF")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117000, 0, -150, 0)
    OP_67(0, 6750, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0xC, 1)
    SetChrPos(0x101, 116240, 0, -160, 90)
    OP_0D()

    ChrTalk(    #21
        0xC,
        (
            "#073F哟，艾丝蒂尔。\x01",
            "你去了哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1025F#6P啊，嗯……\x01",
            "稍微去吹了吹风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "#070F这样啊。\x02\x03",

            "说起来下一站\x01",
            "好像是个叫洛连特的城市……\x02\x03",

            "我记得你家\x01",
            "就在那边吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1011F#6P啊，嗯。\x02\x03",

            "准确地说，不是在城里，\x01",
            "而是在郊外。\x02\x03",

            "似乎是老爸坚持要这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "#073F哦，原来如此。\x02\x03",

            "#071F不过大人建的房子\x01",
            "一定很漂亮吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1008F#6P唔……怎么说呢？\x02\x03",

            "先不管是不是漂亮，\x01",
            "总之住起来很舒适。\x02\x03",

            "充满了我和爸爸妈妈……\x01",
            "还有约修亚的回忆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        "#572F……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1016F#6P别、别这样，金先生。\x01",
            "不要一副那种表情嘛。\x02\x03",

            "#1017F如果真的到了洛连特，\x01",
            "是应该招待一下金先生的……\x02\x03",

            "不过还是下次吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        (
            "#070F啊啊，说得也是。\x02\x03",

            "……对了，艾丝蒂尔。\x02\x03",

            "到了柏斯以后\x01",
            "陪我练习练习吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1004F#6P啊……\x01",
            "怎么突然这么说呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        (
            "#075F在王都睡得太久，\x01",
            "没能好好地运动一下。\x02\x03",

            "我想活动活动僵化的身体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F#6P哈哈，是吗。\x02\x03",

            "#1006F唔～不知道我够不够格\x01",
            "当金先生的练习对手……\x02\x03",

            "不过我还是很乐意奉陪的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        "#071F好，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1808)
    SetChrSubChip(0xC, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_CFA")

    label("loc_BBF")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4F")
    Jump("loc_C91")

    label("loc_C4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C6B")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C91")

    label("loc_C6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C87")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C91")

    label("loc_C87")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C91")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #34
        0xC,
        (
            "#070F那么……\x02\x03",

            "也没有什么可做的事，\x01",
            "我就先睡一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)

    label("loc_CFA")

    Return()

    # Function_1_7C2 end

    def Function_2_CFB(): pass

    label("Function_2_CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C3")
    EventBegin(0x0)
    OP_44(0xD, 0x0)
    Fade(1000)
    OP_6D(89340, -1000, 53720, 0)
    OP_67(0, 7240, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 89280, -1000, 52860, 270)
    TurnDirection(0xD, 0x101, 0)
    SetChrSubChip(0xD, 0)
    OP_0D()

    ChrTalk(    #35
        0xD,
        "#040F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1011F#2P科洛丝。\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xD,
        (
            "#041F#6P嗯……\x01",
            "因为这里的景色很好。\x02\x03",

            "#542F艾丝蒂尔看起来\x01",
            "又是在散步吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1016F#2P啊……嗯，随便走走。\x02\x03",

            "#1025F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "#040F#6P……………………………\x02\x03",

            "#047F……约修亚，\x01",
            "他现在怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x101,
        (
            "#1020F#2P咦咦！？\x02\x03",

            "你、你、你怎么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        (
            "#048F#6P嘻……果然。\x02\x03",

            "奈尔先生他们\x01",
            "是跟你说有关他的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1004F#2P……………………………\x02\x03",

            "#1019F……你，是在套我的话？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "#045F#6P呵呵……\x01",
            "我可是女王候补哦。\x02\x03",

            "多少得会施展\x01",
            "一点小策略。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1007F#2P唉～败给你了。\x02\x03",

            "#1025F嗯……\x01",
            "确实是有关约修亚的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "#047F#6P……约修亚他没事，\x01",
            "而且还在利贝尔国内。\x02\x03",

            "不过有些事情\x01",
            "却使你高兴不起来……\x02\x03",

            "#040F是这么回事吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #46
        0xD,
        "#542F#6P那个，我猜对了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1007F#2P科洛丝……\x01",
            "你的洞察力太强了。\x02\x03",

            "#1006F我觉得你一定能成为\x01",
            "一位了不起的女王。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "#045F#6P呵呵，承蒙夸奖。\x02\x03",

            "#048F……不过，太好了。\x01",
            "约修亚他没事。\x02\x03",

            "光是知道了这点就令人高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1025F#2P嗯……\x01",
            "我也对此感到高兴……\x02\x03",

            "#1003F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        "#044F#6P艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1003F#2P逮捕戴尔蒙市长时……\x02\x03",

            "被市长用枪威胁的时候，\x01",
            "约修亚的态度你还记得吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "#042F#6P……是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1026F#2P如果我说约修亚现在的\x01",
            "眼神也和那时一样……\x02\x03",

            "科洛丝，你会怎样想？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        (
            "#043F#6P啊……\x02\x03",

            "#049F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1007F#2P对不起，科洛丝。\x02\x03",

            "我明明没跟你坦诚相对，\x01",
            "却还要对你说这些故弄玄虚的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "#047F#6P不……没关系。\x02\x03",

            "#040F艾丝蒂尔的烦恼，\x01",
            "我感觉能理解一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1025F#2P是吗……\x02\x03",

            "#1015F…………………………\x02\x03",

            "#1007F另、另外……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        "#044F#6P嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1013F#2P可、可能有点\x01",
            "小题大做了……\x02\x03",

            "我这么担心着他，\x01",
            "他却还跟女孩子在一起，你怎么想？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "#044F#6P………………………………\x02\x03",

            "#042F……那女孩子多大了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1007F#2P和我们差不多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "#043F#6P…………………………………\x01",
            "…………………………………\x02\x03",

            "#047F好像会涌现出一种\x01",
            "无法接受的心情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1005F#2P对、对吧！？\x02\x03",

            "果然是无法接受吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        (
            "#042F#6P嗯，当然了。\x02\x03",

            "#047F约修亚也是的……\x01",
            "到底在干些什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1019F#2P真是的……\x01",
            "找到他以后一定要质问他一天一夜。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0xD)
    Sleep(500)

    ChrTalk(    #66
        0x101,
        "#1016F#2P#1K呵呵……\x02",
    )


    ChrTalk(    #67
        0xD,
        "#045F#6P#1K呵呵……\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#1008F#2P谢谢你，科洛丝。\x02\x03",

            "我感觉心情\x01",
            "好一点点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        (
            "#048F#6P呵呵，不用客气。\x02\x03",

            "能帮上你我就很高兴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1017F#2P等我整理好心情\x01",
            "就会和大家说这件事的。\x02\x03",

            "你能等到那时候吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "#041F#6P嗯，当然。\x02\x03",

            "#040F……那么我就\x01",
            "先回座位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006F#2P嗯，回头见。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    def lambda_16CE():

        label("loc_16CE")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_16CE")

    QueueWorkItem2(0x101, 2, lambda_16CE)
    SetChrFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x20)
    OP_8E(0xD, 0x152CA, 0xFFFFFC18, 0xCE72, 0x9C4, 0x0)

    def lambda_16FD():
        OP_6D(88830, -1000, 50980, 2500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_16FD)
    OP_8E(0xD, 0x1531A, 0xFFFFFC18, 0xC1A2, 0x9C4, 0x0)
    ClearChrFlags(0xD, 0x4)
    OP_8E(0xD, 0x15676, 0x64, 0xABD6, 0x9C4, 0x0)

    def lambda_1742():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1742)
    OP_8E(0xD, 0x1575C, 0x64, 0xA7F8, 0x9C4, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_44(0x101, 0x2)
    Sleep(500)
    Fade(1000)
    OP_6D(89280, -1000, 52860, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1809)
    OP_A3(0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_1922")

    label("loc_17C3")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1853")
    Jump("loc_1895")

    label("loc_1853")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_186F")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1895")

    label("loc_186F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_188B")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1895")

    label("loc_188B")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1895")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #73
        0xD,
        (
            "#040F参加互不侵犯条约签字仪式的\x01",
            "外国来宾就快要到达\x01",
            "格兰赛尔了。\x02\x03",

            "要是能顺利\x01",
            "结束就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)

    label("loc_1922")

    Return()

    # Function_2_CFB end

    def Function_3_1923(): pass

    label("Function_3_1923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2117")
    EventBegin(0x0)
    OP_4A(0xB, 255)
    Fade(1000)
    OP_6D(58860, 0, -1390, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 58800, 0, -870, 180)
    OP_0D()

    ChrTalk(    #74
        0xB,
        "#063F#6P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1004F#5P提妲。\x01",
            "你在这里做什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #76
        0xB,
        (
            "#065F#8P啊……\x01",
            "艾丝蒂尔姐姐。\x02\x03",

            "#561F那个，我稍微\x01",
            "在想一些心事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1015F#5P心事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        (
            "#561F#8P嗯……\x02\x03",

            "#063F……我说，姐姐。\x02\x03",

            "我这个人毕竟还是\x01",
            "靠不住的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1004F#5P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        (
            "#062F#8P姐姐你\x01",
            "看起来好像有烦恼……\x02\x03",

            "在这件事情上，\x01",
            "我是不是帮不了你呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1003F#5P啊，这……\x02\x03",

            "#1007F真是失败啊。\x01",
            "连提妲都看出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xB,
        (
            "#065F#8P果然是这样……\x02\x03",

            "#562F任性地跟着大家来到这里，\x01",
            "可我却什么忙也帮不上……\x02\x03",

            "……也没能\x01",
            "挽留住玲……\x02\x03",

            "我……\x01",
            "果然是个累赘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1025F#5P提妲……\x02\x03",

            "#1016F傻孩子，\x01",
            "你很在意这些吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xB,
        "#065F#8P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1025F#5P我……\x01",
            "与其说是在愤怒\x01",
            "倒不如说是稍微有点混乱。\x02\x03",

            "光是依靠别人的话，\x01",
            "什么问题也解决不了……\x02\x03",

            "所以我现在只想……\x01",
            "一个人稍微考虑考虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xB,
        (
            "#063F#8P姐姐………\x02\x03",

            "现在有什么\x01",
            "我能帮上姐姐的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1006F#5P当然有。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    OP_8E(0x101, 0xE57E, 0x0, 0xFFFFF9C0, 0x3E8, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 43)
    SetChrSubChip(0xB, 0)
    OP_99(0xB, 0x0, 0x2, 0x3E8)
    Sleep(500)

    ChrTalk(    #88
        0xB,
        (
            "#064F#8P咦？\x02\x03",

            "#065F啊，姐姐！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1001F#5P嗯～这样果然最让人安心～\x02\x03",

            "温暖又光滑，\x01",
            "这种拥抱的感觉真是绝妙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        (
            "#067F#8P啊……\x01",
            "艾丝蒂尔姐姐真是的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1017F#5P我……\x01",
            "能有提妲在身边真是太好了。\x02\x03",

            "当然，对机械非常了解啦、\x01",
            "能解决专业问题这些都包括在内……\x02\x03",

            "不过只要看到提妲你的笑容，\x01",
            "就能让人打起精神来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        "#064F#8P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F#5P就算是玲，和你在一起时\x01",
            "不是也玩得很开心吗？\x02\x03",

            "虽然那也有可能\x01",
            "只是用来欺骗我们的演技……\x02\x03",

            "但是，我不觉得\x01",
            "一切都是谎言。\x02\x03",

            "我想那孩子也一定体会到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        (
            "#560F#8P是、是吗……\x02\x03",

            "#061F如果是这样……我也感到很开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1006F#5P呵呵。\x01",
            "你终于笑了。\x02\x03",

            "嗯嗯。\x01",
            "提妲果然还是笑起来最可爱！\x02\x03",

            "#1001F虽然偶尔出现快哭出来的\x01",
            "表情也算得上是很可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xB,
        (
            "#067F#8P真、真是的。\x01",
            "姐姐……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)
    OP_8F(0x101, 0xE57E, 0x0, 0xFFFFFC18, 0x320, 0x0)
    Sleep(500)

    ChrTalk(    #97
        0xB,
        (
            "#560F#8P谢谢姐姐。\x01",
            "谢谢你能这么说……\x02\x03",

            "我该回座位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1006F#5P嗯，一会儿见。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    def lambda_2087():

        label("loc_2087")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2087")

    QueueWorkItem2(0x101, 1, lambda_2087)
    OP_8E(0xB, 0xE1DC, 0x0, 0xFFFFF7EA, 0x9C4, 0x0)

    def lambda_20AC():
        OP_6D(59600, 0, 2700, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20AC)
    OP_8E(0xB, 0xE1BE, 0x0, 0x8B6, 0x9C4, 0x0)
    OP_8E(0xB, 0xEDDA, 0x0, 0x12FC, 0x9C4, 0x0)
    OP_8E(0xB, 0xEE8E, 0xAF0, 0x1FFD, 0x9C4, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_44(0x101, 0x1)
    OP_69(0x101, 0x640)
    OP_A2(0x180A)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_226A")

    label("loc_2117")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21A7")
    Jump("loc_21E9")

    label("loc_21A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21C3")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E9")

    label("loc_21C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21DF")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E9")

    label("loc_21DF")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21E9")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #99
        0xB,
        (
            "#560F似乎很快就要到洛连特了。\x02\x03",

            "目的地柏斯就在它的下一站，\x01",
            "所以还要花点时间吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)

    label("loc_226A")

    Return()

    # Function_3_1923 end

    def Function_4_226B(): pass

    label("Function_4_226B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3152")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xA, 0x0)
    OP_6D(31780, 0, 6980, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 31650, 0, 6980, 274)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 10)
    ClearChrFlags(0xA, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #100
        0xA,
        (
            "#035F嗯……原来如此。\x02\x03",

            "#030F那个，其实有几位记者\x01",
            "来找艾丝蒂尔了。\x02\x03",

            "后来她就变得有些怪怪的，\x01",
            "我还在想是什么事情呢……\x02\x03",

            "#035F呼，疑问终于得到了解答。\x02\x03",

            "…………………………………\x02\x03",

            "#030F嗯，这样就ＯＫ了。\x01",
            "没必要向王国军汇报。\x02\x03",

            "反正对有关他的事，\x01",
            "王国军应该都有所预测了。\x02\x03",

            "…………………………………\x02\x03",

            "#031F哈哈哈。\x01",
            "我的眼力还不错吧？\x02\x03",

            "呵呵，其实本来是很含糊的推测，\x01",
            "想不到居然误打误撞被我蒙对了。\x02\x03",

            "…………………………………\x02\x03",

            "#030F……知道了、知道了。\x01",
            "别发出那么可怕的声音。\x02\x03",

            "无论怎样，等你到了帝都后\x01",
            "就请立即着手准备吧。\x02\x03",

            "#032F啊……尽可能\x01",
            "不要让那个人插手进来。\x02\x03",

            "#035F就拜托你了，我的好友。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrSubChip(0xA, 5)
    OP_0D()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Fade(500)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #101
        0xA,
        (
            "#035F呼，想不到能和穆拉\x01",
            "打得不分伯仲……\x02\x03",

            "不愧是\x01",
            "前『结社』成员呢。\x02\x03",

            "#032F不过如果我\x01",
            "猜的没错的话……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 30720, 0, -1440, 0)
    ClearChrFlags(0x101, 0x80)

    ChrTalk(    #102
        0x101,
        "#1P没猜错什么？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2636():
        OP_6D(31560, 0, 6450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2636)

    def lambda_264E():
        OP_67(0, 7310, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_264E)

    def lambda_2666():
        OP_6E(282, 3000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2666)

    def lambda_2676():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2676)
    TurnDirection(0xA, 0x101, 400)
    OP_8E(0x101, 0x7648, 0x0, 0xA28, 0x9C4, 0x0)
    OP_8E(0x101, 0x7800, 0x0, 0x111C, 0x9C4, 0x0)
    TurnDirection(0x101, 0xA, 400)
    Sleep(500)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #103
        0xA,
        "#033F艾、艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1006F搞什么啊，在这里\x01",
            "偷偷摸摸地说悄悄话……\x02\x03",

            "#1004F咦，奇怪？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    TurnDirection(0x101, 0xA, 400)
    Sleep(500)

    ChrTalk(    #105
        0x101,
        "#1015F奥利维尔你在和谁说话？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "#035F呵呵，你在说什么呢？\x02\x03",

            "#030F难道我会和除了你之外的\x01",
            "其它女性在这种地方幽会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1019F真奇怪……\x02\x03",

            "我明明听见\x01",
            "你和别人说话的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "#031F哈哈哈，真拿你没办法。\x02\x03",

            "自言自语被你听见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1004F自、自言自语？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "#035F要说是自言自语\x01",
            "可能稍微有点不准确……\x02\x03",

            "#030F我只是把以前我饰演主角的\x01",
            "舞台剧的台词念了一下而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1020F舞台剧的台词……\x01",
            "为、为什么要在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        (
            "#034F目的地柏斯是离\x01",
            "埃雷波尼亚最近的地方……\x02\x03",

            "随着离那边距离的缩短，\x01",
            "我不禁顿起思乡之情。\x02\x03",

            "往昔那伤心的回忆\x01",
            "就不自觉地从口中流露出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1026F原、原来是这样……\x02\x03",

            "#1019F──你以为我就那么容易相信？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        "#033F唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1007F不管怎么看，奥利维尔\x01",
            "可疑的地方都很多。\x02\x03",

            "之前好像还和老爸\x01",
            "偷偷摸摸地商谈着什么。\x02\x03",

            "#1009F你也该告诉我你\x01",
            "真正的目的了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        (
            "#030F嗯～想不到会被你\x01",
            "这样穷追猛打。\x02\x03",

            "#031F你真是长大了，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1016F是大家把我锻炼成这样的。\x02\x03",

            "#1002F那么──你是说还是不说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "#035F呵呵，与其说这些，\x01",
            "我还是先给你吃颗定心丸吧。\x02\x03",

            "希望这样你能放过我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xA,
        (
            "#030F关于那艘空贼团的飞艇……\x02\x03",

            "被劫走应该也不至于\x01",
            "构成什么大问题才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1020F咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        (
            "#030F之前我也说过吧？\x02\x03",

            "#035F空贼团的成员\x01",
            "原本是埃雷波尼亚贵族这一点，\x01",
            "对帝国来说也不是件光彩的事。\x02\x03",

            "不过利贝尔为了\x01",
            "顺利签订互不侵犯条约，\x01",
            "也不想过于声张此事……\x02\x03",

            "#030F从这一点上来说，空贼艇\x01",
            "在现在遭劫正好可以\x01",
            "消除一个不安定因素。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1015F原来是这么回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        (
            "#035F当然，如果接下来空贼们不学乖，\x01",
            "还要干抢劫这类勾当的话就另当别论了。\x02\x03",

            "不过似乎不用担心这点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1025F的、的确……\x02\x03",

            "(有约修亚在，\x01",
            "也会阻止他们抢劫的……)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #126
        0x101,
        (
            "#1009F……你为什么知道\x01",
            "空贼们不会去抢劫？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#030F艾丝蒂尔你又为什么\x01",
            "会说出『的确』二字呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1019F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        (
            "#031F呵呵，那么……\x01",
            "我要回座位上去了。\x02\x03",

            "#030F艾丝蒂尔你要不要也一起？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1007F……我就算了吧。\x02\x03",

            "#1015F我说，奥利维尔。\x01",
            "我只问你一个问题可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xA,
        "#030F什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F奥利维尔的事我有\x01",
            "很多都不知道……\x02\x03",

            "#1002F即便如此我还是把你当作同伴，\x01",
            "并且非常信赖你。\x02\x03",

            "无论发生什么，我都会自作主张地\x01",
            "把你当成值得我信赖的人。\x02\x03",

            "#1013F……我这么做会不会给你添麻烦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xA,
        "#033F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1019F怎、怎么了啊。\x01",
            "眼睛睁得那么大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xA,
        (
            "#033F没、没有……\x02\x03",

            "#031F呵呵，怎么可能会\x01",
            "给我添麻烦呢？\x02\x03",

            "为了回报你的爱和信赖，\x01",
            "从现在起我要更加努力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1007F我可没给你什么爱……\x02\x03",

            "#1017F不过还是要谢谢你，奥利维尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xA,
        (
            "#031F呵呵，不用客气。\x02\x03",

            "#030F那么我就先告退了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_307E():
        OP_6D(30630, 0, 4390, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_307E)

    def lambda_3096():
        OP_6C(1000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3096)

    def lambda_30A6():

        label("loc_30A6")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_30A6")

    QueueWorkItem2(0x101, 1, lambda_30A6)
    OP_8E(0xA, 0x740E, 0x0, 0x1112, 0x9C4, 0x0)
    OP_8E(0xA, 0x7396, 0x0, 0xFFFFF1FA, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    SetChrFlags(0xA, 0x80)
    OP_44(0x101, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(30430, 0, 5730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 30430, 0, 5730, 180)
    OP_0D()
    OP_A2(0x180B)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_32C5")

    label("loc_3152")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31E2")
    Jump("loc_3224")

    label("loc_31E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31FE")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3224")

    label("loc_31FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_321A")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3224")

    label("loc_321A")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3224")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #138
        0xA,
        (
            "#035F呼，下一站就是\x01",
            "洛连特了吧。\x02\x03",

            "#030F虽然还想再品尝一次\x01",
            "使用天然原料制作的乡土菜肴……\x02\x03",

            "不过看来得等下次了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)

    label("loc_32C5")

    Return()

    # Function_4_226B end

    def Function_5_32C6(): pass

    label("Function_5_32C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(113330, 200, 4290, 0)
    OP_67(0, 6870, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x16, 60470, -2000, 52850, 0)
    SetChrPos(0x101, 113430, 0, 4430, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #139
        "\x07\x05……久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x32, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x32, 255)

    AnonymousTalk(    #140
        (
            "\x07\x05本船即将\x01",
            "抵达洛连特市。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_33AE():
        OP_8C(0x32, 0, 500)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_33AE)

    AnonymousTalk(    #141
        (
            "\x07\x05着陆时会有少许摇晃，\x01",
            "请尽快回到座位。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #142
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_3407():
        OP_6D(115290, 0, 2910, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3407)
    Sleep(500)
    SetChrSubChip(0x9, 1)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #143
        0x9,
        (
            "#020F#2P快点，艾丝蒂尔。\x01",
            "赶紧坐下。\x02\x03",

            "站着很危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#1025F#5P嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)

    def lambda_3489():
        OP_6D(116550, 0, 2320, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3489)
    OP_8E(0x101, 0x1C764, 0x0, 0x60E, 0x7D0, 0x0)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0x101, 0x4)
    SetChrSubChip(0x101, 0)
    OP_8C(0x101, 0, 400)
    Fade(500)
    SetChrPos(0x101, 116650, 100, 1200, 0)
    SetChrChipByIndex(0x101, 20)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #145
        (
            "\x07\x05承蒙各位今日搭乘飞船公社的航班，\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #146
        (
            "\x07\x05请在洛连特下船的旅客\x01",
            "检查是否有物品遗忘──。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0xBB8)

    def lambda_357D():
        OP_6D(116960, 200, 5430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_357D)

    def lambda_3595():
        OP_67(0, 4780, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3595)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(1000)
    OP_72(0x3, 0x4)
    OP_0D()
    Sleep(300)

    ChrTalk(    #147
        0x101,
        "#1004F#6P咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x9,
        "#023F#2P这是……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x51)
    Sleep(200)
    Fade(1000)
    OP_6D(59370, -450, 53240, 0)
    OP_67(0, 4630, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #149
        0x1E,
        "#5P这、这是什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x1E,
        (
            "#5P为什么会在这种高度\x01",
            "就进入云层之中！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x20,
        (
            "#5P不、不对……\x01",
            "这不像是云……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x1F,
        "#5P塔台传来联络！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x1F,
        (
            "#5P据说洛连特市一带\x01",
            "突然起了浓雾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x1E,
        "#5P你说什么……！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x9, 2)
    SetChrSubChip(0x8, 2)
    SetChrSubChip(0xA, 2)
    SetChrSubChip(0xD, 2)
    SetChrSubChip(0xB, 2)
    SetChrSubChip(0xC, 2)
    SetChrPos(0x32, 116140, 0, 11120, 40)
    OP_4B(0x32, 255)
    SetChrPos(0x31, 116790, 0, 10500, 40)
    SetChrChipByIndex(0x31, 46)
    OP_43(0x31, 0x0, 0x0, 0x2)
    OP_6D(118000, 100, 8660, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(118000, 100, 3330, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #155
        0x101,
        "#1020F#6P这、这是怎么回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xB,
        "#064F#6P哇……一片纯白啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "#030F#6P嗯……\x01",
            "是不是进入了云层？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x9,
        (
            "#022F#6P有可能……\x01",
            "不过这高度也太低了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xC,
        (
            "#072F#6P飞船着陆时\x01",
            "经常会遇到这种事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#552F#6P不，我看很少。\x01",
            "至少我从来没见过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        "#043F#6P我也是……\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #162
        (
            "\x07\x05……各位旅客。\x01",
            "请大家镇静。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #163
        (
            "\x07\x05据控制塔发来的联络，\x01",
            "目前得知在洛连特市一带\x01",
            "起了浓雾。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #164
        (
            "\x07\x05现在，为保证着陆时的视野，\x01",
            "飞船坪方面正在准备\x01",
            "夜间的照明设备。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #165
        "\x07\x05现在请各位旅客耐心等待。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #166
        0x101,
        (
            "#1015F#6P雾……\x02\x03",

            "洛连特确实会起雾，不过\x01",
            "最多也只是薄雾吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "#026F#6P嗯……\x01",
            "我不记得有过这么浓的雾。\x02\x03",

            "#022F……我有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_32C6 end

    def Function_6_3A68(): pass

    label("Function_6_3A68")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_A2(0x1A79)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_3A68 end

    def Function_7_3A7A(): pass

    label("Function_7_3A7A")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(57210, 0, -1640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(57590, 0, -1400, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 57220, 0, -1100, 180)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #168
        0x8,
        "#552F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1004F#5P啊……\x01",
            "你怎么了？阿加特？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        "#053F#6P……没什么。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #171
        0x8,
        "#051F你还在船内散步吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C56")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第４章最后有让阿加特加入】\x01",        # 0
            "【◇在第４章最后没有让阿加特加入】\x01",      # 1
            "【◇什么也没有变更】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C4A"),
        (1, "loc_3C50"),
        (SWITCH_DEFAULT, "loc_3C56"),
    )


    label("loc_3C4A")

    OP_A2(0x183C)
    Jump("loc_3C56")

    label("loc_3C50")

    OP_A3(0x183C)
    Jump("loc_3C56")

    label("loc_3C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 4)), scpexpr(EXPR_END)), "loc_3EC8")

    ChrTalk(    #172
        0x101,
        (
            "#1006F#5P嗯，算是吧。\x02\x03",

            "#1015F话说回来……\x01",
            "那个时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        "#052F那个时候……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1007F#5P哎呀，就是在神秘森林里\x01",
            "我们被催眠的时候啊。\x02\x03",

            "#1025F阿加特你也做梦了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        "#552F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1013F#5P啊……对、对不起。\x02\x03",

            "我是不是问了不该问的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#053F不……没这回事。\x02\x03",

            "#051F我也做了梦。\x02\x03",

            "感觉是一个\x01",
            "让我相当怀念的梦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1016F#5P是吗……\x01",
            "阿加特也是这样啊。\x02\x03",

            "#1008F嗯，那个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#551F喂喂，别这么露骨地\x01",
            "摆出一副想要知道的表情啊。\x02\x03",

            "#556F我梦见了小时候在村子里的\x01",
            "很平常的一些回忆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1016F#5P啊，哈哈……是这样啊。\x02\x03",

            "#1006F说起来，阿加特是\x01",
            "拉文努村出身的吧。\x02\x03",

            "也算是久违的重归故里了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2A")

    label("loc_3EC8")


    ChrTalk(    #181
        0x101,
        (
            "#1016F#5P嗯，算是吧。\x02\x03",

            "#1006F说起来，阿加特是\x01",
            "拉文努村出身的吧。\x02\x03",

            "也算是久违的重归故里了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3FAC")

    ChrTalk(    #182
        0x8,
        (
            "#052F不，因为那起特务兵事件，\x01",
            "前不久才刚刚顺道去过。\x02\x03",

            "#055F──喂，你给我等等。\x02\x03",

            "为什么你已经认定了\x01",
            "我要回村子去？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_402E")

    label("loc_3FAC")


    ChrTalk(    #183
        0x8,
        (
            "#051F嗯，算是有一阵子了。\x02\x03",

            "最近的一次还是在\x01",
            "诞辰庆典刚结束后…\x02\x03",

            "#055F──喂，你给我等等。\x02\x03",

            "为什么你已经认定了\x01",
            "我要回村子去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402E")


    ChrTalk(    #184
        0x101,
        (
            "#1001F#5P别害羞别害羞。\x02\x03",

            "#1006F我记得阿加特曾经说过\x01",
            "自己在故乡有个妹妹吧？\x02\x03",

            "#1028F嘿嘿，你一定\x01",
            "很疼爱她吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        "#555F我说你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1004F#5P对了，我记得阿加特的家\x01",
            "也是在拉文努村吧？\x02\x03",

            "#1015F以前因为空贼事件路过时，\x01",
            "倒是没遇到过类似的孩子呢。\x02\x03",

            "和鲁伊在一起的女孩子，\x01",
            "感觉上年纪也太小了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#051F……嗯，关于米夏，\x01",
            "在不久的将来我会向你们介绍的。\x02\x03",

            "如果有机会路过村子的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1016F#5P啊，嗯，拜托了。\x02\x03",

            "#1006F不过这样一来的话……\x01",
            "提妲也得一起带过去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        "#055F为、为什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1006F#5P因为提妲和阿加特\x01",
            "似乎相当亲近。\x02\x03",

            "如果不向她介绍的话，\x01",
            "她一定会很失望的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        "#552F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1004F#5P啊，我明白了！\x02\x03",

            "#1028F阿加特你是不想让妹妹\x01",
            "和提妲见面吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x8,
        "#052F什…什么…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1016F#5P哈哈，被我猜中了吗。\x02\x03",

            "#1006F因为她们两人会\x01",
            "围绕着阿加特互相吃醋的嘛。\x02\x03",

            "#1001F哎呀～\x01",
            "当哥哥真不容易啊㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        "#053F什么啊……原来是在说这个啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#1015F#5P？？？\x02\x03",

            "#1006F反正你不用担心，\x01",
            "到时候我会帮你的。\x02\x03",

            "所以你可以放心地把提妲\x01",
            "介绍给你妹妹哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#051F嘿嘿……说得也是。\x02\x03",

            "到时候就靠你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A03)
    OP_8C(0x8, 270, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_7_3A7A end

    def Function_8_4453(): pass

    label("Function_8_4453")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(90670, 0, 44790, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 255)
    OP_8C(0xB, 270, 0)
    SetChrPos(0x101, 90160, 0, 44840, 90)
    OP_0D()

    ChrTalk(    #198
        0xB,
        (
            "#061F啊，姐姐。\x01",
            "你又在散步吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4588")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第４章最后有让提妲加入】\x01",        # 0
            "【◇在第４章最后没有让提妲加入】\x01",      # 1
            "【◇什么也没有变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_457C"),
        (1, "loc_4582"),
        (SWITCH_DEFAULT, "loc_4588"),
    )


    label("loc_457C")

    OP_A2(0x183D)
    Jump("loc_4588")

    label("loc_4582")

    OP_A3(0x183D)
    Jump("loc_4588")

    label("loc_4588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 5)), scpexpr(EXPR_END)), "loc_47AC")

    ChrTalk(    #199
        0x101,
        (
            "#1006F#6P嗯，算是吧。\x02\x03",

            "#1015F话说回来……\x01",
            "提妲你呢？\x02\x03",

            "那时候你是不是也做了梦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xB,
        (
            "#066F啊，嗯。\x02\x03",

            "我梦见爸爸妈妈\x01",
            "回到家了。\x02\x03",

            "妈妈和爷爷久别重逢，\x01",
            "又在感情要好地斗嘴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#1016F#6P是、是这样啊。\x02\x03",

            "#1006F不过似乎是个\x01",
            "美梦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xB,
        (
            "#067F嘿嘿……嗯。\x02\x03",

            "因为姐姐你们\x01",
            "也一起出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#1004F#6P啊，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xB,
        (
            "#560F在爸爸妈妈\x01",
            "回家之后……\x02\x03",

            "姐姐和约修亚哥哥\x01",
            "还有阿加特哥哥都来家里。\x02\x03",

            "然后在爷爷的提议下，\x01",
            "大家一起去温泉玩了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#1001F#6P啊哈哈……\x01",
            "真是个相当快乐的梦呢。\x02\x03",

            "#1006F嗯……不过一定要\x01",
            "让这个美梦成真哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xB,
        "#061F嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_48CC")

    label("loc_47AC")


    ChrTalk(    #207
        0x101,
        (
            "#1006F#6P嗯，是啊。\x02\x03",

            "#1015F对了，提妲你是\x01",
            "第一次来柏斯吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xB,
        (
            "#560F嗯，是第一次。\x02\x03",

            "我听说柏斯\x01",
            "有家很大的商店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#1006F#6P哦，你是说柏斯超市啊。\x02\x03",

            "感觉就像是王都的百货商店\x01",
            "变大了的样子。\x02\x03",

            "里面有各种店铺，\x01",
            "非常的热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "#064F哇～好厉害。\x02\x03",

            "#067F嘿嘿嘿……\x01",
            "真想早点到柏斯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48CC")

    OP_8C(0xB, 90, 400)
    OP_4B(0xB, 255)
    OP_A2(0x1A04)
    EventEnd(0x0)
    Return()

    # Function_8_4453 end

    def Function_9_48DD(): pass

    label("Function_9_48DD")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(90670, 0, 44790, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 255)
    OP_8C(0xB, 270, 0)
    SetChrPos(0x101, 90160, 0, 44840, 90)
    OP_0D()

    ChrTalk(    #211
        0xB,
        (
            "#560F对了，姐姐。\x01",
            "你去过拉文努村吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1006F#6P嗯，以前因为工作去过。\x02\x03",

            "#1015F我记得……\x01",
            "那里是阿加特的故乡吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xB,
        (
            "#061F嗯，他妹妹米夏\x01",
            "小姐就住在那里。\x02\x03",

            "听说阿加特先生为了\x01",
            "探望妹妹，\x01",
            "一年要回去好几次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1004F#6P哦，还有这种事啊。\x02\x03",

            "#1006F不过，阿加特的妹妹啊……\x02\x03",

            "有个那么大大咧咧的哥哥，\x01",
            "也一定很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xB,
        (
            "#063F真是的～姐姐你怎么这么说。\x02\x03",

            "阿加特哥哥虽然有些粗鲁，\x01",
            "不过却是个很善良的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        (
            "#1016F#6P啊，知道了知道了。\x02\x03",

            "#1017F粗心又害羞这一点，\x01",
            "我也承认。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        (
            "#061F嘿嘿……\x02\x03",

            "#560F我觉得米夏小姐\x01",
            "一定是个很好的人。\x02\x03",

            "阿加特哥哥\x01",
            "每次提到米夏小姐时\x01",
            "眼神就变得很温柔……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#1004F#6P？　怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xB,
        (
            "#067F不，没什么。\x02\x03",

            "只不过有点……\x01",
            "心里有点复杂的感觉……\x02\x03",

            "嘿嘿，不知是怎么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1016F#6P（唔……\x01",
            "这好像是在吃醋呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)
    OP_4B(0xB, 255)
    OP_A2(0x1A05)
    EventEnd(0x0)
    Return()

    # Function_9_48DD end

    def Function_10_4C57(): pass

    label("Function_10_4C57")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(88790, 0, -3030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 88300, 0, -2780, 90)
    SetChrSubChip(0xA, 1)
    OP_0D()

    ChrTalk(    #221
        0xA,
        (
            "#030F哎呀，艾丝蒂尔。\x01",
            "马上就要到柏斯了。\x02\x03",

            "也就是说回到了我们\x01",
            "初次相遇的回忆之地。\x02\x03",

            "#035F呼……\x01",
            "多么令人感慨啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#1006F#6P被你这么一说，\x01",
            "确实很令人感慨……\x02\x03",

            "#1019F不过那时候的奥利维尔\x01",
            "可是个很没礼貌的人哦。\x02\x03",

            "居然说我『缺乏女性魅力』，\x01",
            "真是过分……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        (
            "#031F呵呵，这是个误会。\x02\x03",

            "你可以把那当作是我\x01",
            "看到心仪之人后，因为害羞\x01",
            "而做出的掩饰表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        (
            "#1007F#6P哼，又开始耍赖……\x02\x03",

            "#1009F明明对雪拉姐和约修亚\x01",
            "马上就发起攻势了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xA,
        (
            "#035F那种事就不要去计较啦。\x02\x03",

            "#030F现在的你，魅力\x01",
            "已经完全不逊于她们了。\x02\x03",

            "柔美又健康的性感，\x01",
            "再加上少女特有的娇羞……\x02\x03",

            "#031F嗯嗯，真是长大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        (
            "#1008F#6P谢、谢谢……\x02\x03",

            "#1013F等等，请你少说这种\x01",
            "会让人感觉不好意思的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xA,
        (
            "#035F呵呵，没什么好害羞的。\x02\x03",

            "#037F不过，你终于离成年人\x01",
            "又更近了一步。\x02\x03",

            "为了向更高层次迈进，\x01",
            "就让大哥哥我来亲切地指导……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1019F#6P这就不用你操心了。\x02\x03",

            "与其拜托奥利维尔，\x01",
            "我还不如去拜托雪拉姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xA,
        (
            "#034F呼，真遗憾。\x02\x03",

            "#033F不过由雪拉来亲切地\x01",
            "指导艾丝蒂尔啊……\x02\x03",

            "…………………………………\x02\x03",

            "#037F…………啊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        "#1005F#6P你、你在想象些什么啊！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第４章最后有让奥利维尔加入】\x01",        # 0
            "【◇在第４章最后没有让奥利维尔加入】\x01",      # 1
            "【◇什么也没有变更】\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5150"),
        (1, "loc_5156"),
        (SWITCH_DEFAULT, "loc_515C"),
    )


    label("loc_5150")

    OP_A2(0x183E)
    Jump("loc_515C")

    label("loc_5156")

    OP_A3(0x183E)
    Jump("loc_515C")

    label("loc_515C")

    SetChrSubChip(0xA, 0)
    OP_A2(0x1A07)
    EventEnd(0x0)
    Return()

    # Function_10_4C57 end

    def Function_11_5167(): pass

    label("Function_11_5167")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(88790, 0, -3030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 88300, 0, -2780, 90)
    SetChrSubChip(0xA, 1)
    OP_0D()

    ChrTalk(    #231
        0x101,
        (
            "#1004F#6P对了……\x02\x03",

            "#1015F奥利维尔那时候\x01",
            "也被催眠了吧。\x02\x03",

            "你一定也做梦了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        (
            "#033F嗯……算是吧。\x02\x03",

            "#032F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        "#1026F#6P？　怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xA,
        (
            "#034F不……\x01",
            "感觉实在是好～可惜啊。\x02\x03",

            "因为那是一个绝世美女\x01",
            "云集的后宫美梦啊。\x02\x03",

            "如果不是被艾丝蒂尔吵醒的话，\x01",
            "我还能做很多事的……\x02\x03",

            "#037F嘻嘻，现在也只能让艾丝蒂尔\x01",
            "你自己来补偿了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        "#1001F#6P要我用棍子来让你永远长眠吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xA,
        "#036F只是开玩笑啦！请原谅我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#1007F#6P真受不了……\x02\x03",

            "#1003F（不过奥利维尔……\x01",
            "刚才的眼神有点孤寂……)\x02\x03",

            "（究竟发生过什么事呢……？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xA,
        (
            "#035F呼……\x01",
            "没必要摆出这副表情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1004F#6P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        (
            "#030F不是什么了不起的梦。\x01",
            "只是少年时代的回忆罢了。\x02\x03",

            "穆拉等人也有在梦中登场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1025F#6P这样啊……\x02\x03",

            "#1019F那、那你\x01",
            "一开始就该这么说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xA,
        "#031F别生气嘛。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    OP_A2(0x1A08)
    EventEnd(0x0)
    Return()

    # Function_11_5167 end

    def Function_12_54C1(): pass

    label("Function_12_54C1")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116960, 0, 3460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116470, 0, 3640, 90)
    SetChrSubChip(0xD, 1)
    OP_0D()

    ChrTalk(    #243
        0xD,
        (
            "#040F艾丝蒂尔。\x01",
            "又在散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        (
            "#1008F#6P嘿嘿，算是吧。\x02\x03",

            "#1007F话说回来，真的很对不起。\x02\x03",

            "约修亚的事情\x01",
            "我那么晚才说出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xD,
        (
            "#041F呵呵，没有那么严重。\x02\x03",

            "#542F说起来，和约修亚\x01",
            "同行的女孩子\x01",
            "是空贼团的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#1019F#6P嗯，是一个名叫乔丝特，\x01",
            "相当刁蛮又很任性的女孩子。\x02\x03",

            "说话也像男孩子，\x01",
            "所以我叫她男人婆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        (
            "#542F是这样啊……\x02\x03",

            "#045F不过，光从照片来看的话，\x01",
            "也是位相当有魅力的女性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1007F#6P唔，我也承认她不开口的话\x01",
            "是个可爱的家伙。\x02\x03",

            "最开始遇见她的时候，\x01",
            "还天衣无缝地扮演了一回大小姐呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xD,
        "#044F？？？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #250
        (
            "\x07\x05向科洛丝诉说了在洛连特\x01",
            "市长家和乔丝特第一次见面时的情景。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #251
        0xD,
        (
            "#044F啊，还有这种事啊……\x02\x03",

            "#041F真是个相当有心机的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#1015F#6P因为她是埃雷波尼亚的\x01",
            "原贵族出身。\x02\x03",

            "所以擅于隐藏自己的真实面目。\x02\x03",

            "#1007F她的本性就像刚才说的，\x01",
            "性格上既刁蛮又很任性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xD,
        (
            "#048F呵呵，不过听到现在\x01",
            "却感觉让人憎恨不起来呢。\x02\x03",

            "我有种预感，如果试着和她\x01",
            "交谈的话一定会很合得来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1019F#6P唔，我可能不行。\x02\x03",

            "感觉性格上\x01",
            "和她相处不来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xD,
        (
            "#045F呵呵，这种事\x01",
            "也是常有的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C5")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第４章最后有让科洛丝加入】\x01",        # 0
            "【◇在第４章最后没有让科洛丝加入】\x01",      # 1
            "【◇什么也没有变更】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_59B9"),
        (1, "loc_59BF"),
        (SWITCH_DEFAULT, "loc_59C5"),
    )


    label("loc_59B9")

    OP_A2(0x183F)
    Jump("loc_59C5")

    label("loc_59BF")

    OP_A3(0x183F)
    Jump("loc_59C5")

    label("loc_59C5")

    SetChrSubChip(0xD, 0)
    OP_A2(0x1A09)
    EventEnd(0x0)
    Return()

    # Function_12_54C1 end

    def Function_13_59D0(): pass

    label("Function_13_59D0")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116960, 0, 3460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116470, 0, 3640, 90)
    SetChrSubChip(0xD, 1)
    OP_0D()

    ChrTalk(    #256
        0x101,
        (
            "#1004F#6P对了……\x02\x03",

            "#1015F科洛丝你那时候，\x01",
            "也被催眠了吧。\x02\x03",

            "你一定也做梦了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xD,
        (
            "#542F嗯……\x01",
            "是『百日战役』时的梦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1004F#6P『百日战役』时……\x02\x03",

            "#1025F这样啊，我记得那时候\x01",
            "你是和特蕾莎老师在一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xD,
        (
            "#040F嗯，受到老师她们的保护，\x01",
            "暂时生活在一起。\x02\x03",

            "#045F不过……呵呵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1004F#6P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xD,
        (
            "#048F不，明明是１０年前的事，\x01",
            "可是不知为什么克拉姆和乔儿他们\x01",
            "中途也都加进来了。\x02\x03",

            "如果一直做下去的话，\x01",
            "艾丝蒂尔和约修亚也\x01",
            "有可能会出现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1016F#6P哈哈，果然是梦境，\x01",
            "总会有不可思议的情景出现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xD,
        (
            "#045F嗯。\x02\x03",

            "#043F可是……\x01",
            "现在想想也还有点后怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        "#1026F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xD,
        (
            "#049F梦中的我真的很幸福……\x02\x03",

            "打从心底里希望日子能够\x01",
            "就这样一直保持下去。\x02\x03",

            "#043F可是我就是觉得\x01",
            "哪里有点不对劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        (
            "#1007F#6P嗯……\x01",
            "我明白你想说什么。\x02\x03",

            "#1002F做了个好梦，确实\x01",
            "感觉挺幸运的……\x02\x03",

            "可是如果问我还想不想再做这个梦，\x01",
            "我就会有点犹豫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xD,
        (
            "#047F嗯……\x02\x03",

            "#042F『福音』拥有着另一种\x01",
            "意义之下的危险性……\x02\x03",

            "我隐约能够感觉到这一点。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    OP_A2(0x1A0A)
    EventEnd(0x0)
    Return()

    # Function_13_59D0 end

    def Function_14_5DDC(): pass

    label("Function_14_5DDC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116890, 0, -550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116390, 0, -360, 90)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #268
        0xC,
        (
            "#071F哟，艾丝蒂尔。\x01",
            "这次辛苦你了。\x02\x03",

            "你又在游击士的\x01",
            "道路上前进了一步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1017F#6P嘿嘿……我还不够成熟。\x02\x03",

            "棒术的水平\x01",
            "也和老爸有千里之遥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xC,
        (
            "#070F哈哈，你不用太\x01",
            "在意大人的。\x02\x03",

            "#075FＳ级的游击士都是\x01",
            "一些悟出了『理』的高人。\x02\x03",

            "老实说，像我这种人花一辈子的时间\x01",
            "都不知道能不能达到那种程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#1004F#6P这、这样啊……\x02\x03",

            "#1025F虽然我对老爸有多强这一点，\x01",
            "到现在为止都没有什么真实感……\x02\x03",

            "不过『理』究竟是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xC,
        (
            "#074F嗯……这个嘛。\x02\x03",

            "#070F大人以前被称为『剑圣』，\x01",
            "是位剑术超群的人。\x02\x03",

            "可是他现在用起棍棒来\x01",
            "就像熟悉的剑一样挥洒自如。\x02\x03",

            "你知道这是为什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        "#1015F#6P嗯～拼命的练习？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xC,
        (
            "#070F当然这也是原因之一。\x02\x03",

            "不过更重要的是，他迅速地\x01",
            "掌握了棒术的本质。\x02\x03",

            "#074F那是超越了招式、反应、力量\x01",
            "和气劲的绝对高度……\x02\x03",

            "把握住事物的本质，\x01",
            "并能自由自在地操纵的境界……\x02\x03",

            "#072F这就是『理』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        "#1002F#6P事物的本质……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xC,
        (
            "#070F恐怕大人在『百日战役』中用来\x01",
            "击退了帝国军的谋略也是同样道理。\x02\x03",

            "正因为掌握了战争\x01",
            "这一事物的本质，才能设计\x01",
            "和实行了那么大胆的反攻作战。\x02\x03",

            "如果他是敌人的话，\x01",
            "一定是个最可怕的敌人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#1007F#6P原，原来如此……\x02\x03",

            "#1002F可是老爸在某种意义上来说，\x01",
            "也被『结社』钻了空子了啊。\x02\x03",

            "政变的时候\x01",
            "也被诱骗到了国外去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xC,
        (
            "#072F嗯，他们也一定拥有\x01",
            "能和大人匹敌的人物吧。\x02\x03",

            "虽然不知道那是『莱维』\x01",
            "还是『教授』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1015F#6P嗯～和我们战斗过的\x01",
            "『洛伦斯少尉』怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        (
            "#073F那家伙啊……\x02\x03",

            "#072F能力确实很强，\x01",
            "不过不知道能不能和大人匹敌。\x02\x03",

            "#572F而且我感觉那家伙的强\x01",
            "并不是来自于『理』。\x02\x03",

            "却像是一把被冷冰冰地磨透、锤炼，\x01",
            "不让任何人侵犯的利刃……\x02\x03",

            "就是那样的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#1002F#6P……嗯。\x01",
            "我可以明白你想说的。\x02\x03",

            "#1007F后来就没见过他了，\x01",
            "他究竟在干些什么呢……\x02\x03",

            "#1003F……约修亚似乎对他也很在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "#072F嗯，在『结社』时\x01",
            "可能有过什么因缘吧。\x02\x03",

            "#074F不管是我还是雪拉扎德，\x01",
            "都和他们有种巧妙因缘呢。\x02\x03",

            "这说不定……\x01",
            "也是女神的引导呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65AE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第４章最后有让金加入】\x01",        # 0
            "【◇在第４章最后没有让金加入】\x01",      # 1
            "【◇什么也没有变更】\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65A2"),
        (1, "loc_65A8"),
        (SWITCH_DEFAULT, "loc_65AE"),
    )


    label("loc_65A2")

    OP_A2(0x1840)
    Jump("loc_65AE")

    label("loc_65A8")

    OP_A3(0x1840)
    Jump("loc_65AE")

    label("loc_65AE")

    SetChrSubChip(0xC, 0)
    OP_A2(0x1A0B)
    EventEnd(0x0)
    Return()

    # Function_14_5DDC end

    def Function_15_65B9(): pass

    label("Function_15_65B9")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116890, 0, -550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116390, 0, -360, 90)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #283
        0x101,
        (
            "#1004F#6P啊，这么说来……\x02\x03",

            "#1015F金先生那时候\x01",
            "也被催眠了吧。\x02\x03",

            "是不是也做了什么梦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xC,
        (
            "#070F啊啊……\x01",
            "我梦见了在道场时的光景。\x02\x03",

            "#071F当我注意到雾香和现在\x01",
            "几乎没什么两样时，\x02\x03",

            "在梦中情不自禁地笑了出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#1011F#6P哦～？雾香小姐\x01",
            "从很早以前就是那样的感觉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xC,
        (
            "#070F嗯，一直是那样。\x02\x03",

            "真想不透，她那个样子\x01",
            "还能和瓦鲁特交往……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        "#1004F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xC,
        (
            "#075F……说漏嘴了。\x02\x03",

            "#070F不好意思，请你忘了刚才的话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        "#1013F#6P嗯、嗯。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    OP_A2(0x1A0C)
    EventEnd(0x0)
    Return()

    # Function_15_65B9 end

    def Function_16_67D9(): pass

    label("Function_16_67D9")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #290
        "\x07\x05……久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #291
        (
            "\x07\x05本船即将\x01",
            "到达柏斯市。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #292
        (
            "\x07\x05着陆时会有少许摇晃，\x01",
            "请尽快回到座位。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_67D9 end

    SaveToFile()

Try(main)
