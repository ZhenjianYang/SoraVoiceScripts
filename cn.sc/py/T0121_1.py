from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0121_1 ._SN',
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
        "Function_1_15B",          # 01, 1
        "Function_2_134A",         # 02, 2
        "Function_3_1397",         # 03, 3
        "Function_4_1724",         # 04, 4
        "Function_5_3000",         # 05, 5
        "Function_6_3030",         # 06, 6
        "Function_7_3060",         # 07, 7
        "Function_8_3090",         # 08, 8
        "Function_9_30C0",         # 09, 9
        "Function_10_3955",        # 0A, 10
        "Function_11_3986",        # 0B, 11
        "Function_12_39C0",        # 0C, 12
        "Function_13_39FA",        # 0D, 13
        "Function_14_3A34",        # 0E, 14
        "Function_15_3A6E",        # 0F, 15
        "Function_16_4992",        # 10, 16
        "Function_17_49EB",        # 11, 17
        "Function_18_4F25",        # 12, 18
        "Function_19_5032",        # 13, 19
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_2A(0xB7, 0xB8, 0xFFFF)
    Jump("loc_157")

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_DC")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0x74, 0x75, 0x76, 0x77, 0xAF, 0xB0, 0xFFFF)
    Jump("loc_157")

    label("loc_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_F7")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0x74, 0xAF, 0xB0, 0xFFFF)
    Jump("loc_157")

    label("loc_F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_10E")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0x74, 0xFFFF)
    Jump("loc_157")

    label("loc_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_123")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0xFFFF)
    Jump("loc_157")

    label("loc_123")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05没发出什么委托。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_157")

    TalkEnd(0xFF)
    Return()

    # Function_0_AA end

    def Function_1_15B(): pass

    label("Function_1_15B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 46210, 0, -1330, 90)
    SetChrPos(0x103, 45510, 0, -550, 90)
    SetChrPos(0xF8, 45070, 0, -1770, 90)
    SetChrPos(0xF9, 44550, 0, -830, 90)
    OP_8C(0xFE, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC")
    SetChrPos(0xF9, 45070, 0, -1770, 90)
    SetChrPos(0xF8, 44550, 0, -830, 90)

    label("loc_1DC")

    OP_6D(47260, 0, -210, 0)
    OP_67(0, 5030, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #1
        0x101,
        "#1011F#1P请问，能麻烦婆婆点事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "#2P什么事，艾丝蒂尔。\x01",
            "想让我做什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1015F#1P嗯，有点小事\x01",
            "想问您。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05诉说了在寻找拉欧老人\x01",
            "所说的炖煮料理食谱的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0xFE,
        (
            "#2P原来是关于\x01",
            "香辣炖煮的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "#2P以前，在这地方\x01",
            "是一道经常吃的传统菜哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3EC")

    label("loc_3AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D5")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3EC")

    label("loc_3D5")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_451")

    label("loc_413")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_451")

    label("loc_43A")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_451")

    Sleep(1000)

    ChrTalk(    #7
        0x101,
        "#1004F#1P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49B")

    ChrTalk(    #8
        0x107,
        "#064F婆婆也知道？？！\x02",
    )

    CloseMessageWindow()
    Jump("loc_510")

    label("loc_49B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C3")

    ChrTalk(    #9
        0x105,
        "#044F真的知道吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_510")

    label("loc_4C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EB")

    ChrTalk(    #10
        0x104,
        "#033F或许会知道？\x02",
    )

    CloseMessageWindow()
    Jump("loc_510")

    label("loc_4EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(    #11
        0x108,
        "#073F难道会知道？\x02",
    )

    CloseMessageWindow()

    label("loc_510")


    ChrTalk(    #12
        0xFE,
        "#2P当然知道啦～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "#2P那在以前可是家家都会做的\x01",
            "一道著名菜式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1011F#1P啊，德瑟鲁大叔他也\x01",
            "这么说过。\x02\x03",

            "#1001F嗯嗯，一定就是这个！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020F#1P找的就是这个食谱。\x02\x03",

            "能不能\x01",
            "教我怎么做？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "#2P啊啊，教吗？\x01",
            "当然是可以，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "#2P我所知道的食谱\x01",
            "大概与你要找的不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "#2P这一点\x01",
            "你们最好先了解清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1011F#1P咦，难道不同么……\x02\x03",

            "……不是一样的菜吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B3")

    ChrTalk(    #20
        0x106,
        "#555F这到底是怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_73A")

    label("loc_6B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E5")

    ChrTalk(    #21
        0x108,
        "#070F嗯，到底是怎么回事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_73A")

    label("loc_6E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70B")

    ChrTalk(    #22
        0x104,
        "#033F怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_73A")

    label("loc_70B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73A")

    ChrTalk(    #23
        0x105,
        "#044F那，那到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    label("loc_73A")


    ChrTalk(    #24
        0xFE,
        (
            "#2P我的食谱呢～\x01",
            "是我们家一代一代传下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "#2P因此，肯定和最原始的料理\x01",
            "味道也有所改变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "#2P如果你认为这没有什么关系，\x01",
            "我就教，如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1002F#1P也就是说……\x01",
            "经过了改良？\x02\x03",

            "#1003F嗯，虽然还是最想\x01",
            "要原始版，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#027F#1P还是先\x01",
            "请您教我们吧。\x02\x03",

            "总不能空手回去，\x01",
            "白来一趟。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AC")

    ChrTalk(    #29
        0x104,
        (
            "#030F雪拉说得没错。\x02\x03",

            "我们不能辜负了\x01",
            "老人的一番厚意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_990")

    label("loc_8AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F9")

    ChrTalk(    #30
        0x108,
        (
            "#070F哈哈，你说的没错。\x02\x03",

            "自然是不忍心\x01",
            "拒绝老人的好意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_990")

    label("loc_8F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946")

    ChrTalk(    #31
        0x105,
        (
            "#040F嗯嗯，是的是的。\x02\x03",

            "无视老人的好意\x01",
            "是件失礼的事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_990")

    label("loc_946")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_990")

    ChrTalk(    #32
        0x106,
        (
            "#051F雪拉扎德说得没错。\x02\x03",

            "一定要学的。\x01",
            "那就安静地听吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #33
        0x101,
        "#1006F#1P嗯……是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "……那就这么决定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "那就你们等我去拿\x01",
            "料理手册。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        "#020F#1P好，那就麻烦您了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xFE, 44800, 0, 2410, 0)
    OP_43(0xFE, 0x0, 0x1, 0x2)
    SetChrPos(0x101, 44360, 0, -280, 0)
    SetChrPos(0x103, 43020, 0, 160, 45)
    SetChrPos(0xF8, 45040, 0, -1020, 0)
    SetChrPos(0xF9, 46250, 0, -820, 315)
    OP_6D(45660, 0, 1500, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #37
        0x101,
        (
            "#1015F（…………………………）\x02\x03",

            "（找了好久，\x01",
            "  这么长时间……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#026F（不要那么着急。\x01",
            "  再稍微等等吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA3")

    ChrTalk(    #39
        0x106,
        (
            "#051F（就算是相当熟悉，\x01",
            "  毕竟是老婆婆，再等等的。）\x02\x03",

            "(找东西花费些时间\x01",
            "  也是没有办法的。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0A")

    ChrTalk(    #40
        0x108,
        (
            "#070F（虽说身体还比较健壮，\x01",
            "  不过年纪确实是大了。）\x02\x03",

            "(就请在这里耐心地等候吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(    #41
        0x104,
        (
            "#031F（虽说很熟悉，\x01",
            "  不过年纪大了是无法否认的事实。)\x02\x03",

            "（我们还是在这里耐心地\x01",
            "  等候吧。 ）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE0")

    ChrTalk(    #42
        0x105,
        (
            "#040F（虽说十分精神，\x01",
            "不过也已经是这个岁数了。)\x02\x03",

            "（还是在这里慢慢地\x01",
            "  等候吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE0")

    OP_4A(0xFE, 255)
    OP_8C(0xFE, 0, 400)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #43
        0xFE,
        "哎呀……那么说来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "……是的是的，应该没错了。\x01",
            "有些事情是无法用理论来解释的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0xAF00, 0x0, 0x96A, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #45
        0xFE,
        (
            "……让你们久等了，\x01",
            "不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "我是不是太慢了？\x01",
            "你们都着急了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1016F哪、哪里……\x01",
            "没有那回事啦。\x02\x03",

            "#1011F那……\x01",
            "找到食谱了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "哎呀，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "其实……很早以前\x01",
            "好像送给谁了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x101,
        "#1020F啊！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(    #51
        0x107,
        "#561F这，这……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F22")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC5")

    ChrTalk(    #52
        0x105,
        "#043F这下糟糕了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F22")

    label("loc_EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF7")

    ChrTalk(    #53
        0x106,
        "#055F喂喂……没有这样的吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F22")

    label("loc_EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F22")

    ChrTalk(    #54
        0x108,
        "#074F呼，真是败给您了。\x02",
    )

    CloseMessageWindow()

    label("loc_F22")


    ChrTalk(    #55
        0xFE,
        (
            "抱歉……\x01",
            "忽然想起来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "有个喜欢收集古书的人\x01",
            "无论如何也想要那本书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "我想也已经没有用了，\x01",
            "就很爽快地送给他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "咳，看来做人\x01",
            "也不能太慷慨呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1007F啊，您还叹什么气啊～\x01",
            "即使要叹，也是我们叹气。\x02\x03",

            "真是的，不知道是哪个家伙\x01",
            "给我们添的麻烦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #60
        0x103,
        (
            "#027F已经发生的事\x01",
            "多说也无济于事。\x02\x03",

            "接下来该怎样做……\x01",
            "才是我们现在应该考虑的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1088():
        TurnDirection(0xF8, 0x103, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1088)
    Sleep(150)
    TurnDirection(0xF9, 0x103, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10ED")

    ChrTalk(    #61
        0x105,
        (
            "#042F嗯，说得没错……\x02\x03",

            "只要能够找到拿着食谱的人\x01",
            "就行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DB")

    label("loc_10ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1138")

    ChrTalk(    #62
        0x104,
        (
            "#035F嗯，我也这么想的。\x02\x03",

            "首先要断定是谁\x01",
            "拿走了食谱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DB")

    label("loc_1138")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1193")

    ChrTalk(    #63
        0x108,
        (
            "#070F啊啊，是啊。\x02\x03",

            "如果能够找到拿到食谱的人，\x01",
            "一切都可以迎刃而解……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DB")

    label("loc_1193")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DB")

    ChrTalk(    #64
        0x106,
        (
            "#050F是，同感。\x02\x03",

            "只要找到拿到食谱的家伙\x01",
            "那就行了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DB")


    ChrTalk(    #65
        0x101,
        (
            "#1015F看来只好重整旗鼓，\x01",
            "继续调查了……\x02\x03",

            "婆婆说了，\x01",
            "是个有古书收集爱好的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#020F如果你感觉可能会是哪些人，\x01",
            "就从这些人身上开始调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "真是抱歉呢。\x01",
            "让你们这么期待。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1296():
        TurnDirection(0xF8, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1296)
    Sleep(150)

    def lambda_12A9():
        TurnDirection(0xF9, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_12A9)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #68
        0x101,
        (
            "#1006F嗯，没有关系的。\x02\x03",

            "总之还是得到了一些线索的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #69
        0x103,
        (
            "#020F嗯，谢谢您提供的帮助。\x02\x03",

            "那么，我们就继续\x01",
            "进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_28(0x75, 0x1, 0x200)
    EventEnd(0x0)
    OP_43(0x12, 0x0, 0x0, 0x2)
    Return()

    # Function_1_15B end

    def Function_2_134A(): pass

    label("Function_2_134A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1396")
    OP_8E(0xFE, 0xAF00, 0x0, 0x96A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xB306, 0x0, 0x96A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_2_134A")

    label("loc_1396")

    Return()

    # Function_2_134A end

    def Function_3_1397(): pass

    label("Function_3_1397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152F")
    EventBegin(0x1)
    OP_6D(13410, 0, 139810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05※进行队伍的重新编组。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #71
        (
            "\x07\x05请选择２名固定成员\x01",
            "以外的同行者。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14B7")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_14B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14DA")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_14DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14FD")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_14FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_152A")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_152A")

    Sleep(300)

    label("loc_152F")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, 1200, 0, 116170, 0)
    SetChrPos(0xF7, 370, 0, 115520, 0)
    SetChrPos(0xF8, 1850, 0, 114800, 0)
    SetChrPos(0xF9, 910, 0, 114140, 0)
    OP_6D(750, 0, 117600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #72
        0x8,
        (
            "#741F#2P好久没有像今天一样痛快地喝上一杯了。\x02\x03",

            "事情的原由先不提了，\x01",
            "还是要对你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1016F#4P这、这、这样虽好……\x02\x03",

            "#1015F对了，奥利维尔那家伙\x01",
            "后来怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#740F#2P嗯，教区长对他进行\x01",
            "了治疗。\x01",
            "现在正在协会的２楼休息着呢。\x02\x03",

            "好像有点筋疲力尽的样子，不过\x01",
            "据说身体已经没有大碍了。\x01",
            "不要有什么顾虑，带走他就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_3_1397 end

    def Function_4_1724(): pass

    label("Function_4_1724")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_173B")
    Call(0, 42)
    Call(1, 16)

    label("loc_173B")

    OP_4A(0x8, 255)
    SetChrFlags(0x11, 0x80)
    OP_6D(340, 0, 118500, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(292, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #75
        0x8,
        "#743F#2P哎呀……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x101, 3810, 0, 110590, 315)
    SetChrPos(0x102, 3810, 0, 110590, 315)
    SetChrPos(0xF8, 3810, 0, 110590, 315)
    SetChrPos(0xF9, 3810, 0, 110590, 315)

    def lambda_1811():
        OP_6D(90, 0, 117790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1811)

    def lambda_1829():
        OP_67(0, 6910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1829)

    def lambda_1841():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1841)

    def lambda_1851():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1851)
    OP_43(0x101, 0x1, 0x1, 0x5)
    Sleep(400)
    OP_43(0x102, 0x1, 0x1, 0x6)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x1, 0x7)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x1, 0x8)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A6D")

    ChrTalk(    #76
        0x103,
        "#021F#6P嗨，爱娜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1006F#6P我们来了呀，爱娜姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        "#1035F#6P……好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#743F#2P雪拉扎德……\x01",
            "啊，还有艾丝蒂尔，约修亚！\x02\x03",

            "#741F真好……看来是平安无事。\x02\x03",

            "你们去『塔』的时候\x01",
            "发生了突变，我很担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#025F#6P的确是十分危险的地方，\x01",
            "不过总算是安然无恙了。\x02\x03",

            "#524F你这边\x01",
            "才真得很严重吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#745F#2P是的……\x01",
            "确实是发生了些骚乱，不过\x01",
            "还好没有导致什么严重的后果。\x02\x03",

            "#740F克劳斯市长和迪拜恩教区长\x01",
            "控制了混乱的局面，功劳不小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1025F#6P是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1A6D")


    ChrTalk(    #83
        0x101,
        "#1006F#6P让你担心了，爱娜姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        "#1035F#6P……好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#741F#2P太好了……你们平安无事。\x02\x03",

            "#740F你们去『塔』的时候\x01",
            "发生了异变，我很担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1016F嗯，确实十分危险。\x01",
            "不过总算是安然无恙了。\x02\x03",

            "#1025F你这边\x01",
            "才真的很严重吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#745F#2P是的……\x01",
            "确实是发生了些骚乱，不过\x01",
            "还好没有导致什么严重的后果。\x02\x03",

            "#740F克劳斯市长和迪拜恩教区长\x01",
            "控制了混乱的局面，功劳不小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1025F是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_1BF5")


    ChrTalk(    #89
        0x8,
        (
            "#740F#2P不管怎样，约修亚。\x02\x03",

            "#741F你平安回来就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#1035F#6P是……\x02\x03",

            "#1043F让大家替我担心。\x01",
            "对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#744F#2P哈哈，没什么。\x02\x03",

            "#740F对于我们协会的接待员来说，\x01",
            "某种意义上，游击士就像孩子一样。\x02\x03",

            "更不用说你们的游击士手册\x01",
            "可是我亲手交给你们的。\x02\x03",

            "#741F能够平安回来，真是太好啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        "#1040F#6P爱娜小姐……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D85")

    ChrTalk(    #93
        0x103,
        "#027F#6P呵呵……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #94
        0x101,
        (
            "#1008F#4P哈哈哈……\x01",
            "真好啊，约修亚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB6")

    label("loc_1D85")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #95
        0x101,
        (
            "#1008F#4P哈哈哈……\x01",
            "真好啊，约修亚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB6")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #96
        0x101,
        (
            "#1004F#6P对了，爱娜姐。\x02\x03",

            "#1002F其实有很多很多的话\x01",
            "想和你说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#744F#2P嗯……关于那浮游岛吧。\x02\x03",

            "#742F如果知道什么详情\x01",
            "能告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        "#1042F#6P是，情况是这样的──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #99
        (
            "\x07\x05艾丝蒂尔等人向爱娜说明了\x01",
            "『浮游都市』出现了的缘由以及\x01",
            "关于『零力场发生器』的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #100
        0x8,
        (
            "#744F#2P是吗……那就是『辉之环』。\x02\x03",

            "与想象中的情形\x01",
            "有相当大的差异……\x02\x03",

            "#742F但是不管怎么说，目前我们\x01",
            "还是没有能力和对方抗衡。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE9")

    ChrTalk(    #101
        0x103,
        (
            "#025F#6P嗯……虽然这件事令人十分懊丧。\x02\x03",

            "#022F但看来首先必须先重新调整我们的状态。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C2")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2052")

    ChrTalk(    #102
        0x106,
        (
            "#053F#6P啊啊……\x01",
            "真是让人生气的事情。\x02\x03",

            "#555F但首先还是必须先重新调整好我们的状态。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C2")

    label("loc_2052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C2")

    ChrTalk(    #103
        0x108,
        (
            "#074F#6P啊啊……\x01",
            "虽然很着急，但是是没有办法的事情。\x02\x03",

            "#070F自然是只有先调整好我们的状态才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2152")

    ChrTalk(    #104
        0x8,
        (
            "#744F嗯，也就是说，如果可以能使用通讯器\x01",
            "那肯定对我们有所帮助。\x02\x03",

            "#740F那就赶快将『零力场发生器』\x01",
            "设置好，如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AA")

    label("loc_2152")


    ChrTalk(    #105
        0x8,
        (
            "#744F嗯，也就是说，如果可以使用通讯器，\x01",
            "那就好了。\x02\x03",

            "#740F尽快将此装置\x01",
            "设置好如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B5")

    ChrTalk(    #106
        0x107,
        (
            "#560F#6P是！\x01",
            "请稍等。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 17)
    SetChrPos(0x107, -560, 0, 119000, 0)
    TurnDirection(0x8, 0x107, 0)
    OP_6D(-810, 0, 119530, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(314000, 0)
    OP_6E(309, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #107
        0x107,
        "#061F#5P……嗯，ＯＫ了吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #108
        "\x07\x05提妲打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_23B8")

    label("loc_22B5")


    ChrTalk(    #109
        0x102,
        "#1040F#6P啊啊，那么开始……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 17)
    SetChrPos(0x102, -560, 0, 119000, 0)
    TurnDirection(0x8, 0x102, 0)
    OP_6D(-810, 0, 119530, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(314000, 0)
    OP_6E(309, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #110
        0x102,
        "#1035F#5P……这下应该好了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #111
        "\x07\x05约修亚打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_23B8")

    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #112
        0x8,
        "#743F启动了……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B5")
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #113
        0x107,
        (
            "#560F#5P这下，通讯器\x01",
            "应该能够使用了。\x02\x03",

            "不过，如果对方的通讯器没修好\x01",
            "还是不能发送的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251D")

    label("loc_24B5")

    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #114
        0x102,
        (
            "#1040F#5P这下，通讯器\x01",
            "能够使用了。\x02\x03",

            "但这必须是在对方的通讯器\x01",
            "也已经修好，可以使用的前提下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251D")


    ChrTalk(    #115
        0x8,
        "#744F这下可真帮了大忙了……\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_2549():
        OP_6D(-150, 0, 118340, 1100)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2549)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #116
        0x8,
        (
            "#740F#2P感谢大家。\x01",
            "这份人情一定会还的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AC")
    OP_8C(0x107, 135, 400)
    Jump("loc_25B3")

    label("loc_25AC")

    OP_8C(0x102, 135, 400)

    label("loc_25B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2639")

    ChrTalk(    #117
        0x103,
        (
            "#021F#6P嗯，那就下次\x01",
            "请大家吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        "#741F#2P嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1052F这两个人还是老样子，一点都没有改变……\x02",
    )

    CloseMessageWindow()
    Jump("loc_269E")

    label("loc_2639")


    ChrTalk(    #120
        0x101,
        (
            "#1016F#6P好了，爱娜姐\x01",
            "就别再说那些见外的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#1040F这也是和我们的工作\x01",
            "息息相关的事情哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇恢复全部的通讯器】\x01",        # 0
            "【◇只恢复这里的通讯器】\x01",      # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_272A"),
        (1, "loc_2733"),
        (SWITCH_DEFAULT, "loc_273C"),
    )


    label("loc_272A")

    OP_A2(0x2001)
    OP_A2(0x2005)
    Jump("loc_273C")

    label("loc_2733")

    OP_A3(0x2001)
    OP_A3(0x2005)
    Jump("loc_273C")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27BB")

    ChrTalk(    #122
        0x108,
        (
            "#070F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，配合各地的状况\x01",
            "进行执行任务的报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A6")

    label("loc_27BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2833")

    ChrTalk(    #123
        0x103,
        (
            "#020F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，结合各地的状况\x01",
            "一起进行一下任务的报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A6")

    label("loc_2833")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A6")

    ChrTalk(    #124
        0x106,
        (
            "#051F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，结合各地的状况，\x01",
            "开始进行任务的汇报吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A6")

    OP_59()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_290C")

    ChrTalk(    #125
        0x8,
        (
            "#741F#2P真是辛苦了。\x02\x03",

            "这下子，就可以\x01",
            "迅速应对了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294C")

    label("loc_290C")


    ChrTalk(    #126
        0x8,
        (
            "#741F#2P大伙们，\x01",
            "真的辛苦了。\x02\x03",

            "这下子，就可以\x01",
            "迅速应对了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2982")

    ChrTalk(    #127
        0x108,
        "#070F还有其它什么事要帮忙的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29E9")

    label("loc_2982")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BC")

    ChrTalk(    #128
        0x103,
        "#020F是否还有其它什么事要帮忙的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29E9")

    label("loc_29BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E9")

    ChrTalk(    #129
        0x106,
        "#051F还有什么要帮忙的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_29E9")

    Jump("loc_2B5E")

    label("loc_29EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A67")

    ChrTalk(    #130
        0x108,
        (
            "#070F#6P嗯，准备照这个样子，\x01",
            "把其他几个协会的通讯器也\x01",
            "给修理好……\x02\x03",

            "不过，这里还有其他事情要帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5E")

    label("loc_2A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AE6")

    ChrTalk(    #131
        0x106,
        (
            "#051F#6P嗯，准备照这个样子，\x01",
            "把其他几个协会的通讯器也\x01",
            "给修理好……\x02\x03",

            "不过，这里没有其他要帮忙的事情了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5E")

    label("loc_2AE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B5E")

    ChrTalk(    #132
        0x103,
        (
            "#020F#6P嗯，准备照这个样子，\x01",
            "把其他几个协会的通讯器也\x01",
            "给修理好……\x02\x03",

            "不过，这里还有什么需要帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C1E")

    ChrTalk(    #133
        0x8,
        (
            "#744F#2P这样啊……\x02\x03",

            "#740F可以的话，就去\x01",
            "查看一下留言板上的工作吧。\x02\x03",

            "另外，希望你们去确认\x01",
            "一下洛连特的近郊是否\x01",
            "有什么情况。\x02\x03",

            "特别是利吉去的\x01",
            "玛鲁加矿山，我总是放心不下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCD")

    label("loc_2C1E")


    ChrTalk(    #134
        0x8,
        (
            "#744F#2P这样啊……\x02\x03",

            "#740F可以的话，就去\x01",
            "查看一下留言板上的工作吧。\x02\x03",

            "另外，希望你们去确认\x01",
            "一下洛连特的近郊是否\x01",
            "有什么情况。\x02\x03",

            "特别是利吉去的\x01",
            "玛鲁加矿山，我总是放心不下……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCD")


    ChrTalk(    #135
        0x101,
        "#1004F#6P啊？矿山出了什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#740F#2P不，只是警备的工作而已。\x02\x03",

            "还记得吧？在以前的塌方事故时，\x01",
            "部分坑道与魔兽的巢穴是相连的。\x02\x03",

            "就在数日前，当正要进行\x01",
            "正式的封锁工程的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#1043F#5P就是在那时候\x01",
            "发生的那起非常事件吧……\x02\x03",

            "……确实很令人在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#740F#2P嗯，如果有时间的话\x01",
            "无论如何一定去观察一下情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1006F#6P嗯，知道了。\x02\x03",

            "缇欧的家啦，矿山啦，\x01",
            "觉得有人去的地方都会试着去看一下的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #140
        0x102,
        (
            "#1040F#5P是啊……\x01",
            "总之，小心行事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        "#741F#2P那就拜托啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #142
        (
            "\x07\x05※因为通讯器已经修好了，可以呼叫在其他支部待命的同伴，\x01",
            "  将他们召集来洛连特支部。\x01",
            "　想呼叫的时候请在接待处选择『呼叫同伴』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_4B(0x8, 255)
    OP_A2(0x2003)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F5F")
    OP_A2(0x2091)
    Jump("loc_2F62")

    label("loc_2F5F")

    OP_A3(0x2091)

    label("loc_2F62")

    OP_28(0x9B, 0x2, 0x40)
    OP_28(0x9B, 0x1, 0x80)
    OP_6D(520, 0, 114520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 520, 0, 114520, 135)
    SetChrPos(0x1, 520, 0, 114520, 135)
    SetChrPos(0x2, 520, 0, 114520, 135)
    SetChrPos(0x3, 520, 0, 114520, 135)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_1724 end

    def Function_5_3000(): pass

    label("Function_5_3000")

    OP_8E(0xFE, 0x942, 0x0, 0x1B7D8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x1C6D8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_3000 end

    def Function_6_3030(): pass

    label("Function_6_3030")

    OP_8E(0xFE, 0x500, 0x0, 0x1B80A, 0x9C4, 0x0)
    OP_8E(0xFE, 0x190, 0x0, 0x1C6D8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_3030 end

    def Function_7_3060(): pass

    label("Function_7_3060")

    OP_8E(0xFE, 0x942, 0x0, 0x1B7D8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x1C264, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_3060 end

    def Function_8_3090(): pass

    label("Function_8_3090")

    OP_8E(0xFE, 0x500, 0x0, 0x1B80A, 0x9C4, 0x0)
    OP_8E(0xFE, 0x190, 0x0, 0x1C264, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_3090 end

    def Function_9_30C0(): pass

    label("Function_9_30C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30DA")
    Return()

    label("loc_30DA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30FA")
    Call(0, 42)
    Call(1, 16)
    FadeToBright(0, 0)

    label("loc_30FA")

    OP_22(0xC3, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)

    ChrTalk(    #143
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_3178():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3178)

    def lambda_3186():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3186)
    Sleep(100)

    def lambda_3199():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3199)
    OP_8C(0x3, 0, 400)

    ChrTalk(    #144
        0x8,
        (
            "#743F#6P啊，刚修好\x01",
            "就有联络来了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-1130, 0, 119950, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    SetChrPos(0x101, 3810, 0, 110590, 0)
    SetChrPos(0x102, 3810, 0, 110590, 0)
    SetChrPos(0xF8, 3810, 0, 110590, 0)
    SetChrPos(0xF9, 3810, 0, 110590, 0)
    OP_8C(0x8, 315, 0)
    OP_8E(0x8, 0xFFFFFDD0, 0x0, 0x1D0D8, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(700)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_43(0x101, 0x0, 0x1, 0xA)
    Sleep(500)

    ChrTalk(    #145
        0x8,
        (
            "#742F#6P这里是游击士协会，\x01",
            "这里是洛连特支部……\x02\x03",

            "#743F……啊啊！\x01",
            "那边也是修好了。\x02\x03",

            "#741F嗯，这边也是\x01",
            "刚刚才弄好的。\x02\x03",

            "#740F……她们吗？\x01",
            "嗯，现在就在这里呢……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)

    def lambda_3382():
        OP_6D(-730, 0, 118880, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3382)

    def lambda_339A():
        OP_67(0, 5820, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_339A)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #146
        0x101,
        "#1004F#6P（找我们的……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        "#1044F#6P（好像有话要说。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#744F#6P……是……是的。\x02\x03",

            "………………………………………\x02\x03",

            "#740F……知道了。\x01",
            "我会向他们本人转达的。\x02\x03",

            "关于这边的状况\x01",
            "过一会儿再和你联络。  \x02\x03",

            "#741F……是呀。\x01",
            "大家一起加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34EC")

    ChrTalk(    #149
        0x103,
        (
            "#023F#6P爱娜。\x01",
            "是哪里来的联络？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3514")

    label("loc_34EC")


    ChrTalk(    #150
        0x101,
        (
            "#1015F#6P爱娜姐。\x01",
            "是哪里来的联络？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3514")

    OP_8E(0x8, 0x2EE, 0x0, 0x1CF48, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #151
        0x8,
        (
            "#740F#2P是王都支部的艾南先生。\x02\x03",

            "艾莉茜雅女王陛下\x01",
            "好像有话要对你们说。\x02\x03",

            "如果去格兰赛尔附近的话，\x01",
            "希望能顺便去王城一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1004F#6P女王陛下！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_360A")

    ChrTalk(    #153
        0x106,
        (
            "#052F#6P真是让人吃惊啊……\x01",
            "到底有什么事呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3691")

    label("loc_360A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3650")

    ChrTalk(    #154
        0x108,
        (
            "#073F#6P那真是让人吃惊啊。\x01",
            "究竟有什么事情呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3691")

    label("loc_3650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3691")

    ChrTalk(    #155
        0x103,
        (
            "#023F#6P这真让人惊讶……\x01",
            "究竟有什么事情呢～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36F9")

    ChrTalk(    #156
        0x8,
        (
            "#744F#2P这就没有详细问了……\x02\x03",

            "#742F好像是不大适合在\x01",
            "通讯器中传达的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3753")

    label("loc_36F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3753")

    ChrTalk(    #157
        0x8,
        (
            "#744F#2P具体就没有细问了……\x02\x03",

            "#742F好像是不大适合在\x01",
            "通讯器中传达的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3753")


    ChrTalk(    #158
        0x101,
        (
            "#1015F#6P不能在通讯中传达……\x02\x03",

            "#1026F是吗，导力通讯\x01",
            "存在被人监听的危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x102,
        (
            "#1042F#6P看来是\x01",
            "比较机密的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#740F#2P不过，也没有让\x01",
            "你们马上就去的意思。\x02\x03",

            "要是以后路过王都附近的话，\x01",
            "就顺便去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1006F#6P这样的啊……知道了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3879")

    ChrTalk(    #162
        0x103,
        "#021F#6P赶快过去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3898")

    label("loc_3879")


    ChrTalk(    #163
        0x102,
        "#1040F#6P赶快过去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3898")

    OP_A2(0x2004)
    OP_28(0x9B, 0x1, 0x100)
    OP_28(0x9B, 0x1, 0x200)
    OP_28(0x9B, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_6D(520, 0, 114520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 520, 0, 114520, 135)
    SetChrPos(0x1, 520, 0, 114520, 135)
    SetChrPos(0x2, 520, 0, 114520, 135)
    SetChrPos(0x3, 520, 0, 114520, 135)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_30C0 end

    def Function_10_3955(): pass

    label("Function_10_3955")

    OP_43(0x101, 0x1, 0x1, 0x5)
    Sleep(400)
    OP_43(0x102, 0x1, 0x1, 0x6)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x1, 0x7)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x1, 0x8)
    WaitChrThread(0xF8, 0x1)
    Return()

    # Function_10_3955 end

    def Function_11_3986(): pass

    label("Function_11_3986")

    OP_8E(0xFE, 0x2E4, 0x0, 0x1B95E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1B8, 0x0, 0x1C76E, 0x7D0, 0x0)

    def lambda_39B4():

        label("loc_39B4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_39B4")

    QueueWorkItem2(0xFE, 2, lambda_39B4)
    Return()

    # Function_11_3986 end

    def Function_12_39C0(): pass

    label("Function_12_39C0")

    OP_8E(0xFE, 0x802, 0x0, 0x1B94A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x492, 0x0, 0x1C778, 0x7D0, 0x0)

    def lambda_39EE():

        label("loc_39EE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_39EE")

    QueueWorkItem2(0xFE, 2, lambda_39EE)
    Return()

    # Function_12_39C0 end

    def Function_13_39FA(): pass

    label("Function_13_39FA")

    OP_8E(0xFE, 0x2E4, 0x0, 0x1B95E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF24, 0x0, 0x1C570, 0x7D0, 0x0)

    def lambda_3A28():

        label("loc_3A28")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A28")

    QueueWorkItem2(0xFE, 2, lambda_3A28)
    Return()

    # Function_13_39FA end

    def Function_14_3A34(): pass

    label("Function_14_3A34")

    OP_8E(0xFE, 0x802, 0x0, 0x1B94A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x78A, 0x0, 0x1C6B0, 0x7D0, 0x0)

    def lambda_3A62():

        label("loc_3A62")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A62")

    QueueWorkItem2(0xFE, 2, lambda_3A62)
    Return()

    # Function_14_3A34 end

    def Function_15_3A6E(): pass

    label("Function_15_3A6E")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(-1470, 0, 125030, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 300, 0, 116600, 135)
    SetChrPos(0x101, 1840, 0, 115000, 0)
    SetChrPos(0x102, 710, 0, 115000, 0)
    SetChrPos(0xF8, 1840, 0, 113800, 0)
    SetChrPos(0xF9, 740, 0, 113800, 0)
    Sleep(1000)

    def lambda_3B20():
        OP_6D(250, 0, 116610, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B20)

    def lambda_3B38():
        OP_67(0, 6910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B38)

    def lambda_3B50():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3B50)

    def lambda_3B60():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3B60)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x3)
    Sleep(400)

    ChrTalk(    #164
        0x8,
        (
            "#745F──原来如此，事情是那样吗。\x02\x03",

            "要是再迟一步的话，\x01",
            "结果真是不堪设想啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x15,
        (
            "#1P啊啊，多亏这位小姐和她的朋友\x01",
            "我们才能得救。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x15,
        (
            "#1P上次被你搭救的时候\x01",
            "还觉得提心吊胆的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x15,
        (
            "#1P但今天感觉却完全不同，\x01",
            "简直像换了个人一样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #168
        0x101,
        (
            "#1008F#4P哎呀？真的吗？\x02\x03",

            "可、可是我倒没觉得\x01",
            "自己有什么变化啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x15,
        "#1P不用谦虚啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x15,
        (
            "#1P这可是我的\x01",
            "真心感想。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #171
        0x102,
        (
            "#1048F#1P谦虚吗……\x02\x03",

            "#1035F如果是艾丝蒂尔的话，\x01",
            "大概是真的没发觉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D65")

    ChrTalk(    #172
        0x107,
        "#560F嘿嘿嘿，也说不定哦。\x02",
    )

    CloseMessageWindow()

    label("loc_3D65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D8E")

    ChrTalk(    #173
        0x103,
        "#021F呵呵，有可能呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC8")

    ChrTalk(    #174
        0x106,
        (
            "#051F错不了，\x01",
            "这家伙本来就是少根筋嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC8")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_8C(0x101, 180, 400)
    Sleep(600)

    ChrTalk(    #175
        0x101,
        (
            "#1019F#4P呜……\x02\x03",

            "明明是在被赞扬，\x01",
            "但为什么一点都高兴不起来呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#741F不管是谁，想要发觉\x01",
            "自己的变化也是很难的。\x02\x03",

            "因为毕竟是一点一点\x01",
            "逐渐变化的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x15,
        (
            "#1P嗯，我是因为好久没有见到你们，\x01",
            "所以感觉才会这样强烈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x15,
        (
            "#1P不管怎么说，你们真的已经是\x01",
            "很出色的游击士了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F87")

    ChrTalk(    #179
        0x8,
        (
            "#740F艾丝蒂尔，约修亚……\x02\x03",

            "还有阿加特和\x01",
            "雪拉扎德……\x02\x03",

            "做的真是很好呢。\x02\x03",

            "我身为协会的一员，\x01",
            "也替你们感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_3F87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4016")

    ChrTalk(    #180
        0x8,
        (
            "#740F艾丝蒂尔，约修亚……\x02\x03",

            "还有金先生和\x01",
            "雪拉扎德……\x02\x03",

            "做的真是很好呢。\x02\x03",

            "我身为协会的一员，\x01",
            "也替你们感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_4016")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40A3")

    ChrTalk(    #181
        0x8,
        (
            "#740F艾丝蒂尔，约修亚……\x02\x03",

            "还有雪拉扎德和\x01",
            "提妲……\x02\x03",

            "做的真是很好呢。\x02\x03",

            "我身为协会的一员，\x01",
            "也替你们感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_40A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_412A")

    ChrTalk(    #182
        0x8,
        (
            "#740F艾丝蒂尔和约修亚。\x01",
            "还有金先生和阿加特…\x02\x03",

            "做的真是很好呢。\x02\x03",

            "我身为协会的一员，\x01",
            "也替你们感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_412A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41B5")

    ChrTalk(    #183
        0x8,
        (
            "#740F艾丝蒂尔，约修亚……\x02\x03",

            "还有阿加特和\x01",
            "提妲……\x02\x03",

            "做的真是很好呢。\x02\x03",

            "我身为协会的一员，\x01",
            "也替你们感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_41B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4237")

    ChrTalk(    #184
        0x8,
        (
            "#740F艾丝蒂尔和约修亚。\x01",
            "还有金先生和提妲，\x02\x03",

            "做的真是很好呢。\x02\x03",

            "我身为协会的一员，\x01",
            "也替你们感到骄傲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4237")


    def lambda_423D():
        OP_8C(0x102, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_423D)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #185
        0x101,
        "#1017F#4P嗯，哪里哪里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x102,
        (
            "#1041F#1P今后也\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42AC")

    ChrTalk(    #187
        0x107,
        "#067F嘿嘿嘿……\x02",
    )

    CloseMessageWindow()

    label("loc_42AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42DD")

    ChrTalk(    #188
        0x108,
        "#070F好了，任务也算是完成了。\x02",
    )

    CloseMessageWindow()

    label("loc_42DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4306")

    ChrTalk(    #189
        0x106,
        "#051F嘿，这是当然了。\x02",
    )

    CloseMessageWindow()

    label("loc_4306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4410")

    ChrTalk(    #190
        0x103,
        (
            "#021F这样的话～爱娜啊～\x01",
            "这次不如请我们喝一杯吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        "#741F哎呀，一杯就够了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x103,
        (
            "#525F呵呵，这嘛…\x01",
            "用超大号杯也就差不多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        "#1007F#4P又、又扯到喝酒……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        (
            "#1048F#1P不管是什么话题，\x01",
            "她们也都能转移到喝酒上去…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4410")


    ChrTalk(    #195
        0x15,
        (
            "#1P不好意思，我也没有什么\x01",
            "礼物送大家表示感谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x15,
        (
            "#1P这就要回\x01",
            "矿山去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x15,
        (
            "#1P虽然事故刚刚结束，\x01",
            "但工作还是不能耽误了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #198
        0x101,
        "#1004F#4P嗯，说的也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x15,
        (
            "#1P上层的坑道也有\x01",
            "不少要做的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x15,
        (
            "#1P请大家替我向那位\x01",
            "警备的兄弟问声好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x8, 400)

    ChrTalk(    #201
        0x15,
        (
            "#1P他已经没事了吧？\x01",
            "那时伤得好像很厉害…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x8,
        (
            "#740F嗯，伤得确实不轻，\x01",
            "不过对游击士来说也没什么大不了的！\x02\x03",

            "现在已经恢复意识了，\x01",
            "正在旅店里面休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x15,
        (
            "#1P是吗……\x01",
            "那我也就放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 135, 400)

    ChrTalk(    #204
        0x15,
        (
            "#1P好了，那我这就告辞了。\x01",
            "今天实在是谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#1006F#4P您也要小心啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#1040F#1P工作请加油哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x15,
        "#1P噢！再见啦！\x02",
    )

    CloseMessageWindow()

    def lambda_4660():
        OP_6D(-30, 0, 115770, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4660)

    def lambda_4678():

        label("loc_4678")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_4678")

    QueueWorkItem2(0x8, 1, lambda_4678)

    def lambda_4689():

        label("loc_4689")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_4689")

    QueueWorkItem2(0x101, 1, lambda_4689)

    def lambda_469A():

        label("loc_469A")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_469A")

    QueueWorkItem2(0x102, 1, lambda_469A)

    def lambda_46AB():

        label("loc_46AB")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_46AB")

    QueueWorkItem2(0xF8, 1, lambda_46AB)

    def lambda_46BC():

        label("loc_46BC")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_46BC")

    QueueWorkItem2(0xF9, 1, lambda_46BC)
    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xFFFFFEB6, 0x0, 0x1BB5C, 0x7D0, 0x0)
    OP_8E(0x15, 0x104A, 0x0, 0x1AE28, 0x7D0, 0x0)
    OP_8C(0x15, 180, 400)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_470B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_470B)
    OP_8E(0x15, 0x1072, 0x0, 0x1A7DE, 0x7D0, 0x0)
    WaitChrThread(0x15, 0x0)
    SetChrFlags(0x15, 0x80)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x11, 0x1)
    OP_44(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_475F():
        OP_6D(90, 0, 117790, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_475F)
    Sleep(800)

    def lambda_477C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_477C)
    Sleep(100)

    def lambda_478F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_478F)
    Sleep(200)

    def lambda_47A2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_47A2)

    def lambda_47B0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_47B0)
    WaitChrThread(0x101, 0x1)

    def lambda_47C3():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47C3)
    Sleep(160)
    WaitChrThread(0x102, 0x1)

    def lambda_47E3():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47E3)
    Sleep(150)
    WaitChrThread(0xF8, 0x1)

    def lambda_4803():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4803)
    Sleep(140)
    WaitChrThread(0xF9, 0x1)

    def lambda_4823():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4823)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #208
        0x8,
        (
            "#740F好了，这下算是完成任务了。\x02\x03",

            "利吉和你们今天\x01",
            "都辛苦了。\x02\x03",

            "以后也请保持这个状态\x01",
            "继续活跃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        "#1040F#1P是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#740F这次的事件，\x01",
            "我也已经评定完毕了，\x02\x03",

            "要想收取报酬的话，\x01",
            "只要另外再向我报告就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1001F#4P嗯!了解。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #212
        "\x07\x02任务【营救矿工】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x8, 255)
    OP_A2(0xB)
    OP_A2(0x2085)
    OP_28(0xBF, 0x4, 0x10)
    OP_28(0xBF, 0x1, 0x200)
    OP_28(0xBF, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_15_3A6E end

    def Function_16_4992(): pass

    label("Function_16_4992")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_16_4992 end

    def Function_17_49EB(): pass

    label("Function_17_49EB")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A0C")
    OP_3F(0x151, 1)
    Jump("loc_4F24")

    label("loc_4A0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F24")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #213
        "\x07\x05请选择取下零力场发生器的成员。\x02",
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A75")
    Call(1, 18)
    Jump("loc_4A79")

    label("loc_4A75")

    Call(1, 19)

    label("loc_4A79")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AA0")
    Call(1, 18)
    Jump("loc_4AA4")

    label("loc_4AA0")

    Call(1, 19)

    label("loc_4AA4")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4ACB")
    Call(1, 18)
    Jump("loc_4ACF")

    label("loc_4ACB")

    Call(1, 19)

    label("loc_4ACF")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AF6")
    Call(1, 18)
    Jump("loc_4AFA")

    label("loc_4AF6")

    Call(1, 19)

    label("loc_4AFA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B41"),
        (1, "loc_4B87"),
        (2, "loc_4BCD"),
        (3, "loc_4C13"),
        (SWITCH_DEFAULT, "loc_4C59"),
    )


    label("loc_4B41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B64")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B84")

    label("loc_4B64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B84")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B84")

    Jump("loc_4C59")

    label("loc_4B87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BAA")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BCA")

    label("loc_4BAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BCA")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BCA")

    Jump("loc_4C59")

    label("loc_4BCD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C10")

    label("loc_4BF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C10")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C10")

    Jump("loc_4C59")

    label("loc_4C13")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C36")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C56")

    label("loc_4C36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C56")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C56")

    Jump("loc_4C59")

    label("loc_4C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C82")

    AnonymousTalk(    #214
        "\x07\x05未装备零力场发生器。\x02",
    )

    Jump("loc_4F15")

    label("loc_4C82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CCA")

    AnonymousTalk(    #215
        (
            "\x07\x05艾丝蒂尔已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4CCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D10")

    AnonymousTalk(    #216
        (
            "\x07\x05约修亚已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4D10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D58")

    AnonymousTalk(    #217
        (
            "\x07\x05雪拉扎德已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4D58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA0")

    AnonymousTalk(    #218
        (
            "\x07\x05奥利维尔已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4DA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE6")

    AnonymousTalk(    #219
        (
            "\x07\x05科洛丝已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4DE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2C")

    AnonymousTalk(    #220
        (
            "\x07\x05阿加特已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E96")

    AnonymousTalk(    #221
        (
            "\x07\x05提妲已取下零力场发生器，\x01",
            "无法使用魔法，战技，普通攻击。\x01",
            "但S战技『炮射冲击』仍可使用。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4E96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED6")

    AnonymousTalk(    #222
        (
            "\x07\x05金已取下零力场发生器\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_4F15")

    label("loc_4ED6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F15")

    AnonymousTalk(    #223
        (
            "\x07\x05凯文已取下零力场发生器\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )


    label("loc_4F15")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_4A0C")

    label("loc_4F24")

    Return()

    # Function_17_49EB end

    def Function_18_4F25(): pass

    label("Function_18_4F25")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_4F52"),
        (1, "loc_4F6D"),
        (2, "loc_4F86"),
        (3, "loc_4FA1"),
        (4, "loc_4FBC"),
        (5, "loc_4FD5"),
        (6, "loc_4FEE"),
        (7, "loc_5005"),
        (8, "loc_501A"),
        (SWITCH_DEFAULT, "loc_5031"),
    )


    label("loc_4F52")

    OP_CC(0x1, 0x0, "【艾丝蒂尔　装备中】")
    Jump("loc_5031")

    label("loc_4F6D")

    OP_CC(0x1, 0x0, "【约修亚　装备中】")
    Jump("loc_5031")

    label("loc_4F86")

    OP_CC(0x1, 0x0, "【雪拉扎德　装备中】")
    Jump("loc_5031")

    label("loc_4FA1")

    OP_CC(0x1, 0x0, "【奥利维尔　装备中】")
    Jump("loc_5031")

    label("loc_4FBC")

    OP_CC(0x1, 0x0, "【科洛丝　装备中】")
    Jump("loc_5031")

    label("loc_4FD5")

    OP_CC(0x1, 0x0, "【阿加特　装备中】")
    Jump("loc_5031")

    label("loc_4FEE")

    OP_CC(0x1, 0x0, "【提妲　装备中】")
    Jump("loc_5031")

    label("loc_5005")

    OP_CC(0x1, 0x0, "【金　装备中】")
    Jump("loc_5031")

    label("loc_501A")

    OP_CC(0x1, 0x0, "【凯文　装备中】")
    Jump("loc_5031")

    label("loc_5031")

    Return()

    # Function_18_4F25 end

    def Function_19_5032(): pass

    label("Function_19_5032")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_505F"),
        (1, "loc_507A"),
        (2, "loc_5093"),
        (3, "loc_50AE"),
        (4, "loc_50C9"),
        (5, "loc_50E2"),
        (6, "loc_50FB"),
        (7, "loc_5112"),
        (8, "loc_5127"),
        (SWITCH_DEFAULT, "loc_513E"),
    )


    label("loc_505F")

    OP_CC(0x1, 0x0, "【艾丝蒂尔　未装备】")
    Jump("loc_513E")

    label("loc_507A")

    OP_CC(0x1, 0x0, "【约修亚　未装备】")
    Jump("loc_513E")

    label("loc_5093")

    OP_CC(0x1, 0x0, "【雪拉扎德　未装备】")
    Jump("loc_513E")

    label("loc_50AE")

    OP_CC(0x1, 0x0, "【奥利维尔　未装备】")
    Jump("loc_513E")

    label("loc_50C9")

    OP_CC(0x1, 0x0, "【科洛丝　未装备】")
    Jump("loc_513E")

    label("loc_50E2")

    OP_CC(0x1, 0x0, "【阿加特　未装备】")
    Jump("loc_513E")

    label("loc_50FB")

    OP_CC(0x1, 0x0, "【提妲　未装备】")
    Jump("loc_513E")

    label("loc_5112")

    OP_CC(0x1, 0x0, "【金　未装备】")
    Jump("loc_513E")

    label("loc_5127")

    OP_CC(0x1, 0x0, "【凯文　未装备】")
    Jump("loc_513E")

    label("loc_513E")

    Return()

    # Function_19_5032 end

    SaveToFile()

Try(main)
