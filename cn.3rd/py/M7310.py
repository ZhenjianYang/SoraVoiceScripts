from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7310   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60224",
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


    DeclActor(
        TriggerX            = -2440,
        TriggerZ            = 6800,
        TriggerY            = -70,
        TriggerRange        = 1000,
        ActorX              = -2440,
        ActorZ              = 8800,
        ActorY              = -70,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_10D",          # 01, 1
        "Function_2_12A",          # 02, 2
        "Function_3_2E9",          # 03, 3
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF")
    OP_A3(0x2C15)
    OP_A3(0x2C16)
    OP_A3(0x2C17)
    OP_A3(0x2C18)

    label("loc_EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x583, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_10C")

    Return()

    # Function_0_CE end

    def Function_1_10D(): pass

    label("Function_1_10D")

    OP_16(0x2, 0xFA0, 0xFFFE4698, 0xFFFE0C00, 0x23009D)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    Return()

    # Function_1_10D end

    def Function_2_12A(): pass

    label("Function_2_12A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_157")

    label("loc_157")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C3")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_1BC")

    label("loc_1BC")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D9"),
        (1, "loc_255"),
        (2, "loc_284"),
        (SWITCH_DEFAULT, "loc_2B3"),
    )


    label("loc_1D9")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C0")

    label("loc_255")

    OP_A9(0x31)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_281")

    label("loc_281")

    Jump("loc_2C0")

    label("loc_284")

    OP_A9(0xD)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2B0")

    label("loc_2B0")

    Jump("loc_2C0")

    label("loc_2B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C0")

    label("loc_2C0")

    Jump("loc_16A")

    label("loc_2C3")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    SetMapFlags(0x100000)
    Return()

    # Function_2_12A end

    def Function_3_2E9(): pass

    label("Function_3_2E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A2(0x2C19)
    LoadEffect(0x0, "map\\mp252_04.eff")
    SetChrPos(0x0, 1000, 6800, -1000, 90)
    SetChrPos(0x1, 1000, 6800, 1000, 90)
    SetChrPos(0x2, -1000, 6800, -1000, 90)
    SetChrPos(0x3, -1000, 6800, 1000, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_6D(16450, 5440, -420, 0)
    OP_67(0, 17420, -10000, 0)
    OP_6B(5540, 0)
    OP_6C(290000, 0)
    OP_6E(262, 0)

    def lambda_3ED():
        OP_6D(430, 6800, 180, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3ED)

    def lambda_405():
        OP_67(0, 13500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_405)

    def lambda_41D():
        OP_6B(3880, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_41D)

    def lambda_42D():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_42D)

    def lambda_43D():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_43D)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C8(0x200, 0x46, "C_PLAC37._CH", 0x1, 0x3E8)
    WaitChrThread(0x0, 0x0)
    FadeToBright(2000, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x162, 0x0, 0x64)
    Sleep(2000)

    def lambda_55D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_55D)

    def lambda_56F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_56F)

    def lambda_581():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_581)

    def lambda_593():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_593)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    OP_83(0x0, 0x2)
    OP_83(0x1, 0x2)
    OP_83(0x2, 0x2)
    OP_83(0x3, 0x2)
    Sleep(2000)
    Fade(1000)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_2E9 end

    SaveToFile()

Try(main)
