from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0310   ._SN',
        MapName             = 'Event',
        Location            = 'E0310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0310_1 ._SN',
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
        'Scherazard',                           # 9
        'Olivier',                              # 10
        'Kloe',                                 # 11
        'Zin',                                  # 12
        'Captain Schwarz',                      # 13
        'General Morgan',                       # 14
        'Helmsman Lux',                         # 15
        'Sensor Operator Echo',                 # 16
        'Comm. Officer Leon',                   # 17
        'Professor Russell',                    # 18
        'Agate',                                # 19
        'Tita',                                 # 20
        'Father Kevin',                         # 21
        'Major Vander',                         # 22
        'Nial',                                 # 23
        'Dorothy',                              # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Sky Bandit Lonnie',                    # 28
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
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT07/CH00070 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT07/CH02080 ._CH',             # 05
        'ED6_DT26/CH20362 ._CH',             # 06
        'ED6_DT06/CH20113 ._CH',             # 07
        'ED6_DT26/CH20367 ._CH',             # 08
        'ED6_DT26/CH20368 ._CH',             # 09
        'ED6_DT26/CH20369 ._CH',             # 0A
        'ED6_DT27/CH03840 ._CH',             # 0B
        'ED6_DT27/CH03850 ._CH',             # 0C
        'ED6_DT27/CH03860 ._CH',             # 0D
        'ED6_DT07/CH02020 ._CH',             # 0E
        'ED6_DT07/CH00050 ._CH',             # 0F
        'ED6_DT07/CH00060 ._CH',             # 10
        'ED6_DT27/CH03080 ._CH',             # 11
        'ED6_DT26/CH20500 ._CH',             # 12
        'ED6_DT27/CH03573 ._CH',             # 13
        'ED6_DT27/CH03210 ._CH',             # 14
        'ED6_DT26/CH20418 ._CH',             # 15
        'ED6_DT07/CH02060 ._CH',             # 16
        'ED6_DT06/CH20063 ._CH',             # 17
        'ED6_DT27/CH03570 ._CH',             # 18
        'ED6_DT27/CH03001 ._CH',             # 19
        'ED6_DT27/CH03011 ._CH',             # 1A
        'ED6_DT07/CH01320 ._CH',             # 1B
        'ED6_DT06/CH20053 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00070P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT07/CH02080P._CP',             # 05
        'ED6_DT26/CH20362P._CP',             # 06
        'ED6_DT06/CH20113P._CP',             # 07
        'ED6_DT26/CH20367P._CP',             # 08
        'ED6_DT26/CH20368P._CP',             # 09
        'ED6_DT26/CH20369P._CP',             # 0A
        'ED6_DT27/CH03840P._CP',             # 0B
        'ED6_DT27/CH03850P._CP',             # 0C
        'ED6_DT27/CH03860P._CP',             # 0D
        'ED6_DT07/CH02020P._CP',             # 0E
        'ED6_DT07/CH00050P._CP',             # 0F
        'ED6_DT07/CH00060P._CP',             # 10
        'ED6_DT27/CH03080P._CP',             # 11
        'ED6_DT26/CH20500P._CP',             # 12
        'ED6_DT27/CH03573P._CP',             # 13
        'ED6_DT27/CH03210P._CP',             # 14
        'ED6_DT26/CH20418P._CP',             # 15
        'ED6_DT07/CH02060P._CP',             # 16
        'ED6_DT06/CH20063P._CP',             # 17
        'ED6_DT27/CH03570P._CP',             # 18
        'ED6_DT27/CH03001P._CP',             # 19
        'ED6_DT27/CH03011P._CP',             # 1A
        'ED6_DT07/CH01320P._CP',             # 1B
        'ED6_DT06/CH20053P._CP',             # 1C
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -1040,
        Z                   = 100,
        Y                   = 99020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 1300,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1760,
        Z                   = 300,
        Y                   = 96770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196626,
        ChipIndex           = 0x12,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3480,
        Z                   = 0,
        Y                   = -840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3480,
        Z                   = 0,
        Y                   = -840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2920,
        Z                   = 2000,
        Y                   = 49050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2670,
        Z                   = 0,
        Y                   = 100010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 3470,
        Y                   = -1000,
        Z                   = -840,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -2920,
        Y                   = 1000,
        Z                   = 49050,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -900,
        Y                   = -500,
        Z                   = 500,
        Range               = -3110,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x898,
        Unknown_18          = 0x0,
        Unknown_1C          = 47,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_C0B",          # 01, 1
        "Function_2_D74",          # 02, 2
        "Function_3_EF1",          # 03, 3
        "Function_4_378A",         # 04, 4
        "Function_5_3C35",         # 05, 5
        "Function_6_6612",         # 06, 6
        "Function_7_6636",         # 07, 7
        "Function_8_6934",         # 08, 8
        "Function_9_69B1",         # 09, 9
        "Function_10_6C0B",        # 0A, 10
        "Function_11_6D3B",        # 0B, 11
        "Function_12_72D6",        # 0C, 12
        "Function_13_731E",        # 0D, 13
        "Function_14_7366",        # 0E, 14
        "Function_15_73AE",        # 0F, 15
        "Function_16_73F6",        # 10, 16
        "Function_17_7872",        # 11, 17
        "Function_18_7C1F",        # 12, 18
        "Function_19_7D87",        # 13, 19
        "Function_20_80AA",        # 14, 20
        "Function_21_854F",        # 15, 21
        "Function_22_8591",        # 16, 22
        "Function_23_85EA",        # 17, 23
        "Function_24_8C02",        # 18, 24
        "Function_25_91FA",        # 19, 25
        "Function_26_9CD4",        # 1A, 26
        "Function_27_9D1C",        # 1B, 27
        "Function_28_9D64",        # 1C, 28
        "Function_29_9DAC",        # 1D, 29
        "Function_30_9DF4",        # 1E, 30
        "Function_31_9E3C",        # 1F, 31
        "Function_32_9E84",        # 20, 32
        "Function_33_9ECC",        # 21, 33
        "Function_34_9F14",        # 22, 34
        "Function_35_A31B",        # 23, 35
        "Function_36_A851",        # 24, 36
        "Function_37_B083",        # 25, 37
        "Function_38_B917",        # 26, 38
        "Function_39_C0B2",        # 27, 39
        "Function_40_C1CD",        # 28, 40
        "Function_41_CAB6",        # 29, 41
        "Function_42_E81E",        # 2A, 42
        "Function_43_E890",        # 2B, 43
        "Function_44_E902",        # 2C, 44
        "Function_45_E988",        # 2D, 45
        "Function_46_EA15",        # 2E, 46
        "Function_47_EC83",        # 2F, 47
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_6CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A1")
    SetChrChipByIndex(0xA, 20)
    SetChrPos(0xA, -910, 2000, 89640, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_55C")
    SetChrPos(0x16, 1860, 2000, 89340, 0)
    ClearChrFlags(0x16, 0x80)
    OP_43(0x16, 0x0, 0x0, 0x2)
    SetChrPos(0x17, 2460, 2000, 88510, 0)
    ClearChrFlags(0x17, 0x80)
    OP_43(0x17, 0x0, 0x0, 0x2)
    SetChrPos(0x18, 3480, 0, -840, 270)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52A")
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 18)

    label("loc_52A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_559")
    SetChrChipByIndex(0x15, 24)
    SetChrPos(0x15, 130, 2000, 91480, 0)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x2)

    label("loc_559")

    Jump("loc_6CB")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_5E8")
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xF, -2660, 0, 99090, 315)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 11)
    ClearChrFlags(0xF, 0x10)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -840, 0, 97770, 45)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 4)
    ClearChrFlags(0xC, 0x10)
    OP_43(0xC, 0x0, 0x0, 0x2)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_5E5")

    Jump("loc_6CB")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_63E")
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    OP_43(0xC, 0x0, 0x0, 0x2)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_63B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_63B")

    Jump("loc_6CB")

    label("loc_63E")

    SetChrPos(0xE, -920, 0, 97790, 0)
    ClearChrFlags(0xE, 0x10)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 13)
    OP_43(0xE, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 370, 0, 97940, 45)
    ClearChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 12)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -1600, 2000, 91460, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x15, 24)
    SetChrPos(0x15, 130, 2000, 91480, 270)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x2)

    label("loc_6CB")

    Jump("loc_92C")

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_733")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_730")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_730")

    Jump("loc_92C")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_79D")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x10)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79A")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_79A")

    Jump("loc_92C")

    label("loc_79D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_848")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 530, 0, 98030, 90)
    SetChrChipByIndex(0x10, 12)
    ClearChrFlags(0x10, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_845")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)

    label("loc_845")

    Jump("loc_92C")

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_8D6")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B8")
    SetChrPos(0x12, 770, 2000, 89910, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 28)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_8B8")

    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_92C")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_8E5")
    ClearChrFlags(0x18, 0x80)
    Jump("loc_92C")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92C")
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 18)
    SetChrPos(0xA, -2290, 2000, 91270, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F0)
    Event(0, 41)
    Jump("loc_C0A")

    label("loc_94D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F1)
    Event(1, 12)
    Jump("loc_C0A")

    label("loc_96E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F2)
    Event(1, 13)
    Jump("loc_C0A")

    label("loc_98F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F3)
    Event(1, 14)
    Jump("loc_C0A")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F4)
    Event(1, 16)
    Jump("loc_C0A")

    label("loc_9D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F5)
    Event(1, 17)
    Jump("loc_C0A")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A11")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_C0A")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_A30")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_C0A")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_A4F")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_C0A")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_A6E")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_C0A")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_A8D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_C0A")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_AAC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_C0A")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_ACB")
    OP_A3(0x10F6)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_C0A")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_AEA")
    OP_A3(0x10F7)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 24)
    Jump("loc_C0A")

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_B09")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F8)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_C0A")

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    OP_A3(0x10FA)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_C0A")

    label("loc_B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_B4E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    SetMapFlags(0x10000000)
    Event(0, 34)
    Jump("loc_C0A")

    label("loc_B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_END)), "loc_B6D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FA)
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_C0A")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_END)), "loc_B8C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FB)
    SetMapFlags(0x10000000)
    Event(0, 37)
    Jump("loc_C0A")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_END)), "loc_BAB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FC)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_C0A")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_END)), "loc_BCA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FD)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_C0A")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 6)), scpexpr(EXPR_END)), "loc_BE9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FE)
    SetMapFlags(0x10000000)
    Event(0, 40)
    Jump("loc_C0A")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0A")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_C0A")

    Return()

    # Function_0_472 end

    def Function_1_C0B(): pass

    label("Function_1_C0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C29")

    Call(0, 9)
    Call(0, 8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4F")
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)

    label("loc_C4F")

    Jump("loc_C63")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C63")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_C63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8C")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C99")

    label("loc_C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C99")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_C99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC4")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_CC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_D08")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    Jump("loc_D73")

    label("loc_D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_D12")
    Jump("loc_D73")

    label("loc_D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_D30")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    Jump("loc_D73")

    label("loc_D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_D53")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    OP_1B(0xA, 0x0, 0x2E)
    Jump("loc_D73")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D73")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)

    label("loc_D73")

    Return()

    # Function_1_C0B end

    def Function_2_D74(): pass

    label("Function_2_D74")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D99")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_EDB")

    label("loc_D99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB2")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_EDB")

    label("loc_DB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_EDB")

    label("loc_DCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_EDB")

    label("loc_DE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_EDB")

    label("loc_DFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E16")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_EDB")

    label("loc_E16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_EDB")

    label("loc_E2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E48")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_EDB")

    label("loc_E48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E61")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_EDB")

    label("loc_E61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_EDB")

    label("loc_E7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E93")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_EDB")

    label("loc_E93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_EDB")

    label("loc_EAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_EDB")

    label("loc_EC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_EDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EF0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_EDB")

    label("loc_EF0")

    Return()

    # Function_2_D74 end

    def Function_3_EF1(): pass

    label("Function_3_EF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F68")

    ChrTalk(    #0
        0xA,
        (
            "#1164FOh, hey, everyone.\x02\x03",

            "#1160FHow's the expedition going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1011FYeah, um...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 19)
    Return()

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_263F")
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
        (0, "loc_FD2"),
        (1, "loc_25E0"),
        (2, "loc_2639"),
        (SWITCH_DEFAULT, "loc_263C"),
    )


    label("loc_FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 2)), scpexpr(EXPR_END)), "loc_16F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x448, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1512")

    ChrTalk(    #2
        0xA,
        (
            "#1162FOh, hey, everyone.\x02\x03",

            "How does it look inside the\x01",
            "Axis Pillar?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B2")

    ChrTalk(    #3
        0x10F,
        (
            "#175FIn truth, Your Majesty...\x02\x03",

            "#176FWe were met by a man who called himself\x01",
            "the Phantom Thief.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x10F, 400)
    Jump("loc_112D")

    label("loc_10B2")


    ChrTalk(    #4
        0x101,
        (
            "#1003FWe got a welcoming party from an\x01",
            "Enforcer right off the bat.\x02\x03",

            "#1007FAnd...it was that Phantom Thief guy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_112D")


    ChrTalk(    #5
        0xA,
        "#1163FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1040FOnce we defeated him, however, he promised\x01",
            "to leave and not harass us any further.\x02\x03",

            "I don't believe you need to worry about\x01",
            "him any more, Kloe. He usually keeps\x01",
            "his word on this sort of thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #7
        0xA,
        (
            "#1167FI see...\x02\x03",

            "#1382FPhew! That's a bit of a burden off\x01",
            "of my mind, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1016FHaha, yeah, I can guess why.\x02\x03",

            "He always had that weirdo thing\x01",
            "about you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143A")

    ChrTalk(    #9
        0x10F,
        (
            "#176FHmph. A poor joke, at best.\x02\x03",

            "#178FShould he appear before Her Highness again,\x01",
            "I shall personally clamp him in irons and\x01",
            "make him the court jester.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1016FAh...hahahaha...\x01",
            "(She'd totally do that, wouldn't she.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#1035FStill...the other Enforcers are no doubt\x01",
            "waiting for us further in.\x02\x03",

            "#1042FWe will need to remain on our guard as\x01",
            "we proceed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C3")

    label("loc_143A")


    ChrTalk(    #12
        0x102,
        (
            "#1035FStill...the other Enforcers are no doubt\x01",
            "waiting for us further in.\x02\x03",

            "#1042FWe will need to remain on our guard as\x01",
            "we proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C3")


    ChrTalk(    #13
        0xA,
        "#1162FYes, very true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1006FRight, then! Let's get back to it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22A5)
    Jump("loc_15A0")

    label("loc_1512")


    ChrTalk(    #15
        0xA,
        (
            "#1162FI'm glad to hear that Bleublanc has\x01",
            "departed...\x02\x03",

            "However, we still have a long fight\x01",
            "ahead of us.\x02\x03",

            "Everyone, be careful, please...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A0")

    Jump("loc_16ED")

    label("loc_15A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1680")

    ChrTalk(    #16
        0xA,
        (
            "#1167FTo be honest, I'm glad Bleublanc departed\x01",
            "without further violence.\x02\x03",

            "#1162FStill, he is just one of many foes we will\x01",
            "likely be facing before we are done.\x02\x03",

            "Everyone, please, be careful as you go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_16ED")

    label("loc_1680")


    ChrTalk(    #17
        0xA,
        (
            "#1162FThe fights yet to come are the most\x01",
            "dangerous we've yet faced...\x02\x03",

            "We should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16ED")

    Jump("loc_25DD")

    label("loc_16F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1B0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_187E")
    TurnDirection(0xA, 0x10F, 400)

    ChrTalk(    #18
        0xA,
        "#1160FAh, Julia. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        (
            "#178FForgive me, Your Highness.\x02\x03",

            "I must leave command here to you\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        (
            "#1168FHaha. Don't worry, that's fine.\x02\x03",

            "Thanks to the crew's hard work,\x01",
            "repairs are going smoothly.\x02\x03",

            "And I was the one who told Grandmother\x01",
            "we would be borrowing the Arseille.\x02\x03",

            "#1160FPlease, leave this to me.\x01",
            "I'm capable of handling it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22D7)
    Jump("loc_1B0C")

    label("loc_187E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1972")

    ChrTalk(    #21
        0xA,
        (
            "#1167FWe will be performing a stress test\x01",
            "on the airship engines soon.\x02\x03",

            "If those succeed, we should be able to\x01",
            "get airborne again...\x02\x03",

            "#1162FSo, please, everyone, come back safely.\x02\x03",

            "I want us all to return to land--together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0C")

    label("loc_1972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A91")

    ChrTalk(    #22
        0xA,
        (
            "#1167FWe will soon be performing a critical\x01",
            "test of the bridge instrumentation.\x02\x03",

            "If that goes well, we'll be close to\x01",
            "finished with the repair work.\x02\x03",

            "#1162FI pray we will succeed in our mission and\x01",
            "all return safely to land...together.\x02\x03",

            "Everyone...please, be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_1B0C")

    label("loc_1A91")


    ChrTalk(    #23
        0x105,
        (
            "#1160FI pray we will succeed in our mission and\x01",
            "all return safely to land...together.\x02\x03",

            "Everyone...please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0C")

    Jump("loc_25DD")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1A")

    ChrTalk(    #24
        0xA,
        (
            "#1160FI'm glad to hear our friends aboard the\x01",
            "Bobcat are safe.\x02\x03",

            "It seems they arrived here even before\x01",
            "we did.\x02\x03",

            "They may have learned something useful\x01",
            "about this floating city.\x02\x03",

            "I think it would be worthwhile to find\x01",
            "the time to visit them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_1C9C")

    label("loc_1C1A")


    ChrTalk(    #25
        0xA,
        (
            "#1160FIt seems the Capuas arrived here even\x01",
            "before we did.\x02\x03",

            "They may have learned something useful\x01",
            "about this floating city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9C")

    Jump("loc_25DD")

    label("loc_1C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_2438")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21DC")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #26
        0xA,
        (
            "#1168FJosette...welcome aboard the Arseille.\x02\x03",

            "I fear we can't welcome you as well as\x01",
            "we should, as we're busy with repair work.\x02\x03",

            "Please, treat our ship as though it were\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10B,
        (
            "#414FUh, s-sure...\x01",
            "Thanks, uh, Your Highness.\x02\x03",

            "#415FHeh, makes me feel kinda...itchy,\x01",
            "gettin' welcomed like this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)

    ChrTalk(    #28
        0x101,
        (
            "#1019FOh, GROSS. Do you, like, not shower\x01",
            "or something, you flea-bitten tomboy?\x01",
            "And in front of a princess!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x10B, 0x101, 400)

    ChrTalk(    #29
        0x10B,
        "#216FY-You idiot! That's not what I meant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1016FHaha, um, sorry. I know, I just kinda...\x02\x03",

            "I mean, when you say 'bandits' you just think\x01",
            "dirty guys with beards and stuff, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10B,
        (
            "#212FHmph. Well, if it was JUST Don and\x01",
            "Kyle and the rest of that lot, maybe.\x02\x03",

            "#210FI make sure everything stays clean on\x01",
            "the Bobcat, though, including smacking\x01",
            "the boys into doing their laundry.\x02\x03",

            "To be honest, the Bobcat's no worse\x01",
            "than this ship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)

    ChrTalk(    #32
        0x102,
        (
            "#1040FIt's true. The Bobcat was surprisingly\x01",
            "clean for an 'outlaw' vessel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10B,
        "#211FHaha! I know, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #34
        0x101,
        (
            "#1015FHuh, okay...\x02\x03",

            "#1019F...So, Joshua?\x01",
            "Why are you taking Josette's side?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #35
        0x102,
        (
            "#1044FEr...?\x02\x03",

            "I, uh, wasn't taking sides, just stating fa--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "#1167FAhem!\x02\x03",

            "#1382FA-Anyway, let's do our best\x01",
            "to be friends.\x02\x03",

            "Helping one another must come first\x01",
            "in our situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    OP_A2(0x22A6)
    Jump("loc_2435")

    label("loc_21DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_226B")

    ChrTalk(    #37
        0xA,
        (
            "#1382FEveryone, please try to keep the peace\x01",
            "inside the ship.\x02\x03",

            "Helping one another must come first\x01",
            "in our situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2435")

    label("loc_226B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236E")

    ChrTalk(    #38
        0xA,
        (
            "#1167FRegardless of what's happened in the\x01",
            "past, we are now all in the same boat.\x02\x03",

            "It's only natural for us to cooperate\x01",
            "with the Capuas.\x02\x03",

            "#1160FI will speak to Julia personally\x01",
            "about this.\x02\x03",

            "You should focus on the exploration\x01",
            "of the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2435")

    label("loc_236E")


    ChrTalk(    #39
        0xA,
        (
            "#1167FRegardless of what's happened in the\x01",
            "past, we are now all in the same boat.\x02\x03",

            "#1160FIt's only natural for us to cooperate\x01",
            "with the Capuas.\x02\x03",

            "You should focus on the exploration\x01",
            "of the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2435")

    Jump("loc_25DD")

    label("loc_2438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_25DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2520")

    ChrTalk(    #40
        0xA,
        (
            "#1162FRight now the crew is surveying the\x01",
            "damage we took.\x02\x03",

            "Once that's done, we can begin repair work.\x02\x03",

            "#1167FWe don't know what will happen going\x01",
            "forward...\x02\x03",

            "We need to be able to fly as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_25DD")

    label("loc_2520")


    ChrTalk(    #41
        0xA,
        (
            "#1162FOnce we've taken stock of how badly\x01",
            "we've been hurt, we intend to start repairs.\x02\x03",

            "We don't know what will happen going\x01",
            "forward...\x02\x03",

            "We need to be able to fly as soon as\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DD")

    Jump("loc_263C")

    label("loc_25E0")


    ChrTalk(    #42
        0xA,
        (
            "#1160FYou wish to change party members?\x01",
            "I understand. Shall I accompany you?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_263C")

    label("loc_2639")

    Jump("loc_263C")

    label("loc_263C")

    Jump("loc_3786")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3182")
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
        (0, "loc_26A9"),
        (1, "loc_3127"),
        (2, "loc_317C"),
        (SWITCH_DEFAULT, "loc_317F"),
    )


    label("loc_26A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1D")

    ChrTalk(    #43
        0xA,
        (
            "#043FThe Enforcer waiting in the last tower...\x01",
            "It'll be that girl, Renne, won't it?\x02\x03",

            "I hope you can bring her to her senses\x01",
            "like you want to, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1003FI'm not sure how well my voice will\x01",
            "reach her...\x02\x03",

            "#1002F...But I'm going to try my hardest and\x01",
            "yell as loud as I need to in order to\x01",
            "be heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1035FThat's right...\x01",
            "Do everything you can, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A2")

    ChrTalk(    #46
        0x106,
        (
            "#051FYeah, go for it, I say.\x02\x03",

            "It's the only way we're gonna save\x01",
            "that kiddo from a life of murder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_28A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292A")

    ChrTalk(    #47
        0x108,
        (
            "#070FThat's the only proper thing for a\x01",
            "bracer to do!\x02\x03",

            "That's the only chance we have to save\x01",
            "that girl, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_292A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C2")

    ChrTalk(    #48
        0x103,
        (
            "#020FYes, try your hardest, Estelle.\x02\x03",

            "There's no other way we can save her from\x01",
            "a life of murderous service to Ouroboros,\x01",
            "I fear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_29C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A75")

    ChrTalk(    #49
        0x109,
        (
            "#1067FDon't give up till the very end.\x02\x03",

            "Knowin' what I do about Ouroboros,\x01",
            "if you really want to save her, it's your\x01",
            "only shot at yanking her from their coils.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A75")


    ChrTalk(    #50
        0xA,
        (
            "#047FI'm sure our voices will reach Renne.\x02\x03",

            "#040FFor now, the most we can do, I think,\x01",
            "is believe in her heart, and never forget\x01",
            "who we're fighting to save.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E4B)
    Jump("loc_2BBF")

    label("loc_2B1D")


    ChrTalk(    #51
        0xA,
        (
            "#047FI'm sure our voices will reach Renne.\x02\x03",

            "#040FFor now, the most we can do, I think,\x01",
            "is believe in her heart, and never forget\x01",
            "who we're fighting to save.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBF")

    Jump("loc_3124")

    label("loc_2BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_2EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6D")
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #52
        0xA,
        (
            "#040FOh, Estelle, Joshua.\x02\x03",

            "I just received word from the guard\x01",
            "force stationed in Manoria.\x02\x03",

            "Matron Theresa and the children were\x01",
            "evacuated safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1004FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        "#047FYes, they said everyone's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1007FPhew! That's a relief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1040FYes... I'd been worried about them.\x02\x03",

            "#1043FStill, with the towers as they are,\x01",
            "no one can let their guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x103,
        (
            "#026FYes, it may be a bit early to rejoice.\x02\x03",

            "#022FRight now, we need to focus on the\x01",
            "task at hand and get to that tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1002FYeah... you're right.\x02\x03",

            "If you're ready, Kloe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#042FYes, if you need me, simply ask any time.\x01",
            "I am prepared.\x02\x03",

            "Everyone, please, be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2EEC")

    label("loc_2E6D")


    ChrTalk(    #60
        0xA,
        (
            "#040FMatron Theresa and the children were all\x01",
            "evacuated safely.\x02\x03",

            "That's one thing we don't need to worry\x01",
            "about, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEC")

    Jump("loc_3124")

    label("loc_2EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3124")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C1")

    ChrTalk(    #61
        0xA,
        (
            "#040FThe Zeiss Guard is working hard.\x02\x03",

            "It looks like the front lines remain\x01",
            "unbroken, for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1011FI see... That's a relief.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC5")

    ChrTalk(    #63
        0x107,
        "#561FBut, but, but... I'm still worried...\x02",
    )

    CloseMessageWindow()

    label("loc_2FC5")


    ChrTalk(    #64
        0x102,
        (
            "#1042FWe should hurry our investigation\x01",
            "of the tower.\x02\x03",

            "The attacks on Zeiss are likely mere\x01",
            "diversions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x108,
        (
            "#072FYes. The tower is definitely their main\x01",
            "goal.\x02\x03",

            "We should focus our efforts on defeating\x01",
            "the Enforcers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1002FRight, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3124")

    label("loc_30C1")


    ChrTalk(    #67
        0xA,
        (
            "#040FThe front lines in Zeiss remain unbroken\x01",
            "for now.\x02\x03",

            "We should hurry and retake the tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3124")

    Jump("loc_317F")

    label("loc_3127")


    ChrTalk(    #68
        0xA,
        (
            "#040FYou wish to change party members?\x01",
            "Very well. Shall I accompany you?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_317F")

    label("loc_317C")

    Jump("loc_317F")

    label("loc_317F")

    Jump("loc_3786")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_3786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E4")
    OP_4A(0xFE, 255)

    ChrTalk(    #69
        0xA,
        (
            "#040FEstelle! Hello.\x02\x03",

            "Are you finding it a little hard\x01",
            "to calm down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1000FYeah, a bit.\x01",
            "Really can't stay still for this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#045FThat reminds me... You, um, always walk\x01",
            "around like this on the passenger ships,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1008FAhaha... Yeah, now that you mention it,\x01",
            "I do.\x02\x03",

            "I dunno, I feel all kinda suffocated and\x01",
            "trapped when I just have to sit around\x01",
            "politely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#048FHaha... That's very like you, Estelle.\x02\x03",

            "But, ah, I wouldn't worry about that too\x01",
            "much on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1011FHuh? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#047FProperty of the Auslese family it may be,\x01",
            "but this is still a fully-functional war\x01",
            "cruiser...\x02\x03",

            "At full speed, its engine capabilities far\x01",
            "exceed those of passenger vessels.\x02\x03",

            "#040FIf we go at flank speed, I don't think you'd\x01",
            "even be able to remain standing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1004FI-Is it seriously that fast\x01",
            "with that new engine?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "#048FHaha. You'll be surprised, I think.\x02\x03",

            "It's a bit like walking into a storm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1004FI, uh, I see!\x02\x03",

            "#1015FSo that kinda makes all this the\x01",
            "'calm before the storm,' then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "#047FYes, after a fashion...\x01",
            "This may be a very brief period of peace\x01",
            "before the 'action' begins.\x02\x03",

            "#040FIf you want to look around the interior,\x01",
            "this may be your only chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1006FI better keep that in mind, then!\x02\x03",

            "Guess I better start wandering around\x01",
            "faster, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        "#040FYes, I'll see you later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A21)
    Jump("loc_3786")

    label("loc_36E4")


    ChrTalk(    #82
        0xA,
        (
            "#040FAs you said, Estelle, this is the calm\x01",
            "before the storm.\x02\x03",

            "If you want to have a look around the\x01",
            "interior of the Arseille, this may be your\x01",
            "only chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3786")

    TalkEnd(0xFE)
    Return()

    # Function_3_EF1 end

    def Function_4_378A(): pass

    label("Function_4_378A")

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
        (0, "loc_37F0"),
        (1, "loc_3BED"),
        (2, "loc_3C2E"),
        (SWITCH_DEFAULT, "loc_3C31"),
    )


    label("loc_37F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9A")

    ChrTalk(    #83
        0x12,
        (
            "#052FOh, you guys.\x02\x03",

            "You still hangin' around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1000FYeah, we were just making sure we're ready.\x02\x03",

            "You look a little out of place up here\x01",
            "yourself, Agate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #85
        0x12,
        (
            "#050FThis's the best place to keep track of\x01",
            "you guys.\x02\x03",

            "The bridge's instruments and stuff let\x01",
            "you check what's goin' on outside the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1028FWhy, is that concern in your voice, Agate?\x01",
            "You're goin' soft on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        "#1040FThanks for your concern, Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        (
            "#050FWell, just don't overdo it.\x01",
            "Remember who the hell you're fightin',\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A2E")

    ChrTalk(    #89
        0x107,
        "#062FW-We will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A68")

    ChrTalk(    #90
        0x103,
        "#022FYes, we'll need to be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A9F")

    ChrTalk(    #91
        0x108,
        "#072FYes, we'll watch ourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3A9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AD3")

    ChrTalk(    #92
        0x105,
        "#042FYes... We should take care.\x02",
    )

    CloseMessageWindow()

    label("loc_3AD3")


    ChrTalk(    #93
        0x101,
        (
            "#1002FAgate, you too... Stay ready.\x02\x03",

            "I don't know when or how we\x01",
            "might need your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        (
            "#051FDon't need to tell me.\x02\x03",

            "Well, good luck out there.\x01",
            "You need me, you know where to find me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E25)
    Jump("loc_3BEA")

    label("loc_3B9A")


    ChrTalk(    #95
        0x12,
        (
            "#050FI'll be watchin' you guys from here.\x02\x03",

            "You need me, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BEA")

    Jump("loc_3C31")

    label("loc_3BED")


    ChrTalk(    #96
        0x12,
        (
            "#050FNeed to change team members?\x01",
            "I'm all set to go.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_3C31")

    label("loc_3C2E")

    Jump("loc_3C31")

    label("loc_3C31")

    TalkEnd(0xFE)
    Return()

    # Function_4_378A end

    def Function_5_3C35(): pass

    label("Function_5_3C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D3B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CD1")
    Jump("loc_3D13")

    label("loc_3CD1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CED")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D13")

    label("loc_3CED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D09")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D13")

    label("loc_3D09")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D13")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_3D3E")

    label("loc_3D3B")

    TalkBegin(0xFE)

    label("loc_3D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_3FCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB0")

    ChrTalk(    #97
        0x10F,
        "#170FAh, everyone. How goes your investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1011FActually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 19)
    Return()

    label("loc_3DB0")

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
        (0, "loc_3E13"),
        (1, "loc_3F5A"),
        (2, "loc_3FC8"),
        (SWITCH_DEFAULT, "loc_3FCB"),
    )


    label("loc_3E13")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED0")

    ChrTalk(    #99
        0xC,
        (
            "#178FWe are beginning our test of the flight\x01",
            "engine.\x02\x03",

            "We shall have the ship ready to fly by\x01",
            "the time you return, Your Highness.\x02\x03",

            "I hope it will meet your expectations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F57")

    label("loc_3ED0")


    ChrTalk(    #100
        0xC,
        (
            "#178FWe are beginning our test of the flight\x01",
            "engine.\x02\x03",

            "We will be ready to fly by the time you\x01",
            "return.\x02\x03",

            "Good luck in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F57")

    Jump("loc_3FCB")

    label("loc_3F5A")


    ChrTalk(    #101
        0xC,
        (
            "#170FYou are altering your team's formation?\x01",
            "Very well. I would be honored to provide\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_3FCB")

    label("loc_3FC8")

    Jump("loc_3FCB")

    label("loc_3FCB")

    Jump("loc_65F7")

    label("loc_3FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_4438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41CB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404D")

    ChrTalk(    #102
        0xC,
        (
            "#170FThe bandit crew seems to be safe.\x02\x03",

            "We just received word from their ship\x01",
            "a moment ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40AD")

    label("loc_404D")


    ChrTalk(    #103
        0xC,
        (
            "#170FSo, you rescued the bandit crew.\x02\x03",

            "We just received word from their ship\x01",
            "a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40AD")


    ChrTalk(    #104
        0x101,
        "#1011FOh, good, you got in touch.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #105
        0xC,
        (
            "#170FYes, it seems they're busy repairing\x01",
            "their own ship.\x02\x03",

            "#176FIf I may be honest, I still cannot entirely\x01",
            "accept the idea of working with them.\x02\x03",

            "But given our situation, it is unavoidable.\x01",
            "I shall obey Her Highness in this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x22AB)
    Jump("loc_4435")

    label("loc_41CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4359")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_429A")

    ChrTalk(    #106
        0xC,
        (
            "#170FThe bandits are busy repairing their own ship.\x02\x03",

            "#176FTo think we'd end up in the same circumstances\x01",
            "in a place like this...\x02\x03",

            "The Goddess possesses a sense of irony,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4356")

    label("loc_429A")


    ChrTalk(    #107
        0xC,
        (
            "#170FThe bandits seem to be busy repairing\x01",
            "their ship.\x02\x03",

            "#176FTo think we'd end up in the same circumstances\x01",
            "in a place like this...\x02\x03",

            "The Goddess possesses a sense of irony,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4356")

    Jump("loc_4435")

    label("loc_4359")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43CC")

    ChrTalk(    #108
        0xC,
        (
            "#170FWe just received word from the bandit ship.\x02\x03",

            "We should ensure they are properly supplied.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4435")

    label("loc_43CC")


    ChrTalk(    #109
        0xC,
        (
            "#170FWe just received word from the bandit ship.\x02\x03",

            "We should check to see if they need any supplies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4435")

    Jump("loc_65F7")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_48AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F6")
    TurnDirection(0xC, 0x10B, 0)

    ChrTalk(    #110
        0xC,
        (
            "#178FHmm... You are Josette Capua, then.\x02\x03",

            "Frankly, normally I would not deign to\x01",
            "cooperate with a base criminal...\x02\x03",

            "Given the circumstances, however, I have no\x01",
            "choice. You are granted special dispensation\x01",
            "to be aboard the ship.\x02\x03",

            "I do, of course, expect you to work to\x01",
            "earn your place aboard this vessel.\x02\x03",

            "Join the rest of the crew and help with\x01",
            "whatever you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10B,
        "#212FUh... y-yeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22AA)
    Jump("loc_46E3")

    label("loc_45F6")

    TurnDirection(0xC, 0x10B, 0)

    ChrTalk(    #112
        0xC,
        (
            "#178FGiven the circumstances, you are granted\x01",
            "special dispensation to be aboard the ship.\x02\x03",

            "I do, of course, expect you to work to\x01",
            "earn your place aboard this vessel.\x02\x03",

            "Join the rest of the crew and help with\x01",
            "whatever you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E3")

    Jump("loc_48A7")

    label("loc_46E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4835")

    ChrTalk(    #113
        0xC,
        (
            "#178FEveryone.\x01",
            "I heard you secured the bandit girl.\x02\x03",

            "#176FFrankly, normally I would not deign to\x01",
            "cooperate with a base criminal...\x02\x03",

            "Given the circumstances, however, I have no\x01",
            "choice. I have granted her special dispensation\x01",
            "to be aboard the ship.\x02\x03",

            "#178FWe cannot...simply throw her back in the\x01",
            "snake pit, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_48A7")

    label("loc_4835")


    ChrTalk(    #114
        0xC,
        (
            "#170FThe bandit girl has special permission\x01",
            "to be aboard the Arseille.\x02\x03",

            "She had best work to earn her place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48A7")

    Jump("loc_65F7")

    label("loc_48AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4CB3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F3")

    ChrTalk(    #115
        0xC,
        (
            "#170FOur biggest problem right now is securing\x01",
            "the resources to even begin repair work...\x02\x03",

            "For the moment, the plan is to collect and\x01",
            "repurpose scrap from across the ship and\x01",
            "the crash site.\x02\x03",

            "It will be a temporary fix, at best, but\x01",
            "we should be able to restore the hull\x01",
            "enough to fly home.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_4A84")

    label("loc_49F3")


    ChrTalk(    #116
        0xC,
        (
            "#170FWe intend to recover scrap from the crash\x01",
            "site and use it to repair the hull.\x02\x03",

            "I have already dispatched a squad on\x01",
            "a salvage mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A84")

    Jump("loc_4CB0")

    label("loc_4A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFD")

    ChrTalk(    #117
        0xC,
        (
            "#178FWe will be using the scraps from the crash\x01",
            "to repair the ship as best we can.\x02\x03",

            "To that end, I've sent out troops to recover\x01",
            "any useful debris they can.\x02\x03",

            "It is not the most efficient plan ever, but\x01",
            "it is the only one that will work, given our\x01",
            "circumstances.\x02\x03",

            "I hate to ask, but if any of your team has\x01",
            "the time, Ms. Bright, help would be\x01",
            "appreciated.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_4CB0")

    label("loc_4BFD")


    ChrTalk(    #118
        0xC,
        (
            "#178FI've sent out my men to recover scrap\x01",
            "from the crash to use in repair work.\x02\x03",

            "I hate to ask, but if any of your team has\x01",
            "the time, Ms. Bright, help would be\x01",
            "appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB0")

    Jump("loc_65F7")

    label("loc_4CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_52F5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F0B")

    ChrTalk(    #119
        0xC,
        (
            "#178FThat girl with the massive scythe awaits\x01",
            "us at the next tower...\x02\x03",

            "She is the one who manipulated Kanone.\x02\x03",

            "#176FFrankly, I would like to venture onto the\x01",
            "field myself to bring down justice upon\x01",
            "her...\x02\x03",

            "I shall, however, leave that in the hands\x01",
            "of Her Highness.\x02\x03",

            "#178FFor the sake of both Her Highness and\x01",
            "Her Majesty the queen, I shall fulfill my\x01",
            "duty here to my utmost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x105,
        (
            "#040FI could never truly replace you, Julia...\x02\x03",

            "We will do everything we can to stop her.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xC, 29)
    SetChrSubChip(0xC, 0)
    OP_99(0xC, 0x0, 0x1, 0x5DC)

    ChrTalk(    #121
        0xC,
        "#172FYour Highness! I wish you the best of luck!\x02",
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x0, 0x5DC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_A2(0x1E48)
    Jump("loc_508C")

    label("loc_4F0B")


    ChrTalk(    #122
        0xC,
        (
            "#178FThat girl with the massive scythe awaits\x01",
            "us at the next tower...\x02\x03",

            "#176FFrankly, I would like to venture onto the\x01",
            "field myself to bring down justice upon\x01",
            "her...\x02\x03",

            "I shall, however, leave that in the hands\x01",
            "of Her Highness.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xC, 29)
    SetChrSubChip(0xC, 0)
    OP_99(0xC, 0x0, 0x1, 0x5DC)

    ChrTalk(    #123
        0xC,
        (
            "#172FFor the sake of both Her Highness and\x01",
            "Her Majesty the Queen, I shall fulfill my\x01",
            "duty here to my utmost.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x0, 0x5DC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_A2(0x8)

    label("loc_508C")

    Jump("loc_52F2")

    label("loc_508F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_520B")

    ChrTalk(    #124
        0xC,
        (
            "#178FThat girl with the massive scythe awaits\x01",
            "us at the next tower...\x02\x03",

            "She is the one who manipulated Kanone.\x02\x03",

            "#176FFrankly, I would like to venture onto the\x01",
            "field myself to bring down justice upon\x01",
            "her...\x02\x03",

            "For now, however, I shall leave things to\x01",
            "you who have been entrusted this mission\x01",
            "by Her Highness.\x02\x03",

            "#178FOur hopes go with you...\x01",
            "Strive to do your best.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_52F2")

    label("loc_520B")


    ChrTalk(    #125
        0xC,
        (
            "#178FFrankly, I would like to venture onto the field\x01",
            "myself to bring down justice upon her...\x02\x03",

            "For now, however, I shall leave things to you\x01",
            "who have been entrusted this mission by Her\x01",
            "Highness. Fortune favor you, Ms. Bright.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F2")

    Jump("loc_65F7")

    label("loc_52F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_557F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C9")

    ChrTalk(    #126
        0xC,
        (
            "#170FThe Ruan Rearguard division has arrived\x01",
            "safely in Manoria.\x02\x03",

            "All the citizens living along the roads\x01",
            "have been safely evacuated...\x02\x03",

            "We've avoided one disaster, at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_5448")

    label("loc_53C9")


    ChrTalk(    #127
        0xC,
        (
            "#170FThe Ruan Rearguard has arrived safely\x01",
            "in Manoria with the outlying civilians.\x02\x03",

            "We've avoided one disaster, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5448")

    Jump("loc_557C")

    label("loc_544B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5510")

    ChrTalk(    #128
        0xC,
        (
            "#170FThe Ruan Rearguard division has arrived\x01",
            "safely in Manoria.\x02\x03",

            "According to reports, they evacuated all\x01",
            "civilians living near the roads.\x02\x03",

            "We've avoided one disaster, at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_557C")

    label("loc_5510")


    ChrTalk(    #129
        0xC,
        (
            "#170FThe Ruan Rearguard division has arrived\x01",
            "safely in Manoria.\x02\x03",

            "We've avoided one disaster, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557C")

    Jump("loc_65F7")

    label("loc_557F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_59D6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56DA")

    ChrTalk(    #130
        0xC,
        (
            "#178FThe Zeiss Guard is engaged in heavy\x01",
            "combat on the outskirts of the city.\x02\x03",

            "Never fear, though. Every one of those men has\x01",
            "sworn on the honor of the Royal Army to defend\x01",
            "the city to their last breath.\x02\x03",

            "Please, Your Highness, focus your efforts\x01",
            "on the investigation of the tower.\x01",
            "We will defend your realm.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_57BF")

    label("loc_56DA")


    ChrTalk(    #131
        0xC,
        (
            "#178FEvery one of those men in Zeiss has sworn\x01",
            "on the honor of the Royal Army to defend the\x01",
            "city to their last breath.\x02\x03",

            "Please, Your Highness, focus your efforts\x01",
            "on the investigation of the tower.\x01",
            "We will defend your realm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57BF")

    Jump("loc_59D3")

    label("loc_57C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58FC")

    ChrTalk(    #132
        0xC,
        (
            "#178FThe Zeiss Guard is engaged in heavy\x01",
            "combat on the outskirts of the city.\x02\x03",

            "Never fear, though. Every one of those men has\x01",
            "sworn on the honor of the Royal Army to defend\x01",
            "the city to their last breath.\x02\x03",

            "The best thing you can do to help now is to\x01",
            "investigate the tower as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_59D3")

    label("loc_58FC")


    ChrTalk(    #133
        0xC,
        (
            "#178FEvery one of those men in Zeiss has sworn\x01",
            "on the honor of the Royal Army to defend the\x01",
            "city to their last breath.\x02\x03",

            "The best thing you can do to help now is to\x01",
            "investigate the tower as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59D3")

    Jump("loc_65F7")

    label("loc_59D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_5D98")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B8E")

    ChrTalk(    #134
        0xC,
        (
            "#170FI'm sure I need not explain to Your Highness,\x01",
            "but to disembark, use the cargo lift in the\x01",
            "storeroom.\x02\x03",

            "I've assigned a crewman to operate the\x01",
            "lift so that you may use it at any time.\x02\x03",

            "Our enemies are extremely capable.\x01",
            "Please proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x105,
        (
            "#040FThank you, Julia.\x02\x03",

            "Take care of the Arseille while I'm away.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xC, 29)
    SetChrSubChip(0xC, 0)
    OP_99(0xC, 0x0, 0x1, 0x5DC)

    ChrTalk(    #136
        0xC,
        "#172FYes, Your Highness! Of course!\x02",
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x0, 0x5DC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_A2(0x1E47)
    Jump("loc_5C0F")

    label("loc_5B8E")


    ChrTalk(    #137
        0xC,
        (
            "#170FYou may disembark by using the cargo\x01",
            "lift in the storeroom.\x02\x03",

            "Well, then, Your Highness.\x01",
            "Please, take care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C0F")

    Jump("loc_5D95")

    label("loc_5C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFE")

    ChrTalk(    #138
        0xC,
        (
            "#170FYou may disembark by using the cargo\x01",
            "lift in the storeroom.\x02\x03",

            "I've assigned a crewman to operate the\x01",
            "lift so that you may use it at any time.\x02\x03",

            "I expect good news from your fight.\x01",
            "The Goddess' fortune be with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_5D95")

    label("loc_5CFE")


    ChrTalk(    #139
        0xC,
        (
            "#170FYou may disembark by using the cargo\x01",
            "lift in the storeroom.\x02\x03",

            "I've assigned a crewman to operate the\x01",
            "lift so that you may use it at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D95")

    Jump("loc_65F7")

    label("loc_5D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_65F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D4")

    ChrTalk(    #140
        0xC,
        (
            "#170FMs. Bright! Good day.\x02\x03",

            "How do you find the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1001FIt's really, really cool!\x02\x03",

            "I guess I shouldn't be surprised the\x01",
            "queen's ship is awesome, but still!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xC,
        (
            "#171FThank you for your kindness, Ms. Bright.\x02\x03",

            "I am simply relieved the new engine\x01",
            "made it in time.\x02\x03",

            "#176FOf course, I hardly expected to use\x01",
            "it on a mission of quite this...nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1007FI hear that...\x02\x03",

            "Who'd imagine a dragon would show up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        (
            "#178FYes, it is an utter mystery as a foe,\x01",
            "even to us.\x02\x03",

            "We may have a plan of attack, but it would\x01",
            "be foolish to rely completely on it in the face\x01",
            "of the unknown.\x02\x03",

            "Be prepared for anything, in case something\x01",
            "goes...amiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1015FIf anything happens, it'll all be up to us,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xC,
        (
            "#175FHopefully it will not come to that...\x02\x03",

            "But only Aidios knows what lies before us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A6D)
    Jump("loc_65F7")

    label("loc_60D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 0)), scpexpr(EXPR_END)), "loc_653C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6496")

    ChrTalk(    #147
        0x101,
        (
            "#1011FOh, by the way, Julia.\x02\x03",

            "Did you know that Nial, uh, Mr. Nial Burns,\x01",
            "wants to cover you for an article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xC,
        "#173FAn article...? About me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1006FYeah, he wants the citizens to know\x01",
            "the real Royal Guard, he says.\x02\x03",

            "He's pretty serious about his job,\x01",
            "so I think you can trust him, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xC,
        (
            "#176FI am well aware of Mr. Burns' professional\x01",
            "credentials.\x02\x03",

            "If not, I would not have allowed him to\x01",
            "accompany us and cover this story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1015FOh, yeah, good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xC,
        (
            "#175FTo be honest, I absolutely support the\x01",
            "idea behind such an article...\x02\x03",

            "However, I am afraid I must decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1004FHuh? Even if you support it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xC,
        (
            "#176FWe have refused similar proposals from\x01",
            "other companies as well, you see.\x02\x03",

            "We cannot give the Liberl News any\x01",
            "special treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#1007FAwwww... I guess not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xC,
        (
            "#170FForgive me, but please tell him as much.\x02\x03",

            "I still look forward to seeing the article,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#1015FOkay, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x1A6E)
    Jump("loc_6539")

    label("loc_6496")


    ChrTalk(    #158
        0xC,
        (
            "#176FUnfortunately, it would be difficult for\x01",
            "us to agree to the Liberl News' request.\x02\x03",

            "While I like the idea of the article,\x01",
            "we have to be fair to everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6539")

    Jump("loc_65F7")

    label("loc_653C")


    ChrTalk(    #159
        0xC,
        (
            "#170FAs soon as the dragon is sighted,\x01",
            "we will begin operations.\x02\x03",

            "We shall do our best, but we don't\x01",
            "know what will happen.\x02\x03",

            "Ms. Bright. Please make sure you are\x01",
            "ready for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_660E")
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Jump("loc_6611")

    label("loc_660E")

    TalkEnd(0xFE)

    label("loc_6611")

    Return()

    # Function_5_3C35 end

    def Function_6_6612(): pass

    label("Function_6_6612")

    TalkBegin(0xFE)

    ChrTalk(    #160
        0xFE,
        "#030F◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    # Function_6_6612 end

    def Function_7_6636(): pass

    label("Function_7_6636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_66AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_END)), "loc_6668")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    Jump("loc_66AA")

    label("loc_6668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_668F")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_66AA")

    label("loc_668F")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_66AA")

    Jump("loc_672B")

    label("loc_66AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_66D0")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_672B")

    label("loc_66D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_66F1")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_672B")

    label("loc_66F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_6712")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_672B")

    label("loc_6712")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_672B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6762")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_6762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_6875")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6791")
    SetChrChipByIndex(0xA, 20)
    SetChrPos(0xA, -910, 2000, 89640, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_6791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_END)), "loc_6800")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67D1")
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xC, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)

    label("loc_67D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6800")
    SetChrChipByIndex(0x15, 24)
    SetChrPos(0x15, 130, 2000, 91480, 0)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x2)

    label("loc_6800")

    Jump("loc_6872")

    label("loc_6803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_683E")
    OP_8C(0xA, 45, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_683B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_683B")

    Jump("loc_6872")

    label("loc_683E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_6872")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_686F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_686F")

    Jump("loc_6872")

    label("loc_6872")

    Jump("loc_6932")

    label("loc_6875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_68A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_689F")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_689F")

    Jump("loc_6932")

    label("loc_68A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_68CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68CC")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_68CC")

    Jump("loc_6932")

    label("loc_68CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_68FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68F9")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_68F9")

    Jump("loc_6932")

    label("loc_68FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_6932")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6932")
    SetChrPos(0x12, 770, 2000, 89910, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 28)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_6932")

    OP_0D()
    Return()

    # Function_7_6636 end

    def Function_8_6934(): pass

    label("Function_8_6934")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6958")
    OP_10(0x0, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0x7, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0xA, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    Jump("loc_69B0")

    label("loc_6958")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697C")
    OP_10(0x9, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0xA, 0x0)
    OP_10(0x8, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_69B0")

    label("loc_697C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_699B")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0xB, 0x1)
    OP_10(0xA, 0x1)
    OP_10(0x8, 0x0)
    OP_10(0x1, 0x0)
    Jump("loc_69B0")

    label("loc_699B")

    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x9, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x0)
    OP_10(0xA, 0x1)

    label("loc_69B0")

    Return()

    # Function_8_6934 end

    def Function_9_69B1(): pass

    label("Function_9_69B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_69F3")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    Jump("loc_6A5E")

    label("loc_69F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_6A24")
    OP_B1("E0310_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_72(0xF, 0x4)
    Jump("loc_6A5E")

    label("loc_6A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 7)), scpexpr(EXPR_END)), "loc_6A3C")
    OP_B1("E0310_2")
    OP_71(0x19, 0x4)
    Jump("loc_6A5E")

    label("loc_6A3C")

    OP_B1("E0310_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)

    label("loc_6A5E")

    Jump("loc_6C0A")

    label("loc_6A61")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_END)), "loc_6A9E")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_72(0xE, 0x4)
    Jump("loc_6B74")

    label("loc_6A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_6AC5")
    OP_B1("E0310_4")
    OP_71(0xD, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x14, 0x4)
    Jump("loc_6B74")

    label("loc_6AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_6AEC")
    OP_B1("E0310_4")
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    Jump("loc_6B74")

    label("loc_6AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 7)), scpexpr(EXPR_END)), "loc_6B1D")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    Jump("loc_6B74")

    label("loc_6B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_6B44")
    OP_B1("E0310_4")
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x14, 0x4)
    Jump("loc_6B74")

    label("loc_6B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 0)), scpexpr(EXPR_END)), "loc_6B6B")
    OP_B1("E0310_4")
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x14, 0x4)
    Jump("loc_6B74")

    label("loc_6B6B")

    OP_B1("E0310_3")

    label("loc_6B74")

    Jump("loc_6C0A")

    label("loc_6B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_6BA3")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    Jump("loc_6C0A")

    label("loc_6BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BE3")
    OP_B1("E0310_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    Jump("loc_6C0A")

    label("loc_6BE3")

    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)

    label("loc_6C0A")

    Return()

    # Function_9_69B1 end

    def Function_10_6C0B(): pass

    label("Function_10_6C0B")

    EventBegin(0x0)
    OP_22(0xAB, 0x1, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Captain Schwarz")

    AnonymousTalk(    #161
        (
            "\x07\x05Signal from the Melder!\x02\x03",

            "Dragon in flight in airspace above\x01",
            "the Malga Mine!\x02\x03",

            "All crew to battle stations!\x01",
            "All crew to battle stations!\x02\x03",

            "Guild observers, report to the bridge!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #162
        0x101,
        "#1005FHere we go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_6C0B end

    def Function_11_6D3B(): pass

    label("Function_11_6D3B")

    EventBegin(0x0)
    OP_6D(-470, 2000, 93430, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(300)
    OP_43(0x101, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x8, 0x0, 0x0, 0xD)
    Sleep(500)
    OP_43(0x9, 0x0, 0x0, 0xF)
    Sleep(500)
    OP_43(0xB, 0x0, 0x0, 0xE)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #163
        0x101,
        "#1005F#2PWhat's happening?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 225, 400)
    OP_8C(0xA, 180, 400)

    ChrTalk(    #164
        0xD,
        (
            "#160F#6PThe dragon is above the Malga Mine.\x02\x03",

            "Look at the display.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EA1():
        OP_6D(720, 2000, 95220, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EA1)

    def lambda_6EB9():
        OP_67(0, 5150, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6EB9)
    OP_8C(0xD, 45, 400)

    def lambda_6ED8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6ED8)
    Sleep(50)

    def lambda_6EEB():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6EEB)
    Sleep(50)

    def lambda_6EFE():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6EFE)
    Sleep(50)

    def lambda_6F11():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6F11)
    Sleep(50)

    def lambda_6F24():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F24)
    WaitChrThread(0x101, 0x2)
    OP_6F(0xC, 1)
    OP_70(0xC, 0x3C)
    Sleep(150)
    OP_22(0x127, 0x0, 0x64)
    OP_73(0xC)
    OP_22(0x9D, 0x0, 0x64)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x1)
    OP_74(0xC, 0x8, 0x1)
    OP_74(0xC, 0xA, 0x1)
    OP_0D()
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_AD(0x24010E, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #165
        "\x07\x00#1002FMalga... So it's in Rolent!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #166
        "\x07\x00#022FI'm amazed we found it...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #167
        0xC,
        "#178F#5PWhere shall we intercept it, sir?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(400)

    ChrTalk(    #168
        0xD,
        (
            "#163F#2PA good question.\x02\x03",

            "We need to lure it to the lake, but we cannot\x01",
            "afford to let it near the capital.\x02\x03",

            "#160F...Our interception point will be near the\x01",
            "Lenhardt River estuary!\x02\x03",

            "Patrol ships! Lure the dragon to the riverside!\x02\x03",

            "Attack ships, forward!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xC,
        "#170F#5PAye, sir!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(400)

    ChrTalk(    #170
        0xC,
        (
            "#176F#5PThis is the Arseille to all ships.\x02\x03",

            "#178FOur interception point will be the\x01",
            "Lenhardt River estuary.\x02\x03",

            "All patrol ships, lead the dragon to\x01",
            "the interception point.\x01",
            "Use formation B!\x02\x03",

            "Attack ships, launch and proceed to\x01",
            "the interception point!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3108   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_6D3B end

    def Function_12_72D6(): pass

    label("Function_12_72D6")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_72FD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72FD)
    OP_8E(0xFE, 0xFFFFFB6E, 0x7D0, 0x1659E, 0x1388, 0x0)
    Return()

    # Function_12_72D6 end

    def Function_13_731E(): pass

    label("Function_13_731E")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7345():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7345)
    OP_8E(0xFE, 0xFFFFF6AA, 0x7D0, 0x163AA, 0x1388, 0x0)
    Return()

    # Function_13_731E end

    def Function_14_7366(): pass

    label("Function_14_7366")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_738D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_738D)
    OP_8E(0xFE, 0xFFFFF9B6, 0x7D0, 0x15EC8, 0x1388, 0x0)
    Return()

    # Function_14_7366 end

    def Function_15_73AE(): pass

    label("Function_15_73AE")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_73D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_73D5)
    OP_8E(0xFE, 0xFFFFFF4C, 0x7D0, 0x1630A, 0x1388, 0x0)
    Return()

    # Function_15_73AE end

    def Function_16_73F6(): pass

    label("Function_16_73F6")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToDark(0, 0, -1)
    OP_AD(0x24010F, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #171
        0xC,
        (
            "#178F#5PAll attack ships have launched.\x02\x03",

            "Estimate their arrival at 1220 hours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xD,
        (
            "#163F#2PHmmm...\x02\x03",

            "#160FFull speed ahead!\x01",
            "Put us southwest of the interception point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xC,
        "#170F#5PAye, sir.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(400)

    ChrTalk(    #174
        0xC,
        (
            "#178F#5PRestore orbal power flow to all sections!\x02\x03",

            "Ahead full! Helm, take us to the southwest\x01",
            "of the Lenhardt River estuary!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS219._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS230._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS231._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS232._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_73F6 end

    def Function_17_7872(): pass

    label("Function_17_7872")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #175
        0xC,
        (
            "#170F#5PAll attack ships have arrived at their\x01",
            "designated positions.\x02\x03",

            "Tranquilizer rounds loaded and ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xD,
        (
            "#163F#2PAll right. All that's left is to wait for\x01",
            "the dragon to show up.\x02\x03",

            "#160FAll attack ships, prepare to fire.\x01",
            "Begin attack on my command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xC,
        "#178F#5PAye, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#1002F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        "#042F#5PAnd it begins...\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS233._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS234._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS235._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_7872 end

    def Function_18_7C1F(): pass

    label("Function_18_7C1F")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)

    def lambda_7D2D():
        OP_6B(3300, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D2D)
    OP_0D()
    Sleep(500)

    ChrTalk(    #180
        0xD,
        "#162F#2P#5SAll ships! FIRE!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_7C1F end

    def Function_19_7D87(): pass

    label("Function_19_7D87")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #181
        0xD,
        "#164F#2PHa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1018F#5PI think we got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "#020F#5PAbsolutely incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xB,
        (
            "#071F#2PHah, not even a dragon could stand\x01",
            "up against this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        (
            "#031FMy goodness...such spectacle.\x01",
            "What a performance.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #186
        0xC,
        (
            "#170F#5PConfirming splashdown of dragon into\x01",
            "Lake Valleria!\x02\x03",

            "Shall we proceed as planned and bind it,\x01",
            "sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xD,
        (
            "#163F#2PProceed.\x02\x03",

            "#160FAs soon as you've confirmed it safe,\x01",
            "bring the Arseille down.\x02\x03",

            "We'll perform a water landing and\x01",
            "inspect the dragon ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xC,
        "#171F#5PAye, sir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_23(0x7A)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_7D87 end

    def Function_20_80AA(): pass

    label("Function_20_80AA")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_23(0x7A)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_72(0x9, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #189
        0xC,
        (
            "#176F#5PWater landing complete.\x02\x03",

            "#178FNo response from the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xD,
        (
            "#163F#2PRight, then...time to see this\x01",
            "with my own eyes.\x02\x03",

            "#160FCaptain, accompany me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #191
        0xC,
        "#172F#5PSir!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -1050, 2000, 94150, 0)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_0D()
    Sleep(200)

    def lambda_82AF():
        OP_6D(-340, 2000, 90490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_82AF)

    def lambda_82C7():
        OP_6C(36000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_82C7)

    def lambda_82D7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_82D7)
    Sleep(70)

    def lambda_82EA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_82EA)
    Sleep(70)

    def lambda_82FD():

        label("loc_82FD")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_82FD")

    QueueWorkItem2(0x101, 2, lambda_82FD)

    def lambda_830E():

        label("loc_830E")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_830E")

    QueueWorkItem2(0x9, 2, lambda_830E)
    Sleep(70)

    def lambda_8324():

        label("loc_8324")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_8324")

    QueueWorkItem2(0x8, 2, lambda_8324)
    Sleep(80)

    def lambda_833A():

        label("loc_833A")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_833A")

    QueueWorkItem2(0xB, 2, lambda_833A)
    Sleep(70)

    def lambda_8350():

        label("loc_8350")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_8350")

    QueueWorkItem2(0xA, 2, lambda_8350)

    def lambda_8361():
        OP_8F(0xFE, 0x294, 0x7D0, 0x15FEA, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8361)
    OP_43(0xD, 0x0, 0x0, 0x16)
    OP_43(0xC, 0x0, 0x0, 0x15)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    def lambda_8394():

        label("loc_8394")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_8394")

    QueueWorkItem2(0x9, 2, lambda_8394)
    Sleep(2300)

    ChrTalk(    #192
        0x101,
        "#1004F#6PUm, can we...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x0)
    TurnDirection(0xC, 0x101, 400)
    Sleep(500)

    ChrTalk(    #193
        0xC,
        (
            "#171FYes, you should come, too.\x02\x03",

            "This is an ancient dragon of legend.\x01",
            "Not exactly something you'll get to see\x01",
            "every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        "#1008F#6PYeah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    AddParty(0x7, 0xFA, 0xFF)
    OP_6D(-890, 2000, 88540, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -890, 2000, 88540, 180)
    SetChrPos(0x105, -890, 2000, 88540, 180)
    SetChrPos(0x103, -890, 2000, 88540, 180)
    SetChrPos(0x104, -890, 2000, 88540, 180)
    SetChrPos(0x108, -890, 2000, 88540, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1A23)
    OP_28(0x95, 0x1, 0x20)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_20_80AA end

    def Function_21_854F(): pass

    label("Function_21_854F")

    Sleep(800)
    OP_8E(0xFE, 0xFFFFFF1A, 0x7D0, 0x16E04, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFE5C, 0x7D0, 0x15D2E, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFD12, 0x7D0, 0x1564E, 0x7D0, 0x0)
    Return()

    # Function_21_854F end

    def Function_22_8591(): pass

    label("Function_22_8591")

    OP_8E(0xFE, 0xFFFFFE5C, 0x7D0, 0x15D2E, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFBB4, 0x7D0, 0x1480C, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFC36, 0x7D0, 0x1451E, 0x7D0, 0x0)

    def lambda_85D3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_85D3)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_8591 end

    def Function_23_85EA(): pass

    label("Function_23_85EA")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_D2(0x270009, 0x27000D, 0x1D)
    OP_D2(0x70025, 0x7002D, 0x1E)
    OP_D2(0x70035, 0x7003D, 0x1F)
    OP_D2(0x70045, 0x7004D, 0x20)
    OP_D2(0x70075, 0x7007D, 0x21)
    OP_22(0x7A, 0x1, 0x50)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x103, -2390, 2000, 91050, 0)
    SetChrPos(0x108, -1610, 2000, 89800, 0)
    SetChrPos(0x104, -180, 2000, 90890, 0)
    SetChrPos(0x105, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrName("Helmsman Lux")

    ChrTalk(    #195
        0xE,
        (
            "#5PNo good! Guided missiles can't\x01",
            "get a lock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xE,
        (
            "#5PDamn it all, we can see the heat signature\x01",
            "right there, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xC,
        (
            "#176F#2PIt must be jamming our missiles\x01",
            "somehow...\x02\x03",

            "#177FAll right, then! Give it a taste\x01",
            "of the main guns!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrName("Sensor Operator Echo")

    ChrTalk(    #198
        0xF,
        "#2PThe target is increasing speed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xF,
        "#2P2300 selge per hour...2400...2500, 2600...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xD,
        (
            "#162F#2PTch. What a monster.\x02\x03",

            "None of the patrol ships will\x01",
            "be able to pursue it...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(300)

    ChrTalk(    #201
        0xC,
        (
            "#172F#5PThe Arseille's engine can\x01",
            "keep up with that!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #202
        0xC,
        (
            "#176F#2PAll hands!\x02\x03",

            "#177FWe will now accelerate to\x01",
            "flank combat speed! 3,200 SPH!\x02\x03",

            "All hands, brace for g-force shock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#1020FWh-What does THAT mean?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 600)

    ChrTalk(    #204
        0x105,
        (
            "#046F#5PThe massive acceleration and thrust will\x01",
            "feel like it makes us heavier!\x02\x03",

            "Crouch down and brace yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#1002FOkay!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 600)
    Fade(500)
    SetChrChipByIndex(0x105, 32)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x101, 29)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x103, 30)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x104, 31)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x108, 33)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0xD, 6)
    SetChrSubChip(0xD, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #206
        0xC,
        (
            "#177F#2PFlank speed, ENGAGE!\x01",
            "DO NOT LET IT ESCAPE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xE,
        "#5PAye, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_22(0x129, 0x1, 0x46)
    Sleep(200)
    OP_24(0x129, 0x50)
    Sleep(200)
    OP_24(0x129, 0x5A)
    Sleep(200)
    OP_24(0x129, 0x64)
    Sleep(500)

    def lambda_8B57():

        label("loc_8B57")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_8B57")

    QueueWorkItem2(0x101, 3, lambda_8B57)
    Fade(500)
    OP_71(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    Sleep(1000)

    ChrTalk(    #208
        0x101,
        "#1021FWAAAAAAAAAAHHHHH!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_8BB6():
        OP_6D(-2040, 2000, 69140, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8BB6)

    def lambda_8BCE():
        OP_67(0, 7960, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8BCE)
    Sleep(1000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_85EA end

    def Function_24_8C02(): pass

    label("Function_24_8C02")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x103, -2390, 2000, 91050, 0)
    SetChrPos(0x108, -1610, 2000, 89800, 0)
    SetChrPos(0x104, -180, 2000, 90890, 0)
    SetChrPos(0x105, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_D2(0x270009, 0x27000D, 0x1D)
    OP_D2(0x70025, 0x7002D, 0x1E)
    OP_D2(0x70035, 0x7003D, 0x1F)
    OP_D2(0x70045, 0x7004D, 0x20)
    OP_D2(0x70075, 0x7007D, 0x21)
    SetChrChipByIndex(0x101, 29)
    SetChrChipByIndex(0x103, 30)
    SetChrChipByIndex(0x104, 31)
    SetChrChipByIndex(0x108, 33)
    SetChrChipByIndex(0xD, 6)
    SetChrChipByIndex(0x105, 32)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x104, 0)
    SetChrSubChip(0x108, 0)
    SetChrSubChip(0xD, 0)
    OP_22(0x7A, 0x1, 0x50)
    OP_22(0x129, 0x1, 0x64)

    def lambda_8D52():

        label("loc_8D52")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_8D52")

    QueueWorkItem2(0x101, 3, lambda_8D52)
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_72(0xD, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #209
        0xF,
        "#2PDragon is descending.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xF,
        "#2PAt this rate, we'll lose visual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xC,
        (
            "#177F#2PKeep going! Do not lose it!\x02\x03",

            "#175FTch! How can we still be in a cloud?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x103,
        "#024F#5PWait! Where is this?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(400)

    ChrTalk(    #213
        0xC,
        "#173F#2PWhat do you--\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240120, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(160, 220, -1, -1)
    SetChrName("Captain Schwarz")

    AnonymousTalk(    #214
        "\x07\x00#172FThe Nebel Valley...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #215
        "\x07\x00#1020FCould we already be in the mist?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #216
        "\x07\x00#162FHmmmm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #217
        0xF,
        "#2PDragon has descended to 1200 arge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xF,
        "#2P1100, 1000, 900...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xF,
        "#2PDragon...lost, ma'am.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(400)

    ChrTalk(    #220
        0xC,
        "#175F#5PTch!...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x105,
        "#043F#5PJulia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1015FSo we lost sight of it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xC,
        (
            "#176F#5P...We did.\x02\x03",

            "#175FThe northwestern part of the Nebel Valley...\x01",
            "the place where the fog is deepest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xD,
        "#160F#2PCan we dock the Arseille in that old fort?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 2)

    ChrTalk(    #225
        0xC,
        "#175F#5PNo, the Arseille is too large.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xD,
        (
            "#163F#2PI see.\x02\x03",

            "#160FThe operation is over, then.\x02\x03",

            "All operation ships are to patrol\x01",
            "the Nebel Valley region.\x02\x03",

            "#163FThe Arseille will return to Bose.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x7A)
    OP_23(0x129)
    Sleep(1000)
    OP_A2(0x1A24)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_8C02 end

    def Function_25_91FA(): pass

    label("Function_25_91FA")

    EventBegin(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x8, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_6D(490, 2000, 88600, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(287, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0xC, -250, 2000, 92100, 270)
    SetChrPos(0x11, -1630, 2000, 92100, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x4)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_92BE():

        label("loc_92BE")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_92BE")

    QueueWorkItem2(0xC, 1, lambda_92BE)
    Sleep(100)

    def lambda_92D4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_92D4)
    Sleep(400)

    def lambda_92E7():
        OP_6D(190, 2000, 92150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_92E7)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(300)
    OP_43(0x102, 0x1, 0x0, 0x1B)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x1C)
    Sleep(300)
    OP_43(0xA, 0x1, 0x0, 0x1D)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x1E)
    Sleep(300)
    OP_43(0x12, 0x1, 0x0, 0x1F)
    Sleep(300)
    OP_43(0x14, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0xB, 0x1, 0x0, 0x21)
    WaitChrThread(0x101, 0x1)
    OP_44(0xC, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #227
        0x101,
        "#1004FHey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x13,
        "#064F#2PGrandpa?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x11,
        (
            "#101F#6PHello again, friends!\x02\x03",

            "#100FTita, have you been a good girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x13,
        "#067F#2PHeehee! Yep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x12,
        (
            "#051FBack up a sec, Gramps.\x01",
            "Why're you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x11,
        (
            "#104F#6PWell, as you MAY have noticed,\x01",
            "a fair bit's going on. They brought\x01",
            "me on board a few days ago.\x02\x03",

            "#100FFar more importantly...\x01",
            "Estelle, Joshua!\x02\x03",

            "It does an old man's heart good\x01",
            "to see you two back safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1016FHahaha... Yeah, we managed it,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x102,
        (
            "#1035F#2PI'm sincerely sorry to have\x01",
            "worried you, Professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x11,
        (
            "#101F#6PNo, no, my boy. If you're back safe,\x01",
            "that's what matters.\x02\x03",

            "#102FSo, the business at hand is the Tetracyclic\x01",
            "Towers and that strangeness atop them.\x02\x03",

            "Looks like I'll have to throw this old\x01",
            "back back into another mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#1006FThanks, Professor.\x02\x03",

            "#1015FI was wondering, too. Do you\x01",
            "have any suggestions for which\x01",
            "tower we should start with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x102,
        (
            "#1043F#2PThat's a good question. The closest\x01",
            "are the Amberl and Carnelia Towers,\x01",
            "but really, they're all the same now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xC,
        (
            "#176FWith the Arseille's speed, the\x01",
            "distance doesn't really matter.\x02\x03",

            "#178FMy advice would be to prioritize\x01",
            "targets where we have solid\x01",
            "information on our enemies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1004FInformation? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xC,
        (
            "#178FWe received an update from the scout\x01",
            "unit dispatched to Esmelas Tower.\x02\x03",

            "A masked man in formal, white\x01",
            "clothing appeared there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #241
        0x101,
        "#1005FThat must be that 'Phantom Thief' guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xA,
        (
            "#043FBut what we heard back in the castle...\x01",
            "To be defeated by one man...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99F6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as chose Agate during Chapter 1\x01",           # 0
            "Set as chose Scherazard during Chapter 1\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_99EA"),
        (1, "loc_99F0"),
        (SWITCH_DEFAULT, "loc_99F6"),
    )


    label("loc_99EA")

    OP_A2(0x1201)
    Jump("loc_99F6")

    label("loc_99F0")

    OP_A3(0x1200)
    Jump("loc_99F6")

    label("loc_99F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9A41")

    ChrTalk(    #243
        0x12,
        (
            "#057FHmph. Guess he isn't just\x01",
            "some opera clown, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A87")

    label("loc_9A41")


    ChrTalk(    #244
        0x8,
        (
            "#022FSeems he has the skill to back\x01",
            "up all that bragging he did.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A87")


    ChrTalk(    #245
        0x102,
        (
            "#1035FBleublanc, the Phantom Thief...\x02\x03",

            "#1042FHis specialty as an Enforcer is in trickery;\x01",
            "false image copies, shadow pinning, that\x01",
            "sort of thing.\x02\x03",

            "Fighting him is going to be\x01",
            "like fighting a riddle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#1007FThat sounds ducky.\x02\x03",

            "#1015FStill, just knowing who the enemy is will\x01",
            "make it easier than any other tower.\x02\x03",

            "#1006FOkay! Let's head to Esmelas Tower first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xC,
        "#170FAs you wish.\x02",
    )

    CloseMessageWindow()

    def lambda_9C14():
        OP_6D(310, 2000, 95070, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9C14)

    def lambda_9C2C():
        OP_67(0, 4710, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C2C)

    def lambda_9C44():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9C44)
    Sleep(800)
    OP_8C(0x11, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #248
        0xC,
        (
            "#172F#2PEngines full ahead!\x02\x03",

            "Set course for Esmelas Tower\x01",
            "in the Rolent region!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E00)
    OP_BB(0x1, 0x0, 0x200033)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_91FA end

    def Function_26_9CD4(): pass

    label("Function_26_9CD4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9CFB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CFB)
    OP_8F(0xFE, 0xFFFFFE70, 0x7E4, 0x161E8, 0xBB8, 0x0)
    Return()

    # Function_26_9CD4 end

    def Function_27_9D1C(): pass

    label("Function_27_9D1C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9D43():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D43)
    OP_8F(0xFE, 0xFFFFFA74, 0x7E4, 0x161E8, 0xBB8, 0x0)
    Return()

    # Function_27_9D1C end

    def Function_28_9D64(): pass

    label("Function_28_9D64")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9D8B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D8B)
    OP_8F(0xFE, 0xFFFFF5A6, 0x7D0, 0x15E64, 0xBB8, 0x0)
    Return()

    # Function_28_9D64 end

    def Function_29_9DAC(): pass

    label("Function_29_9DAC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9DD3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9DD3)
    OP_8F(0xFE, 0x64, 0x7D0, 0x15EC8, 0xBB8, 0x0)
    Return()

    # Function_29_9DAC end

    def Function_30_9DF4(): pass

    label("Function_30_9DF4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9E1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9E1B)
    OP_8F(0xFE, 0xFFFFF9C0, 0x7D0, 0x15C70, 0xBB8, 0x0)
    Return()

    # Function_30_9DF4 end

    def Function_31_9E3C(): pass

    label("Function_31_9E3C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9E63():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9E63)
    OP_8F(0xFE, 0xFFFFF650, 0x7D0, 0x157C0, 0xBB8, 0x0)
    Return()

    # Function_31_9E3C end

    def Function_32_9E84(): pass

    label("Function_32_9E84")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9EAB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9EAB)
    OP_8F(0xFE, 0xFFFFFBA0, 0x7D0, 0x158EC, 0xBB8, 0x0)
    Return()

    # Function_32_9E84 end

    def Function_33_9ECC(): pass

    label("Function_33_9ECC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9EF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9EF3)
    OP_8F(0xFE, 0xFFFFFDB2, 0x7D0, 0x15694, 0xBB8, 0x0)
    Return()

    # Function_33_9ECC end

    def Function_34_9F14(): pass

    label("Function_34_9F14")

    EventBegin(0x0)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2400, 2000, 91710, 0)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_22(0x7A, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #249
        0xC,
        "#176F#2PWe've arrived at Esmelas Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        (
            "#1004FWhoa, that was seriously fast.\x02\x03",

            "That wasn't even thirty minutes, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x13,
        (
            "#061F#5PHeehee, that's about right, yeah.\x02\x03",

            "#560FWe were about three times as fast\x01",
            "as a big passenger airship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        "#1006FThe engine, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x102,
        "#1042F#2PWhat's happening on top of the tower?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xC,
        "#178F#2PLet me put it on the display.\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)

    def lambda_A247():
        OP_67(0, 5150, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A247)
    OP_72(0x13, 0x4)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x3C)
    SetChrSubChip(0xC, 2)
    Sleep(100)

    def lambda_A27C():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A27C)

    def lambda_A28A():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A28A)
    Sleep(50)
    OP_22(0x127, 0x0, 0x64)

    def lambda_A2A2():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2A2)

    def lambda_A2B0():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A2B0)
    Sleep(50)

    def lambda_A2C3():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A2C3)
    OP_73(0x13)
    WaitChrThread(0x101, 0x0)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0x13, 0x6, 0x2)
    OP_74(0x13, 0x8, 0x2)
    OP_74(0x13, 0xA, 0x2)
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0706   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_9F14 end

    def Function_35_A31B(): pass

    label("Function_35_A31B")

    EventBegin(0x0)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x13, 0x4)
    OP_6F(0x13, 60)
    OP_74(0x13, 0x6, 0x2)
    OP_74(0x13, 0x8, 0x2)
    OP_74(0x13, 0xA, 0x2)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2400, 2000, 91710, 0)
    OP_4A(0xA, 255)

    def lambda_A44C():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A44C)

    def lambda_A45A():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A45A)

    def lambda_A468():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A468)

    def lambda_A476():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A476)

    def lambda_A484():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A484)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_22(0x7A, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x102, 0, 400)
    Sleep(500)

    ChrTalk(    #255
        0x102,
        (
            "#1042F#2PJulia.\x02\x03",

            "How will we get to the surface?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xC,
        (
            "#176F#5PUnfortunately, the terrain is too\x01",
            "rough to land the Arseille.\x02\x03",

            "#178FWe should be able to get close enough\x01",
            "to lower the lift while hovering. Use that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #257
        0x101,
        "#1004FThe 'lift'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xA,
        (
            "#040F#2PThe cargo bay elevator lift.\x02\x03",

            "It's normally used to load\x01",
            "items onto the ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, -180, 400)

    ChrTalk(    #259
        0x101,
        "#1006F#5PAh, okay.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)

    ChrTalk(    #260
        0x102,
        (
            "#1040F#5PNow we just need to decide who\x01",
            "should investigate the tower, and\x01",
            "who should stay in reserve.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x13, 0x4)
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A78C")
    Call(0, 44)

    label("loc_A78C")

    SetChrName("")

    AnonymousTalk(    #261
        (
            "\x07\x05Please form your party. You may choose two other\x01",
            "members aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(200)
    Sleep(1000)
    OP_A2(0x10F9)
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0310   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_35_A31B end

    def Function_36_A851(): pass

    label("Function_36_A851")

    EventBegin(0x0)
    OP_6D(-740, 2000, 46900, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x101, -430, 2000, 47400, 180)
    SetChrPos(0x102, -1430, 2000, 47400, 180)
    SetChrPos(0xF8, -1430, 2000, 48400, 180)
    SetChrPos(0xF9, -430, 2000, 48400, 180)
    SetChrPos(0x11, -920, 2000, 45630, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #262
        0x11,
        (
            "#100FRight, then. I'll be busy in\x01",
            "the lab downstairs.\x02\x03",

            "If you kids need your orbments tuned\x01",
            "or you need new quartz, come by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        "#1006F#6PYou bet!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB69")

    ChrTalk(    #264
        0x11,
        "#102FTita...take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x107,
        (
            "#560F#6PUh-huh! Don't worry, Grandpa.\x02\x03",

            "#061FI haven't been traveling this long with\x01",
            "everyone without learning a little!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x11,
        "#100FMmm. I bet you haven't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1006F#6PDon't worry, Professor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x106,
        "#051F#6PLeave it to us, Gramps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x11,
        (
            "#104FYes, take care of her, please.\x02\x03",

            "#102FWe still don't know what\x01",
            "the enemy's goal is.\x02\x03",

            "Have a care as you rush into\x01",
            "danger like Poms, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADAC")

    label("loc_AB69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD20")

    ChrTalk(    #270
        0x11,
        "#102FTita...take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x107,
        (
            "#560F#6PUh-huh! Don't worry, Grandpa.\x02\x03",

            "#061FI haven't been traveling this long with\x01",
            "everyone without learning a little!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x11,
        "#100FMmm. I bet you haven't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        "#1006F#6PDon't worry, Professor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        "#1040F#6PWe'll make sure she stays safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x11,
        (
            "#104FYes, take care of her, please.\x02\x03",

            "#102FWe still don't know what\x01",
            "the enemy's goal is.\x02\x03",

            "Have a care as you rush into\x01",
            "danger like Poms, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADAC")

    label("loc_AD20")


    ChrTalk(    #276
        0x11,
        (
            "#102FRight, remember, you lot.\x01",
            "We still don't know what\x01",
            "the enemy's goal is.\x02\x03",

            "Have a care as you rush into\x01",
            "danger like Poms, you hear?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADAC")

    OP_8C(0x11, 90, 400)

    def lambda_ADB9():

        label("loc_ADB9")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_ADB9")

    QueueWorkItem2(0x101, 1, lambda_ADB9)

    def lambda_ADCA():

        label("loc_ADCA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_ADCA")

    QueueWorkItem2(0x102, 1, lambda_ADCA)

    def lambda_ADDB():

        label("loc_ADDB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_ADDB")

    QueueWorkItem2(0xF8, 1, lambda_ADDB)

    def lambda_ADEC():

        label("loc_ADEC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_ADEC")

    QueueWorkItem2(0xF9, 1, lambda_ADEC)
    SetChrFlags(0x11, 0x4)
    OP_8E(0x11, 0x686, 0x802, 0xB252, 0x7D0, 0x0)
    ClearChrFlags(0x11, 0x4)
    OP_8E(0x11, 0x820, 0x0, 0xC170, 0x7D0, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_AE49():
        OP_6D(-710, 2000, 47510, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE49)
    TurnDirection(0x101, 0x102, 400)

    def lambda_AE68():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE68)

    def lambda_AE76():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_AE76)
    Sleep(50)

    def lambda_AE89():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_AE89)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #277
        0x101,
        (
            "#1006F#4POkay, once we're ready,\x01",
            "let's get to the surface!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        "#1040F#6PYeah. The lift is in the cargo bay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1210, 2000, 46360, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1210, 2000, 46360, 180)
    SetChrPos(0x102, -1210, 2000, 46360, 180)
    SetChrPos(0xF8, -1210, 2000, 46360, 180)
    SetChrPos(0xF9, -1210, 2000, 46360, 180)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B027")
    SetChrPos(0x12, 770, 2000, 89910, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 28)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_B027")

    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_A2(0x1E01)
    OP_28(0x99, 0x1, 0x800)
    OP_28(0x9A, 0x4, 0x2)
    OP_28(0x9A, 0x4, 0x8)
    OP_28(0x9A, 0x1, 0x1)
    OP_28(0x9A, 0x1, 0x2)
    OP_28(0x9A, 0x1, 0x4)
    OP_28(0x9A, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_36_A851 end

    def Function_37_B083(): pass

    label("Function_37_B083")

    EventBegin(0x0)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    ClearChrFlags(0x101, 0x80)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    SetChrPos(0xE, -1040, 200, 99240, 0)
    SetChrPos(0xF, -3530, 200, 99080, 315)
    SetChrPos(0x10, 1380, 200, 99090, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #279
        0xC,
        (
            "#178F#5PWe've arrived in the area\x01",
            "around Carnelia Tower.\x02\x03",

            "The tower's peak is still shrouded\x01",
            "by that strange barrier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        "#1002F#2PJust like the Esmelas Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x102,
        (
            "#1035F#5PIt's quite likely that the inside of\x01",
            "the tower will be strange again.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_B35E():
        OP_6D(-130, 2000, 90500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B35E)

    def lambda_B376():
        OP_67(0, 5000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B376)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -1040, 2000, 83000, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_B3AF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B3AF)

    def lambda_B3C1():
        OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14FF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B3C1)

    def lambda_B3DC():

        label("loc_B3DC")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B3DC")

    QueueWorkItem2(0x101, 1, lambda_B3DC)
    Sleep(50)

    def lambda_B3F2():

        label("loc_B3F2")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B3F2")

    QueueWorkItem2(0x102, 1, lambda_B3F2)
    Sleep(50)

    def lambda_B408():

        label("loc_B408")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B408")

    QueueWorkItem2(0x13, 1, lambda_B408)
    Sleep(50)

    def lambda_B41E():

        label("loc_B41E")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B41E")

    QueueWorkItem2(0xA, 1, lambda_B41E)
    Sleep(50)

    def lambda_B434():

        label("loc_B434")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B434")

    QueueWorkItem2(0x12, 1, lambda_B434)
    Sleep(50)

    def lambda_B44A():

        label("loc_B44A")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B44A")

    QueueWorkItem2(0x8, 1, lambda_B44A)
    Sleep(100)

    def lambda_B460():

        label("loc_B460")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_B460")

    QueueWorkItem2(0x14, 1, lambda_B460)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #282
        0xB,
        "#070F#2PHey, sorry to make you wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1004F#6POh, Zin!\x02\x03",

            "#1015FWhat was Kilika contacting\x01",
            "us about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xB,
        (
            "#074F#2PShe wanted to know how\x01",
            "things were up here.\x02\x03",

            "#070FI told her about everything that\x01",
            "happened at Esmelas Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#1006F#6POh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x102,
        (
            "#1040F#6PI'm guessing you didn't mention\x01",
            "our suspect for this tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xB,
        (
            "#070F#2PWell...anyway, shall we hurry\x01",
            "and get inside?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B653")
    Call(0, 44)

    label("loc_B653")

    SetChrName("")

    AnonymousTalk(    #288
        (
            "\x07\x05Please form your party. You may choose one other\x01",
            "member aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(200)
    OP_6D(-1320, 2000, 87840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, -1320, 2000, 87840, 180)
    SetChrPos(0x1, -1320, 2000, 87840, 180)
    SetChrPos(0x2, -1320, 2000, 87840, 180)
    SetChrPos(0x3, -1320, 2000, 87840, 180)
    OP_69(0x0, 0x0)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 4)
    SetChrPos(0xC, -1090, 2000, 94920, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 1330, 0, 98300, 225)
    SetChrChipByIndex(0x10, 12)
    ClearChrFlags(0x10, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x10)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 530, 0, 98030, 90)
    SetChrChipByIndex(0x10, 12)
    ClearChrFlags(0x10, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B8E7")
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_8C(0xA, 0, 0)

    label("loc_B8E7")

    Sleep(500)
    OP_A2(0x1E0A)
    OP_28(0x9A, 0x1, 0x10)
    OP_28(0x9A, 0x1, 0x20)
    OP_28(0x9A, 0x1, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_37_B083 end

    def Function_38_B917(): pass

    label("Function_38_B917")

    EventBegin(0x0)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    ClearChrFlags(0x101, 0x80)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)

    def lambda_B945():

        label("loc_B945")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_B945")

    QueueWorkItem2(0x101, 3, lambda_B945)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    SetChrPos(0xE, -1040, 200, 99240, 0)
    SetChrPos(0xF, -3530, 200, 99080, 315)
    SetChrPos(0x10, 1380, 200, 99090, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_71(0x14, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #289
        0x101,
        (
            "#1025F#5PAnd now we're off to Ruan.\x02\x03",

            "I wonder how Matron Theresa and\x01",
            "the kids are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xA,
        (
            "#043F#2PIf the plan is going well, they're\x01",
            "being evacuated to a safe location\x01",
            "under army protection.\x02\x03",

            "#049FI hope they're safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x102,
        (
            "#1040F#5PI'm certain they'll be fine.\x01",
            "We don't need to worry.\x02\x03",

            "Dad's ordered the army to work\x01",
            "together with the guild to keep\x01",
            "the battle in Ruan under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xA,
        "#542F#2PJoshua...thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        (
            "#1006F#5PYeah, definitely! Dad isn't going\x01",
            "to let anything happen to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x12,
        (
            "#051F#2PYeah, the old man ain't gonna\x01",
            "screw up on this.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #295
        0xC,
        (
            "#178F#5PEveryone.\x02\x03",

            "We're five minutes out from\x01",
            "Sapphirl Tower.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_BE92():
        OP_6D(370, 2000, 93430, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE92)

    def lambda_BEAA():
        OP_67(0, 4500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEAA)

    def lambda_BEC2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BEC2)
    Sleep(50)

    def lambda_BED5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BED5)

    def lambda_BEE3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BEE3)
    Sleep(50)

    def lambda_BEF6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BEF6)

    def lambda_BF04():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BF04)
    Sleep(50)

    def lambda_BF17():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BF17)

    def lambda_BF25():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BF25)
    Sleep(400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #296
        0x101,
        "#1026F#6PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x8,
        (
            "#026F#2PYes... I'm ready.\x02\x03",

            "#020FOnce we arrive, we'll head off.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFED")
    Call(0, 44)

    label("loc_BFED")

    SetChrName("")

    AnonymousTalk(    #298
        (
            "\x07\x05Please form your party. You may choose one other\x01",
            "member aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x1E11)
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_B917 end

    def Function_39_C0B2(): pass

    label("Function_39_C0B2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0C9")
    Call(0, 44)
    Call(0, 45)

    label("loc_C0C9")

    OP_6D(-1320, 2000, 87840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1320, 2000, 87840, 180)
    SetChrPos(0x1, -1320, 2000, 87840, 180)
    SetChrPos(0x2, -1320, 2000, 87840, 180)
    SetChrPos(0x3, -1320, 2000, 87840, 180)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1A5")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_C1A5")

    OP_28(0x9A, 0x1, 0x80)
    OP_28(0x9A, 0x1, 0x100)
    OP_28(0x9A, 0x1, 0x200)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_39_C0B2 end

    def Function_40_C1CD(): pass

    label("Function_40_C1CD")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(460, 2000, 94360, 0)
    OP_67(0, 4750, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    SetChrPos(0xE, -1040, 200, 99240, 0)
    SetChrPos(0xF, -3530, 200, 99080, 315)
    SetChrPos(0x10, 1380, 200, 99090, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #299
        0xC,
        (
            "#178F#6PWe've arrived in Amberl Tower airspace.\x02\x03",

            "We've also just received a further\x01",
            "report from the scout unit.\x02\x03",

            "#176FThe reports say...the attacker was a\x01",
            "girl with an enormous scythe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        "#1003F#2PI...was afraid of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x13,
        "#063F#5PRenne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        (
            "#1035F#5PRenne, the 'Angel of Slaughter.'\x02\x03",

            "When I was last in the society,\x01",
            "she was simply being considered\x01",
            "for the mantle of Enforcer.\x02\x03",

            "#1043FCan she really control the Pater-Mater?\x01",
            "Does it even really WORK properly?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #303
        0x101,
        (
            "#1004F#2PJoshua, do you know what\x01",
            "that huge puppet is?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #304
        0x102,
        (
            "#1042F#5PI know the concept. It's a tactical assault\x01",
            "archaism the society was working on when\x01",
            "I was...deployed.\x02\x03",

            "As far as I know, they ended up freezing\x01",
            "its development because of issues with its\x01",
            "control system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x14,
        (
            "#1063F#2PThat little girlie seems to command\x01",
            "it like a puppy, though.\x02\x03",

            "#1068FDon't think I've ever been so scared of\x01",
            "a grade-schooler before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x13,
        "#561F#5P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)
    Sleep(300)

    ChrTalk(    #307
        0x101,
        (
            "#1006F#5PIt's okay, Tita.\x01",
            "Don't make that face.\x02\x03",

            "We'll make her see the truth!\x01",
            "Just you watch!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)
    Sleep(300)

    ChrTalk(    #308
        0x13,
        "#560F#5PEstelle... Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x102,
        "#1043F#5P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #310
        0x101,
        (
            "#1015F#2PEr. You think I'm being a little\x01",
            "optimistic, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x102,
        (
            "#1035F#5P...No.\x02\x03",

            "#1040FOf all the people in the world, you,\x01",
            "maybe you...can actually reach her.\x02\x03",

            "Come on. We'll do our best together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        "#1016F#2PYeah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C963")
    Call(0, 44)

    label("loc_C963")

    SetChrName("")

    AnonymousTalk(    #313
        (
            "\x07\x05Please form your party. You may choose two other\x01",
            "members aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-1160, 2000, 46570, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1160, 2000, 46570, 180)
    SetChrPos(0x1, -1160, 2000, 46570, 180)
    SetChrPos(0x2, -1160, 2000, 46570, 180)
    SetChrPos(0x3, -1160, 2000, 46570, 180)
    OP_28(0x9A, 0x1, 0x400)
    OP_28(0x9A, 0x1, 0x800)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x2)
    SetMapFlags(0x1)
    SetMapFlags(0x2000000)
    Return()

    # Function_40_C1CD end

    def Function_41_CAB6(): pass

    label("Function_41_CAB6")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    SetChrPos(0x101, -290, 2000, 90360, 0)
    SetChrPos(0x102, -1500, 2000, 90260, 0)
    SetChrPos(0x13, -1660, 2000, 88720, 0)
    SetChrPos(0x14, 500, 2000, 89150, 0)
    SetChrPos(0x12, -1880, 2000, 87500, 0)
    SetChrPos(0x8, -2540, 2000, 88900, 0)
    SetChrPos(0xB, -140, 2000, 87500, 0)
    SetChrPos(0xA, -490, 2000, 88880, 0)
    TurnDirection(0x101, 0xC, 0)
    TurnDirection(0x102, 0xC, 0)
    TurnDirection(0x13, 0xC, 0)
    TurnDirection(0xA, 0xC, 0)
    TurnDirection(0x12, 0xC, 0)
    TurnDirection(0x8, 0xC, 0)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0x14, 0xC, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrChipByIndex(0xC, 4)
    SetChrPos(0xC, -1130, 2000, 92290, 180)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_6D(-10, 2000, 92570, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #314
        0xC,
        (
            "#176F#6PFrom all reports, the society's jaeger\x01",
            "and mechanical forces in all regions\x01",
            "have been driven back.\x02\x03",

            "#171FWe'll be maintaining alert status,\x01",
            "but I think we'll be standing down\x01",
            "from that ourselves soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xA,
        "#542F#2PThat's wonderful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x12,
        (
            "#051F#2PWhat a friggin' day. Invasion's over and\x01",
            "the weirdness at the towers has stopped.\x02\x03",

            "Guess we can finally take a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x8,
        "#524F#2POne can hope, at any rate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xB,
        (
            "#074F#2PIf only I could understand what\x01",
            "the enemy's plan was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        "#1003F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x14,
        (
            "#1063F#2PYou don't seem like you're\x01",
            "in a party mood, Estelle.\x02\x03",

            "You upset about the kiddo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#1007F#2PYeah...\x02",
    )

    CloseMessageWindow()

    def lambda_CF12():
        OP_6D(-10, 2000, 91570, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CF12)
    OP_8C(0x101, 180, 400)

    def lambda_CF31():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF31)

    def lambda_CF3F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CF3F)
    Sleep(50)

    def lambda_CF52():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CF52)

    def lambda_CF60():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CF60)
    Sleep(50)

    def lambda_CF73():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CF73)

    def lambda_CF81():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CF81)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #322
        0x101,
        (
            "#1025F#6PI was just thinking, I was all on\x01",
            "a righteous high horse without\x01",
            "even knowing why she joined.\x02\x03",

            "I think I just made things worse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x13,
        "#063F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xA,
        "#043F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        (
            "#1003F#6PI've always been kind of sheltered\x01",
            "from the really nasty stuff in the world.\x02\x03",

            "So for me to try and save someone\x01",
            "like her...\x02\x03",

            "#1007FMaybe it really was just\x01",
            "a selfish dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x102,
        "#1040F#6PNo, Estelle. I don't think so at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #328
        0x102,
        (
            "#1035F#6PRenne is, in the truest sense of\x01",
            "the word, a genius.\x02\x03",

            "She's capable of understanding\x01",
            "any information she comes across\x01",
            "and can turn it to her advantage.\x02\x03",

            "She's capable of adapting to any\x01",
            "situation in her way, and she can\x01",
            "control her surroundings perfectly.\x02\x03",

            "#1042FAs far as I know, she was\x01",
            "born with those abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x101,
        (
            "#1026F#4PWow... I knew she was capable, but\x01",
            "thinking about it, yeah, that's all true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x102,
        (
            "#1043F#6PBefore the society took her in, she was...\x01",
            "in a horrible situation. Worse than what\x01",
            "I went though, in many ways.\x02\x03",

            "Unlike me, though, her heart never really\x01",
            "'broke.' At least not in the same way.\x02\x03",

            "#1035FAt this point, 'adversity' is just another\x01",
            "obstacle to her--one she can overcome\x01",
            "with guile or force.\x02\x03",

            "Rather than shutting down, she became\x01",
            "as flexible as a snake. More so than any\x01",
            "of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x101,
        (
            "#1020F#4PBut, but hang on! Even if she wasn't\x01",
            "'heartbroken' or whatever, she still...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x102,
        (
            "#1043F#6POh, trust me, I agree.\x02\x03",

            "No matter how happy she might say\x01",
            "she is, she's still obviously in pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        "#1026F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x102,
        (
            "#1035F#6PIt may have been years ago, but in all\x01",
            "my time with her--and it was a lot\x01",
            "- I've never seen her get that worked up.\x02\x03",

            "I think your words reached a part of\x01",
            "Renne even she doesn't recognize.\x02\x03",

            "#1040FThat's something only you could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1025F#4PJoshua...\x02\x03",

            "#1007FWell, nuts, when you put it like that,\x01",
            "how CAN I be depressed?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #336
        0x101,
        (
            "#1022F#6PJust you wait, Renne!\x02\x03",

            "#1005F'Next time we meet'...\x01",
            "I'll get to your real self!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #337
        0x13,
        "#067F#5PYou can do it, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x8,
        (
            "#027F#5PHeh. Never gives up,\x01",
            "does she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x14,
        "#1061F#4PHaha! Wouldn't be Estelle otherwise!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(300)

    ChrTalk(    #340
        0x101,
        (
            "#1016F#6PAaaanyway, uh, that aside.\x02\x03",

            "#1015FWhat DO we do now?\x02\x03",

            "I don't feel safe just cruising back\x01",
            "to Grancel without knowing what\x01",
            "the society was really up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xC,
        (
            "#170F#6PIn that case, might I suggest\x01",
            "a stop at Leiston Fortress?\x02\x03",

            "We can consult with General\x01",
            "Bright as to what to do next.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D8FA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8FA)

    def lambda_D908():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D908)
    Sleep(50)

    def lambda_D91B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D91B)

    def lambda_D929():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D929)
    Sleep(50)

    def lambda_D93C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D93C)

    def lambda_D94A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D94A)
    Sleep(50)

    def lambda_D95D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D95D)

    def lambda_D96B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D96B)
    Sleep(200)

    ChrTalk(    #342
        0x101,
        "#1004F#4POh, good idea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x102,
        "#1040F#4PI think that's for the best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xA,
        (
            "#040F#2PWell, then, Julia.\x01",
            "Please set course for Leiston.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xC,
        "#171F#6PBy your command, mila--\x02",
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1040, 2000, 83000, 0)

    NpcTalk(    #346
        0x11,
        "Old Man's Voice",
        "#1PBLAST IT ALL! BLAST IT!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_DB68():
        OP_6D(-130, 2000, 90500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB68)

    def lambda_DB80():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_DB80)

    def lambda_DB92():
        OP_8E(0xFE, 0xFFFFFB50, 0x7D0, 0x14FF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_DB92)

    def lambda_DBAD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBAD)

    def lambda_DBBB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DBBB)
    Sleep(50)

    def lambda_DBCE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DBCE)

    def lambda_DBDC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DBDC)
    Sleep(50)

    def lambda_DBEF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DBEF)

    def lambda_DBFD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DBFD)
    Sleep(50)

    def lambda_DC10():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DC10)

    def lambda_DC1E():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DC1E)
    Sleep(50)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #347
        0x13,
        "#064F#5PGrandpa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x101,
        (
            "#1015F#6PProfessor? What's wrong?\x01",
            "You seem really worked up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x11,
        (
            "#105F#2PThat data crystal you found in the tower!\x02\x03",

            "Capel just finished analyzing it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        "#1004F#6PUh. Okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x102,
        (
            "#1042F#6PCalm down, Professor.\x01",
            "What was recorded on it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x11,
        (
            "#105F#2PThe function of the Tetracyclic Towers!\x02\x03",

            "You were right...in part! The four\x01",
            "towers were built to keep the Aureole\x01",
            "sealed away in another dimension!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        "#1020F#6PA... Hang on, what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x102,
        (
            "#1044F#6PIn another DIMENSION?\x01",
            "How in the world...?\x01",
            "WHY in the...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x14,
        (
            "#1064F#6PWait a second!\x02\x03",

            "So the shadow towers were--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x11,
        (
            "#104F#2PYes, I suspect you're among the\x01",
            "first humans in a millennium to travel\x01",
            "dimensionally.\x02\x03",

            "#102FAnd the Gospels. They're--\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #357
        (
            "\x07\x05Yes, indeed. Conduits for the\x01",
            "power of the Shining Ring.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x5A)
    Sleep(500)

    def lambda_E075():
        OP_6D(1970, 2000, 92640, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E075)

    def lambda_E08D():
        OP_67(0, 5150, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E08D)

    def lambda_E0A5():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E0A5)

    def lambda_E0B3():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0B3)
    Sleep(50)

    def lambda_E0C6():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0C6)

    def lambda_E0D4():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E0D4)
    Sleep(50)

    def lambda_E0E7():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E0E7)

    def lambda_E0F5():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E0F5)
    Sleep(50)

    def lambda_E108():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E108)

    def lambda_E116():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E116)
    Sleep(50)

    def lambda_E129():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E129)
    OP_72(0xC, 0x4)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3C)
    Sleep(150)
    OP_22(0x127, 0x0, 0x64)
    OP_73(0xC)
    WaitChrThread(0x101, 0x2)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x3)
    OP_74(0xC, 0x8, 0x3)
    OP_74(0xC, 0xA, 0x3)
    OP_0D()
    Sleep(200)

    ChrTalk(    #358
        0x102,
        "#1042F#5PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1020F#2PWEISSMANN?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x12,
        "#052F#2PHow in the hell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xA,
        "#044F#2PThat man... Is that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x14,
        "#1063F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xC,
        (
            "#173F#5PH-How is he doing this\x01",
            "without authorization...?\x02\x03",

            "#177FLeon, report!\x01",
            "What's going on?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x10,
        "#6PI, I don't know, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x10,
        (
            "#6PI just noticed we received a transmission,\x01",
            "and then we lost control!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x11,
        (
            "#104F#2PForced computer entry...\x01",
            "'Hacking,' some call it.\x02\x03",

            "#102FI suppose having these advanced computers\x01",
            "aboard the Arseille backfired on us.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName("Weissmann")

    AnonymousTalk(    #367
        (
            "\x07\x05Hahaha. A pleasure to make your\x01",
            "acquaintance, Professor Russell.\x02\x03",

            "Yes, it's just as you suppose. I must\x01",
            "admit surprise that you were able to\x01",
            "realize such a system on your own.\x02\x03",

            "Though I suppose it's no surprise, coming\x01",
            "from a student of Epstein himself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #368
        0x11,
        (
            "#102F#2PHmph. As full of yourself as a balloon.\x02\x03",

            "#104FI'll point out, 'Professor' Weissmann,\x01",
            "that our flight controls are not networked\x01",
            "to any other system.\x02\x03",

            "You won't be able to crash us or\x01",
            "force open our doors or any other\x01",
            "such harebrained nonsense.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName("Weissmann")

    AnonymousTalk(    #369
        (
            "\x07\x05I wouldn't dream of it, regardless.\x02\x03",

            "I simply wanted to contact you to ensure\x01",
            "you were properly informed and prepared.\x02\x03",

            "To make sure you knew of\x01",
            "the coming moment of glory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #370
        0x11,
        "#102F#2PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x102,
        "#1046F#2PMoment of... No!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName("Weissmann")

    AnonymousTalk(    #372
        (
            "\x07\x05Hahaha... Let me see, given your\x01",
            "position, the best place to see it\x01",
            "should be your foredeck.\x02\x03",

            "Good evening, then, everyone.\x01",
            "And welcome to the new age.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x0)
    OP_74(0xC, 0x8, 0x0)
    OP_74(0xC, 0xA, 0x0)
    OP_0D()
    Sleep(200)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x101, 0x102, 600)
    Sleep(300)

    ChrTalk(    #373
        0x101,
        "#1005F#2PJoshua!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 600)
    Sleep(300)

    ChrTalk(    #374
        0x102,
        "#1042F#5PLet's get to the deck!\x02",
    )

    CloseMessageWindow()
    OP_3F(0x401, 1)
    OP_3F(0x402, 1)
    OP_3F(0x403, 1)
    OP_3F(0x404, 1)
    OP_3F(0x405, 1)
    OP_3F(0x406, 1)
    OP_3F(0x407, 1)
    OP_3F(0x408, 1)
    OP_3F(0x409, 1)
    OP_3F(0x412, 1)
    OP_3F(0x413, 1)
    OP_3F(0x414, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_41_CAB6 end

    def Function_42_E81E(): pass

    label("Function_42_E81E")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x101, 25)
    OP_8E(0xFE, 0xFFFFF27C, 0x7D0, 0x15F7C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF1C8, 0x7D0, 0x15388, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFCCC, 0x7D0, 0x14E60, 0x1770, 0x0)

    def lambda_E86A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E86A)
    OP_8E(0xFE, 0xFFFFFB8C, 0x7D0, 0x146CC, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_E81E end

    def Function_43_E890(): pass

    label("Function_43_E890")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFF27C, 0x7D0, 0x15F7C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF1C8, 0x7D0, 0x15388, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFCCC, 0x7D0, 0x14E60, 0x1770, 0x0)

    def lambda_E8DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E8DC)
    OP_8E(0xFE, 0xFFFFFB8C, 0x7D0, 0x146CC, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_E890 end

    def Function_44_E902(): pass

    label("Function_44_E902")

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
        (0, "loc_E97B"),
        (1, "loc_E981"),
        (SWITCH_DEFAULT, "loc_E987"),
    )


    label("loc_E97B")

    OP_A2(0x1200)
    Jump("loc_E987")

    label("loc_E981")

    OP_A2(0x1201)
    Jump("loc_E987")

    label("loc_E987")

    Return()

    # Function_44_E902 end

    def Function_45_E988(): pass

    label("Function_45_E988")

    FadeToDark(0, 0, -1)
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_45_E988 end

    def Function_46_EA15(): pass

    label("Function_46_EA15")

    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_EA33"),
        (2, "loc_EA9B"),
        (4, "loc_EAEE"),
        (3, "loc_EB87"),
        (7, "loc_EBFD"),
        (SWITCH_DEFAULT, "loc_EC67"),
    )


    label("loc_EA33")


    ChrTalk(    #375
        0x101,
        (
            "#1016FOh, hey, so this is the back of the ship.\x02\x03",

            "#1008FA legendary dragon... My heart's racing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC67")

    label("loc_EA9B")


    ChrTalk(    #376
        0x103,
        (
            "#025FThis is the stern, then.\x02\x03",

            "#020FLet's go and look a legend in the eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC67")

    label("loc_EAEE")


    ChrTalk(    #377
        0x105,
        (
            "#047FThis is the ship's stern.\x02\x03",

            "#042F...A dragon who has lived since the time\x01",
            "of our forefathers. I don't think I will ever\x01",
            "forget this sight...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC67")

    label("loc_EB87")


    ChrTalk(    #378
        0x104,
        (
            "#033FAh, this is the ship's stern.\x02\x03",

            "#035F...Heh. Even I cannot help but be\x01",
            "nervous before a legendary dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC67")

    label("loc_EBFD")


    ChrTalk(    #379
        0x108,
        (
            "#073FAh, this is the stern.\x02\x03",

            "#070F...We'll be facing a legend.\x01",
            "Don't think I'll ever forget this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC67")

    label("loc_EC67")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_46_EA15 end

    def Function_47_EC83(): pass

    label("Function_47_EC83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE87")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_ECAD"),
        (2, "loc_ECFD"),
        (4, "loc_ED52"),
        (3, "loc_EDAE"),
        (7, "loc_EE1A"),
        (SWITCH_DEFAULT, "loc_EE6C"),
    )


    label("loc_ECAD")


    ChrTalk(    #380
        0x101,
        (
            "#1007FNo point in going down here.\x02\x03",

            "#1000F...Let's hurry to the dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE6C")

    label("loc_ECFD")


    ChrTalk(    #381
        0x103,
        (
            "#026FNo real point in going below.\x02\x03",

            "#020FLet's hurry and go face the dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE6C")

    label("loc_ED52")


    ChrTalk(    #382
        0x105,
        (
            "#047FWe don't have any business down below.\x02\x03",

            "#042FLet us hurry and face the dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE6C")

    label("loc_EDAE")


    ChrTalk(    #383
        0x104,
        (
            "#030FA legend is all but before our very eyes.\x02\x03",

            "#035FTo leave the stage now would be\x01",
            "most improper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE6C")

    label("loc_EE1A")


    ChrTalk(    #384
        0x108,
        (
            "#074FWe've got nothing to do down there.\x02\x03",

            "#070FLet's hurry to the dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE6C")

    label("loc_EE6C")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_EE87")

    Return()

    # Function_47_EC83 end

    SaveToFile()

Try(main)
