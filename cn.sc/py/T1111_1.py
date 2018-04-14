from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1111_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1111_1 ._SN',
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
        "Function_1_176",          # 01, 1
        "Function_2_6E1",          # 02, 2
        "Function_3_9CE",          # 03, 3
        "Function_4_A09",          # 04, 4
        "Function_5_B36",          # 05, 5
        "Function_6_2B06",         # 06, 6
        "Function_7_2B4D",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9")
    Return()

    label("loc_C9")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_104")
    Call(1, 1)
    Jump("loc_16F")

    label("loc_104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_113")
    Call(1, 2)
    Jump("loc_16F")

    label("loc_113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xB)"), scpexpr(EXPR_END)), "loc_122")
    Call(1, 3)
    Jump("loc_16F")

    label("loc_122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xC)"), scpexpr(EXPR_END)), "loc_131")
    Call(1, 4)
    Jump("loc_16F")

    label("loc_131")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_16F")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_176(): pass

    label("Function_1_176")

    EventBegin(0x0)
    Fade(1000)
    SetChrSubChip(0x8, 1)
    SetChrPos(0x101, -119000, 0, 68680, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6")
    SetChrPos(0xF8, -118380, 0, 69420, 270)
    SetChrPos(0xF7, -117250, 0, 68490, 270)
    SetChrPos(0xF9, -118000, 0, 67990, 270)
    Jump("loc_28F")

    label("loc_1D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219")
    SetChrPos(0xF7, -118380, 0, 69420, 270)
    SetChrPos(0xF8, -117250, 0, 68490, 270)
    SetChrPos(0xF9, -118000, 0, 67990, 270)
    Jump("loc_28F")

    label("loc_219")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    SetChrPos(0xF7, -118380, 0, 69420, 270)
    SetChrPos(0xF9, -117250, 0, 68490, 270)
    SetChrPos(0xF8, -118000, 0, 67990, 270)
    Jump("loc_28F")

    label("loc_25C")

    SetChrPos(0xF7, -118380, 0, 69420, 270)
    SetChrPos(0xF8, -117250, 0, 68490, 270)
    SetChrPos(0xF9, -118000, 0, 67990, 270)

    label("loc_28F")

    OP_6D(-119770, 0, 69530, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_436")

    ChrTalk(    #1
        0x8,
        (
            "#612F那么，各位……\x02\x03",

            "那张照片……\x01",
            "已经给莉拉看过了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_3DE")

    ChrTalk(    #2
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "给她看过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#612F那么……\x01",
            "她有说什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1015F不，她看起来虽然\x01",
            "感到很吃惊……\x02\x03",

            "但是，她也只是吃惊一下，\x01",
            "却什么都没说呢。\x02\x03",

            "#1002F看来果然是\x01",
            "在隐瞒着什么。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 5)
    Jump("loc_433")

    label("loc_3DE")


    ChrTalk(    #5
        0x101,
        "#1002F不，还没有。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#612F那就先把照片给\x01",
            "莉拉看吧。\x02\x03",

            "我想一定能\x01",
            "得到线索的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_433")

    Jump("loc_6D9")

    label("loc_436")

    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x8,
        (
            "#613F啊，这是……！？\x02\x03",

            "这张照片你们到底是从哪里得到的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1015F嗯，其实是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05艾丝蒂尔等人说明了\x01",
            "关于寻找科尔娜在『百日战役』中失踪的侄女的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #10
        0x8,
        (
            "#618F是吗……\x02\x03",

            "到了现在还有这样的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1002F你有什么印象吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#615F嗯……有点。\x02\x03",

            "#612F那个，这张照片……\x01",
            "已经给莉拉看过了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_672")

    ChrTalk(    #13
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "刚才给她看过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#612F那么……\x01",
            "她有说什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1015F不，她看起来虽然\x01",
            "相当吃惊……\x02\x03",

            "但是，她也只是吃惊一下，\x01",
            "什么都没说呢。\x02\x03",

            "#1002F看来果然是\x01",
            "在隐瞒着什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x10)
    Call(1, 5)
    Jump("loc_6D9")

    label("loc_672")


    ChrTalk(    #16
        0x101,
        (
            "#1011F莉拉小姐？\x02\x03",

            "#1000F不，还没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#612F那就先给她\x01",
            "看看吧。\x02\x03",

            "我想大概能\x01",
            "得到线索的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x4)

    label("loc_6D9")

    SetChrSubChip(0x8, 0)
    EventEnd(0x4)
    Return()

    # Function_1_176 end

    def Function_2_6E1(): pass

    label("Function_2_6E1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_72E")

    ChrTalk(    #18
        0x9,
        (
            "#620F现在我正在打扫，\x02\x03",

            "实在抱歉，\x01",
            "有事的话请等会再说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CA")

    label("loc_72E")

    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x9,
        (
            "#628F…………！？\x02\x03",

            "这张照片……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1015F嗯，其实是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05艾丝蒂尔等人说明了\x01",
            "关于寻找科尔娜在『百日战役』中失踪的侄女的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #22
        0x9,
        "#627F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1002F你有印象吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #24
        0x9,
        (
            "#624F不……\x01",
            "没什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1002F……真的？\x02\x03",

            "你好像看上去\x01",
            "很吃惊的样子……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_966")

    ChrTalk(    #26
        0x9,
        (
            "#620F嗯，和我的一个\x01",
            "熟人长得很像……\x02\x03",

            "所以我就\x01",
            "愣了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015F是，是吗……\x02\x03",

            "唔，真奇怪。\x02\x03",

            "梅贝尔市长明明说\x01",
            "问了莉拉小姐就会明白的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#620F啊，是吗……\x02\x03",

            "那好我先要\x01",
            "告辞了。\x02\x03",

            "因为还有工作\x01",
            "等着我去做。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C4")

    label("loc_966")


    ChrTalk(    #29
        0x9,
        (
            "#620F嗯，和我的一个\x01",
            "熟人长得很像……\x02\x03",

            "所以我就\x01",
            "愣了一下。\x02\x03",

            "那我就先告辞了。\x01",
            "我还有工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C4")

    OP_28(0x79, 0x1, 0x8)

    label("loc_9CA")

    TalkEnd(0x9)
    Return()

    # Function_2_6E1 end

    def Function_3_9CE(): pass

    label("Function_3_9CE")

    TalkBegin(0xB)

    ChrTalk(    #30
        0xB,
        "哇～好可爱的女孩子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        "和我小时候可能很像！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_3_9CE end

    def Function_4_A09(): pass

    label("Function_4_A09")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A66")

    ChrTalk(    #32
        0xC,
        (
            "因为我记得曾经在老爷的\x01",
            "书房见过这名少女的照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        (
            "到底是谁的\x01",
            "照片呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_A66")


    ChrTalk(    #34
        0xC,
        "哎呀，这张照片……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1004F你有印象吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #36
        0xC,
        (
            "虽然记\x01",
            "不太清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "因为我记得曾经在老爷的\x01",
            "书房见过这名少女的照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xC,
        (
            "到底是谁的\x01",
            "照片呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "不过看到的时候\x01",
            "我也觉得很不可思议。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_B32")

    TalkEnd(0xC)
    Return()

    # Function_4_A09 end

    def Function_5_B36(): pass

    label("Function_5_B36")

    SetChrSubChip(0x8, 0)

    ChrTalk(    #40
        0x8,
        (
            "#615F是吗……\x02\x03",

            "呼，看来还是要\x01",
            "从我嘴里说出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x101,
        (
            "#1011F那个，我还是\x01",
            "不大明白……\x02\x03",

            "……到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x3E8)
    Sleep(400)

    ChrTalk(    #42
        0x8,
        (
            "#618F那张照片上的少女……\x02\x03",

            "……正是莉拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x53)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x101,
        "#1004F咦咦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C57")

    ChrTalk(    #44
        0x105,
        "#044F啊……\x02",
    )

    CloseMessageWindow()

    label("loc_C57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7E")

    ChrTalk(    #45
        0x107,
        "#064F真、真的吗……\x02",
    )

    CloseMessageWindow()

    label("loc_C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC6")

    ChrTalk(    #46
        0x104,
        (
            "#033F这……\x02\x03",

            "怎么说……\x01",
            "真是个具有震撼性的新发现呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF1")

    ChrTalk(    #47
        0x108,
        "#073F这可真让人吃惊……\x02",
    )

    CloseMessageWindow()

    label("loc_CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D21")

    ChrTalk(    #48
        0x109,
        "#1064F啊，女神也会吓一跳吧。\x02",
    )

    CloseMessageWindow()

    label("loc_D21")


    ChrTalk(    #49
        0x101,
        (
            "#1004F那、那个……\x01",
            "你确定？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(    #50
        0x8,
        (
            "#612F嗯，我敢肯定。\x02\x03",

            "#615F莉拉是在十年前的\x01",
            "某一天来到我家的……\x02\x03",

            "正是柏斯被『百日战役』的\x01",
            "战火席卷的那一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1026F原、原来是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#618F从市民避难的地方回来的父亲\x01",
            "带来了一名少女。\x02\x03",

            "父亲说是受到了\x01",
            "陌生人的托付……\x02\x03",

            "……那个女孩子就是莉拉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(    #53
        0x103,
        (
            "#022F和科尔娜女士的证词有\x01",
            "很多相符的地方。\x02\x03",

            "我觉得这很可信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDA")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EEA")

    ChrTalk(    #54
        0x106,
        (
            "#050F和委托人的证词有\x01",
            "很多相符的地方。\x02\x03",

            "我觉得这很可信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDA")

    label("loc_EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3E")

    ChrTalk(    #55
        0x108,
        (
            "#074F和委托人的证词有\x01",
            "很多相符的地方。\x02\x03",

            "#072F我觉得这很可信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDA")

    label("loc_F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(    #56
        0x104,
        (
            "#030F和委托人的证词有\x01",
            "很多相符的地方。\x02\x03",

            "我觉得这很可信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDA")

    label("loc_F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDA")

    ChrTalk(    #57
        0x109,
        (
            "#1063F和委托人的证词有\x01",
            "很多相符的地方。\x02\x03",

            "我觉得这很可信。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDA")


    ChrTalk(    #58
        0x101,
        (
            "#1015F不过……\x01",
            "名字好像不一样。\x02\x03",

            "科尔娜女士的侄女\x01",
            "名字应该叫蕾妮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#613F蕾妮……？\x02\x03",

            "这就是莉拉原来的名字？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1002F嗯……\x01",
            "委托人是这么说的。\x02\x03",

            "莫非梅贝尔市长\x01",
            "也不知道莉拉小姐的本名？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#618F嗯，很遗憾……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(    #62
        0x106,
        (
            "#052F她本人没说过自己的原名吗？\x02\x03",

            "照片上的年龄还没小到\x01",
            "连名字也说不清的程度吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AD")

    label("loc_111B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1180")

    ChrTalk(    #63
        0x104,
        (
            "#033F她本人没说过自己的原名吗？\x02\x03",

            "照片上的年龄还没小到\x01",
            "连名字也说不清的程度吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AD")

    label("loc_1180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #64
        0x108,
        (
            "#073F她本人没说过自己的原名吗？\x02\x03",

            "照片上的年龄还没小到\x01",
            "连名字也说不清的程度吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AD")

    label("loc_11E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124A")

    ChrTalk(    #65
        0x103,
        (
            "#023F她本人没说过自己的原名吗？\x02\x03",

            "照片上的年龄还没小到\x01",
            "连名字也说不清的程度吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AD")

    label("loc_124A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(    #66
        0x109,
        (
            "#1064F她本人没说过自己的原名吗？\x02\x03",

            "照片上的年龄还没小到\x01",
            "连名字也说不清的程度吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AD")


    ChrTalk(    #67
        0x8,
        (
            "#618F嗯，她要是说出\x01",
            "自己的名字当然好……\x02\x03",

            "不过她来我家的时候\x01",
            "并不开口说话。\x02\x03",

            "怎么说好呢……\x02\x03",

            "……对，就好像是\x01",
            "忘了应该怎么说话一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1020F什、什么意思？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DB")

    ChrTalk(    #69
        0x109,
        (
            "#1067F大概是暂时性\x01",
            "失语症吧。\x02\x03",

            "是一种过度的精神负担\x01",
            "所引发的症状……\x02\x03",

            "对那么小的孩子来说，\x01",
            "那段时间真的是太残酷了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1647")

    label("loc_13DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147E")

    ChrTalk(    #70
        0x108,
        (
            "#072F可能是因为精神打击\x01",
            "而引发的暂时性失语症。\x02\x03",

            "好像过度残酷的经历\x01",
            "就会造成这种情况……\x02\x03",

            "真是的，这真是令人感叹啊。\x01",
            "她当初应该受了不少苦吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1647")

    label("loc_147E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(    #71
        0x104,
        (
            "#032F可能是因为精神打击\x01",
            "而引发的暂时性失语症。\x02\x03",

            "我听说过因为在战争中\x01",
            "经历了过于残酷的事而发病的病例。\x02\x03",

            "真可怜……\x01",
            "她当初应该受了不少苦吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1647")

    label("loc_151F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(    #72
        0x103,
        (
            "#522F可能是因为受打击\x01",
            "而引发的暂时性失语症。\x02\x03",

            "好像过度残酷的经历\x01",
            "就会造成这种情况……\x02\x03",

            "真可怜……\x01",
            "她当初应该受了不少苦吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1647")

    label("loc_15B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1647")

    ChrTalk(    #73
        0x106,
        (
            "#053F可能是因为受打击\x01",
            "而引发的暂时性失语症。\x02\x03",

            "好像过度残酷的经历\x01",
            "就会造成这种情况……\x02\x03",

            "#552F真是很可怜啊。\x01",
            "她当初应该受了不少苦吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1647")


    ChrTalk(    #74
        0x8,
        (
            "#615F嗯，她的内心一定\x01",
            "受过很深的伤吧。\x02\x03",

            "虽然大家都努力过，\x01",
            "不过她还是没打开自己的心扉……\x02\x03",

            "……所以，我们也\x01",
            "不知道莉拉的本名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1002F那、那么……\x01",
            "莉拉小姐现在的名字呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#612F是父亲给她起的。\x02\x03",

            "因为没有名字\x01",
            "是很不方便的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1787")

    ChrTalk(    #77
        0x103,
        (
            "#026F原来如此，明白了。\x02\x03",

            "那样的话，\x01",
            "接下来只有去问问她本人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_1787")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17DC")

    ChrTalk(    #78
        0x106,
        (
            "#053F原来如此，明白了。\x02\x03",

            "那样的话，\x01",
            "接下来只有去问问她本人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_17DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1831")

    ChrTalk(    #79
        0x108,
        (
            "#074F原来如此，明白了。\x02\x03",

            "那样的话，\x01",
            "接下来只有去问问她本人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_1831")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1886")

    ChrTalk(    #80
        0x104,
        (
            "#032F原来如此，明白了。\x02\x03",

            "那样的话，\x01",
            "接下来只有去问问她本人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_1886")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D2")

    ChrTalk(    #81
        0x105,
        (
            "#042F原来如此，明白了。\x02\x03",

            "这样的话，\x01",
            "只有去问问她本人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D2")


    ChrTalk(    #82
        0x8,
        (
            "#615F嗯，确实如此……\x02\x03",

            "#612F总之，我先去\x01",
            "把她叫来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -120720, 0, 66270, 135)
    SetChrPos(0x101, -121860, 0, 65600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198A")
    SetChrPos(0xF8, -121860, 0, 64500, 90)
    SetChrPos(0xF9, -122900, 0, 65080, 90)
    SetChrPos(0xF7, -122900, 0, 66180, 90)
    Jump("loc_1A43")

    label("loc_198A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CD")
    SetChrPos(0xF7, -121860, 0, 64500, 90)
    SetChrPos(0xF9, -122900, 0, 65080, 90)
    SetChrPos(0xF8, -122900, 0, 66180, 90)
    Jump("loc_1A43")

    label("loc_19CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A10")
    SetChrPos(0xF7, -121860, 0, 64500, 90)
    SetChrPos(0xF8, -122900, 0, 65080, 90)
    SetChrPos(0xF9, -122900, 0, 66180, 90)
    Jump("loc_1A43")

    label("loc_1A10")

    SetChrPos(0xF7, -121860, 0, 64500, 90)
    SetChrPos(0xF8, -122900, 0, 65080, 90)
    SetChrPos(0xF9, -122900, 0, 66180, 90)

    label("loc_1A43")

    OP_6D(-120720, 0, 66270, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x8, 255)
    OP_67(0, 4710, -10000, 0)
    OP_6B(3000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0xB, -118000, 0, 62730, 0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0x9, -118000, 0, 62730, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x40)
    OP_43(0xB, 0x0, 0x1, 0x7)
    OP_43(0x9, 0x0, 0x1, 0x6)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #83
        0xB,
        "我把她带来了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)

    ChrTalk(    #84
        0x8,
        (
            "#610F#5P谢谢你，萨拉。\x01",
            "麻烦你先出去下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        "是，失陪了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)
    OP_8E(0xB, 0xFFFE3310, 0x0, 0xFC12, 0x7D0, 0x0)

    def lambda_1B5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B5E)
    OP_8E(0xB, 0xFFFE3310, 0x0, 0xF50A, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x80)

    def lambda_1B89():

        label("loc_1B89")

        TurnDirection(0x8, 0x9, 0)
        OP_48()
        Jump("loc_1B89")

    QueueWorkItem2(0x8, 1, lambda_1B89)

    ChrTalk(    #86
        0x8,
        "#612F#5P你到这边来，莉拉。\x02",
    )

    CloseMessageWindow()

    def lambda_1BBA():
        OP_6D(-121200, 0, 66520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BBA)
    OP_8E(0x9, 0xFFFE2ED8, 0x0, 0x102DE, 0x7D0, 0x0)
    TurnDirection(0x9, 0x8, 400)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)

    ChrTalk(    #87
        0x9,
        "#620F您有什么吩咐吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#615F#5P那张照片……\x01",
            "我也看过了。\x02\x03",

            "好久没像这样\x01",
            "见到了一张令人怀念的脸。\x02\x03",

            "#612F莉拉……\x01",
            "那是你吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        "#620F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#612F#5P你沉默的理由\x01",
            "我很明白。\x02\x03",

            "你很在意我\x01",
            "父亲吧？\x02\x03",

            "我知道你念及\x01",
            "亡父的深厚恩情。\x02\x03",

            "#615F但是莉拉……\x02\x03",

            "我不希望这\x01",
            "成为你人生的重担。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "#624F重担吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#612F#5P嗯，你现在沉默不语\x01",
            "正说明了这一点。\x02\x03",

            "正是因为感到欠父亲的人情\x01",
            "你才会这么做的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        "#627F我、我没……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#615F#5P父亲以前经常说，\x02\x03",

            "只要还在为过去所束缚，\x01",
            "就决不可能开辟新的道路……\x02\x03",

            "#612F莉拉，你已经为我家\x01",
            "做了够多的事了。\x02\x03",

            "不必再一直\x01",
            "陷在过去的影子里。\x02\x03",

            "……你去见见科尔娜女士吧。\x02\x03",

            "去见她，去取回\x01",
            "属于你的人生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#620F…………………………\x02\x03",

            "小姐……\x01",
            "我明白您的意思。\x02\x03",

            "#621F可是很遗憾……\x02\x03",

            "各位所寻找的蕾妮\x01",
            "并不在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1026F#1P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "#613F#5P……什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#620F蕾妮在那场战争中\x01",
            "和父母一起丧失了生命。\x02\x03",

            "现在她正在大地的\x01",
            "某个角落安详地沉睡……\x02\x03",

            "……我相信着这一点，\x01",
            "一直活到了今天。\x02\x03",

            "#625F不这么想的话，\x01",
            "我就会感到很孤单……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        "#618F#5P莉拉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1026F#1P莉拉小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#618F#5P是吗……\x02\x03",

            "是这样的吗……\x02\x03",

            "没想到你是一直怀抱着\x01",
            "这样的心情走过来的……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #102
        0x101,
        (
            "#1010F#1P…………………………\x02\x03",

            "#1025F可是，莉拉小姐……\x02\x03",

            "那样的谎言\x01",
            "已经不需要了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        "#620F…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1000F#1P梅贝尔市长和萨拉小姐……\x02\x03",

            "管家门特斯先生和\x01",
            "超市里的人们……\x02\x03",

            "大家都把莉拉\x01",
            "当成是自己的亲人一样。\x02\x03",

            "现在的莉拉小姐\x01",
            "一点也不孤独。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #105
        0x8,
        "#613F#5P艾丝蒂尔小姐……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_219A")

    ChrTalk(    #106
        0x103,
        "#020F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_219A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21BD")

    ChrTalk(    #107
        0x107,
        "#060F嗯，没错。\x02",
    )

    CloseMessageWindow()

    label("loc_21BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EB")

    ChrTalk(    #108
        0x105,
        (
            "#047F我也……\x01",
            "觉得是这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221D")

    ChrTalk(    #109
        0x106,
        (
            "#051F啊啊……\x01",
            "这家伙说得没错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225C")

    ChrTalk(    #110
        0x109,
        (
            "#1060F人与人之间的羁绊\x01",
            "比你想象的更为紧密。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B2")

    ChrTalk(    #111
        0x108,
        (
            "#070F嗯，我也同意。\x02\x03",

            "就凭这次案件调查中\x01",
            "的亲身经历给我留下的印象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F6")

    ChrTalk(    #112
        0x104,
        (
            "#031F呵呵，是啊。\x02\x03",

            "至少我还是\x01",
            "深深爱着莉拉你的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F6")

    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #113
        0x8,
        (
            "#612F#5P莉拉……\x01",
            "你听见各位的话了吗？\x02\x03",

            "#615F对我来说，你是\x01",
            "家庭成员中的重要的一份子了……\x02\x03",

            "不，父亲去世之后\x01",
            "你已经是我唯一的亲人了。\x02\x03",

            "#618F可你还说自己孤独……\x02\x03",

            "以后请你不要再说\x01",
            "这么悲伤的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        "#627F小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#615F而且，莉拉……\x02\x03",

            "为了忘却痛苦的事情\x01",
            "而欺骗自己……\x02\x03",

            "把自己囚禁在过去中的行为…\x01",
            "这正是父亲所讨厌的。\x02\x03",

            "#612F请不要让父亲真心的教诲……\x01",
            "付之东流。\x02\x03",

            "莉拉……\x01",
            "去见见科尔娜女士吧。\x02\x03",

            "难道说……\x01",
            "你是那种无视恩人教诲的\x01",
            "不感恩之人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "#627F……………………………………\x02\x03",

            "#623F……明白了，我投降。\x02\x03",

            "唉，小姐你真是\x01",
            "伶牙俐齿…………\x02\x03",

            "被这么一说，\x01",
            "任何人都无法拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#610F呵呵，这种激将法\x01",
            "是谈判的基本功。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A5")

    ChrTalk(    #118
        0x108,
        (
            "#070F嗯，看来\x01",
            "已经有结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2669")

    label("loc_25A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D4")

    ChrTalk(    #119
        0x106,
        (
            "#051F看来\x01",
            "已经有结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2669")

    label("loc_25D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2609")

    ChrTalk(    #120
        0x103,
        (
            "#027F呵呵，看来\x01",
            "已经有结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2669")

    label("loc_2609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_263C")

    ChrTalk(    #121
        0x104,
        (
            "#031F嗯，看来\x01",
            "已经有结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2669")

    label("loc_263C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2669")

    ChrTalk(    #122
        0x109,
        (
            "#1060F看来已经\x01",
            "有结果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2669")


    ChrTalk(    #123
        0x101,
        (
            "#1007F呼，事情能圆满解决\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #124
        0x8,
        (
            "#617F嗯，总算……\x02\x03",

            "#611F那么，我们就\x01",
            "马上去见她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "#622F……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #126
        0x101,
        (
            "#1011F去见科尔娜女士……\x02\x03",

            "……梅贝尔市长你亲自去？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2783")

    ChrTalk(    #127
        0x106,
        (
            "#051F这倒没什么问题。\x02\x03",

            "以代表父亲的名义一同出席，\x01",
            "对方也应该会同意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_2783")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E0")

    ChrTalk(    #128
        0x103,
        (
            "#020F这倒没什么问题。\x02\x03",

            "以代表父亲的名义一同出席，\x01",
            "对方也应该会同意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_27E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_283F")

    ChrTalk(    #129
        0x108,
        (
            "#070F嗯，应该没问题的。\x02\x03",

            "以代表父亲的名义一同出席，\x01",
            "对方也应该会同意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_283F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A0")

    ChrTalk(    #130
        0x104,
        (
            "#030F嗯，应该没任何问题。\x02\x03",

            "以代表父亲的名义一同出席，\x01",
            "对方也应该会同意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_28A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FD")

    ChrTalk(    #131
        0x109,
        (
            "#1060F我觉得没什么问题。\x02\x03",

            "以代表父亲的名义一同出席，\x01",
            "对方也应该会同意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FD")


    ChrTalk(    #132
        0x8,
        "#611F呵呵，那就谢谢你们了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #133
        0x8,
        "#610F莉拉，我们走。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "#621F……是。\x02\x03",

            "那么我陪您去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "#617F真是的，你在说些什么啊。\x01",
            "是我陪你去。\x02\x03",

            "快点，你走在我前面。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFE2C30, 0x0, 0x102F2, 0x7D0, 0x0)
    OP_8C(0x9, 135, 400)

    def lambda_29C8():
        OP_8E(0x8, 0xFFFE2D3E, 0x0, 0x10284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29C8)

    def lambda_29E3():
        OP_8E(0x9, 0xFFFE30C2, 0x0, 0x100E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29E3)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x9, 0x0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #136
        0x9,
        "#623F可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#1001F哈哈，偶尔一次\x01",
            "也无妨吧。\x02\x03",

            "再说主角本来就是莉拉小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#611F呵呵，就是这样。\x02\x03",

            "好，快点去吧。\x01",
            "我等会儿会跟着你去的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #139
        0x9,
        "#626F小、小姐……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x79, 0x1, 0x20)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B36 end

    def Function_6_2B06(): pass

    label("Function_6_2B06")

    Sleep(1500)

    def lambda_2B11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B11)
    OP_8E(0xFE, 0xFFFE3310, 0x0, 0xFC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE319E, 0x0, 0xFE69, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_6_2B06 end

    def Function_7_2B4D(): pass

    label("Function_7_2B4D")


    def lambda_2B53():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B53)
    OP_8E(0xFE, 0xFFFE3310, 0x0, 0xFC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE2F82, 0x0, 0xFC12, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_7_2B4D end

    SaveToFile()

Try(main)
