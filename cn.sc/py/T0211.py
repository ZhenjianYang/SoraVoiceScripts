from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0211   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0211.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60084",
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
        '米蕾奴夫人',                           # 9
        '玲达',                                 # 10
        '克劳斯市长',                           # 11
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


    AddCharChip(
        'ED6_DT07/CH01180 ._CH',             # 00
        'ED6_DT26/CH20330 ._CH',             # 01
        'ED6_DT07/CH02350 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01180P._CP',             # 00
        'ED6_DT26/CH20330P._CP',             # 01
        'ED6_DT07/CH02350P._CP',             # 02
    )

    DeclNpc(
        X                   = 200400,
        Z                   = 0,
        Y                   = 48360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 201800,
        Z                   = 0,
        Y                   = 48800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 77760,
        Z                   = 0,
        Y                   = 3410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_171",          # 01, 1
        "Function_2_180",          # 02, 2
        "Function_3_2FD",          # 03, 3
        "Function_4_3AE",          # 04, 4
        "Function_5_B87",          # 05, 5
        "Function_6_C62",          # 06, 6
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_159")
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    SetChrPos(0x8, 200400, 0, 48360, 90)
    OP_4A(0x9, 255)

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_170")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 5)

    label("loc_170")

    Return()

    # Function_0_122 end

    def Function_1_171(): pass

    label("Function_1_171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_17F")
    OP_6F(0x5, 10)

    label("loc_17F")

    Return()

    # Function_1_171 end

    def Function_2_180(): pass

    label("Function_2_180")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2E7")

    label("loc_1A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2E7")

    label("loc_1BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2E7")

    label("loc_1D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2E7")

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2E7")

    label("loc_209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2E7")

    label("loc_222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2E7")

    label("loc_23B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2E7")

    label("loc_254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2E7")

    label("loc_26D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2E7")

    label("loc_286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2E7")

    label("loc_29F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2E7")

    label("loc_2B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2E7")

    label("loc_2D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2E7")

    label("loc_2FC")

    Return()

    # Function_2_180 end

    def Function_3_2FD(): pass

    label("Function_3_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C")
    Call(0, 6)
    Jump("loc_3AD")

    label("loc_30C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_367")

    ChrTalk(    #0
        0xFE,
        (
            "如果有事\x01",
            "我会马上联系协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "呼，这座城市\x01",
            "现在到底在发生着什么啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA")

    label("loc_367")


    ChrTalk(    #2
        0xFE,
        (
            "如果有事\x01",
            "我会马上联系协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "你们也……\x01",
            "一定要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3AA")

    TalkEnd(0x8)

    label("loc_3AD")

    Return()

    # Function_3_2FD end

    def Function_4_3AE(): pass

    label("Function_4_3AE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 3)), scpexpr(EXPR_END)), "loc_4AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_418")

    ChrTalk(    #4
        0xA,
        (
            "#602F玲达\x01",
            "在对面的房间里休息。\x02\x03",

            "米蕾奴在陪着她，\x01",
            "详细情况你们可以去问她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AC")

    label("loc_418")


    ChrTalk(    #5
        0xA,
        (
            "#602F调查的事我已经\x01",
            "传达给爱娜了。\x02\x03",

            "艾丝蒂尔你们就\x01",
            "专心地调查吧。\x02\x03",

            "……玲达\x01",
            "在对面的房间里休息。\x02\x03",

            "米蕾奴在陪着她，\x01",
            "详细情况你们可以去问她。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4AC")

    Jump("loc_B83")

    label("loc_4AF")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 1)), scpexpr(EXPR_END)), "loc_6F9")

    ChrTalk(    #6
        0xA,
        (
            "#604F哦，是艾丝蒂尔你们啊。\x02\x03",

            "#603F真想不到会\x01",
            "变成这样……\x02\x03",

            "本来我只是推迟去王都，\x01",
            "现在看来只能放弃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1004F啊……！？\x01",
            "您、您不去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x103,
        "#023F就是说要缺席签字仪式？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "#603F嗯，虽然对女王陛下感到抱歉，\x01",
            "不过现在也只能这么做了。\x02\x03",

            "虽然参加仪式也是\x01",
            "市长的工作……\x02\x03",

            "#602F可是不管有什么样的理由，\x01",
            "我现在都不能离开这座城市。\x02\x03",

            "……就算那是\x01",
            "陛下的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1020F市长爷爷……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #11
        0xA,
        (
            "#602F调查的事我已经\x01",
            "传达给爱娜了。\x02\x03",

            "艾丝蒂尔你们请\x01",
            "马上开始调查。\x02\x03",

            "即便是为了防止\x01",
            "受害者的增加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1002F嗯！明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        "#022F嗯，我们会尽全力的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B80")

    label("loc_6F9")


    ChrTalk(    #14
        0xA,
        (
            "#604F哦，是艾丝蒂尔你们啊。\x02\x03",

            "#603F真想不到会\x01",
            "变成这样……\x02\x03",

            "呼，看来我放弃去\x01",
            "王都是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1015F啊？在王都也有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#023F去王都，难道是……\x02\x03",

            "互不侵犯条约的签字仪式吗？！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0x101,
        "#1004F啊！签字仪式！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "#602F嗯，你说得没错。\x02\x03",

            "虽然对不起女王陛下，\x01",
            "不过我还是得缺席了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1020F缺、缺席……！？\x02\x03",

            "真、真的打算\x01",
            "不去了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #20
        0xA,
        (
            "#603F当然，参加仪式也是\x01",
            "市长的工作……\x02\x03",

            "可是不管有什么样的理由，\x01",
            "我现在都不能离开这座城市。\x02\x03",

            "#602F……就算那是\x01",
            "女王陛下的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1026F市长爷爷……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_966")

    ChrTalk(    #22
        0x105,
        (
            "#047F……我觉得这是一个英明的抉择。\x02\x03",

            "#042F祖母大人\x01",
            "也一定会理解您的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_966")


    ChrTalk(    #23
        0xA,
        (
            "#602F如果接下来再发生什么问题，\x01",
            "我打算与协会合作应对。\x02\x03",

            "不好意思，这段时间\x01",
            "我要借助各位的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1002F嗯，当然没问题！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #25
        0x106,
        (
            "#050F啊，那是应该的。\x02\x03",

            "再次来到这里也算\x01",
            "是缘分吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF5")

    label("loc_A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A83")

    ChrTalk(    #26
        0x108,
        (
            "#072F嗯，我们会配合的。\x02\x03",

            "再次来到这里…\x01",
            "这一定是女神的召唤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF5")

    label("loc_A83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD2")

    ChrTalk(    #27
        0x104,
        (
            "#030F呼，交给我们好啦。\x02\x03",

            "再次来到这里\x01",
            "也算是一种缘分啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF5")

    label("loc_AD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF5")

    ChrTalk(    #28
        0x107,
        "#062F是、是的！\x02",
    )

    CloseMessageWindow()

    label("loc_AF5")


    ChrTalk(    #29
        0xA,
        "#603F那就先谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        (
            "#022F那如果有什么事的话\x01",
            "请随时和协会联络。\x02\x03",

            "爱娜会马上\x01",
            "联络到我们的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #31
        0xA,
        "#602F嗯，我们会的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1881)

    label("loc_B80")

    OP_A2(0x189B)

    label("loc_B83")

    TalkEnd(0xA)
    Return()

    # Function_4_3AE end

    def Function_5_B87(): pass

    label("Function_5_B87")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6F(0x5, 10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 200400, 0, 48360, 90)
    OP_4A(0x9, 255)
    OP_6D(200500, 0, 45550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(201840, 0, 49170, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0135   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B87 end

    def Function_6_C62(): pass

    label("Function_6_C62")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x101, 199890, 0, 46520, 0)
    SetChrPos(0x103, 200990, 0, 46580, 0)
    SetChrPos(0xF8, 199780, 0, 45200, 0)
    SetChrPos(0xF9, 200960, 0, 45200, 0)
    OP_6D(200720, 0, 47460, 0)
    OP_67(0, 6690, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #32
        0xFE,
        (
            "#5P哎呀，艾丝蒂尔……\x01",
            "和雪拉扎德吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1002F晚上好。\x01",
            "米蕾奴阿姨。\x02\x03",

            "市长先生跟您说过了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "#5P嗯，你们要调查\x01",
            "这次的事件吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "#5P有什么问题\x01",
            "尽管问我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#026F#4P那真是太好了。\x02\x03",

            "#022F那么首先……\x01",
            "玲达小姐的情况怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "#5P嗯……\x01",
            "一点也没有要醒的迹象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "#5P如果明天早上能\x01",
            "自然地醒过来就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "#5P现在只能继续观察了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1007F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        (
            "#022F#4P玲达小姐是于何时昏倒的？\x01",
            "当时是什么样的情况？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "#5P让我想想……\x01",
            "大概是傍晚的５点前吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "#5P我从楼下的厨房出来后，\x01",
            "就看到玲达倒在门口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "#5P我就赶紧到书房去叫我先生，\x01",
            "然后把她扶到了床上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "#5P不过，真没想到还有其他的人\x01",
            "也遇上了同样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1015F倒在门口……\x02\x03",

            "那时大门锁着吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "#5P我记得……\x01",
            "应该是没有锁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "#5P因为有很多人来跟我先生\x01",
            "商量大雾的对策。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1007F嗯……\x02\x03",

            "#1002F阿姨您准备饭菜大概\x01",
            "用了多久？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "#5P让我想想……\x01",
            "３０分钟左右。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        (
            "#026F#4P是这样啊……\x01",
            "大致情况我们了解了。\x02\x03",

            "#022F最后一个问题……\x02\x03",

            "在玲达小姐昏睡的前后……\x01",
            "有发生过什么怪事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#5P怪事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020F#4P比如有陌生人来访\x01",
            "或者异常的响动之类的……\x02\x03",

            "只要能想到的什么都行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#5P让我想想……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "#5P有一件与其说是怪事倒不如\x01",
            "说是令人印象深刻的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "#5P我在厨房准备饭菜的时候，\x01",
            "听见了微弱的铃声。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1283")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没在其他地方听说过铃的事(没从亚尔丽&胡里奥哪里听说)】\x01",      # 0
            "【◇已在其他地方听说过铃的事(已从亚尔丽&胡里奥哪里听说)】\x01",      # 1
            "【◇不变更】\x01",                                                   # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1277"),
        (1, "loc_127D"),
        (SWITCH_DEFAULT, "loc_1283"),
    )


    label("loc_1277")

    OP_A3(0x1815)
    Jump("loc_1283")

    label("loc_127D")

    OP_A2(0x1815)
    Jump("loc_1283")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1326")

    ChrTalk(    #57
        0x103,
        "#023F#4P铃声……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1004F那是……\x01",
            "我们也听到过的那个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "#5P音色很美，\x01",
            "我还以为是玲达\x01",
            "在摇呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "#5P说起来真让人想不出\x01",
            "是从哪里传来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C1")

    label("loc_1326")


    ChrTalk(    #61
        0x103,
        "#022F#4P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002F这里也提到了铃声……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "#5P音色很美，\x01",
            "我还以为是玲达\x01",
            "在摇呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "#5P说起来真让人想不出\x01",
            "是从哪里传来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C1")


    ChrTalk(    #65
        0x103,
        (
            "#026F#4P……您给了我们很好的参考。\x02\x03",

            "#020F如果再发现什么事\x01",
            "请联系协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "#5P你们也……\x01",
            "请一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1025F嗯，我们会的。\x02\x03",

            "谢谢。\x01",
            "米蕾奴阿姨。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 0)
    OP_4B(0x8, 255)
    OP_A2(0x1813)
    OP_28(0x90, 0x2, 0x2)
    OP_28(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AB")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_14AB")

    label("loc_14AB")

    EventEnd(0x0)
    Return()

    # Function_6_C62 end

    SaveToFile()

Try(main)
