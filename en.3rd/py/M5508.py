from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_3_7BB",          # 03, 3
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_319")

    ChrTalk(    #0
        0x10D,
        "#270F#6PThis is quite an impressive training facility.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F0")

    label("loc_319")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_366")

    ChrTalk(    #1
        0x10E,
        "#178F#6PThis is quite an impressive training facility.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F0")

    label("loc_366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1")

    ChrTalk(    #2
        0x108,
        "#073F#6PMan... They spared no expense with this one.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F0")

    label("loc_3B1")


    ChrTalk(    #3
        0x109,
        (
            "#1079F#5PNow THIS is one fancy-lookin'\x01",
            "training facility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_528")

    ChrTalk(    #4
        0x10A,
        (
            "#1316F#6PIt's crazy complicated inside, too. Estelle and\x01",
            "I had a blast trying to get through it when we\x01",
            "were here.\x02\x03",

            "#812FEspecially the rooms where it's pitch black.\x01",
            "Those were juuust aweeesome... Not.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_525")

    ChrTalk(    #5
        0x103,
        (
            "#1525F#6PI remember having my fair share of trouble\x01",
            "with those, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525")

    Jump("loc_6D7")

    label("loc_528")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_624")

    ChrTalk(    #6
        0x103,
        (
            "#1525F#6PIt's a real maze inside. I can still remember\x01",
            "what a major pain it was getting through it\x01",
            "to this day.\x02\x03",

            "#1522FThere're even rooms which have no lighting \x01",
            "whatsoever...and I'm sure you can imagine\x01",
            "how dangerous THOSE are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D7")

    label("loc_624")


    ChrTalk(    #7
        0x102,
        (
            "#1502F#11PI think this is the place Estelle did her final\x01",
            "training exercise.\x02\x03",

            "#1505FSupposedly the inside's similar to a maze,\x01",
            "and there are even parts that are pitch\x01",
            "black.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D7")


    ChrTalk(    #8
        0x109,
        (
            "#1067F#5PCan't wait to see what kinda traps we bump\x01",
            "into inside, then.\x02\x03",

            "#1063FAnyway, as far as I can tell, this should be our\x01",
            "final ordeal on this plane... Let's get this done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1502F#11PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290B)
    OP_28(0x34, 0x1, 0x1)
    OP_28(0x34, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_C6 end

    def Function_3_7BB(): pass

    label("Function_3_7BB")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_7DE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EF")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_7EF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EF")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_814"),
        (1, "loc_843"),
        (2, "loc_872"),
        (SWITCH_DEFAULT, "loc_8A1"),
    )


    label("loc_814")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_8A1")

    label("loc_843")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_8A1")

    label("loc_872")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_8A1")

    label("loc_8A1")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDB")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_901"),
        (1, "loc_92D"),
        (2, "loc_96E"),
        (SWITCH_DEFAULT, "loc_9C2"),
    )


    label("loc_901")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_9C2")

    label("loc_92D")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_9C2")

    label("loc_96E")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_9C2")

    label("loc_9C2")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9EC"),
        (1, "loc_A63"),
        (2, "loc_ADE"),
        (3, "loc_B5C"),
        (SWITCH_DEFAULT, "loc_BD8"),
    )


    label("loc_9EC")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05Travel to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A50"),
        (1, "loc_A5D"),
        (SWITCH_DEFAULT, "loc_A60"),
    )


    label("loc_A50")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A60")

    label("loc_A5D")

    Jump("loc_A60")

    label("loc_A60")

    Jump("loc_BD8")

    label("loc_A63")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #11
        "\x07\x05Travel to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ACB"),
        (1, "loc_AD8"),
        (SWITCH_DEFAULT, "loc_ADB"),
    )


    label("loc_ACB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADB")

    label("loc_AD8")

    Jump("loc_ADB")

    label("loc_ADB")

    Jump("loc_BD8")

    label("loc_ADE")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05Travel to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B49"),
        (1, "loc_B56"),
        (SWITCH_DEFAULT, "loc_B59"),
    )


    label("loc_B49")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B59")

    label("loc_B56")

    Jump("loc_B59")

    label("loc_B59")

    Jump("loc_BD8")

    label("loc_B5C")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05Travel to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BC5"),
        (1, "loc_BD2"),
        (SWITCH_DEFAULT, "loc_BD5"),
    )


    label("loc_BC5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BD5")

    label("loc_BD2")

    Jump("loc_BD5")

    label("loc_BD5")

    Jump("loc_BD8")

    label("loc_BD8")

    Jump("loc_8D6")

    label("loc_BDB")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BF4"),
        (1, "loc_C28"),
        (2, "loc_C5C"),
        (3, "loc_C90"),
        (SWITCH_DEFAULT, "loc_CC4"),
    )


    label("loc_BF4")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_CC4")

    label("loc_C28")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_CC4")

    label("loc_C5C")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_CC4")

    label("loc_C90")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_CC4")

    label("loc_CC4")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_CE6"),
        (1, "loc_D06"),
        (2, "loc_D12"),
        (3, "loc_D1E"),
        (SWITCH_DEFAULT, "loc_D2A"),
    )


    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFA")
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_D03")

    label("loc_CFA")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_D03")

    Jump("loc_D2A")

    label("loc_D06")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_D2A")

    label("loc_D12")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_D2A")

    label("loc_D1E")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_D2A")

    label("loc_D2A")

    Return()

    # Function_3_7BB end

    SaveToFile()

Try(main)
