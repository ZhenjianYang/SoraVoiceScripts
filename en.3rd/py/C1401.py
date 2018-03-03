from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1401   ._SN',
        MapName             = 'Bose',
        Location            = 'C1401.x',
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
        "Function_1_FF",           # 01, 1
        "Function_2_106",          # 02, 2
        "Function_3_283",          # 03, 3
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6")

    label("loc_D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_FE")

    Return()

    # Function_0_CA end

    def Function_1_FF(): pass

    label("Function_1_FF")

    OP_71(0x401, 0x0)
    ExitThread()
    Return()

    # Function_1_FF end

    def Function_2_106(): pass

    label("Function_2_106")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_26D")

    label("loc_12B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_26D")

    label("loc_144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_26D")

    label("loc_15D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_26D")

    label("loc_176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_26D")

    label("loc_18F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_26D")

    label("loc_1A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_26D")

    label("loc_1C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_26D")

    label("loc_1DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_26D")

    label("loc_1F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_26D")

    label("loc_20C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_225")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_26D")

    label("loc_225")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_26D")

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_26D")

    label("loc_257")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_26D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_282")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_26D")

    label("loc_282")

    Return()

    # Function_2_106 end

    def Function_3_283(): pass

    label("Function_3_283")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x00#40W'Why don't you guys try becoming bracers?'\x01",
            "#500W \x01",
            "#40WThose words were all it took to set the\x01",
            "wheels in motion.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00#40WThe three young men Estelle had spoken to,\x01",
            "Deen, Rais, and Rocco, were the leaders of a\x01",
            "group of delinquents who spent most of their\x01",
            "time in the warehouse district of Ruan...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x00#40WIn light of the unprecedented chaos that\x01",
            "swept over Liberl, they soon began\x01",
            "reexamining themselves and their lives...\x01",
            "#500W \x01",
            "#40Wand after much thought, they agreed that\x01",
            "the path of a bracer--a protector of the land's\x01",
            "peace and its people's safety--may be the best\x01",
            "road forward for them.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x00#40WThat's not to say, however, that they didn't\x01",
            "have any ulterior motives.\x01",
            "#500W \x01",
            "#40WNo, no, no. They did think it would also give\x01",
            "them the opportunity to be trained directly by\x01",
            "the guild's Carna.\x01",
            "#500W \x01",
            "#40WWith this hope in their hearts, they made\x01",
            "their way to the Ruan Bracer Guild and expressed\x01",
            "interest in joining.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x00#40WBut the guild's crafty receptionist, Jean,\x01",
            "had other ideas swirling in his brain...\x01",
            "#500W \x01",
            "#40Wand unfortunately for them, they were\x01",
            "to receive their training from their longtime\x01",
            "sworn enemy and former Raven group leader,\x01",
            "Agate Crosner.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x00#40WTheir grueling training began in earnest under \x01",
            "his strict guidance.\x01",
            "#500W \x01",
            "#40WAfter roughly three months of pure hell,\x01",
            "the end was finally in sight.\x01",
            "#500W \x01",
            "#40WOnly today's final examination remained...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(-6340, 2000, 107480, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(450, 0)
    OP_1D(0x16)
    Sleep(500)
    FadeToBright(2000, 0)

    def lambda_8AA():
        OP_67(0, 8000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8AA)

    def lambda_8C2():
        OP_6E(356, 10000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8C2)
    WaitChrThread(0x10, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_283 end

    SaveToFile()

Try(main)
