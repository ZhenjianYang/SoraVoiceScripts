from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1400   ._SN',
        MapName             = 'Bose',
        Location            = 'C1400.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        '维姆拉',                               # 9
        '阿加特',                               # 10
        '',                                     # 11
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT06/CH20053 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT06/CH20053P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -59360,
        Y                   = 2000,
        Z                   = 181540,
        Range               = -67440,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0x2B390,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_163",          # 01, 1
        "Function_2_186",          # 02, 2
        "Function_3_19C",          # 03, 3
        "Function_4_54B",          # 04, 4
        "Function_5_9E6",          # 05, 5
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 0)), scpexpr(EXPR_END)), "loc_143")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -60800, 3970, 187600, 270)

    label("loc_143")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_162")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_162")

    Return()

    # Function_0_11A end

    def Function_1_163(): pass

    label("Function_1_163")

    OP_72(0x401, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_185")

    Return()

    # Function_1_163 end

    def Function_2_186(): pass

    label("Function_2_186")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_186")

    label("loc_19B")

    Return()

    # Function_2_186 end

    def Function_3_19C(): pass

    label("Function_3_19C")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "怎么了，想说点什么吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "休息\x01",      # 0
            "吃饭\x01",      # 1
            "离开\x01",      # 2
        )
    )

    Jump("loc_1FF")

    label("loc_1FF")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x10, 0xFE, 0x0)
    OP_31(0x11, 0xFE, 0x0)
    OP_31(0x12, 0xFE, 0x0)
    Sleep(1000)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #1
        0xFE,
        (
            "是不是\x01",
            "觉得舒服一些了？\x02",
        )
    )

    Jump("loc_28E")

    label("loc_28E")

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "那就赶快\x01",
            "鼓起干劲出发吧。\x02",
        )
    )

    Jump("loc_2C0")

    label("loc_2C0")

    CloseMessageWindow()
    Jump("loc_547")

    label("loc_2C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F4")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #3
        "\x06\x07\x02地狱极乐锅\x07\x00品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_34D"),
        (1, "loc_38E"),
        (2, "loc_3CF"),
        (SWITCH_DEFAULT, "loc_410"),
    )


    label("loc_34D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_365")
    OP_31(0x10, 0x2, 0x1)
    OP_31(0x10, 0x5, 0x0)

    label("loc_365")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_378")
    OP_31(0x11, 0x5, 0x64)

    label("loc_378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B")
    OP_31(0x12, 0x5, 0x64)

    label("loc_38B")

    Jump("loc_410")

    label("loc_38E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A1")
    OP_31(0x10, 0x5, 0x64)

    label("loc_3A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B9")
    OP_31(0x11, 0x2, 0x1)
    OP_31(0x11, 0x5, 0x0)

    label("loc_3B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CC")
    OP_31(0x12, 0x5, 0x64)

    label("loc_3CC")

    Jump("loc_410")

    label("loc_3CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E2")
    OP_31(0x10, 0x5, 0x64)

    label("loc_3E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F5")
    OP_31(0x11, 0x5, 0x64)

    label("loc_3F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D")
    OP_31(0x12, 0x2, 0x1)
    OP_31(0x12, 0x5, 0x0)

    label("loc_40D")

    Jump("loc_410")

    label("loc_410")

    Jump("loc_496")

    label("loc_413")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_43A"),
        (1, "loc_468"),
        (SWITCH_DEFAULT, "loc_496"),
    )


    label("loc_43A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_452")
    OP_31(0x10, 0x2, 0x1)
    OP_31(0x10, 0x5, 0x0)

    label("loc_452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_465")
    OP_31(0x11, 0x5, 0x64)

    label("loc_465")

    Jump("loc_496")

    label("loc_468")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47B")
    OP_31(0x10, 0x5, 0x64)

    label("loc_47B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_493")
    OP_31(0x11, 0x2, 0x1)
    OP_31(0x11, 0x5, 0x0)

    label("loc_493")

    Jump("loc_496")

    label("loc_496")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #4
        0xFE,
        "怎么样，满足了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "那就赶快\x01",
            "鼓起干劲出发吧。\x02",
        )
    )

    Jump("loc_4F0")

    label("loc_4F0")

    CloseMessageWindow()
    Jump("loc_547")

    label("loc_4F4")


    ChrTalk(    #6
        0xFE,
        "这样啊，不接受帮助吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "那你们就\x01",
            "好好努力干吧。\x02",
        )
    )

    Jump("loc_546")

    label("loc_546")

    CloseMessageWindow()

    label("loc_547")

    TalkEnd(0xFE)
    Return()

    # Function_3_19C end

    def Function_4_54B(): pass

    label("Function_4_54B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-62140, 3940, 188700, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -63680, 3950, 188120, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -62400, 3950, 188260, 180)
    OP_4A(0x10, 255)
    SetChrPos(0x113, -64780, 4070, 185560, 0)
    SetChrPos(0x111, -63880, 4070, 185560, 0)
    SetChrPos(0x112, -62980, 4070, 185560, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x11,
        (
            "#051F#5P这里就是你们一直期盼的\x01",
            "最终考试的会场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x111,
        "#1743F#12P这、这样的地方居然有洞窟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x112,
        "#1750F#12P嘿，我们是要进到这里面去吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        "#1765F#6P哼，又是骗小孩子的伎俩。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#053F#5P……考试的内容\x01",
            "就是刚才所说的。\x02\x03",

            "#051F我就先走一步，在里面等着你们啦。\x01",
            "你们给我打起精神，赶快跟上来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 500)
    Sleep(200)

    def lambda_76B():
        OP_8E(0xFE, 0xFFFF0740, 0xFAA, 0x2EB80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_76B)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)

    ChrTalk(    #13
        0x10,
        (
            "#5P我来担当\x01",
            "你们的后援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#5P我会为你们安排\x01",
            "简单的食宿，\x01",
            "如果遇到什么危险就回到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x113,
        "#1761F#6P『如果遇到什么危险』吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x112,
        "#1751F#12P不过，应该没啥大不了的吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        "#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x10, 90, 500)

    def lambda_890():
        OP_8E(0xFE, 0xFFFF1280, 0xF82, 0x2DCD0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_890)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 500)
    Sleep(300)

    ChrTalk(    #18
        0x111,
        "#1741F#12P好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x112,
        "#1750F#12P那就……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x113,
        "#1761F#6P开始干吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F90)
    OP_C2(0x1, 0x4)
    OP_31(0x10, 0x10, 0x2D)
    OP_31(0x10, 0xFE, 0x0)
    OP_31(0x10, 0x5, 0x0)
    OP_35(0x10, 0xFFFF)
    OP_34(0x10, 0xFFFF)
    OP_35(0x10, 0x0)
    OP_BB(0x10, 0x6, 0x0)
    OP_41(0x10, 0x0, 0xFF)
    OP_41(0x10, 0x605, 0xFF)
    OP_41(0x10, 0x640, 0xFF)
    OP_41(0x10, 0x80, 0xFF)
    OP_31(0x11, 0x10, 0x2D)
    OP_31(0x11, 0xFE, 0x0)
    OP_31(0x11, 0x5, 0x0)
    OP_35(0x11, 0xFFFF)
    OP_34(0x11, 0xFFFF)
    OP_35(0x11, 0x0)
    OP_BB(0x11, 0x6, 0x0)
    OP_41(0x11, 0x0, 0xFF)
    OP_41(0x11, 0x605, 0xFF)
    OP_41(0x11, 0x640, 0xFF)
    OP_41(0x11, 0x80, 0xFF)
    OP_31(0x12, 0x10, 0x2D)
    OP_31(0x12, 0xFE, 0x0)
    OP_31(0x12, 0x5, 0x0)
    OP_35(0x12, 0xFFFF)
    OP_34(0x12, 0xFFFF)
    OP_35(0x12, 0x0)
    OP_BB(0x2, 0x6, 0x0)
    OP_41(0x12, 0x0, 0xFF)
    OP_41(0x12, 0x605, 0xFF)
    OP_41(0x12, 0x640, 0xFF)
    OP_41(0x12, 0x80, 0xFF)
    OP_3E(0x1D6, 3)
    OP_3E(0x1D7, 2)
    OP_3E(0x1D8, 2)
    OP_3E(0x1D9, 4)
    OP_3E(0x1DA, 2)
    OP_3E(0x13E, 1)
    OP_3E(0x1F0, 1)
    EventEnd(0x0)
    OP_4B(0x10, 255)
    Return()

    # Function_4_54B end

    def Function_5_9E6(): pass

    label("Function_5_9E6")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A83")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21")

    ChrTalk(    #21
        0x111,
        "#1740F呼，赶快回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A80")

    label("loc_A21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(    #22
        0x112,
        "#1750F好了，回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A80")

    label("loc_A51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A80")

    ChrTalk(    #23
        0x113,
        "#1763F哼，赶快回去了。\x02",
    )

    CloseMessageWindow()

    label("loc_A80")

    Jump("loc_D87")

    label("loc_A83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C21")
    OP_4A(0x10, 255)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B01")

    ChrTalk(    #24
        0x10,
        "#6P怎么，放弃了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#6P嗯，也好。\x01",
            "知难而退也很重要嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAD")

    label("loc_B01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B66")

    ChrTalk(    #26
        0x10,
        "#6P怎么，放弃了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#6P嗯，也好。\x01",
            "知难而退也很重要嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAD")

    label("loc_B66")


    ChrTalk(    #28
        0x10,
        "怎么，放弃了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "嗯，也好。\x01",
            "知难而退也很重要嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAD")


    ChrTalk(    #30
        0x111,
        "#1741F嘁，谁要……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x113,
        "#1763F怎么可能放弃嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x112,
        "#1756F好了，回去吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_8C(0x10, 270, 0)
    OP_4B(0x10, 255)
    Jump("loc_D87")

    label("loc_C21")

    OP_4A(0x10, 255)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8D")

    ChrTalk(    #33
        0x10,
        "#6P哦，你们两个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#6P想丢下同伴\x01",
            "就这样逃走吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D31")

    label("loc_C8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEE")

    ChrTalk(    #35
        0x10,
        "#6P哦，你们两个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#6P想丢下同伴\x01",
            "就这样逃走吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D31")

    label("loc_CEE")


    ChrTalk(    #37
        0x10,
        "哦，你们两个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "想丢下同伴\x01",
            "就这样逃走吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D31")


    ChrTalk(    #39
        0x111,
        "#1744F哎，很不巧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x112,
        "#1750F我们可没那么薄情呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_8C(0x10, 270, 0)
    OP_4B(0x10, 255)

    label("loc_D87")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_9E6 end

    SaveToFile()

Try(main)
