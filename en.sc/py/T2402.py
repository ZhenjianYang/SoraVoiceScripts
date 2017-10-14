from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2402   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2402.x',
        MapIndex            = 1,
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
        'Matron Theresa',                       # 9
        'Clem',                                 # 10
        'Polly',                                # 11
        'Mary',                                 # 12
        'Daniel',                               # 13
        'Chicken',                              # 14
        'Chicken',                              # 15
        'Chicken',                              # 16
        'Targeting Camera',                     # 17
        'Gull Seaside Way',                     # 18
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02500 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02640 ._CH',             # 04
        'ED6_DT07/CH01720 ._CH',             # 05
        'ED6_DT26/CH20237 ._CH',             # 06
        'ED6_DT26/CH20272 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02500P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02640P._CP',             # 04
        'ED6_DT07/CH01720P._CP',             # 05
        'ED6_DT26/CH20237P._CP',             # 06
        'ED6_DT26/CH20272P._CP',             # 07
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
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


    DeclEvent(
        X                   = -1820,
        Y                   = 0,
        Z                   = 2670,
        Range               = 2120,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x157C,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = -186,
        TriggerZ            = 0,
        TriggerY            = 32147,
        TriggerRange        = 400,
        ActorX              = -186,
        ActorZ              = 1250,
        ActorY              = 32147,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26E",          # 00, 0
        "Function_1_3C2",          # 01, 1
        "Function_2_403",          # 02, 2
        "Function_3_580",          # 03, 3
        "Function_4_664",          # 04, 4
        "Function_5_688",          # 05, 5
        "Function_6_7DB",          # 06, 6
        "Function_7_82A",          # 07, 7
        "Function_8_DED",          # 08, 8
        "Function_9_138F",         # 09, 9
        "Function_10_14F8",        # 0A, 10
        "Function_11_1DE3",        # 0B, 11
        "Function_12_1E69",        # 0C, 12
        "Function_13_1E8F",        # 0D, 13
        "Function_14_2F33",        # 0E, 14
        "Function_15_32AF",        # 0F, 15
    )


    def Function_0_26E(): pass

    label("Function_0_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2CE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -3270, 0, 9200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298")
    SetChrFlags(0x9, 0x10)

    label("loc_298")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2970, 0, 27510, 45)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 13060, 0, 20500, 90)
    Jump("loc_3AE")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2D8")
    Jump("loc_3AE")

    label("loc_2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_348")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 8320, -170, 15270, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -6449, -198, 20931, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 7012, 0, 23975, 180)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 4690, 0, 26500, 220)
    OP_43(0xB, 0x0, 0x0, 0x3)
    Jump("loc_3AE")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_3AE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -9630, 40, 16570, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 9460, 10, 19760, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2970, 0, 27510, 47)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5190, 0, 29630, 225)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3C1")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3C1")

    Return()

    # Function_0_26E end

    def Function_1_3C2(): pass

    label("Function_1_3C2")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x230067)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E6")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FE")
    OP_72(0x0, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_402")

    label("loc_3FE")

    OP_64(0x0, 0x1)

    label("loc_402")

    Return()

    # Function_1_3C2 end

    def Function_2_403(): pass

    label("Function_2_403")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_56A")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_56A")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_56A")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_56A")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_56A")

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_56A")

    label("loc_4A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_56A")

    label("loc_4BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_56A")

    label("loc_4D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_56A")

    label("loc_4F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_509")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_56A")

    label("loc_509")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_522")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_56A")

    label("loc_522")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_56A")

    label("loc_53B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_56A")

    label("loc_554")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_56A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_56A")

    label("loc_57F")

    Return()

    # Function_2_403 end

    def Function_3_580(): pass

    label("Function_3_580")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_663")
    OP_8E(0xFE, 0x1365, 0x25, 0x5C94, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x416, 0x65E7, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0x416, 0x0, 0x65E7, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x2D3, 0x5565, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0x2D3, 0x1A, 0x5565, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x10BE, 0x6B64, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0x10BE, 0x0, 0x6B64, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0xFFFFF991, 0x4BAE, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFF991, 0xBD, 0x4BAE, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x1365, 0x5C94, 0x190)
    Sleep(200)
    Jump("Function_3_580")

    label("loc_663")

    Return()

    # Function_3_580 end

    def Function_4_664(): pass

    label("Function_4_664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_687")
    OP_8D(0xFE, 1350, 26320, 3220, 28450, 2000)
    Jump("Function_4_664")

    label("loc_687")

    Return()

    # Function_4_664 end

    def Function_5_688(): pass

    label("Function_5_688")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_761():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_761)
    Jump("loc_797")

    label("loc_774")


    def lambda_77A():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77A)
    Sleep(200)

    label("loc_797")

    Sleep(30)
    Jump("loc_7D7")

    label("loc_79F")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D7")
    OP_44(0xFE, 0x2)

    def lambda_7BF():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BF)

    label("loc_7D7")

    Jump("loc_6B6")

    label("loc_7DA")

    Return()

    # Function_5_688 end

    def Function_6_7DB(): pass

    label("Function_6_7DB")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_7DB end

    def Function_7_82A(): pass

    label("Function_7_82A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0D")
    OP_8C(0xFE, 90, 0)
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #1
        0xFE,
        (
            "#1714FAh...\x02\x03",

            "#1712FUm... Is... Is it you, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1054FYeah... It's been a while, Mary.\x02\x03",

            "Did I surprise you? I know I'm\x01",
            "dressed a bit differently.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #3
        0xFE,
        (
            "#1716FN-No, not at all!\x02\x03",

            "#1710FYour clothes are, um...really cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#1049FHaha... Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "#1718FIf you're looking for Matron Theresa,\x01",
            "she's inside. You should say hi!\x02\x03",

            "#1903FAhaha...\x01",
            "I'm sure she'd be happy if you did.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20EB)
    Jump("loc_C87")

    label("loc_A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A9F")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #6
        0xFE,
        (
            "#1718FMatron Theresa is inside, so you\x01",
            "should definitely say hi.\x02\x03",

            "#1903FAhaha...\x01",
            "I'm sure she'd be happy if you did.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2F")

    label("loc_A9F")


    ChrTalk(    #7
        0xFE,
        (
            "#1716FEver since that weird thingy in the sky\x01",
            "appeared, we've stopped getting letters...\x02\x03",

            "#1713FI wonder if Kloe is okay in the capital...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2F")

    Jump("loc_C87")

    label("loc_B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_BBD")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #8
        0xFE,
        (
            "#1718FMatron Theresa is inside, so you\x01",
            "should definitely say hi.\x02\x03",

            "#1903FAhaha...\x01",
            "I'm sure she'd be happy if you did.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C87")

    label("loc_BBD")


    ChrTalk(    #9
        0xFE,
        (
            "#1718FEven if we can't use orbal stuff,\x01",
            "it's okay.\x02\x03",

            "We've got eggs, and vegetables, and we've\x01",
            "got fire as long as we've got kindling...\x02\x03",

            "Even if the vacuum doesn't work,\x01",
            "we'll be fine with brooms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C87")

    Jump("loc_DE9")

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CFD")

    ChrTalk(    #10
        0xFE,
        (
            "#1718FOur chickens' eggs are delicious.\x02\x03",

            "#1900FMaybe it's because we let them\x01",
            "wander around?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D51")

    label("loc_CFD")

    OP_A2(0x3)

    ChrTalk(    #11
        0xFE,
        (
            "#1710FI've gotta collect eggs.\x02\x03",

            "I'd better hurry or everyone'll crush them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D51")

    Jump("loc_DE9")

    label("loc_D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_DE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #12
        0xFE,
        "#1716FPolly's so silly sometimes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE9")

    label("loc_D8C")

    OP_A2(0x3)

    ChrTalk(    #13
        0xFE,
        (
            "#1716FWhy does Polly want to see\x01",
            "that white shadow again?\x02\x03",

            "She's so silly sometimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE9")

    TalkEnd(0xFE)
    Return()

    # Function_7_82A end

    def Function_8_DED(): pass

    label("Function_8_DED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED9")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #14
        0x102,
        "#1040FHi, Polly. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "#1733FWhooooa, it's Joshuaaa.\x02\x03",

            "You seem kinda different.\x02\x03",

            "#1732FDifferent, but you still look cool,\x01",
            "so I gueeeeeess it's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1054FHaha... Thank you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x20EC)
    Jump("loc_10C5")

    label("loc_ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F5C")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #17
        0xFE,
        (
            "#1730FYou seem kinda different.\x02\x03",

            "#1732FDifferent, but you still look cool,\x01",
            "so I gueeeeeess it's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEB")

    label("loc_F5C")


    ChrTalk(    #18
        0xFE,
        (
            "#1730FMr. Soldier over there seems kinda nervous.\x02\x03",

            "I said something to him from behind\x01",
            "and he jumped up REAL high.\x02\x03",

            "It was so fuuuuuunny.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEB")

    Jump("loc_10C5")

    label("loc_FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_106A")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #19
        0xFE,
        (
            "#1730FYou seem kinda different.\x02\x03",

            "#1732FDifferent, but you still look cool,\x01",
            "so I gueeeeeess it's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C5")

    label("loc_106A")


    ChrTalk(    #20
        0xFE,
        (
            "#1733FAirships are ships that fly in the air,\x01",
            "right?\x02\x03",

            "Why are they on the beach then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C5")

    Jump("loc_138B")

    label("loc_10C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_117D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1107")

    ChrTalk(    #21
        0xFE,
        "#1730FClem has been helpin' lots lately!\x02",
    )

    CloseMessageWindow()
    Jump("loc_117A")

    label("loc_1107")

    OP_A2(0x2)

    ChrTalk(    #22
        0xFE,
        (
            "#1730FClem has been helpin' lots lately!\x02\x03",

            "#1732FWell, he's also workin' hard on\x01",
            "his pranks, too. Yup, yup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117A")

    Jump("loc_138B")

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_138B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11D4")

    ChrTalk(    #23
        0xFE,
        (
            "#1732FI wonder if the white shadow\x01",
            "will come again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1316")

    label("loc_11D4")

    TurnDirection(0xFE, 0x109, 0)
    OP_A2(0x2)

    ChrTalk(    #24
        0xFE,
        (
            "#1731FOh, it's Mr. Kevin.\x02\x03",

            "#1732FMr. Kevin! Mr. Kevin!\x01",
            "Will I see the white old guy again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1064FUh...!\x02\x03",

            "#1068FI, uh...dunno.\x02\x03",

            "Sorry, but even ol' Mr. Kevin doesn't\x01",
            "know that guy's schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "#1733FAwww, I wanna meet him again.\x02\x03",

            "#1731FHe could spin round and round in the sky...\x01",
            "It was really fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1316")

    Jump("loc_138B")

    label("loc_1319")


    ChrTalk(    #27
        0xFE,
        (
            "#1730FI wanna meet that white old guy again.\x02\x03",

            "He could spin round and round in the sky...\x01",
            "It was really fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138B")

    TalkEnd(0xFE)
    Return()

    # Function_8_DED end

    def Function_9_138F(): pass

    label("Function_9_138F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1444")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13CE")

    ChrTalk(    #28
        0xFE,
        "#1720FI hope Kloe comes to play soon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1441")

    label("loc_13CE")

    OP_A2(0x1)

    ChrTalk(    #29
        0xFE,
        (
            "#1720FI hope Kloe comes to play soon!\x02\x03",

            "#1721FI'm gonna get her to bake some\x01",
            "bread and eat until I EXPLODE.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1441")

    Jump("loc_14F4")

    label("loc_1444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_14F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1487")

    ChrTalk(    #30
        0xFE,
        "#1722FI wonder what that white shadow was...\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F4")

    label("loc_1487")

    OP_A2(0x1)

    ChrTalk(    #31
        0xFE,
        (
            "#1722FI wonder what that white shadow was...\x02\x03",

            "If it was a ghost, it should have been\x01",
            "scarier, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F4")

    TalkEnd(0xFE)
    Return()

    # Function_9_138F end

    def Function_10_14F8(): pass

    label("Function_10_14F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C5")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2350, 0, 9510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -2300, 0, 8780, 270)
    SetChrPos(0x101, -2260, 0, 9660, 270)
    SetChrPos(0xF8, -1470, 0, 8720, 270)
    SetChrPos(0xF9, -1410, 0, 9580, 270)
    OP_8C(0xFE, 270, 0)
    OP_4A(0xFE, 255)
    OP_0D()
    OP_62(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x9,
        (
            "#773F#6PMaaan, chopping wood's pretty hard.\x02\x03",

            "But, if I don't do it Matron Theresa's\x01",
            "gonna have it even harder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1040F#4PHey, Clem. Seems like you're doing well.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 90, 600)
    Sleep(500)

    ChrTalk(    #34
        0x9,
        (
            "#774F#6P#3SAhhhhh!#2S\x02\x03",

            "#3SJ-Joshua!!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#1049F#4PIt's been a while, Clem.\x02\x03",

            "#1040FI heard from Estelle that you've been\x01",
            "working hard to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#770F#6PO-Of course!\x02\x03",

            "#770FI'm not slacking off on weedin' or takin'\x01",
            "care of the chickens or anything.\x02\x03",

            "I gotta work hard for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#1053F#4PYeah, good thinking.\x02\x03",

            "#1054FI know there's a lot that's tough right now,\x01",
            "but help out everyone you can, okay?\x02\x03",

            "We're doing our best to help out too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#771F#6PHaha, got it!\x02\x03",

            "#770FI'll do my best to help as much as you!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x0)
    OP_A2(0x20B2)
    EventEnd(0x0)
    OP_4B(0xFE, 255)
    Jump("loc_1AD9")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_19C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1942")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #39
        0x9,
        (
            "#770FI'll do my best to help as much\x01",
            "as you, Joshua!\x02\x03",

            "I'll keep everyone at the orphanage\x01",
            "safe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BD")

    label("loc_1942")


    ChrTalk(    #40
        0x9,
        (
            "#770FMatron Theresa said that Kloe's doing\x01",
            "a lot back home at the capital.\x02\x03",

            "#771FAll right, I gotta match up to that!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BD")

    Jump("loc_1AD9")

    label("loc_19C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A36")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #41
        0x9,
        (
            "#770FI'll do my best to help as much\x01",
            "as you, Joshua!\x02\x03",

            "I'll keep everyone at the orphanage\x01",
            "safe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD9")

    label("loc_1A36")


    ChrTalk(    #42
        0x9,
        (
            "#772FDidja know there's an airship\x01",
            "stuck on the beach nearby?\x02\x03",

            "I reeeeally wanna go see it,\x01",
            "but I still got chores to do...\x02\x03",

            "#773FRrrrrrrr, I gotta hold out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD9")

    Jump("loc_1DDF")

    label("loc_1ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 7)), scpexpr(EXPR_END)), "loc_1C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B3C")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #43
        0x9,
        (
            "#770FGive my best to Joshua.\x02\x03",

            "Aaanyway, gotta get back to weeding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C75")

    label("loc_1B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1BD8")

    ChrTalk(    #44
        0x9,
        (
            "#770FWe've just started growin' some\x01",
            "new sprouts in this field.\x02\x03",

            "They're still small and weak,\x01",
            "so we gotta be real careful\x01",
            "with the weeding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C75")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_1C75")

    ChrTalk(    #45
        0x9,
        (
            "#770FWeeds gotta be pulled out from the roots\x01",
            "down or they'll just regrow, ya know.\x02\x03",

            "Just you watch, weeds. Learn the power\x01",
            "of Clem and TREMBLE!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C75")

    Jump("loc_1DDF")

    label("loc_1C78")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122F)
    OP_A2(0x0)

    ChrTalk(    #46
        0x9,
        (
            "#773FAww, it's too bad Joshua's not with you.\x02\x03",

            "I wanted to show him how hard\x01",
            "I'm workin', too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#772FHey, Estelle.\x02\x03",

            "If you see Joshua, you be sure\x01",
            "to tell him, okay?\x02\x03",

            "That I'm here workin' hard with everyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1025FClem...\x02\x03",

            "#1006F... Yeah, got it.\x02\x03",

            "I'll definitely tell Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "#770FYeah, it's a promise!\x02",
    )

    CloseMessageWindow()

    label("loc_1DDF")

    TalkEnd(0xFE)
    Return()

    # Function_10_14F8 end

    def Function_11_1DE3(): pass

    label("Function_11_1DE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E68")
    OP_43(0xFE, 0x2, 0x0, 0xC)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_1E68")
    TalkBegin(0xFE)
    OP_A2(0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x00Received #907i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_1E68")

    Return()

    # Function_11_1DE3 end

    def Function_12_1E69(): pass

    label("Function_12_1E69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E84")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_12_1E69")

    label("loc_1E84")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_1E69 end

    def Function_13_1E8F(): pass

    label("Function_13_1E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA8")
    Call(0, 15)

    label("loc_1EA8")

    EventBegin(0x0)
    Fade(1000)
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    ClearMapFlags(0x1)
    SetChrFlags(0x109, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, -390, 0, 3340, 0)
    SetChrPos(0xF7, 450, 0, 2620, 0)
    OP_6D(170, 0, 3940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        "#1004F#6PHoly...\x02",
    )

    CloseMessageWindow()
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x1, 0x7D0)
    OP_DE("Mercia Orphanage")

    def lambda_1F9B():
        OP_6D(320, 0, 32530, 6000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1F9B)

    def lambda_1FB3():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FB3)

    def lambda_1FCB():
        OP_6B(4210, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1FCB)

    def lambda_1FDB():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1FDB)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    SetChrPos(0x101, -620, 0, 17860, 0)
    SetChrPos(0xF7, 680, 70, 17860, 0)

    def lambda_2021():
        OP_8E(0xFE, 0xFFFFFF56, 0xA, 0x69A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2021)
    Sleep(300)

    def lambda_2041():
        OP_8E(0xFE, 0x438, 0x0, 0x6860, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2041)
    Sleep(2000)
    Fade(500)
    OP_6D(510, 0, 28590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 6540, 0, 33360, 230)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2136")

    ChrTalk(    #53
        0x106,
        (
            "#052FOkay, this is a surprise.\x02\x03",

            "They managed to turn that black stain\x01",
            "on the ground into THIS that quick?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AF")

    label("loc_2136")


    ChrTalk(    #54
        0x103,
        (
            "#020FWasn't there a nasty fire here?\x02\x03",

            "Looking at this, you'd barely know\x01",
            "there'd been so much as a campfire\x01",
            "lately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AF")


    ChrTalk(    #55
        0x101,
        (
            "#1008F#5PI think they built the building\x01",
            "the same way, just...uh, newer...\x02\x03",

            "Thank the Goddess...\x01",
            "This is so wonderful.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x8,
        "Woman's Voice",
        "#6PEstelle?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_226C():
        OP_6D(3480, 0, 30020, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_226C)

    def lambda_2284():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2284)
    TurnDirection(0x101, 0x8, 400)
    Sleep(300)
    TurnDirection(0xF7, 0x8, 400)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #57
        0x101,
        "#1018F#5PMatron Theresa!\x02",
    )

    CloseMessageWindow()

    def lambda_22D7():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_22D7)

    def lambda_22E7():
        OP_8E(0xFE, 0xC6C, 0x0, 0x7396, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22E7)
    Sleep(200)

    def lambda_2307():
        OP_8E(0xFE, 0xF46, 0x0, 0x7666, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2307)
    Sleep(500)

    def lambda_2327():
        OP_8E(0xFE, 0xEE2, 0x0, 0x6E6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2327)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    TurnDirection(0xF7, 0x8, 400)
    WaitChrThread(0x8, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_24ED")

    ChrTalk(    #58
        0x8,
        (
            "#751F#4PYes, I thought it was you!\x02\x03",

            "Welcome back.\x01",
            "I'm glad to see you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)
    Sleep(500)

    ChrTalk(    #59
        0x8,
        "#753F#6PAnd you are...Agate, yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x106,
        "#051F#2PThat's right. Been a while, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#750F#6PWe last met during that mess with\x01",
            "Clem, yes.\x02\x03",

            "It really has been a while. Thank you\x01",
            "so much for your help back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x106,
        (
            "#051F#2PHey, don't sweat it. Really.\x02\x03",

            "I'm just sorry I haven't stopped\x01",
            "by since then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B5")

    label("loc_24ED")


    ChrTalk(    #63
        0x8,
        (
            "#751F#4PYes, I thought it was you!\x02\x03",

            "Welcome back.\x01",
            "I'm glad to see you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)
    Sleep(500)

    ChrTalk(    #64
        0x8,
        (
            "#753F#6PAnd...I'm sorry, I don't believe\x01",
            "we've met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#020F#2PWe haven't, my apologies.\x01",
            "I'm Scherazard Harvey, Estelle's\x01",
            "bracer mentor.\x02\x03",

            "#021FI have, however, heard a great deal\x01",
            "about you from a certain someone,\x01",
            "Matron Theresa.\x02\x03",

            "You're a loving mother figure to every\x01",
            "child here...and, apparently, your tea\x01",
            "is first-rate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "#751F#6POh, my... I'm flattered!\x02",
    )

    CloseMessageWindow()

    label("loc_26B5")


    ChrTalk(    #67
        0x101,
        (
            "#1017F#6PU-Umm, congratulations on getting\x01",
            "the orphanage rebuilt!\x02\x03",

            "I'm amazed. It looks pretty much\x01",
            "exactly how it used to be, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #68
        0x8,
        (
            "#750F#4PHeehee. I know it sounds silly to ask\x01",
            "them to build it that way, but everyone\x01",
            "was kind enough to humor me.\x02\x03",

            "I can't imagine this orphanage looking\x01",
            "any other way. It just wouldn't be the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1016F#6PHaha. Yeah, I think you're right.\x02\x03",

            "#1017FSo, uh, are the kids inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#750F#4PAh, no. They're actually out in Manoria\x01",
            "for class.\x02\x03",

            "A traveling priest comes by once a week\x01",
            "and holds Sunday School for us, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#6POh, okay.\x01",
            "That's a bit of a problem, though.\x02\x03",

            "Y'see, we actually want to ask the kids\x01",
            "about something, on top of just saying hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#753F#4POh?\x02\x03",

            "Would this have to do with\x01",
            "the 'white man' Polly saw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1011F#6PAh, probably, yes!\x02\x03",

            "I see, so it was Polly who\x01",
            "saw the person...thing.\x02\x03",

            "I always did peg her as a sharp one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#751F#4PWell, come inside. You can wait\x01",
            "here until they return.\x02\x03",

            "I do have some tea on the kettle,\x01",
            "and a few snacks, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1011F#6PTh-Thanks...\x02\x03",

            "#1003F...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2B4D")
    OP_62(0x106, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 315, 400)

    ChrTalk(    #76
        0x106,
        "#052F#2PWhat's up? Tea not your thing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B94")

    label("loc_2B4D")

    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 315, 400)

    ChrTalk(    #77
        0x103,
        "#023F#2PEstelle, what's wrong?\x02",
    )

    CloseMessageWindow()

    label("loc_2B94")


    ChrTalk(    #78
        0x101,
        (
            "#1025F#6PMatron Theresa...\x02\x03",

            "You're not going to ask\x01",
            "about Joshua, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#757F#4PAh...\x02\x03",

            "#754FKloe...already told me everything.\x02\x03",

            "She worries easily, and she needed\x01",
            "to unburden her soul onto someone\x01",
            "when she found out...\x02\x03",

            "#756FEstelle...you've been through so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1026F#6PI...\x02\x03",

            "#1016FHaha... Come on...\x02\x03",

            "If you say things like that, I...\x02\x03",

            "#1027FI can't...hold it in...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(    #81
        0x106,
        "#552F#2P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D64")

    label("loc_2D48")


    ChrTalk(    #82
        0x103,
        "#522F#2POh, Estelle...\x02",
    )

    CloseMessageWindow()

    label("loc_2D64")


    ChrTalk(    #83
        0x8,
        (
            "#754F#4P...\x02\x03",

            "#750FYou don't need to hold it in.\x01",
            "You shouldn't...\x02\x03",

            "I'm all too familiar with how it\x01",
            "feels to lose someone important.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DF3():
        OP_6D(3360, 0, 29840, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DF3)
    OP_8E(0x8, 0xDAC, 0x0, 0x742C, 0x3E8, 0x0)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x1, 0x3E8)
    Sleep(500)

    ChrTalk(    #84
        0x101,
        "#1027F#6P...*sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#754F#4PNow, now. Don't say anything.\x02\x03",

            "I may not be able to be a mother\x01",
            "for you, but...\x02\x03",

            "At the very least...I can hold you\x01",
            "for a little while.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EEA():
        OP_6D(-150, 0, 38820, 4000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EEA)

    def lambda_2F02():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2F02)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2F32")

    Return()

    # Function_13_1E8F end

    def Function_14_2F33(): pass

    label("Function_14_2F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F44")
    Call(0, 15)

    label("loc_2F44")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x101, 470, 0, -2190, 0)
    SetChrPos(0xF7, -200, 0, -3480, 8)
    SetChrPos(0x109, 1300, 0, -2780, 0)
    SetChrPos(0x8, 390, 0, 480, 185)
    SetChrPos(0x9, 1160, 0, -90, 196)
    SetChrPos(0xA, -80, 0, 940, 186)
    SetChrPos(0xB, -1070, 0, 370, 193)
    SetChrPos(0xC, 2210, 0, 150, 208)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_6D(1020, 0, -510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30E3")

    ChrTalk(    #86
        0x8,
        (
            "#750FEstelle, Agate.\x02\x03",

            "Whenever you're in Ruan, you're\x01",
            "more than welcome to stop by.\x02\x03",

            "Father, I'll see you the next time\x01",
            "there's a class, I hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317E")

    label("loc_30E3")


    ChrTalk(    #87
        0x8,
        (
            "#750FEstelle, Scherazard.\x02\x03",

            "Whenever you're in Ruan, you're\x01",
            "more than welcome to stop by.\x02\x03",

            "Father, I'll see you the next\x01",
            "time there's a class, I hope.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317E")


    ChrTalk(    #88
        0x101,
        "#1017F#2PYeah, you bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x109,
        (
            "#1061FAb-so-lutely! I'll drop by every time\x01",
            "I have a chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#771FSee ya, Father Kevin!\x02\x03",

            "#770FYou too, Estelle!\x02\x03",

            "And bring Joshua next time too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1016F#2PY-Yeah...\x02\x03",

            "#1006FI dunno when I'll be back...\x01",
            "but we will come see you again!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2F33 end

    def Function_15_32AF(): pass

    label("Function_15_32AF")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3328"),
        (1, "loc_332E"),
        (SWITCH_DEFAULT, "loc_3334"),
    )


    label("loc_3328")

    OP_A2(0x1200)
    Jump("loc_3334")

    label("loc_332E")

    OP_A2(0x1201)
    Jump("loc_3334")

    label("loc_3334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3342")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3346")

    label("loc_3342")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3346")

    Return()

    # Function_15_32AF end

    SaveToFile()

Try(main)
