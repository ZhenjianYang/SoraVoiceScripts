from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Private Dan',                          # 9
        'Private Aluts',                        # 10
        'Leader',                               # 11
        'Man in Black',                         # 12
        'Man in Black',                         # 13
        'Gentleman',                            # 14
        'Company Commander',                    # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Target Camera',                        # 20
        'Tourist',                              # 21
        'Tourist',                              # 22
        'Tourist',                              # 23
        'Tourist',                              # 24
        'Tourist',                              # 25
        'Woman',                                # 26
        'Woman',                                # 27
        'Woman',                                # 28
        'Woman',                                # 29
        'Woman',                                # 30
        'Woman',                                # 31
        'Woman',                                # 32
        'Woman',                                # 33
        'Woman',                                # 34
        'Woman',                                # 35
        'Woman',                                # 36
        'Woman',                                # 37
        'Woman',                                # 38
        'Woman',                                # 39
        'Archbishop Currant',                   # 40
        'Dummy',                                # 41
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


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01600 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT27/CH03460 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT27/CH04230 ._CH',             # 09
        'ED6_DT26/CH20618 ._CH',             # 0A
        'ED6_DT26/CH20419 ._CH',             # 0B
        'ED6_DT07/CH01410 ._CH',             # 0C
        'ED6_DT07/CH01400 ._CH',             # 0D
        'ED6_DT07/CH01030 ._CH',             # 0E
        'ED6_DT07/CH01130 ._CH',             # 0F
        'ED6_DT07/CH01230 ._CH',             # 10
        'ED6_DT07/CH01170 ._CH',             # 11
        'ED6_DT07/CH01070 ._CH',             # 12
        'ED6_DT07/CH01350 ._CH',             # 13
        'ED6_DT07/CH00323 ._CH',             # 14
        'ED6_DT27/CH03420 ._CH',             # 15
        'ED6_DT27/CH04462 ._CH',             # 16
        'ED6_DT27/CH04460 ._CH',             # 17
        'ED6_DT27/CH04461 ._CH',             # 18
        'ED6_DT26/CH20613 ._CH',             # 19
        'ED6_DT26/CH20683 ._CH',             # 1A
        'ED6_DT26/CH20690 ._CH',             # 1B
        'ED6_DT27/CH03231 ._CH',             # 1C
        'ED6_DT26/CH20684 ._CH',             # 1D
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01600P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT27/CH03460P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT27/CH04230P._CP',             # 09
        'ED6_DT26/CH20618P._CP',             # 0A
        'ED6_DT26/CH20419P._CP',             # 0B
        'ED6_DT07/CH01410P._CP',             # 0C
        'ED6_DT07/CH01400P._CP',             # 0D
        'ED6_DT07/CH01030P._CP',             # 0E
        'ED6_DT07/CH01130P._CP',             # 0F
        'ED6_DT07/CH01230P._CP',             # 10
        'ED6_DT07/CH01170P._CP',             # 11
        'ED6_DT07/CH01070P._CP',             # 12
        'ED6_DT07/CH01350P._CP',             # 13
        'ED6_DT07/CH00323P._CP',             # 14
        'ED6_DT27/CH03420P._CP',             # 15
        'ED6_DT27/CH04462P._CP',             # 16
        'ED6_DT27/CH04460P._CP',             # 17
        'ED6_DT27/CH04461P._CP',             # 18
        'ED6_DT26/CH20613P._CP',             # 19
        'ED6_DT26/CH20683P._CP',             # 1A
        'ED6_DT26/CH20690P._CP',             # 1B
        'ED6_DT27/CH03231P._CP',             # 1C
        'ED6_DT26/CH20684P._CP',             # 1D
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6640,
        Z                   = 0,
        Y                   = 24120,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = 2060,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8130,
        Z                   = 0,
        Y                   = 11800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6210,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 12840,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0xC8,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_5BA",          # 00, 0
        "Function_1_649",          # 01, 1
        "Function_2_66A",          # 02, 2
        "Function_3_7E7",          # 03, 3
        "Function_4_80B",          # 04, 4
        "Function_5_82F",          # 05, 5
        "Function_6_949",          # 06, 6
        "Function_7_A70",          # 07, 7
        "Function_8_1888",         # 08, 8
        "Function_9_1BD7",         # 09, 9
        "Function_10_1EE7",        # 0A, 10
        "Function_11_1F0F",        # 0B, 11
        "Function_12_1F37",        # 0C, 12
        "Function_13_1F5F",        # 0D, 13
        "Function_14_1FC3",        # 0E, 14
        "Function_15_205C",        # 0F, 15
        "Function_16_29E7",        # 10, 16
        "Function_17_2AEB",        # 11, 17
        "Function_18_34B9",        # 12, 18
        "Function_19_34F1",        # 13, 19
        "Function_20_3529",        # 14, 20
        "Function_21_4C21",        # 15, 21
        "Function_22_4CC9",        # 16, 22
        "Function_23_4D51",        # 17, 23
        "Function_24_4DD9",        # 18, 24
        "Function_25_4E41",        # 19, 25
        "Function_26_4EE2",        # 1A, 26
    )


    def Function_0_5BA(): pass

    label("Function_0_5BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_5DC")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_5EF")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_5EF")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_5EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 17)

    label("loc_60D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_635")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_648")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_648")

    Return()

    # Function_0_5BA end

    def Function_1_649(): pass

    label("Function_1_649")

    OP_B1("T4200_n")
    OP_72(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_649 end

    def Function_2_66A(): pass

    label("Function_2_66A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7D1")

    label("loc_68F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7D1")

    label("loc_6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7D1")

    label("loc_6C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7D1")

    label("loc_6DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7D1")

    label("loc_6F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7D1")

    label("loc_70C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_725")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7D1")

    label("loc_725")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7D1")

    label("loc_73E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7D1")

    label("loc_757")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7D1")

    label("loc_770")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_789")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7D1")

    label("loc_789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7D1")

    label("loc_7A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7D1")

    label("loc_7BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7D1")

    label("loc_7E6")

    Return()

    # Function_2_66A end

    def Function_3_7E7(): pass

    label("Function_3_7E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_80A")
    OP_8D(0xFE, 2620, 2600, -590, 3530, 2000)
    Jump("Function_3_7E7")

    label("loc_80A")

    Return()

    # Function_3_7E7 end

    def Function_4_80B(): pass

    label("Function_4_80B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82E")
    OP_8D(0xFE, -1730, 10700, -4110, 14100, 2000)
    Jump("Function_4_80B")

    label("loc_82E")

    Return()

    # Function_4_80B end

    def Function_5_82F(): pass

    label("Function_5_82F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    OP_6D(-1020, 3250, -890, 0)
    OP_67(0, 9510, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(45000, 0)
    OP_6E(455, 0)

    def lambda_8A6():
        OP_6D(-1020, 3250, 37010, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8A6)

    def lambda_8BE():
        OP_67(0, 4330, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8BE)

    def lambda_8D6():
        OP_6B(3320, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8D6)

    def lambda_8E6():
        OP_6C(33000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8E6)

    def lambda_8F6():
        OP_6E(455, 8000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_8F6)
    OP_43(0x1E, 0x0, 0x0, 0x6)
    OP_43(0x1F, 0x0, 0x0, 0x6)
    OP_62(0x1C, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_82F end

    def Function_6_949(): pass

    label("Function_6_949")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6F")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_985")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_985")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC")
    Sleep(1300)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_9AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D3")
    Sleep(1600)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_9D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    Sleep(1900)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_9FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21")
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_A21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A48")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")
    Sleep(2800)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_A6C")

    Jump("Function_6_949")

    label("loc_A6F")

    Return()

    # Function_6_949 end

    def Function_7_A70(): pass

    label("Function_7_A70")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1300, 250, 42740, 0)
    OP_67(0, 6060, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 450)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -1300, 0, 28300, 180)
    SetChrPos(0x11, 1300, 0, 28700, 180)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    LoadEffect(0x0, "map\\\\mp012_00.eff")
    SoundLoad(228)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x21, 390, 0, 27650, 45)
    SetChrPos(0x22, -1260, 0, 27080, 0)
    SetChrPos(0x23, -500, 0, 26260, 0)
    SetChrPos(0x24, 940, 0, 26760, 0)
    SetChrPos(0x25, 1880, 0, 26230, 0)
    SetChrPos(0x26, -2040, 0, 25530, 0)
    SetChrPos(0x27, 240, 0, 25280, 0)
    SetChrPos(0x28, -2880, 0, 26700, 45)
    SetChrPos(0x29, 1370, 0, 24890, 0)
    SetChrPos(0x2A, 2320, 0, 27300, 315)
    SetChrPos(0x2B, -3270, 0, 25200, 45)
    SetChrPos(0x2C, -1760, 0, 24490, 0)
    SetChrPos(0x2D, 180, 0, 24020, 0)
    SetChrPos(0x2E, 2860, 0, 25120, 315)
    SetChrPos(0x10E, 0, 750, 51200, 180)
    FadeToBright(2000, 0)

    def lambda_C6F():
        OP_8E(0xFE, 0x0, 0x2EE, 0xACA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_C6F)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #0
        0x10E,
        "Captain Schwarz",
        (
            "#170F#5PBeing granted a day off is all well and good in\x01",
            "theory...\x02\x03",

            "#176F...but I haven't had one in so long, I haven't the\x01",
            "faintest idea what to do with it.\x02\x03",

            "Should I go shopping? Perhaps do maintenance\x01",
            "work on my equipment? Or would I be best\x01",
            "just returning to my room and reading a book?\x02\x03",

            "#175F...No. I need to do more than simply rest with my\x01",
            "time. I need to use it productively.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #1
        0x10E,
        "Captain Schwarz",
        (
            "#179F#5PI know! Wouldn't it be nice to take a light stroll\x01",
            "along the scenic route? I haven't done that in\x01",
            "ages.\x02\x03",

            "#170FIt would be an excellent use of my time, even.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F01():
        OP_8E(0xFE, 0x0, 0x0, 0x940C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_F01)
    WaitChrThread(0x10E, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x1388)

    def lambda_F42():
        OP_6D(1160, 0, 27600, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_F42)

    def lambda_F5A():
        OP_67(0, 5340, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_F5A)

    def lambda_F72():
        OP_6B(3280, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_F72)

    def lambda_F82():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_F82)
    WaitChrThread(0x1B, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x21,
        (
            "#4PIs it really true that Julia has returned\x01",
            "to Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x22,
        "#4PWhere is she?! WHERE. IS. SHE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "#1PP-Please, don't push!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        "#1PEveryone, please calm down!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10E, 120, 0, 37400, 180)

    def lambda_1055():
        OP_8E(0xFE, 0x78, 0x0, 0x78DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1055)
    WaitChrThread(0x10E, 0x1)

    NpcTalk(    #6
        0x10E,
        "Captain Schwarz",
        "#173FWh-What exactly is going on here?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)

    def lambda_10EA():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_10EA)

    def lambda_10F8():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_10F8)
    WaitChrThread(0x10, 0x2)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #7
        0x10,
        (
            "C-Captain?!\x02\x03",

            "Oh, no... Why did you have to come now?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#2PIt's dangerous here! Please, retreat back\x01",
            "inside the castle at once!\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x21, 255)
    OP_8C(0x21, 0, 500)
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    NpcTalk(    #9
        0x21,
        "Shrill Voice",
        "#4PIt's Julia!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    OP_4A(0x2C, 255)
    OP_4A(0x2D, 255)
    OP_4A(0x2E, 255)

    NpcTalk(    #10
        0x22,
        "Shrill Voice",
        "#4PWhat?!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x52)
    Sleep(500)
    OP_43(0x21, 0x0, 0x0, 0x8)
    OP_43(0x21, 0x3, 0x0, 0xA)
    Sleep(500)

    NpcTalk(    #11
        0x23,
        "Shrill Scream",
        "#4P*squeal* It really is!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10E, 225, 600)
    Sleep(600)
    OP_8C(0x10E, 135, 600)
    Sleep(600)
    OP_8C(0x10E, 180, 600)
    Sleep(300)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #12
        0x10E,
        "Captain Schwarz",
        "#172FWh-What the devil is this?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x23,
        "Shrill Scream",
        "#3S#4PJuliaaaaaaaaa!#2S\x02",
    )

    CloseMessageWindow()
    OP_44(0x21, 0x0)
    Sleep(100)

    def lambda_1336():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1336)

    def lambda_1344():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1344)

    def lambda_1352():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1352)

    def lambda_136C():
        OP_8F(0xFE, 0xFFFFFAEC, 0x0, 0x7148, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_136C)

    def lambda_1387():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1387)

    def lambda_13A1():
        OP_8F(0xFE, 0x514, 0x0, 0x72D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_13A1)

    def lambda_13BC():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_13BC)

    def lambda_13D1():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_13D1)

    def lambda_13E6():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_13E6)
    Sleep(50)

    def lambda_1400():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_1400)

    def lambda_1415():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1415)

    def lambda_142A():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_142A)
    Sleep(50)

    def lambda_1444():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1444)

    def lambda_1459():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_1459)

    def lambda_146E():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_146E)
    Sleep(50)

    def lambda_1488():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_1488)

    def lambda_149D():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_149D)

    def lambda_14B2():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_14B2)
    Sleep(50)

    def lambda_14CC():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_14CC)

    def lambda_14E1():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_14E1)
    Sleep(100)
    OP_44(0x21, 0x2)
    OP_44(0x22, 0x2)
    OP_44(0x23, 0x2)
    Sleep(100)
    OP_44(0x24, 0x2)
    OP_44(0x25, 0x2)
    OP_44(0x26, 0x2)
    Sleep(100)
    OP_44(0x27, 0x2)
    OP_44(0x28, 0x2)
    OP_44(0x29, 0x2)
    Sleep(100)
    OP_44(0x2A, 0x2)
    OP_44(0x2B, 0x2)
    OP_44(0x2C, 0x2)
    Sleep(100)
    OP_44(0x2D, 0x2)
    OP_44(0x2E, 0x2)
    OP_43(0x21, 0x0, 0x0, 0x8)

    NpcTalk(    #14
        0x10E,
        "Captain Schwarz",
        "#174F...Wha...?!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x30, 120, 0, 31300, 0)
    OP_8C(0x10E, 0, 500)

    def lambda_158C():
        OP_6D(1160, 0, 32600, 1500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_158C)
    OP_62(0x30, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_15B6():
        OP_8E(0xFE, 0x78, 0x2EE, 0xBCAC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_15B6)

    def lambda_15D1():
        OP_8E(0xFE, 0x78, 0x2EE, 0xBB44, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_15D1)
    Sleep(1500)

    NpcTalk(    #15
        0x23,
        "Shrill Scream",
        "#3S#4PWaaait! Juliaaaaaa!#2S㈱\x02",
    )

    CloseMessageWindow()
    OP_43(0x21, 0x3, 0x0, 0xB)

    NpcTalk(    #16
        0x22,
        "Shrill Scream",
        "#3S#4PDon't gooooooooo!#2S\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0xD)
    Sleep(150)
    OP_22(0xAF, 0x0, 0x64)
    OP_43(0x21, 0x3, 0x0, 0xC)

    def lambda_1670():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_1670)

    def lambda_168B():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_168B)
    Sleep(50)

    def lambda_16AB():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_16AB)

    def lambda_16C6():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_16C6)
    Sleep(50)

    def lambda_16E6():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_16E6)

    def lambda_1701():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_1701)
    Sleep(100)
    OP_43(0x11, 0x3, 0x0, 0xE)
    Sleep(150)

    def lambda_172D():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_172D)
    Sleep(50)

    def lambda_174D():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_174D)

    def lambda_1768():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1768)
    Sleep(50)

    def lambda_1788():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1788)

    def lambda_17A3():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_17A3)
    Sleep(50)

    def lambda_17C3():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_17C3)

    def lambda_17DE():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_17DE)

    def lambda_17F9():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_17F9)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_43(0x21, 0x0, 0x0, 0x9)
    OP_0D()
    OP_20(0x1388)
    OP_24(0x85, 0x5A)
    Sleep(500)
    OP_24(0x85, 0x50)
    Sleep(500)
    OP_24(0x85, 0x46)
    Sleep(400)
    OP_24(0x85, 0x3C)
    Sleep(300)
    OP_24(0x85, 0x32)
    Sleep(300)
    OP_24(0x85, 0x28)
    Sleep(300)
    OP_24(0x85, 0x1E)
    Sleep(300)
    OP_24(0x85, 0x14)
    Sleep(300)
    OP_23(0x85)
    Sleep(800)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_A70 end

    def Function_8_1888(): pass

    label("Function_8_1888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BD6")
    OP_62(0x27, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_18CA():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_18CA)
    Sleep(200)
    OP_62(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1920():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_1920)
    Sleep(300)
    OP_62(0x24, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1976():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1976)
    Sleep(200)
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_19CC():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_19CC)
    Sleep(400)

    def lambda_19EF():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_19EF)
    OP_62(0x2C, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1A40():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1A40)
    Sleep(300)
    OP_62(0x2A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1A96():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1A96)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1AEC():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1AEC)
    Sleep(300)
    OP_62(0x2B, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1B42():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1B42)
    Sleep(400)

    def lambda_1B65():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1B65)
    OP_62(0x2D, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1BB6():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_1BB6)
    Sleep(400)
    Jump("Function_8_1888")

    label("loc_1BD6")

    Return()

    # Function_8_1888 end

    def Function_9_1BD7(): pass

    label("Function_9_1BD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EE6")
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1C02():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1C02)
    Sleep(200)
    OP_62(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1C53():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_1C53)
    Sleep(300)
    OP_62(0x24, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1CA4():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1CA4)
    Sleep(200)
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1CF5():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1CF5)
    Sleep(400)

    def lambda_1D18():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1D18)
    OP_62(0x2C, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x2E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1D64():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1D64)
    Sleep(300)
    OP_62(0x2A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1DB5():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1DB5)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1E06():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1E06)
    Sleep(300)
    OP_62(0x2B, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1E57():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1E57)
    Sleep(400)

    def lambda_1E7A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1E7A)
    OP_62(0x2D, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1EC6():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_1EC6)
    Sleep(400)
    Jump("Function_9_1BD7")

    label("loc_1EE6")

    Return()

    # Function_9_1BD7 end

    def Function_10_1EE7(): pass

    label("Function_10_1EE7")

    OP_22(0x85, 0x1, 0x50)

    label("loc_1EEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F0E")
    OP_7C(0x0, 0x78, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_1EEC")

    label("loc_1F0E")

    Return()

    # Function_10_1EE7 end

    def Function_11_1F0F(): pass

    label("Function_11_1F0F")

    OP_22(0x85, 0x1, 0x50)

    label("loc_1F14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F36")
    OP_7C(0x0, 0xB4, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_1F14")

    label("loc_1F36")

    Return()

    # Function_11_1F0F end

    def Function_12_1F37(): pass

    label("Function_12_1F37")

    OP_22(0x85, 0x1, 0x64)

    label("loc_1F3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F5E")
    OP_7C(0x0, 0xF0, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_1F3C")

    label("loc_1F5E")

    Return()

    # Function_12_1F37 end

    def Function_13_1F5F(): pass

    label("Function_13_1F5F")

    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(    #17 op#A
        0x10,
        "#10A#3S#1PGuh!#2S\x02",
    )

    Sleep(200)
    SetChrChipByIndex(0x10, 20)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x4)

    def lambda_1F94():
        OP_96(0xFE, 0xFFFFF510, 0xFFFFFE70, 0x7C60, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F94)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 0, 0)
    SetChrChipByIndex(0x10, 11)
    SetChrSubChip(0x10, 0)
    Return()

    # Function_13_1F5F end

    def Function_14_1FC3(): pass

    label("Function_14_1FC3")

    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(    #18 op#A
        0x11,
        "#10A#3S#5PAgh!#2S\x02",
    )

    Sleep(200)
    OP_8C(0x11, 270, 0)
    SetChrChipByIndex(0x11, 20)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x4)

    def lambda_1FFF():
        OP_96(0xFE, 0x1900, 0xFFFFF448, 0x7E90, 0x5DC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FFF)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_22(0xE4, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 6400, -3000, 32400, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_14_1FC3 end

    def Function_15_205C(): pass

    label("Function_15_205C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1220, 0, 42880, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -1660, 0, 41680, 180)
    SetChrPos(0x11, 1660, 0, 41680, 180)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x21, 690, 0, 40650, 0)
    SetChrPos(0x22, -960, 0, 40480, 0)
    SetChrPos(0x23, -200, 0, 39560, 0)
    SetChrPos(0x24, 1240, 0, 39760, 0)
    SetChrPos(0x25, 2180, 0, 39230, 0)
    SetChrPos(0x26, -1740, 0, 38830, 0)
    SetChrPos(0x27, 540, 0, 38280, 0)
    SetChrPos(0x28, -2580, 0, 40000, 45)
    SetChrPos(0x29, 1670, 0, 37890, 0)
    SetChrPos(0x2A, 2620, 0, 40300, 315)
    SetChrPos(0x2B, -2970, 0, 38500, 45)
    SetChrPos(0x2C, -1460, 0, 37790, 0)
    SetChrPos(0x2D, -180, 0, 37020, 0)
    SetChrPos(0x2E, 3160, 0, 38120, 315)
    SetChrPos(0x10E, 340, 750, 51700, 180)
    SetChrChipByIndex(0x10E, 12)
    SetChrSubChip(0x10E, 0)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, 0, 750, 51200, 180)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #19
        0x10,
        (
            "#1PEveryone! Please move a little farther\x01",
            "from the castle gates!\x02",
        )
    )

    OP_9E(0x10, 0x1E, 0x0, 0x1F4, 0xBB8)
    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#1PPlease, just a little more!\x02",
    )

    CloseMessageWindow()
    OP_9E(0x10, 0x1E, 0x0, 0x12C, 0xBB8)
    Sleep(800)

    ChrTalk(    #21
        0x11,
        "#1PIf everyone could please remain calm...\x02",
    )

    OP_9E(0x11, 0x1E, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    OP_70(0x0, 0x1C2)
    Sleep(800)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_237C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_237C)

    def lambda_239A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_239A)
    Sleep(600)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    OP_4A(0x2C, 255)
    OP_4A(0x2D, 255)
    OP_4A(0x2E, 255)

    def lambda_23F5():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_23F5)
    OP_8C(0x11, 0, 500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x21, 0x0, 0x0, 0x8)
    Sleep(1000)

    NpcTalk(    #22
        0x21,
        "Shrill Scream",
        "#4PI-It's Julia!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0x22,
        "Shrill Scream",
        "#4PShe's coming out! She's coming out!\x02",
    )

    CloseMessageWindow()

    def lambda_2498():
        OP_6D(0, 0, 43900, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_2498)

    def lambda_24B0():
        OP_67(0, 5800, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_24B0)

    def lambda_24C8():
        OP_6B(3260, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_24C8)

    def lambda_24D8():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_24D8)

    def lambda_24E8():

        label("loc_24E8")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24E8")

    QueueWorkItem2(0x10, 2, lambda_24E8)

    def lambda_24F9():

        label("loc_24F9")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24F9")

    QueueWorkItem2(0x11, 2, lambda_24F9)

    def lambda_250A():

        label("loc_250A")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_250A")

    QueueWorkItem2(0x21, 2, lambda_250A)

    def lambda_251B():

        label("loc_251B")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_251B")

    QueueWorkItem2(0x22, 2, lambda_251B)

    def lambda_252C():

        label("loc_252C")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_252C")

    QueueWorkItem2(0x23, 2, lambda_252C)

    def lambda_253D():

        label("loc_253D")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_253D")

    QueueWorkItem2(0x24, 2, lambda_253D)

    def lambda_254E():

        label("loc_254E")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_254E")

    QueueWorkItem2(0x25, 2, lambda_254E)

    def lambda_255F():

        label("loc_255F")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_255F")

    QueueWorkItem2(0x26, 2, lambda_255F)

    def lambda_2570():

        label("loc_2570")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2570")

    QueueWorkItem2(0x27, 2, lambda_2570)

    def lambda_2581():

        label("loc_2581")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2581")

    QueueWorkItem2(0x28, 2, lambda_2581)

    def lambda_2592():

        label("loc_2592")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2592")

    QueueWorkItem2(0x29, 2, lambda_2592)

    def lambda_25A3():

        label("loc_25A3")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_25A3")

    QueueWorkItem2(0x2A, 2, lambda_25A3)

    def lambda_25B4():

        label("loc_25B4")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_25B4")

    QueueWorkItem2(0x2B, 2, lambda_25B4)

    def lambda_25C5():

        label("loc_25C5")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_25C5")

    QueueWorkItem2(0x2C, 2, lambda_25C5)

    def lambda_25D6():

        label("loc_25D6")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_25D6")

    QueueWorkItem2(0x2D, 2, lambda_25D6)

    def lambda_25E7():

        label("loc_25E7")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_25E7")

    QueueWorkItem2(0x2E, 2, lambda_25E7)

    def lambda_25F8():
        OP_8E(0xFE, 0x0, 0x2EE, 0xACD0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_25F8)
    Sleep(50)

    def lambda_2618():
        OP_8E(0xFE, 0x154, 0x2EE, 0xAEC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_2618)
    WaitChrThread(0x2F, 0x1)
    OP_44(0x21, 0x0)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x29, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x22,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x21,
        "Aww... It's just the archbishop and a sister...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x2F,
        (
            "Come, now, everyone. Move aside and let us\x01",
            "pass.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #27
        0x10E,
        "Sister Ellen",
        "...\x02",
    )

    CloseMessageWindow()

    def lambda_27D4():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_27D4)

    def lambda_27EF():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_27EF)
    Sleep(50)

    def lambda_280F():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_280F)

    def lambda_282A():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_282A)
    Sleep(50)

    def lambda_284A():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_284A)

    def lambda_2865():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2865)

    def lambda_2880():
        OP_91(0xFE, 0x190, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2880)
    Sleep(50)

    def lambda_28A0():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_28A0)

    def lambda_28BB():
        OP_91(0xFE, 0x190, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_28BB)
    Sleep(50)

    def lambda_28DB():
        OP_91(0xFE, 0xC8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_28DB)

    def lambda_28F6():
        OP_91(0xFE, 0xC8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_28F6)

    def lambda_2911():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_2911)

    def lambda_292C():
        OP_8E(0xFE, 0x0, 0x0, 0x85C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_292C)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_295E():
        OP_8E(0xFE, 0x154, 0x0, 0x87B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_295E)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_205C end

    def Function_16_29E7(): pass

    label("Function_16_29E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -2090, 0, 42000, 180)
    SetChrPos(0x11, 2440, 0, 42000, 180)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x1C2, 0x0, 0x64)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 450)

    def lambda_2A65():
        OP_6E(496, 9000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2A65)
    OP_6D(3500, 100, 49020, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(37000, 0)
    OP_6E(496, 0)

    def lambda_2AB2():
        OP_6B(3330, 5000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_2AB2)
    FadeToBright(2000, 0)
    OP_0D()
    OP_23(0x1C2)
    WaitChrThread(0x1B, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_29E7 end

    def Function_17_2AEB(): pass

    label("Function_17_2AEB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(0, 3540, 26420, 0)
    OP_67(0, 2660, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 760, 0, 28520, 180)
    SetChrPos(0x13, -2280, 0, 30400, 180)
    SetChrPos(0x14, 2280, 0, 30400, 180)
    SetChrPos(0x15, -760, 0, 28520, 180)
    SetChrPos(0x103, -1400, 0, 18240, 0)
    SetChrPos(0x151, 0, 0, 18300, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #28
        0x12,
        "#2PThey're sure taking their time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        "#2PThe hell are they even doing?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 135, 400)
    Sleep(300)

    ChrTalk(    #30
        0x15,
        "#1PNow, now. There's no need to be so hasty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x15,
        (
            "#1PCapturing her isn't even necessary to the\x01",
            "plan as far as I'm concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x15,
        "#1PAs soon as the noon bell chimes...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 225, 400)
    Sleep(300)

    ChrTalk(    #33
        0x12,
        "#2PT-True as that may be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x12,
        (
            "#2PSure, that would invalidate the will and ensure\x01",
            "she doesn't get all of the money, but it'd also\x01",
            "mean you have to share it with everyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "#2PWhich means our share will end up going down...\x01",
            "I'd kinda like to avoid that if we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x15,
        "#1PDon't you worry. We've got plenty of options.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x15,
        (
            "#1PRemember: you're only dealing with a single\x01",
            "young girl.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x151,
        "Voice",
        "#5P...What?\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2F05():
        OP_6D(0, 0, 25920, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_2F05)

    def lambda_2F1D():
        OP_67(0, 3880, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2F1D)

    def lambda_2F35():
        OP_6B(3460, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_2F35)

    def lambda_2F45():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F45)
    Sleep(100)

    def lambda_2F58():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2F58)
    WaitChrThread(0x1B, 0x0)
    Sleep(500)

    def lambda_2F70():
        OP_8E(0xFE, 0x0, 0x0, 0x5398, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2F70)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #39
        0x151,
        (
            "#1653F#12PUn...cle...?\x02\x03",

            "#1656F...Why...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x15,
        "Oh, dear! What are you doing here, Aina?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x15,
        (
            "I keep telling you how dangerous it is to go\x01",
            "venturing outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x15,
        "And alone, at that.\x02",
    )

    CloseMessageWindow()

    def lambda_304A():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4FD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_304A)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #43
        0x103,
        (
            "#1644F#6PYou blind, old man?\x02\x03",

            "She isn't here alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x15,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x15,
        "Oh, I can see you. Getting in my WAY.\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x13, 0)
    Sleep(100)
    OP_7D(0x0, 0x103, 0xA, 0xC8)

    def lambda_3108():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0x52BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3108)
    WaitChrThread(0x103, 0x1)
    OP_7D(0x1, 0x103, 0x0, 0x0)

    def lambda_3130():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3130)
    OP_43(0x103, 0x3, 0x0, 0x12)
    Sleep(10)
    OP_43(0x151, 0x3, 0x0, 0x13)
    OP_22(0x1F7, 0x0, 0x64)
    SetChrSubChip(0x13, 1)
    Sleep(100)
    SetChrSubChip(0x13, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -1400, 0, 20440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    SetChrSubChip(0x13, 1)
    Sleep(100)
    SetChrSubChip(0x13, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0, 0, 21400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    Sleep(1000)

    ChrTalk(    #46
        0x103,
        (
            "#1647F#6P(Ugh... It's like they don't even care if they\x01",
            "kill Aina in the process!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x15,
        "#5PTsk tsk. That wasn't a very good shot.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13, 500)
    Sleep(300)

    ChrTalk(    #48
        0x15,
        "#5PI take it marksmanship isn't exactly your forte?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 0)
    Sleep(100)
    TurnDirection(0x13, 0x15, 500)
    Sleep(300)

    ChrTalk(    #49
        0x13,
        "S-Sorry, sir.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_3319():
        OP_8F(0xFE, 0x0, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3319)
    Sleep(500)

    def lambda_3339():
        OP_8F(0xFE, 0xFFFFFC40, 0x0, 0x4BF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3339)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #50
        0x151,
        "#1654F#12P...Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        "#1642F#6PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x151,
        (
            "#1654F#12PLet's just force our way through here.\x02\x03",

            "#1652FWe don't have time to mess around.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 9)
    SetChrSubChip(0x103, 0)
    Sleep(250)

    ChrTalk(    #53
        0x103,
        "#1640F#6PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x15,
        "It's time to come along home, Aina.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(600)
    TurnDirection(0x15, 0x151, 300)
    OP_0D()
    Sleep(300)
    OP_8C(0x13, 180, 500)
    Sleep(400)

    ChrTalk(    #55
        0x15,
        "...Everyone's waiting for you, you know.\x02",
    )

    CloseMessageWindow()
    Battle(0x3AF, 0x0, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 20)
    Return()

    # Function_17_2AEB end

    def Function_18_34B9(): pass

    label("Function_18_34B9")

    SetChrChipByIndex(0x103, 28)
    SetChrSubChip(0x103, 2)

    def lambda_34C9():
        OP_96(0xFE, 0xFFFFFC40, 0x0, 0x48D0, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34C9)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    Return()

    # Function_18_34B9 end

    def Function_19_34F1(): pass

    label("Function_19_34F1")

    SetChrChipByIndex(0x151, 29)
    SetChrSubChip(0x151, 2)

    def lambda_3501():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4A9C, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3501)
    WaitChrThread(0x151, 0x1)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    Return()

    # Function_19_34F1 end

    def Function_20_3529(): pass

    label("Function_20_3529")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0xE)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_6D(480, 0, 29600, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x12, 0x800)
    SetChrFlags(0x13, 0x800)
    SetChrFlags(0x14, 0x800)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x12, -2120, -200, 27400, 225)
    SetChrPos(0x13, -2080, 0, 30400, 270)
    SetChrPos(0x14, 2500, 0, 30260, 180)
    SetChrPos(0x15, 0, 0, 30200, 180)
    SetChrPos(0x103, -320, 0, 26220, 0)
    SetChrPos(0x151, 1340, 0, 26760, 0)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_364A"),
        (SWITCH_DEFAULT, "loc_3657"),
    )


    label("loc_364A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3664")

    label("loc_3657")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3664")

    label("loc_3664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36BE")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆Defeated Gentleman\x01",           # 0
            "◆Didn't defeat Gentleman\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_36BE")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_36CF"),
        (1, "loc_36E3"),
        (SWITCH_DEFAULT, "loc_36E6"),
    )


    label("loc_36CF")

    OP_8C(0x15, 0, 0)
    SetChrChipByIndex(0x15, 26)
    SetChrSubChip(0x15, 0)
    Jump("loc_36E6")

    label("loc_36E3")

    Jump("loc_36E6")

    label("loc_36E6")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_36F7"),
        (0, "loc_3D9B"),
        (SWITCH_DEFAULT, "loc_4003"),
    )


    label("loc_36F7")


    def lambda_36FD():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_36FD)
    FadeToBright(1000, 0)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x15, 90, 500)
    Sleep(500)
    OP_8C(0x15, 270, 500)
    Sleep(500)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x15, 90, 500)
    Sleep(500)
    OP_8C(0x15, 270, 500)
    Sleep(500)

    ChrTalk(    #56
        0x15,
        "Wh-What is the meaning of this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x15,
        (
            "I paid good mira to hire them, and THIS is the\x01",
            "quality of service I receive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x15,
        (
            "This has to be a breach of contract, surely.\x01",
            "This isn't acceptable at all!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x15, 90, 500)
    Sleep(500)
    OP_8C(0x15, 270, 500)
    Sleep(500)

    ChrTalk(    #59
        0x103,
        (
            "#1646F...I can barely bring myself to watch.\x02\x03",

            "#1642FI think it's time you took a little nap yourself.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38C6():
        OP_8E(0xFE, 0xFFFFFEC0, 0x0, 0x6BE4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38C6)
    WaitChrThread(0x103, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 9)
    SetChrSubChip(0x103, 0)
    Sleep(250)
    OP_8C(0x15, 180, 500)
    Sleep(200)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_391D():
        OP_8F(0xFE, 0x0, 0x0, 0x7A6C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_391D)
    Sleep(300)

    ChrTalk(    #60
        0x15,
        "Wh-What are you doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x15,
        "Is that all you're capable of? Reckless violence?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x15,
        "What a poor upbringing you must have had!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x1)

    ChrTalk(    #63
        0x103,
        "#1648F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x151,
        "#1654FUncle...\x02",
    )

    CloseMessageWindow()

    def lambda_39E9():
        OP_8E(0xFE, 0x410, 0x0, 0x6EC8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_39E9)
    WaitChrThread(0x151, 0x1)

    def lambda_3A09():
        OP_8E(0xFE, 0x0, 0x0, 0x7300, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3A09)
    WaitChrThread(0x151, 0x1)
    TurnDirection(0x151, 0x15, 500)
    Fade(250)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    Sleep(300)

    ChrTalk(    #65
        0x151,
        (
            "#1656FI've got no interest in inheriting Grandfather's\x01",
            "land or his money.\x02\x03",

            "That's not why I've been running away from you\x01",
            "or doing any of what I've done.\x02\x03",

            "#1654FBut much as I don't need it...\x02\x03",

            "#1652F...I know I don't want you to have a single mira\x01",
            "of it, either!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B50():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_3B50)

    def lambda_3B60():
        OP_8E(0xFE, 0x0, 0x0, 0x774C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3B60)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #66 op#A op#5
        0x151,
        "#1652F#6P#3S#17AI'm so sorry!#2S\x05\x02",
    )

    SetChrChipByIndex(0x151, 27)
    SetChrSubChip(0x151, 0)
    Sleep(800)

    def lambda_3BB5():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_3BB5)
    Sleep(600)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
    OP_22(0x8E, 0x0, 0x64)
    SetChrFlags(0x15, 0x4)

    def lambda_3BE5():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3BE5)

    def lambda_3BFF():
        OP_95(0xFE, 0xFFFFFF9C, 0xFFFFFF9C, 0x514, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3BFF)
    WaitChrThread(0x15, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x15, 26)
    SetChrSubChip(0x15, 0)
    OP_8C(0x15, 0, 0)
    Sleep(1000)

    def lambda_3C3D():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3C3D)
    Sleep(200)
    OP_62(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x103,
        (
            "#1645FDamn. That's gonna hurt in the morning...\x02\x03",

            "I sometimes really find myself doubting you're\x01",
            "actually from a rich family like you say you are.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    Sleep(100)
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #68
        0x151,
        (
            "#1651FHow awful of you to say such a thing.\x02\x03",

            "I'd like to believe I act the part more than you,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4003")

    label("loc_3D9B")


    def lambda_3DA1():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_3DA1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1B, 0x0)

    ChrTalk(    #69
        0x151,
        "#1652F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#1642FBoy, did he rub me the wrong way. Can I give\x01",
            "him another crack with my whip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x151,
        (
            "#1654FJust leave him. I can't even bring myself to feel\x01",
            "anything towards him anymore.\x02\x03",

            "#1656FI still don't think he was originally a bad person,\x01",
            "though.\x02\x03",

            "He'll come around when the whole inheritance\x01",
            "matter is settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#1646FYou really think so? I think you're being naive,\x01",
            "to be honest.\x02\x03",

            "#1642FHe was trying to kill you, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x151,
        (
            "#1650FIf he does anything to cause trouble again,\x01",
            "I'll hit him myself.\x02\x03",

            "#1651F...With this bag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        "#1645FTh-That sounds painful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4003")

    label("loc_4003")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 450)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x16, 0, 750, 44100, 180)
    SetChrPos(0x17, 1700, 750, 45000, 180)
    SetChrPos(0x18, -1700, 750, 45000, 180)
    SetChrPos(0x19, 1700, 750, 46420, 180)
    SetChrPos(0x1A, -1700, 750, 46420, 180)

    NpcTalk(    #75
        0x16,
        "Voice",
        "What are you doing?!\x02",
    )

    CloseMessageWindow()

    def lambda_40BD():
        OP_6D(480, 0, 42200, 1500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_40BD)

    def lambda_40D5():
        OP_6B(3400, 1500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_40D5)
    WaitChrThread(0x1B, 0x0)
    SetChrPos(0x103, -680, 0, 28940, 0)
    SetChrPos(0x151, 700, 0, 29340, 0)
    SetChrPos(0x15, -500, 0, 27040, 180)
    SetChrPos(0x12, 1460, 0, 27120, 225)
    SetChrPos(0x13, -2540, 0, 26100, 180)
    SetChrPos(0x14, -900, -400, 24780, 90)
    SetChrChipByIndex(0x12, 10)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x14, 25)
    SetChrSubChip(0x14, 0)
    Sleep(500)

    def lambda_4169():
        OP_6D(780, 0, 30200, 3000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_4169)

    def lambda_4181():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4181)

    def lambda_4199():
        OP_6B(3320, 3000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_4199)

    def lambda_41A9():
        OP_8E(0xFE, 0x0, 0x0, 0x7D3C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_41A9)
    Sleep(50)

    def lambda_41C9():
        OP_8E(0xFE, 0x6A4, 0x0, 0x8124, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_41C9)

    def lambda_41E4():
        OP_8E(0xFE, 0xFFFFF95C, 0x0, 0x8124, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_41E4)
    Sleep(50)

    def lambda_4204():
        OP_8E(0xFE, 0x6A4, 0x0, 0x8700, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4204)

    def lambda_421F():
        OP_8E(0xFE, 0xFFFFF95C, 0x0, 0x8700, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_421F)
    WaitChrThread(0x16, 0x1)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x17,
        "Wh-What in Aidios' name happened out here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x16,
        "Y-You there! Throw down your weapon at once!\x02",
    )

    CloseMessageWindow()

    def lambda_4324():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0x7300, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4324)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #78
        0x103,
        "#1642FI'm from the Bracer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x16,
        "What?! The guild?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05Scherazard showed the soldiers her junior bracer badge.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #81
        0x16,
        "S-So you are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x16,
        "Still, what's a bracer doing here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x16,
        (
            "Her Majesty may recognize the guild, but that\x01",
            "doesn't make it all right for you to cause a\x01",
            "commotion right outside the castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#1646FI had reason to believe that these people were\x01",
            "responsible for numerous criminal acts within\x01",
            "the capital.\x02\x03",

            "I knocked them out for the sake of peace and\x01",
            "order in Grancel, and the safety of its people.\x02\x03",

            "#1642F...So could you do me a favor and arrest them?\x01",
            "I haven't covered that part yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x16,
        "W-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x16,
        "...Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "Ordinarily, we'd be taking you away with us as\x01",
            "well, but I'll let you off this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 0, 600)
    Sleep(300)

    ChrTalk(    #88
        0x16,
        "You know what to do!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #89
        "\x07\x00#3SRight!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_43(0x17, 0x3, 0x0, 0x17)
    OP_43(0x18, 0x3, 0x0, 0x15)
    OP_43(0x19, 0x3, 0x0, 0x18)
    OP_43(0x1A, 0x3, 0x0, 0x16)
    Sleep(1000)
    OP_8C(0x16, 180, 500)
    Sleep(300)

    ChrTalk(    #90
        0x16,
        (
            "Still, while you may have gotten away without\x01",
            "punishment this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x16,
        (
            "...don't expect to be so lucky next time you try\x01",
            "and overreach your authority. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x16,
        (
            "Protecting the capital is OUR job, and we'll show\x01",
            "no mercy to anyone who causes trouble...bracer\x01",
            "or otherwise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        (
            "#1640FOh, it is? Cool, can I ask another favor, then?\x02\x03",

            "There're a bunch of their friends still in the city.\x01",
            "You couldn't take care of those, could you?\x02\x03",

            "#1641FOf course, last I saw, Kurt was with them, so you\x01",
            "probably won't have to lift a finger there, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x16,
        "U-Urghh...\x02",
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x19)

    def lambda_4913():

        label("loc_4913")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_4913")

    QueueWorkItem2(0x17, 3, lambda_4913)

    def lambda_4924():

        label("loc_4924")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_4924")

    QueueWorkItem2(0x18, 3, lambda_4924)
    Sleep(100)

    ChrTalk(    #95 op#A
        0x16,
        "#15AYou two! Follow me!\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #96
        0x17,
        "#11PS-Sir!\x02",
    )


    ChrTalk(    #97
        0x18,
        "#1PS-Sir!\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_497C():

        label("loc_497C")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_497C")

    QueueWorkItem2(0x103, 3, lambda_497C)

    def lambda_498D():

        label("loc_498D")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_498D")

    QueueWorkItem2(0x151, 3, lambda_498D)
    WaitChrThread(0x16, 0x3)
    OP_44(0x17, 0x3)

    def lambda_49A7():
        OP_8F(0xFE, 0x3AC, 0x0, 0x3AF2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_49A7)
    Sleep(100)
    OP_44(0x18, 0x3)

    def lambda_49CB():
        OP_8F(0xFE, 0xFFFFF5BA, 0x0, 0x36BA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_49CB)
    Sleep(1000)
    OP_44(0x103, 0x3)
    OP_44(0x151, 0x3)
    OP_44(0x17, 0x3)
    OP_44(0x18, 0x3)
    Sleep(800)

    ChrTalk(    #98
        0x103,
        (
            "#1645F*sigh* I'll never get used to dealing with the\x01",
            "army.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x151)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x103, 0x151, 400)
    Sleep(200)

    ChrTalk(    #99
        0x103,
        "#1643F...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x151,
        (
            "#1650F#2POh, I was just impressed by how much authority\x01",
            "the bracer badge wields.\x02\x03",

            "You were...kind of cool.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #101
        0x103,
        (
            "#1646FTh-That was the first time I've tried using my\x01",
            "badge like that, I'll have you know!\x02\x03",

            "#1642FBut never mind my badge now. We're running\x01",
            "out of time! We need to hurry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x151,
        "#1651F#2PRight!\x02",
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x1A)
    Sleep(50)
    OP_8C(0x151, 0, 500)

    def lambda_4BF7():
        OP_8E(0xFE, 0x2BC, 0x0, 0x99AC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4BF7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T4212   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3529 end

    def Function_21_4C21(): pass

    label("Function_21_4C21")


    def lambda_4C27():
        OP_8E(0xFE, 0xFFFFF894, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C27)
    WaitChrThread(0x18, 0x1)

    def lambda_4C47():
        OP_8E(0xFE, 0xFFFFF5EC, 0x0, 0x6DD8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C47)
    WaitChrThread(0x18, 0x1)

    def lambda_4C67():
        OP_8E(0xFE, 0xFFFFEFDE, 0x0, 0x670C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C67)
    WaitChrThread(0x18, 0x1)

    def lambda_4C87():
        OP_8E(0xFE, 0xFFFFF02E, 0x0, 0x5FDC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C87)
    WaitChrThread(0x18, 0x1)

    def lambda_4CA7():
        OP_8E(0xFE, 0xFFFFF5BA, 0x0, 0x5DCA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4CA7)
    WaitChrThread(0x18, 0x1)
    TurnDirection(0x18, 0x14, 500)
    Return()

    # Function_21_4C21 end

    def Function_22_4CC9(): pass

    label("Function_22_4CC9")


    def lambda_4CCF():
        OP_8E(0xFE, 0xFFFFF894, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4CCF)
    WaitChrThread(0x1A, 0x1)

    def lambda_4CEF():
        OP_8E(0xFE, 0xFFFFF5EC, 0x0, 0x6DD8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4CEF)
    WaitChrThread(0x1A, 0x1)

    def lambda_4D0F():
        OP_8E(0xFE, 0xFFFFEFDE, 0x0, 0x670C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4D0F)
    WaitChrThread(0x1A, 0x1)

    def lambda_4D2F():
        OP_8E(0xFE, 0xFFFFF362, 0x0, 0x670C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4D2F)
    WaitChrThread(0x1A, 0x1)
    TurnDirection(0x1A, 0x13, 500)
    Return()

    # Function_22_4CC9 end

    def Function_23_4D51(): pass

    label("Function_23_4D51")


    def lambda_4D57():
        OP_8E(0xFE, 0x76C, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D57)
    WaitChrThread(0x17, 0x1)

    def lambda_4D77():
        OP_8E(0xFE, 0xB40, 0x0, 0x6BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D77)
    WaitChrThread(0x17, 0x1)

    def lambda_4D97():
        OP_8E(0xFE, 0x820, 0x0, 0x64DC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D97)
    WaitChrThread(0x17, 0x1)

    def lambda_4DB7():
        OP_8E(0xFE, 0x3AC, 0x0, 0x6202, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4DB7)
    WaitChrThread(0x17, 0x1)
    TurnDirection(0x17, 0x14, 500)
    Return()

    # Function_23_4D51 end

    def Function_24_4DD9(): pass

    label("Function_24_4DD9")


    def lambda_4DDF():
        OP_8E(0xFE, 0x76C, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4DDF)
    WaitChrThread(0x19, 0x1)

    def lambda_4DFF():
        OP_8E(0xFE, 0xB40, 0x0, 0x6BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4DFF)
    WaitChrThread(0x19, 0x1)

    def lambda_4E1F():
        OP_8E(0xFE, 0x8C0, 0x0, 0x6928, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4E1F)
    WaitChrThread(0x19, 0x1)
    TurnDirection(0x19, 0x12, 500)
    Return()

    # Function_24_4DD9 end

    def Function_25_4E41(): pass

    label("Function_25_4E41")


    def lambda_4E47():
        OP_8E(0xFE, 0xFFFFF754, 0x0, 0x74F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4E47)
    WaitChrThread(0x16, 0x1)

    def lambda_4E67():
        OP_8E(0xFE, 0xFFFFF6FA, 0x0, 0x6F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4E67)
    WaitChrThread(0x16, 0x1)

    def lambda_4E87():
        OP_8E(0xFE, 0xFFFFED40, 0x0, 0x64F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4E87)
    WaitChrThread(0x16, 0x1)

    def lambda_4EA7():
        OP_8E(0xFE, 0xFFFFED40, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4EA7)
    WaitChrThread(0x16, 0x1)

    def lambda_4EC7():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4EC7)
    WaitChrThread(0x16, 0x1)
    Return()

    # Function_25_4E41 end

    def Function_26_4EE2(): pass

    label("Function_26_4EE2")

    OP_8C(0x103, 0, 500)

    def lambda_4EEF():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0x981C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4EEF)
    Return()

    # Function_26_4EE2 end

    SaveToFile()

Try(main)
