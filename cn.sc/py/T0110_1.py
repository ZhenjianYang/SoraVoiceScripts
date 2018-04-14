from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0110_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0110_1 ._SN',
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
        "Function_1_48C",          # 01, 1
        "Function_2_A0B",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0xFE,
        "哎呀，是游击士们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "我家的鲁克\x01",
            "终于醒来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "已经完全恢复了呢。\x01",
            "现在已经出去玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 0)), scpexpr(EXPR_END)), "loc_18E")

    ChrTalk(    #3
        0x101,
        (
            "#1017F啊，嗯。\x01",
            "已经见过他了呢。\x02\x03",

            "真的比之前\x01",
            "有精神多了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "现在反倒更担心\x01",
            "会不会得意忘形反而受伤呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B")

    label("loc_18E")


    ChrTalk(    #5
        0x101,
        (
            "#1001F嘿嘿，太好了。\x01",
            "这样就放心了。\x02\x03",

            "待会儿我们\x01",
            "也去看看他吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "啊啊，就这么办吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "那个孩子\x01",
            "好像很喜欢你似的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #8
        0xFE,
        (
            "话说回来，是不是\x01",
            "有什么事才来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1008F啊，您看出来了？\x02\x03",

            "其实是\x01",
            "向您询问一些事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "哎呀，是什么呢？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05诉说了在寻找拉欧老人\x01",
            "所说的炖煮材理食谱的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #12
        0xFE,
        "放了胡椒的炖煮料理啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "我确实吃过，\x01",
            "不过没有做过哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "以前帮着父母做过，\x01",
            "都是些简单的事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1007F哎呀呀，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_3C1")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #16
        0x103,
        (
            "#020F总之\x01",
            "先去报告那个食谱吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #17
        0x101,
        "#1015F嗯，只有先这样了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_482")

    label("loc_3C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_429")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #18
        0x103,
        (
            "#020F老老实实调查一下\x01",
            "雷特拉先生家不好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #19
        0x101,
        "#1015F嗯……或许是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_482")

    label("loc_429")


    ChrTalk(    #20
        0x103,
        (
            "#020F……问问其他人\x01",
            "可能比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #21
        0xFE,
        "啊啊，不好意思…但也只能这么办了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_482")

    OP_A2(0x9)
    OP_28(0x75, 0x1, 0x10)
    Return()

    # Function_0_AA end

    def Function_1_48C(): pass

    label("Function_1_48C")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 91960, 0, 162870, 90)
    SetChrPos(0xF7, 91150, 0, 162270, 90)
    SetChrPos(0xF8, 90480, 0, 163570, 90)
    SetChrPos(0xF9, 91330, 0, 164280, 135)
    OP_8C(0xFE, 270, 0)
    OP_6D(91870, 0, 163740, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #22
        0xFE,
        "啊，有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1000F不，没什么\x01",
            "特别重要的事……\x02\x03",

            "……雷特拉先生\x01",
            "好像有很多书吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "哼哼，这可是\x01",
            "我自豪的收藏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "对以收集古书为兴趣的我来说，\x01",
            "这里就像是我的城堡一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015F以收集古书为兴趣……吗。\x02\x03",

            "嗯～慎重起见，\x01",
            "问问看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#027F#1P嗯，我看\x01",
            "有确认一下的价值哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "你们说什么？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x05传达了协会的工作，要寻找\x01",
            "布露姆老奶奶的食谱册的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #31
        0x101,
        (
            "#1011F──就是这么回事……\x02\x03",

            "那个食谱册，\x01",
            "雷特拉先生有吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "听说是老奶奶的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "啊啊，记得以前，\x01",
            "她的确是送给我了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#1004F咦，真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "啊啊，因为是传统料理的食谱，\x01",
            "所以她说想设法保存下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "于是我就拜托老奶奶\x01",
            "转手给我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1011F原来是这样啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_815")

    ChrTalk(    #38
        0x107,
        "#060F没错了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC")

    label("loc_815")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83D")

    ChrTalk(    #39
        0x105,
        "#040F好像没错了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC")

    label("loc_83D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_869")

    ChrTalk(    #40
        0x108,
        "#070F嗯，看来没错了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC")

    label("loc_869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_895")

    ChrTalk(    #41
        0x104,
        "#030F呵，好像没错了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC")

    label("loc_895")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BC")

    ChrTalk(    #42
        0x106,
        "#051F好像没错了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_8BC")


    ChrTalk(    #43
        0x103,
        (
            "#021F#1P呵呵，看来\x01",
            "终于找到目标了。\x02\x03",

            "那么，麻烦立刻\x01",
            "拿给我们看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1000F……就是这样，\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "啊啊，小事一桩。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "……话虽如此，\x01",
            "其实放在哪里\x01",
            "我也记不清了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "不好意思，\x01",
            "你们自己去找找看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "一定在这个房间里，\x01",
            "我确定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1006F啊，嗯，明白了。\x02\x03",

            "既然同意给我们看，\x01",
            "这点小事当然自己做啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x75, 0x1, 0x400)
    OP_65(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_1_48C end

    def Function_2_A0B(): pass

    label("Function_2_A0B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05书架上有『布露姆老奶奶的食谱册』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读书】\x01",      # 0
            "【否】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA9")
    OP_B8(0x236, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA6")
    Sleep(400)
    OP_3E(0x236, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x00得到了\x1F\x36\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #52
        0x101,
        (
            "#1028F好……\x01",
            "做好笔记了。\x02\x03",

            "#1007F说实话，完全不懂什么意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020F算了，解读就交给专业人士吧。\x02\x03",

            "必要的食材也知道了，\x01",
            "赶快准备回去报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x75, 0x1, 0x800)

    label("loc_BA6")

    Jump("loc_BA9")

    label("loc_BA9")

    TalkEnd(0xFF)
    Return()

    # Function_2_A0B end

    SaveToFile()

Try(main)
