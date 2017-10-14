from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5900   ._SN',
        MapName             = 'Other',
        Location            = 'C5900.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Scherazard',                           # 9
        'Olivier',                              # 10
        'Kloe',                                 # 11
        'Agate',                                # 12
        'Tita',                                 # 13
        'Zin',                                  # 14
        'Father Kevin',                         # 15
        'Professor Russell',                    # 16
        'Nial',                                 # 17
        'Dorothy',                              # 18
        'Major Vander',                         # 19
        'Captain Schwarz',                      # 20
        'Sieg',                                 # 21
        'Helmsman Lux',                         # 22
        'Faye',                                 # 23
        'Josette',                              # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Clive',                                # 29
        'Park Block - Calmare',                 # 30
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT27/CH03210 ._CH',             # 02
        'ED6_DT07/CH00050 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT27/CH03080 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT06/CH20063 ._CH',             # 09
        'ED6_DT27/CH03570 ._CH',             # 0A
        'ED6_DT27/CH03580 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
        'ED6_DT27/CH03860 ._CH',             # 0D
        'ED6_DT06/CH20064 ._CH',             # 0E
        'ED6_DT07/CH00310 ._CH',             # 0F
        'ED6_DT27/CH04107 ._CH',             # 10
        'ED6_DT07/CH01550 ._CH',             # 11
        'ED6_DT27/CH03100 ._CH',             # 12
        'ED6_DT07/CH01320 ._CH',             # 13
        'ED6_DT07/CH01450 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT27/CH03210P._CP',             # 02
        'ED6_DT07/CH00050P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT27/CH03080P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT06/CH20063P._CP',             # 09
        'ED6_DT27/CH03570P._CP',             # 0A
        'ED6_DT27/CH03580P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
        'ED6_DT27/CH03860P._CP',             # 0D
        'ED6_DT06/CH20064P._CP',             # 0E
        'ED6_DT07/CH00310P._CP',             # 0F
        'ED6_DT27/CH04107P._CP',             # 10
        'ED6_DT07/CH01550P._CP',             # 11
        'ED6_DT27/CH03100P._CP',             # 12
        'ED6_DT07/CH01320P._CP',             # 13
        'ED6_DT07/CH01450P._CP',             # 14
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13600,
        Z                   = 0,
        Y                   = 37280,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -21910,
        Z                   = 3500,
        Y                   = 23300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -20140,
        Z                   = 3500,
        Y                   = 22380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2830,
        Z                   = 0,
        Y                   = 28680,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -24350,
        Z                   = 0,
        Y                   = 18840,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -21600,
        Z                   = 0,
        Y                   = 15040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -24920,
        Z                   = 0,
        Y                   = 16710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -13210,
        Z                   = -3390,
        Y                   = 27060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -10,
        Z                   = 0,
        Y                   = -43810,
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
        X                   = -16900,
        Y                   = -3300,
        Z                   = 24600,
        Range               = -15900,
        Unknown_10          = 0xFFFFFAEC,
        Unknown_14          = 0x67E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -24500,
        Y                   = 3200,
        Z                   = 26800,
        Range               = -23500,
        Unknown_10          = 0x1450,
        Unknown_14          = 0x7080,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -2800,
        Y                   = 0,
        Z                   = -34600,
        Range               = 2700,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFF7CC0,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_7D4",          # 01, 1
        "Function_2_8C4",          # 02, 2
        "Function_3_FCC",          # 03, 3
        "Function_4_184C",         # 04, 4
        "Function_5_1EBA",         # 05, 5
        "Function_6_271D",         # 06, 6
        "Function_7_2CD6",         # 07, 7
        "Function_8_35A1",         # 08, 8
        "Function_9_3FFF",         # 09, 9
        "Function_10_4EAC",        # 0A, 10
        "Function_11_5656",        # 0B, 11
        "Function_12_565A",        # 0C, 12
        "Function_13_5AED",        # 0D, 13
        "Function_14_5D5E",        # 0E, 14
        "Function_15_6085",        # 0F, 15
        "Function_16_6346",        # 10, 16
        "Function_17_6BDE",        # 11, 17
        "Function_18_73CE",        # 12, 18
        "Function_19_7627",        # 13, 19
        "Function_20_80E0",        # 14, 20
        "Function_21_8103",        # 15, 21
        "Function_22_8126",        # 16, 22
        "Function_23_8149",        # 17, 23
        "Function_24_816C",        # 18, 24
        "Function_25_818F",        # 19, 25
        "Function_26_81B2",        # 1A, 26
        "Function_27_81D5",        # 1B, 27
        "Function_28_81F8",        # 1C, 28
        "Function_29_8216",        # 1D, 29
        "Function_30_821C",        # 1E, 30
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_7C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -38250, 4500, 28710, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -45190, 5000, 33140, 45)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E9")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17120, 3500, 23510, 135)

    label("loc_4E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20610, 0, 16960, 315)

    label("loc_50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -23120, 0, 16149, 0)

    label("loc_52F")

    Jump("loc_7C0")

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -43870, 5000, 31520, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -39890, 4500, 33700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_573")
    SetChrFlags(0x11, 0x10)

    label("loc_573")

    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -18420, 3500, 22380, 227)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1440, -4000, 23570, 45)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 33290, -4000, 16740, 225)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -11560, 0, 34340, 262)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 4340, -4000, 19880, 315)
    OP_43(0x12, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4310, -4000, 22130, 315)

    label("loc_615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_627")
    ClearChrFlags(0x17, 0x80)

    label("loc_627")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5070, -3880, 23930, 270)

    label("loc_64A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_66D")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_66D")

    Jump("loc_7C0")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_736")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -18600, 3500, 25160, 35)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 10, -4000, 24410, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 14280, 0, 25700, 135)
    OP_43(0x12, 0x0, 0x6, 0x2)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -16370, 3500, 27040, 170)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 14760, -4000, 19280, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_710")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34850, -4000, 16079, 225)

    label("loc_710")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_733")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_733")

    Jump("loc_7C0")

    label("loc_736")

    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -22940, 0, 39040, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_792")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_792")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -18510, 3500, 22430, 180)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_792")
    SetChrFlags(0x8, 0x10)

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C0")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -43550, 5000, 31240, 225)

    label("loc_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_7D3")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 19)

    label("loc_7D3")

    Return()

    # Function_0_472 end

    def Function_1_7D4(): pass

    label("Function_1_7D4")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE3EC8, 0x230079)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C3, 0x1, 0x50)
    OP_22(0x1C7, 0x1, 0x64)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_837")
    OP_71(0x4, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0x6, 0x4)
    OP_72(0x12, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    Jump("loc_873")

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_855")
    OP_71(0x4, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0x6, 0x4)
    OP_72(0x12, 0x4)
    Jump("loc_873")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_86E")
    OP_71(0x4, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_873")

    label("loc_86E")

    OP_71(0x12, 0x4)

    label("loc_873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    OP_D2(0x600FC, 0x60101, 0x15)
    Jump("loc_8C3")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A4")
    OP_D2(0x600FC, 0x60101, 0x15)
    Jump("loc_8C3")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B9")
    OP_D2(0x600FC, 0x60101, 0x15)
    Jump("loc_8C3")

    label("loc_8B9")

    OP_D2(0x600FC, 0x60101, 0x15)

    label("loc_8C3")

    Return()

    # Function_1_7D4 end

    def Function_2_8C4(): pass

    label("Function_2_8C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_DC5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x10B, 0)
    Sleep(1000)

    ChrTalk(    #0
        0x10,
        (
            "#143FWhoa, hang on, ain't you one of\x01",
            "the sky bandits...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        (
            "#210FHeheh, darn right!\x01",
            "I'm Josette of the Capua family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#141FYeah, I thought so!\x02\x03",

            "Hey, if you got a minute, I'd love\x01",
            "to ask you a few things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10B,
        (
            "#212FSorry, but I'm about as interested in\x01",
            "helping the Liberl News as I am about\x01",
            "sticking my head in a toilet.\x02\x03",

            "I'm amazed you can even ask that with a\x01",
            "straight face after the things you've\x01",
            "written about us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#147FHeeeeey, it's all water under the bridge,\x01",
            "right?\x02\x03",

            "C'mon, I can give you a chance to tell\x01",
            "your side of the story. Whaddya say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10B,
        "#214FI say: bleeeeeeeah!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x2299)
    Jump("loc_C30")

    label("loc_B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_BCE")
    TurnDirection(0x10, 0x10B, 0)

    ChrTalk(    #6
        0x10,
        (
            "#147FAww, c'mon, give us a shot.\x02\x03",

            "We won't do bad by you this time.\x01",
            "Reporter's honor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C30")

    label("loc_BCE")

    TurnDirection(0x10, 0x10B, 0)

    ChrTalk(    #7
        0x10,
        (
            "#147FAww, c'mon, give us a shot.\x02\x03",

            "We won't do bad by you this time.\x01",
            "Reporter's honor!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C30")

    Jump("loc_DC2")

    label("loc_C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4C")

    ChrTalk(    #8
        0x10,
        (
            "#140FWasn't expecting to see the Capuas\x01",
            "way up here.\x02\x03",

            "I would love to snag a photo of\x01",
            "that ship of theirs...\x02\x03",

            "But my finely-honed reporter instincts\x01",
            "are tellin' me to not be an idiot and\x01",
            "wander too far.\x02\x03",

            "Well, guess I'll wait and see if\x01",
            "an opportunity comes up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_DC2")

    label("loc_D4C")


    ChrTalk(    #9
        0x10,
        (
            "#142FWasn't expecting to see the Capuas\x01",
            "way up here.\x02\x03",

            "They're practically like weeds,\x01",
            "just can't get rid of 'em.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC2")

    Jump("loc_FC8")

    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(    #10
        0x10,
        (
            "#143FNow that I've had a chance to actually\x01",
            "look around, this place is blowin' my\x01",
            "Goddamned mind.\x02\x03",

            "May be a bit late, but this is makin' me\x01",
            "remember all those old stories about the\x01",
            "Sept-Terrion Seven Treasures things.\x02\x03",

            "#145FGreat sources of power bestowed on man\x01",
            "by Aidios Herself, huh? Standin' here\x01",
            "makes you think it ain't all a fairy tale.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_FC8")

    label("loc_F37")


    ChrTalk(    #11
        0x10,
        (
            "#145FSorry, could you leave me alone for a bit?\x02\x03",

            "I'm still feelin' a little shaky thanks to,\x01",
            "y'know, common sense blowing up under my feet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC8")

    TalkEnd(0xFE)
    Return()

    # Function_2_8C4 end

    def Function_3_FCC(): pass

    label("Function_3_FCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_16AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1471")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-38760, 4500, 32630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -37750, 4500, 32580, 298)
    SetChrPos(0x102, -39650, 4500, 31210, 360)
    SetChrPos(0x10B, -38490, 4500, 31610, 317)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1084")
    SetChrPos(0xF9, -37690, 4500, 30730, 307)
    Jump("loc_1095")

    label("loc_1084")

    SetChrPos(0xF8, -37690, 4500, 30730, 307)

    label("loc_1095")

    OP_0D()
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x10B, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #12
        0x11,
        (
            "#151FWooow! What cute goggles!\x02\x03",

            "Umm, excuse me!\x01",
            "Could you pose for a second?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1111():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1111)

    def lambda_111F():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111F)

    ChrTalk(    #13
        0x10B,
        "#213FWhaaaaa??? Pose?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 14)

    ChrTalk(    #14
        0x11,
        (
            "#153FAww, come on, hurry!\x01",
            "Or I'll take the photo anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10B,
        "#216FUhhhh...\x02",
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x10B, 15)
    OP_0D()

    ChrTalk(    #16
        0x10B,
        (
            "#214F...L-Like...THIS, right?\x01",
            "All ROUGH and TOUGH?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "#151FOoooh! Nice!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(    #18
        0x11,
        (
            "#151FOkay, one more!\x01",
            "Give me something cute this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10B,
        "#413FUmmm... How about this...?\x02",
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x10B, 16)
    OP_0D()

    ChrTalk(    #20
        0x11,
        "#151FOoooooooo! Very nice!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x11, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x11,
        (
            "#151FOkaaaay, all done!\x01",
            "Thanks for helping!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Fade(400)
    SetChrChipByIndex(0x10B, 65535)
    OP_0D()
    OP_6D(-38090, 4500, 31080, 1000)

    ChrTalk(    #22
        0x10B,
        (
            "#213F...\x02\x03",

            "#215F...What the heck did I just experience?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040FAh, call it a photographer's way of\x01",
            "saying hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1016FShe's, uh, kinda gotten better at shoving\x01",
            "people into it as time's gone on, though.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x5)
    OP_A2(0x229A)
    Jump("loc_153A")

    label("loc_1471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_14C7")

    ChrTalk(    #25
        0x11,
        (
            "#150FHeehee, I got some great photos\x01",
            "out of that!\x02\x03",

            "Thanks for helping!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153A")

    label("loc_14C7")


    ChrTalk(    #26
        0x11,
        (
            "#151FThe sky's so close, looking at\x01",
            "it from here.\x02\x03",

            "I kinda feel like it's gonna suck me\x01",
            "up and carry me away!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153A")

    Jump("loc_16AC")

    label("loc_153D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1639")

    ChrTalk(    #27
        0x11,
        (
            "#151FThe sky's so close, looking at\x01",
            "it from here.\x02\x03",

            "I kinda feel like it's gonna suck me\x01",
            "up and carry me away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1019F...PLEASE don't fall off the edge, Dorothy.\x01",
            "I don't think my heart can take any more\x01",
            "random tragedy, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_16AC")

    label("loc_1639")


    ChrTalk(    #29
        0x11,
        (
            "#151FThe sky's so close, looking at\x01",
            "it from here.\x02\x03",

            "I kinda feel like it's gonna suck me\x01",
            "up and carry me away!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AC")

    Jump("loc_1848")

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1848")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A9")

    ChrTalk(    #30
        0x11,
        (
            "#151FWow, it's so PRETTY here!\x02\x03",

            "The air's clean and fresh, too!\x01",
            "I'd loooove to live here!\x02\x03",

            "#154FAww, but wait, there's no factory nearby,\x01",
            "huh. So I couldn't get any more photo-quartz.\x02\x03",

            "Awwww, that really would be a problem!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1848")

    label("loc_17A9")


    ChrTalk(    #31
        0x11,
        (
            "#150FThe landscape around here's SO pretty!\x01",
            "I'd love to try living here!\x02\x03",

            "Maybe if I convince all the editors and\x01",
            "factory people to move here with me...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1848")

    TalkEnd(0xFE)
    Return()

    # Function_3_FCC end

    def Function_4_184C(): pass

    label("Function_4_184C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1859")
    Jump("loc_1EB6")

    label("loc_1859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1B2A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1956")

    ChrTalk(    #32
        0xFE,
        "Oh! Your Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "We're currently tuning the Flight Field.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It's difficult work, but it's the final obstacle\x01",
            "to getting the ship fully repaired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "We're only one push away from\x01",
            "being back in action again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EF")

    label("loc_1956")


    ChrTalk(    #36
        0xFE,
        (
            "Tuning the flight engine is hard work,\x01",
            "but it's the final obstacle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "If this goes well, we'll be all but a\x01",
            "push away from being back in action!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EF")

    Jump("loc_1B27")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB3")

    ChrTalk(    #38
        0xFE,
        "Right now we're tuning the flight engine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Airships change direction by angling\x01",
            "their thrust, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "So tuning the engine is essentially\x01",
            "like tuning the controls.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1B27")

    label("loc_1AB3")


    ChrTalk(    #41
        0xFE,
        (
            "Airships change direction by angling\x01",
            "their thrust, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "So how the engine is tuned is very important.\x02",
    )

    CloseMessageWindow()

    label("loc_1B27")

    Jump("loc_1EB6")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_1EAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C98")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #43
        0xFE,
        (
            "Hey, I thought I saw a new face\x01",
            "in your group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "So you're the girl from the bandit group.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Have to admit, I never thought we'd\x01",
            "be working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "You'll forgive me if I'm a little cautious,\x01",
            "but at the same time we could sure use\x01",
            "the help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Frankly, we're so busy, I'd put Antoine\x01",
            "to work if I could.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)
    OP_A2(0x22D0)
    Jump("loc_1EAC")

    label("loc_1C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D78")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #48
        0xFE,
        (
            "You'll forgive me if I'm a little cautious\x01",
            "about you working with us...\x02",
        )
    )


    ChrTalk(    #49
        0xFE,
        (
            "But at the same time, we could sure\x01",
            "use the help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Frankly, we're so busy, I'd put Antoine\x01",
            "to work if I could.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1D78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E31")

    ChrTalk(    #51
        0xFE,
        (
            "The biggest problem's going to be replacing\x01",
            "or reattaching the outrigger we lost when\x01",
            "we crashed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "We need to put our heads together and\x01",
            "figure something out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1E31")


    ChrTalk(    #53
        0xFE,
        (
            "Repairing the outrigger is going to\x01",
            "be a real job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "We need to put our heads together and\x01",
            "figure something out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAC")

    Jump("loc_1EB6")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1EB6")

    label("loc_1EB6")

    TalkEnd(0xFE)
    Return()

    # Function_4_184C end

    def Function_5_1EBA(): pass

    label("Function_5_1EBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21AF")
    TurnDirection(0x16, 0x101, 0)

    ChrTalk(    #55
        0xFE,
        "Looks like we meet again!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F76")

    ChrTalk(    #56
        0x101,
        "#1004FOh, Faye!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        (
            "#064FYou stayed on the Arseille when\x01",
            "it left for the island?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAA")

    label("loc_1F76")


    ChrTalk(    #58
        0x101,
        (
            "#1004FOh, Faye!\x02\x03",

            "You stayed with the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAA")


    ChrTalk(    #59
        0xFE,
        (
            "Yeah, I figured if the professor was\x01",
            "coming, I ought to as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I talked it over with the engineers\x01",
            "and we all decided to stay aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Kinda glad we decided to at this point,\x01",
            "lemme tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1018FNo kidding, that's great!\x02\x03",

            "We really need some help in fixing\x01",
            "up the Arseille, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1040FYes, thank you. Having professional engineers\x01",
            "here will make things much easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Haha, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "We'll do our best to live up to your expectations!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1001FThanks!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x229B)
    Jump("loc_2719")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2224")

    ChrTalk(    #67
        0xFE,
        (
            "Looks like staying on the ship was\x01",
            "the right choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "I'll do my best to get everything fixed up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_2224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_23EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2361")

    ChrTalk(    #69
        0xFE,
        (
            "Phew! That's all the scrap collected.\x01",
            "All the useful stuff, at any rate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "We've got the gangway set up, too,\x01",
            "so I'd better get back to the ship and\x01",
            "start helping with the repairs proper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I'm sure everyone else is already busy\x01",
            "hammering together new parts and tuning\x01",
            "the orbments.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_23E9")

    label("loc_2361")


    ChrTalk(    #72
        0xFE,
        (
            "That's the scrap collected and the gangway\x01",
            "set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I'd better get back to the ship and start\x01",
            "helping with the repairs proper.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E9")

    Jump("loc_2719")

    label("loc_23EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_264C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_252F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CF")

    ChrTalk(    #74
        0xFE,
        "Gotta say, that new girl's good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "She's familiar with the tools and has\x01",
            "a pretty good understanding of airship\x01",
            "maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "You brought us someone useful at just\x01",
            "the right time!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_252C")

    label("loc_24CF")


    ChrTalk(    #77
        0xFE,
        "That new girl's pretty good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "You brought us someone useful at just\x01",
            "the right time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252C")

    Jump("loc_2649")

    label("loc_252F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25ED")

    ChrTalk(    #79
        0xFE,
        "We've got the gangway all set up now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "The idea is, we'll place it like this\x01",
            "wherever it's needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "We'll probably set up one more for\x01",
            "getting down below, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2649")

    label("loc_25ED")


    ChrTalk(    #82
        0xFE,
        (
            "We just finished setting up the gangway.\x01",
            "We'll be putting it wherever we need it\x01",
            "most.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2649")

    Jump("loc_2719")

    label("loc_264C")


    ChrTalk(    #83
        0xFE,
        (
            "Once we've got the scraps below cleaned\x01",
            "up, we'll be putting a bridge here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "After all, it's easier to get in and out\x01",
            "from the deck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Be easier for you guys when you go\x01",
            "exploring, too, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2719")

    TalkEnd(0xFE)
    Return()

    # Function_5_1EBA end

    def Function_6_271D(): pass

    label("Function_6_271D")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2783"),
        (1, "loc_2CC8"),
        (2, "loc_2CCF"),
        (SWITCH_DEFAULT, "loc_2CD2"),
    )


    label("loc_2783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2806")

    ChrTalk(    #86
        0x17,
        (
            "#214FWhat're we hangin' around for?!\x01",
            "Let's go to that ship of the society's!\x02\x03",

            "My brothers HAVE to be there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC5")

    label("loc_2806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 0)), scpexpr(EXPR_END)), "loc_29BD")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #87
        0x17,
        (
            "#210FHi, Joshua...!\x02\x03",

            "#213F...What's wrong?\x01",
            "You look like you want to say something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        "#1042FYes, we came to tell you--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x17,
        "#213FWait... Did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1015FYeah, so...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #91
        (
            "\x07\x05Estelle and Joshua told Josette about how they found the\x01",
            "Glorious in the Factoria District.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x17,
        (
            "#214FFor real?!\x02\x03",

            "L-Let's go right now, then!\x01",
            "Kyle and Don HAVE to be there!!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22D5)
    Jump("loc_2CC5")

    label("loc_29BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C02")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #93
        0x17,
        "#415FHi, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        "#1040FAlready helping out, Josette?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x17,
        (
            "#210FY-Yeah, of course I am!\x02\x03",

            "I told you I'd pitch in around here,\x01",
            "didn't I?\x02\x03",

            "Besides, I have a lot of experience with\x01",
            "this sort of thing, thanks to the Bobcat.\x02\x03",

            "I know I'd be a lot more useful than a\x01",
            "certain SOMEONE around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1019F(Grrrrrr... Hate to admit it, but she's right.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#1049FAh... Thank you, Josette.\x01",
            "I'm sure you'll be a big help.\x02\x03",

            "And once we find Kyle and Don,\x01",
            "we'll come back and let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x17,
        (
            "#210FI'll be waiting!\x02\x03",

            "Anyway, be careful, Joshua...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22C7)
    Jump("loc_2CC5")

    label("loc_2C02")


    ChrTalk(    #99
        0x17,
        (
            "#210FI'll help out around here until you\x01",
            "find my brothers.\x02\x03",

            "Thanks to the Bobcat, I've got a lot\x01",
            "of experience working on ships.\x02\x03",

            "I'll be a lot more helpful than a certain\x01",
            "someone would be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC5")

    Jump("loc_2CD2")

    label("loc_2CC8")

    Call(0, 18)
    Jump("loc_2CD2")

    label("loc_2CCF")

    Jump("loc_2CD2")

    label("loc_2CD2")

    TalkEnd(0xFE)
    Return()

    # Function_6_271D end

    def Function_7_2CD6(): pass

    label("Function_7_2CD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D3C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2D3C")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D51"),
        (1, "loc_3558"),
        (2, "loc_359A"),
        (SWITCH_DEFAULT, "loc_359D"),
    )


    label("loc_2D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3364")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30B0")
    TurnDirection(0x9, 0x10B, 0)

    ChrTalk(    #100
        0x9,
        (
            "#035FAh! I believe this is the first time we've met\x01",
            "since our scrap in the Grand Arena in Grancel.\x02\x03",

            "In fact, I do believe we have traded\x01",
            "violence, rather than words, before now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10B,
        (
            "#210FNo kidding. I do remember you, though.\x02\x03",

            "Y'know, you aren't much of an Erebonian.\x01",
            "And I do mean that in a bad way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#033FMy, my! Such harsh criticism.\x02\x03",

            "#031FThough I do think I...rather love the\x01",
            "Fatherland in my own way, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10B,
        (
            "#215FIf you feel that way, then why don't you head\x01",
            "back to the Empire and do something useful?\x02\x03",

            "Hanging around a pissy little backwater\x01",
            "like this... Hmph. Some 'lover of the\x01",
            "Fatherland' you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "#035FHeh... Well, the time for that is\x01",
            "not far off, truth be told.\x02\x03",

            "#030FRegardless. I do look forward to working\x01",
            "with you.\x02\x03",

            "It shall be good to have another user\x01",
            "of firearms in our merry band.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x229D)
    Jump("loc_3361")

    label("loc_30B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3143")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #105
        0x9,
        (
            "#030FI do look forward to working with you.\x02\x03",

            "It shall be good to have another user\x01",
            "of firearms in our merry band.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3361")

    label("loc_3143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B8")

    ChrTalk(    #106
        0x9,
        (
            "#035FApparently we're all going to carry this\x01",
            "massive piece of scrap.\x02\x03",

            "I'm not sure why, but even my presence\x01",
            "has been requested.\x02\x03",

            "#037FAnd this is apropos of nothing, but do you\x01",
            "need my help with your explorations?\x02\x03",

            "If you do, then Olivier Lenheim is yours!\x01",
            "You need merely say the word.\x02\x03",

            "#034FPlease, say the word!\x01",
            "Take me away from here! Pleeeeeaase!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_3361")

    label("loc_32B8")


    ChrTalk(    #107
        0x9,
        (
            "#037FIf you need my help, then Olivier Lenheim\x01",
            "shall give it to you! You need merely say\x01",
            "the word.\x02\x03",

            "#034FPlease, say the word!\x01",
            "Take me away from here! Pleeeeeaase!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3361")

    Jump("loc_3555")

    label("loc_3364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3555")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AA")

    ChrTalk(    #108
        0x9,
        (
            "#034FThe parts of our noble vessel have\x01",
            "certainly...distributed themselves!\x02\x03",

            "Collecting them by hand, as we must,\x01",
            "will be quite the onerous task.\x02\x03",

            "#035FI, of course, shall give my all to help...\x01",
            "as a performer.\x02\x03",

            "Now, to encourage these fine men and women\x01",
            "with sweat on their brow with a lovely tune!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_3555")

    label("loc_34AA")


    ChrTalk(    #109
        0x9,
        (
            "#035FI shall support everyone as they work up\x01",
            "a sweat...from here, with my songs,\x01",
            "as a true bard should.\x02\x03",

            "If you have any need of physical labor,\x01",
            "speak with Mueller.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3555")

    Jump("loc_359D")

    label("loc_3558")


    ChrTalk(    #110
        0x9,
        (
            "#035FAh, you require the power of genius,\x01",
            "then? Come!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_359D")

    label("loc_359A")

    Jump("loc_359D")

    label("loc_359D")

    TalkEnd(0xFE)
    Return()

    # Function_7_2CD6 end

    def Function_8_35A1(): pass

    label("Function_8_35A1")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3607"),
        (1, "loc_3FBD"),
        (2, "loc_3FF8"),
        (SWITCH_DEFAULT, "loc_3FFB"),
    )


    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_END)), "loc_3AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A55")

    ChrTalk(    #111
        0x101,
        "#1011FOh, hi, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "#020FAh! There you all are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        "#1044FWere you expecting us?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #114
        0x8,
        (
            "#026FI had a feeling you'd be back soon.\x02\x03",

            "You all...fought Luci, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#1043FWe did, yes.\x02\x03",

            "#1035FShe left the Ark after our fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1003FShe specifically said that the karma\x01",
            "between you two remains 'uneven'...\x02\x03",

            "...and that you'd meet again.\x01",
            "She left after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#522FDid she...\x02\x03",

            "No, I suppose she won't let the curtain\x01",
            "fall on the two of us that easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#1026FSchera...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #119
        0x8,
        (
            "#524FDon't worry.\x02\x03",

            "As she said, I'm sure we'll meet again.\x02\x03",

            "For now, I'll simply have to believe that\x01",
            "and keep it in my heart.\x02\x03",

            "Besides, I believe we have more important\x01",
            "things to do than stand around and mope,\x01",
            "hmm?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3924")

    ChrTalk(    #120
        0x104,
        "#035FHeh, Schera has a point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39D1")

    label("loc_3924")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_395F")

    ChrTalk(    #121
        0x106,
        "#051FYeah, Scherazard's got a point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39D1")

    label("loc_395F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3993")

    ChrTalk(    #122
        0x108,
        "#070FYes, Schera has a point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39D1")

    label("loc_3993")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39D1")

    ChrTalk(    #123
        0x109,
        "#1060FHeck yeah! We got a lot to do still!\x02",
    )

    CloseMessageWindow()

    label("loc_39D1")


    ChrTalk(    #124
        0x101,
        (
            "#1002FYeah. For now, we just gotta keep\x01",
            "going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#020FIf you need my help, just ask.\x02\x03",

            "Either way, be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22A1)
    Jump("loc_3AD1")

    label("loc_3A55")


    ChrTalk(    #126
        0x8,
        (
            "#020FDon't worry, I can deal with my feelings\x01",
            "about Luciola on my own time.\x02\x03",

            "For now, we need to focus on our mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD1")

    Jump("loc_3FBA")

    label("loc_3AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_END)), "loc_3FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F23")

    ChrTalk(    #127
        0x8,
        "#522F...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B28")

    ChrTalk(    #128
        0x104,
        "#033FSchera...are you well?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    Jump("loc_3BD8")

    label("loc_3B28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B63")

    ChrTalk(    #129
        0x106,
        "#052FScherazard, you all right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    Jump("loc_3BD8")

    label("loc_3B63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA2")

    ChrTalk(    #130
        0x108,
        "#072FScherazard... you look unwell.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    Jump("loc_3BD8")

    label("loc_3BA2")


    ChrTalk(    #131
        0x102,
        "#1044FSchera...are you feeling all right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    label("loc_3BD8")


    ChrTalk(    #132
        0x8,
        (
            "#524FYes, I'm just...lost in thought a bit.\x02\x03",

            "I'm all right. I've got my feelings in\x01",
            "order. Or... Hah, I think I do, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CBF")

    ChrTalk(    #133
        0x104,
        (
            "#033FVery well, but...do not feel the need\x01",
            "to push yourself beyond your limits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5B")

    label("loc_3CBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2E")

    ChrTalk(    #134
        0x106,
        (
            "#552FWell, all right, but make sure you aren't\x01",
            "drivin' yourself too hard on purpose, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5B")

    label("loc_3D2E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DAC")

    ChrTalk(    #135
        0x108,
        (
            "#072FI see. Further introspection would be\x01",
            "no failing, Scherazard. Do not push\x01",
            "yourself too hard or fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5B")

    label("loc_3DAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DFB")

    ChrTalk(    #136
        0x109,
        (
            "#1063FAll right then, just...watch out for yourself,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5B")

    label("loc_3DFB")


    ChrTalk(    #137
        0x102,
        (
            "#1043FAll right, but please, don't feel the\x01",
            "need to push yourself too hard on our\x01",
            "account.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E5B")


    ChrTalk(    #138
        0x8,
        (
            "#025FYes, I know...\x02\x03",

            "*sigh* Men. The kindness only comes out\x01",
            "when we vulnerable waifs are having a\x01",
            "hard time of it.\x02\x03",

            "Most girls would rather you were\x01",
            "like this all the time, you know.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x22A1)
    Jump("loc_3FBA")

    label("loc_3F23")


    ChrTalk(    #139
        0x8,
        (
            "#020FI really am fine, don't worry.\x02\x03",

            "I've put myself in order, and I can\x01",
            "help any time you need.\x02\x03",

            "Just say the word and I'll be there,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBA")

    Jump("loc_3FFB")

    label("loc_3FBD")


    ChrTalk(    #140
        0x8,
        "#020FShall I join the exploration party, then?\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_3FFB")

    label("loc_3FF8")

    Jump("loc_3FFB")

    label("loc_3FFB")

    TalkEnd(0xFE)
    Return()

    # Function_8_35A1 end

    def Function_9_3FFF(): pass

    label("Function_9_3FFF")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4065"),
        (1, "loc_4E76"),
        (2, "loc_4EA5"),
        (SWITCH_DEFAULT, "loc_4EA8"),
    )


    label("loc_4065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_472F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_END)), "loc_4542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445A")

    ChrTalk(    #141
        0x101,
        "#1011FOh, Zin! Here you are.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #142
        0xD,
        (
            "#070FAh, Estelle!\x02\x03",

            "... You look as though you have something\x01",
            "to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1002FYeah... it's about Walter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "#074FSo he did show up.\x02\x03",

            "#070FIf you're here to talk about it,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#1040FYes, we managed to drive him off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1015FWasn't exactly easy, though.\x02\x03",

            "But either way, he's definitely out\x01",
            "of our hair, at least for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        (
            "#074FSo he departed in the end...\x02\x03",

            "I'm guessing he said OUR decisive fight\x01",
            "is still to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x102,
        (
            "#1043FThat's almost exactly what he said, yes.\x02\x03",

            "His exact words were, 'the match is held\x01",
            "up till next time.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        (
            "#074FYes, it is that.\x02\x03",

            "It is regrettable, but...\x01",
            "perhaps this is for the better.\x02\x03",

            "#572FMy business with Walter is something\x01",
            "I should settle on my own...\x02\x03",

            "There's no reason to involve any of\x01",
            "you in what is our dispute alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1026FZin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        (
            "#070FFor now, though, we should be happy\x01",
            "we broke through their defenses!\x02\x03",

            "We're making progress toward our goal,\x01",
            "one battle at a time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_453C")

    label("loc_445A")


    ChrTalk(    #152
        0xD,
        (
            "#070FI have a lot to settle still with Walter,\x01",
            "but maybe this is all for the best.\x02\x03",

            "My business with Walter is something\x01",
            "I should settle on my own...\x02\x03",

            "There's no reason to involve any of\x01",
            "you in what is our dispute alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453C")

    OP_A2(0x22A8)
    Jump("loc_472C")

    label("loc_4542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_472C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4686")

    ChrTalk(    #153
        0xD,
        (
            "#074FWalter was a martial artist blessed with\x01",
            "far more talent than I.\x02\x03",

            "But, in the end, he lost to me, bearer of\x01",
            "the Taito Living Fist.\x02\x03",

            "#072FWhat matters is not disparity in power,\x01",
            "but how power is used.\x02\x03",

            "This whole affair is making me, as a\x01",
            "martial artist, look at how I'm using\x01",
            "my own strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_472C")

    label("loc_4686")


    ChrTalk(    #154
        0xD,
        (
            "#074FWhat matters is not disparity in power,\x01",
            "but how power is used.\x02\x03",

            "This whole affair is making me, as a\x01",
            "martial artist, look at how I'm using\x01",
            "my own strength.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_472C")

    Jump("loc_4E73")

    label("loc_472F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_491B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484A")

    ChrTalk(    #155
        0xD,
        (
            "#070FThat's most of the parts cleaned\x01",
            "up at this point, eh?\x02\x03",

            "Once this is done, I can leave the rest\x01",
            "to the Royal Guard, I think.\x02\x03",

            "It also sounds like we're hitting the\x01",
            "best parts of exploring the city!\x02\x03",

            "It's about time we lived up to our\x01",
            "names as bracers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_4918")

    label("loc_484A")


    ChrTalk(    #156
        0xD,
        (
            "#070FOnce this is done, I can leave the\x01",
            "rest to the Royal Guard, I think.\x02\x03",

            "It also sounds like we're hitting the\x01",
            "best parts of exploring the city!\x02\x03",

            "It's about time we lived up to our\x01",
            "names as bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4918")

    Jump("loc_4E73")

    label("loc_491B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_4CC4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A80")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #157
        0xD,
        (
            "#073FAh, hello, miss.\x01",
            "You're Josette, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10B,
        (
            "#210FYeah! Actually kinda nice to\x01",
            "meet you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "#071FHaha. It's not where either of us expected\x01",
            "to see each other again, I'd bet.\x02\x03",

            "#070FStill! At this point, we're all in the\x01",
            "same boat.\x02\x03",

            "For now, let's help each other as best\x01",
            "we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10B,
        "#210FYou bet!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x17)
    OP_A2(0x22A7)
    Jump("loc_4CC1")

    label("loc_4A80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B11")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #161
        0xD,
        (
            "#070FI really never expected to meet you here,\x01",
            "of all places.\x02\x03",

            "Ha, She Above does seem to enjoy twists\x01",
            "of fate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC1")

    label("loc_4B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C24")

    ChrTalk(    #162
        0xD,
        (
            "#070FWe're going to make a passage here so\x01",
            "we can more easily reach the back of\x01",
            "the ship to repair it.\x02\x03",

            "I think it's a good idea, since having\x01",
            "a way to get to all parts of the ship\x01",
            "easily will help repairs.\x02\x03",

            "I'd better put my back into it and\x01",
            "get to work!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_4CC1")

    label("loc_4C24")


    ChrTalk(    #163
        0xD,
        (
            "#070FWe're going to make a passage here so\x01",
            "we can more easily reach the back of\x01",
            "the ship to repair it.\x02\x03",

            "I'd better put my back into it and\x01",
            "get to work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CC1")

    Jump("loc_4E73")

    label("loc_4CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE0")

    ChrTalk(    #164
        0xD,
        (
            "#070FWe're going to put a bridge to the\x01",
            "deck here.\x02\x03",

            "First, though, we need to clear away\x01",
            "this scrap.\x02\x03",

            "If any of you have a moment to help out,\x01",
            "we could surely use a few more hands.\x02\x03",

            "Doing this on my own is going to be\x01",
            "a bit difficult, even with my training!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_4E73")

    label("loc_4DE0")


    ChrTalk(    #165
        0xD,
        (
            "#070FFirst we need to clear this scrap and\x01",
            "put a bridge here.\x02\x03",

            "If any of you have a moment to help out,\x01",
            "we could surely use a few more hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E73")

    Jump("loc_4EA8")

    label("loc_4E76")


    ChrTalk(    #166
        0xD,
        "#070FTime for me to join the team?\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_4EA8")

    label("loc_4EA5")

    Jump("loc_4EA8")

    label("loc_4EA8")

    TalkEnd(0xFE)
    Return()

    # Function_9_3FFF end

    def Function_10_4EAC(): pass

    label("Function_10_4EAC")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F12"),
        (1, "loc_560E"),
        (2, "loc_564F"),
        (SWITCH_DEFAULT, "loc_5652"),
    )


    label("loc_4F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_5083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF0")

    ChrTalk(    #167
        0xB,
        (
            "#050FWe've made some good progress in\x01",
            "gettin' the scrap picked up.\x02\x03",

            "Once we get that huge piece out of the\x01",
            "way, we can move on to other things.\x02\x03",

            "Well, time to roll up our sleeves and get\x01",
            "to it...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_5080")

    label("loc_4FF0")


    ChrTalk(    #168
        0xB,
        (
            "#050FWe've made some good progress in\x01",
            "gettin' the scrap picked up.\x02\x03",

            "Once that huge piece is outta the way,\x01",
            "we can move on to other things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5080")

    Jump("loc_560B")

    label("loc_5083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_5376")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514B")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #169
        0xB,
        (
            "#051FYo, helpin' with the exploring already,\x01",
            "huh?\x02\x03",

            "Good to see you meant what you\x01",
            "said. You keep it up, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10B,
        "#210FHeheh! Just leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x19)
    OP_A2(0x22A9)
    Jump("loc_5373")

    label("loc_514B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51BB")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #171
        0xB,
        (
            "#051FHelpin' out already, huh?\x01",
            "You really are turnin' a new leaf.\x02\x03",

            "Keep it up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5373")

    label("loc_51BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B9")

    ChrTalk(    #172
        0xB,
        (
            "#552FPutting aside the friggin' propeller\x01",
            "for a sec...\x02\x03",

            "A whole bunch of the parts around here\x01",
            "look like they'll be a pain to collect.\x02\x03",

            "#053FSome of 'em look important, though.\x01",
            "Maybe I should talk to Gramps about\x01",
            "what to do with them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_5373")

    label("loc_52B9")


    ChrTalk(    #173
        0xB,
        (
            "#053FA whole bunch of the parts around here\x01",
            "look like they'll be a pain to collect...\x02\x03",

            "Some of 'em look important, though.\x01",
            "Maybe I should talk to Gramps about\x01",
            "what to do with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5373")

    Jump("loc_560B")

    label("loc_5376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_560B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B3")

    ChrTalk(    #174
        0xB,
        (
            "#552FFriggin'...\x01",
            "Kinda big for a 'piece of scrap.'\x02\x03",

            "Askin' us to move this with our bare hands?\x01",
            "Even slave drivers oughtta have limits.\x02\x03",

            "#053FStill, given the situation, guess I can't\x01",
            "complain too much...\x02\x03",

            "First thing is to grab that idiot who's\x01",
            "wasting his time up on deck...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_5510")

    label("loc_54B3")


    ChrTalk(    #175
        0xB,
        (
            "#552FWell, no point in complaining now.\x02\x03",

            "Time to put my shoulder to it\x01",
            "and get it done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5510")

    Jump("loc_560B")

    label("loc_5513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55AE")

    ChrTalk(    #176
        0xB,
        (
            "#552FFriggin'...\x01",
            "Kinda big for a 'piece of scrap.'\x02\x03",

            "Askin' us to move this with our bare hands?\x01",
            "Even slave drivers oughtta have limits.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_560B")

    label("loc_55AE")


    ChrTalk(    #177
        0xB,
        (
            "#053FWell, no point in complaining now.\x02\x03",

            "Time to put my shoulder to it\x01",
            "and get it done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_560B")

    Jump("loc_5652")

    label("loc_560E")


    ChrTalk(    #178
        0xB,
        (
            "#050FNeed to change team members?\x01",
            "I'm all set to go.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_5652")

    label("loc_564F")

    Jump("loc_5652")

    label("loc_5652")

    TalkEnd(0xFE)
    Return()

    # Function_10_4EAC end

    def Function_11_5656(): pass

    label("Function_11_5656")

    TalkBegin(0xFE)
    Return()

    # Function_11_5656 end

    def Function_12_565A(): pass

    label("Function_12_565A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_586C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56D9")
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #179
        0xFE,
        "Your Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Our squad is currently preparing for the\x01",
            "next operation!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Jump("loc_5869")

    label("loc_56D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D0")

    ChrTalk(    #181
        0xFE,
        (
            "Phew! We're getting the scrap moved,\x01",
            "but only thanks to the help of the bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "Man, though, the bracer dudes have\x01",
            "some serious muscle on their arms!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "We train pretty hard, but they're\x01",
            "just on a whole different level.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_5869")

    label("loc_57D0")


    ChrTalk(    #184
        0xFE,
        "The bracer men have some serious muscle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "We Royal Guards always felt pretty\x01",
            "confident in our strength, but these\x01",
            "guys are a whole other story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5869")

    Jump("loc_5AE9")

    label("loc_586C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595C")

    ChrTalk(    #186
        0xFE,
        "Ack, Your Highness!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #187
        0xFE,
        (
            "A-Allow me to assure you that we'll\x01",
            "have no problems with a little piece\x01",
            "of scrap like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "We'll have it removed immediately,\x01",
            "so please, don't be concerned!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_A2(0x11)
    Jump("loc_5A05")

    label("loc_595C")

    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #189
        0xFE,
        (
            "On the honor and glory of the Royal\x01",
            "Guard, we will remove this scrap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "Your Highness, please, continue your\x01",
            "investigations without concern!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)

    label("loc_5A05")

    Jump("loc_5AE9")

    label("loc_5A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A83")

    ChrTalk(    #191
        0xFE,
        (
            "You're... you're telling me we're moving\x01",
            "this by hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "Am I the only one who thinks this is nuts?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_5AE9")

    label("loc_5A83")


    ChrTalk(    #193
        0xFE,
        (
            "We're going to have to get rid of\x01",
            "this ourselves...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "My arms ache just thinking about it...\x02",
    )

    CloseMessageWindow()

    label("loc_5AE9")

    TalkEnd(0xFE)
    Return()

    # Function_12_565A end

    def Function_13_5AED(): pass

    label("Function_13_5AED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BC4")

    ChrTalk(    #195
        0xFE,
        "Ah, Your Highness!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #196
        0xFE,
        (
            "We're currently constructing a path under\x01",
            "the supervision of the mechanics!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "We will be finished soon!\x01",
            "Please be patient until then!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_A2(0x10)
    Jump("loc_5C66")

    label("loc_5BC4")

    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #198
        0xFE,
        (
            "We're currently constructing a path under\x01",
            "the supervision of the mechanics!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "We will be finished soon!\x01",
            "Please be patient until then!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)

    label("loc_5C66")

    Jump("loc_5D5A")

    label("loc_5C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CED")

    ChrTalk(    #200
        0xFE,
        "So we're going to be building a path here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Once we've got the scrap removed,\x01",
            "we'll be asking Faye for help.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_5D5A")

    label("loc_5CED")


    ChrTalk(    #202
        0xFE,
        "Man, am I glad Faye is with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "She can do everything from welding\x01",
            "to fine-tuning an orbal engine!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5A")

    TalkEnd(0xFE)
    Return()

    # Function_13_5AED end

    def Function_14_5D5E(): pass

    label("Function_14_5D5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_5F28")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DE6")
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #204
        0xFE,
        "Well done with the investigation so far!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "Our repair work is proceeding steadily!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Jump("loc_5F25")

    label("loc_5DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA3")

    ChrTalk(    #206
        0xFE,
        (
            "There's no way I'll be able to\x01",
            "move scrap like this on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "I mean, look at it, it's a solid chunk of metal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "Guess I need to ask the bracers\x01",
            "for help again!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_5F25")

    label("loc_5EA3")


    ChrTalk(    #209
        0xFE,
        (
            "There's no way I'll be able to move\x01",
            "scrap like this on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "Ah well. Guess I need to ask the\x01",
            "bracers for help again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F25")

    Jump("loc_6081")

    label("loc_5F28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FC3")
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #211
        0xFE,
        (
            "Bits of scrap like this are but pieces\x01",
            "of dust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "We'll have them tidied up momentarily.\x01",
            "You need not worry!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Jump("loc_6081")

    label("loc_5FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6049")

    ChrTalk(    #213
        0xFE,
        (
            "W-We're going to be moving THAT now?\x01",
            "By ourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "Uhh, the captain sure has a lot of\x01",
            "faith in us, I guess...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_6081")

    label("loc_6049")


    ChrTalk(    #215
        0xFE,
        (
            "W-We're going to be moving THAT now?\x01",
            "By ourselves?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6081")

    TalkEnd(0xFE)
    Return()

    # Function_14_5D5E end

    def Function_15_6085(): pass

    label("Function_15_6085")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_6185")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6110")

    ChrTalk(    #216
        0xFE,
        (
            "Looks like recovering this outrigger will\x01",
            "be the final step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "I hope we can get this repaired in time...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6182")

    label("loc_6110")


    ChrTalk(    #218
        0xFE,
        (
            "Looks like recovering this outrigger will\x01",
            "be the final step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "I hope we can get this repaired in time...\x02",
    )

    CloseMessageWindow()

    label("loc_6182")

    Jump("loc_6342")

    label("loc_6185")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6248")

    ChrTalk(    #220
        0xFE,
        (
            "Oh, Your Highness.\x01",
            "You intend to depart?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "We should have a bridge in place\x01",
            "by the time you return, my lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "We will do our best to meet your expectations!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    Jump("loc_62BA")

    label("loc_6248")


    ChrTalk(    #223
        0xFE,
        (
            "We should have a bridge in place\x01",
            "by the time you return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "We will do our best to meet your\x01",
            "expectations!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BA")

    Jump("loc_6342")

    label("loc_62BD")


    ChrTalk(    #225
        0xFE,
        (
            "Mmmmmph. Now that I look at it, this thing\x01",
            "really is big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "We're gonna have to put some elbow grease\x01",
            "into moving it at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6342")

    TalkEnd(0xFE)
    Return()

    # Function_15_6085 end

    def Function_16_6346(): pass

    label("Function_16_6346")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6353")
    Jump("loc_6BDA")

    label("loc_6353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_654C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6459")

    ChrTalk(    #227
        0x12,
        (
            "#270FWe probably can't move something this large\x01",
            "without mechanical aid of some sort.\x02\x03",

            "The problem is, just the one outrigger\x01",
            "engine probably won't be enough for\x01",
            "stable flight...\x02\x03",

            "We need to figure out if we can recover\x01",
            "this, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6549")

    label("loc_6459")


    ChrTalk(    #228
        0x12,
        (
            "#270FWe probably can't move something this large\x01",
            "without mechanical aid of some sort.\x02\x03",

            "The problem is, just the one outrigger\x01",
            "engine probably won't be enough for\x01",
            "stable flight...\x02\x03",

            "We need to figure out if we can recover\x01",
            "this, somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6549")

    Jump("loc_6BDA")

    label("loc_654C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_6BD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6723")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #229
        0x12,
        "#270FAh, so you're the little bandit girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10B,
        "#212FThe WHAT?! And what does THAT mean?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x12,
        (
            "#270FI don't see the problem with calling\x01",
            "a little girl a little girl.\x02\x03",

            "Let me make one thing clear: you should take\x01",
            "care not to be disruptive, for your own sake.\x02\x03",

            "Remember that you are only being allowed\x01",
            "to stay here because this is an emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x10B,
        "#214FYeah, I know, all right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x12,
        (
            "#272FGood, then.\x02\x03",

            "I hope you work hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C)
    OP_A2(0x22AC)
    Jump("loc_6BD0")

    label("loc_6723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B4")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #234
        0x12,
        (
            "#270FI hope you work hard.\x02\x03",

            "Remember that you are only being allowed\x01",
            "to stay here because this is an emergency.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD0")

    label("loc_67B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6866")

    ChrTalk(    #235
        0x12,
        (
            "#270FFeel free to ignore Olivier, by the way.\x02\x03",

            "After all, I doubt there will ever be as\x01",
            "good an opportunity to teach him the\x01",
            "value of hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_68AF")

    label("loc_6866")


    ChrTalk(    #236
        0x12,
        (
            "#270FFeel free to ignore him.\x02\x03",

            "Go and continue your investigations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AF")

    Jump("loc_6BD0")

    label("loc_68B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B26")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #237
        0x12,
        (
            "#276FWe're going to be moving this large\x01",
            "piece of scrap.\x02\x03",

            "#270FI have to say, I was rather hoping\x01",
            "you'd be here to help with it. For once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x104,
        (
            "#035FI am never one to shy from the strain\x01",
            "and sweat of labor, but, alas, my talents\x01",
            "are required elsewhere.\x02\x03",

            "I shall have to learn of work's sweetest\x01",
            "fruits some other time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x12,
        (
            "#274FFunny you should praise the value\x01",
            "of hard work only after you've wormed\x01",
            "your way out of it yourself.\x02\x03",

            "Miss Bright, if you change your mind,\x01",
            "remember that you can take him out of\x01",
            "your party at any time.\x02\x03",

            "I'll take responsibility for him and keep\x01",
            "a close eye on him instead.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)
    Jump("loc_6BD0")

    label("loc_6B26")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #240
        0x12,
        (
            "#270FMiss Bright, remember that you can leave\x01",
            "the nitwit here with us at any time.\x02\x03",

            "I think he needs to experience the value\x01",
            "of hard work in person for once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD0")

    Jump("loc_6BDA")

    label("loc_6BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_6BDA")

    label("loc_6BDA")

    TalkEnd(0xFE)
    Return()

    # Function_16_6346 end

    def Function_17_6BDE(): pass

    label("Function_17_6BDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC0")

    ChrTalk(    #241
        0xFE,
        (
            "We're beginning final checks on the primary\x01",
            "flight engine inside the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "It should be perfectly tuned, but I just\x01",
            "can't stop worrying about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "I came out here to check the outer hull.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_6D62")

    label("loc_6CC0")


    ChrTalk(    #244
        0xFE,
        (
            "We're beginning final checks on the primary\x01",
            "flight engine inside the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "If we can just get the left side of the\x01",
            "ship in shape, we'll be able to fly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D62")

    Jump("loc_73CA")

    label("loc_6D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_6F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E75")

    ChrTalk(    #246
        0xFE,
        (
            "The flight engine's adjustments are a\x01",
            "very delicate thing, so we'll have to\x01",
            "have a talk with the helmsman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "He's the one who'll be flying the ship,\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "In a sense, it's an even more harrowing\x01",
            "and intense job than being a captain.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_6F1D")

    label("loc_6E75")


    ChrTalk(    #249
        0xFE,
        (
            "The flight engine's adjustments are a\x01",
            "very delicate thing, so we'll have to\x01",
            "have a talk with the helmsman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "He's the one who'll be flying the ship,\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F1D")

    Jump("loc_73CA")

    label("loc_6F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_715D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A8")

    ChrTalk(    #251
        0xFE,
        (
            "The bit on the hull here was called an\x01",
            "outrigger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "It had a supplementary flight engine\x01",
            "and a few other systems in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "Under normal circumstances, there's one\x01",
            "on each side of the ship to ensure stability...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "Unfortunately, our landing sheared our\x01",
            "left outrigger clean off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "We're doing everything we can to\x01",
            "prepare to fly with just one outrigger.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_715A")

    label("loc_70A8")


    ChrTalk(    #256
        0xFE,
        (
            "For now, I'm going to tune the surviving\x01",
            "engine in the right outrigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "It'll be a hard job, but on the other\x01",
            "hand, it's a chance to show off my\x01",
            "skills as an engineer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_715A")

    Jump("loc_73CA")

    label("loc_715D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D9")

    ChrTalk(    #258
        0xFE,
        "Looks like there's no trouble with this fin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "It endured the shock of the landing well.\x01",
            "That's good, since it means we don't\x01",
            "have to spend time repairing it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "Okay, next comes checking the outrigger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "Oh, the outriggers? Those are the 'pods'\x01",
            "you see on the sides of the hull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "They have various supplementary flight\x01",
            "engines and whatnot in them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_73CA")

    label("loc_72D9")


    ChrTalk(    #263
        0xFE,
        (
            "The outriggers are the 'pods' on the\x01",
            "sides of the hull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "They have various supplementary flight\x01",
            "engines and whatnot in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "And one of the outriggers was sheared off\x01",
            "in the crash. It isn't too surprising, given\x01",
            "how we landed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73CA")

    TalkEnd(0xFE)
    Return()

    # Function_17_6BDE end

    def Function_18_73CE(): pass

    label("Function_18_73CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73FD")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    Jump("loc_743F")

    label("loc_73FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_7424")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_743F")

    label("loc_7424")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_743F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7491")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17120, 3500, 23510, 135)

    label("loc_7491")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_74B4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20610, 0, 16960, 315)

    label("loc_74B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_74D7")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -23120, 0, 16149, 0)

    label("loc_74D7")

    Jump("loc_7625")

    label("loc_74DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7560")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7505")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4310, -4000, 22130, 315)

    label("loc_7505")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7517")
    ClearChrFlags(0x17, 0x80)

    label("loc_7517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_753A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5070, -3880, 23930, 270)

    label("loc_753A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_755D")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_755D")

    Jump("loc_7625")

    label("loc_7560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_758B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34850, -4000, 16079, 225)

    label("loc_758B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_75AE")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_75AE")

    Jump("loc_7625")

    label("loc_75B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_75F7")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -18510, 3500, 22430, 180)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75F7")
    SetChrFlags(0x8, 0x10)

    label("loc_75F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7625")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7625")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -43550, 5000, 31240, 225)

    label("loc_7625")

    OP_0D()
    Return()

    # Function_18_73CE end

    def Function_19_7627(): pass

    label("Function_19_7627")

    EventBegin(0x0)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)
    OP_D2(0x260222, 0x260227, 0x15)
    OP_D2(0x6007C, 0x60081, 0x16)
    OP_D2(0x260068, 0x26006D, 0x17)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(58350, -4000, 15070, 0)
    OP_67(0, 9860, -10000, 0)
    OP_6B(4650, 0)
    OP_6C(310000, 0)
    OP_6E(684, 0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -20700, 3500, 24660, 180)
    SetChrPos(0xC, -22360, 3500, 24090, 225)
    SetChrPos(0xB, -22990, 3500, 24700, 180)
    SetChrPos(0xD, -22150, 3500, 28290, 90)
    SetChrPos(0x102, -21110, 3500, 26540, 135)
    SetChrPos(0xA, -19850, 3500, 23160, 180)
    SetChrPos(0x8, -18490, 3500, 26100, 135)
    SetChrPos(0x9, -17510, 3500, 28380, 45)
    SetChrPos(0xE, -19700, 3500, 25650, 90)
    SetChrPos(0xF, -22180, 3500, 25600, 0)
    SetChrPos(0x13, -18800, 3500, 23370, 0)
    SetChrPos(0x12, -18590, 3500, 27820, 0)
    SetChrPos(0x10, -20780, 3500, 28750, 0)
    SetChrPos(0x11, -19600, 3500, 28870, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    FadeToBright(2000, 0)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 30)

    def lambda_7819():
        OP_6D(-55380, -4000, 35510, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7819)

    def lambda_7831():
        OP_67(0, 8530, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7831)

    def lambda_7849():
        OP_6E(662, 11000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7849)
    OP_A2(0x0)
    OP_43(0x101, 0x1, 0x0, 0x14)
    OP_43(0x11, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    OP_43(0xD, 0x1, 0x0, 0x18)
    OP_43(0xA, 0x1, 0x0, 0x14)
    Sleep(100)
    OP_43(0xF, 0x1, 0x0, 0x1A)
    OP_43(0x10, 0x1, 0x0, 0x1B)
    OP_43(0x8, 0x1, 0x0, 0x17)
    OP_43(0x12, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0xB, 0x1, 0x0, 0x15)
    OP_43(0x13, 0x1, 0x0, 0x16)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0xC, 0x1, 0x0, 0x14)
    OP_43(0x9, 0x1, 0x0, 0x19)
    OP_C8(0x80, 0x172, "C_PLAC25._CH", 0x1, 0x9C4)
    Sleep(8000)
    OP_A3(0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x2)
    Fade(500)
    OP_6D(-20600, 3500, 26640, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(339000, 0)
    OP_6E(392, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #266
        0x101,
        "#1020F#5POh, WOW...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xC,
        "#560F#5PIt's really pretty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x11,
        (
            "#151F#6PWowowow...\x01",
            "Soooo many PIIIIICTURES!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 22)
    OP_0D()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0x11, 225, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0x11, 90, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0x11, 0, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    Sleep(300)

    ChrTalk(    #269
        0x10,
        (
            "#142F#6PEr, Dorothy, don't blow all your photo\x01",
            "quartz in five minutes, all right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #270
        0xE,
        (
            "#1063F#6PGotta admit, this isn't what\x01",
            "I expected at all.\x02\x03",

            "This is less like a city and\x01",
            "more like a garden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x102,
        (
            "#1043F#6PI wonder...\x02\x03",

            "#1042FPerhaps this is like the city parks\x01",
            "in certain large cities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        (
            "#1007F#5PIt does sorta feel that way,\x01",
            "looking at it.\x02\x03",

            "#1019FThough I've never heard of a city park\x01",
            "so huge that you can't see the end of\x01",
            "it in any direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x9,
        "#035F#6PThe scale of it does overwhelm.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #274
        0x101,
        "#1004F#5PSieg!\x02",
    )

    CloseMessageWindow()

    def lambda_7D33():
        OP_6D(-23900, 3500, 19660, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D33)
    SetChrPos(0x14, -28880, 6500, 7610, 45)
    ClearChrFlags(0x14, 0x80)

    def lambda_7D61():

        label("loc_7D61")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7D61")

    QueueWorkItem2(0xA, 1, lambda_7D61)
    Sleep(50)

    def lambda_7D77():

        label("loc_7D77")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7D77")

    QueueWorkItem2(0x102, 1, lambda_7D77)

    def lambda_7D88():

        label("loc_7D88")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7D88")

    QueueWorkItem2(0x8, 1, lambda_7D88)
    Sleep(50)

    def lambda_7D9E():

        label("loc_7D9E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7D9E")

    QueueWorkItem2(0x101, 1, lambda_7D9E)

    def lambda_7DAF():

        label("loc_7DAF")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7DAF")

    QueueWorkItem2(0x9, 1, lambda_7DAF)
    Sleep(50)

    def lambda_7DC5():

        label("loc_7DC5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7DC5")

    QueueWorkItem2(0xC, 1, lambda_7DC5)

    def lambda_7DD6():

        label("loc_7DD6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7DD6")

    QueueWorkItem2(0xE, 1, lambda_7DD6)

    def lambda_7DE7():

        label("loc_7DE7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7DE7")

    QueueWorkItem2(0x12, 1, lambda_7DE7)
    Sleep(50)

    def lambda_7DFD():

        label("loc_7DFD")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7DFD")

    QueueWorkItem2(0xB, 1, lambda_7DFD)

    def lambda_7E0E():

        label("loc_7E0E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7E0E")

    QueueWorkItem2(0xF, 1, lambda_7E0E)

    def lambda_7E1F():

        label("loc_7E1F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7E1F")

    QueueWorkItem2(0x10, 1, lambda_7E1F)
    Sleep(50)

    def lambda_7E35():

        label("loc_7E35")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7E35")

    QueueWorkItem2(0xD, 1, lambda_7E35)

    def lambda_7E46():

        label("loc_7E46")

        OP_8C(0xFE, 225, 400)
        OP_48()
        Jump("loc_7E46")

    QueueWorkItem2(0x13, 1, lambda_7E46)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 9)

    def lambda_7E61():

        label("loc_7E61")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_7E61")

    QueueWorkItem2(0x11, 1, lambda_7E61)
    WaitChrThread(0x101, 0x2)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_7E7C():
        OP_8E(0xFE, 0xFFFFB078, 0x157C, 0x5262, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7E7C)
    Sleep(500)

    def lambda_7E9C():
        OP_6D(-20680, 3500, 25150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E9C)
    WaitChrThread(0x14, 0x1)
    OP_43(0x14, 0x1, 0x0, 0x1C)
    WaitChrThread(0x101, 0x2)
    OP_8E(0x14, 0xFFFFB154, 0x1194, 0x5942, 0xBB8, 0x0)
    OP_8C(0x14, 180, 400)
    OP_8F(0x14, 0xFFFFB154, 0xE74, 0x5942, 0x3E8, 0x0)
    OP_A3(0x1)
    Fade(500)
    OP_44(0xA, 0x1)
    SetChrPos(0x14, -19850, 3800, 23160, 0)
    SetChrFlags(0x14, 0x80)
    SetChrSubChip(0xA, 5)
    SetChrChipByIndex(0xA, 21)

    def lambda_7F20():

        label("loc_7F20")

        OP_8C(0xFE, 315, 400)
        OP_48()
        Jump("loc_7F20")

    QueueWorkItem2(0x13, 1, lambda_7F20)
    OP_0D()

    ChrTalk(    #275
        0x14,
        "#311F#5PScreee, screee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xA,
        (
            "#1165F#2PSieg, thank goodness!\x01",
            "I was afraid you'd been hurt or got lost.\x02\x03",

            "#1168FDon't worry, we're all fine too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x14,
        (
            "#311F#5PScreee. ♪\x02\x03",

            "#310FScreee!\x02\x03",

            "Screee-eee, screeee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xA,
        "#1167F#2PAh, I see... Thank you.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 3)
    OP_8C(0xA, 0, 400)
    ClearChrFlags(0xA, 0x20)
    Sleep(300)

    ChrTalk(    #279
        0xA,
        (
            "#1162F#5PApparently, we've crashed on the\x01",
            "easternmost side of the city.\x02\x03",

            "And...the Glorious is docked on\x01",
            "the exact opposite side.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_19_7627 end

    def Function_20_80E0(): pass

    label("Function_20_80E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8102")
    OP_8C(0xFE, 45, 400)
    Sleep(1200)
    OP_8C(0xFE, 225, 400)
    Sleep(1200)
    Jump("Function_20_80E0")

    label("loc_8102")

    Return()

    # Function_20_80E0 end

    def Function_21_8103(): pass

    label("Function_21_8103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8125")
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    Jump("Function_21_8103")

    label("loc_8125")

    Return()

    # Function_21_8103 end

    def Function_22_8126(): pass

    label("Function_22_8126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8148")
    OP_8C(0xFE, 45, 400)
    Sleep(1300)
    OP_8C(0xFE, 135, 400)
    Sleep(1300)
    Jump("Function_22_8126")

    label("loc_8148")

    Return()

    # Function_22_8126 end

    def Function_23_8149(): pass

    label("Function_23_8149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_816B")
    OP_8C(0xFE, 225, 400)
    Sleep(1800)
    OP_8C(0xFE, 135, 400)
    Sleep(1800)
    Jump("Function_23_8149")

    label("loc_816B")

    Return()

    # Function_23_8149 end

    def Function_24_816C(): pass

    label("Function_24_816C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_818E")
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    Jump("Function_24_816C")

    label("loc_818E")

    Return()

    # Function_24_816C end

    def Function_25_818F(): pass

    label("Function_25_818F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_81B1")
    OP_8C(0xFE, 180, 400)
    Sleep(1200)
    OP_8C(0xFE, 45, 400)
    Sleep(1200)
    Jump("Function_25_818F")

    label("loc_81B1")

    Return()

    # Function_25_818F end

    def Function_26_81B2(): pass

    label("Function_26_81B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_81D4")
    OP_8C(0xFE, 45, 400)
    Sleep(1300)
    OP_8C(0xFE, 180, 400)
    Sleep(1300)
    Jump("Function_26_81B2")

    label("loc_81D4")

    Return()

    # Function_26_81B2 end

    def Function_27_81D5(): pass

    label("Function_27_81D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_81F7")
    OP_8C(0xFE, 90, 400)
    Sleep(1200)
    OP_8C(0xFE, 45, 400)
    Sleep(1200)
    Jump("Function_27_81D5")

    label("loc_81F7")

    Return()

    # Function_27_81D5 end

    def Function_28_81F8(): pass

    label("Function_28_81F8")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 23)

    label("loc_8202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8215")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_8202")

    label("loc_8215")

    Return()

    # Function_28_81F8 end

    def Function_29_8216(): pass

    label("Function_29_8216")

    SetMapFlags(0x2000000)
    Return()

    # Function_29_8216 end

    def Function_30_821C(): pass

    label("Function_30_821C")

    ClearMapFlags(0x2000000)
    Return()

    # Function_30_821C end

    SaveToFile()

Try(main)
