from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5508   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5508.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_C0",           # 01, 1
        "Function_2_C6",           # 02, 2
        "Function_3_640",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_BF")

    Return()

    # Function_0_AA end

    def Function_1_C0(): pass

    label("Function_1_C0")

    OP_1B(0x1, 0x0, 0x3)
    Return()

    # Function_1_C0 end

    def Function_2_C6(): pass

    label("Function_2_C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -1700, 0, -31490, 0)
    SetChrPos(0x102, -360, 0, -31750, 0)
    SetChrPos(0xF0, -1810, 0, -33150, 0)
    SetChrPos(0xF1, -440, 0, -33460, 0)
    OP_6D(-800, 20100, -21880, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(0, 0)
    OP_6E(293, 0)

    def lambda_159():
        OP_6D(-800, 6500, -20080, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_159)

    def lambda_171():
        OP_67(0, 4600, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_171)

    def lambda_189():
        OP_6B(4000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_189)

    def lambda_199():
        OP_6E(293, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_199)
    FadeToBright(2000, 0)

    def lambda_1B2():
        OP_8E(0xFE, 0xFFFFFA92, 0x0, 0xFFFFBF46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B2)
    Sleep(200)

    def lambda_1D2():
        OP_8E(0xFE, 0xFFFFFFEC, 0x0, 0xFFFFBEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D2)
    Sleep(230)

    def lambda_1F2():
        OP_8E(0xFE, 0xFFFFF90C, 0x0, 0xFFFFB82A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1F2)
    Sleep(150)

    def lambda_212():
        OP_8E(0xFE, 0x1A4, 0x0, 0xFFFFB6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_212)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(1000)
    OP_6D(130, 0, -15780, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(269, 0)
    SetChrPos(0x109, -1620, 0, -16239, 0)
    SetChrPos(0x102, -100, 0, -16370, 0)
    SetChrPos(0xF0, -1760, 0, -17880, 0)
    SetChrPos(0xF1, -180, 0, -17880, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F")

    ChrTalk(    #0
        0x10D,
        (
            "#270F#6P嗯……\x01",
            "这是相当正式的设施啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0")

    label("loc_30F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_350")

    ChrTalk(    #1
        0x10E,
        (
            "#178F#6P这是……\x01",
            "相当正式的设施啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0")

    label("loc_350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F")

    ChrTalk(    #2
        0x108,
        (
            "#073F#6P哦……\x01",
            "这可是相当正式啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0")

    label("loc_38F")


    ChrTalk(    #3
        0x109,
        (
            "#1079F#5P这是……\x01",
            "相当正式的设施呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_484")

    ChrTalk(    #4
        0x10A,
        (
            "#1316F#6P嗯，里面结构很复杂，\x01",
            "要探索的确挺辛苦的。\x02\x03",

            "#812F还有一片漆黑什么也看不见\x01",
            "的为难地方。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_481")

    ChrTalk(    #5
        0x103,
        (
            "#1525F#6P是啊，\x01",
            "我当时也吃够了苦头呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481")

    Jump("loc_59B")

    label("loc_484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_512")

    ChrTalk(    #6
        0x103,
        (
            "#1525F#6P嗯，里面结构很复杂，\x01",
            "我当时也吃够了苦头呢。\x02\x03",

            "#1522F还有一片漆黑什么也看不见\x01",
            "的阴险至极的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59B")

    label("loc_512")


    ChrTalk(    #7
        0x102,
        (
            "#1502F#11P这里大概……\x01",
            "是艾丝蒂尔她们进行\x01",
            "最终训练的地方吧。\x02\x03",

            "#1505F听说内部很复杂，\x01",
            "还有关了灯就什么都看不见的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59B")


    ChrTalk(    #8
        0x109,
        (
            "#1067F#5P嗯，\x01",
            "似乎应该做好面对陷阱的准备……\x02\x03",

            "#1063F最后的『修炼场』……\x01",
            "打起精神冲进去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1502F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290B)
    OP_28(0x34, 0x1, 0x1)
    OP_28(0x34, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_C6 end

    def Function_3_640(): pass

    label("Function_3_640")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_663")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_674")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_674")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_674")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_699"),
        (1, "loc_6C8"),
        (2, "loc_6F7"),
        (SWITCH_DEFAULT, "loc_726"),
    )


    label("loc_699")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_726")

    label("loc_6C8")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_726")

    label("loc_6F7")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_726")

    label("loc_726")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_786"),
        (1, "loc_7B2"),
        (2, "loc_7EF"),
        (SWITCH_DEFAULT, "loc_841"),
    )


    label("loc_786")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_841")

    label("loc_7B2")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_841")

    label("loc_7EF")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_841")

    label("loc_841")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_86B"),
        (1, "loc_8FF"),
        (2, "loc_995"),
        (3, "loc_A2B"),
        (SWITCH_DEFAULT, "loc_AC5"),
    )


    label("loc_86B")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_8CA")

    label("loc_8CA")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8EC"),
        (1, "loc_8F9"),
        (SWITCH_DEFAULT, "loc_8FC"),
    )


    label("loc_8EC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FC")

    label("loc_8F9")

    Jump("loc_8FC")

    label("loc_8FC")

    Jump("loc_AC5")

    label("loc_8FF")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #11
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_960")

    label("loc_960")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_982"),
        (1, "loc_98F"),
        (SWITCH_DEFAULT, "loc_992"),
    )


    label("loc_982")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_992")

    label("loc_98F")

    Jump("loc_992")

    label("loc_992")

    Jump("loc_AC5")

    label("loc_995")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_9F6")

    label("loc_9F6")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A18"),
        (1, "loc_A25"),
        (SWITCH_DEFAULT, "loc_A28"),
    )


    label("loc_A18")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A28")

    label("loc_A25")

    Jump("loc_A28")

    label("loc_A28")

    Jump("loc_AC5")

    label("loc_A2B")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_A90")

    label("loc_A90")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AB2"),
        (1, "loc_ABF"),
        (SWITCH_DEFAULT, "loc_AC2"),
    )


    label("loc_AB2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC2")

    label("loc_ABF")

    Jump("loc_AC2")

    label("loc_AC2")

    Jump("loc_AC5")

    label("loc_AC5")

    Jump("loc_75B")

    label("loc_AC8")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_AE1"),
        (1, "loc_B15"),
        (2, "loc_B49"),
        (3, "loc_B7D"),
        (SWITCH_DEFAULT, "loc_BB1"),
    )


    label("loc_AE1")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_BB1")

    label("loc_B15")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_BB1")

    label("loc_B49")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_BB1")

    label("loc_B7D")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_BB1")

    label("loc_BB1")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BD3"),
        (1, "loc_BF3"),
        (2, "loc_BFF"),
        (3, "loc_C0B"),
        (SWITCH_DEFAULT, "loc_C17"),
    )


    label("loc_BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE7")
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_BF0")

    label("loc_BE7")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_BF0")

    Jump("loc_C17")

    label("loc_BF3")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C17")

    label("loc_BFF")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_C17")

    label("loc_C0B")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_C17")

    label("loc_C17")

    Return()

    # Function_3_640 end

    SaveToFile()

Try(main)
