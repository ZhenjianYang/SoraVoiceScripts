from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5508   ._SN',
        MapName             = 'Other',
        Location            = 'C5508.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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


    DeclEvent(
        X                   = -8100,
        Y                   = -200,
        Z                   = -42000,
        Range               = 5600,
        Unknown_10          = 0x1C20,
        Unknown_14          = 0xFFFF7874,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_F2",           # 02, 2
        "Function_3_5EA",          # 03, 3
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_DB")

    Return()

    # Function_0_CA end

    def Function_1_DC(): pass

    label("Function_1_DC")

    OP_10(0x1, 0x0)
    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFDCD80, 0x230070)
    Return()

    # Function_1_DC end

    def Function_2_F2(): pass

    label("Function_2_F2")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_110")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_121")

    label("loc_110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_121")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_121")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_192")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1BD"),
        (1, "loc_1E9"),
        (2, "loc_22A"),
        (SWITCH_DEFAULT, "loc_27E"),
    )


    label("loc_1BD")


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

    Jump("loc_27E")

    label("loc_1E9")


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

    Jump("loc_27E")

    label("loc_22A")


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

    Jump("loc_27E")

    label("loc_27E")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A8"),
        (1, "loc_321"),
        (2, "loc_39E"),
        (3, "loc_41E"),
        (SWITCH_DEFAULT, "loc_49C"),
    )


    label("loc_2A8")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05Move to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30E"),
        (1, "loc_31B"),
        (SWITCH_DEFAULT, "loc_31E"),
    )


    label("loc_30E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31E")

    label("loc_31B")

    Jump("loc_31E")

    label("loc_31E")

    Jump("loc_49C")

    label("loc_321")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05Move to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38B"),
        (1, "loc_398"),
        (SWITCH_DEFAULT, "loc_39B"),
    )


    label("loc_38B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39B")

    label("loc_398")

    Jump("loc_39B")

    label("loc_39B")

    Jump("loc_49C")

    label("loc_39E")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05Move to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40B"),
        (1, "loc_418"),
        (SWITCH_DEFAULT, "loc_41B"),
    )


    label("loc_40B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41B")

    label("loc_418")

    Jump("loc_41B")

    label("loc_41B")

    Jump("loc_49C")

    label("loc_41E")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #3
        "\x07\x05Move to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_489"),
        (1, "loc_496"),
        (SWITCH_DEFAULT, "loc_499"),
    )


    label("loc_489")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_499")

    label("loc_496")

    Jump("loc_499")

    label("loc_499")

    Jump("loc_49C")

    label("loc_49C")

    Jump("loc_192")

    label("loc_49F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4B8"),
        (1, "loc_4EC"),
        (2, "loc_520"),
        (3, "loc_554"),
        (SWITCH_DEFAULT, "loc_588"),
    )


    label("loc_4B8")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_588")

    label("loc_4EC")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_588")

    label("loc_520")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_588")

    label("loc_554")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_588")

    label("loc_588")

    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5B9"),
        (1, "loc_5C5"),
        (2, "loc_5D1"),
        (3, "loc_5DD"),
        (SWITCH_DEFAULT, "loc_5E9"),
    )


    label("loc_5B9")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5E9")

    label("loc_5C5")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5E9")

    label("loc_5D1")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_5E9")

    label("loc_5DD")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_5E9")

    label("loc_5E9")

    Return()

    # Function_2_F2 end

    def Function_3_5EA(): pass

    label("Function_3_5EA")

    EventBegin(0x0)
    OP_6D(-770, 500, -3680, 0)
    OP_67(0, 12230, -10000, 0)
    OP_6B(5220, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2000, 0, -31300, 13)
    SetChrPos(0x10A, -200, 0, -31500, 360)
    OP_C8(0x200, 0x46, "C_PLAC03._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_66F():
        OP_6D(-770, 0, -21740, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_66F)
    Sleep(1500)

    def lambda_68C():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0xFFFFAD76, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68C)
    Sleep(400)

    def lambda_6AC():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xFFFFAD76, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6AC)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(-590, 0, -18490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #4
        0x101,
        "#1004F#5PSo this is Grimsel Fortress...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10A,
        (
            "#5P#812FWhoa, this is one weirdo training facility.\x02\x03",

            "Anyway, I don't see or hear anyone\x01",
            "from out here, buuut...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFCE0, 0x0, 0xFFFFB3F2, 0x7D0, 0x0)

    def lambda_7D0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_7D0)
    OP_8C(0x101, 90, 500)
    Sleep(200)
    OP_8C(0x101, 0, 500)
    OP_8C(0x101, 270, 500)
    Sleep(400)
    OP_8C(0x101, 0, 500)
    OP_8C(0x101, 180, 500)
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#1002F#1PYeah, no doubt about it.\x02\x03",

            "You can see the footprints of several people\x01",
            "who've come through here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#811FHaha, looks like that tracking\x01",
            "training actually paid off!\x02\x03",

            "#810FAnyway, given the number of footprint\x01",
            "sets, there can't be that many enemies.\x02\x03",

            "Three people? Maybe four?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F#1POur enemies are good, and they outnumber\x01",
            "us, but...we're senior bracers.\x02\x03",

            "There's nothing we can't beat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        (
            "#816FHeck, yeah!\x01",
            "Let's give it everything we got!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1023)
    OP_28(0x80, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_3_5EA end

    SaveToFile()

Try(main)
