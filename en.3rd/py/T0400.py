from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0400   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0400.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60015",
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
        'Cow',                                  # 9
        'Cow',                                  # 10
        'Chicken',                              # 11
        'Chicken',                              # 12
        'Chicken',                              # 13
        'Chicken',                              # 14
        'Joshua',                               # 15
        'Tio',                                  # 16
        'Elissa',                               # 17
        'Franz',                                # 18
        'Hannah',                               # 19
        'Baby',                                 # 20
        'Dummy',                                # 21
        'Target Camera',                        # 22
        'Milch Main Road',                      # 23
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
        'ED6_DT07/CH01710 ._CH',             # 00
        'ED6_DT07/CH01720 ._CH',             # 01
        'ED6_DT07/CH02750 ._CH',             # 02
        'ED6_DT07/CH02740 ._CH',             # 03
        'ED6_DT07/CH02730 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT26/CH20790 ._CH',             # 07
        'ED6_DT26/CH20791 ._CH',             # 08
        'ED6_DT26/CH20792 ._CH',             # 09
        'ED6_DT26/CH20793 ._CH',             # 0A
        'ED6_DT26/CH20788 ._CH',             # 0B
        'ED6_DT26/CH20789 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01710P._CP',             # 00
        'ED6_DT07/CH01720P._CP',             # 01
        'ED6_DT07/CH02750P._CP',             # 02
        'ED6_DT07/CH02740P._CP',             # 03
        'ED6_DT07/CH02730P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT26/CH20790P._CP',             # 07
        'ED6_DT26/CH20791P._CP',             # 08
        'ED6_DT26/CH20792P._CP',             # 09
        'ED6_DT26/CH20793P._CP',             # 0A
        'ED6_DT26/CH20788P._CP',             # 0B
        'ED6_DT26/CH20789P._CP',             # 0C
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 22850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 48160,
        Z                   = 460,
        Y                   = 18800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 38780,
        Z                   = 0,
        Y                   = 19310,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40470,
        Z                   = 0,
        Y                   = 16320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 25300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xCC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
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


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_34A",          # 02, 2
        "Function_3_4C7",          # 03, 3
        "Function_4_614",          # 04, 4
        "Function_5_63A",          # 05, 5
        "Function_6_654",          # 06, 6
        "Function_7_65A",          # 07, 7
        "Function_8_14B0",         # 08, 8
        "Function_9_2ED2",         # 09, 9
        "Function_10_2F25",        # 0A, 10
        "Function_11_2F6E",        # 0B, 11
        "Function_12_3CAE",        # 0C, 12
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_31D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_32F")

    label("loc_31D")

    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_32F")

    Return()

    # Function_0_2F2 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 0)), scpexpr(EXPR_END)), "loc_340")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_340")

    OP_B1("T0400_0")
    Return()

    # Function_1_330 end

    def Function_2_34A(): pass

    label("Function_2_34A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4B1")

    label("loc_36F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4B1")

    label("loc_388")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4B1")

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4B1")

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4B1")

    label("loc_3D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4B1")

    label("loc_3EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4B1")

    label("loc_405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4B1")

    label("loc_41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4B1")

    label("loc_437")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_450")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4B1")

    label("loc_450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4B1")

    label("loc_469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4B1")

    label("loc_482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4B1")

    label("loc_49B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4B1")

    label("loc_4C6")

    Return()

    # Function_2_34A end

    def Function_3_4C7(): pass

    label("Function_3_4C7")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 28710, 33610, 41830, 44000, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_613")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7026), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x834A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xA366), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xABE0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AD")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_59A():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59A)
    Jump("loc_5D0")

    label("loc_5AD")


    def lambda_5B3():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B3)
    Sleep(200)

    label("loc_5D0")

    Sleep(30)
    Jump("loc_610")

    label("loc_5D8")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_610")
    OP_44(0xFE, 0x2)

    def lambda_5F8():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F8)

    label("loc_610")

    Jump("loc_4F0")

    label("loc_613")

    Return()

    # Function_3_4C7 end

    def Function_4_614(): pass

    label("Function_4_614")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_4_614")

    label("loc_62F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_614 end

    def Function_5_63A(): pass

    label("Function_5_63A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653")
    OP_43(0xFE, 0x2, 0x0, 0x4)
    OP_22(0x191, 0x0, 0x64)

    label("loc_653")

    Return()

    # Function_5_63A end

    def Function_6_654(): pass

    label("Function_6_654")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_6_654 end

    def Function_7_65A(): pass

    label("Function_7_65A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_6D(24110, 20, 51410, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x19, 24530, 110, 32759, 0)
    SetChrPos(0x17, 25060, 140, 34870, 180)
    SetChrPos(0x18, 23990, 130, 34570, 180)
    SetChrPos(0x101, 24480, 100, 57310, 180)
    SetChrPos(0x16, 23730, 80, 58020, 180)

    def lambda_712():
        OP_8E(0xFE, 0x5FA0, 0xA, 0x8FFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_712)
    Sleep(50)

    def lambda_732():
        OP_8E(0xFE, 0x5C4E, 0x0, 0x92E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_732)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_757():
        OP_6D(24700, 40, 35720, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_757)

    def lambda_76F():
        OP_67(0, 6840, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_76F)

    def lambda_787():
        OP_6C(24000, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_787)
    WaitChrThread(0x1D, 0x0)
    Sleep(400)
    OP_62(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x18, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(120)
    OP_62(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_7E6():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_7E6)
    Sleep(50)
    OP_8C(0x18, 0, 500)

    ChrTalk(    #0
        0x18,
        "Estelle! Oh, Joshua came, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x17,
        (
            "#2PI bet you dragged him along by force,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        (
            "#290F#5PHey!\x02\x03",

            "We've come to help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x19,
        "Well, well! Music to my ears!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x19,
        (
            "Thanks much for coming over. You did an\x01",
            "awful lot for us while Hannah was pregnant\x01",
            "as it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#291F#5PAww. That was nothin'.\x02\x03",

            "Piece of cake for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x19,
        (
            "Haha. You're a force to be reckoned with,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x19,
        "Oh, but who is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x17,
        "#2PHe's Estelle's new little brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x17,
        (
            "#2PYou know about him! I told you before.\x01",
            "His name's Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x19,
        (
            "Oh! That does ring a bell...\x02\x03",

            "The one who had a big fight\x01",
            "with her at some point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x16,
        "#1677F...\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 24530, 170, 26700, 0)
    SetChrChipByIndex(0x1A, 7)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)

    def lambda_AAF():

        label("loc_AAF")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_AAF")

    QueueWorkItem2(0x19, 2, lambda_AAF)
    Sleep(50)

    def lambda_AC5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_AC5)
    Sleep(50)

    def lambda_AD8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_AD8)
    Sleep(1000)

    def lambda_AEB():
        OP_8E(0xFE, 0x5FD2, 0x6E, 0x7F58, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_AEB)
    Sleep(2000)

    def lambda_B0B():
        OP_8F(0xFE, 0x6400, 0x168, 0x7F58, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B0B)

    ChrTalk(    #12
        0x101,
        "#290F#5PMrs. Perzel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x18,
        "#5PHello, Mrs. Perzel!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1A, 0x1)
    Sleep(200)

    ChrTalk(    #14
        0x1A,
        "#6PWhy, hello to you, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1A,
        (
            "#6PI'm so sorry to make you two help out again.\x01",
            "You've been helping out so much as it is.\x02\x03",

            "If I could get right back to work, I would, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x19,
        (
            "#11PE-Easy, now. You need to rest for a while longer\x01",
            "before we can start thinking about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1A,
        (
            "#6PWhy? I was back to work in no time after Tio\x01",
            "was born.\x02\x03",

            "I just put her on my back and got right to work\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)

    ChrTalk(    #18
        0x18,
        "#3PR-Really?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 500)

    ChrTalk(    #19
        0x17,
        "#11PHow am I supposed to know? I was a baby!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1A,
        (
            "#6PSticking twins on my back IS probably pushing it,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x1A,
        "#6POh? Who's our black-haired friend?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x19,
        (
            "#11PThat's Joshua.\x02\x03",

            "Tio told us about him a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1A,
        (
            "#6PRight! Estelle's younger brother.\x01",
            "I remember now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x1A,
        "#6PWhy, isn't he adorable?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x16,
        "#1676F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1A,
        (
            "#6PHave you come to help us, too?\x01",
            "Sorry if it's not much fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x1A,
        "#6PWait. Is that a bandage I see?\x02",
    )

    CloseMessageWindow()

    def lambda_F00():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_F00)
    Sleep(100)

    def lambda_F13():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_F13)
    Sleep(120)
    OP_44(0x19, 0x2)
    OP_8C(0x19, 0, 500)

    ChrTalk(    #28
        0x19,
        (
            "Uh-oh. You're right... Didn't even notice\x01",
            "till you pointed it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x16,
        (
            "#1676F...\x02\x03",

            "#1671FMy injuries are more-or-less healed. They won't\x01",
            "have any effect on my ability to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x19,
        (
            "But 'more-or-less healed' means they're still healing!\x01",
            "We can't ask an injured boy do all our work for us.\x01",
            "You need to sit and rest...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x1A,
        "#6PHoney! I have the perfect idea!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x16, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_10D7():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_10D7)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(25360, 260, 40170, 0)
    OP_67(0, 6570, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(24000, 0)
    OP_6E(262, 0)
    SetChrPos(0x18, 25600, 270, 39300, 180)
    SetChrPos(0x17, 24710, 80, 39730, 180)
    SetChrPos(0x101, 23640, 0, 39430, 180)
    SetChrPos(0x16, 24610, 170, 41190, 180)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    SetChrPos(0x19, 25170, 160, 36800, 0)
    SetChrPos(0x1A, 24070, 110, 36720, 0)
    SetChrChipByIndex(0x1A, 6)
    SetChrSubChip(0x1A, 0)
    Sleep(500)
    SetMessageWindowPos(280, 250, -1, -1)
    SetChrName("Franz")

    AnonymousTalk(    #32
        (
            "\x07\x00Okay! Let me explain the harvesting process.\x02\x03",

            "Estelle, Elissa, Tio! You can handle the fields\x01",
            "in this area here.\x02\x03",

            "Try and start from the fields on the north side.\x01",
            "It'll probably be more efficient to split up, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 280, -1, -1)
    SetChrName("Hannah")

    AnonymousTalk(    #33
        (
            "\x07\x00Franz and I will take care of the vegetables in\x01",
            "the greenhouses.\x02\x03",

            "And as for Joshua...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    def lambda_131D():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_131D)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1D, 0x1)

    ChrTalk(    #34
        0x1A,
        "...I'll leave taking care of the babies to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1A,
        "The boy is Will, and the girl is Chere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x16,
        (
            "#1677F#5P...\x02\x03",

            "#1671FUnderstood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x19,
        "Well, let's get to work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x19,
        (
            "If you run into any problems or there's something\x01",
            "you don't understand, don't be afraid to ask.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    ChrTalk(    #39
        0x17,
        "#1POkay.\x02",
    )

    Sleep(50)

    ChrTalk(    #40
        0x18,
        "#4POkay!\x02",
    )

    Sleep(50)

    ChrTalk(    #41
        0x101,
        "#3POkay!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #42
        0x16,
        "#1677F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_1491():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_1491)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 8)
    Return()

    # Function_7_65A end

    def Function_8_14B0(): pass

    label("Function_8_14B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    SetChrPos(0x16, 50120, 500, 26010, 225)
    OP_6D(50620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)

    def lambda_1529():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_1529)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #43
        0x16,
        "#1675F...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1D, 0x0)
    Sleep(300)
    OP_20(0xBB8)
    Fade(2500)
    SetChrPos(0x16, 80120, 500, 26010, 225)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_6D(80620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)
    Sleep(3500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x18\x07\x0CThe past few weeks, there's been no sign at\x01",
            "all that anyone's coming after me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #45
        "\x18\x07\x0CWhy not?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #46
        "\x18\x07\x0CThey must've worked out where I am by now.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x18\x07\x0CSo am I supposed to take this to mean that\x01",
            "they're not interested in me anymore?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x18\x07\x0C...So they just stole my memories and cast me\x01",
            "aside?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #49
        "\x18\x07\x0CBut still...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #50
        "\x18\x07\x0CI still feel like...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #51
        "\x18\x07\x0C...like I've lost something really important to me...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #52
        "\x18\x07\x0CWhat is it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #53
        "\x18\x07\x0CJust what have I...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #54
        "\x07\x00#1S...Jo...a...!#2S\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x18\x07\x0CWhat have I...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Cheery Voice")

    AnonymousTalk(    #56
        "\x07\x00#3SJoshua!#2S\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Joshua")

    ChrTalk(    #57
        0x16,
        "#5P...What?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 49080, 140, 25500, 75)
    Fade(1500)
    SetChrPos(0x16, 50120, 500, 26010, 225)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    OP_6D(50620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    NpcTalk(    #58
        0x101,
        "Estelle",
        "Are you listening, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x16,
        (
            "#1678F#11P...\x02\x03",

            "Estelle?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xF)
    Sleep(500)

    ChrTalk(    #60
        0x101,
        "#290F#6PCheck THIS out!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05Estelle held out a large carrot.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #62
        0x101,
        (
            "#291F#6PIsn't it cool? I harvested this myself!\x02\x03",

            "And this eggplant, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x101,
        "#291F#6PLook! It's so shiny!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        (
            "#1671F#11P...\x02\x03",

            "...Uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#290F#6PHmm? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x16,
        (
            "#1671F#11P...\x02\x03",

            "#1677F*sigh*...\x02\x03",

            "You do know you scraped your knee, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#293F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x16,
        (
            "#1677F#11POne day, you'll learn to think before you leap...\x01",
            "or at least learn to take care of yourself after.\x02\x03",

            "#1689FCome on. Let me take a look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#290F#6PO-Okay..\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x20)
    OP_8C(0x16, 150, 300)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x46)
    Fade(1000)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 50780, 420, 25700, 45)
    SetChrPos(0x1C, 50780, 420, 25700, 45)
    OP_0D()
    Sleep(500)
    Fade(300)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_0D()
    TurnDirection(0x16, 0x101, 400)

    def lambda_1BEB():
        OP_8F(0xFE, 0xC256, 0x154, 0x6464, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1BEB)
    WaitChrThread(0x16, 0x1)
    Fade(300)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05Joshua took out some disinfectant.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #71
        0x101,
        (
            "#297F#6POwww!\x02\x03",

            "That stiiings...\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(600)

    def lambda_1CA3():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CA3)
    CloseMessageWindow()

    ChrTalk(    #72
        0x16,
        (
            "#1676F#11PJust endure it. It'll be over soon.\x02\x03",

            "#1675F(I swear, she attracts scratches and scrapes\x01",
            "like a magnet...)\x02\x03",

            "(It's a wonder she hasn't caught tetanus or\x01",
            "something.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#293F#6PHmm? Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x16,
        "#1677F#11PYou really do love causing people trouble...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#292F#6PI...\x02\x03",

            "#294FI never asked you to do anything for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x16,
        (
            "#1670F#11PThat just makes you cause people even\x01",
            "more trouble.\x02\x03",

            "You don't do anything about your injuries\x01",
            "--or even NOTICE them--and it just makes\x01",
            "more work for others.\x02\x03",

            "#1676FYou're a danger to yourself no matter how\x01",
            "you look at it.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77 op#A
        0x101,
        "#293F#6P#25AAnyway, Joshua... Why do you...?\x02\x02",
    )

    Sleep(2300)
    SetChrSubChip(0x16, 2)
    Sleep(200)

    ChrTalk(    #78
        0x16,
        "#1678F#11P(Oh, she's cut the back of her hand, too.)\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(500)

    ChrTalk(    #79
        0x101,
        (
            "#297F#6PEeek!\x02\x03",

            "#294FTell me where you're gonna put\x01",
            "that stuff before doing it!\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(600)

    def lambda_2001():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2001)
    CloseMessageWindow()

    ChrTalk(    #80
        0x16,
        "#1679F#11P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x05Joshua finished treating Estelle's wounds.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(300)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_0D()

    def lambda_2091():
        OP_8F(0xFE, 0xC3C8, 0x1F4, 0x659A, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2091)
    WaitChrThread(0x16, 0x1)
    Sleep(300)

    ChrTalk(    #82
        0x16,
        (
            "#1676F#11PThere. I'm done.\x02\x03",

            "Try and take a bit more care in future,\x01",
            "unless you want a lot more of 'that stuff'\x01",
            "being ap--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x1B,
        "Wah...\x02",
    )

    CloseMessageWindow()
    OP_43(0x1B, 0x3, 0x0, 0xA)

    ChrTalk(    #84
        0x1B,
        "Waaaaaah!\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_8C(0x16, 150, 500)
    OP_62(0x1B, 0x190, 800, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x1C, 0x0, 1100, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #85
        0x1B,
        "#2PWaaaaaah!\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #86
        0x101,
        (
            "#293F#6POh, no!\x02\x03",

            "#295FWhat can we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "#1679F#5PYou don't need to do anything.\x01",
            "Looking after them is my job.\x02\x03",

            "You go back to your own work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#296F#6PBut...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    OP_0D()
    Sleep(500)
    OP_22(0x8F, 0x0, 0x46)
    Fade(1000)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    SetChrPos(0x1B, 49900, 760, 25900, 225)
    SetChrPos(0x1C, 49900, 760, 25900, 225)
    SetChrFlags(0x1B, 0x8)
    OP_63(0x1B)
    OP_63(0x1C)
    OP_0D()
    SetChrFlags(0x16, 0x20)
    OP_8C(0x16, 225, 300)
    ClearChrFlags(0x16, 0x20)
    OP_62(0x1B, 0xFFFFFF38, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x1C, 0xC8, 1000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(300)

    ChrTalk(    #89
        0x1B,
        "#4PWaaah... Wah...\x02",
    )

    CloseMessageWindow()
    OP_44(0x1B, 0x3)

    def lambda_2329():
        OP_9E(0xFE, 0x0, 0xA, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_2329)
    Sleep(1500)

    def lambda_2348():
        OP_9E(0xFE, 0x0, 0xA, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_2348)
    Sleep(1500)
    OP_63(0x1B)
    OP_63(0x1C)
    Sleep(1000)
    OP_23(0x184)

    ChrTalk(    #90
        0x1B,
        "#4P...*gurgle*\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0x101,
        (
            "#293F#6PWow! They stopped!\x02\x03",

            "You sure you're not their mom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x16,
        (
            "#1677F#11PI'm not even going to dignify that with an\x01",
            "answer...\x02\x03",

            "#1679FJust go back to work. You're never going\x01",
            "to finish if you're not doing anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#290F#6POh, okay.\x02\x03",

            "#291FThanks, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 500)

    def lambda_24B5():
        OP_8E(0xFE, 0xA87A, 0xA, 0x4E48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24B5)
    WaitChrThread(0x101, 0x1)
    OP_62(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x16)

    ChrTalk(    #94
        0x16,
        "#1675F#11P#40W...Thanks, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x16)
    OP_20(0xBB8)
    SetChrFlags(0x16, 0x20)
    OP_8C(0x16, 150, 300)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x46)
    Fade(1000)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x1B, 0x8)
    SetChrPos(0x1B, 50780, 420, 25700, 45)
    OP_0D()
    Sleep(500)
    Fade(300)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_0D()
    OP_8C(0x16, 225, 400)
    Fade(300)
    SetChrFlags(0x16, 0x2)
    SetChrChipByIndex(0x16, 10)
    SetChrSubChip(0x16, 2)
    OP_0D()
    Fade(300)
    SetChrSubChip(0x16, 10)
    OP_0D()
    Sleep(2000)
    Fade(1000)
    OP_6B(2780, 0)
    SetChrSubChip(0x16, 7)
    OP_0D()
    Sleep(300)
    OP_43(0x16, 0x3, 0x0, 0x9)
    OP_1D(0x4A)
    Sleep(2500)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrPos(0x17, 49740, -170, 50680, 100)
    SetChrPos(0x101, 49970, -290, 40830, 110)
    SetChrPos(0x18, 42240, -200, 41770, 280)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    Fade(4000)
    OP_44(0x1D, 0xFF)
    OP_6D(24450, 0, 24100, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(318000, 0)
    OP_6E(504, 0)

    def lambda_2672():
        OP_6D(44250, 0, 44300, 20000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_2672)

    def lambda_268A():
        OP_6C(340000, 20000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_268A)
    OP_77(0xFF, 0x97, 0x8A, 0x0, 0x4E20)
    WaitChrThread(0x1D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(43260, 70, 20300, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 41720, 0, 18800, 45)
    SetChrPos(0x18, 41720, 0, 17800, 45)
    SetChrPos(0x17, 40720, 0, 18800, 45)
    OP_44(0x101, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x17, 0x0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x17, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #95
        0x18,
        (
            "Whoooa...\x02\x03",

            "He's so cool...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x17,
        (
            "#6PI didn't know he could do that...\x02\x03",

            "A handsome boy playing the harmonica beautifully\x01",
            "with the setting sun in the background... There's a\x01",
            "picture if I ever saw one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x17,
        "#6PDid you know he could play, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#5P#292FUuugh...\x02\x03",

            "He's supposed to be my brother,\x01",
            "and he never told me at all!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #99
        0x101,
        "#5P#294F#3SHe's gonna get a HUUUGE lecture later!#2S\x02",
    )

    Sleep(150)
    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_62(0x18, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x18,
        "Oh, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x17,
        "#6PWhat are you getting so mad for?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x16, 50120, 500, 26010, 225)
    OP_6D(50620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_29B3():
        OP_6B(2780, 8000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_29B3)
    Sleep(2000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #102
        "\x07\x02#40WWell, hello there.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #103
        (
            "\x07\x02#40WThere's no need to be so afraid.\x01",
            "I am but a humble magician.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #104
        "\x07\x02#40WI will heal your broken heart for you.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #105
        (
            "\x07\x02#40WProvided, of course...#500W\x01",
            "#40WI am compensated.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_1D(0xB2)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "\x18\x07\x0C#40WI finally understand.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #107
        "\x18\x07\x0C#40WI finally know what I lost.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #108
        (
            "\x18\x07\x0C#40WEverything that was important to me.\x01",
            "My happy memories, all that made me myself...\x01",
            "That was the 'compensation' I gave.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #109
        (
            "\x18\x07\x0C#40WAll that remains now is a doll...\x01",
            "A twisted, broken fragment of who I was.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #110
        (
            "\x18\x07\x0C#40WSomeone who exists only to destroy what\x01",
            "others love...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #111
        "\x18\x07\x0C#40WI need to leave.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #112
        (
            "\x18\x07\x0C#40WIf I stay any longer, I'll end up destroying the\x01",
            "happiness of everyone around me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #113
        (
            "\x18\x07\x0C#40WI need to keep the things that I care about as\x01",
            "far away from me as possible. Not close by.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #114
        "\x18\x07\x0C#40WI need them to be far, far out of my reach.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #115
        (
            "\x18\x07\x0C#40WAnd I need to do it now...before the darkness\x01",
            "within me contaminates this place forever.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #116
        "\x18\x07\x0C#40WI need to leave.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #117
        (
            "\x18\x07\x0C#40WBefore my very existence causes her irreparable\x01",
            "harm.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_20(0x1388)
    OP_21()
    Sleep(2000)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_14B0 end

    def Function_9_2ED2(): pass

    label("Function_9_2ED2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F24")
    SetChrSubChip(0x16, 7)
    Sleep(250)
    SetChrSubChip(0x16, 15)
    Sleep(250)
    SetChrSubChip(0x16, 23)
    Sleep(250)
    SetChrSubChip(0x16, 31)
    Sleep(250)
    SetChrSubChip(0x16, 39)
    Sleep(250)
    SetChrSubChip(0x16, 47)
    Sleep(250)
    SetChrSubChip(0x16, 55)
    Sleep(250)
    Jump("Function_9_2ED2")

    label("loc_2F24")

    Return()

    # Function_9_2ED2 end

    def Function_10_2F25(): pass

    label("Function_10_2F25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F6D")
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1100)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1200)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1300)
    Jump("Function_10_2F25")

    label("loc_2F6D")

    Return()

    # Function_10_2F25 end

    def Function_11_2F6E(): pass

    label("Function_11_2F6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(26470, 130, 44280, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(237000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 27520, -70, 41470, 90)
    SetChrPos(0x155, 25510, 320, 53280, 180)

    def lambda_2FE4():
        OP_6B(2840, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_2FE4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #118
        0x155,
        "#291F#1PTiooo!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x155, 0x3, 0x0, 0xC)
    OP_62(0x17, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_3036():

        label("loc_3036")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_3036")

    QueueWorkItem2(0x17, 2, lambda_3036)
    Sleep(500)

    def lambda_304C():
        OP_6D(26910, 0, 41800, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_304C)

    def lambda_3064():
        OP_67(0, 6230, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3064)

    def lambda_307C():
        OP_6C(216000, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_307C)
    WaitChrThread(0x155, 0x3)
    OP_44(0x17, 0x2)
    Sleep(300)

    ChrTalk(    #119
        0x17,
        "#5PHey, Estelle. What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x17,
        (
            "#5P...Wait. Forget it. I know just from how you're\x01",
            "dressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x155,
        (
            "#290F#12PHeehee. Today's bug catching is special,\x01",
            "though!\x02\x03",

            "But FIRST, I need some fresh milk and fresh\x01",
            "eggs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x17,
        "#5PWhat in heaven's name do you need those for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x17,
        (
            "#5PDon't tell me you've suddenly developed an\x01",
            "interest in cooking or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x155,
        "#291F#12PWeeell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #125
        "\x07\x05Estelle explained what she was trying to do.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #126
        0x17,
        "#5P#100WB-Bug of #20WLegends?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x155,
        (
            "#291F#12PYup! I'm trying to give Joshua the surprise\x01",
            "of his life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x17,
        "#5PI'm still not sure I'm following all of this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x17,
        "#5PLet me try again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x17,
        (
            "#5PI guess you're trying to make some kind of \x01",
            "aromatic capable of attracting that bug?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x155,
        "#290F#12PProbably!\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0x17,
        (
            "#5PJust, whatever you do, promise not to get\x01",
            "any of it on me, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x155,
        "#291F#12PI won't! I won't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x17,
        "#5PI don't know if I believe you...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)

    def lambda_344E():
        OP_8E(0xFE, 0x6C8E, 0xFFFFFF4C, 0x9308, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_344E)
    WaitChrThread(0x17, 0x1)

    def lambda_346E():
        OP_8E(0xFE, 0x58F2, 0x8C, 0x7846, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_346E)
    WaitChrThread(0x17, 0x1)
    Sleep(2000)

    def lambda_3493():
        OP_8E(0xFE, 0x6C8E, 0xFFFFFF4C, 0x9308, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3493)
    WaitChrThread(0x17, 0x1)

    def lambda_34B3():
        OP_8E(0xFE, 0x6B80, 0xFFFFFFBA, 0xA1FE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_34B3)
    WaitChrThread(0x17, 0x1)
    Sleep(300)

    ChrTalk(    #135
        0x17,
        "#5PWell, here's what you wanted.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x07\x05Estelle received both \x07\x02Fresh Milk\x07\x05 and \x07\x02Fresh Eggs\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #137
        0x17,
        "#5POh, and one more thing before you go, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x155,
        "#290F#12PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x17,
        (
            "#5PIf you really see him as your little brother,\x01",
            "you should start gradually opening up to him\x01",
            "about the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x17,
        "#5PTry getting him to do the same with you, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x17,
        "#5PMaybe try talking to him about your mom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x155,
        (
            "#296F#12P...Yeah. I can do that.\x02\x03",

            "#290FIt doesn't feel like the kinda thing you need\x01",
            "to sit and have a big serious discussion about,\x01",
            "though.\x02\x03",

            "We're always gonna be together, so I think\x01",
            "he'll get it eventually.\x02\x03",

            "Because we're family now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x17,
        "#5P...Well, I tried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x17,
        (
            "#5PThat's a very you way to look at it...\x01",
            "but I mean that in a good way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x155,
        (
            "#290F#12PHeehee...\x02\x03",

            "#291FThanks, Tio!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x155, 0, 500)
    OP_A2(0x2F62)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 1)), scpexpr(EXPR_END)), "loc_3A8B")

    ChrTalk(    #146
        0x155,
        (
            "#292F#5POkay! I've got everything I need now.\x02\x03",

            "All I gotta do is head to Mistwald and catch\x01",
            "me the Bug of Legends!\x02\x03",

            "#294FYou just wait, Joshua! I'm gonna blow your\x01",
            "socks off!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38DC():
        OP_6D(26810, -70, 45830, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_38DC)

    def lambda_38F4():
        OP_6C(226000, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_38F4)

    def lambda_3904():

        label("loc_3904")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_3904")

    QueueWorkItem2(0x17, 2, lambda_3904)
    SetChrFlags(0x155, 0x40)
    SetChrFlags(0x155, 0x4)

    def lambda_391F():
        OP_8E(0xFE, 0x6B1C, 0xFFFFFFC4, 0xB2D4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_391F)
    WaitChrThread(0x155, 0x1)

    def lambda_393F():
        OP_96(0xFE, 0x6E50, 0xFFFFFFA6, 0xBEC8, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_393F)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x155, 0x40)
    ClearChrFlags(0x155, 0x4)

    def lambda_3971():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xBEC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3971)
    WaitChrThread(0x155, 0x1)

    def lambda_3991():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xF80C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3991)
    WaitChrThread(0x155, 0x1)
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #147
        0x17,
        "#5PW-Wait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x17,
        (
            "#5PShe's not gonna go there all\x01",
            "by herself, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x17,
        (
            "#5PAnd just what is this #100WBug of Legends#30W\x01",
            "thingy, anyway?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A67():
        OP_6B(2740, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_3A67)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3CAD")

    label("loc_3A8B")


    ChrTalk(    #150
        0x155,
        "#291F#5PNext I need to go see Elissa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x17,
        "#5PWhat for? Do you still need more ingredients?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x155, 0x17, 500)
    Sleep(300)

    ChrTalk(    #152
        0x155,
        "#290F#12PYup! I need some dragon beans.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x17,
        "#5P...Oh. Well, good luck.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x155, 0, 500)
    Sleep(300)

    def lambda_3B57():
        OP_6D(26810, -70, 45830, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_3B57)

    def lambda_3B6F():
        OP_6C(226000, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3B6F)

    def lambda_3B7F():

        label("loc_3B7F")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_3B7F")

    QueueWorkItem2(0x17, 2, lambda_3B7F)
    SetChrFlags(0x155, 0x40)
    SetChrFlags(0x155, 0x4)

    def lambda_3B9A():
        OP_8E(0xFE, 0x6B1C, 0xFFFFFFC4, 0xB2D4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3B9A)
    Sleep(100)

    ChrTalk(    #154 op#A
        0x155,
        "#291F#5P#10AZooooooooom!\x02",
    )

    WaitChrThread(0x155, 0x1)

    def lambda_3BDC():
        OP_96(0xFE, 0x6E50, 0xFFFFFFA6, 0xBEC8, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3BDC)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x155, 0x40)
    ClearChrFlags(0x155, 0x4)

    def lambda_3C0E():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xBEC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3C0E)
    WaitChrThread(0x155, 0x1)

    def lambda_3C2E():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xF80C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3C2E)
    WaitChrThread(0x155, 0x1)
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #155
        0x17,
        "She's sure fired up today...\x02",
    )

    CloseMessageWindow()

    def lambda_3C8C():
        OP_6B(2740, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_3C8C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3CAD")

    Return()

    # Function_11_2F6E end

    def Function_12_3CAE(): pass

    label("Function_12_3CAE")

    SetChrPos(0x155, 24380, 100, 60730, 180)

    def lambda_3CC5():
        OP_8E(0xFE, 0x5F3C, 0x64, 0xB234, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3CC5)
    WaitChrThread(0x155, 0x1)

    def lambda_3CE5():
        OP_8E(0xFE, 0x6B1C, 0xFFFFFF92, 0xA7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3CE5)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x17, 500)
    Return()

    # Function_12_3CAE end

    SaveToFile()

Try(main)
