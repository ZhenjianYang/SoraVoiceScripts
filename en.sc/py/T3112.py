from ED6SCScenarioHelper import *

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
        "Function_1_AF",           # 01, 1
        "Function_2_C6",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Event(0, 2)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5")
    OP_71(0x0, 0x4)
    OP_79(0xFF, 0x2)
    OP_7B()

    label("loc_C5")

    Return()

    # Function_1_AF end

    def Function_2_C6(): pass

    label("Function_2_C6")

    ClearMapFlags(0x1)
    EventBegin(0x1)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6D(1400, 0, 4500, 0)
    SetChrPos(0x0, 1750, 0, 1370, 90)
    SetChrPos(0x1, 1280, 0, 2600, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140")
    SetChrPos(0x2, 70, 0, 1470, 180)

    label("loc_140")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D")
    SetChrPos(0x3, -50, 0, 2600, 180)

    label("loc_15D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A")
    SetChrPos(0x4, -1380, 0, 1470, 180)

    label("loc_17A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197")
    SetChrPos(0x5, -1380, 0, 2600, 180)

    label("loc_197")

    Sleep(200)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [ RF ]\x01",        # 0
            "  [ 5F ]\x01",        # 1
            "  [ 4F ]\x01",        # 2
            "  [ 3F ]\x01",        # 3
            "  [ 2F ]\x01",        # 4
            "  [ 1F ]\x01",        # 5
            "★[ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_21B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [ RF ]\x01",        # 0
            "  [ 5F ]\x01",        # 1
            "  [ 4F ]\x01",        # 2
            "  [ 3F ]\x01",        # 3
            "  [ 2F ]\x01",        # 4
            "★[ 1F ]\x01",        # 5
            "  [ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_287")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [ RF ]\x01",        # 0
            "  [ 5F ]\x01",        # 1
            "  [ 4F ]\x01",        # 2
            "  [ 3F ]\x01",        # 3
            "★[ 2F ]\x01",        # 4
            "  [ 1F ]\x01",        # 5
            "  [ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_2F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [ RF ]\x01",        # 0
            "  [ 5F ]\x01",        # 1
            "  [ 4F ]\x01",        # 2
            "★[ 3F ]\x01",        # 3
            "  [ 2F ]\x01",        # 4
            "  [ 1F ]\x01",        # 5
            "  [ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_35F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [ RF ]\x01",        # 0
            "  [ 5F ]\x01",        # 1
            "★[ 4F ]\x01",        # 2
            "  [ 3F ]\x01",        # 3
            "  [ 2F ]\x01",        # 4
            "  [ 1F ]\x01",        # 5
            "  [ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_3CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [ RF ]\x01",        # 0
            "★[ 5F ]\x01",        # 1
            "  [ 4F ]\x01",        # 2
            "  [ 3F ]\x01",        # 3
            "  [ 2F ]\x01",        # 4
            "  [ 1F ]\x01",        # 5
            "  [ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_437")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★[ RF ]\x01",        # 0
            "  [ 5F ]\x01",        # 1
            "  [ 4F ]\x01",        # 2
            "  [ 3F ]\x01",        # 3
            "  [ 2F ]\x01",        # 4
            "  [ 1F ]\x01",        # 5
            "  [ B1 ]\x01",        # 6
            "  [Cancel]\x01",      # 7
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A0")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E6")
    Jump("loc_551")

    label("loc_4E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51D")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, -11900, 4500, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)
    Jump("loc_551")

    label("loc_51D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_551")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, 11900, 4500, 2000)
    OP_0D()
    Sleep(800)
    OP_23(0x67)

    label("loc_551")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DA")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_583"),
        (1, "loc_58F"),
        (2, "loc_59B"),
        (3, "loc_5A7"),
        (4, "loc_5B3"),
        (5, "loc_5BF"),
        (6, "loc_5CB"),
        (SWITCH_DEFAULT, "loc_5D7"),
    )


    label("loc_583")

    NewScene("ED6_DT21/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_58F")

    NewScene("ED6_DT21/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_59B")

    NewScene("ED6_DT21/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_5A7")

    NewScene("ED6_DT21/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_5B3")

    NewScene("ED6_DT21/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_5BF")

    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_5CB")

    NewScene("ED6_DT21/T3101   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_5D7")

    label("loc_5D7")

    Jump("loc_699")

    label("loc_5DA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5FF"),
        (1, "loc_615"),
        (2, "loc_62B"),
        (3, "loc_641"),
        (4, "loc_657"),
        (5, "loc_66D"),
        (6, "loc_683"),
        (SWITCH_DEFAULT, "loc_699"),
    )


    label("loc_5FF")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_615")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_62B")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_641")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_657")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_66D")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_683")

    OP_22(0xE, 0x0, 0x64)
    Sleep(500)
    NewScene("ED6_DT21/T3101   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_699")

    label("loc_699")

    Return()

    # Function_2_C6 end

    SaveToFile()

Try(main)
