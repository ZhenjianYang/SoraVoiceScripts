from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2131_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '',                                     # 8
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
        "Function_1_45F",          # 01, 1
        "Function_2_89A6",         # 02, 2
        "Function_3_89D6",         # 03, 3
        "Function_4_8A0B",         # 04, 4
        "Function_5_8A3B",         # 05, 5
        "Function_6_8A63",         # 06, 6
        "Function_7_8A6B",         # 07, 7
        "Function_8_8A73",         # 08, 8
        "Function_9_8A7B",         # 09, 9
        "Function_10_8A83",        # 0A, 10
        "Function_11_8A8B",        # 0B, 11
        "Function_12_8AC8",        # 0C, 12
        "Function_13_8B0C",        # 0D, 13
        "Function_14_8B66",        # 0E, 14
        "Function_15_8BCD",        # 0F, 15
        "Function_16_92E9",        # 10, 16
        "Function_17_97A1",        # 11, 17
        "Function_18_97ED",        # 12, 18
        "Function_19_9828",        # 13, 19
        "Function_20_984C",        # 14, 20
        "Function_21_9870",        # 15, 21
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_28B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_FF")

    ChrTalk(    #0
        0xFE,
        "今天真是麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "如果有事\x01",
            "还请多多帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140")

    label("loc_FF")


    ChrTalk(    #2
        0xFE,
        "我在这里等我丈夫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "之后娱乐场的人\x01",
            "一定会想办法解决的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140")

    Jump("loc_288")

    label("loc_143")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_19C")

    ChrTalk(    #4
        0xFE,
        "特地麻烦你们真不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "如果再发生什么事\x01",
            "还请多多帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF")

    label("loc_19C")


    ChrTalk(    #6
        0xFE,
        "我在这里再等等丈夫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "娱乐场的人\x01",
            "要是能解决那个人就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF")

    Jump("loc_288")

    label("loc_1E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1FB")
    TalkEnd(0xFE)
    EventBegin(0x0)
    Call(1, 1)
    EventEnd(0x0)
    Return()

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_21E")

    ChrTalk(    #8
        0xFE,
        (
            "谁来\x01",
            "阻止我丈夫啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288")

    label("loc_21E")

    OP_A2(0x7)

    ChrTalk(    #9
        0xFE,
        "啊啊，怎么办呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "我老公\x01",
            "已经完全打算\x01",
            "放手一搏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "拜托谁来帮帮忙啊！\x01",
            "请阻止我丈夫吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288")

    Jump("loc_45B")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_36D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2EF")

    ChrTalk(    #12
        0xFE,
        (
            "我实在看不下去了,\x01",
            "所以来了１楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "啊啊，娱乐场的人\x01",
            "求求你们阻止我丈夫吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A")

    label("loc_2EF")

    OP_A2(0x7)

    ChrTalk(    #14
        0xFE,
        (
            "啊，真伤脑筋……\x01",
            "我丈夫真是昏了头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "他再这样下去，\x01",
            "搞不好就要\x01",
            "变成废人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "啊啊，娱乐场的人\x01",
            "请努力啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A")

    Jump("loc_45B")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_3AD")

    ChrTalk(    #17
        0xFE,
        (
            "真奇怪。\x01",
            "店里没人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "服务生都\x01",
            "到哪里去了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B")

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_400")

    ChrTalk(    #19
        0xFE,
        (
            "但是，必须\x01",
            "见好就收才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "否则我丈夫\x01",
            "容易得意忘形。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B")

    label("loc_400")

    OP_A2(0x7)

    ChrTalk(    #21
        0xFE,
        (
            "吃角子游戏机真有趣。\x01",
            "运气好可能会中大奖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "我丈夫好像也赢了，\x01",
            "会赚钱回来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_45F(): pass

    label("Function_1_45F")

    OP_4A(0xE, 0)
    Fade(1000)
    SetChrPos(0x101, 5600, 250, 33020, 0)
    SetChrPos(0xF7, 4770, 250, 32659, 0)
    SetChrPos(0x104, 5560, 250, 31520, 0)
    SetChrPos(0x105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_4F6")

    ChrTalk(    #23
        0xE,
        "啊，游击士！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        "有空听我说话了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7")

    label("loc_4F6")


    ChrTalk(    #25
        0x101,
        (
            "#1011F请问～打扰一下行吗？\x02\x03",

            "你是拉科舒小姐？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #26
        0xE,
        "啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xE,
        "难道你们是游击士！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1000F是啊。\x01",
            "我们看了公告板来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xE,
        (
            "我、我有事\x01",
            "想马上拜托你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        "……能听我说吗？\x02",
    )

    CloseMessageWindow()

    label("loc_5C7")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_743")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_699")

    ChrTalk(    #31
        0x101,
        (
            "#1015F嗯……抱歉……\x02\x03",

            "还不大方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        "咦～不行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xE,
        (
            "如果方便了\x01",
            "请立刻过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1000F嗯，先就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_735")

    label("loc_699")


    ChrTalk(    #35
        0x101,
        (
            "#1007F啊，抱歉……\x02\x03",

            "现在有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        "咦～这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "那，方便的时候\x01",
            "请立刻过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        (
            "这关系到\x01",
            "我们夫妇的未来啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1000F嗯、嗯，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_735")

    OP_28(0x68, 0x1, 0x8000)
    OP_4B(0xE, 0)
    Return()

    label("loc_743")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_78C")

    ChrTalk(    #40
        0x101,
        (
            "#1006F嗯，没问题了。\x01",
            "让你久等了。\x02\x03",

            "那么，是怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BA")

    label("loc_78C")


    ChrTalk(    #41
        0x101,
        (
            "#1006F嗯，当然可以。\x02\x03",

            "那么，是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BA")

    OP_4A(0xD, 0)
    OP_4A(0xB, 0)
    OP_28(0x68, 0x1, 0x1)
    OP_28(0x68, 0x1, 0x2)

    ChrTalk(    #42
        0xE,
        (
            "我想拜托的\x01",
            "是很简单的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "希望你们想办法\x01",
            "打败我丈夫！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x101,
        "#1004F……咦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8B1")

    ChrTalk(    #45
        0x106,
        "#052F这就是委托的内容？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C8")

    label("loc_8B1")


    ChrTalk(    #46
        0x103,
        "#023F这是委托吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8C8")


    ChrTalk(    #47
        0x104,
        (
            "#033F只要\x01",
            "赢了你丈夫就行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "对，任何游戏都可以，\x01",
            "无论如何要赢了我丈夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        (
            "我丈夫本来\x01",
            "就容易得意忘形……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xE,
        (
            "在娱乐场稍微连胜几盘\x01",
            "就马上一副恶棍嘴脸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xE,
        (
            "他就是这种人，这样下去\x01",
            "真的会沉迷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xE,
        (
            "所以，在变成那样之前\x01",
            "我希望让他吃点苦头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1016F哈、哈哈……原来如此。\x02\x03",

            "真是家家有本难念的经啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A2C")

    ChrTalk(    #54
        0x106,
        "#551F……你也够辛苦的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4B")

    label("loc_A2C")


    ChrTalk(    #55
        0x103,
        "#026F嗯，你也够辛苦的呢。\x02",
    )

    CloseMessageWindow()

    label("loc_A4B")


    ChrTalk(    #56
        0xE,
        "哪里，我也想得太简单了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xE,
        (
            "他邀请我去娱乐场游玩的时候\x01",
            "就该断然拒绝的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        "唉，发牢骚也不是办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "……那么，作为资本\x01",
            "给你们１０００米拉吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #60
        "\x07\x00得到了\x07\x04１０００\x07\x00米拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #61
        0xE,
        (
            "如果全部压上一回定胜负\x01",
            "我丈夫一定会上钩的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#044F这么说……\x02\x03",

            "你丈夫现在就在二楼的娱乐场里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xE,
        "是的，他一直逗留在那里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xE,
        (
            "在扑克台那里\x01",
            "叫菲利奥的就是他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1000F明白。\x01",
            "扑克台那里的菲利奥对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "绝不要手下留情。\x01",
            "请彻底打败他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xE,
        "……其它还有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1015F嗯，大概知道要做什么了……\x02\x03",

            "话说回来，怎样赢他\x01",
            "才是个问题呢。\x02\x03",

            "因为这些\x01",
            "完全是靠运气嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D01")

    ChrTalk(    #69
        0x106,
        (
            "#050F啊啊，不过活用运势\x01",
            "也是靠手段的。\x02\x03",

            "能不能赢就看对手了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D43")

    label("loc_D01")


    ChrTalk(    #70
        0x103,
        (
            "#027F嗯，不过活用运势\x01",
            "也是靠手段的。\x02\x03",

            "能不能赢就看对手了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D43")


    ChrTalk(    #71
        0x104,
        "#031F呵，就是说要因势利导啦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #72
        0x101,
        (
            "#1015F嗯～……\x01",
            "是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xE,
        (
            "那就没问题了。\x01",
            "我丈夫耍花招可是外行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "又不擅长说谎，\x01",
            "想什么都一目了然……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "本来就是个\x01",
            "完全不适合玩这个的人哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #76
        0x101,
        (
            "#1011F啊，真的吗？\x02\x03",

            "#1006F嗯，这样说\x01",
            "我就有点自信了。\x02\x03",

            "……好！有精神了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_EB3")

    ChrTalk(    #77
        0x106,
        (
            "#051F哦，就是这股劲。\x02\x03",

            "要是输了气势，\x01",
            "本来能赢的牌局也赢不了了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFF")

    label("loc_EB3")


    ChrTalk(    #78
        0x103,
        (
            "#020F呵呵，就是这种气势。\x02\x03",

            "或许算不上什么理由，\x01",
            "不过比赛要的就是气势。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFF")


    ChrTalk(    #79
        0xE,
        "那么，努力哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "请尽可能的\x01",
            "打败我丈夫吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_20(0x3E8)
    SoundLoad(254)
    SoundLoad(256)
    SoundLoad(663)
    SetChrPos(0xD, 32530, 0, 29680, 79)
    SetChrPos(0x101, 29280, 0, 35000, 180)
    SetChrPos(0xF7, 30180, 0, 35430, 180)
    SetChrPos(0x104, 28980, 0, 36040, 180)
    SetChrPos(0x105, 29800, 0, 36620, 180)
    OP_6D(28300, 0, 25990, 0)
    OP_6C(332000, 0)

    def lambda_FC5():
        OP_6D(29350, 0, 36160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FC5)

    def lambda_FDD():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_FDD)
    OP_21()
    OP_1D(0x19)
    Sleep(400)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    Sleep(400)

    ChrTalk(    #81
        0x104,
        (
            "#030F唔，这娱乐场\x01",
            "气氛还挺不错嘛。\x02\x03",

            "设备也挺新，\x01",
            "开张还没多久吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x105,
        (
            "#040F对，似乎是诞辰庆典的时候\x01",
            "重新装修开放的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1011F啊，说起来\x01",
            "之前来的时候还在装修中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        (
            "#035F原来如此……\x02\x03",

            "#033F……对了，\x01",
            "关键的对象在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1015F嗯，记得太太\x01",
            "说是在扑克台来着……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0xF7, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xF7, 0xB, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1166")

    ChrTalk(    #86
        0x106,
        "#050F……嗯，是那位吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_118A")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_118A")

    ChrTalk(    #87
        0x103,
        "#020F……一定是那位吧。\x02",
    )

    CloseMessageWindow()

    label("loc_118A")


    def lambda_1190():
        TurnDirection(0x101, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1190)
    Sleep(100)

    def lambda_11A3():
        TurnDirection(0x105, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11A3)
    Sleep(50)

    def lambda_11B6():
        TurnDirection(0x104, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11B6)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)
    OP_6D(32170, 0, 30500, 2000)

    ChrTalk(    #88
        0xD,
        "#1P……好～来吧～～\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #89
        0xD,
        "#3S#1P你看来了！是Ｊ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xD,
        (
            "#1P唔～～这超强的手气！\x01",
            "简直是无敌的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        "#2P……客人赢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        (
            "#1P哎呀～你也很努力了。\x01",
            "就是找错了对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        "#1P哈哈哈哈哈哈。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(29520, 0, 35790, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #94
        0x101,
        (
            "#1007F……真是一目了然啊～\x02\x03",

            "嗯，是那个人没错了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(    #95
        0x106,
        (
            "#050F赶快去搭话吧。\x02\x03",

            "再磨磨蹭蹭的\x01",
            "又要开始啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CC")

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_13CC")

    ChrTalk(    #96
        0x103,
        (
            "#020F马上去搭话吧。\x02\x03",

            "再磨磨蹭蹭的\x01",
            "又要开始啰。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CC")


    ChrTalk(    #97
        0x101,
        "#1002F啊，是哦。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_43(0x101, 0x1, 0x1, 0x2)
    Sleep(100)
    OP_43(0x104, 0x1, 0x1, 0x4)
    Sleep(400)
    OP_43(0xF7, 0x1, 0x1, 0x3)
    Sleep(200)
    OP_43(0x105, 0x1, 0x1, 0x5)
    Sleep(400)
    Fade(1000)
    OP_6D(32170, 0, 30500, 0)
    OP_6D(31090, 0, 31350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #98
        0xD,
        "好，那就……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #99
        0xD,
        "咦？你们怎么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1006F#5P大哥你\x01",
            "就是传说中的强者吧。\x02\x03",

            "其实我们\x01",
            "是来挑战你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        "挑战？找我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "倒是可以，不过你们有钱吗？\x01",
            "五块十块的恕不奉陪哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_155F")

    ChrTalk(    #103
        0x106,
        (
            "#050F#2P１０００米拉，\x01",
            "全部押上定胜负怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1597")

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1597")

    ChrTalk(    #104
        0x103,
        (
            "#027F#2P１０００米拉，\x01",
            "全部押上定胜负如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1597")


    ChrTalk(    #105
        0xD,
        "呵呵，真是不怕死啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xD,
        (
            "好啊，我就\x01",
            "接受挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        "……那，谁来做我的对手？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "不然一起上\x01",
            "也没关系哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1016F#5P一、一起上怎么可能……\x01",
            "又不是抓阄。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_6D(32240, 0, 31870, 1000)

    ChrTalk(    #110
        0xB,
        (
            "#2P……那么，客人。\x01",
            "变规则同花顺怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#2P这个还能用复数次\x01",
            "的胜负来做个决断。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16BC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_16BC)
    Sleep(100)

    def lambda_16CF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_16CF)

    def lambda_16DD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_16DD)
    Sleep(150)

    def lambda_16F0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_16F0)
    TurnDirection(0xD, 0xB, 400)
    Sleep(400)

    ChrTalk(    #112
        0x101,
        "#1004F有这样的游戏吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        (
            "唔～好像很有趣嘛。\x01",
            "说明一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xB,
        (
            "#2P好的，双方各出选手，\x01",
            "以三回合对战决胜负。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "#2P对战就用普通的同花顺，\x01",
            "先获得１胜的队伍就算赢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        (
            "#2P不过，『放弃』的机会\x01",
            "两个队都只能有一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xB,
        (
            "#2P队伍中有一人放弃之后，\x01",
            "那个队伍的选手\x01",
            "就无法再放弃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xD,
        "原来如此，三回定胜负吗～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xD,
        (
            "嗯，方便的\x01",
            "好办法嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xD, 0x101, 400)
    OP_6D(30280, 0, 32090, 1000)

    ChrTalk(    #120
        0xD,
        (
            "咦……？\x01",
            "但是，你们有４人啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #121
        0x101,
        (
            "#1006F#1P４人也无所谓啦。\x02\x03",

            "既然多的话，\x01",
            "就退出一人好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xD, 400)

    ChrTalk(    #122
        0x105,
        (
            "#043F#2P那个，这样的话……\x02\x03",

            "……就让我退出吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    def lambda_1948():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1948)

    def lambda_1956():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1956)

    def lambda_1964():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1964)
    TurnDirection(0x0, 0x105, 400)

    ChrTalk(    #123
        0x101,
        "#1004F#3P咦？科洛丝吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x105,
        (
            "#043F#2P对，校规禁止\x01",
            "学生在娱乐场游玩。\x02\x03",

            "所以，我就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1016F#3P啊哈哈……这样啊。\x02\x03",

            "唔，确实\x01",
            "是不利于教育。\x02\x03",

            "#1000F……嗯，情况明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        "#047F#2P嗯，对不起了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xD, 400)

    ChrTalk(    #127
        0x104,
        (
            "#030F#1P嗯，这样\x01",
            "３回定胜负就没问题了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xD,
        "我几回定胜负都无所谓。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        (
            "反正最后\x01",
            "总是要赢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "就用刚才说明的\x01",
            "游戏可以吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AD3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1AD3)

    def lambda_1AE1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1AE1)

    def lambda_1AEF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1AEF)

    def lambda_1AFD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1AFD)
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #131
        0xD,
        "嗯，这个就行。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B4C")

    ChrTalk(    #132
        0x106,
        "#050F#2P啊啊，我们也没问题。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B73")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1B73")

    ChrTalk(    #133
        0x103,
        "#020F#2P嗯，我们也没问题。\x02",
    )

    CloseMessageWindow()

    label("loc_1B73")


    ChrTalk(    #134
        0xB,
        "那么，我去准备一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xB,
        (
            "趁此机会请客人们\x01",
            "决定出场顺序。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1000F决定出场的\x01",
            "顺序就可以了吧？\x02\x03",

            "嗯，明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        "就麻烦你们了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #138
        0xD,
        "赶快定吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_43(0xB, 0x1, 0x1, 0x11)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1C61():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C61)
    Sleep(100)

    def lambda_1C74():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1C74)
    Sleep(150)

    def lambda_1C87():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1C87)
    TurnDirection(0x0, 0x105, 400)

    def lambda_1C9C():
        OP_8C(0xD, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C9C)
    OP_69(0x105, 0x5DC)

    ChrTalk(    #139
        0x101,
        (
            "#1015F话是这么说……\x02\x03",

            "那么，怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x104,
        (
            "#035F#1P嗯，应该按照\x01",
            "玩牌的水平来决定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(    #141
        0x101,
        (
            "#1019F话先说在前头，\x01",
            "我可没什么自信。\x02\x03",

            "以前总是输给约修亚的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x106,
        (
            "#053F#2P我也金盆洗手\x01",
            "好久了……\x02\x03",

            "#050F……不过，比赛是靠气势的。\x01",
            "我尽量努力啦。\x02\x03",

            "那，你怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x104,
        (
            "#031F#1P呼，放心吧。\x01",
            "玩牌我略有心得。\x02\x03",

            "因势利导的中坚\x01",
            "就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x106,
        "#050F#2P好，那就这么办吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1002F奥利维尔是２号。\x02\x03",

            "然后就看我和阿加特了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #146
        0x106,
        (
            "#057F#2P我第一个上。\x02\x03",

            "你垫后吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #147
        0x101,
        (
            "#1020F啊……！？\x02\x03",

            "怎、怎么擅自决定？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #148
        0x104,
        (
            "#031F#1P呵，所谓先手必胜嘛。\x02\x03",

            "就是说，策略就是\x01",
            "靠我和阿加特来定胜负。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x106,
        (
            "#053F#2P就这么回事。\x02\x03",

            "嗯，顺序什么的没多大意义。\x01",
            "关键是能赢就行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x10)

    ChrTalk(    #150
        0x101,
        (
            "#1007F话、话是没错啦，\x01",
            "压力好大……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 270, 400)

    ChrTalk(    #151
        0xB,
        "客人，准备就绪了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 400)

    ChrTalk(    #152
        0x104,
        "#032F#1P嗯，那就上吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1009F呜～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x106,
        "#552F#2P……来，开始啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x105,
        "#040F#1P艾丝蒂尔，加油。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #156
        0x101,
        "#1016F唔，嗯，谢了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #157
        0x101,
        (
            "#1002F好，事到如今\x01",
            "只有硬着头皮上了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2370")

    label("loc_207F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2370")

    ChrTalk(    #158
        0x101,
        (
            "#1019F话先说在前头，\x01",
            "我可没什么自信。\x02\x03",

            "以前总是输给约修亚的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #159
        0x101,
        (
            "#1006F啊，但是……\x01",
            "雪拉姐有自信吧？\x02\x03",

            "占卜也是用牌的嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #160
        0x103,
        (
            "#020F#2P嗯，会一点。\x02\x03",

            "#026F不过，我嘛…\x01",
            "万不得已还有秘技……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #161
        0x101,
        "#1011F秘技……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x103,
        "#525F#2P呵呵，秘技当然就是秘密啰。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x104,
        (
            "#031F#1P呼，那就麻烦\x01",
            "雪拉垫后了。\x02\x03",

            "#030F相对的，\x01",
            "就由我担任中坚吧。\x02\x03",

            "因为第二战\x01",
            "似乎更需要策略。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#1015F雪拉姐最后，\x01",
            "奥利维尔第二，这么说来……\x02\x03",

            "#1004F我打头阵？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x103,
        (
            "#021F#2P嗯，很轻松吧。\x02\x03",

            "轻松的上场吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    OP_A3(0x10)

    ChrTalk(    #166
        0x101,
        "#1007F唔，轻松倒是轻松……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 270, 400)

    ChrTalk(    #167
        0xB,
        "客人，准备就绪了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #168
        0x101,
        "#1002F啊，好像要开始了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #169
        0x104,
        "#030F#1P嗯，那就上吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x105,
        (
            "#040F各位，\x01",
            "请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#1005F好，抖擞精神上阵吧！\x02",
    )

    CloseMessageWindow()

    label("loc_2370")

    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0x18, 255)
    TurnDirection(0x18, 0xD, 0)
    LoadEffect(0x0, "craft\\cr201_01.eff")
    Sleep(1000)
    OP_6D(27430, 0, 32610, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23E5")
    SetChrPos(0xF7, 33000, 0, 31870, 135)
    SetChrPos(0x101, 28570, 0, 31000, 90)
    Jump("loc_2407")

    label("loc_23E5")

    SetChrPos(0x101, 33000, 0, 31870, 135)
    SetChrPos(0xF7, 28570, 0, 31000, 90)

    label("loc_2407")

    SetChrPos(0x105, 27670, 0, 31940, 90)
    SetChrPos(0x104, 28850, 0, 32500, 90)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6D(32073, 0, 31585, 2000)
    Sleep(1000)

    ChrTalk(    #172
        0xB,
        (
            "……那么现在\x01",
            "开始三回战决胜负。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xB,
        (
            "同花顺的规则\x01",
            "和本地普通规则相同……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        (
            "不过图案也是有强弱之分的\x01",
            "这点请多加注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "最强的是黑桃，\x01",
            "其次是红心，再次是方块\x01",
            "梅花是最弱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xB,
        "……那么，现在发放手牌。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3582")
    Call(2, 3)
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #177
        0xD,
        (
            "哟呵呵！\x01",
            "起手就是好兆头！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xD,
        (
            "呀～这下搞不好\x01",
            "可以速战速决了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #179
        0x101,
        (
            "#1002F（怎，怎么对手\x01",
            "  状况那么好啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x104,
        (
            "#035F（哼，如果真是好牌\x01",
            "  一般应该是沉默的哦。）\x02\x03",

            "#030F（对手要是放弃了\x01",
            "  就不算赢的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1015F（啊，原来如此啊。）\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x190, 0x0, 0x1F4, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x0, 0x140, 0x64, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0xC8, 0x140, 0x12C, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x64, 0x0, 0xC8, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #182
        (
            "#050F（……那么，这样吧。）\x02\x03",

            "（应该以大牌为目标\x01",
            "还是小牌保底呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【除了Ｋ其它全部换】\x01",          # 0
            "【以４～８的顺子为目标】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B1")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #183
        (
            "#050F（哪边都一样危险……）\x02\x03",

            "（不过，反正还是首战。\x01",
            "  这里就以概率高的一方为目标吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_29FD")

    label("loc_29B1")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #184
        (
            "#050F（哪边都一样危险……）\x02\x03",

            "（那就以大牌为目标吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_29FD")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x106, 400)

    ChrTalk(    #185
        0xB,
        "要换牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A84")

    ChrTalk(    #186
        0x106,
        "#050F#2P啊啊，换４张。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #187
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xD,
        "#1P我换３张。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ACE")

    label("loc_2A84")


    ChrTalk(    #189
        0x106,
        "#050F#2P啊啊，换２张。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #190
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xD,
        "#1P我换３张。\x02",
    )

    CloseMessageWindow()

    label("loc_2ACE")

    OP_59()
    Call(2, 4)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #192
        0x105,
        (
            "#042F（阿加特的表情……\x01",
            "  纹丝不动。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x104,
        (
            "#031F#2P（嗯嗯，简直\x01",
            "  就是扑克脸。）\x02\x03",

            "（充满了气魄的眼神，\x01",
            "  令人着迷的男人风采。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #194
        0xD,
        (
            "#1P呼呼，不错哦～\x01",
            "来的就是我要的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #195
        0xD,
        (
            "#1P好了，挑战者们。\x01",
            "放马过来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #196
        0x101,
        (
            "#1007F（对、对方真是截然相反啊～）\x02\x03",

            "（说是那么说，\x01",
            "  谁知道是真是假。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 5)
    OP_0D()
    TurnDirection(0xB, 0x106, 400)

    ChrTalk(    #197
        0xB,
        "……要比牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EAA")
    OP_28(0x68, 0x1, 0x8)

    ChrTalk(    #198
        0x106,
        (
            "#053F#2P…………………………\x02\x03",

            "#050F……哎呀，我放弃。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #199
        0xD,
        "#1P咦～要放弃吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xD,
        (
            "#1P嗯～难得\x01",
            "我凑得一手好牌，真可惜啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        (
            "那么，这边的客人。\x01",
            "之后就不能再放弃了哦。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #202
        0x101,
        "#1026F啊～啊，放弃了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x104,
        "#033F#2P唔，看来是没办法的。\x02",
    )

    CloseMessageWindow()

    def lambda_2DAC():

        label("loc_2DAC")

        TurnDirection(0x104, 0x106, 400)
        OP_48()
        Jump("loc_2DAC")

    QueueWorkItem2(0x104, 1, lambda_2DAC)
    OP_8E(0x106, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #204
        0x101,
        (
            "#1006F辛苦了，阿加特。\x02\x03",

            "放弃不像你的作风嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x106,
        (
            "#551F#4P别说了……\x01",
            "我也这么想。\x02\x03",

            "#552F……不过，这下\x01",
            "后面可没有退路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x105,
        (
            "#042F#1P嗯，因为规定是\x01",
            "只能放弃一次嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F啊，对哦……\x02\x03",

            "比想象的更严苛啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_2EAA")

    OP_28(0x68, 0x1, 0x4)

    ChrTalk(    #208
        0x106,
        (
            "#053F#2P啊啊，当然。\x02\x03",

            "现在就比牌吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #209
        0xD,
        "#1P咦……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #210
        0xD,
        (
            "#1P这，这行吗？\x01",
            "我手里可是无上的好牌……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0xD, 400)
    Sleep(1000)

    ChrTalk(    #211
        0x106,
        (
            "#050F#2P……说得倒是好听。\x02\x03",

            "说比就比。\x01",
            "别说废话，快决定吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #212
        0xB,
        "客人要怎样做？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #213
        0xD,
        "#1P唔～怎么办呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xD,
        (
            "#1P这手牌要比的话\x01",
            "大概也能取胜……\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0x106, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    OP_22(0x297, 0x0, 0x64)

    ChrTalk(    #215
        0x106,
        "#057F#2P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #216
        0xD,
        "#1P…………行不行！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_D9(0x0, "CTI00150")
    FadeToDark(300, 0, 100)
    OP_22(0x21F, 0x0, 0x64)
    Sleep(2000)
    OP_D9(0x1)
    FadeToBright(300, 0)

    def lambda_30E0():

        label("loc_30E0")

        TurnDirection(0xB, 0xD, 400)
        OP_48()
        Jump("loc_30E0")

    QueueWorkItem2(0xB, 1, lambda_30E0)

    def lambda_30F1():

        label("loc_30F1")

        TurnDirection(0x18, 0xD, 400)
        OP_48()
        Jump("loc_30F1")

    QueueWorkItem2(0x18, 1, lambda_30F1)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3114():
        OP_8F(0xD, 0x7E88, 0x0, 0x6E3E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3114)

    def lambda_312F():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_312F)

    ChrTalk(    #217
        0xD,
        "啊啊啊…啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xD,
        "放、放弃！　我放弃！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xD,
        "我放弃就是了，饶了我吧！？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_44(0xB, 0x1)
    OP_44(0x18, 0x1)
    TurnDirection(0x106, 0xB, 400)
    Sleep(500)

    ChrTalk(    #220
        0x106,
        "#050F#2P喂，他说放弃了。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x106, 400)

    ChrTalk(    #221
        0xB,
        "咦！？啊，是哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #222
        0xB,
        (
            "那么，菲利奥先生。\x01",
            "以后的比赛中就不能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x2, 0x1, 0x14)

    ChrTalk(    #223
        0xD,
        "呼，呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xD,
        "吓、吓死我了～～\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    ChrTalk(    #225
        0x101,
        (
            "#1018F好啊，对手放弃了！\x02\x03",

            "#1016F不过，与其说是『放弃』，\x01",
            "感觉更像是『被迫放弃』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x105,
        (
            "#041F#1P嘻嘻……\x01",
            "真像阿加特的风格。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3322():

        label("loc_3322")

        TurnDirection(0x104, 0x106, 400)
        OP_48()
        Jump("loc_3322")

    QueueWorkItem2(0x104, 1, lambda_3322)

    def lambda_3333():

        label("loc_3333")

        TurnDirection(0xD, 0x106, 400)
        OP_48()
        Jump("loc_3333")

    QueueWorkItem2(0xD, 1, lambda_3333)
    OP_8E(0x106, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)
    OP_44(0xD, 0x1)

    ChrTalk(    #227
        0x101,
        (
            "#1001F辛苦了，阿加特。\x02\x03",

            "你平时老说『胜负靠气势』\x01",
            "果然不是盖的啊～\x02\x03",

            "仅靠气势就赢了牌，\x01",
            "真是令人大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x104,
        (
            "#031F#2P唔，这就叫做\x01",
            "转败为胜吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x106,
        (
            "#051F#4P啊啊，算是吧。\x02\x03",

            "#050F不过，还不算赢了。\x01",
            "之后也要鼓足气势上阵哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x105,
        (
            "#042F#1P说得也是……\x02\x03",

            "要是对方赢了\x01",
            "胜负就定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x104,
        (
            "#030F#2P根据不同情况\x01",
            "也可能需要激流勇退。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A1")

    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #232
        0xB,
        (
            "客人，下一场比赛\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #233
        0x104,
        (
            "#033F#2P哦哦，该我上场了。\x02\x03",

            "#035F呼，那么我上了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #234
        0x106,
        "#050F#2P啊啊，靠你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #235
        0x101,
        (
            "#1009F#1P牛皮都吹过了\x01",
            "输了可不饶你哦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    Jump("loc_4A38")

    label("loc_3582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4A38")
    Call(2, 6)
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #236
        0xD,
        (
            "哟呵呵！\x01",
            "起手就是好兆头！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xD,
        (
            "呀～这下搞不好\x01",
            "能马上拿下一局啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #238
        0x105,
        (
            "#040F（菲利奥的情况\x01",
            "好像不错呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x104,
        (
            "#035F（哼，如果真是好牌\x01",
            "一般应该是沉默的哦。）\x02\x03",

            "#030F（对手要是放弃了\x01",
            "是不算赢的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x103,
        (
            "#020F（要是那孩子\x01",
            "察觉到就好了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x0, 0xA0, 0x64, 0x140, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x12C, 0xA0, 0x190, 0x140, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #241
        (
            "#1000F（……那么，就这样吧。）\x02\x03",

            "（以大牌为目标换牌，\x01",
            "  还是踏实保本……）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【只留一个对子换牌】\x01",      # 0
            "【目标红心同花】\x01",          # 1
        )
    )

    MenuEnd(0x4)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E4")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #242
        (
            "#1015F（还有续局，\x01",
            "  稳妥一点比较合理。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3A56")

    label("loc_39E4")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #243
        (
            "#1015F（还有续局，稳妥一点\x01",
            "  似乎比较合理……）\x02\x03",

            "#1002F（就反其道以大牌为目标试试看吧！）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3A56")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #244
        0xB,
        "要换牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ADE")

    ChrTalk(    #245
        0x101,
        "#1000F#2P嗯，换３张。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #246
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        "#1P我也换３张。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B2C")

    label("loc_3ADE")


    ChrTalk(    #248
        0x101,
        "#1000F#2P嗯，换２张。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #249
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xD,
        "#1P我换３张。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    label("loc_3B2C")

    OP_59()
    Call(2, 7)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C14")

    ChrTalk(    #251
        0x105,
        (
            "#040F（艾丝蒂尔……\x01",
            "  表情有点明显了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x104,
        (
            "#030F（嗯，这种程度\x01",
            "  大概还不至于被看穿……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x103,
        (
            "#025F（不过，万一牌不好\x01",
            "  她一定会表现在脸上的。）\x02\x03",

            "（她说自己弱，\x01",
            "  这也难怪了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D33")

    label("loc_3C14")

    OP_59()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #254
        0x105,
        (
            "#045F（艾、艾丝蒂尔……\x01",
            "  表情有点过于明显了……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x104,
        (
            "#031F（唔，要看出艾丝蒂尔\x01",
            "  在想什么简直易如反掌。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x103,
        (
            "#025F（唉，她还说自己弱，\x01",
            "  没想到这么离谱。）\x02\x03",

            "（这样怎么可能\x01",
            " 赢得了约修亚嘛。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D33")

    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #257
        0xD,
        (
            "#1P呼呼，不错哦～\x01",
            "来的就是我要的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #258
        0xD,
        (
            "#1P好了，挑战者们。\x01",
            "放马过来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x105,
        (
            "#045F（菲利奥\x01",
            "  也是老样子。）\x02\x03",

            "（到底有几分\x01",
            "  是真的呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 8)
    OP_0D()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #260
        0xB,
        "……要比牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_416F")
    OP_28(0x68, 0x1, 0x40)

    ChrTalk(    #261
        0x101,
        "#1007F#2P唔唔，我放弃。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xD,
        "#1P咦～要放弃吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xD,
        (
            "#1P嗯～难得\x01",
            "我凑得一手好牌，真可惜啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xB,
        (
            "那么，这边的客人。\x01",
            "之后就不能再放弃了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #265
        0x103,
        "#023F哎呀呀，放弃了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x104,
        "#030F唔，看来对自己的牌没什么自信啊。\x02",
    )

    CloseMessageWindow()

    def lambda_3F2A():

        label("loc_3F2A")

        TurnDirection(0x104, 0x101, 400)
        OP_48()
        Jump("loc_3F2A")

    QueueWorkItem2(0x104, 1, lambda_3F2A)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #267
        0x103,
        (
            "#021F没想到会放弃，\x01",
            "还挺成熟的嘛。\x02\x03",

            "还以为你一定\x01",
            "会生气争个输赢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        (
            "#1003F#4P我是很想比啦，\x01",
            "不过手气实在是差强人意。\x02\x03",

            "#1007F逞强押下去的话\x01",
            "输掉就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x103,
        (
            "#027F嗯，这也是一种判断嘛……\x02\x03",

            "#026F不过，这下\x01",
            "就被逼入绝境了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x105,
        (
            "#042F#1P嗯，因为规定是\x01",
            "只能放弃一次嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#1015F#4P啊，是哦……\x02\x03",

            "比想象的更严重啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #272
        0xB,
        (
            "客人，下一场比赛\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #273
        0x104,
        (
            "#033F#2P哦哦，该我上场了。\x02\x03",

            "#035F呼，那么我上了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #274
        0x103,
        "#020F#1P嗯，我期待着。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #275
        0x101,
        (
            "#1009F#4P说这种大话\x01",
            "输了可不饶你哦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_4A38")

    label("loc_416F")


    ChrTalk(    #276
        0x101,
        (
            "#1005F#2P当然了！\x01",
            "当然要比。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C1")
    OP_28(0x68, 0x1, 0x10)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 400)
    Sleep(500)

    ChrTalk(    #277
        0xD,
        "#1P咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xD,
        (
            "#1P这，这行吗？\x01",
            "我手里可是无上的好牌……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #279
        0x101,
        (
            "#1012F#2P是吗，无所谓啊。\x02\x03",

            "#1028F既然如此，\x01",
            "不如趁早放马过来吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #280
        0xB,
        "客人要怎样做？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #281
        0xD,
        "#1P唔～怎么办呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xD,
        (
            "#1P这手牌要比的话\x01",
            "倒是不一定输……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xD,
        "#1P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xD,
        "#1P……不，我放弃。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xB,
        (
            "那么，菲利奥先生。\x01",
            "以后的比赛中就不能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #286
        0x101,
        "#1018F#2P好，成功了！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    def lambda_4377():

        label("loc_4377")

        TurnDirection(0x104, 0x101, 400)
        OP_48()
        Jump("loc_4377")

    QueueWorkItem2(0x104, 1, lambda_4377)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #287
        0x103,
        (
            "#021F呵呵，看来\x01",
            "挺努力的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x105,
        "#040F#1P气势强硬看来是走对棋了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#1001F#4P嗯，总之\x01",
            "没输就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x104,
        (
            "#031F#2P呼，这就够了。\x02\x03",

            "这下对手\x01",
            "就被逼入绝境了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015F#4P啊，是哦……\x01",
            "因为只能放弃一次嘛。\x02\x03",

            "#1002F不过，还不算赢了，\x01",
            "之后也不可松懈哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x105,
        (
            "#042F#1P只要对方胜出一次，\x01",
            "胜负就定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x103,
        "#022F说得对，谨慎地上吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #294
        0xB,
        (
            "客人，下一场比赛\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #295
        0x104,
        (
            "#033F#2P哦哦，该我上场了。\x02\x03",

            "#035F呵，那么我上场了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #296
        0x103,
        "#020F#1P嗯，我期待着。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #297
        0x101,
        (
            "#1009F#4P说这种大话\x01",
            "输了可不饶你哦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_4A38")

    label("loc_45C1")

    OP_28(0x68, 0x1, 0x20)
    TurnDirection(0xD, 0x101, 400)
    Sleep(500)

    ChrTalk(    #298
        0xD,
        "#1P嗯～这样好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xD,
        (
            "#1P情况好像不太妙，\x01",
            "有什么绝招吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #300
        0x101,
        "#1019F#2P呜…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #301
        0x101,
        (
            "#1022F#2P少说废话，\x01",
            "要上就上吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #302
        0xB,
        "客人要怎样做？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #303
        0xD,
        "#1P唔～怎么办呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xD,
        (
            "#1P这手牌要比的话\x01",
            "倒是不一定输……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xD,
        "#1P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xD,
        "#1P……好，就这样比牌吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #307
        0x101,
        (
            "#1020F#2P（惨、惨了……！\x01",
            "  竟然将计就计了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)

    ChrTalk(    #308
        0xB,
        (
            "那么，从这边的客人开始\x01",
            "请展示手牌。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0xB, 400)
    Sleep(1000)
    OP_63(0xFFFF)
    Call(2, 22)
    OP_59()

    ChrTalk(    #309
        0xB,
        "菲利奥先生赢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xB,
        (
            "那么，按照事前的规定，\x01",
            "胜负已定。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #311
        0x101,
        "#1008F#2P啊，呜……………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #312
        0x105,
        "#045F#1P输、输了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x103,
        "#026F……你还真敢乱来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x104,
        (
            "#031F#2P哈哈哈。\x01",
            "哎呀，到底是艾丝蒂尔。\x02\x03",

            "输得真是豪爽啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_493B():
        OP_6D(29690, 0, 31480, 1000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_493B)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0x7E68, 0x0, 0x7B70, 0xBB8, 0x0)
    OP_8E(0x101, 0x7E86, 0x0, 0x779C, 0xBB8, 0x0)
    ClearChrFlags(0x101, 0x40)

    def lambda_4985():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4985)
    OP_43(0xD, 0x2, 0x1, 0x12)

    ChrTalk(    #315
        0xD,
        "#1P哇、哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#1016F#2P喂、喂！\x01",
            "拜托再来１次！\x02\x03",

            "求求你再比１次吧～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x103,
        (
            "#025F唉，那个大傻瓜……\x02\x03",

            "太丢人了\x01",
            "还是赶快抓回去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    Sleep(1000)
    Call(1, 15)
    Return()

    label("loc_4A38")

    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0x18, 255)
    TurnDirection(0x18, 0xD, 0)
    Sleep(1000)
    OP_6D(32073, 0, 31585, 0)
    SetChrPos(0x104, 33000, 0, 31870, 135)
    SetChrPos(0x101, 28570, 0, 31000, 90)
    SetChrPos(0xF7, 28850, 0, 32500, 90)
    SetChrPos(0x105, 27670, 0, 31940, 90)
    SetChrPos(0xD, 32530, 0, 29680, 79)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #318
        0xB,
        "那么，开始发放手牌。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Call(2, 9)
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #319
        0xD,
        "#1P……………我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xD,
        (
            "#1P呀……\x01",
            "感觉好像也转运了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xD,
        "#1P嗯～…………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #322
        0x101,
        (
            "#1002F（好、好像\x01",
            "真的很烦恼呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x105,
        "#042F（嗯嗯，表情都不一样了。）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4BF2")

    ChrTalk(    #324
        0x106,
        "#052F（说不定有什么招。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C27")

    label("loc_4BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4C27")

    ChrTalk(    #325
        0x103,
        (
            "#022F（应该是真的拿到了\x01",
            "  很不错的牌。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C27")

    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x0, 0x140, 0x64, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0xC8, 0x0, 0x12C, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x190, 0x0, 0x1F4, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x64, 0x0, 0xC8, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0xC8, 0x140, 0x12C, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #326
        (
            "#030F（那么，怎么办。）\x02\x03",

            "（直接进攻呢，\x01",
            "  还是迷惑对手……）\x02\x03",

            "（呵呵，两种看起来都很有趣。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【保留对子其余交换】\x01",      # 0
            "【保留对子只换一张】\x01",      # 1
        )
    )

    MenuEnd(0x4)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7A")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #327
        (
            "#030F（嗯，那么……\x01",
            "  还是老老实实上吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4FBB")

    label("loc_4F7A")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #328
        (
            "#030F（嗯，那么……\x01",
            "  还是迂回看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4FBB")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x104, 400)

    ChrTalk(    #329
        0xB,
        "要换牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5044")

    ChrTalk(    #330
        0x104,
        "#030F#2P嗯，麻烦换３张。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #331
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xD,
        "#1P我换２张。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5092")

    label("loc_5044")


    ChrTalk(    #333
        0x104,
        "#030F#2P只换１张，麻烦了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #334
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xD,
        "#1P我换２张。\x02",
    )

    CloseMessageWindow()

    label("loc_5092")

    OP_59()
    Call(2, 10)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #336
        0x101,
        (
            "#1002F（嗯～那表情……\x01",
            "　完全看不透。）\x02\x03",

            "（奥利维尔那家伙\x01",
            "　在想什么呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x105,
        (
            "#040F（呵呵，那也算是\x01",
            "　一种扑克脸呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xD)

    ChrTalk(    #338
        0xD,
        "#1P……好…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xD,
        "#1P嗯，没问题了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_51C7")

    ChrTalk(    #340
        0x106,
        (
            "#555F（和刚才不同，\x01",
            "　很保守的反应嘛。）\x02\x03",

            "（……拿到大牌了吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5216")

    label("loc_51C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5216")

    ChrTalk(    #341
        0x103,
        (
            "#022F（和刚才不同，\x01",
            "　非常保守的反应呢。）\x02\x03",

            "（会是拿到大牌了吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5216")

    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 20)
    OP_0D()
    TurnDirection(0xB, 0x104, 400)

    ChrTalk(    #342
        0xB,
        "……要比牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8F")
    OP_28(0x68, 0x1, 0x100)

    ChrTalk(    #343
        0x104,
        (
            "#031F#2P呼，我放弃了。\x02\x03",

            "因为『退却』也是出色的战略嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xD,
        "#1P可恶，放弃了吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xD, 400)

    ChrTalk(    #345
        0x104,
        (
            "#033F#2P哎呀？看起来很懊恼嘛。\x02\x03",

            "#031F要是浪费了\x01",
            "你难得的好牌，我道歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xD, 0x104, 400)
    Sleep(400)

    ChrTalk(    #346
        0xD,
        "#1P哪、哪里，也没什么懊恼的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xD,
        (
            "#1P我这里的牌\x01",
            "也不是太好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xB,
        (
            "那么，这下这边的客人\x01",
            "之后也不能再放弃了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(28820, 0, 31840, 0)
    OP_8C(0xD, 90, 0)
    OP_8C(0xB, 270, 0)
    OP_0D()

    ChrTalk(    #349
        0x101,
        "#1004F哎呀呀，放弃了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5413")

    ChrTalk(    #350
        0x106,
        "#050F#2P看来是感觉对方的牌比较好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5447")

    label("loc_5413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5447")

    ChrTalk(    #351
        0x103,
        (
            "#020F#2P嗯～看来\x01",
            "是觉得对方比较有希望。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5447")


    def lambda_544D():

        label("loc_544D")

        TurnDirection(0xF7, 0x104, 400)
        OP_48()
        Jump("loc_544D")

    QueueWorkItem2(0xF7, 1, lambda_544D)
    OP_8E(0x104, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0xF7, 0x1)

    ChrTalk(    #352
        0x104,
        (
            "#031F#4P嗨，各位⊙\x02\x03",

            "呼呼，看到了吗？\x01",
            "我那冷静的思考。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1015F不过，菲利奥\x01",
            "的手牌真那么好？\x02\x03",

            "要是比了的话\x01",
            "说不定就赢了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x104,
        (
            "#035F#4P呼，十之八九是不会错的。\x02\x03",

            "要是比了的话，\x01",
            "此时我们就在泪海里游泳了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        "#1016F少～来，又夸大其辞。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x105,
        (
            "#040F#1P不过，这下\x01",
            "双方各放弃一次了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_58D4")

    ChrTalk(    #357
        0x106,
        (
            "#050F#2P啊啊，没错。\x02\x03",

            "下场胜负\x01",
            "就是关键了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        (
            "#1002F嗯，是啊……我说。\x02\x03",

            "#1004F下场胜负\x01",
            "那不就是我上场！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #359
        0x106,
        "#555F#2P事到如今还迷糊什么呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x104,
        (
            "#030F#4P加油哦，艾丝蒂尔。\x02\x03",

            "我也会\x01",
            "在背后支持你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1016F支、支持有什么用……\x02\x03",

            "#1015F又不是支持我\x01",
            "就能抽到好牌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x104,
        "#031F#4P呵呵，这～可难说了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        (
            "#1019F什、什么啦？\x01",
            "话里有话的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x104,
        (
            "#032F#4P艾丝蒂尔，\x01",
            "我有一言相劝……\x02\x03",

            "与其为选牌而困惑，\x01",
            "不如全部扔掉的好哦。\x02\x03",

            "#031F喏，俗话不是这么说的吗？\x02\x03",

            "『与其重新涂奶油\x01",
            "  不如重新烤蛋糕』嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x101,
        (
            "#1007F没、没听说过啦，\x01",
            "哪有这么奇怪的俗话。\x02\x03",

            "#1002F不过，为什么\x01",
            "这么说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x104,
        (
            "#031F#4P不，只是直觉。\x01",
            "觉得这样比较好～的样子嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #367
        0xB,
        (
            "客人，到最后一局了。\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x106,
        "#050F#2P喂，看来差不多到时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x104,
        "#031F#4P呼，那么祝你好运。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1011F呜，嗯…………\x01",
            "#1015F（真令人介意～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A69")

    label("loc_58D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5A69")

    ChrTalk(    #371
        0x103,
        (
            "#026F#2P嗯嗯，就是这样。\x02\x03",

            "下场胜负\x01",
            "好好做个了结吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #372
        0x101,
        (
            "#1011F接着轮到雪拉姐了吗……\x02\x03",

            "#1001F嗯⊙感觉\x01",
            "好像赢得了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #373
        0x103,
        (
            "#027F是就好了……\x02\x03",

            "不过，这个\x01",
            "就要看空之女神的意思了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #374
        0xB,
        (
            "客人，到最后的比赛了。\x01",
            "准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x104,
        "#030F#4P嗯，看来到时间了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #376
        0x104,
        (
            "#030F#4P那么，雪拉。\x01",
            "就让我们见识一下你的手腕吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #377
        0x103,
        (
            "#021F呵呵……\x01",
            "希望能让你满意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A69")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0xD, 32398, 0, 30463, 90)
    OP_8C(0xB, 270, 0)
    Jump("loc_6084")

    label("loc_5A8F")


    ChrTalk(    #378
        0x104,
        (
            "#031F#2P哼，当然了。\x02\x03",

            "我的辞典里\x01",
            "可没有『退却』两字。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #379
        0xB,
        "客人要怎样做？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xD,
        "#1P啊啊，我接受。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 400)

    ChrTalk(    #381
        0xB,
        (
            "那么，从这边的客人开始\x01",
            "请展示手牌。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 21)
    OP_59()

    ChrTalk(    #382
        0xB,
        "菲利奥先生赢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xB,
        (
            "那么，按照事前的规定，\x01",
            "胜负已定。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #384
        0x104,
        (
            "#035F#2P呵呵，胜败乃时运。\x01",
            "若是败北也没有办法……\x02\x03",

            "#031F可、可是，难道是错觉？\x02\x03",

            "从刚才开始背后\x01",
            "就一直感到一股异样的压力。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(    #385
        0x101,
        (
            "#1009F#1P那、那个三流音乐家～～\x02\x03",

            "奥利维尔～你\x01",
            "心知肚明的～吧～～～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #386
        0x105,
        "#045F#1P艾、艾丝蒂尔，冷静点。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5DBE")

    ChrTalk(    #387
        0x106,
        (
            "#053F#2P你还好意思说。\x02\x03",

            "开始前，拼命发牢骚的\x01",
            "到底是谁？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #388
        0x101,
        "#1019F#1P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x106,
        (
            "#057F#2P我们之所以会输\x01",
            "又不光是那家伙的错。\x02\x03",

            "有空起内讧，\x01",
            "还不如考虑一下怎么对委托人解释。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #390
        0x101,
        (
            "#1007F#1P是、是哦……\x01",
            "工作失败了呢。\x02\x03",

            "唉，没脸\x01",
            "去见委托人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6069")

    label("loc_5DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6069")
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F3E")

    ChrTalk(    #391
        0x103,
        (
            "#027F#2P哎呀，艾丝蒂尔。\x01",
            "你有立场这么说吗？\x02\x03",

            "你不是也\x01",
            "首战就放弃了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #392
        0x101,
        "#1019F#1P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x103,
        (
            "#025F#2P正因为你那时候放弃了，\x01",
            "现在才不得不比的哦？\x02\x03",

            "你自己也有一半的原因，\x01",
            "就别胡乱指责别人了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #394
        0x101,
        (
            "#1007F#1P知、知道啦。\x01",
            "我知道了啦。\x02\x03",

            "唉，话说回来\x01",
            "该怎么向委托人道歉才好呢。\x02\x03",

            "#1014F啊～早知这样\x01",
            "当时就比了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6069")

    label("loc_5F3E")


    ChrTalk(    #395
        0x103,
        (
            "#027F#2P哎呀，艾丝蒂尔。\x01",
            "你有立场这么说吗？\x02\x03",

            "开始之前，是谁说\x01",
            "不会打牌的啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #396
        0x101,
        "#1019F#1P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x103,
        (
            "#026F#2P我们会输\x01",
            "并不仅是奥利维尔的原因。\x02\x03",

            "有空发牢骚，\x01",
            "还不如考虑一下怎么对委托人解释。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #398
        0x101,
        (
            "#1007F#1P是、是哦……\x01",
            "工作失败了呢。\x02\x03",

            "唉，没脸\x01",
            "去见委托人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6069")

    OP_28(0x68, 0x1, 0x80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(1, 15)
    Return()

    label("loc_6084")

    OP_6D(32073, 0, 31585, 0)
    SetChrPos(0x105, 27670, 0, 31940, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_60E3")
    SetChrPos(0x101, 33000, 0, 31870, 135)
    SetChrPos(0xF7, 28570, 0, 31000, 90)
    SetChrPos(0x104, 28850, 0, 32500, 90)
    Jump("loc_611D")

    label("loc_60E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_611D")
    SetChrPos(0xF7, 33000, 0, 31870, 135)
    SetChrPos(0x104, 28850, 0, 32500, 90)
    SetChrPos(0x101, 28570, 0, 31000, 90)

    label("loc_611D")

    SetChrPos(0xD, 32530, 0, 29680, 79)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #399
        0xB,
        "两位都准备好了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xB,
        "那么，开始最后一局了。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7A04")
    Call(2, 11)
    OP_59()
    Sleep(400)
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #401
        0x101,
        (
            "#1002F#2P（菲利奥的\x01",
            "情况怎样？）\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 21)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #402
        0x105,
        (
            "#045F（看、看起来\x01",
            "  情况很古怪。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x106,
        "#050F（啊啊，好像转运了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x104,
        (
            "#030F（来吧，艾丝蒂尔该怎么办呢。）\x02\x03",

            "（要是我刚刚的意思\x01",
            "  她能听懂就好了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x190, 0x0, 0x1F4, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x0, 0xA0, 0x64, 0x140, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0xC8, 0x0, 0x12C, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    TurnDirection(0x101, 0xB, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #405
        (
            "#1002F（不妙啊……\x01",
            "  菲利奥看来形势大好。）\x02\x03",

            "（即使凑成同花\x01",
            "  说不定对方还有更厉害的。）\x02\x03",

            "#1015F（话虽如此，除了同花\x01",
            "  也没别的牌好凑……）\x02\x03",

            "#1022F（啊～真像奥利维尔说的，\x01",
            "  简直想全部扔掉换牌了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【目标方块同花】\x01",      # 0
            "【交换全部手牌】\x01",      # 1
        )
    )

    MenuEnd(0x4)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66AF")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #406
        (
            "#1007F（嗯，可是孤注一掷的话\x01",
            "  无疑也是最佳选择哦。）\x02\x03",

            "（无谓的强求也没什么意义。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_6736")

    label("loc_66AF")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #407
        (
            "#1002F（即使完成了同花，\x01",
            "  最后输了也没有意义。）\x02\x03",

            "#1007F（嗯……这里就孤注一掷\x01",
            "  试着遵从奥利维尔的意见吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6736")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #408
        0xB,
        "要换牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D34")

    ChrTalk(    #409
        0x101,
        "#1002F#2P嗯，换２张。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #410
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xD,
        "#1P哦，我只换１张。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 12)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #412
        0x105,
        (
            "#040F（啊，艾丝蒂尔\x01",
            "  似乎也转运了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x104,
        (
            "#030F#2P（那个表情看来\x01",
            "  好像是相当不错的牌……）\x02\x03",

            "#034F（不过，居然连我们\x01",
            "  旁观者都如此一目了然。）\x02\x03",

            "（艾丝蒂尔的表情\x01",
            "  简直像手旗信号一样嘛。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x106,
        (
            "#551F（虽然她早说过不擅长玩牌，\x01",
            "  我看问题可不在这里……）\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(1, 14)
    OP_59()
    Call(2, 19)
    OP_59()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xD, 400)
    Sleep(1000)

    ChrTalk(    #415
        0x101,
        (
            "#1020F#2P同、同花大顺什么的……咦！？\x02\x03",

            "那不是最强的牌吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #416
        0x106,
        (
            "#055F喂、喂喂……\x01",
            "怎么偏偏是那个啊。\x02\x03",

            "那种牌一般怎么可能凑得出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x105,
        "#042F真的比不过……了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x104,
        (
            "#031F哈哈哈。\x01",
            "这实在是束手无策了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #419
        0xB,
        "……客人也请开牌。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xB,
        (
            "不展示手牌的话，\x01",
            "胜负是不清楚的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #421
        0x101,
        (
            "#1016F#2P不、不过，这次\x01",
            "已经是一目了然了……\x02",
        )
    )

    CloseMessageWindow()
    Call(2, 16)
    OP_59()

    ChrTalk(    #422
        0xB,
        "唔，确实……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #423
        0xB,
        (
            "那么这次比赛───\x01",
            "菲利奥先生赢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xD,
        (
            "#1P哈哈哈。\x01",
            "哎呀～这是当然的结果嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xD,
        (
            "#1P你们也很努力了\x01",
            "就是选错了对手。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #426
        0x105,
        "#043F#5P唉，输了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x104,
        (
            "#030F#2P唔～真可惜啊。\x01",
            "就差一口气了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x106,
        "#053F#1P唉，对手运气太好也没办法。\x02",
    )

    CloseMessageWindow()

    def lambda_6BE9():

        label("loc_6BE9")

        TurnDirection(0x104, 0x101, 400)
        OP_48()
        Jump("loc_6BE9")

    QueueWorkItem2(0x104, 1, lambda_6BE9)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #429
        0x101,
        "#1007F#4P抱歉，输了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x106,
        (
            "#050F#1P别跟我们道歉啊。\x01",
            "输了是全体人员的责任。\x02\x03",

            "要道歉的话，\x01",
            "就去对这件工作的委托人道歉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x101,
        (
            "#1003F#4P是、是哦……\x01",
            "工作失败了啊。\x02\x03",

            "#1007F唉，没脸见人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x106,
        (
            "#552F#1P啊啊，话虽如此\x01",
            "还是必须去见的。\x02\x03",

            "……这是游击士职业的尊严啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0x68, 0x1, 0x200)
    Call(1, 15)
    Return()

    label("loc_6D34")


    ChrTalk(    #433
        0x101,
        (
            "#1002F#2P嗯…………\x02\x03",

            "#1007F……５张全换哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xB,
        "…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_6D85():

        label("loc_6D85")

        TurnDirection(0x101, 0x104, 400)
        OP_48()
        Jump("loc_6D85")

    QueueWorkItem2(0x101, 1, lambda_6D85)

    ChrTalk(    #435
        0x101,
        "#1009F#2P（看，照你说的做了啦。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x104,
        "#031F（呼呼，判断得好。）\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0xB)
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #437
        0xB,
        "……那么，客人呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xD,
        "#1P哦，我只换１张。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #439
        0x101,
        "#1002F#2P（……想，想干什么？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x104,
        "#035F#2P（呼…………）\x02",
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_D9(0x0, "CTI00130")
    OP_22(0x21F, 0x0, 0x64)
    Sleep(2000)
    OP_D9(0x1)
    FadeToBright(300, 0)
    Sleep(400)
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #441
        0x104,
        "#035F#2P……呼～……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #442
        "\x07\x05奥利维尔朝发牌者的耳朵吹了口气。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_9E(0xB, 0xF, 0x0, 0x12C, 0x1388)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xB, 0x1, 0x1, 0xD)

    ChrTalk(    #443
        0xB,
        "呜，呜哇啊啊！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #444
        0xB,
        "您、您干什么呢！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x104,
        (
            "#031F#2P哈哈哈，失礼了。\x01",
            "哎呀，不觉得紧张得受不了了嘛。\x02\x03",

            "只是稍微打个岔，\x01",
            "缓和一下气氛嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    TurnDirection(0xD, 0x104, 400)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x5DC, 0x1388)

    ChrTalk(    #446
        0x101,
        "#1022F#2P（那、那个呆子～～～～～！！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xB,
        "那你已经达到目的了吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xB,
        (
            "好了，快下去！\x01",
            "游戏都进行不下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x104,
        "#030F#2P呼，那么打扰了。\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0xC)
    Sleep(2000)

    ChrTalk(    #450
        0x101,
        (
            "#1009F#2P（………………～～唔！！）\x02\x03",

            "（呜～相信那呆子的我\x01",
            "  也真够蠢的。）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_8E(0xB, 0x88C2, 0x0, 0x7684, 0x7D0, 0x0)
    OP_8C(0xB, 270, 400)
    Sleep(500)

    ChrTalk(    #451
        0xB,
        "那、那么，回到正题……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #452
        0xB,
        "……客人是换５张？\x02",
    )

    CloseMessageWindow()

    def lambda_71D6():
        TurnDirection(0x18, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_71D6)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #453
        0x101,
        "#1007F#2P呜呜……是啦………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #454
        0xB,
        "那，我是１张……好了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #455
        0xD,
        (
            "#1P呼呼呼……\x01",
            "好，来吧～！\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 14)
    OP_59()
    Call(2, 19)
    OP_59()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xD, 400)
    Sleep(1000)

    ChrTalk(    #456
        0x101,
        (
            "#1020F#2P同、同花大顺什么的……咦！？\x02\x03",

            "那不是最强的牌吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #457
        0x106,
        (
            "#052F喂、喂喂……\x01",
            "怎么偏偏是那个啊。\x02\x03",

            "那种牌一般怎么可能凑得出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x105,
        "#042F穷途末路……了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x104,
        (
            "#035F呼呼……\x02\x03",

            "这～个嘛，可难说哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x105,
        "#044F咦……？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #461
        0xB,
        "……客人也请开牌。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xB,
        (
            "不展示手牌的话，\x01",
            "胜负是不清楚的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #463
        0x101,
        (
            "#1007F#2P……好好，开牌了。\x02\x03",

            "不过，面对那种手牌\x01",
            "开牌也没什么意义了……\x02",
        )
    )

    CloseMessageWindow()
    Call(2, 18)
    OP_59()

    ChrTalk(    #464
        0xB,
        "……确实没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xB,
        "而且，还是黑桃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xB,
        (
            "唔，那么这边的牌\x01",
            "比菲利奥先生的更大。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #467
        0xD,
        "#1P骗、骗人的吧！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xB,
        (
            "这场比赛───\x01",
            "是各位赢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x14)

    ChrTalk(    #469
        0x101,
        (
            "#1004F#2P赢、赢了……！\x02\x03",

            "赢了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_7522():
        OP_95(0x101, 0x0, 0x3E8, 0x0, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7522)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #470
        0x101,
        "#1001F#3S#2P呀呵～～赢了！！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x101, 0x1, 0x1, 0x13)

    ChrTalk(    #471
        0xB,
        (
            "……这是赌金。\x01",
            "请确认。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #472
        "\x07\x00得到了\x07\x04２０００\x07\x00米拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(    #473
        0x105,
        "#044F#5P赢、赢了哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x104,
        (
            "#031F哈哈哈。\x01",
            "简直是大逆转呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #475
        0x106,
        "#057F#1P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x106, 400)
    Sleep(1000)

    ChrTalk(    #476
        0x104,
        "#031F怎、怎么了？阿加特兄。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x106,
        (
            "#053F#1P……哼，原来如此啊。\x02\x03",

            "怪不得会做出\x01",
            "那种可疑的举动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0x104,
        "#031F哈哈，你说什～么呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x106,
        (
            "#551F#1P算了……\x01",
            "就当没看见吧。\x02\x03",

            "因为这次就是\x01",
            "靠那个才赢的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x104,
        (
            "#030F呵呵……\x01",
            "能帮上忙是我的荣幸。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_44(0x101, 0x1)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)

    ChrTalk(    #481
        0x101,
        (
            "#1001F#4P嘿嘿～久等了～⊙\x02\x03",

            "好了，赶快去报告…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #482
        0x101,
        (
            "#1019F#4P你、你们两个……\x01",
            "干嘛在这大眼瞪小眼啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #483
        0x104,
        (
            "#035F#2P呼，你都看到啦。\x02\x03",

            "阿加特想强迫我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0x106,
        (
            "#055F#1P白、白痴啊！！\x01",
            "少在这说胡话！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x106, 400)

    ChrTalk(    #485
        0x104,
        (
            "#031F#2P哈哈哈。\x01",
            "有什么好掩饰的嘛。\x02\x03",

            "真是的～阿加特害·羞·了㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #486
        0x101,
        "#1020F#4P……哇、哇啊…\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #487
        0x106,
        (
            "#055F#1P别、别当真啊！\x02\x03",

            "好、好啦！\x01",
            "赶快去报告啦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0xD, 0x1)
    OP_28(0x68, 0x1, 0x400)
    Call(1, 16)
    Return()

    label("loc_7A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_89A5")
    Call(2, 14)
    OP_59()
    Sleep(400)
    TurnDirection(0x103, 0xD, 400)

    ChrTalk(    #488
        0x103,
        (
            "#027F#2P（好了……\x01",
            "对方的情况怎样？）\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 21)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #489
        0x105,
        (
            "#045F（看、看起来\x01",
            "  情况很古怪。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0x101,
        "#1002F（嗯，看来有好牌。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x104,
        (
            "#030F（好了，雪拉\x01",
            "  打算怎样出？）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x190, 0x140, 0x1F4, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x64, 0x0, 0xC8, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x0, 0x140, 0x64, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    TurnDirection(0x103, 0xB, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #492
        (
            "#022F（那个样子的话\x01",
            "对方是来了大牌了……）\x02\x03",

            "（这么说，普通的手牌\x01",
            "  输的几率很大。）\x02\x03",

            "（这里还是应该追求\x01",
            "  理想形态的同花顺吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【只留对Ａ其余交换】\x01",        # 0
            "【除黑桃以外全部交换】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ECE")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #493
        (
            "#022F（话虽如此……\x01",
            "  放弃对Ａ也不太可能。）\x02\x03",

            "（……好，就用这方法。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_7ECE")

    label("loc_7ECE")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #494
        0xB,
        "要换牌吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F25")

    ChrTalk(    #495
        0x103,
        "#022F#2P麻烦换３张。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F3F")

    label("loc_7F25")


    ChrTalk(    #496
        0x103,
        "#022F#2P麻烦换２张。\x02",
    )

    CloseMessageWindow()

    label("loc_7F3F")

    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #497
        0xB,
        "……客人您呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xD,
        "#1P哦，我只换１张。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 15)
    OP_59()
    Call(1, 14)
    OP_59()
    Call(2, 19)
    OP_59()

    ChrTalk(    #499
        0x103,
        "#022F#2P…………………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #500
        0x101,
        (
            "#1020F#2P同、同花大顺什么的……咦！？\x02\x03",

            "那不是最强的牌吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x105,
        "#042F穷途末路……了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x104,
        "#032F#2P唔……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #503
        0xB,
        "……客人也请开牌。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0xB,
        (
            "不展示手牌的话，\x01",
            "胜负是不清楚的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8309")

    ChrTalk(    #505
        0x103,
        (
            "#025F#1P嗯，意料之中，\x01",
            "这次已经一目了然了……\x02",
        )
    )

    CloseMessageWindow()
    Call(2, 17)
    OP_59()

    ChrTalk(    #506
        0xB,
        "唔，确实……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #507
        0xB,
        (
            "那么这次比赛───\x01",
            "菲利奥先生赢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xD,
        (
            "#1P哈哈哈。\x01",
            "哎呀～这是当然的结果嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xD,
        (
            "#1P你们也很努力了\x01",
            "就是选错了对手。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #510
        0x105,
        "#043F#5P唉，输了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0x104,
        (
            "#030F#2P唔～真可惜啊。\x01",
            "虽说还是有机会的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81D4():

        label("loc_81D4")

        TurnDirection(0x104, 0x103, 400)
        OP_48()
        Jump("loc_81D4")

    QueueWorkItem2(0x104, 1, lambda_81D4)
    OP_8E(0x103, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #512
        0x103,
        (
            "#025F抱歉，我输了。\x02\x03",

            "虽然有好牌，\x01",
            "但我不够坚持。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x101,
        (
            "#1003F#1P哪里，连雪拉姐\x01",
            "都输了的话就没办法了。\x02\x03",

            "#1015F不过，这下\x01",
            "委托就失败了。\x02\x03",

            "嗯～该拿什么脸\x01",
            "去见委托人才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x103,
        (
            "#026F即使没脸去见\x01",
            "也是非见不可的哦。\x02\x03",

            "嗯，这职业的痛苦就在于此。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0x68, 0x1, 0x800)
    Call(1, 15)
    Return()

    label("loc_8309")


    ChrTalk(    #515
        0x103,
        "#021F#2P呵呵，说得没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x103, 400)

    ChrTalk(    #516
        0xD,
        "#1P哼，开也没用的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xD,
        (
            "#1P因为我这可是\x01",
            "最强手牌啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x103,
        (
            "#027F#2P哎呀……\x01",
            "那又怎样？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_D9(0x0, "CTI00120")
    OP_22(0x21F, 0x0, 0x64)
    Sleep(2000)
    OP_D9(0x1)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #519
        0x101,
        "#1004F哎，咦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #520
        0x105,
        "#044F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x101,
        (
            "#1015F刚才，雪拉姐的手……\x02\x03",

            "……………………………\x02\x03",

            "#1016F……抱、抱歉。\x01",
            "看来是我错觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x105,
        "#040F？？？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_8C(0x105, 90, 0)
    OP_0D()
    Call(2, 18)
    OP_59()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #523
        0xD,
        "#1P怎、怎么会！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0xB,
        "……确实，看来没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0xB,
        "而且，还是黑桃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0xB,
        (
            "唔，那么这边的牌\x01",
            "比菲利奥先生的更大。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_8554():
        OP_95(0xD, 0x0, 0x3E8, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8554)
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #527
        0xD,
        "#1P骗、骗人的吧！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0xB,
        (
            "这场比赛───\x01",
            "是各位赢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x14)

    ChrTalk(    #529
        0x103,
        "#025F#2P呼，哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #530
        0xB,
        (
            "……这是赌金。\x01",
            "请确认。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #531
        "\x07\x00得到了\x07\x04２０００\x07\x00米拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(    #532
        0x101,
        (
            "#1008F#1P啊哈哈……\x01",
            "好、好像赢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x105,
        "#045F#5P难、难以置信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0x104,
        (
            "#031F哈哈哈。\x01",
            "简直是大逆转呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_86C2():

        label("loc_86C2")

        TurnDirection(0x104, 0x103, 400)
        OP_48()
        Jump("loc_86C2")

    QueueWorkItem2(0x104, 1, lambda_86C2)
    OP_8E(0x103, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #535
        0x101,
        (
            "#1001F#1P雪拉姐，辛苦了！\x02\x03",

            "居然能在那里反败为胜，\x01",
            "真是～姐姐最可靠了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0x104,
        "#031F#2P呵呵，长见识了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #537
        0x103,
        (
            "#027F好久没做了有点紧张……\x02\x03",

            "#525F嗯，还好没岀差错。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #538
        0x101,
        "#1011F#1P嗯？你们说什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #539
        0x104,
        "#035F#2P呵，这是大人的私事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0x105,
        "#040F#5P？？？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #541
        0x101,
        (
            "#1004F#1P…………啊………\x02\x03",

            "……难、难不成！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #542
        0x103,
        (
            "#023F哎呀，你没发现吗？\x02\x03",

            "还以为你和奥利维尔\x01",
            "都能看穿呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #543
        0x101,
        (
            "#1022F#1P败、败给你了～～\x02\x03",

            "怪不得那个时候\x01",
            "觉得怪怪的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x103,
        (
            "#021F呵呵，所谓蛇行蛇道嘛。\x02\x03",

            "#020F……那么，赶快\x01",
            "去委托人那里报告吧。\x02\x03",

            "虽说似乎没被拆穿，\x01",
            "但还是不便久留吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0x101,
        (
            "#1002F#1P确、确实如此……\x02\x03",

            "好，赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0xD, 0x1)
    OP_28(0x68, 0x1, 0x1000)
    Call(1, 16)

    label("loc_89A5")

    Return()

    # Function_1_45F end

    def Function_2_89A6(): pass

    label("Function_2_89A6")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x7260, 0x0, 0x7F8A, 0x41A, 0x0)
    OP_8E(0xFE, 0x7A1C, 0x0, 0x77E2, 0x41A, 0x0)
    Return()

    # Function_2_89A6 end

    def Function_3_89D6(): pass

    label("Function_3_89D6")

    OP_8C(0xFE, 180, 400)
    Sleep(200)
    OP_8E(0xFE, 0x75D0, 0x0, 0x80AC, 0x3E8, 0x0)
    OP_8E(0xFE, 0x7A12, 0x0, 0x7C6A, 0x3E8, 0x0)
    Return()

    # Function_3_89D6 end

    def Function_4_8A0B(): pass

    label("Function_4_8A0B")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x7134, 0x0, 0x7C88, 0x41A, 0x0)
    OP_8E(0xFE, 0x75DA, 0x0, 0x7814, 0x41A, 0x0)
    Return()

    # Function_4_8A0B end

    def Function_5_8A3B(): pass

    label("Function_5_8A3B")

    OP_8C(0xFE, 180, 400)
    Sleep(200)
    OP_8E(0xFE, 0x7468, 0x0, 0x7D64, 0x3E8, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_5_8A3B end

    def Function_6_8A63(): pass

    label("Function_6_8A63")

    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_6_8A63 end

    def Function_7_8A6B(): pass

    label("Function_7_8A6B")

    TurnDirection(0xFE, 0x19, 400)
    Return()

    # Function_7_8A6B end

    def Function_8_8A73(): pass

    label("Function_8_8A73")

    TurnDirection(0xFE, 0x104, 400)
    Return()

    # Function_8_8A73 end

    def Function_9_8A7B(): pass

    label("Function_9_8A7B")

    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_9_8A7B end

    def Function_10_8A83(): pass

    label("Function_10_8A83")

    OP_69(0xD, 0x7D0)
    Return()

    # Function_10_8A83 end

    def Function_11_8A8B(): pass

    label("Function_11_8A8B")

    OP_8E(0x104, 0x79C2, 0x0, 0x7FC6, 0x7D0, 0x0)
    OP_8E(0x104, 0x8868, 0x0, 0x7DFD, 0x7D0, 0x0)
    OP_8E(0x104, 0x8949, 0x0, 0x792F, 0x7D0, 0x0)
    Return()

    # Function_11_8A8B end

    def Function_12_8AC8(): pass

    label("Function_12_8AC8")

    OP_8E(0x104, 0x8868, 0x0, 0x7DFD, 0x7D0, 0x0)
    OP_8E(0x104, 0x79C2, 0x0, 0x7FC6, 0x7D0, 0x0)
    OP_8E(0x104, 0x70B2, 0x0, 0x7EF4, 0x7D0, 0x0)
    TurnDirection(0x104, 0x101, 400)
    Return()

    # Function_12_8AC8 end

    def Function_13_8B0C(): pass

    label("Function_13_8B0C")

    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_8B29():
        TurnDirection(0xB, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8B29)

    def lambda_8B37():
        TurnDirection(0x18, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8B37)
    OP_8F(0xB, 0x88D5, 0x0, 0x7134, 0x1F40, 0x0)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Return()

    # Function_13_8B0C end

    def Function_14_8B66(): pass

    label("Function_14_8B66")

    Sleep(1000)

    ChrTalk(    #546
        0xB,
        "……牌凑好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xB,
        "那么─────\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0xB,
        "────请亮岀手牌。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #549
        0xD,
        "好，从我开始开吧。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_14_8B66 end

    def Function_15_8BCD(): pass

    label("Function_15_8BCD")

    OP_28(0x68, 0x4, 0x40)
    OP_28(0x68, 0x4, 0x80)
    OP_22(0x106, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #550
        "\x07\x02任务【急聘牌技高手】\x07\x00失败了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4A(0xE, 0)
    OP_4A(0xE, 0)
    SetChrPos(0x101, 5600, 250, 33020, 0)
    SetChrPos(0xF7, 4770, 250, 32659, 0)
    SetChrPos(0x104, 5560, 250, 31520, 0)
    SetChrPos(0x105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0xC)
    Sleep(400)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #551
        0x101,
        (
            "#1003F……就是这样…………\x02\x03",

            "经过苦战，\x01",
            "还是失败了。\x02\x03",

            "#1007F……真是对不起。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8D23")

    ChrTalk(    #552
        0x106,
        (
            "#053F抱歉，无可辩驳。\x02\x03",

            "关于这件事\x01",
            "完全怪我们力量不足。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D62")

    label("loc_8D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8D62")

    ChrTalk(    #553
        0x103,
        (
            "#025F无可辩驳了。\x02\x03",

            "关于这件事\x01",
            "完全怪我们力量不足。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D62")


    ChrTalk(    #554
        0xE,
        "是吗……不行啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #555
        0xE,
        (
            "唉，不过，这也没办法。\x01",
            "这个什么的纯粹靠运气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0xE,
        (
            "当然，游击士们\x01",
            "请在别的事情上多加努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x101,
        "#1007F真、真丢脸……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x104,
        (
            "#035F呼，确实我们\x01",
            "没帮上忙……\x02\x03",

            "#030F但是，您丈夫的事\x01",
            "我想不必担心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0x8)
    OP_43(0x105, 0x1, 0x1, 0x8)
    OP_43(0xE, 0x1, 0x1, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8E6A")
    OP_43(0x106, 0x1, 0x1, 0x8)
    Jump("loc_8E78")

    label("loc_8E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8E78")
    OP_43(0x103, 0x1, 0x1, 0x8)

    label("loc_8E78")


    ChrTalk(    #559
        0xE,
        "咦？为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0x101,
        "#1004F我、我说奥利维尔……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8EE3")

    ChrTalk(    #561
        0x106,
        (
            "#050F嗯，没什么不好啊。\x02\x03",

            "听他想说什么吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F17")

    label("loc_8EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8F17")

    ChrTalk(    #562
        0x103,
        (
            "#020F嗯，没关系吧。\x02\x03",

            "听听他想说什么吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F17")


    ChrTalk(    #563
        0x101,
        "#1015F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #564
        0x104,
        (
            "#035F是这样的，大部分娱乐场\x01",
            "都会有个王牌类的人物。\x02\x03",

            "平时不会去店里，\x01",
            "但却是那个店里最强的。\x02\x03",

            "#030F不过，在我看来……\x02\x03",

            "这个店里，那个人物\x01",
            "似乎还没出现呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9006")

    ChrTalk(    #565
        0x106,
        (
            "#052F也就是说，还没到\x01",
            "那家伙出场的时候吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903D")

    label("loc_9006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_903D")

    ChrTalk(    #566
        0x103,
        (
            "#023F也就是说，还没到\x01",
            "那个人出场的时候吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_903D")

    TurnDirection(0x104, 0xF7, 400)

    ChrTalk(    #567
        0x104,
        (
            "#030F啊啊，因为我们输了，\x01",
            "所以我想很快就会登场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x101,
        "#1015F王牌……啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0xE,
        (
            "唉，真是\x01",
            "这样就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0xE,
        (
            "这个人的话……\x01",
            "可以相信吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_912C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_912C)

    def lambda_913A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_913A)

    def lambda_9148():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9148)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #571
        0x101,
        (
            "#1016F唔，嗯～怎么说呢。\x02\x03",

            "相信不相信\x01",
            "就看您自己的判断了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0xE,
        (
            "总之，我在这里\x01",
            "再稍微等等看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #573
        0xE,
        (
            "不管会不会\x01",
            "像这个人说的一样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_921C")

    ChrTalk(    #574
        0x106,
        (
            "#050F既然如此，\x01",
            "我们就先走了。\x02\x03",

            "今天真是抱歉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9259")

    label("loc_921C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9259")

    ChrTalk(    #575
        0x103,
        (
            "#020F既然如此，\x01",
            "我们就先走了。\x02\x03",

            "今天真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9259")


    ChrTalk(    #576
        0xE,
        "我相信你们都尽力了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0xE,
        (
            "那么，游击士们。\x01",
            "以后有事再麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0x101,
        "#1006F嗯，请随时吩咐。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_8C(0xE, 180, 0)
    OP_4B(0xE, 255)
    OP_4B(0xE, 255)
    OP_4B(0xD, 255)
    OP_4B(0x18, 255)
    OP_4B(0xB, 255)
    OP_8C(0x18, 270, 0)
    OP_8C(0xB, 270, 0)
    Return()

    # Function_15_8BCD end

    def Function_16_92E9(): pass

    label("Function_16_92E9")

    OP_28(0x68, 0x4, 0x10)
    OP_4A(0xE, 0)
    SetChrPos(0x101, 5600, 250, 33020, 0)
    SetChrPos(0xF7, 4770, 250, 32659, 0)
    SetChrPos(0x104, 5560, 250, 31520, 0)
    SetChrPos(0x105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0xC)
    Sleep(400)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #579
        0xE,
        "真的……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #580
        0xE,
        (
            "呵，真的\x01",
            "赢了我丈夫吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0x101,
        (
            "#1006F嗯，虽然挺辛苦\x01",
            "总算还是成功了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_93FE")

    ChrTalk(    #582
        0x106,
        (
            "#050F这是拿回来的钱。\x02\x03",

            "１０００加倍\x01",
            "正好２０００米拉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9441")

    label("loc_93FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9441")

    ChrTalk(    #583
        0x103,
        (
            "#020F这是拿回来的钱。\x02\x03",

            "１０００加倍\x01",
            "正好２０００米拉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9441")


    ChrTalk(    #584
        0xE,
        (
            "啊，不用了。\x01",
            "请你们收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0xE,
        (
            "就当作是补偿那\x01",
            "太过便宜的报酬吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x101,
        (
            "#1011F咦？可以吗？\x02\x03",

            "既然您都这样说了,\x01",
            "那我们就感激地收下了……\x02\x03",

            "#1015F……不过，真的\x01",
            "这样就行了吗？\x02\x03",

            "您丈夫好像\x01",
            "并没怎么吸取教训哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #587
        0xE,
        (
            "之后我想娱乐场的人\x01",
            "会想办法解决的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #588
        0xE,
        (
            "他们也是专业的，\x01",
            "不会让我丈夫一直赢下去的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_95C2")

    ChrTalk(    #589
        0x106,
        (
            "#051F呵，那倒是。\x02\x03",

            "#050F既然如此\x01",
            "我们这就告辞了……\x02\x03",

            "……没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9614")

    label("loc_95C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9614")

    ChrTalk(    #590
        0x103,
        (
            "#021F呵呵，那倒也是。\x02\x03",

            "#020F既然如此\x01",
            "我们就先走了……\x02\x03",

            "……没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9614")


    ChrTalk(    #591
        0xE,
        (
            "嗯，可以了。\x01",
            "你们已经做得够多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0xE,
        (
            "这样胡来的委托\x01",
            "游击士也在认真帮我们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0xE,
        "……对你们有点改观了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0x101,
        (
            "#1001F嘿嘿，谢谢。\x02\x03",

            "从今以后也请继续努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0xE,
        (
            "那么，游击士们。\x01",
            "以后有事再麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9706")

    ChrTalk(    #596
        0x106,
        "#051F啊啊，随时吩咐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_972A")

    label("loc_9706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_972A")

    ChrTalk(    #597
        0x103,
        "#020F嗯嗯，请随时吩咐。\x02",
    )

    CloseMessageWindow()

    label("loc_972A")

    OP_A2(0x7)
    AddMira(2000)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #598
        "\x07\x02任务【急聘牌技高手】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0xE, 255)
    OP_4B(0xD, 255)
    OP_4B(0x18, 255)
    OP_4B(0xB, 255)
    OP_8C(0x18, 270, 0)
    OP_8C(0xB, 270, 0)
    Return()

    # Function_16_92E9 end

    def Function_17_97A1(): pass

    label("Function_17_97A1")

    OP_8E(0xB, 0x8944, 0x0, 0x6FAE, 0x3E8, 0x0)
    TurnDirection(0x18, 0xB, 400)
    OP_4A(0x18, 255)
    OP_A5(0x10)

    def lambda_97C9():
        OP_8C(0x18, 270, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_97C9)
    OP_8E(0xB, 0x88C2, 0x0, 0x7684, 0x3E8, 0x0)
    OP_8C(0xB, 270, 400)
    Return()

    # Function_17_97A1 end

    def Function_18_97ED(): pass

    label("Function_18_97ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9827")
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_18_97ED")

    label("loc_9827")

    Return()

    # Function_18_97ED end

    def Function_19_9828(): pass

    label("Function_19_9828")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_984B")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_19_9828")

    label("loc_984B")

    Return()

    # Function_19_9828 end

    def Function_20_984C(): pass

    label("Function_20_984C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_986F")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    Jump("Function_20_984C")

    label("loc_986F")

    Return()

    # Function_20_984C end

    def Function_21_9870(): pass

    label("Function_21_9870")

    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #599
        0xD,
        "#1P………嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #600
        0xD,
        (
            "#1P……来、来了！\x01",
            "这下来了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #601
        0xD,
        "#1P……啊……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(2000)

    ChrTalk(    #602
        0xD,
        "#1P没，没事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0xD,
        "#1P请、请别介意。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    Sleep(1000)

    ChrTalk(    #604
        0xD,
        (
            "#1P啊……唉～……\x01",
            "手气真差啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0xD,
        (
            "#1P唔～这恐怕\x01",
            "不行啊～\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_21_9870 end

    SaveToFile()

Try(main)
