from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_869",          # 01, 1
        "Function_2_4B9B",         # 02, 2
        "Function_3_4BAD",         # 03, 3
        "Function_4_4BB7",         # 04, 4
        "Function_5_4BD0",         # 05, 5
        "Function_6_4C8C",         # 06, 6
        "Function_7_4CA8",         # 07, 7
        "Function_8_4CEC",         # 08, 8
        "Function_9_4D0D",         # 09, 9
        "Function_10_4D29",        # 0A, 10
        "Function_11_4D83",        # 0B, 11
        "Function_12_4DEA",        # 0C, 12
        "Function_13_4E0A",        # 0D, 13
        "Function_14_4E34",        # 0E, 14
        "Function_15_4EE6",        # 0F, 15
        "Function_16_4F1B",        # 10, 16
        "Function_17_4F5E",        # 11, 17
        "Function_18_4F93",        # 12, 18
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_18E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B")

    ChrTalk(    #0
        0xFE,
        (
            "仓库里的年轻人们洗心革面\x01",
            "是少数的好消息之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "我在街角看见他们时\x01",
            "也会打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "照这样走上正道\x01",
            "就好了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_18B")

    label("loc_13B")


    ChrTalk(    #3
        0xFE,
        (
            "仓库里的年轻人们洗心革面\x01",
            "是少数的好消息之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "照这样走上正道\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B")

    Jump("loc_865")

    label("loc_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243")

    ChrTalk(    #5
        0xFE,
        (
            "导力器不能使用时，\x01",
            "城里一片骚乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "大惊失色的市民们\x01",
            "一齐拥到协会和市长官邸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "教区长尽力劝说\x01",
            "状况才总算好了点，\x01",
            "但还是有暴动会一触即发的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_295")

    label("loc_243")


    ChrTalk(    #8
        0xFE,
        (
            "导力器不能使用时，\x01",
            "城里一片骚乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "人们仿佛连理智\x01",
            "都同导力一起丢失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295")

    Jump("loc_865")

    label("loc_298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_43F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_331")

    ChrTalk(    #10
        0xFE,
        (
            "主日学校招了准游击士\x01",
            "来做讲师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "不过那个人，好像连协会规章\x01",
            "都记不好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "唉，平时要再\x01",
            "努力学习一下就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C")

    label("loc_331")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3")

    ChrTalk(    #13
        0xFE,
        (
            "哎呀，游击士。\x01",
            "前几天承蒙照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "那次授课，孩子们的\x01",
            "评价都很好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "今后也请为王国的和平\x01",
            "而努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C")

    label("loc_3B3")


    ChrTalk(    #16
        0xFE,
        (
            "哎呀，游击士。\x01",
            "前几天承蒙照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "只是，后面的问题\x01",
            "再努力学习一下就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "好像回答得不太好\x01",
            "那样可没法得到孩子们的信任哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C")

    Jump("loc_865")

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_6B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B2")

    ChrTalk(    #19
        0xFE,
        (
            "诸位，\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "托你们的福\x01",
            "终于没让孩子们失望了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_553")

    label("loc_4B2")

    OP_A2(0x3)

    ChrTalk(    #21
        0xFE,
        (
            "嗯，诸位……\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "托你们的福\x01",
            "终于没让孩子们失望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "各位游击士\x01",
            "百忙之中还麻烦你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "希望今后也能多加重视\x01",
            "和地区民众的接触。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_553")

    Jump("loc_668")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A6")

    ChrTalk(    #25
        0xFE,
        (
            "诸位，\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "以后基础性的知识\x01",
            "也请多加学习学习。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668")

    label("loc_5A6")

    OP_A2(0x3)

    ChrTalk(    #27
        0xFE,
        (
            "嗯，诸位……\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "请各位百忙之中抽空\x01",
            "我也深知这样说很冒昧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "但一般性的知识\x01",
            "也务必要掌握啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "各位掌管着地区的治安，\x01",
            "也是孩子们憧憬的对象哦。\x01",
            "请不要忘记这点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_668")

    Jump("loc_6B4")

    label("loc_66B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_67C")
    Call(1, 1)
    Jump("loc_6B4")

    label("loc_67C")


    ChrTalk(    #31
        0xFE,
        (
            "唉，讲师\x01",
            "还没好吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "再不来\x01",
            "授课都要结束了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4")

    Jump("loc_865")

    label("loc_6B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(    #33
        0xFE,
        (
            "刚才开始总觉得\x01",
            "外边好像吵吵嚷嚷的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "是错觉吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_865")

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_76D")

    ChrTalk(    #35
        0xFE,
        (
            "应该已经去找讲师了，\x01",
            "但游击士那边似乎没人在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "必须赶快请求\x01",
            "协会找个代替的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_805")

    label("loc_76D")

    OP_A2(0x3)

    ChrTalk(    #37
        0xFE,
        "唉，真伤脑筋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "应该已经去找游击士来当\x01",
            "主日学校的讲师了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "不凑巧那位由于工作关系\x01",
            "好像不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "呼，必须赶快\x01",
            "委托协会找个代替的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_805")

    Jump("loc_865")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_865")

    ChrTalk(    #41
        0xFE,
        (
            "选举运动的声音\x01",
            "从这里都听得见哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "似乎会扰乱祈愿者的安宁，\x01",
            "真令人感到为难。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_865")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_869(): pass

    label("Function_1_869")

    EventBegin(0x0)
    OP_4A(0xD, 255)
    Fade(1000)
    SetChrPos(0xF7, 54000, 0, 50610, 0)
    SetChrPos(0x101, 53000, 0, 50800, 0)
    SetChrPos(0x104, 52900, 0, 49660, 0)
    SetChrPos(0x127, 54100, 0, 49500, 0)
    OP_8C(0xD, 180, 0)
    OP_51(0x1A, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x1A, 0x0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_94C")

    ChrTalk(    #43
        0xD,
        "嗯，诸位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "讲师的工作\x01",
            "可以拜托你了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FE")

    label("loc_94C")


    ChrTalk(    #45
        0xD,
        "哎呀，诸位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "莫非你们\x01",
            "是看了公告板而来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1000F啊，嗯，看了哦。\x02\x03",

            "好像有要紧事\x01",
            "要委托我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "嗯，今天的主日学校\x01",
            "想请个讲师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        (
            "怎么样，\x01",
            "可以拜托你了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【听工作的说明】\x01",      # 0
            "【放弃】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD1")

    ChrTalk(    #50
        0x101,
        "#1007F抱歉，现在不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        "啊，那就为难了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "但是没办法呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        (
            "那么，事情办完的话\x01",
            "请马上再来。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x67, 0x1, 0x8000)
    OP_30(0x0)
    EventEnd(0x0)
    Return()

    label("loc_AD1")


    ChrTalk(    #54
        0x101,
        (
            "#1000F嗯，没问题。\x02\x03",

            "#1015F虽然没什么自信，\x01",
            "暂且试着做做看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "非常感谢。\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "本来委托的卡露娜小姐\x01",
            "突然出差……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "已经是\x01",
            "走投无路了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BA9")

    ChrTalk(    #58
        0x106,
        (
            "#050F原来如此啊……\x01",
            "所以才这么着急吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD7")

    label("loc_BA9")


    ChrTalk(    #59
        0x103,
        (
            "#020F原来如此呢……\x01",
            "所以才这么着急的吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD7")


    ChrTalk(    #60
        0x101,
        (
            "#1011F……那我该\x01",
            "怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        "是，首先请到隔壁房间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "在那边我把授课的内容\x01",
            "简单地说明一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x67, 0x4, 0x4)
    OP_28(0x67, 0x4, 0x8)
    OP_28(0x67, 0x1, 0x1)
    OP_28(0x67, 0x1, 0x2)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x101, -15920, 0, 42640, 0)
    SetChrPos(0xD, -15920, 0, 43790, 180)
    SetChrPos(0xF7, -16200, 0, 45190, 180)
    SetChrPos(0x104, -17400, 0, 44260, 135)
    SetChrPos(0x127, -17380, 0, 42570, 90)
    OP_6D(-11190, 0, 49840, 0)
    OP_51(0x1A, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D10():
        OP_69(0x1A, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D10)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0xD, 0x1)
    Sleep(400)

    ChrTalk(    #63
        0x101,
        (
            "#1012F……原来如此呢。\x02\x03",

            "#1006F嗯，授课的方法\x01",
            "我想大致能理解了。\x02\x03",

            "从对协会手册的复习开始\x01",
            "其次是游击士职务的说明……\x02\x03",

            "最后正确回答孩子们\x01",
            "的问题就行了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        "对，这样就可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        "那么，我就回去授课了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "结束后来叫你，\x01",
            "请先在这里等候。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E2F():

        label("loc_E2F")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_E2F")

    QueueWorkItem2(0xF7, 1, lambda_E2F)

    def lambda_E40():

        label("loc_E40")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_E40")

    QueueWorkItem2(0x104, 1, lambda_E40)

    def lambda_E51():

        label("loc_E51")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_E51")

    QueueWorkItem2(0x127, 1, lambda_E51)
    OP_8B(0xD, 0xFFFFC7CA, 0xB7F2, 0x190)

    def lambda_E6F():
        OP_6D(-14950, 0, 45890, 2000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_E6F)
    OP_8E(0xD, 0xFFFFC7C0, 0x0, 0xB0FE, 0x7D0, 0x0)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    OP_8E(0xD, 0xFFFFCC48, 0x0, 0xB798, 0x7D0, 0x1)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_EC6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_EC6)
    OP_8E(0xD, 0xFFFFD404, 0x0, 0xB798, 0x7D0, 0x0)
    SetChrPos(0xD, 48141, 1000, 50075, 180)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xD, 0x2)
    Sleep(800)

    def lambda_F12():
        TurnDirection(0x104, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F12)

    def lambda_F20():
        TurnDirection(0x127, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_F20)
    OP_43(0xF7, 0x1, 0x1, 0x6)
    OP_6D(-16500, 0, 44400, 2000)
    Sleep(400)

    ChrTalk(    #67
        0x104,
        (
            "#030F嗯，不过……\x02\x03",

            "还真有世事难料的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_FAF")

    ChrTalk(    #68
        0x106,
        (
            "#050F呵，难得和你意见一致。\x02\x03",

            "我也这么想。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_FAF")


    ChrTalk(    #69
        0x103,
        (
            "#027F哎呀，难得和你意见一致呢。\x02\x03",

            "我也这么想哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE4")

    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x101, 0x104, 400)
    Sleep(1000)

    ChrTalk(    #70
        0x101,
        (
            "#1011F嗯？你们俩怎么了？\x02\x03",

            "我脸上有什么东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x104,
        (
            "#031F呀，就算是我\x01",
            "也料不到啊。\x02\x03",

            "没想到艾丝蒂尔\x01",
            "竟有站上讲台的一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x127,
        "#151F嗯嗯，吓我一跳。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10EB")

    ChrTalk(    #73
        0x106,
        (
            "#051F啊啊，一点不错。\x02\x03",

            "这家伙比起教人\x01",
            "还是更像被教的类型啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_10EB")


    ChrTalk(    #74
        0x103,
        (
            "#021F主日学校的逃课惯犯\x01",
            "也成长至今了啊。\x02\x03",

            "呀～姐姐真是开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112D")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#1009F有、有你们这样说话的吗～\x02\x03",

            "虽说确实没什么自信，\x01",
            "但教教孩子们还是能行的啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_11F4")

    ChrTalk(    #76
        0x106,
        (
            "#053F呼，是就好了……\x02\x03",

            "#050F……那，结束之前\x01",
            "我先去小睡一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_11F4")


    ChrTalk(    #77
        0x103,
        (
            "#026F是就好了……\x02\x03",

            "#020F那，结束之前\x01",
            "我就休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122F")

    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #78
        0x101,
        "#1000F奥利维尔你们怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x104,
        (
            "#031F呼，虽然力量微薄\x01",
            "也让我支持下艾丝蒂尔吧。\x02\x03",

            "这里的２楼\x01",
            "能把授课看得清清楚楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x127, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #80
        0x127,
        (
            "#153F哦～ＮＩＣＥ　ＩＤＥＡ嘛～\x02\x03",

            "#151F我也带相机去～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x127, 400)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        (
            "#1019F你们两个……\x01",
            "可别妨碍我哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x400000)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_137A")
    SetChrPos(0x103, 52248, 5000, 50355, 90)

    label("loc_137A")

    SetChrPos(0x104, 52248, 5000, 49470, 90)
    SetChrPos(0xD, 52960, 0, 48670, 90)
    OP_4A(0xC, 255)
    OP_4A(0xF, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x10, 255)
    OP_4A(0xB, 255)
    OP_6D(52220, 5000, 48532, 0)
    OP_6B(3789, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)

    def lambda_13E3():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_13E3)

    def lambda_13F3():
        OP_6D(58920, 1000, 50630, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_13F3)
    OP_6C(320000, 3000)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(    #82
        0xC,
        "好了────\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "那么，现在开始\x01",
            "由讲师来授课。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "人家特地来为大家授课，\x01",
            "大家要有礼貌哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        "#5P是～～\x02",
    )


    ChrTalk(    #86
        0x11,
        "#2P是～～\x02",
    )


    ChrTalk(    #87
        0x12,
        "#2P是～～\x02",
    )


    ChrTalk(    #88
        0x10,
        "#1P是～～\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_8C(0xC, 90, 400)
    OP_8E(0xC, 0xF050, 0x3E8, 0xCC38, 0x7D0, 0x0)
    OP_8C(0xC, 180, 400)
    OP_6D(54420, 0, 51310, 2000)
    OP_8B(0xD, 0xCA84, 0xC49A, 0x190)

    ChrTalk(    #89
        0xD,
        "那么，请──\x02",
    )

    CloseMessageWindow()
    OP_43(0x1A, 0x0, 0x1, 0x2)
    OP_43(0xF, 0x0, 0x1, 0x5)
    OP_43(0x11, 0x0, 0x1, 0x5)
    OP_43(0x10, 0x0, 0x1, 0x5)
    OP_43(0x12, 0x0, 0x1, 0x5)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 50390, 0, 50280, 90)

    def lambda_1547():

        label("loc_1547")

        TurnDirection(0xD, 0x101, 400)
        OP_48()
        Jump("loc_1547")

    QueueWorkItem2(0xD, 1, lambda_1547)

    def lambda_1558():

        label("loc_1558")

        TurnDirection(0xC, 0x101, 400)
        OP_48()
        Jump("loc_1558")

    QueueWorkItem2(0xC, 1, lambda_1558)

    def lambda_1569():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1569)
    OP_8E(0x101, 0xDB60, 0x3E8, 0xC468, 0x7D0, 0x0)
    OP_8E(0x101, 0xE196, 0x3E8, 0xCBE8, 0x7D0, 0x0)
    OP_8E(0x101, 0xE65A, 0x3E8, 0xCBB6, 0x7D0, 0x0)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    WaitChrThread(0x1A, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x12, 0x0)

    def lambda_15D8():
        OP_8C(0xF, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_15D8)

    def lambda_15E6():
        OP_8C(0x11, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15E6)

    def lambda_15F4():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15F4)
    OP_8C(0x12, 315, 400)

    ChrTalk(    #90
        0x12,
        "#2P姐姐，你是～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)
    Sleep(250)

    ChrTalk(    #91
        0x101,
        "#1016F这、这就自我介绍，别急哦。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0xD, 0x1)
    OP_44(0xC, 0x1)
    OP_8C(0x101, 180, 400)
    Sleep(1000)

    ChrTalk(    #92
        0x101,
        (
            "#1018F……嗯……大家好！\x02\x03",

            "姐姐叫做\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "虽然还是新人，\x01",
            "但也算是游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #93
        0xF,
        "#5P咦～是游击士～～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        "#2P骗人吧，帅呆了～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x11,
        "#5P姐姐多大了～！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(    #96
        0xC,
        "喂喂，待会儿才提问呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xC,
        (
            "首先让老师\x01",
            "复习一下之前的内容。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #98
        0xC,
        "──那么，请多指教啦。\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x1, 0x7)
    OP_43(0xD, 0x1, 0x1, 0x8)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #99
        0x101,
        "#1010F唔咳…………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    Sleep(600)

    ChrTalk(    #100
        0x101,
        (
            "#1006F……那，大家\x01",
            "准备好了吗？\x02\x03",

            "立刻开始今天\x01",
            "授课中的复习吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)
    OP_20(0x3E8)
    Fade(1000)
    OP_6D(59000, 1000, 53470, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(400)
    OP_1D(0x19)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #101
        (
            "\x07\x05授课开始！\x01",
            "～关于游击士的全部活动～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #102
        (
            "\x07\x05　※选择正确的答案\x01",
            "　　引导特别授课走向成功！　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)

    ChrTalk(    #103
        0x101,
        (
            "#1006F#5P首先是我的工作，\x01",
            "关于游击士的事。\x02\x03",

            "游击士\x01",
            "是调查和战斗的专家。\x02\x03",

            "我们\x01",
            "游击士的主要使命…………\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #104
        "\x18游击士的使命是？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①国土的防卫与治安的保障】\x01",          # 0
            "【②地区的和平与民间人士的保护】\x01",      # 1
            "【③古代遗物的发现与封印】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1ABB"),
        (1, "loc_1B87"),
        (2, "loc_1C45"),
        (SWITCH_DEFAULT, "loc_1D1F"),
    )


    label("loc_1ABB")


    ChrTalk(    #105
        0x101,
        "#1006F#5P……是国土的防卫与治安的保障。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #106
        0x101,
        (
            "#1015F#5P唔……为了保卫治安\x01",
            "需要抵御外敌的侵入。\x02\x03",

            "（感、感觉好像不大一样……\x01",
            "  总、总之现在必须先继续。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_1D1F")

    label("loc_1B87")


    ChrTalk(    #107
        0x101,
        (
            "#1006F#5P……是地区的和平与民间人士的保护。\x02\x03",

            "不仅仅是击退魔兽和防止犯罪，\x01",
            "还要护送物品和寻找遗失物，\x01",
            "是以各种各样的形式为地区作贡献的工作。\x02\x03",

            "#1001F（好！刚才表现很完美。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1D1F")

    label("loc_1C45")


    ChrTalk(    #108
        0x101,
        "#1006F#5P……是古代遗物的发现与封印。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #109
        0x101,
        (
            "#1008F#5P当、当然，不止是这些，\x01",
            "但最近可是找到了很了不起的东西哦。\x02\x03",

            "#1007F（明、明显错误……\x01",
            "  总、总之现在必须先继续。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_1D1F")

    label("loc_1D1F")

    Call(1, 12)

    ChrTalk(    #110
        0x101,
        (
            "#1000F#5P我们游击士的身份\x01",
            "有正游击士和准游击士两种。\x02\x03",

            "其中所谓准游击士\x01",
            "可以说像见习一样……\x02\x03",

            "在这时积累功绩，\x01",
            "最后晋升为正游击士。\x02\x03",

            "#1015F不过，成为正游击士以后\x01",
            "又有另外的阶级划分。\x02\x03",

            "被称为『Ｒａｎｋ』，\x01",
            "这个阶段根据经验和实际成绩……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #111
        "\x18正游击士的Ｒａｎｋ有几等级？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①从Ｇ级到Ａ级共７等级】\x01",      # 0
            "【②从初级到上级共５等级】\x01",      # 1
            "【③从９级到１级共９等级】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EE1"),
        (1, "loc_1FE5"),
        (2, "loc_2087"),
        (SWITCH_DEFAULT, "loc_20F9"),
    )


    label("loc_1EE1")


    ChrTalk(    #112
        0x101,
        (
            "#1006F#5P……从Ｇ级到Ａ级共７等级。\x02\x03",

            "正式的阶级就这７级，\x01",
            "接近升级时阶级上会附上『＋』。\x02\x03",

            "#1015F还有更高的Ｓ级，\x01",
            "不过那是建立了特殊功绩的人物\x01",
            "被非正式授予的名誉阶级。\x02\x03",

            "#1006F所以一般来说Ａ级的人\x01",
            "就是最高Ｒａｎｋ的游击士了。\x02\x03",

            "（嗯，没错吧。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_20F9")

    label("loc_1FE5")


    ChrTalk(    #113
        0x101,
        "#1006F#5P……从初级到上级共５等级。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        (
            "#1016F#5P……很、很容易明白吧。\x01",
            "虽说太土了点。\x02\x03",

            "（太、太可疑了…………）\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0xB)
    Sleep(1000)
    Jump("loc_20F9")

    label("loc_2087")


    ChrTalk(    #115
        0x101,
        (
            "#1006F#5P……从９级到１级共９等级。\x02\x03",

            "根据完成的工作\x01",
            "逐渐提高等级。\x02\x03",

            "#1015F（咦？这不是\x01",
            "说准游击士的吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F9")

    label("loc_20F9")

    Call(1, 12)

    ChrTalk(    #116
        0x101,
        (
            "#1011F#5P好了，约束游击士们的组织\x01",
            "是大家都知道的游击士协会。\x02\x03",

            "#1000F我想你们都学过了，\x01",
            "协会不仅在利贝尔王国，\x01",
            "在大陆的各处都有活动。\x02\x03",

            "这个世界性组织的设立\x01",
            "是在与导力革命基本同时代的…………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #117
        "\x18游击士协会成立的时间是？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①距今约１０年前】\x01",      # 0
            "【②距今约３０年前】\x01",      # 1
            "【③距今约５０年前】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2278"),
        (1, "loc_2306"),
        (2, "loc_2392"),
        (SWITCH_DEFAULT, "loc_2422"),
    )


    label("loc_2278")


    ChrTalk(    #118
        0x101,
        "#1000F#5P……距今约１０年前。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #119
        0x101,
        (
            "#1008F#5P好、好像意外的近呢。\x02\x03",

            "（啊……１０年前\x01",
            "不是百日战役吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2422")

    label("loc_2306")


    ChrTalk(    #120
        0x101,
        "#1000F#5P……距今约３０年前。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #121
        0x101,
        (
            "#1008F#5P比、比想象的近呢。\x02\x03",

            "（呜哇～完全没自信。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_2422")

    label("loc_2392")


    ChrTalk(    #122
        0x101,
        (
            "#1000F#5P……距今约５０年前。\x02\x03",

            "导力技术与协会渊源深厚，\x01",
            "现在似乎也有受到导力器相关财团\x01",
            "的资金援助哦。\x02\x03",

            "（嗯，确实是这样吧。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2422")

    label("loc_2422")

    Call(1, 13)

    ChrTalk(    #123
        0x101,
        (
            "#1015F#5P嗯……接下来是游击士与\x01",
            "各国关系的问题哦。\x02\x03",

            "现在，游击士协会\x01",
            "在大陆全境都有设立支部……\x02\x03",

            "能发展壮大至此是因为\x01",
            "协会是一个不与特定国家\x01",
            "相关联的非政府性组织。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    Sleep(400)

    ChrTalk(    #124
        0x101,
        (
            "#1006F#5P但是，在实际活动中\x01",
            "游击士协会也必须考虑许多东西。\x02\x03",

            "譬如为了防止与国家对立\x01",
            "必须遵守一些约定俗成的规则。\x02\x03",

            "其中最有名的规定是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #125
        "\x18协会与国家的约定是？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①与国家军队的非战斗协议】\x01",      # 0
            "【②不逮捕贵族·王族】\x01",            # 1
            "【③不干涉国家权力】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2629"),
        (1, "loc_26EF"),
        (2, "loc_27BB"),
        (SWITCH_DEFAULT, "loc_2872"),
    )


    label("loc_2629")


    ChrTalk(    #126
        0x101,
        (
            "#1000F#5P……与国家军队的非战斗协定。\x02\x03",

            "就是说，不与那个国家\x01",
            "的军队作战的协定。\x02\x03",

            "因为在万不得已的时候\x01",
            "说不定会成为敌人的组织，\x01",
            "谁都不会接受的。\x02\x03",

            "#1015F（感觉没错，\x01",
            "　不过总觉得不大合适……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2872")

    label("loc_26EF")


    ChrTalk(    #127
        0x101,
        (
            "#1002F#5P……不逮捕贵族·王族。\x02\x03",

            "就是说，不逮捕\x01",
            "身份高贵者的协定。\x02\x03",

            "即使国王做了坏事\x01",
            "能够裁决的也是那个国家的人民。\x02\x03",

            "插手他国内务\x01",
            "是违反国际准则的。\x02\x03",

            "#1015F（应该没错吧，\x01",
            "　嗯～有这样的规定吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2872")

    label("loc_27BB")


    ChrTalk(    #128
        0x101,
        (
            "#1002F#5P……不干涉国家权力。\x02\x03",

            "就是说，不参与\x01",
            "国家及其机关的事。\x02\x03",

            "国家内部问题，\x01",
            "完全归其国民管理。\x02\x03",

            "插手这样的事\x01",
            "是违反国际准则的。\x02\x03",

            "#1018F（好～～说明得很顺利！）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2872")

    label("loc_2872")

    Call(1, 12)

    ChrTalk(    #129
        0x101,
        (
            "#1000F#5P协会就是这样以各种手段\x01",
            "为国家分担大任。\x02\x03",

            "#1015F当然，并不是所有事情\x01",
            "都是遵照规则就能很好地解决的……\x02\x03",

            "碰上紧急事态也可能会\x01",
            "处于与规则相矛盾的立场。\x02\x03",

            "#1002F不过这种时候，\x01",
            "游击士们只要遵从原则\x01",
            "来行动就可以了。\x02\x03",

            "总之，我们游击士\x01",
            "在任何情况下……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #130
        "\x18游击士在任何情况下都必须……？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①优先政府方面的判断】\x01",        # 0
            "【②优先保护民间人士】\x01",          # 1
            "【③优先与国家军队的合作】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A41"),
        (1, "loc_2B00"),
        (2, "loc_2BBB"),
        (SWITCH_DEFAULT, "loc_2C78"),
    )


    label("loc_2A41")


    ChrTalk(    #131
        0x101,
        (
            "#1002F#5P……优先政府方面的判断。\x02\x03",

            "#1015F与活动地区的国家进行对立\x01",
            "是必须避免的问题。\x02\x03",

            "发生大事件的时候\x01",
            "会变得更加重要哦。\x02\x03",

            "#1019F（虽然听起来挺象样的……\x01",
            "　但规章里应该没有这条吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C78")

    label("loc_2B00")


    ChrTalk(    #132
        0x101,
        (
            "#1002F#5P……优先保护民间人士。\x02\x03",

            "只要优先考虑这个，\x01",
            "行动自然会被引向正途。\x02\x03",

            "不过，展开行动时\x01",
            "也会出现各种问题，\x01",
            "要克服这些也是必要的能力哦。\x02\x03",

            "#1006F（嗯，总结得很好！）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2C78")

    label("loc_2BBB")


    ChrTalk(    #133
        0x101,
        (
            "#1002F#5P……优先与国家军队的合作。\x02\x03",

            "与国家军队的合作\x01",
            "在游击士的工作里是不可或缺的。\x02\x03",

            "相互弥补彼此的弱点，\x01",
            "任何事件都能解决哦。\x02\x03",

            "#1019F（……虽说是事实，\x01",
            "但规章里应该没有这条吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C78")

    label("loc_2C78")

    Call(1, 12)
    Sleep(1000)

    ChrTalk(    #134
        0x101,
        (
            "#1000F#5P──以上，复习到此结束了哦。\x02\x03",

            "#1001F#5P如何？　大家明白了吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    Fade(1000)
    OP_6D(51560, 5000, 50610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(400)
    OP_43(0x19, 0x1, 0x1, 0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2EAB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2DA2")

    ChrTalk(    #135
        0x104,
        (
            "#030F#1P嗯，这样授课的前半段就结束了吧。\x02\x03",

            "#031F不过，真不愧是艾丝蒂尔。\x02\x03",

            "毫不胆怯\x01",
            "教得有模有样的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_2DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E32")

    ChrTalk(    #136
        0x104,
        (
            "#030F#1P嗯，这样授课的前半段就结束了吧。\x02\x03",

            "可是，就连艾丝蒂尔\x01",
            "这次好像也陷入苦战了那。\x02\x03",

            "那么，从这里开始\x01",
            "还能挽回多少呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_2E32")


    ChrTalk(    #137
        0x104,
        (
            "#030F#1P嗯，这样授课的前半段就结束了吧。\x02\x03",

            "#031F不过，真不愧是艾丝蒂尔。\x02\x03",

            "说得那样风马牛不相及\x01",
            "居然还能如此镇定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA8")

    Jump("loc_2FDC")

    label("loc_2EAB")


    ChrTalk(    #138
        0x104,
        "#030F#1P嗯，这样授课的前半段就结束了吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F24")

    ChrTalk(    #139
        0x103,
        (
            "#021F#5P呵呵，挺努力的嘛。\x02\x03",

            "那孩子\x01",
            "什么时候学习过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2F24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F85")

    ChrTalk(    #140
        0x103,
        (
            "#025F#5P话说回来，真是好险。\x02\x03",

            "那孩子真是，不知道的事\x01",
            "还堂堂正正的胡编乱造。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDC")

    label("loc_2F85")


    ChrTalk(    #141
        0x103,
        (
            "#025F#5P啊～真是看不下去了。\x02\x03",

            "那孩子大部分\x01",
            "都是在胡编乱造嘛。\x02\x03",

            "真亏教区长忍得住。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDC")

    OP_59()
    Sleep(400)
    Fade(1000)
    SetChrPos(0xC, 61337, 1000, 50629, 180)
    OP_6D(60430, 1000, 50280, 0)
    OP_44(0x19, 0x1)
    SetChrChipByIndex(0x19, 22)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #142
        0xC,
        (
            "好～那么现在开始\x01",
            "是大家期待已久的问答时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xC,
        (
            "如果有问题\x01",
            "想问讲师，\x01",
            "就尽量举手吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #144
        0xC,
        "那么，后半段也请多指教了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_30CF")

    ChrTalk(    #145
        0x101,
        "#1006F嗯！　包在我身上。\x02",
    )

    CloseMessageWindow()
    Jump("loc_311B")

    label("loc_30CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_30FB")

    ChrTalk(    #146
        0x101,
        "#1002F嗯，我会尽力的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_311B")

    label("loc_30FB")


    ChrTalk(    #147
        0x101,
        "#1016F嗯、嗯，我会努力的。\x02",
    )

    CloseMessageWindow()

    label("loc_311B")

    OP_43(0xC, 0x1, 0x1, 0x9)
    Sleep(400)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #148
        0x101,
        (
            "#1018F好了，那么\x01",
            "问答时间开始啰～\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)
    Fade(1000)
    OP_6D(59000, 1000, 53470, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #149
        (
            "\x07\x05　问答时间开始！　\x01",
            "～平日的疑问随便问～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #150
        (
            "\x07\x05　※选择正确的回答\x01",
            "　　突破难题！　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_95(0x12, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #151
        0x12,
        "这里，这里～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_43(0x101, 0x1, 0x1, 0xF)
    OP_6D(61300, 1000, 53470, 1500)

    ChrTalk(    #152
        0x101,
        (
            "#1018F#5P哦，真有精神啊～\x02\x03",

            "是什么问题呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x12,
        "唔，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x12,
        (
            "游击士\x01",
            "要多大才能当呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1006F#5P年满几岁\x01",
            "才能当游击士吗？\x02\x03",

            "#1011F#5P嗯，要当游击士\x01",
            "首先得当上准游击士。\x02\x03",

            "考试合格就能当，\x01",
            "不过要接受那个考试……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #156
        "\x18游击士资格鉴定考试有年龄限制吗？\x02",
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①没有特别的年龄限制】\x01",      # 0
            "【②条件是１６岁以上】\x01",        # 1
            "【③条件是１８岁以上】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3442"),
        (1, "loc_34FA"),
        (2, "loc_35CD"),
        (SWITCH_DEFAULT, "loc_368C"),
    )


    label("loc_3442")


    ChrTalk(    #157
        0x101,
        "#1000F#5P……没有特别的年龄限制。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #158
        0x101,
        (
            "#1008F#5P但、但是，因为实力是必须的\x01",
            "所以一般都是１６岁以后\x01",
            "才开始接受考试哦。\x02\x03",

            "#1007F（哎哟哟……我在说什么呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368C")

    label("loc_34FA")


    ChrTalk(    #159
        0x101,
        (
            "#1006F#5P……条件是１６岁以上。\x02\x03",

            "但是，通过了考试\x01",
            "也不是马上就能当上的。\x02\x03",

            "需要暂时在游击士前辈的指导下\x01",
            "进行基础性的进修才行。\x02\x03",

            "在那里充分地提高了实力以后\x01",
            "才能成为准游击士哦。\x02\x03",

            "（顺利的回答！）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_368C")

    label("loc_35CD")


    ChrTalk(    #160
        0x101,
        "#1000F#5P……条件是１８岁以上。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #161
        0x101,
        (
            "#1008F#5P不、不过，有实力的话\x01",
            "或许也能更早地接受。\x02\x03",

            "嗯～大概１６岁左右\x01",
            "就可以了吧？\x02\x03",

            "#1013F（惨了～差点误人子弟了。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_368C")

    label("loc_368C")


    ChrTalk(    #162
        0x12,
        (
            "……唔～这样吗。\x01",
            "到１６岁就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x12,
        (
            "嗯，明白了。\x01",
            "谢谢老师。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 16)
    OP_6D(59000, 1000, 53470, 1500)
    OP_62(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #164
        0x11,
        (
            "这里，老师。\x01",
            "可以提问吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #165
        0x101,
        "#1000F#5P嗯，什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        (
            "魔兽是必须\x01",
            "打败不可的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        "明明也有很可爱的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1011F#5P啊，问得好。\x01",
            "对付魔兽可是很困难的哦。\x02\x03",

            "#1010F不过一般来说…………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #169
        "\x18应对魔兽的方法如何决定？\x02",
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①根据外观判断】\x01",          # 0
            "【②必然要打倒】\x01",            # 1
            "【③重视委托人的意向】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3873"),
        (1, "loc_3948"),
        (2, "loc_39E8"),
        (SWITCH_DEFAULT, "loc_3AB4"),
    )


    label("loc_3873")


    ChrTalk(    #170
        0x101,
        "#1010F#5P……要根据外观判断。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #171
        0x101,
        (
            "#1008F#5P不过，其中也有\x01",
            "虽然可爱但很不好对付的魔兽哦。\x02\x03",

            "因此过分依靠外观\x01",
            "判断也是不行的……\x02\x03",

            "总、总而言之\x01",
            "要见机行事。\x02\x03",

            "#1007F（乱、乱七八糟……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB4")

    label("loc_3948")


    ChrTalk(    #172
        0x101,
        (
            "#1002F#5P……必然要打倒。\x02\x03",

            "魔兽的危险性\x01",
            "与外观是没有关系的。\x02\x03",

            "#1015F但是，也有委托人\x01",
            "不希望打倒魔兽，\x01",
            "而是放生的情况哦。\x02\x03",

            "（唔～应该有\x01",
            "更好的答法……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB4")

    label("loc_39E8")


    ChrTalk(    #173
        0x101,
        (
            "#1000F#5P……要重视委托人的意向。\x02\x03",

            "应对魔兽的方法是没有标准答案的。\x01",
            "必须见机行事。\x02\x03",

            "所以，在委托人\x01",
            "不希望打倒魔兽的情况下，\x01",
            "也有可能会放生哦。\x02\x03",

            "#1006F（虽然是个难题\x01",
            "但看来回答得不错。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3AB4")

    label("loc_3AB4")


    ChrTalk(    #174
        0x11,
        "哦～原来如此啊～\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #175
        0x10,
        "我也可以提问吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#1000F#5P嗯，可以呀。\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0x11)
    OP_6D(57600, 1000, 53470, 1500)

    ChrTalk(    #177
        0x10,
        (
            "前阵子有发生空贼团\x01",
            "袭击定期船的事件吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10,
        (
            "那时逮捕空贼的\x01",
            "是王国军的士兵们？\x01",
            "还是游击士们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1011F#5P定期船『林德号』\x01",
            "被袭击的事件吗？\x02\x03",

            "#1015F那时最后\x01",
            "逮捕了空贼团的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #180
        "\x18逮捕了空贼团卡普亚一家的是？\x02",
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①当然是游击士】\x01",        # 0
            "【②是王国军的部队】\x01",      # 1
            "【③是亲卫队的队员】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C95"),
        (1, "loc_3D76"),
        (2, "loc_3E4A"),
        (SWITCH_DEFAULT, "loc_3F4B"),
    )


    label("loc_3C95")


    ChrTalk(    #181
        0x101,
        "#1012F#5P……当然是游击士。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #182
        0x101,
        (
            "#1008F#5P啊，不过突击作战\x01",
            "是和王国军配合进行的哦。\x02\x03",

            "……抱、抱歉\x01",
            "稍微有点记忆混乱。\x02\x03",

            "#1015F总、总之是游击士和王国军\x01",
            "齐心协力逮捕的哦。\x02\x03",

            "（呜～是哪一个来着……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4B")

    label("loc_3D76")


    ChrTalk(    #183
        0x101,
        (
            "#1000F#5P……是王国军的部队。\x02\x03",

            "最后的突击作战，\x01",
            "游击士和王国军形成\x01",
            "将空贼两面夹击之势。\x02\x03",

            "空贼逃跑时\x01",
            "王国军赶到将其逮捕。\x02\x03",

            "就是说，是游击士和王国军\x01",
            "齐心协力逮捕到的哦。\x02\x03",

            "#1006F（好，没问题吧。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F4B")

    label("loc_3E4A")


    ChrTalk(    #184
        0x101,
        "#1000F#5P……是亲卫队的队员。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x101,
        (
            "#1015F#5P咦，不过那个时候\x01",
            "亲卫队好像是不在的……\x02\x03",

            "#1013F……抱、抱歉\x01",
            "稍微有点记忆混乱。\x02\x03",

            "总、总之是游击士和王国军\x01",
            "齐心协力逮捕的哦。\x02\x03",

            "#1007F（亲卫队出现是在\x01",
            "逮捕戴尔蒙市长的时候吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4B")

    label("loc_3F4B")


    ChrTalk(    #186
        0x10,
        (
            "是吗，是王国军\x01",
            "与游击士合力抓到的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10,
        "嗯，这是最重要的。\x02",
    )

    CloseMessageWindow()
    Call(1, 16)
    ClearChrFlags(0x1B, 0x80)

    def lambda_3F9F():
        OP_8F(0x1B, 0xDC1E, 0x0, 0xAEBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3F9F)
    OP_6D(59000, 1000, 53470, 1500)

    ChrTalk(    #188
        0x1B,
        "#1P请问～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x1B,
        "#1P可以提问吗。\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0x12)
    OP_6D(57260, 1000, 50270, 1500)
    TurnDirection(0x101, 0x1B, 400)

    ChrTalk(    #190
        0x101,
        "#1000F好的，请说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1B,
        (
            "#1P我正在准备考试\x01",
            "不过忘记了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1B,
        (
            "#1P『对民间人士的保护义务』\x01",
            "是协会规章的第几项？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1004F（唔唔…………！？）\x02\x03",

            "（这、这怎么\x01",
            "可能背得下来嘛！）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(600)

    ChrTalk(    #194
        0x101,
        (
            "#1015F稍、稍等一下，\x01",
            "『对民间人士的保护义务』对吧？\x02\x03",

            "唔，嗯～那个大概……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #195
        "\x18『对民间人士的保护义务』是第几项？\x02",
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①协会规章第一项】\x01",      # 0
            "【②协会规章第二项】\x01",      # 1
            "【③协会规章第三项】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_421B"),
        (1, "loc_4343"),
        (2, "loc_43DF"),
        (SWITCH_DEFAULT, "loc_4509"),
    )


    label("loc_421B")


    ChrTalk(    #196
        0x101,
        "#1015F……协会规章第一项，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x1B,
        "#1P咦……是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x1B,
        "#1P第一项不是『基本理念』吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x101,
        "#1008F哎，咦……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x1B,
        (
            "#1P啊，不好意思。\x01",
            "我自己想起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x1B,
        "#1P『对民间人士的保护』是第二项吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1016F想、想起来就好了。\x02\x03",

            "#1007F（真、真没面子～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4509")

    label("loc_4343")


    ChrTalk(    #203
        0x101,
        "#1015F……协会规章第二项，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x1B,
        (
            "#1P啊，对了。\x01",
            "我现在也想起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x1B,
        "#1P谢谢您。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1016F哪里，不客气。\x02\x03",

            "（呼～总算撑过去了。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4509")

    label("loc_43DF")


    ChrTalk(    #207
        0x101,
        "#1000F……协会规章第三项，是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x1B,
        "#1P嗯……是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x1B,
        "#1P第三项不是『不干涉国家』吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #210
        0x101,
        "#1008F哎，咦……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x1B,
        (
            "#1P啊，不好意思。\x01",
            "我自己想起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x1B,
        "#1P『对民间人士的保护』是第二项吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#1016F想、想起来就好了。\x02\x03",

            "#1007F（真、真没面子～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4509")

    label("loc_4509")

    OP_43(0x101, 0x1, 0x1, 0x10)
    OP_6D(59000, 1000, 53470, 1500)

    def lambda_4527():
        OP_8F(0x1B, 0xDC1E, 0xFFFFFDA8, 0xAEBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4527)

    ChrTalk(    #214
        0x101,
        "#1000F……嗯……还有别的问题吗？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 0x1)
    SetChrFlags(0x1B, 0x80)

    ChrTalk(    #215
        0xF,
        "#2P那么，请问老师。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#1000F#5P嗯，什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xF,
        (
            "#2P那个，和今天的授课\x01",
            "虽然没多大关系……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xF,
        (
            "#2P逮捕市长的时候，\x01",
            "女王陛下的飞船来了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xF,
        (
            "#2P那艘飞船……\x01",
            "有多大？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #220
        0x101,
        (
            "#1019F#5P（来、来了……\x01",
            "完全不合时宜的问题。\x02\x03",

            "#1016F……嗯……女王陛下的飞船\x01",
            "是说埃尔赛尤号吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xF,
        "#2P嗯，就是那个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xF,
        (
            "#2P看起来好像非常大，\x01",
            "到底有多大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1015F#5P埃尔赛尤的大小啊……\x02\x03",

            "嗯～记得之前在什么书上\x01",
            "看到过似的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #224
        "\x18埃尔赛尤号的全长是？\x02",
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "【①全长２２亚矩】\x01",      # 0
            "【②全长３２亚矩】\x01",      # 1
            "【③全长４２亚矩】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47D6"),
        (1, "loc_4898"),
        (2, "loc_495A"),
        (SWITCH_DEFAULT, "loc_49D0"),
    )


    label("loc_47D6")


    ChrTalk(    #225
        0x101,
        "#1015F#5P……全长２２亚矩吧？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)

    ChrTalk(    #226
        0x101,
        (
            "#1007F#5P抱、抱歉……\x01",
            "说实话我也没什么自信。\x02\x03",

            "说不定搞错了，\x01",
            "大家还是查查书吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xF,
        "是吗～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xF,
        "那么，还是去看书吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49D0")

    label("loc_4898")


    ChrTalk(    #229
        0x101,
        "#1015F#5P……全长３２亚矩吧？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)

    ChrTalk(    #230
        0x101,
        (
            "#1007F#5P抱、抱歉……\x01",
            "说实话我也没什么自信。\x02\x03",

            "说不定搞错了，\x01",
            "大家还是查查书吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xF,
        "是吗～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xF,
        "那么，还是去看书吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49D0")

    label("loc_495A")


    ChrTalk(    #233
        0x101,
        (
            "#1015F#5P我记得……\x01",
            "全长是４２亚矩吧。\x02\x03",

            "不一定完全正确\x01",
            "不过大体上应该差不多吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xF,
        "咦～果然好大。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_49D0")

    label("loc_49D0")


    ChrTalk(    #235
        0xF,
        "谢谢～老师～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrPos(0xC, 61337, 1000, 50629, 180)
    OP_6D(58920, 1000, 50630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #236
        0xC,
        "──好了，没有问题了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xC,
        (
            "……好，那么到这里\x01",
            "老师的授课就结束啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xC,
        "好了，对老师说声谢谢吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xF,
        "#5P谢谢～老师～\x02",
    )


    ChrTalk(    #240
        0x11,
        "#2P谢谢～老师～\x02",
    )


    ChrTalk(    #241
        0x12,
        "#2P谢谢～老师～\x02",
    )


    ChrTalk(    #242
        0x10,
        "#1P谢谢～老师～\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #243
        0x101,
        "#1001F那么，再见喽～⊙\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B73")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B65")
    OP_2B(0x67, 0x2)
    OP_2C(0x67, 0x3E8)
    OP_28(0x67, 0x1, 0x2000)
    OP_28(0x67, 0x1, 0x4)
    Jump("loc_4B6B")

    label("loc_4B65")

    OP_28(0x67, 0x1, 0x8)

    label("loc_4B6B")

    OP_28(0x67, 0x4, 0x10)
    Jump("loc_4B89")

    label("loc_4B73")

    OP_28(0x67, 0x1, 0x4000)
    OP_28(0x67, 0x1, 0x10)
    OP_28(0x67, 0x4, 0x40)
    OP_28(0x67, 0x4, 0x80)

    label("loc_4B89")

    ClearMapFlags(0x400000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2100   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_1_869 end

    def Function_2_4B9B(): pass

    label("Function_2_4B9B")

    OP_6D(58920, 1000, 50630, 3000)
    Return()

    # Function_2_4B9B end

    def Function_3_4BAD(): pass

    label("Function_3_4BAD")

    OP_6B(2800, 4000)
    Return()

    # Function_3_4BAD end

    def Function_4_4BB7(): pass

    label("Function_4_4BB7")

    SetChrPos(0x1A, 57760, 0, 48830, 0)
    OP_69(0x1A, 0xFA0)
    Return()

    # Function_4_4BB7 end

    def Function_5_4BD0(): pass

    label("Function_5_4BD0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C8B")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4BF6"),
        (1, "loc_4BFE"),
        (2, "loc_4C06"),
        (3, "loc_4C0E"),
        (SWITCH_DEFAULT, "loc_4C16"),
    )


    label("loc_4BF6")

    Sleep(200)
    Jump("loc_4C16")

    label("loc_4BFE")

    Sleep(300)
    Jump("loc_4C16")

    label("loc_4C06")

    Sleep(400)
    Jump("loc_4C16")

    label("loc_4C0E")

    Sleep(500)
    Jump("loc_4C16")

    label("loc_4C16")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C39")
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    label("loc_4C39")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4C56"),
        (1, "loc_4C60"),
        (2, "loc_4C6A"),
        (3, "loc_4C74"),
        (SWITCH_DEFAULT, "loc_4C7E"),
    )


    label("loc_4C56")

    OP_8C(0xFE, 45, 400)
    Jump("loc_4C88")

    label("loc_4C60")

    OP_8C(0xFE, 90, 400)
    Jump("loc_4C88")

    label("loc_4C6A")

    OP_8C(0xFE, 315, 400)
    Jump("loc_4C88")

    label("loc_4C74")

    OP_8C(0xFE, 270, 400)
    Jump("loc_4C88")

    label("loc_4C7E")

    OP_8C(0xFE, 0, 400)
    Jump("loc_4C88")

    label("loc_4C88")

    Jump("Function_5_4BD0")

    label("loc_4C8B")

    Return()

    # Function_5_4BD0 end

    def Function_6_4C8C(): pass

    label("Function_6_4C8C")

    OP_8E(0xF7, 0xFFFFC1D0, 0x0, 0xAEEC, 0x3E8, 0x0)
    TurnDirection(0xF7, 0x101, 400)
    Return()

    # Function_6_4C8C end

    def Function_7_4CA8(): pass

    label("Function_7_4CA8")

    OP_8E(0xC, 0xF848, 0x0, 0xCB98, 0x7D0, 0x0)
    OP_8E(0xC, 0xF88E, 0x0, 0xC4AE, 0x7D0, 0x0)
    OP_8E(0xC, 0xFFDC, 0x0, 0xC4A4, 0x7D0, 0x0)
    OP_8C(0xC, 270, 400)
    Return()

    # Function_7_4CA8 end

    def Function_8_4CEC(): pass

    label("Function_8_4CEC")

    Sleep(800)
    OP_8E(0xD, 0xCF26, 0x0, 0xB446, 0x7D0, 0x0)
    OP_8C(0xD, 90, 400)
    Return()

    # Function_8_4CEC end

    def Function_9_4D0D(): pass

    label("Function_9_4D0D")

    OP_8E(0xC, 0xFFDC, 0x0, 0xC4A4, 0x7D0, 0x0)
    OP_8C(0xC, 270, 400)
    Return()

    # Function_9_4D0D end

    def Function_10_4D29(): pass

    label("Function_10_4D29")

    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x11, 0xF, 400)
    Sleep(400)
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0xF, 0x11, 400)
    Sleep(2000)
    OP_8C(0x11, 0, 400)
    OP_8C(0xF, 0, 400)
    Return()

    # Function_10_4D29 end

    def Function_11_4D83(): pass

    label("Function_11_4D83")

    OP_62(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Return()

    # Function_11_4D83 end

    def Function_12_4DEA(): pass

    label("Function_12_4DEA")

    Sleep(400)
    FadeToDark(600, 0, -1)
    OP_0D()
    Sleep(800)
    FadeToBright(600, 0)
    OP_0D()
    Return()

    # Function_12_4DEA end

    def Function_13_4E0A(): pass

    label("Function_13_4E0A")

    Sleep(400)
    FadeToDark(600, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    FadeToBright(600, 0)
    OP_0D()
    Return()

    # Function_13_4E0A end

    def Function_14_4E34(): pass

    label("Function_14_4E34")

    LoadEffect(0x0, "map\\\\mp032_00.eff")

    label("loc_4E48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EE5")
    Sleep(600)
    SetChrChipByIndex(0x19, 25)
    Sleep(600)

    label("loc_4E60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4ED3")
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x19, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED0")
    Jump("loc_4ED3")

    label("loc_4ED0")

    Jump("loc_4E60")

    label("loc_4ED3")

    Sleep(1000)
    SetChrChipByIndex(0x19, 22)
    Sleep(1000)
    Jump("loc_4E48")

    label("loc_4EE5")

    Return()

    # Function_14_4E34 end

    def Function_15_4EE6(): pass

    label("Function_15_4EE6")


    def lambda_4EEC():
        TurnDirection(0x10, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EEC)
    Sleep(100)

    def lambda_4EFF():
        TurnDirection(0x11, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4EFF)
    Sleep(50)

    def lambda_4F12():
        TurnDirection(0xF, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F12)
    Return()

    # Function_15_4EE6 end

    def Function_16_4F1B(): pass

    label("Function_16_4F1B")


    def lambda_4F21():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F21)
    Sleep(100)

    def lambda_4F34():
        OP_8C(0x11, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F34)

    def lambda_4F42():
        OP_8C(0x12, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F42)
    Sleep(50)

    def lambda_4F55():
        OP_8C(0xF, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F55)
    Return()

    # Function_16_4F1B end

    def Function_17_4F5E(): pass

    label("Function_17_4F5E")


    def lambda_4F64():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F64)
    Sleep(100)

    def lambda_4F77():
        TurnDirection(0x11, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F77)
    Sleep(50)

    def lambda_4F8A():
        TurnDirection(0xF, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F8A)
    Return()

    # Function_17_4F5E end

    def Function_18_4F93(): pass

    label("Function_18_4F93")


    def lambda_4F99():
        TurnDirection(0x12, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F99)
    Sleep(100)

    def lambda_4FAC():
        TurnDirection(0x11, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4FAC)
    Sleep(50)

    def lambda_4FBF():
        TurnDirection(0xF, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FBF)

    def lambda_4FCD():
        TurnDirection(0x10, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4FCD)
    Return()

    # Function_18_4F93 end

    SaveToFile()

Try(main)
