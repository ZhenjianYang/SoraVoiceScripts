from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2120_1 ._SN',
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
        "Function_1_140",          # 01, 1
        "Function_2_F3B",          # 02, 2
        "Function_3_12B5",         # 03, 3
        "Function_4_17EF",         # 04, 4
        "Function_5_18FC",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_2A(0xB9, 0xBA, 0xFFFF)
    Jump("loc_13C")

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_D8")
    OP_2A(0x65, 0x66, 0xA1, 0xA3, 0x67, 0x68, 0xA2, 0xA4, 0xFFFF)
    Jump("loc_13C")

    label("loc_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_F3")
    OP_2A(0x65, 0x66, 0xA1, 0xA3, 0x67, 0xA2, 0xA4, 0xFFFF)
    Jump("loc_13C")

    label("loc_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_108")
    OP_2A(0x65, 0x66, 0xA1, 0xA3, 0xFFFF)
    Jump("loc_13C")

    label("loc_108")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05没发出什么委托。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13C")

    TalkEnd(0xFF)
    Return()

    # Function_0_AA end

    def Function_1_140(): pass

    label("Function_1_140")

    EventBegin(0x0)
    OP_6D(-32970, 0, 5800, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x9, -33640, 0, 6750, 0)
    SetChrPos(0x15, -29550, 0, 3100, 0)
    SetChrPos(0x101, -30640, 0, 3100, 0)
    SetChrPos(0xF7, -29970, 0, 1750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E6")
    SetChrPos(0x127, -31340, 0, 1210, 0)

    label("loc_1E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_204")
    SetChrPos(0x104, -31640, 0, 2480, 0)

    label("loc_204")

    OP_4A(0x9, 255)

    def lambda_20E():

        label("loc_20E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_20E")

    QueueWorkItem2(0x0, 1, lambda_20E)

    def lambda_21F():

        label("loc_21F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_21F")

    QueueWorkItem2(0x1, 1, lambda_21F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_259")

    def lambda_23D():

        label("loc_23D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_23D")

    QueueWorkItem2(0x2, 1, lambda_23D)

    def lambda_24E():

        label("loc_24E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_24E")

    QueueWorkItem2(0x3, 1, lambda_24E)

    label("loc_259")


    def lambda_25F():

        label("loc_25F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_25F")

    QueueWorkItem2(0x15, 1, lambda_25F)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_27F():
        OP_6D(-29850, 0, 3090, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_27F)
    OP_8E(0x9, 0xFFFF8882, 0x0, 0x17A2, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF8AD0, 0x0, 0x132E, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    Sleep(400)
    WaitChrThread(0x0, 0x2)
    OP_44(0x15, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2EB")
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    label("loc_2EB")


    ChrTalk(    #1
        0x9,
        "好，完成了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x15,
        "……嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    def lambda_317():

        label("loc_317")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_317")

    QueueWorkItem2(0x0, 1, lambda_317)

    def lambda_328():

        label("loc_328")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_328")

    QueueWorkItem2(0x1, 1, lambda_328)

    def lambda_339():

        label("loc_339")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_339")

    QueueWorkItem2(0x2, 1, lambda_339)

    def lambda_34A():

        label("loc_34A")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_34A")

    QueueWorkItem2(0x3, 1, lambda_34A)

    ChrTalk(    #3
        0x15,
        "好～了，看看照得怎样……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x15)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_6EC")

    ChrTalk(    #4
        0x15,
        "……啊，真令人惊讶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x15,
        (
            "专业人士看了都会惊讶的……不，\x01",
            "说白了就是超越专业人士的水准了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1004F那，那么厉害吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x15,
        "看，请看呀。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0x0, 0x0, 0x258, 0x12C, 0x14, 0x5A, 0x280, 0x12C, 0x0, 0x0, 0x258, 0x12C, 0xFFFFFF, 0x0, "C_VIS198._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #8
        "#1011F哎呀～确实漂亮啊。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #9
        (
            "嗯，十分难得的是\x01",
            "焦点也对得非常准确……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #10
        (
            "不～不管怎么说\x01",
            "这光线的处理实在是绝妙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #11
        (
            "『装置』的漫长历史\x01",
            "光是在照片里看就能感受到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #12
        (
            "这照片\x01",
            "足够作为研究资料了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #13
        (
            "这照片作为保留资料\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #14
        (
            "#1004F是、是这样啊……\x02\x03",

            "#1016F啊，哈～好深奥啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("朵洛希")

    AnonymousTalk(    #15
        "#151F嘿嘿～了不起。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(1500)
    OP_C7(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6AB")

    ChrTalk(    #16
        0x106,
        "#051F……那，这样就算完成工作了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D9")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6D9")

    ChrTalk(    #17
        0x103,
        "#020F那么，这样就算完成工作了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6D9")

    OP_2B(0x66, 0x2)
    OP_2C(0x66, 0x3E8)
    OP_28(0x66, 0x1, 0x10)
    Jump("loc_AA2")

    label("loc_6EC")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_745")

    ChrTalk(    #18
        0x15,
        "……嗯……马马虎虎吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x15,
        "作为资料来说还算能用吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x66, 0x1, 0x80)
    Jump("loc_7D0")

    label("loc_745")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(    #20
        0x15,
        (
            "……嗯，做得好哦。\x01",
            "完全没有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x66, 0x1)
    OP_2C(0x66, 0x3E8)
    OP_28(0x66, 0x1, 0x20)
    Jump("loc_7D0")

    label("loc_78B")


    ChrTalk(    #21
        0x15,
        "……嗯……马马虎虎吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x15,
        "作为资料来说还算能用吧。\x02",
    )

    CloseMessageWindow()
    OP_2C(0x66, 0x1F4)
    OP_28(0x66, 0x1, 0x40)

    label("loc_7D0")


    ChrTalk(    #23
        0x15,
        "要看看吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1018F嗯，看啊看啊⊙\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(300, 0, 100)
    Call(1, 2)
    OP_C5(0x1, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x0, 0x0, 0x190, 0x12C, 0xFFFFFF, 0x0, "C_VIS199._CH")
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #25
        (
            "#1001F啊，太好了～\x02\x03",

            "比想象的\x01",
            "拍得还漂亮嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8DD")
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #26
        "#031F光线掌握得很好啊。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_8DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_916")
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("朵洛希")

    AnonymousTalk(    #27
        "#150F嗯，拍得很棒嘛⊙\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_916")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EC")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #28
        "很遗憾啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #29
        (
            "因为是资料照片，可以的话\x01",
            "最好从正面拍摄哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #30
        (
            "#1008F呜，也对啊……\x02\x03",

            "不，不知不觉就得意忘形的\x01",
            "从奇怪的角度拍摄了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_A1E")

    label("loc_9EC")

    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("森特")

    AnonymousTalk(    #31
        (
            "嗯，这样的话\x01",
            "我也能够认可哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A1E")

    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(1500)
    OP_C7(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(    #32
        0x106,
        "#050F这样就算完成工作了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA2")

    label("loc_A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AA2")

    ChrTalk(    #33
        0x103,
        "#020F这样就算完成工作了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_AA2")

    TurnDirection(0x15, 0xF7, 400)

    ChrTalk(    #34
        0x15,
        "是，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x15,
        (
            "呀～各位，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x15,
        (
            "特意麻烦你们\x01",
            "去绀碧之塔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1015F嗯，确实挺辛苦的……\x02\x03",

            "#1006F不过，这也是工作嘛。\x01",
            "请别介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x15,
        (
            "啊哈哈，这么说\x01",
            "我就感觉轻松多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x15,
        (
            "对了。\x01",
            "虽说也算不上什么谢礼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x15,
        "……请收下这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #41
        "\x07\x00得到了\x1F\x55\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x155, 1)
    Sleep(500)

    ChrTalk(    #42
        0x15,
        (
            "这是为了此次调查，\x01",
            "用研究费购买的物品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x15,
        (
            "去危险的地方时\x01",
            "我想一定能帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1001F嘿嘿，谢谢⊙\x02\x03",

            "难得你一番好意，\x01",
            "就不客气地接受喽。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CAA")

    ChrTalk(    #45
        0x106,
        (
            "#051F不好意思呢。\x01",
            "让你破费了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD5")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CD5")

    ChrTalk(    #46
        0x103,
        (
            "#020F不好意思啊。\x01",
            "让你破费了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD5")


    ChrTalk(    #47
        0x15,
        (
            "哪里哪里。\x01",
            "也不是什么大不了的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x15,
        (
            "……那么，差不多了，\x01",
            "我先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x15,
        "今天非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1000F你也要加油\x01",
            "继续努力对『装置』的调查哦。\x02\x03",

            "许多地方都挺令人好奇的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #51
        0x15,
        (
            "啊、啊哈哈……\x01",
            "那也是辛苦的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x15,
        (
            "不过，为了不负期待，\x01",
            "我们也会尽最大努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x15,
        "……那么，我就告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1006F嗯，那再见了。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x15, 180, 400)

    def lambda_E48():
        OP_91(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_E48)
    OP_8E(0x15, 0xFFFF8C92, 0x0, 0xFFFFFC18, 0x7D0, 0x1)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_E82():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E82)
    OP_8E(0x15, 0xFFFF8C92, 0xFFFFFDFA, 0xFFFFF574, 0x7D0, 0x0)
    WaitChrThread(0x15, 0x2)
    SetChrFlags(0x15, 0x80)
    Sleep(1500)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x02任务【『绀碧之塔』的照片拍摄】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x66, 0x1, 0x100)
    OP_28(0x66, 0x4, 0x10)
    OP_A2(0x5)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_1_140 end

    def Function_2_F3B(): pass

    label("Function_2_F3B")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F76")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x78, 0x0, 0x208, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_F76")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB2")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x64, 0x0, 0x1F4, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_FB2")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FED")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x8C, 0x0, 0x21C, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_FED")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1029")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x50, 0x0, 0x1E0, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_1029")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1064")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xA0, 0x0, 0x230, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_1064")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A0")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x3C, 0x0, 0x1CC, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_10A0")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DB")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xB4, 0x0, 0x244, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_10DB")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1117")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x14, 0x0, 0x1A4, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_1117")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1152")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xDC, 0x0, 0x26C, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_12B4")

    label("loc_1152")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118E")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x3C, 0x0, 0x1CC, 0x12C, 0xFFFFFF, 0x0, "C_VIS196._CH")
    Jump("loc_12B4")

    label("loc_118E")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CA")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x78, 0x0, 0x208, 0x12C, 0xFFFFFF, 0x0, "C_VIS196._CH")
    Jump("loc_12B4")

    label("loc_11CA")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1206")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xDC, 0x0, 0x26C, 0x12C, 0xFFFFFF, 0x0, "C_VIS196._CH")
    Jump("loc_12B4")

    label("loc_1206")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1241")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xB4, 0x0, 0x244, 0x12C, 0xFFFFFF, 0x0, "C_VIS197._CH")
    Jump("loc_12B4")

    label("loc_1241")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127C")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x3C, 0x0, 0x1CC, 0x12C, 0xFFFFFF, 0x0, "C_VIS197._CH")
    Jump("loc_12B4")

    label("loc_127C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B4")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x14, 0x0, 0x1A4, 0x12C, 0xFFFFFF, 0x0, "C_VIS197._CH")

    label("loc_12B4")

    Return()

    # Function_2_F3B end

    def Function_3_12B5(): pass

    label("Function_3_12B5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D6")
    OP_3F(0x151, 1)
    Jump("loc_17EE")

    label("loc_12D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EE")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #56
        "\x07\x05请选择取下零力场发生器的成员。\x02",
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_133F")
    Call(1, 4)
    Jump("loc_1343")

    label("loc_133F")

    Call(1, 5)

    label("loc_1343")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_136A")
    Call(1, 4)
    Jump("loc_136E")

    label("loc_136A")

    Call(1, 5)

    label("loc_136E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1395")
    Call(1, 4)
    Jump("loc_1399")

    label("loc_1395")

    Call(1, 5)

    label("loc_1399")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13C0")
    Call(1, 4)
    Jump("loc_13C4")

    label("loc_13C0")

    Call(1, 5)

    label("loc_13C4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_140B"),
        (1, "loc_1451"),
        (2, "loc_1497"),
        (3, "loc_14DD"),
        (SWITCH_DEFAULT, "loc_1523"),
    )


    label("loc_140B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_144E")

    label("loc_142E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_144E")

    Jump("loc_1523")

    label("loc_1451")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1474")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1494")

    label("loc_1474")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1494")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1494")

    Jump("loc_1523")

    label("loc_1497")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14DA")

    label("loc_14BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14DA")

    Jump("loc_1523")

    label("loc_14DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1500")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1520")

    label("loc_1500")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1520")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1520")

    Jump("loc_1523")

    label("loc_1523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154C")

    AnonymousTalk(    #57
        "\x07\x05未装备零力场发生器。\x02",
    )

    Jump("loc_17DF")

    label("loc_154C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1594")

    AnonymousTalk(    #58
        (
            "\x07\x05艾丝蒂尔已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_1594")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DA")

    AnonymousTalk(    #59
        (
            "\x07\x05约修亚已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_15DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1622")

    AnonymousTalk(    #60
        (
            "\x07\x05雪拉扎德已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_1622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166A")

    AnonymousTalk(    #61
        (
            "\x07\x05奥利维尔已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_166A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B0")

    AnonymousTalk(    #62
        (
            "\x07\x05科洛丝已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_16B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F6")

    AnonymousTalk(    #63
        (
            "\x07\x05阿加特已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_16F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1760")

    AnonymousTalk(    #64
        (
            "\x07\x05提妲已取下零力场发生器，\x01",
            "无法使用魔法，战技，普通攻击。\x01",
            "但S战技『炮射冲击』仍可使用。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_1760")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A0")

    AnonymousTalk(    #65
        (
            "\x07\x05金已取下零力场发生器\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_17DF")

    label("loc_17A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DF")

    AnonymousTalk(    #66
        (
            "\x07\x05凯文已取下零力场发生器\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )


    label("loc_17DF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_12D6")

    label("loc_17EE")

    Return()

    # Function_3_12B5 end

    def Function_4_17EF(): pass

    label("Function_4_17EF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_181C"),
        (1, "loc_1837"),
        (2, "loc_1850"),
        (3, "loc_186B"),
        (4, "loc_1886"),
        (5, "loc_189F"),
        (6, "loc_18B8"),
        (7, "loc_18CF"),
        (8, "loc_18E4"),
        (SWITCH_DEFAULT, "loc_18FB"),
    )


    label("loc_181C")

    OP_CC(0x1, 0x0, "【艾丝蒂尔　装备中】")
    Jump("loc_18FB")

    label("loc_1837")

    OP_CC(0x1, 0x0, "【约修亚　装备中】")
    Jump("loc_18FB")

    label("loc_1850")

    OP_CC(0x1, 0x0, "【雪拉扎德　装备中】")
    Jump("loc_18FB")

    label("loc_186B")

    OP_CC(0x1, 0x0, "【奥利维尔　装备中】")
    Jump("loc_18FB")

    label("loc_1886")

    OP_CC(0x1, 0x0, "【科洛丝　装备中】")
    Jump("loc_18FB")

    label("loc_189F")

    OP_CC(0x1, 0x0, "【阿加特　装备中】")
    Jump("loc_18FB")

    label("loc_18B8")

    OP_CC(0x1, 0x0, "【提妲　装备中】")
    Jump("loc_18FB")

    label("loc_18CF")

    OP_CC(0x1, 0x0, "【金　装备中】")
    Jump("loc_18FB")

    label("loc_18E4")

    OP_CC(0x1, 0x0, "【凯文　装备中】")
    Jump("loc_18FB")

    label("loc_18FB")

    Return()

    # Function_4_17EF end

    def Function_5_18FC(): pass

    label("Function_5_18FC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1929"),
        (1, "loc_1944"),
        (2, "loc_195D"),
        (3, "loc_1978"),
        (4, "loc_1993"),
        (5, "loc_19AC"),
        (6, "loc_19C5"),
        (7, "loc_19DC"),
        (8, "loc_19F1"),
        (SWITCH_DEFAULT, "loc_1A08"),
    )


    label("loc_1929")

    OP_CC(0x1, 0x0, "【艾丝蒂尔　未装备】")
    Jump("loc_1A08")

    label("loc_1944")

    OP_CC(0x1, 0x0, "【约修亚　未装备】")
    Jump("loc_1A08")

    label("loc_195D")

    OP_CC(0x1, 0x0, "【雪拉扎德　未装备】")
    Jump("loc_1A08")

    label("loc_1978")

    OP_CC(0x1, 0x0, "【奥利维尔　未装备】")
    Jump("loc_1A08")

    label("loc_1993")

    OP_CC(0x1, 0x0, "【科洛丝　未装备】")
    Jump("loc_1A08")

    label("loc_19AC")

    OP_CC(0x1, 0x0, "【阿加特　未装备】")
    Jump("loc_1A08")

    label("loc_19C5")

    OP_CC(0x1, 0x0, "【提妲　未装备】")
    Jump("loc_1A08")

    label("loc_19DC")

    OP_CC(0x1, 0x0, "【金　未装备】")
    Jump("loc_1A08")

    label("loc_19F1")

    OP_CC(0x1, 0x0, "【凯文　未装备】")
    Jump("loc_1A08")

    label("loc_1A08")

    Return()

    # Function_5_18FC end

    SaveToFile()

Try(main)
