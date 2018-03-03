from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3112   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Target Camera',                        # 9
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_101",          # 01, 1
        "Function_2_102",          # 02, 2
        "Function_3_410",          # 03, 3
        "Function_4_44D",          # 04, 4
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_F5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_F9")

    label("loc_F5")

    Event(0, 4)

    label("loc_F9")

    Jump("loc_100")

    label("loc_FC")

    Event(0, 4)

    label("loc_100")

    Return()

    # Function_0_CA end

    def Function_1_101(): pass

    label("Function_1_101")

    Return()

    # Function_1_101 end

    def Function_2_102(): pass

    label("Function_2_102")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x53)
    OP_6D(1780, 0, 2220, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x107, -40, 0, -1160, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x107, 0x4)
    Sleep(2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_191():
        OP_6D(1600, 0, 2860, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_191)
    OP_43(0x107, 0x0, 0x0, 0x3)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x107, 270, 400)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #0
        0x107,
        (
            "#561F#40WI know all of what Mom's saying is true...\x02\x03",

            "I know... Really, I do...\x02\x03",

            "#069FBut... But...\x02\x03",

            "But then what am I supposed to do?!\x02\x03",

            "#068FJust sit around helplessly?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #1
        0x107,
        (
            "#561F#40W...I know. I'll go and see what Dad thinks.\x02\x03",

            "Maybe he'll actually listen to me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x107, 90, 400)

    def lambda_31E():
        OP_6D(2500, 0, 2870, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_31E)

    def lambda_336():
        OP_8E(0xFE, 0x690, 0x0, 0x578, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_336)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Tita inserted a card into a slot in the elevator panel.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    OP_77(0xFF, 0x64, 0x64, 0x0, 0x0)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(2500, 11900, 2870, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_102 end

    def Function_3_410(): pass

    label("Function_3_410")


    def lambda_416():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_416)

    def lambda_428():
        OP_8F(0xFE, 0x5A, 0x0, 0x622, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_428)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x6D, 0x0, 0x64)
    Return()

    # Function_3_410 end

    def Function_4_44D(): pass

    label("Function_4_44D")

    ClearMapFlags(0x1)
    EventBegin(0x1)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6D(1400, 0, 4500, 0)
    SetChrPos(0x0, 1750, 0, 1370, 90)
    SetChrPos(0x1, 1280, 0, 2600, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C7")
    SetChrPos(0x2, 70, 0, 1470, 180)

    label("loc_4C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E4")
    SetChrPos(0x3, -50, 0, 2600, 180)

    label("loc_4E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_501")
    SetChrPos(0x4, -1380, 0, 1470, 180)

    label("loc_501")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E")
    SetChrPos(0x5, -1380, 0, 2600, 180)

    label("loc_51E")

    Sleep(200)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[ RF ]\x01",        # 0
            "[ 5F ]\x01",        # 1
            "[ 4F ]\x01",        # 2
            "[ 3F ]\x01",        # 3
            "[ 2F ]\x01",        # 4
            "[ 1F ]\x01",        # 5
            "★[ B1 ]\x01",      # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C5")

    label("loc_594")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[ RF ]\x01",        # 0
            "[ 5F ]\x01",        # 1
            "[ 4F ]\x01",        # 2
            "[ 3F ]\x01",        # 3
            "[ 2F ]\x01",        # 4
            "★[ 1F ]\x01",      # 5
            "[ B1 ]\x01",        # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C5")

    label("loc_5F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_650")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[ RF ]\x01",        # 0
            "[ 5F ]\x01",        # 1
            "[ 4F ]\x01",        # 2
            "[ 3F ]\x01",        # 3
            "★[ 2F ]\x01",      # 4
            "[ 1F ]\x01",        # 5
            "[ B1 ]\x01",        # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C5")

    label("loc_650")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[ RF ]\x01",        # 0
            "[ 5F ]\x01",        # 1
            "[ 4F ]\x01",        # 2
            "★[ 3F ]\x01",      # 3
            "[ 2F ]\x01",        # 4
            "[ 1F ]\x01",        # 5
            "[ B1 ]\x01",        # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C5")

    label("loc_6AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70C")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[ RF ]\x01",        # 0
            "[ 5F ]\x01",        # 1
            "★[ 4F ]\x01",      # 2
            "[ 3F ]\x01",        # 3
            "[ 2F ]\x01",        # 4
            "[ 1F ]\x01",        # 5
            "[ B1 ]\x01",        # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C5")

    label("loc_70C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[ RF ]\x01",        # 0
            "★[ 5F ]\x01",      # 1
            "[ 4F ]\x01",        # 2
            "[ 3F ]\x01",        # 3
            "[ 2F ]\x01",        # 4
            "[ 1F ]\x01",        # 5
            "[ B1 ]\x01",        # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C5")

    label("loc_76A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C5")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★[ RF ]\x01",      # 0
            "[ 5F ]\x01",        # 1
            "[ 4F ]\x01",        # 2
            "[ 3F ]\x01",        # 3
            "[ 2F ]\x01",        # 4
            "[ 1F ]\x01",        # 5
            "[ B1 ]\x01",        # 6
            "[Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C5")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80B")
    Jump("loc_876")

    label("loc_80B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_842")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, -11900, 4500, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)
    Jump("loc_876")

    label("loc_842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_876")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, 11900, 4500, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)

    label("loc_876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_8A8"),
        (1, "loc_8B4"),
        (2, "loc_8C0"),
        (3, "loc_8CC"),
        (4, "loc_8D8"),
        (5, "loc_8E4"),
        (6, "loc_8F0"),
        (SWITCH_DEFAULT, "loc_8FC"),
    )


    label("loc_8A8")

    NewScene("ED6_DT21/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8B4")

    NewScene("ED6_DT21/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8C0")

    NewScene("ED6_DT21/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8CC")

    NewScene("ED6_DT21/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8D8")

    NewScene("ED6_DT21/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8E4")

    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8F0")

    NewScene("ED6_DT21/T3101   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_8FC")

    label("loc_8FC")

    Jump("loc_9BE")

    label("loc_8FF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_924"),
        (1, "loc_93A"),
        (2, "loc_950"),
        (3, "loc_966"),
        (4, "loc_97C"),
        (5, "loc_992"),
        (6, "loc_9A8"),
        (SWITCH_DEFAULT, "loc_9BE"),
    )


    label("loc_924")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_93A")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_950")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_966")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_97C")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_992")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_9A8")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3101   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_9BE")

    label("loc_9BE")

    Return()

    # Function_4_44D end

    SaveToFile()

Try(main)
