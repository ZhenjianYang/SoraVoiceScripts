from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0010   ._SN',
        MapName             = 'event',
        Location            = 'E0010.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Captain Grandt',                       # 9
        'Crew Mem. Timon',                      # 10
        'Crew Mem. Colton',                     # 11
        'Crew Mem. Clare',                      # 12
        'Crew Mem. Parker',                     # 13
        'Lloyd',                                # 14
        'Scherazard',                           # 15
        'Agate',                                # 16
        'Sister Rosa',                          # 17
        'Phelio',                               # 18
        'Lakeisha',                             # 19
        'Simon',                                # 20
        'Burrell',                              # 21
        'Orvid',                                # 22
        'Passenger',                            # 23
        'Passenger',                            # 24
        'Passenger',                            # 25
        'Passenger',                            # 26
        'Passenger',                            # 27
        'Passenger',                            # 28
        'Duncan',                               # 29
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
        'ED6_DT07/CH01443 ._CH',             # 00
        'ED6_DT07/CH01290 ._CH',             # 01
        'ED6_DT07/CH01293 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01290 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH00023 ._CH',             # 06
        'ED6_DT07/CH00053 ._CH',             # 07
        'ED6_DT07/CH01410 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01030 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01143 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH01013 ._CH',             # 0E
        'ED6_DT07/CH01213 ._CH',             # 0F
        'ED6_DT07/CH01103 ._CH',             # 10
        'ED6_DT07/CH01133 ._CH',             # 11
        'ED6_DT07/CH01490 ._CH',             # 12
        'ED6_DT07/CH01043 ._CH',             # 13
        'ED6_DT07/CH01450 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH01443P._CP',             # 00
        'ED6_DT07/CH01290P._CP',             # 01
        'ED6_DT07/CH01293P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01290P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH00023P._CP',             # 06
        'ED6_DT07/CH00053P._CP',             # 07
        'ED6_DT07/CH01410P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01030P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01143P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH01013P._CP',             # 0E
        'ED6_DT07/CH01213P._CP',             # 0F
        'ED6_DT07/CH01103P._CP',             # 10
        'ED6_DT07/CH01133P._CP',             # 11
        'ED6_DT07/CH01490P._CP',             # 12
        'ED6_DT07/CH01043P._CP',             # 13
        'ED6_DT07/CH01450P._CP',             # 14
    )

    DeclNpc(
        X                   = 59020,
        Z                   = -600,
        Y                   = 49310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 60800,
        Z                   = -2000,
        Y                   = 53360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 59190,
        Z                   = -1950,
        Y                   = 54200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 88840,
        Z                   = 0,
        Y                   = 47400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 85950,
        Z                   = 0,
        Y                   = 9240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 115970,
        Z                   = 0,
        Y                   = 11300,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 117330,
        Z                   = 200,
        Y                   = 1160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 117330,
        Z                   = 200,
        Y                   = 1160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 89500,
        Z                   = 0,
        Y                   = 9050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 91250,
        Z                   = 0,
        Y                   = 44510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 91250,
        Z                   = 0,
        Y                   = 45520,
        Direction           = 120,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 57200,
        Z                   = 0,
        Y                   = -1850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 117490,
        Z                   = 100,
        Y                   = 5290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 89340,
        Z                   = -1000,
        Y                   = 52850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 89270,
        Z                   = 200,
        Y                   = -3230,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 85350,
        Z                   = 150,
        Y                   = -1370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 117490,
        Z                   = 100,
        Y                   = 7300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 89270,
        Z                   = 150,
        Y                   = 430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 88030,
        Z                   = 0,
        Y                   = 430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 113400,
        Z                   = 100,
        Y                   = -630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 31990,
        Z                   = 0,
        Y                   = 5410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_4C4",          # 01, 1
        "Function_2_4EA",          # 02, 2
        "Function_3_667",          # 03, 3
        "Function_4_D31",          # 04, 4
        "Function_5_E11",          # 05, 5
        "Function_6_F33",          # 06, 6
        "Function_7_117C",         # 07, 7
        "Function_8_1287",         # 08, 8
        "Function_9_13AE",         # 09, 9
        "Function_10_16ED",        # 0A, 10
        "Function_11_18EB",        # 0B, 11
        "Function_12_1A05",        # 0C, 12
        "Function_13_1AB5",        # 0D, 13
        "Function_14_2378",        # 0E, 14
        "Function_15_2842",        # 0F, 15
        "Function_16_293F",        # 10, 16
        "Function_17_29F2",        # 11, 17
        "Function_18_2B34",        # 12, 18
        "Function_19_2C65",        # 13, 19
        "Function_20_2E1E",        # 14, 20
        "Function_21_2F15",        # 15, 21
        "Function_22_3094",        # 16, 22
        "Function_23_331D",        # 17, 23
        "Function_24_3427",        # 18, 24
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_89(0x101, 84860, 130, 5970, 0)

    label("loc_40F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_43F"),
        (102, "loc_43F"),
        (103, "loc_43F"),
        (104, "loc_43F"),
        (105, "loc_43F"),
        (106, "loc_43F"),
        (107, "loc_43F"),
        (109, "loc_43F"),
        (110, "loc_43F"),
        (115, "loc_43F"),
        (SWITCH_DEFAULT, "loc_4C3"),
    )


    label("loc_43F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 7)), scpexpr(EXPR_END)), "loc_45A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 0)), scpexpr(EXPR_END)), "loc_46B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 1)), scpexpr(EXPR_END)), "loc_47C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 2)), scpexpr(EXPR_END)), "loc_48D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 3)), scpexpr(EXPR_END)), "loc_49E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 5)), scpexpr(EXPR_END)), "loc_4AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    Event(0, 24)

    label("loc_4C0")

    Jump("loc_4C3")

    label("loc_4C3")

    Return()

    # Function_0_3F2 end

    def Function_1_4C4(): pass

    label("Function_1_4C4")

    OP_22(0x7A, 0x1, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4D8")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_4DD")

    label("loc_4D8")

    ClearChrFlags(0xF, 0x80)

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 1)), scpexpr(EXPR_END)), "loc_4E9")
    ClearChrFlags(0xD, 0x10)

    label("loc_4E9")

    Return()

    # Function_1_4C4 end

    def Function_2_4EA(): pass

    label("Function_2_4EA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_651")

    label("loc_50F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_528")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_651")

    label("loc_528")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_651")

    label("loc_541")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_651")

    label("loc_55A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_651")

    label("loc_573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_651")

    label("loc_58C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_651")

    label("loc_5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_651")

    label("loc_5BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_651")

    label("loc_5D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F0")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_651")

    label("loc_5F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_651")

    label("loc_609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_622")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_651")

    label("loc_622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_651")

    label("loc_63B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_651")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_666")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_651")

    label("loc_666")

    Return()

    # Function_2_4EA end

    def Function_3_667(): pass

    label("Function_3_667")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 7)), scpexpr(EXPR_END)), "loc_8E6")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69E")
    SetChrSubChip(0xFE, 1)
    Jump("loc_6C4")

    label("loc_69E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BF")
    SetChrSubChip(0xFE, 2)
    Jump("loc_6C4")

    label("loc_6BF")

    SetChrSubChip(0xFE, 0)

    label("loc_6C4")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_761")

    ChrTalk(    #0
        0xFE,
        "I'm glad to hear you found your father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Our trip won't last much longer, but enjoy\x01",
            "the rest of your journey through the sky.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E3")

    label("loc_761")

    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "Incidentally, miss...\x01",
            "Did you ever find your father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1000FAh, yeah. He did come back eventually.\x02\x03",

            "#1007FHe waited until the very last second\x01",
            "to show up, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "I see! I'm glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Just between you and I, I was a bit worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "After all, he IS the kind of man who would\x01",
            "be willing to leap off a moving airship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1008FAhaha... yeah, I...guess?\x02",
    )

    CloseMessageWindow()

    label("loc_8E3")

    Jump("loc_D28")

    label("loc_8E6")

    OP_A2(0x1207)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_920")
    SetChrSubChip(0xFE, 1)
    Jump("loc_946")

    label("loc_920")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_941")
    SetChrSubChip(0xFE, 2)
    Jump("loc_946")

    label("loc_941")

    SetChrSubChip(0xFE, 0)

    label("loc_946")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #8
        0xFE,
        "Do you have some business on the--\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #9
        0xFE,
        (
            "Wait a moment...\x01",
            "You're that girl from before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1011FHi, sir! I haven't seen you in a while.\x02\x03",

            "I saved you at the bandit hideout, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Yes, I thought so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "You must forgive me. I never had\x01",
            "a chance to properly thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Allow me to offer my thanks on\x01",
            "behalf of the entire crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1008FHaha, you're welcome! I was really\x01",
            "just doing my job, though.\x02\x03",

            "#1000FStill, it is kind of funny, though.\x02\x03",

            "Taking a trip on the same airship\x01",
            "I once helped to rescue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Repairing the damage those thugs did\x01",
            "took some time, but the Linde's as good\x01",
            "as new now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I'm sure she's doing her best with\x01",
            "you on board.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(600)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0x101,
        "#1004FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Haha! Looks like she heard us talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "With conditions like today's, we should\x01",
            "arrive in Ruan in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Please, enjoy the rest of your journey.\x01",
            "Let us know if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1001FI will. Thanks, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_D28")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_667 end

    def Function_4_D31(): pass

    label("Function_4_D31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DA4")

    ChrTalk(    #22
        0xFE,
        (
            "I'm glad the winds aren't too\x01",
            "strong today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "It'd be best to not stress the\x01",
            "engine too much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0D")

    label("loc_DA4")

    OP_A2(0x1)

    ChrTalk(    #24
        0xFE,
        "Maintain altitude, keep throttle at 60%.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Maintain heading until we reach\x01",
            "the Roubine River.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0D")

    TalkEnd(0xFE)
    Return()

    # Function_4_D31 end

    def Function_5_E11(): pass

    label("Function_5_E11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E93")

    ChrTalk(    #26
        0xFE,
        (
            "Ahem! In a moment, we will\x01",
            "be seeing a large river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "That is the Roubine River,\x01",
            "the largest in the kingdom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_E93")

    OP_A2(0x3)

    ChrTalk(    #28
        0xFE,
        (
            "Ahem! To the right, you can see\x01",
            "Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Regrettably, it is cloudy at the moment,\x01",
            "but you should be able to see the outline\x01",
            "of the lake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2F")

    TalkEnd(0xFE)
    Return()

    # Function_5_E11 end

    def Function_6_F33(): pass

    label("Function_6_F33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1019")

    ChrTalk(    #30
        0xFE,
        (
            "I've finished my duties at Grancel Cathedral\x01",
            "and I'm on my way home to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "The head of our church is...somewhat 'laid\x01",
            "back,' shall we say, so I'm a little worried\x01",
            "about how things have been in my absence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1178")

    label("loc_1019")

    OP_A2(0x4)

    ChrTalk(    #32
        0xFE,
        (
            "I've finished my duties at Grancel Cathedral\x01",
            "and I'm on my way home to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I must confess, though, all the time I've been\x01",
            "away, I've been so worried I thought I'd go\x01",
            "crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "This ship isn't even going the right way,\x01",
            "but I jumped on without thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Ohhh, did Sunday School end safely,\x01",
            "at least? Oh, dear, oh, dear...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1178")

    TalkEnd(0xFE)
    Return()

    # Function_6_F33 end

    def Function_7_117C(): pass

    label("Function_7_117C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #36
        0xFE,
        (
            "P-Please let nothing happen this time,\x01",
            "almighty Aidios...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1283")

    label("loc_11C8")

    OP_A2(0x7)

    ChrTalk(    #37
        0xFE,
        (
            "Th-This is my second time riding a\x01",
            "passenger liner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "The first time I rode one...\x01",
            "we got attacked by bandits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "P-Please let nothing happen this time,\x01",
            "almighty Aidios...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1283")

    TalkEnd(0xFE)
    Return()

    # Function_7_117C end

    def Function_8_1287(): pass

    label("Function_8_1287")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 2)), scpexpr(EXPR_END)), "loc_1331")

    ChrTalk(    #40
        0xFE,
        (
            "Our cargo this time is almost entirely\x01",
            "orbments we loaded on at Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I dunno why, but lately there's been a\x01",
            "lot of stuff gettin' shipped around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AA")

    label("loc_1331")

    OP_A2(0x120A)

    ChrTalk(    #42
        0xFE,
        (
            "This is the cargo room.\x01",
            "Ain't no place for passengers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Watch that you don't hit your head\x01",
            "wanderin' around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AA")

    TalkEnd(0xFE)
    Return()

    # Function_8_1287 end

    def Function_9_13AE(): pass

    label("Function_9_13AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1454")

    ChrTalk(    #44
        0xFE,
        (
            "Hmm, looking over the foodstuffs\x01",
            "of Manoria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "If I'm to get anything from this, I'll need\x01",
            "to make a list and investigate with\x01",
            "a careful plan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E9")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Cleared either Mushroom Hunt or Escort Job\x01",            # 0
            "Did not clear either Mushroom Hunt or Escort Job\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F7")
    OP_28(0x5, 0x4, 0x10)

    label("loc_14F7")

    OP_A2(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(    #46
        0xFE,
        (
            "Hmm...\x01",
            "Hmmmmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#1019F(This guy... Oh, no way.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I absolutely must make this\x01",
            "next deal happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I should look over the local\x01",
            "foodstuffs again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "That's a good idea. I should return to my\x01",
            "roots and do some plain old investigating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E9")

    label("loc_1623")


    ChrTalk(    #51
        0xFE,
        (
            "Hmmmmm, I absolutely must make\x01",
            "this deal happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I should look over the local\x01",
            "foodstuffs again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "That's a good idea. I should return to my\x01",
            "roots and do some plain old investigating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E9")

    TalkEnd(0xFE)
    Return()

    # Function_9_13AE end

    def Function_10_16ED(): pass

    label("Function_10_16ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17C7")

    ChrTalk(    #54
        0xFE,
        (
            "Phew! Man, just when I thought we'd get to\x01",
            "rest in Bose for a bit, it's straight off to Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Mirano's schedule is always so tight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "If nothing else, I guess it means we\x01",
            "don't waste time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E7")

    label("loc_17C7")

    OP_A2(0x6)

    ChrTalk(    #57
        0xFE,
        (
            "Phew! Man, just when I thought we'd get to\x01",
            "rest in Bose for a bit, it's straight off to Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "If that non-aggression pact with the Empire\x01",
            "happens, our trade in orbments is going to\x01",
            "explode, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "The plan is to get to Zeiss now and\x01",
            "secure some product in advance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E7")

    TalkEnd(0xFE)
    Return()

    # Function_10_16ED end

    def Function_11_18EB(): pass

    label("Function_11_18EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_199B")

    ChrTalk(    #60
        0xFE,
        (
            "Phelio HAS been working hard lately,\x01",
            "granted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I guess it's all right so long as he's\x01",
            "doing his job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "...Wait, no, I keep spoiling him like this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A01")

    label("loc_199B")

    OP_A2(0x5)

    ChrTalk(    #63
        0xFE,
        (
            "Hah! 'Sometimes,' he says.\x01",
            "'Sometimes,' my foot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "You've only JUST managed to find a job!\x02",
    )

    CloseMessageWindow()

    label("loc_1A01")

    TalkEnd(0xFE)
    Return()

    # Function_11_18EB end

    def Function_12_1A05(): pass

    label("Function_12_1A05")

    TalkBegin(0xFE)

    ChrTalk(    #65
        0xFE,
        (
            "I hear the casino in Ruan's FINALLY finished its\x01",
            "renovations. I left Grancel as soon as I heard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Sometimes you just need to kick back\x01",
            "and chill out, you know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1A05 end

    def Function_13_1AB5(): pass

    label("Function_13_1AB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 1)), scpexpr(EXPR_END)), "loc_1BFC")

    ChrTalk(    #67
        0xFE,
        (
            "Normally, when you think Ruan, you think\x01",
            "of sea fishing. But there're other good\x01",
            "fishing spots, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The Roubine River, the one that flows through\x01",
            "town, and the ever-famous Air-Letten waterfall\x01",
            "are also great fishing spots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "If you get the chance to visit them,\x01",
            "you should definitely bring your rod.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2374")

    label("loc_1BFC")

    OP_A2(0x1209)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 115920, 0, 10120, 0)
    OP_69(0x101, 0x0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #70
        0xFE,
        "Hmm. Valleria Lake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Somewhere in that wide-open lake...\x01",
            "the legendary Guardian of Valleria's\x01",
            "waters lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1016F#4P(Someone hasn't changed a bit...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Hmm?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)

    ChrTalk(    #74
        0xFE,
        (
            "Oh, I was wondering who it was!\x01",
            "Hello, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1000F#4PHi, Lloyd. I haven't seen you in forever.\x02\x03",

            "Looking to challenge the lord-king-mugwump-fish\x01",
            "of Valleria Lake again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "For now, no. I'm off to Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I've heard there's a nice, convenient\x01",
            "spot right in the city limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1016F#4PWow, you sure are dedicated!\x02\x03",

            "It sounds fun, but I guess I'm just\x01",
            "not that into fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "That's a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "You've got quite a talent for it,\x01",
            "from what I saw at the Kingfisher Inn...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0xFE,
        "I know! Let me give you this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1000F#4PHuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #84
        "\x07\x00Received #526i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x07\x00Received #591i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20E, 1)
    OP_3E(0x24F, 1)

    ChrTalk(    #86
        0x101,
        "#1015F#4PThis is, uh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "It's a rod for beginners and a notebook\x01",
            "for recording your fishing records.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "We, the members of the Fisherman's Guild,\x01",
            "are dedicated to the expansion of the\x01",
            "culture of fishing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "We're always happy to provide promising\x01",
            "rookies with the tools of the trade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "Incidentally...are you bound for Ruan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1000F#4PYeah, I am, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Oh, well, then. You'll have a chance to\x01",
            "swing that rod right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "There are all sorts of fishing spots\x01",
            "in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1011F#4PHuh, I guess it would be a good chance.\x02\x03",

            "Now that you mention it, Ruan as a region\x01",
            "IS kind of full of waterside areas!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "As I mentioned, there's a point within the\x01",
            "city itself, too. You should go there first to\x01",
            "practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "For now, so long as you enjoy it,\x01",
            "that's enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1001F#4PYeah, thanks.\x01",
            "I'll definitely give it a shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "I pray that you'll join our ranks someday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "Well, then! Safe journey to you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 45, 400)
    EventEnd(0x0)

    label("loc_2374")

    TalkEnd(0xFE)
    Return()

    # Function_13_1AB5 end

    def Function_14_2378(): pass

    label("Function_14_2378")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 0)), scpexpr(EXPR_END)), "loc_2423")

    ChrTalk(    #100
        0xFE,
        (
            "Bracers like yourself always seem so busy,\x01",
            "miss. It must be so rough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Still, it's because of your efforts that\x01",
            "our lives are peaceful. Thank you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283E")

    label("loc_2423")

    OP_A2(0x1208)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4A(0xFE, 255)

    ChrTalk(    #102
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #103
        0xFE,
        (
            "Umm, excuse me, are you from the\x01",
            "Bracer Guild, miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1000FI am, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "I thought so!\x01",
            "I'm glad we could meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Do you remember me?\x01",
            "I was one of the people you saved when\x01",
            "the sky bandits held us hostage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1004FOh! You were with the captain, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "That's right. I'm Clare.\x01",
            "I manage the passenger cabin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Our entire crew owes you our lives\x01",
            "and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "We're still here at our posts because\x01",
            "you managed to save us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1008FHeehee, you're welcome!\x02\x03",

            "#1000FIs the entire crew of the Linde\x01",
            "back at work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Yes, everyone is working even\x01",
            "harder than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1006FThat's great!\x02\x03",

            "I'm glad everyone was able to get\x01",
            "back to their lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Forgive me for asking, Miss Bracer,\x01",
            "but are you traveling for pleasure\x01",
            "today? Or...work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1016FHaha, unfortunately it's always work.\x02\x03",

            "I'll probably end up riding airships a\x01",
            "lot from now on.\x02\x03",

            "I hope you'll treat me well if I end\x01",
            "up on the Linde again. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Absolutely! I hope we get to\x01",
            "serve you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)

    label("loc_283E")

    TalkEnd(0xFE)
    Return()

    # Function_14_2378 end

    def Function_15_2842(): pass

    label("Function_15_2842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28C8")

    ChrTalk(    #117
        0xFE,
        (
            "Confirming throttle at 60%.\x01",
            "Orbal driver set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Okay! We should make touchdown\x01",
            "at Ruan on schedule at this rate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293B")

    label("loc_28C8")

    OP_A2(0x2)

    ChrTalk(    #119
        0xFE,
        (
            "Altitude okay.\x01",
            "Setting throttle at 60%.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Maintaining current heading until\x01",
            "we cross the Roubine River.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293B")

    TalkEnd(0xFE)
    Return()

    # Function_15_2842 end

    def Function_16_293F(): pass

    label("Function_16_293F")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0xFE,
        (
            "When I was young, the only way to get around\x01",
            "was a long, hard trip on the roads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "We really have it easy these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "And it's all thanks to Her Majesty!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_16_293F end

    def Function_17_29F2(): pass

    label("Function_17_29F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2A7E")

    ChrTalk(    #124
        0xFE,
        (
            "So...a choice between a man representing\x01",
            "the harbor or a businessman promoting\x01",
            "tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "I wonder which one will win?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2B")

    label("loc_2A7E")

    OP_A2(0x9)

    ChrTalk(    #126
        0xFE,
        (
            "Ruan is in the middle of an election\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "The candidates, I believe, are the harbor\x01",
            "manager and the owner of a local hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "I wonder which will win?\x02",
    )

    CloseMessageWindow()

    label("loc_2B2B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_17_29F2 end

    def Function_18_2B34(): pass

    label("Function_18_2B34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2B86")

    ChrTalk(    #129
        0xFE,
        (
            "Even to an outsider, the whole Mayor\x01",
            "Dalmore thing is shocking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C61")

    label("loc_2B86")

    OP_A2(0xA)

    ChrTalk(    #130
        0xFE,
        "So next up is Ruan, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Speaking of Ruan, that whole thing with\x01",
            "Mayor Dalmore being arrested was a\x01",
            "real shocker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Seems like the whole town's still in\x01",
            "an uproar over it, but that's not too\x01",
            "surprising.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C61")

    TalkEnd(0xFE)
    Return()

    # Function_18_2B34 end

    def Function_19_2C65(): pass

    label("Function_19_2C65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2D16")

    ChrTalk(    #133
        0xFE,
        (
            "I'm not worried about the sky bandits.\x01",
            "They don't even have a ship anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "What're they gonna do? Flap their arms\x01",
            "real hard and run us down with wishes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2D16")

    OP_A2(0xB)

    ChrTalk(    #135
        0xFE,
        (
            "Oh, really, Grandpa is such a worrywart!\x01",
            "I dunno what to do with him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Sure there WERE bandits, but according\x01",
            "to the news, they don't even have a ship\x01",
            "anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "What're they gonna do? Flap their arms\x01",
            "real hard and run us down with wishes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E15")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_19_2C65 end

    def Function_20_2E1E(): pass

    label("Function_20_2E1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2E94")

    ChrTalk(    #138
        0xFE,
        (
            "It seems likely the sky bandits've fled\x01",
            "the country, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "...Even so, I'm a wee bit worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F11")

    label("loc_2E94")

    OP_A2(0xC)

    ChrTalk(    #140
        0xFE,
        (
            "Come to think of it, that group of\x01",
            "bandits still hasn't been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "No... They wouldn't attack us, would they?\x02",
    )

    CloseMessageWindow()

    label("loc_2F11")

    TalkEnd(0xFE)
    Return()

    # Function_20_2E1E end

    def Function_21_2F15(): pass

    label("Function_21_2F15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2FBD")

    ChrTalk(    #142
        0xFE,
        (
            "Airships are still very rare vehicles\x01",
            "outside of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "It was kind of a shock when I found out\x01",
            "normal citizens use them so casually\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308B")

    label("loc_2FBD")

    OP_A2(0xD)

    ChrTalk(    #144
        0xFE,
        (
            "Incredible...\x01",
            "Liberl never ceases to amaze me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Back home, in Calvard, airships are still\x01",
            "very rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "It was kind of a shock when I found out\x01",
            "normal citizens use them so casually\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_21_2F15 end

    def Function_22_3094(): pass

    label("Function_22_3094")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30C4")
    SetChrSubChip(0xFE, 2)
    Jump("loc_30EA")

    label("loc_30C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30E5")
    SetChrSubChip(0xFE, 1)
    Jump("loc_30EA")

    label("loc_30E5")

    SetChrSubChip(0xFE, 0)

    label("loc_30EA")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 5)), scpexpr(EXPR_END)), "loc_31A7")

    ChrTalk(    #147
        0xFE,
        (
            "#020FYou're welcome to walk around, Estelle,\x01",
            "but don't forget to get off at Ruan!\x02\x03",

            "There'll be a broadcast before we land,\x01",
            "so make sure to get back to your seat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3314")

    label("loc_31A7")

    OP_A2(0x120D)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #148
        0xFE,
        (
            "#020FEstelle! All done with your walk?\x02\x03",

            "We still have a bit of time before\x01",
            "we land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1015FHmm... Okay.\x02\x03",

            "#1011FI'm gonna walk around a bit more,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "#020FYou're welcome to walk around, Estelle,\x01",
            "but don't forget to get off at Ruan!\x02\x03",

            "There'll be a broadcast before we land,\x01",
            "so make sure to get back to your seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1006FYeah, I will.\x02",
    )

    CloseMessageWindow()

    label("loc_3314")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_22_3094 end

    def Function_23_331D(): pass

    label("Function_23_331D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 5)), scpexpr(EXPR_END)), "loc_339C")
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #152
        0xFE,
        "#053F...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)

    ChrTalk(    #153
        0x101,
        (
            "#1015F(I guess I've gotta respect being\x01",
            "able to sleep like this.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_3426")

    label("loc_339C")

    OP_A2(0x120D)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #154
        0xFE,
        "#053F...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #155
        0x101,
        "#1019F(He's...already completely passed out.)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_3426")

    Return()

    # Function_23_331D end

    def Function_24_3427(): pass

    label("Function_24_3427")

    EventBegin(0x0)
    OP_0D()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #156
        "\x07\x05Thank you for flying with us today.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #157
        "\x07\x05We will be arriving in Ruan shortly.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #158
        (
            "\x07\x05Please be aware that there may be turbulence\x01",
            "while landing, so we ask that all passengers\x01",
            "take their seats.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #159
        0x101,
        "#1004FWhoops, I'd better get to my seat!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3427 end

    SaveToFile()

Try(main)
