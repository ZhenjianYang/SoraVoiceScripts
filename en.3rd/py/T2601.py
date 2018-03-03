from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2601   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2601.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Anton',                                # 9
        'Academy - Back Road',                  # 10
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
        'ED6_DT07/CH02900 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02900P._CP',             # 00
    )

    DeclNpc(
        X                   = -37100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 315,
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
        X                   = 170,
        Z                   = 0,
        Y                   = -16239,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1000,
        TriggerY            = 9720,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 2000,
        ActorY              = 9720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_128",          # 01, 1
        "Function_2_14D",          # 02, 2
        "Function_3_2CA",          # 03, 3
        "Function_4_306",          # 04, 4
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127")
    ClearChrFlags(0x10, 0x80)

    label("loc_127")

    Return()

    # Function_0_116 end

    def Function_1_128(): pass

    label("Function_1_128")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x23004E)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_71(0x2, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    Return()

    # Function_1_128 end

    def Function_2_14D(): pass

    label("Function_2_14D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2B4")

    label("loc_172")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2B4")

    label("loc_18B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2B4")

    label("loc_1A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2B4")

    label("loc_1BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2B4")

    label("loc_1D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2B4")

    label("loc_1EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2B4")

    label("loc_208")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2B4")

    label("loc_221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2B4")

    label("loc_23A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2B4")

    label("loc_253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2B4")

    label("loc_26C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2B4")

    label("loc_285")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2B4")

    label("loc_29E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2B4")

    label("loc_2C9")

    Return()

    # Function_2_14D end

    def Function_3_2CA(): pass

    label("Function_3_2CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_302")

    ChrTalk(    #0
        0xFE,
        "I'm trying to hide!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Leave me alone!\x02",
    )

    CloseMessageWindow()

    label("loc_302")

    TalkEnd(0xFE)
    Return()

    # Function_3_2CA end

    def Function_4_306(): pass

    label("Function_4_306")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_306 end

    SaveToFile()

Try(main)
