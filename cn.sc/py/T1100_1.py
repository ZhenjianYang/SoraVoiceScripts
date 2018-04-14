from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1100_1 ._SN',
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
        "Function_1_E8D",          # 01, 1
        "Function_2_F93",          # 02, 2
        "Function_3_1004",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31F")

    ChrTalk(    #0
        0x101,
        (
            "#1002F那卡片里写的地方……\x02\x03",

            "……莫非是指这里？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C")

    ChrTalk(    #1
        0x103,
        (
            "#022F嗯，虽然有这可能性……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在要赶紧赶去拉文努村哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B")

    label("loc_17C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A")

    ChrTalk(    #3
        0x108,
        (
            "#072F嗯，是有这可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在应该赶紧赶去拉文努村。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #4
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B")

    label("loc_20A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_296")

    ChrTalk(    #5
        0x104,
        (
            "#030F唔，是有这可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在先赶紧去拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #6
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B")

    label("loc_296")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B")

    ChrTalk(    #7
        0x105,
        (
            "#042F嗯，说不定就是……\x02\x03",

            "不过这里迟些再调查吧。\x01",
            "现在得赶紧赶去拉文努村啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#1002F啊，嗯……说得对。\x02",
    )

    CloseMessageWindow()

    label("loc_31B")

    TalkEnd(0xFF)
    Return()

    label("loc_31F")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 65390, 3000, 33170, 0)
    SetChrPos(0xF7, 65090, 3000, 31150, 0)
    SetChrPos(0xF8, 66060, 3000, 31080, 0)
    SetChrPos(0xF9, 65600, 3000, 30290, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_387")
    SetChrPos(0x4, 64830, 3000, 29670, 0)

    label("loc_387")

    OP_6D(65390, 3000, 32689, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42D")

    ChrTalk(    #9
        0x105,
        (
            "#042F卡片上的提示是\x01",
            "『ＲＩＣＵＬ』和『花的后面』。\x02\x03",

            "还有写着\x01",
            "『结束就是开端』……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_562")

    label("loc_42D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_495")

    ChrTalk(    #10
        0x107,
        (
            "#062F卡片上的提示是\x01",
            "『ＲＩＣＵＬ』和『花的后面』。\x02\x03",

            "还有写着\x01",
            "『结束就是开端』……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_562")

    label("loc_495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FD")

    ChrTalk(    #11
        0x104,
        (
            "#035F卡片上的提示是\x01",
            "『ＲＩＣＵＬ』和『花的后面』。\x02\x03",

            "而且写着\x01",
            "『结束就是开端』……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_562")

    label("loc_4FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_562")

    ChrTalk(    #12
        0x103,
        (
            "#026F卡片上的提示是\x01",
            "『ＲＩＣＵＬ』和『花的后面』。\x02\x03",

            "还有写着\x01",
            "『结束就是开端』……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #13
        0x101,
        (
            "#1015F#2P大概是要我们\x01",
            "倒过来念吧？\x02\x03",

            "如果从背后开始读的话……\x02\x03",

            "就是『调查ＬＵＣＩＲ\x01",
            "背后的花』\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_629")

    ChrTalk(    #14
        0x106,
        (
            "#051F呼，原来如此。\x02\x03",

            "在柏斯名字叫ＬＵＣＩＲ的，\x01",
            "只有这间鲁希尔工房了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74E")

    label("loc_629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_689")

    ChrTalk(    #15
        0x103,
        (
            "#021F呵呵，看来就是这儿了。\x02\x03",

            "在柏斯名字叫LUCIR的，\x01",
            "只有这间鲁希尔工房了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74E")

    label("loc_689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F4")

    ChrTalk(    #16
        0x108,
        (
            "#070F嗯，看来就是这儿了。\x02\x03",

            "在这座城市里名字叫ＬＵＣＩＲ的\x01",
            "看来只有这间鲁希尔工房了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74E")

    label("loc_6F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #17
        0x104,
        (
            "#030F嗯，原来如此。\x02\x03",

            "在柏斯名字叫ＬＵＣＩＲ的，\x01",
            "只有这间鲁希尔工房了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74E")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #18
        0x101,
        (
            "#1006F#2P嗯，而且和卡片上所写的一样，\x01",
            "这里也有『花』……\x02\x03",

            "不管怎样，先调查看看。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B1():

        label("loc_7B1")

        TurnDirection(0xF7, 0x101, 400)
        OP_48()
        Jump("loc_7B1")

    QueueWorkItem2(0xF7, 1, lambda_7B1)

    def lambda_7C2():

        label("loc_7C2")

        TurnDirection(0xF8, 0x101, 400)
        OP_48()
        Jump("loc_7C2")

    QueueWorkItem2(0xF8, 1, lambda_7C2)

    def lambda_7D3():

        label("loc_7D3")

        TurnDirection(0xF9, 0x101, 400)
        OP_48()
        Jump("loc_7D3")

    QueueWorkItem2(0xF9, 1, lambda_7D3)

    def lambda_7E4():
        OP_6D(65470, 3000, 35800, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_7E4)
    OP_8E(0x101, 0xFF6E, 0xBB8, 0x8B9C, 0x7D0, 0x0)
    Sleep(1000)
    WaitChrThread(0xF7, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #19
        (
            "\x07\x05调查了盆栽，\x01",
            "发现贴着卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        "#1018F#2P好！找到了。\x02",
    )

    CloseMessageWindow()
    Sleep(600)
    OP_8C(0x101, 180, 400)

    def lambda_893():
        OP_6D(65470, 3000, 32689, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_893)
    OP_8E(0x101, 0xFF6E, 0xBB8, 0x8192, 0x7D0, 0x0)
    WaitChrThread(0xF7, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F2")

    ChrTalk(    #21
        0x104,
        "#031F看来我们找到正确答案了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_8F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_926")

    ChrTalk(    #22
        0x108,
        "#070F看来我们找到正确答案了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95A")

    ChrTalk(    #23
        0x103,
        "#020F看来我们找到正确答案了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_95A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98B")

    ChrTalk(    #24
        0x106,
        "#051F看来我们找到正确答案了。\x02",
    )

    CloseMessageWindow()

    label("loc_98B")


    ChrTalk(    #25
        0x101,
        "#1006F嗯，快点看看吧。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 8)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x05　　第二把钥匙是如下的咒语──\x01",
            "　　　　ＦＴＨＫＣ２Ｅ \x01",
            "　　　  看那打开着的书。　　　　　　\x02\x03",

            "　　  绝不要忘记一个道理。　　　　\x01",
            "    辨清真相的人总抢先一步。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x101,
        (
            "#1019F#2P唔、唔……\x02\x03",

            "接下来的提示\x01",
            "『ＦＴＨＫＣ２Ｅ』是？\x02\x03",

            "真的搞不懂是什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B89")

    ChrTalk(    #28
        0x105,
        (
            "#047F大概跟前面一样，\x01",
            "也有某种念法吧。\x02\x03",

            "#042F我觉得『总抢先一步』\x01",
            "应该是一条线索……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE")

    label("loc_B89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF1")

    ChrTalk(    #29
        0x107,
        (
            "#064F这应该跟前面一样，\x01",
            "也有某种念法吧。\x02\x03",

            "我觉得『总抢先一步』\x01",
            "应该是一条线索……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE")

    label("loc_BF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C59")

    ChrTalk(    #30
        0x104,
        (
            "#030F这应该跟前面一样，\x01",
            "也有某种念法吧。\x02\x03",

            "我觉得『总抢先一步』\x01",
            "恐怕是一条线索……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE")

    label("loc_C59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBE")

    ChrTalk(    #31
        0x103,
        (
            "#027F这应该跟前面一样，\x01",
            "也有某种念法吧。\x02\x03",

            "我觉得『总抢先一步』\x01",
            "一定是一条线索……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBE")

    OP_59()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()

    ChrTalk(    #32
        0x101,
        (
            "#1015F#2P总之只能先\x01",
            "在城里再调查一下了。\x02\x03",

            "那样的话有可能会\x01",
            "发现一点什么。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D62")

    ChrTalk(    #33
        0x106,
        (
            "#050F嗯，呆坐着瞎想也\x01",
            "没什么用。\x02\x03",

            "赶快开始调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5F")

    label("loc_D62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(    #34
        0x103,
        (
            "#020F嗯，呆坐着瞎想也\x01",
            "没什么用。\x02\x03",

            "赶快开始调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5F")

    label("loc_DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E00")

    ChrTalk(    #35
        0x108,
        (
            "#070F嗯，在外面走的时候\x01",
            "思路也会更清晰一些。\x02\x03",

            "好，那么出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5F")

    label("loc_E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5F")

    ChrTalk(    #36
        0x104,
        (
            "#030F嗯，边走边想的话\x01",
            "常会有好的想法浮现呢。\x02\x03",

            "既然决定了，\x01",
            "赶快开始调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5F")


    ChrTalk(    #37
        0x101,
        "#1000F#2P是啊，走吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x78, 0x1, 0x4)
    OP_28(0x78, 0x1, 0x8)
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_E8D(): pass

    label("Function_1_E8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9A")
    Return()

    label("loc_E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EAC")
    Return()

    label("loc_EAC")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xF)"), scpexpr(EXPR_END)), "loc_EE7")
    Call(1, 2)
    Jump("loc_F8C")

    label("loc_EE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xE)"), scpexpr(EXPR_END)), "loc_EF6")
    Call(1, 3)
    Jump("loc_F8C")

    label("loc_EF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_F4E")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_F8C")

    label("loc_F4E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_F8C")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_1_E8D end

    def Function_2_F93(): pass

    label("Function_2_F93")

    TalkBegin(0xF)

    ChrTalk(    #40
        0xF,
        (
            "哎呀，好可爱的小姑娘啊。\x01",
            "不过不巧，我没印象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "要寻问的话，去比南街区\x01",
            "人多的北街区看看怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_2_F93 end

    def Function_3_1004(): pass

    label("Function_3_1004")

    TalkBegin(0xE)

    ChrTalk(    #42
        0xE,
        (
            "啊，是在『百日战役』中\x01",
            "成为孤儿的……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "……真可怜。\x01",
            "我对帮不了你们感到很遗憾。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_3_1004 end

    SaveToFile()

Try(main)
