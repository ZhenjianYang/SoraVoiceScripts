from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1121_1 ._SN',
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
        "Function_1_15F",          # 01, 1
        "Function_2_DB1",          # 02, 2
        "Function_3_EB7",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_2A(0xB5, 0xB6, 0xFFFF)
    Jump("loc_15B")

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_DA")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xB4, 0x79, 0x7C, 0xFFFF)
    Jump("loc_15B")

    label("loc_DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_F5")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xB4, 0xFFFF)
    Jump("loc_15B")

    label("loc_F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_10E")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xFFFF)
    Jump("loc_15B")

    label("loc_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_127")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xFFFF)
    Jump("loc_15B")

    label("loc_127")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05没发出什么委托。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_15B")

    TalkEnd(0xFF)
    Return()

    # Function_0_AA end

    def Function_1_15F(): pass

    label("Function_1_15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D0")

    ChrTalk(    #1
        0x101,
        (
            "#1002F卡片里说的地方……\x02\x03",

            "……莫非是指这里？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B")

    ChrTalk(    #2
        0x103,
        (
            "#022F嗯，虽然有这可能性……\x02\x03",

            "那个事件的调查稍后再进行吧。\x01",
            "现在要赶紧前往拉文努村哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #3
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CC")

    label("loc_22B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B9")

    ChrTalk(    #4
        0x108,
        (
            "#072F嗯，是有这可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在应该赶紧前往拉文努村。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #5
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CC")

    label("loc_2B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347")

    ChrTalk(    #6
        0x104,
        (
            "#030F唔，是有这可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在先赶紧前往拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #7
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CC")

    label("loc_347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CC")

    ChrTalk(    #8
        0x105,
        (
            "#042F嗯，说不定就是……\x02\x03",

            "不过这里迟些再调查吧。\x01",
            "现在得赶紧前往拉文努村啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #9
        0x101,
        "#1002F啊，嗯……说得对。\x02",
    )

    CloseMessageWindow()

    label("loc_3CC")

    TalkEnd(0xFF)
    Return()

    label("loc_3D0")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 27040, 0, 22430, 270)
    SetChrPos(0xF7, 28320, 0, 22190, 270)
    SetChrPos(0xF8, 29010, 0, 21500, 270)
    SetChrPos(0xF9, 27620, 0, 24010, 220)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_438")
    SetChrPos(0x4, 29870, 0, 22190, 270)

    label("loc_438")

    OP_6D(28000, 0, 23000, 0)
    OP_67(0, 4340, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05调查书本\x01",
            "发现贴着卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #11
        0x101,
        (
            "#1002F好，找到喽。\x02\x03",

            "#1015F嗯……写着什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 17)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05　想找到第三把钥匙，\x01",
            "就去检查『被托起的棺材』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #13
        0x101,
        (
            "#1007F呼，看来\x01",
            "是答对了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_615")

    ChrTalk(    #14
        0x105,
        (
            "#047F将『ＦＴＨＫＣ２Ｅ』\x01",
            "各推进一个字的话，\x01",
            "『ＧＵＩＬＤ３Ｆ』……\x02\x03",

            "#040F也就是说\x01",
            "在协会３楼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_782")

    label("loc_615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68E")

    ChrTalk(    #15
        0x107,
        (
            "#060F将『ＦＴＨＫＣ２Ｅ』\x01",
            "各推进一个字的话，\x01",
            "『ＧＵＩＬＤ３Ｆ』……\x02\x03",

            "也就是在\x01",
            "协会３楼的意思了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_782")

    label("loc_68E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70C")

    ChrTalk(    #16
        0x104,
        (
            "#035F将『ＦＴＨＫＣ２Ｅ』\x01",
            "各推进一个字的话，\x01",
            "『ＧＵＩＬＤ３Ｆ』……\x02\x03",

            "#030F也就是在\x01",
            "协会３楼的意思了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_782")

    label("loc_70C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_782")

    ChrTalk(    #17
        0x103,
        (
            "#020F将『ＦＴＨＫＣ２Ｅ』\x01",
            "各推进一个字的话，\x01",
            "『ＧＵＩＬＤ３Ｆ』……\x02\x03",

            "也就是在\x01",
            "协会３楼的意思了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_782")


    ChrTalk(    #18
        0x101,
        (
            "#1015F唔，虽说解开谜题了\x01",
            "是很好……\x02\x03",

            "#1007F但没、没想到居然\x01",
            "在协会里做了手脚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_839")

    ChrTalk(    #19
        0x106,
        (
            "#057F哼，真是\x01",
            "太目中无人了……\x02\x03",

            "下次碰到那家伙，\x01",
            "可要好好回敬一番。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_95A")

    label("loc_839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #20
        0x108,
        (
            "#075F啊啊，真是\x01",
            "被藐视了啊。\x02\x03",

            "#072F下次碰上那家伙，\x01",
            "可得好好回敬一番。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_95A")

    label("loc_89D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FA")

    ChrTalk(    #21
        0x103,
        (
            "#025F咳，真是\x01",
            "被小看了啊。\x02\x03",

            "下次碰上那家伙，\x01",
            "好好回敬他一番吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_95A")

    label("loc_8FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95A")

    ChrTalk(    #22
        0x104,
        (
            "#031F呼，真是\x01",
            "被小瞧了啊。\x02\x03",

            "下次碰上那家伙，\x01",
            "必须好好地回敬他一番呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_95A")


    ChrTalk(    #23
        0x101,
        "#1002F嗯，那可不是。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D9")

    ChrTalk(    #24
        0x104,
        (
            "#030F那，下一条线索是\x01",
            "『被托起的棺材』吗。\x02\x03",

            "可能这也是\x01",
            "某种『比喻』吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Jump("loc_AFF")

    label("loc_9D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3C")

    ChrTalk(    #25
        0x103,
        (
            "#022F那，下一条线索\x01",
            "『被托起的棺材』吗。\x02\x03",

            "我想大概\x01",
            "是某种『比喻』……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_AFF")

    label("loc_A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9D")

    ChrTalk(    #26
        0x107,
        (
            "#062F下一条线索是\x01",
            "『被托起的棺材』吗。\x02\x03",

            "我想大概\x01",
            "是某种『比喻』……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Jump("loc_AFF")

    label("loc_A9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFF")

    ChrTalk(    #27
        0x105,
        (
            "#042F那么，下一条线索是\x01",
            "『被托起的棺材』吗。\x02\x03",

            "恐怕是\x01",
            "某种『比喻』吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_AFF")


    ChrTalk(    #28
        0x101,
        (
            "#1002F这么想没错。\x02\x03",

            "因为真正的『棺材』之类的\x01",
            "东西哪可能在这附近随便乱放。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB1")

    ChrTalk(    #29
        0x108,
        (
            "#073F噢，相当\x01",
            "敏锐的洞察力啊。\x02\x03",

            "#070F那么就尽快去确认那个\x01",
            "『棺材』的原形吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF")

    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C15")

    ChrTalk(    #30
        0x106,
        (
            "#051F呵，看来已经\x01",
            "看破对方的手法了。\x02\x03",

            "那么就立刻去确认那个\x01",
            "『棺材』的原形吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF")

    label("loc_C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C72")

    ChrTalk(    #31
        0x103,
        (
            "#020F哎呀，洞察力挺敏锐的嘛。\x02\x03",

            "那么就尽快去确认那个\x01",
            "『棺材』的原形吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF")

    label("loc_C72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(    #32
        0x104,
        (
            "#030F呼，观察力\x01",
            "也敏锐起来了嘛。\x02\x03",

            "那么就尽快去确认那个\x01",
            "『棺材』的原形吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCF")

    OP_A2(0x1)
    OP_A3(0x0)
    OP_28(0x78, 0x1, 0x10)
    OP_28(0x78, 0x1, 0x20)
    OP_64(0x3, 0x1)

    def lambda_CEB():
        OP_8E(0x0, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_CEB)

    def lambda_D06():
        OP_8E(0x1, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_D06)

    def lambda_D21():
        OP_8E(0x2, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_D21)

    def lambda_D3C():
        OP_8E(0x3, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_D3C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D78")

    def lambda_D63():
        OP_8E(0x4, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_D63)

    label("loc_D78")

    OP_6D(27700, 0, 22200, 1000)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAE")
    WaitChrThread(0x4, 0x0)

    label("loc_DAE")

    EventEnd(0x0)
    Return()

    # Function_1_15F end

    def Function_2_DB1(): pass

    label("Function_2_DB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBE")
    Return()

    label("loc_DBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD0")
    Return()

    label("loc_DD0")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_E0B")
    Call(1, 3)
    Jump("loc_EB0")

    label("loc_E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_E1A")
    Call(1, 3)
    Jump("loc_EB0")

    label("loc_E1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_E72")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_EB0")

    label("loc_E72")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_EB0")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_2_DB1 end

    def Function_3_EB7(): pass

    label("Function_3_EB7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(    #35
        0x8,
        (
            "#632F原来如此，在做公告板上\x01",
            "找人的委托啊。\x02\x03",

            "我想这工作大概不轻松，\x01",
            "尽量想办法找吧。\x02\x03",

            "#632F因为来委托工作的女人\x01",
            "除了我们以外\x01",
            "已经没有别人可依靠了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_FBF")

    label("loc_F60")


    ChrTalk(    #36
        0x8,
        (
            "#632F因为来委托工作的女人\x01",
            "已经没有别人可依靠了。\x02\x03",

            "我想这工作大概不轻松，\x01",
            "尽量想办法找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBF")

    TalkEnd(0x8)
    Return()

    # Function_3_EB7 end

    SaveToFile()

Try(main)
