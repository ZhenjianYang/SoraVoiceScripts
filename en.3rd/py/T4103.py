from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4103.x',
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
        'Man in Black',                         # 9
        'Man in Black',                         # 10
        'Man in Black',                         # 11
        'Man in Black',                         # 12
        'Man in Black',                         # 13
        'Man in Black',                         # 14
        'Man in Black',                         # 15
        'Man in Black',                         # 16
        'Man in Black',                         # 17
        'Man in Black',                         # 18
        'Kurt',                                 # 19
        'Gundolf',                              # 20
        'Cat',                                  # 21
        'Nial',                                 # 22
        'Dorothy',                              # 23
        'Noel',                                 # 24
        'Becker',                               # 25
        'Palmer',                               # 26
        'Box',                                  # 27
        'Woman',                                # 28
        'Woman',                                # 29
        'Woman',                                # 30
        'Archbishop Currant',                   # 31
        'Major Vander',                         # 32
        'Grancel - West Block',                 # 33
        'Grancel Castle',                       # 34
        'Grancel - East Block',                 # 35
        'Grancel - South Block',                # 36
        'Target Camera',                        # 37
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
        'ED6_DT27/CH03460 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT26/CH20682 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH02720 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT26/CH20618 ._CH',             # 09
        'ED6_DT27/CH04230 ._CH',             # 0A
        'ED6_DT27/CH04232 ._CH',             # 0B
        'ED6_DT27/CH04234 ._CH',             # 0C
        'ED6_DT27/CH04231 ._CH',             # 0D
        'ED6_DT27/CH04464 ._CH',             # 0E
        'ED6_DT27/CH04463 ._CH',             # 0F
        'ED6_DT07/CH01410 ._CH',             # 10
        'ED6_DT07/CH01400 ._CH',             # 11
        'ED6_DT27/CH03570 ._CH',             # 12
        'ED6_DT07/CH01030 ._CH',             # 13
        'ED6_DT07/CH01130 ._CH',             # 14
        'ED6_DT07/CH01170 ._CH',             # 15
        'ED6_DT26/CH20686 ._CH',             # 16
        'ED6_DT26/CH20681 ._CH',             # 17
        'ED6_DT27/CH04462 ._CH',             # 18
        'ED6_DT27/CH04460 ._CH',             # 19
        'ED6_DT27/CH04461 ._CH',             # 1A
        'ED6_DT26/CH20680 ._CH',             # 1B
        'ED6_DT27/CH03420 ._CH',             # 1C
        'ED6_DT26/CH20684 ._CH',             # 1D
        'ED6_DT26/CH20684 ._CH',             # 1E
        'ED6_DT07/CH00410 ._CH',             # 1F
        'ED6_DT07/CH00411 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT27/CH03460P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT26/CH20682P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH02720P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT26/CH20618P._CP',             # 09
        'ED6_DT27/CH04230P._CP',             # 0A
        'ED6_DT27/CH04232P._CP',             # 0B
        'ED6_DT27/CH04234P._CP',             # 0C
        'ED6_DT27/CH04231P._CP',             # 0D
        'ED6_DT27/CH04464P._CP',             # 0E
        'ED6_DT27/CH04463P._CP',             # 0F
        'ED6_DT07/CH01410P._CP',             # 10
        'ED6_DT07/CH01400P._CP',             # 11
        'ED6_DT27/CH03570P._CP',             # 12
        'ED6_DT07/CH01030P._CP',             # 13
        'ED6_DT07/CH01130P._CP',             # 14
        'ED6_DT07/CH01170P._CP',             # 15
        'ED6_DT26/CH20686P._CP',             # 16
        'ED6_DT26/CH20681P._CP',             # 17
        'ED6_DT27/CH04462P._CP',             # 18
        'ED6_DT27/CH04460P._CP',             # 19
        'ED6_DT27/CH04461P._CP',             # 1A
        'ED6_DT26/CH20680P._CP',             # 1B
        'ED6_DT27/CH03420P._CP',             # 1C
        'ED6_DT26/CH20684P._CP',             # 1D
        'ED6_DT26/CH20684P._CP',             # 1E
        'ED6_DT07/CH00410P._CP',             # 1F
        'ED6_DT07/CH00411P._CP',             # 20
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0xE4,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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

    DeclNpc(
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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

    DeclNpc(
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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

    DeclNpc(
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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


    DeclEvent(
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -3000,
        Y                   = 0,
        Z                   = 70200,
        Range               = 2000,
        Unknown_10          = 0x1D4C,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 3000,
        Y                   = 0,
        Z                   = 70200,
        Range               = 2000,
        Unknown_10          = 0x1D4C,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 16560,
        Y                   = 0,
        Z                   = 70500,
        Range               = 18000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xD6D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = -35600,
        Y                   = 0,
        Z                   = 54000,
        Range               = -33600,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xB1BC,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    ScpFunction(
        "Function_0_5F2",          # 00, 0
        "Function_1_74B",          # 01, 1
        "Function_2_7D7",          # 02, 2
        "Function_3_7ED",          # 03, 3
        "Function_4_833",          # 04, 4
        "Function_5_A6C",          # 05, 5
        "Function_6_AC6",          # 06, 6
        "Function_7_B5D",          # 07, 7
        "Function_8_C64",          # 08, 8
        "Function_9_C88",          # 09, 9
        "Function_10_E27",         # 0A, 10
        "Function_11_F7F",         # 0B, 11
        "Function_12_1112",        # 0C, 12
        "Function_13_190F",        # 0D, 13
        "Function_14_2459",        # 0E, 14
        "Function_15_248B",        # 0F, 15
        "Function_16_24E9",        # 10, 16
        "Function_17_251A",        # 11, 17
        "Function_18_2EE6",        # 12, 18
        "Function_19_2F4D",        # 13, 19
        "Function_20_2FCC",        # 14, 20
        "Function_21_4561",        # 15, 21
        "Function_22_50AE",        # 16, 22
        "Function_23_50D6",        # 17, 23
        "Function_24_5108",        # 18, 24
        "Function_25_515F",        # 19, 25
        "Function_26_5199",        # 1A, 26
        "Function_27_51B2",        # 1B, 27
        "Function_28_51D0",        # 1C, 28
        "Function_29_52B6",        # 1D, 29
        "Function_30_539C",        # 1E, 30
        "Function_31_5482",        # 1F, 31
        "Function_32_5568",        # 20, 32
        "Function_33_5E89",        # 21, 33
        "Function_34_5EEE",        # 22, 34
        "Function_35_5F81",        # 23, 35
        "Function_36_724D",        # 24, 36
        "Function_37_7251",        # 25, 37
        "Function_38_7299",        # 26, 38
        "Function_39_72FF",        # 27, 39
    )


    def Function_0_5F2(): pass

    label("Function_0_5F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_6EC")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x10, -4660, 0, 68440, 180)
    SetChrPos(0x11, -1500, 0, 68440, 180)
    SetChrPos(0x12, -3080, 0, 68080, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x13, 4660, 0, 68440, 180)
    SetChrPos(0x14, 1500, 0, 68440, 180)
    SetChrPos(0x15, 3080, 0, 68080, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 27400, 0, 65260, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 27400, 0, 63660, 270)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 25020, 0, 64500, 90)
    Jump("loc_707")

    label("loc_6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_6F6")
    Jump("loc_707")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_700")
    Jump("loc_707")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_707")

    label("loc_707")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_72B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_74A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_74A")

    Return()

    # Function_0_5F2 end

    def Function_1_74B(): pass

    label("Function_1_74B")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_772")

    OP_B1("T4103_n")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    OP_B2(0x0, 0x4, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7D6")
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_B2(0x1, 0x3, 0x80)
    OP_B2(0x1, 0x4, 0x80)
    OP_1B(0x0, 0x0, 0x1C)
    OP_1B(0x1, 0x0, 0x1D)
    OP_1B(0x2, 0x0, 0x1F)
    OP_1B(0x3, 0x0, 0x1E)

    label("loc_7D6")

    Return()

    # Function_1_74B end

    def Function_2_7D7(): pass

    label("Function_2_7D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7D7")

    label("loc_7EC")

    Return()

    # Function_2_7D7 end

    def Function_3_7ED(): pass

    label("Function_3_7ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_832")
    SetChrPos(0xFE, 31870, 0, 62180, 270)
    OP_8E(0xFE, 0x1324, 0x0, 0xF2E4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1324, 0x0, 0x40CE, 0x7D0, 0x0)
    Jump("Function_3_7ED")

    label("loc_832")

    Return()

    # Function_3_7ED end

    def Function_4_833(): pass

    label("Function_4_833")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6B")
    SetChrPos(0xFE, -40860, 0, 28340, 0)
    OP_8E(0xFE, 0xFFFF6064, 0x0, 0xBAE0, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF624E, 0x0, 0xC422, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF9F48, 0xFA, 0xF1F4, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(400)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFE674, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xCED6, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xF276, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFF16E, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x3070, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x37F0, 0x0, 0xF604, 0x2328, 0x0)
    OP_8E(0xFE, 0x9B8C, 0x0, 0xF604, 0x2328, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 39650, 0, 62210, 90)
    OP_8E(0xFE, 0x67A2, 0x0, 0xF302, 0x2328, 0x0)
    OP_8E(0xFE, 0x56B8, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2A9E, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xDC00, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xC030, 0x2328, 0x0)
    OP_8E(0xFE, 0x2BE8, 0xFA, 0xB6D0, 0x2328, 0x0)
    OP_8E(0xFE, 0x402E, 0xFA, 0xB6D0, 0x2328, 0x0)
    Sleep(400)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x8E12, 0x2328, 0x0)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x1F04, 0x2328, 0x0)
    Sleep(2000)
    Jump("Function_4_833")

    label("loc_A6B")

    Return()

    # Function_4_833 end

    def Function_5_A6C(): pass

    label("Function_5_A6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC5")
    SetChrPos(0xFE, -4340, 0, 16160, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0x6B58, 0x9C4, 0x0)
    Jump("Function_5_A6C")

    label("loc_AC5")

    Return()

    # Function_5_A6C end

    def Function_6_AC6(): pass

    label("Function_6_AC6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5C")
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0x5528, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xF94C, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_6_AC6")

    label("loc_B5C")

    Return()

    # Function_6_AC6 end

    def Function_7_B5D(): pass

    label("Function_7_B5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C63")
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF65E6, 0x0, 0xBBE4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0x9592, 0x9C4, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF676C, 0x0, 0xC1E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFE2F0, 0x0, 0xC0F8, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_7_B5D")

    label("loc_C63")

    Return()

    # Function_7_B5D end

    def Function_8_C64(): pass

    label("Function_8_C64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C87")
    OP_8D(0xFE, 8130, 41700, 5710, 43100, 2000)
    Jump("Function_8_C64")

    label("loc_C87")

    Return()

    # Function_8_C64 end

    def Function_9_C88(): pass

    label("Function_9_C88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_E08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D44")

    ChrTalk(    #0
        0xFE,
        (
            "The best tourist spot in Grancel is the castle's\x01",
            "garden terrace, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It doesn't seem to be open to the public lately,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "I wonder why?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E05")

    label("loc_D44")


    ChrTalk(    #3
        0xFE,
        (
            "The best tourist spot in Grancel is the castle's\x01",
            "garden terrace, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "The city's got plenty of other highlights,\x01",
            "too, but if I had to pick only one, I'd say\x01",
            "the terrace.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_E05")

    Jump("loc_E23")

    label("loc_E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_E12")
    Jump("loc_E23")

    label("loc_E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_E1C")
    Jump("loc_E23")

    label("loc_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_E23")

    label("loc_E23")

    TalkEnd(0xFE)
    Return()

    # Function_9_C88 end

    def Function_10_E27(): pass

    label("Function_10_E27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EDA")

    ChrTalk(    #5
        0xFE,
        (
            "I feel like I've been seeing men dressed\x01",
            "all in black a lot lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Even their glasses are black! Is that some kind\x01",
            "of fashion trend or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5D")

    label("loc_EDA")


    ChrTalk(    #7
        0xFE,
        (
            "Ugh! So much to do, so much to do... The amount\x01",
            "of my day I just spend running around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Move it! Get out of the way!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_F5D")

    Jump("loc_F7B")

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_F6A")
    Jump("loc_F7B")

    label("loc_F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_F74")
    Jump("loc_F7B")

    label("loc_F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_F7B")

    label("loc_F7B")

    TalkEnd(0xFE)
    Return()

    # Function_10_E27 end

    def Function_11_F7F(): pass

    label("Function_11_F7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_10F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1014")

    ChrTalk(    #9
        0xFE,
        (
            "General Morgan's son is back in the country\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Which is exceptionally unusual... He's usually\x01",
            "REALLY busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F0")

    label("loc_1014")


    ChrTalk(    #11
        0xFE,
        (
            "I've heard Irving's come back here to Liberl for\x01",
            "a while, which is pretty unusual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "He's General Morgan's son, and he's usually abroad\x01",
            "as a military attache...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "What could've happened to make him return?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_10F0")

    Jump("loc_110E")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_10FD")
    Jump("loc_110E")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1107")
    Jump("loc_110E")

    label("loc_1107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_110E")

    label("loc_110E")

    TalkEnd(0xFE)
    Return()

    # Function_11_F7F end

    def Function_12_1112(): pass

    label("Function_12_1112")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(21960, 250, 46140, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(58000, 0)
    OP_6E(330, 0)
    SetChrPos(0x151, 8900, 250, 26340, 0)
    SetChrPos(0x103, 8900, 250, 24140, 0)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_11B3():
        OP_6D(11260, 250, 39200, 5000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_11B3)

    def lambda_11CB():
        OP_8E(0xFE, 0x22C4, 0xFA, 0xBCAC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_11CB)
    OP_43(0x151, 0x3, 0x0, 0xE)

    def lambda_11ED():
        OP_8E(0xFE, 0x22C4, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11ED)
    WaitChrThread(0x2C, 0x0)
    Sleep(1000)

    def lambda_1212():
        OP_6D(9920, 250, 46880, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1212)

    def lambda_122A():
        OP_6B(3500, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_122A)

    def lambda_123A():
        OP_6C(35000, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_123A)

    def lambda_124A():
        OP_6E(266, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_124A)
    WaitChrThread(0x2C, 0x0)
    WaitChrThread(0x103, 0x1)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x103,
        (
            "#1643FW-Wait a second...\x02\x03",

            "Isn't this the hotel? The building you've just\x01",
            "walked right past?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x151, 0x3)

    ChrTalk(    #15
        0x151,
        "#1652FWell, yes, but...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 4500, 0, 67380, 180)
    SetChrPos(0x16, 2400, 0, 67380, 180)
    OP_59()

    def lambda_1330():
        OP_6D(6440, 0, 58060, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1330)

    def lambda_1348():
        OP_67(0, 3620, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_1348)

    def lambda_1360():
        OP_6B(3700, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_1360)

    def lambda_1370():
        OP_6C(0, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_1370)

    def lambda_1380():
        OP_6E(276, 2500)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_1380)
    WaitChrThread(0x2C, 0x0)
    Sleep(500)

    def lambda_139A():
        OP_8F(0xFE, 0x274C, 0xFA, 0xBF40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_139A)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #16
        0x151,
        (
            "#1652F(Grancel Castle looks really heavily guarded...\x01",
            "I should have known.)\x02\x03",

            "#1656F(Hmm... There's got to be some way to get\x01",
            "past.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(11340, 250, 49020, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(35000, 0)
    OP_6E(267, 0)
    SetChrPos(0x151, 10460, 250, 48960, 0)
    Sleep(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    def lambda_14AF():
        OP_8E(0xFE, 0x28DC, 0x0, 0xB4DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14AF)
    WaitChrThread(0x103, 0x1)

    def lambda_14CF():
        OP_8E(0xFE, 0x28DC, 0x0, 0xB860, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14CF)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #17
        0x103,
        (
            "#1648F#4P...\x02\x03",

            "That way leads to Grancel Castle. Do you want\x01",
            "to go and have a look around it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(    #18
        0x151,
        (
            "#1654F#5P...Y-Yes. I suppose I do...\x02\x03",

            "But...umm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#1646F#4P(Looks like I've almost cracked her.)\x02\x03",

            "#1648F(Time to talk, young lady!)\x02\x03",

            "(I want to know exactly what I've been\x01",
            "dragged all over the city for!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1634():
        OP_6D(15540, 0, 46880, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1634)
    WaitChrThread(0x2C, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 20500, 750, 44000, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #20
        0x10,
        "Man's Voice",
        "#3PGah... This job's such a pain.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x10,
        "Man's Voice",
        "#3PI'm gonna go and catch a breather outside.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(21160, 250, 44340, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(82000, 0)
    OP_6E(266, 0)
    Sleep(500)
    OP_20(0x7D0)
    OP_70(0x4, 0x3B)
    OP_73(0x4)

    def lambda_173B():
        OP_6D(13640, 250, 46420, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_173B)

    def lambda_1753():
        OP_8E(0xFE, 0x3B24, 0xFA, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1753)

    def lambda_176E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_176E)
    WaitChrThread(0x10, 0x1)

    def lambda_1785():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1785)

    def lambda_1793():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_1793)

    def lambda_17A1():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_17A1)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x10,
        "#3STh-There she is!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        "#1643FWh-What?! What's going on?!\x02",
    )

    CloseMessageWindow()
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x10, 0)
    Sleep(300)

    ChrTalk(    #24
        0x10,
        "#3SYou stay right where you are!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_18B3():
        OP_6B(2340, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_18B3)
    SetChrChipByIndex(0x10, 26)
    SetChrSubChip(0x10, 0)

    def lambda_18CD():
        OP_8E(0xFE, 0x2FA8, 0xFA, 0xB694, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18CD)
    Sleep(500)
    OP_44(0x2C, 0xFF)
    OP_44(0x10, 0xFF)
    Battle(0x3AC, 0x0, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    Return()

    # Function_12_1112 end

    def Function_13_190F(): pass

    label("Function_13_190F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_6D(13240, 250, 46040, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(60000, 0)
    OP_6E(266, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 13640, 250, 44740, 270)
    SetChrPos(0x103, 10920, 250, 44860, 90)
    SetChrPos(0x151, 12940, 250, 46860, 180)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_19AA():
        OP_6B(3340, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_19AA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x2C, 0x0)

    ChrTalk(    #25
        0x103,
        (
            "#1645F*pant*...*pant*...\x02\x03",

            "#1642FWh-What the...?! That guy was no amateur.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(500)
    OP_8C(0x151, 315, 500)
    Sleep(300)

    def lambda_1A43():
        OP_8E(0xFE, 0x2A30, 0xFA, 0xBE8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1A43)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 0, 500)
    Sleep(500)

    ChrTalk(    #26
        0x151,
        (
            "#1652F#5P(Well, they haven't noticed anything has\x01",
            "happened just yet by the looks of it.)\x02\x03",

            "#1654F(It's only going to be a matter of time,\x01",
            "though... I need to do something!)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(300)

    ChrTalk(    #27
        0x103,
        (
            "#1644FLook, you. It's time for you to start talking.\x02\x03",

            "Who IS this guy?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x151,
        (
            "#1654F#5P(I don't want the army to notice anything\x01",
            "amiss, either...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BC3():
        OP_8E(0xFE, 0x2AA8, 0xFA, 0xB324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BC3)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #29
        0x103,
        "#1644F#120W#4SAre you listening to me?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(    #30
        0x151,
        "#1652F#5PShhh! Please, be quiet!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 20500, 750, 44500, 270)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 20500, 750, 43500, 270)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #31
        0x11,
        "Man's Voice",
        (
            "#3PWell, at least now we know she's not\x01",
            "on the hotel's guest list...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CE4():
        OP_6D(14840, 250, 46040, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1CE4)
    OP_62(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1D20():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_1D20)

    def lambda_1D2E():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D2E)
    WaitChrThread(0x2C, 0x0)

    NpcTalk(    #32
        0x12,
        "Man's Voice",
        "#3PBah...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #33
        0x12,
        "Man's Voice",
        (
            "#3PI figured a rich girl like her would have\x01",
            "to stay at a hotel, but I guess not.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #34
        0x11,
        "Man's Voice",
        (
            "#3PWe're just gonna have to start scouring\x01",
            "the city...\x02",
        )
    )

    CloseMessageWindow()
    OP_70(0x4, 0x3B)
    OP_73(0x4)

    def lambda_1E11():
        OP_8E(0xFE, 0x4470, 0xFA, 0xADD4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E11)

    def lambda_1E2C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1E2C)
    Sleep(250)

    def lambda_1E43():
        OP_8E(0xFE, 0x459C, 0xFA, 0xA924, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E43)

    def lambda_1E5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1E5E)
    Sleep(500)

    ChrTalk(    #35
        0x11,
        "#3P...from top#80W...to bottom?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(200)
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(    #36 op#A
        0x11,
        "#3S#20AThere she is!\x02",
    )

    CloseMessageWindow()
    OP_7C(0x0, 0x96, 0xBB8, 0x64)
    #Sleep(2200)

    ChrTalk(    #37 op#A
        0x12,
        "#3S#4P#17AGet her!\x02",
    )
    CloseMessageWindow()

    OP_7C(0x0, 0x96, 0xBB8, 0x64)
    #Sleep(1800)

    ChrTalk(    #38
        0x151,
        "#1653F#4SNo! Don't shout!\x02",
    )

    OP_7C(0x0, 0xDC, 0xBB8, 0x64)
    Sleep(200)
    OP_56(0x1)
    OP_59()
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, 4500, 0, 68380, 180)
    SetChrPos(0x14, 2000, 0, 68380, 180)

    def lambda_1F67():
        OP_6D(4960, 0, 68860, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1F67)
    WaitChrThread(0x2C, 0x0)

    def lambda_1F84():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1F84)
    Sleep(100)

    def lambda_1F97():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1F97)
    Sleep(300)

    ChrTalk(    #39
        0x13,
        "#2PHey, did you hear that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14,
        "Yeah! It came from over there!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x13, 0)

    def lambda_1FF8():
        OP_8E(0xFE, 0x1194, 0x0, 0xBCFC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FF8)
    Sleep(100)
    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0x14, 0)

    def lambda_2022():
        OP_8E(0xFE, 0x7D0, 0x0, 0xBCFC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2022)
    Sleep(1000)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    Fade(500)
    OP_6D(6280, 0, 44480, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(35000, 0)
    OP_6E(266, 0)
    SetChrPos(0x103, 6760, 0, 43740, 90)
    SetChrPos(0x151, 4000, 0, 42440, 90)
    SetChrPos(0x11, 10140, 0, 45600, 270)
    SetChrPos(0x12, 10400, 0, 43360, 270)
    SetChrPos(0x13, 6200, 0, 58500, 180)
    SetChrPos(0x14, 3940, 0, 59000, 180)
    Sleep(500)
    OP_43(0x151, 0x3, 0x0, 0xF)

    def lambda_2102():
        OP_8E(0xFE, 0x23B4, 0x0, 0xB220, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2102)
    Sleep(200)

    def lambda_2122():
        OP_8E(0xFE, 0x251C, 0x0, 0xA960, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2122)
    Sleep(400)

    def lambda_2142():
        OP_8F(0xFE, 0x1680, 0x0, 0xAADC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2142)
    WaitChrThread(0x103, 0x1)

    def lambda_2162():
        OP_8E(0xFE, 0x1838, 0x0, 0xBAA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2162)
    Sleep(100)

    def lambda_2182():
        OP_8E(0xFE, 0xF64, 0x0, 0xB860, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2182)
    WaitChrThread(0x13, 0x1)
    SetChrChipByIndex(0x13, 0)
    SetChrSubChip(0x13, 0)
    WaitChrThread(0x14, 0x1)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 0)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x103, 0x3, 0x0, 0x10)

    Sleep(1500)
    ChrTalk(    #41
        0x103,
        (
            "#1643F#3SWhat's going on?!#2S\x02\x03",

            "#1644F#3SYou've got some SERIOUS explaining to do,\x01",
            "missy!#2S\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x3)

    ChrTalk(    #42
        0x151,
        "#1652FWell... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43 op#A
        0x151,
        "#3S#28A#1PLet's start running!#2S\x02",
    )


    def lambda_2279():
        OP_8E(0xFE, 0xFA0, 0x0, 0x6F68, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2279)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(3000)
    OP_8C(0x103, 180, 500)
    Sleep(100)

    ChrTalk(    #44
        0x103,
        (
            "#1644F#3SThe hell?!#2S\x02\x03",

            "#3SW-Wait!#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_22F2():

        label("loc_22F2")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_22F2")

    QueueWorkItem2(0x11, 2, lambda_22F2)

    def lambda_2303():

        label("loc_2303")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_2303")

    QueueWorkItem2(0x12, 2, lambda_2303)

    def lambda_2314():

        label("loc_2314")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_2314")

    QueueWorkItem2(0x13, 2, lambda_2314)

    def lambda_2325():

        label("loc_2325")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_2325")

    QueueWorkItem2(0x14, 2, lambda_2325)

    def lambda_2336():
        OP_8E(0xFE, 0x1680, 0x0, 0x7044, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2336)
    Sleep(500)
    OP_44(0x13, 0x2)
    OP_8C(0x13, 180, 0)
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x13, 0)

    def lambda_236B():
        OP_8E(0xFE, 0x1838, 0x0, 0x6C84, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_236B)
    Sleep(100)
    OP_44(0x12, 0x2)
    OP_8C(0x12, 180, 0)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)

    def lambda_23A0():
        OP_8E(0xFE, 0x251C, 0x0, 0x5B40, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_23A0)
    Sleep(50)
    OP_44(0x14, 0x2)
    OP_8C(0x14, 180, 0)
    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0x14, 0)

    def lambda_23D5():
        OP_8E(0xFE, 0xF64, 0x0, 0x6A40, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23D5)
    Sleep(100)
    OP_44(0x11, 0x2)
    OP_8C(0x11, 180, 0)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)

    def lambda_240A():
        OP_8E(0xFE, 0x23B4, 0x0, 0x6400, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_240A)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x151, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_190F end

    def Function_14_2459(): pass

    label("Function_14_2459")

    WaitChrThread(0x151, 0x1)

    def lambda_2464():
        OP_8E(0xFE, 0x28DC, 0xFA, 0xBF40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2464)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 0, 500)
    Sleep(400)
    Return()

    # Function_14_2459 end

    def Function_15_248B(): pass

    label("Function_15_248B")


    ChrTalk(    #45 op#A
        0x13,
        "#4P#23AThere she is! There's our target!\x02",
    )

    Sleep(2500)
    OP_56(0x0)
    OP_59()

    ChrTalk(    #46 op#A
        0x14,
        "#4P#23AThe blonde! Get her!\x02",
    )

    Sleep(2700)
    OP_56(0x0)
    OP_59()
    Return()

    # Function_15_248B end

    def Function_16_24E9(): pass

    label("Function_16_24E9")

    OP_8C(0x103, 0, 500)
    Sleep(600)
    OP_8C(0x103, 90, 500)
    Sleep(600)
    OP_8C(0x103, 0, 500)
    Sleep(600)
    OP_8C(0x103, 90, 500)
    Sleep(600)
    Return()

    # Function_16_24E9 end

    def Function_17_251A(): pass

    label("Function_17_251A")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x20000000)
    EventBegin(0x0)
    OP_6D(-3000, 0, 69580, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(0, 0)
    OP_6E(244, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x10, -3950, 0, 69340, 135)
    SetChrPos(0x11, -2050, 0, 69340, 225)
    SetChrPos(0x12, -3000, 0, 68080, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x13, 4660, 0, 68440, 180)
    SetChrPos(0x14, 1500, 0, 68440, 180)
    SetChrPos(0x15, 3080, 0, 68080, 180)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, -13180, 3000, 60360, 90)
    SetChrPos(0x151, -13180, 3000, 59060, 90)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    SoundLoad(372)
    SoundLoad(402)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26D2")
    Call(0, 32)

    def lambda_2670():
        OP_6D(-3000, 0, 69580, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2670)

    def lambda_2688():
        OP_67(0, 7500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2688)

    def lambda_26A0():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_26A0)

    def lambda_26B0():
        OP_6B(3280, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_26B0)

    def lambda_26C0():
        OP_6E(244, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_26C0)
    WaitChrThread(0x2C, 0x0)
    Jump("loc_26DC")

    label("loc_26D2")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_26DC")

    Sleep(500)
    OP_20(0xBB8)

    def lambda_26EC():
        OP_6D(-3000, 0, 68000, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_26EC)

    def lambda_2704():
        OP_67(0, 4160, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2704)

    def lambda_271C():
        OP_6B(4220, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_271C)
    Sleep(3000)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    OP_A1(0x22, 0x8)
    SetChrPos(0x22, -3000, 0, 57440, 0)
    OP_72(0x408, 0x0)
    ExitThread()

    def lambda_2757():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xE574, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2757)
    OP_22(0x174, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    Sleep(500)

    def lambda_2781():
        OP_8F(0xFE, 0xFFFFF470, 0x0, 0xE574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2781)
    WaitChrThread(0x22, 0x1)

    def lambda_27A1():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xE574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_27A1)
    WaitChrThread(0x22, 0x1)

    def lambda_27C1():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xE574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_27C1)
    WaitChrThread(0x22, 0x1)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0x13)
    OP_22(0x174, 0x0, 0x64)

    def lambda_27F2():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEA88, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_27F2)
    WaitChrThread(0x22, 0x1)
    Sleep(500)

    def lambda_2817():
        OP_8F(0xFE, 0xFFFFF470, 0x0, 0xEA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2817)
    WaitChrThread(0x22, 0x1)

    def lambda_2837():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xEA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2837)
    WaitChrThread(0x22, 0x1)

    def lambda_2857():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2857)
    WaitChrThread(0x22, 0x1)
    Sleep(500)
    OP_22(0x174, 0x0, 0x64)

    def lambda_2881():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2881)
    WaitChrThread(0x22, 0x1)
    Sleep(500)

    def lambda_28A6():
        OP_8F(0xFE, 0xFFFFF470, 0x0, 0xEF9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_28A6)
    WaitChrThread(0x22, 0x1)

    def lambda_28C6():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xEF9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_28C6)
    WaitChrThread(0x22, 0x1)

    def lambda_28E6():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEF9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_28E6)
    WaitChrThread(0x22, 0x1)
    Sleep(500)
    Sleep(300)

    ChrTalk(    #47
        0x10,
        "Hmph. I knew you'd come eventually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        "Today's her last chance, after all.\x02",
    )

    CloseMessageWindow()

    def lambda_2962():
        OP_6D(-3000, 0, 67000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2962)

    def lambda_297A():
        OP_6B(3820, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_297A)

    def lambda_298A():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0x104DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_298A)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x2C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x40)
    SetChrPos(0x1C, -3000, 0, 61340, 0)
    OP_22(0x192, 0x0, 0x64)

    NpcTalk(    #49
        0x1C,
        "Meowing Voice",
        "#6PNya~n.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(70)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A40():
        OP_8F(0xFE, 0xFFFFF45C, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2A40)
    WaitChrThread(0x22, 0x1)

    def lambda_2A60():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2A60)
    WaitChrThread(0x22, 0x1)

    def lambda_2A80():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2A80)
    WaitChrThread(0x22, 0x1)
    OP_22(0x16E, 0x0, 0x50)
    Sleep(500)

    def lambda_2AAA():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xFB2C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2AAA)
    WaitChrThread(0x1C, 0x1)
    OP_22(0x192, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #50
        0x12,
        "#5PYou're kiddin' me. A cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "...No, no. Wait a sec.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        "There might be something else inside.\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_2B8D():
        OP_6D(-2009, 0, 64700, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2B8D)

    def lambda_2BA5():
        OP_6B(3700, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2BA5)

    def lambda_2BB5():
        OP_67(0, 4600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_2BB5)

    def lambda_2BCD():
        OP_6C(30000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_2BCD)

    def lambda_2BDD():
        OP_8E(0xFE, 0xFFFFEE3A, 0x0, 0xF3AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2BDD)
    Sleep(150)

    def lambda_2BFD():
        OP_8E(0xFE, 0xFFFFFA56, 0x0, 0xF794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BFD)
    Sleep(600)

    def lambda_2C1D():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xF794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C1D)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2C4F():
        OP_8E(0xFE, 0x2760, 0x0, 0xFB2C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2C4F)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 225, 500)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 135, 500)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #53
        0x10,
        "Don't let your guard down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        "#1PI know.\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_2CBC():
        OP_6D(-6780, 250, 66570, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2CBC)
    Sleep(500)

    def lambda_2CD9():
        OP_67(0, 4550, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2CD9)

    def lambda_2CF1():
        OP_6C(344000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_2CF1)

    def lambda_2D01():
        OP_6B(1720, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_2D01)

    def lambda_2D11():
        OP_6E(536, 1000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2D11)
    OP_7D(0x0, 0x103, 0x1E, 0x96)
    OP_43(0x103, 0x3, 0x0, 0x12)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x151, 29)
    SetChrSubChip(0x151, 2)
    OP_7D(0x0, 0x151, 0x1E, 0x96)

    def lambda_2D4C():
        OP_96(0xFE, 0xFFFFDFBC, 0xFA, 0xFFEF, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2D4C)
    WaitChrThread(0x151, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x151, 0x0, 0x0)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    Sleep(100)

    def lambda_2D8B():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2D8B)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    TurnDirection(0x10, 0x103, 500)
    Sleep(100)
    OP_1D(0x35)
    Sleep(200)

    ChrTalk(    #55
        0x10,
        "#3SThere they are!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_2DF4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DF4)
    Sleep(50)

    def lambda_2E07():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2E07)
    Sleep(100)

    ChrTalk(    #56
        0x103,
        "#1644F#3S#1PToo late!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2E57():
        OP_6B(1520, 500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2E57)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 13)
    SetChrSubChip(0x103, 0)

    def lambda_2E76():
        OP_8F(0xFE, 0xFFFFEFE8, 0xFA, 0xF6E0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E76)

    def lambda_2E91():
        OP_8F(0xFE, 0xFFFFEBB0, 0xFA, 0xF6E0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2E91)
    Sleep(300)
    OP_44(0x2C, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x151, 0xFF)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x151, 0x4)
    Battle(0x3AE, 0x0, 0x2, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 20)
    Return()

    # Function_17_251A end

    def Function_18_2EE6(): pass

    label("Function_18_2EE6")

    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x103, 13)
    SetChrSubChip(0x103, 2)

    def lambda_2EFB():
        OP_96(0xFE, 0xFFFFE430, 0xFA, 0xFE88, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2EFB)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 12)
    SetChrSubChip(0x103, 3)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x103, 0x0, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x103, 10)
    SetChrSubChip(0x103, 0)

    def lambda_2F44():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F44)
    Return()

    # Function_18_2EE6 end

    def Function_19_2F4D(): pass

    label("Function_19_2F4D")

    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)

    def lambda_2F98():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F98)
    Sleep(200)

    def lambda_2FAB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2FAB)
    Sleep(150)

    def lambda_2FBE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2FBE)
    Sleep(500)
    Return()

    # Function_19_2F4D end

    def Function_20_2FCC(): pass

    label("Function_20_2FCC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x56)
    OP_6D(-3400, 0, 63380, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(35000, 0)
    OP_6E(244, 0)
    ClearMapFlags(0x10)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    SetChrPos(0x22, -1680, 0, 59140, 0)
    OP_A1(0x22, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x10, -2880, 0, 62740, 270)
    SetChrPos(0x11, -2040, 0, 65099, 270)
    SetChrPos(0x12, -1480, 0, 61240, 270)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 3)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0x11, 3)
    SetChrChipByIndex(0x12, 14)
    SetChrSubChip(0x12, 3)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrPos(0x103, -4920, 0, 63180, 90)
    SetChrPos(0x151, -5060, 0, 61700, 90)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    SetChrFlags(0x1C, 0x80)
    SoundLoad(132)
    SoundLoad(521)
    LoadEffect(0x0, "battle\\\\damage5.eff")

    def lambda_313D():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_313D)
    FadeToBright(1000, 0)
    Sleep(1000)

    def lambda_315B():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_315B)
    Sleep(1000)

    ChrTalk(    #57
        0x10,
        "This isn't good...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(100)

    ChrTalk(    #58
        0x103,
        "#1644F#1PNow's our chance, Aina!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(100)

    ChrTalk(    #59
        0x151,
        "#1652FAll right!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrPos(0x13, -4019, 250, 76600, 180)
    SetChrPos(0x14, -1880, 250, 76600, 180)

    def lambda_321C():
        OP_8E(0xFE, 0xFFFFF04D, 0xFA, 0x113C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_321C)

    def lambda_3237():
        OP_6D(-3720, 0, 68980, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3237)
    OP_8C(0x103, 0, 600)
    Sleep(50)

    def lambda_325B():
        OP_8F(0xFE, 0xFFFFF100, 0x0, 0x10554, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_325B)
    Sleep(200)
    OP_43(0x14, 0x3, 0x0, 0x16)

    def lambda_3282():
        OP_8E(0xFE, 0xFFFFED90, 0x0, 0xFF14, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3282)
    WaitChrThread(0x103, 0x1)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x151, 0x1)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x103,
        "#1647FUgh... There's more of them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x151,
        "#1656FNo!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x3)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 4240, 0, 66760, 270)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x16, -5840, 0, 52800, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x17, -4059, 0, 51940, 0)

    def lambda_3368():
        OP_6D(-3360, 0, 65740, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3368)

    def lambda_3380():
        OP_6B(3620, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3380)

    def lambda_3390():
        OP_67(0, 5470, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_3390)

    def lambda_33A8():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x104C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_33A8)

    def lambda_33C3():
        OP_8E(0xFE, 0xFFFFE930, 0x0, 0xEBC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_33C3)

    def lambda_33DE():
        OP_8E(0xFE, 0xFFFFF025, 0x0, 0xE9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_33DE)
    OP_43(0x103, 0x3, 0x0, 0x17)
    OP_43(0x151, 0x3, 0x0, 0x18)
    Sleep(1500)

    def lambda_340C():
        OP_8F(0xFE, 0xFFFFF7CC, 0x0, 0x10C48, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_340C)
    Sleep(1000)

    def lambda_342C():
        OP_8F(0xFE, 0xFFFFEED0, 0x0, 0x10E28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_342C)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(1000)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrChipByIndex(0x18, 28)
    SetChrSubChip(0x18, 0)
    SetChrPos(0x18, -2420, 0, 75240, 0)

    NpcTalk(    #62
        0x18,
        "Man's Voice",
        "#4PNice of you to finally show yourselves.\x02",
    )

    CloseMessageWindow()

    def lambda_34B7():
        OP_6D(-3480, 0, 68000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_34B7)

    def lambda_34CF():
        OP_8E(0xFE, 0xFFFFF68C, 0x0, 0x11620, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_34CF)
    Sleep(200)

    def lambda_34EF():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_34EF)
    Sleep(100)

    def lambda_3502():
        OP_8C(0xFE, 40, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3502)
    Sleep(100)

    def lambda_3515():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3515)
    WaitChrThread(0x18, 0x1)
    Sleep(300)
    WaitChrThread(0x2C, 0x0)

    NpcTalk(    #63
        0x18,
        "Leader",
        (
            "#4PWhat's the hold up? Why haven't you made\x01",
            "an example out of them yet?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #64
        0x18,
        "Leader",
        "#4POur client's waiting. Get a move on.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x18, 0, 500)
    Sleep(200)

    def lambda_35C7():
        OP_6D(-3360, 0, 65740, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_35C7)

    def lambda_35DF():
        OP_8E(0xFE, 0xFFFFF68C, 0x0, 0x125E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_35DF)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x2C, 0x0)

    def lambda_3604():
        OP_8C(0xFE, 230, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3604)
    Sleep(50)

    def lambda_3617():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3617)
    Sleep(50)

    def lambda_362A():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_362A)
    Sleep(500)

    def lambda_363D():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_363D)

    def lambda_364B():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_364B)
    Sleep(100)

    def lambda_366A():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_366A)
    Sleep(100)
    Fade(200)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_3698():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3698)
    Sleep(100)
    Fade(200)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    Fade(200)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)

    def lambda_36DA():
        OP_8C(0xFE, 315, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_36DA)
    Sleep(200)

    def lambda_36ED():
        OP_8F(0xFE, 0xFFFFE340, 0xFA, 0xF870, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_36ED)
    Sleep(300)

    def lambda_370D():
        OP_8F(0xFE, 0xFFFFE78C, 0x0, 0xFC94, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_370D)
    Sleep(200)
    TurnDirection(0x13, 0x103, 400)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x151, 0x1)

    def lambda_373E():
        OP_8E(0xFE, 0xFFFFF5B0, 0x0, 0xFE4B, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_373E)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #65
        0x11,
        (
            "You're reeeally gonna regret messing with us,\x01",
            "kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        (
            "I hope you don't expect to just be able to walk\x01",
            "away after showing yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #67
        0x11,
        "First, I'm gonna kill you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "The other young lady can live a while longer.\x01",
            "She's still useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "As long as we can get her to write her own will,\x01",
            "it'll save us having to forge one later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#1646F...\x02\x03",

            "#1648FYou really think this will be that simple?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x11,
        (
            "Hmph. If you think saying that is going to\x01",
            "unnerve us, you've got another thing coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#1642F(...Aina.)\x02\x03",

            "(You can still run, right?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x151,
        "#1652F(Y-Yes...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#1646F(I'll take all of these guys on myself.)\x02\x03",

            "(While I'm doing that, you run!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x151,
        (
            "#1653F(What?!)\x02\x03",

            "#1652F(Y-You can't take this many opponents on\x01",
            "yourself and have any chance of winning!\x01",
            "You'll...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        "Heh. Not going to beg for mercy, I take it?\x02",
    )

    CloseMessageWindow()

    def lambda_3AB6():
        OP_8E(0xFE, 0xFFFFEA48, 0x0, 0xFC94, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AB6)
    Sleep(200)

    def lambda_3AD6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3AD6)

    def lambda_3AE4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3AE4)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #77
        0x103,
        (
            "#1644FYou've got something you need to do--and so do I!\x02\x03",

            "So let's just do them!\x02\x03",

            "#1641FDon't worry about me. As if I have any intention\x01",
            "of dying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "What are you even talking abo--\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3BC1():
        OP_6B(3260, 400)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3BC1)
    OP_43(0x103, 0x3, 0x0, 0x19)
    Sleep(500)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x11, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)

    def lambda_3C21():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3C21)

    def lambda_3C3B():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xFE4B, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3C3B)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0x11, 3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #79
        0x11,
        "Gaaah!\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x10)

    ChrTalk(    #80
        0x12,
        "D-Damn you!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x15, 25)
    SetChrSubChip(0x15, 0)
    Sleep(100)
    Fade(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x13, 25)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x16, 25)
    SetChrSubChip(0x16, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(70)
    Fade(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 25)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x17, 25)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x10, 0)
    Sleep(100)

    ChrTalk(    #81
        0x103,
        "#1642FGo, Aina!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #82
        0x151,
        "#1652FB-But!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        "#1644F#3SI said, GO!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 13280, 0, 65040, 270)
    OP_20(0xBB8)

    NpcTalk(    #84
        0x1A,
        "Young Man's Voice",
        (
            "You seem to be having a little trouble over there,\x01",
            "Scherazard.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_3EFB():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3EFB)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)

    def lambda_3F13():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3F13)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)

    def lambda_3F2B():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3F2B)
    SetChrChipByIndex(0x13, 0)
    SetChrSubChip(0x13, 0)

    def lambda_3F43():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3F43)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 0)

    def lambda_3F5B():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3F5B)
    SetChrChipByIndex(0x15, 0)
    SetChrSubChip(0x15, 0)

    def lambda_3F73():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3F73)
    SetChrChipByIndex(0x16, 0)
    SetChrSubChip(0x16, 0)

    def lambda_3F8B():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3F8B)
    SetChrChipByIndex(0x17, 0)
    SetChrSubChip(0x17, 0)

    def lambda_3FA3():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3FA3)
    Sleep(300)

    ChrTalk(    #85
        0x103,
        "#1643FWhat...?\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3FCB():
        OP_8E(0xFE, 0x2C10, 0x0, 0xFE10, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_3FCB)

    def lambda_3FE6():
        OP_6D(11520, 0, 65040, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3FE6)

    def lambda_3FFE():
        OP_67(0, 4040, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3FFE)

    def lambda_4016():
        OP_6B(3500, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4016)

    def lambda_4026():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_4026)
    WaitChrThread(0x2C, 0x0)
    Sleep(300)
    SetChrPos(0x11, -900, 0, 65040, 90)
    SetChrPos(0x10, -2880, 0, 63240, 90)
    SetChrPos(0x12, -1480, 0, 61740, 45)
    SetChrPos(0x16, -5840, 0, 61060, 45)
    SetChrPos(0x17, -4059, 0, 60140, 45)
    SetChrPos(0x13, -4700, 0, 68980, 135)
    SetChrPos(0x14, -2400, 0, 68500, 135)
    SetChrPos(0x15, -900, 0, 66760, 90)

    ChrTalk(    #86
        0x11,
        "#5PWho the hell are you?!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, -5560, 0, 65040, 90)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)

    ChrTalk(    #87
        0x103,
        (
            "#1643F#5PK-Kurt...?\x02\x03",

            "What are you doing here?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4136():
        OP_6D(2860, 0, 65040, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_4136)

    def lambda_414E():
        OP_67(0, 5400, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_414E)

    def lambda_4166():
        OP_6B(3760, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4166)

    def lambda_4176():
        OP_8E(0xFE, 0x1194, 0x0, 0xFE10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4176)
    WaitChrThread(0x1A, 0x1)
    WaitChrThread(0x2C, 0x0)

    ChrTalk(    #88
        0x1A,
        (
            "#840F#5PHave you forgotten that I'm affiliated with the\x01",
            "Grancel branch of the guild? I see nothing odd\x01",
            "about my presence here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        "#1643F#5PW-Well, I know, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x1A,
        (
            "#840F#5PI'm happy that you seem to have realized exactly\x01",
            "what it is that you must do.\x02\x03",

            "#842FBut I can't say I'm as pleased about how willing\x01",
            "you appear to be to throw away your life without\x01",
            "first exploring other options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        "#1642FI-I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x1A,
        (
            "#843F#5PI can't entirely fault your decision from the\x01",
            "perspective of a bracer, but I would like you to\x01",
            "give a little more attention to your surroundings.\x02\x03",

            "I'm well aware that you seem staunchly opposed\x01",
            "to relying on others...\x02\x03",

            "#840F...but take a good look at the situation you're \x01",
            "currently in, and tell me exactly what it is that\x01",
            "you should really be doing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #93
        0x103,
        (
            "#1646F...Kurt.\x02\x03",

            "#1644FCan you take care of things here for me?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x33)
    Fade(500)

    def lambda_4500():
        OP_6D(3300, 0, 65040, 100)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_4500)

    def lambda_4518():
        OP_6B(3400, 100)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4518)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1A, 31)
    SetChrSubChip(0x1A, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #94
        0x1A,
        "#843F#5PCertainly.\x02",
    )

    CloseMessageWindow()
    Battle(0x2710, 0x30000B, 0x0, 0x0, 0xFF)
    Call(0, 21)
    Return()

    # Function_20_2FCC end

    def Function_21_4561(): pass

    label("Function_21_4561")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x33)
    OP_82(0x82, 0x0)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_6D(-2240, 0, 65600, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(244, 0)
    SetMapFlags(0x10)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    SetChrPos(0x22, -1520, 0, 58740, 0)
    OP_A1(0x22, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x10, -1840, 0, 66660, 90)
    SetChrPos(0x11, -1700, 0, 64500, 90)
    SetChrPos(0x12, -2660, 0, 68480, 135)
    SetChrPos(0x13, 1360, 0, 68480, 180)
    SetChrPos(0x16, 60, 250, 61100, 0)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x16, 9)
    SetChrSubChip(0x16, 0)
    SetChrPos(0x14, -5140, 0, 61740, 45)
    SetChrPos(0x15, -2220, 0, 62900, 45)
    SetChrPos(0x17, -1400, 0, 61340, 45)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 840, 0, 66460, 225)
    SetChrChipByIndex(0x1A, 31)
    SetChrSubChip(0x1A, 0)
    SetChrPos(0x103, -4540, 0, 66200, 90)
    SetChrPos(0x151, -4600, 0, 64400, 90)

    def lambda_4756():
        OP_6B(3760, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4756)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4786():
        OP_8F(0xFE, 0xFFFFF830, 0x0, 0xED44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4786)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_47B8():
        OP_8F(0xFE, 0xFFFFEAC0, 0x0, 0xF000, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_47B8)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_47EA():
        OP_8F(0xFE, 0xFFFFF36C, 0x0, 0xF1CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_47EA)
    OP_0D()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #95
        0x103,
        "#1644F#1PNow, Aina!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #96
        0x151,
        "#1652FR-Right!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 600)
    Sleep(100)

    def lambda_4857():
        OP_8E(0xFE, 0xFFFFEF34, 0x0, 0x12674, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4857)
    Sleep(100)

    def lambda_4877():
        OP_8E(0xFE, 0xFFFFEED0, 0x0, 0x1228C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4877)
    Sleep(400)
    OP_8C(0x14, 0, 500)
    Sleep(200)

    ChrTalk(    #97
        0x14,
        "They're getting away!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 45, 500)
    Sleep(200)

    ChrTalk(    #98
        0x14,
        (
            "Half of us should be enough to take care\x01",
            "of this guy. Everyone else--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4915():
        OP_6D(-1900, 0, 63560, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_4915)

    def lambda_492D():
        OP_6C(36000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_492D)
    WaitChrThread(0x2C, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrPos(0x1B, -4000, 0, 51040, 0)
    OP_22(0x209, 0x0, 0x64)

    NpcTalk(    #99 op#A
        0x19,
        "Man in Black",
        "#3S#1P#10AAaargh!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x8)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x19, -5200, 0, 53660, 180)
    SetChrChipByIndex(0x19, 15)
    SetChrSubChip(0x19, 0)

    def lambda_49C3():
        OP_96(0xFE, 0xFFFFEBB0, 0x0, 0xDF0C, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_49C3)
    WaitChrThread(0x19, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    OP_8C(0x19, 0, 0)
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    Sleep(1000)
    OP_22(0x209, 0x0, 0x64)

    NpcTalk(    #100 op#A
        0x18,
        "Man in Black",
        "#3S#1P#10AWhat?!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8)
    SetChrFlags(0x18, 0x40)
    SetChrPos(0x18, -3100, 0, 54060, 180)
    SetChrChipByIndex(0x18, 15)
    SetChrSubChip(0x18, 0)

    def lambda_4A63():
        OP_96(0xFE, 0xFFFFF3E4, 0x0, 0xE31C, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4A63)
    WaitChrThread(0x18, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    OP_8C(0x18, 45, 0)
    SetChrChipByIndex(0x18, 9)
    SetChrSubChip(0x18, 0)
    Sleep(800)

    NpcTalk(    #101
        0x1B,
        "Man's Voice",
        "#1PSorry for the delay, Kurt.\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_4AD1():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4AD1)
    Sleep(50)

    def lambda_4AE4():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4AE4)
    Sleep(50)

    def lambda_4AF7():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4AF7)
    Sleep(500)
    Fade(1000)
    OP_6D(-3560, 0, 50340, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(145000, 0)
    OP_6E(324, 0)
    SetChrPos(0x10, -1840, 0, 65660, 90)
    SetChrPos(0x11, -1700, 0, 63500, 180)
    SetChrPos(0x12, -6330, 0, 48660, 315)
    SetChrPos(0x13, -2460, 0, 47180, 220)
    SetChrFlags(0x12, 0x800)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x16, -260, 250, 60700, 90)
    SetChrPos(0x14, -5440, 0, 59940, 180)
    SetChrPos(0x15, -3220, 0, 60400, 180)
    SetChrPos(0x17, -2000, 0, 59240, 180)
    SetChrPos(0x18, -2700, 0, 56540, 45)
    SetChrPos(0x19, -5660, 0, 56200, 0)
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x22, -1520, 0, 57740, 0)
    SetChrPos(0x1A, 840, 0, 65459, 225)
    SetChrPos(0x1B, -4000, 0, 50840, 0)

    def lambda_4C3E():
        OP_6D(-2780, 0, 58340, 3500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_4C3E)

    def lambda_4C56():
        OP_6C(132000, 3500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4C56)

    def lambda_4C66():
        OP_6B(2600, 3500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4C66)

    def lambda_4C76():
        OP_8E(0xFE, 0xFFFFF060, 0x0, 0xDCC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4C76)
    Sleep(1000)
    SetChrChipByIndex(0x1A, 32)
    SetChrSubChip(0x1A, 0)

    def lambda_4CA0():
        OP_8E(0xFE, 0xFFFFF060, 0x0, 0xFB2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4CA0)
    Sleep(500)

    def lambda_4CC0():
        OP_8F(0xFE, 0xFFFFEAC0, 0x0, 0xEC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4CC0)
    Sleep(200)

    def lambda_4CE0():
        OP_8F(0xFE, 0xFFFFF36C, 0x0, 0xEDE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4CE0)
    Sleep(200)

    def lambda_4D00():
        OP_8F(0xFE, 0xFFFFF830, 0x0, 0xE95C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D00)
    WaitChrThread(0x1A, 0x1)
    TurnDirection(0x1A, 0x1B, 500)
    SetChrChipByIndex(0x1A, 31)
    SetChrSubChip(0x1A, 0)
    Sleep(200)

    ChrTalk(    #102
        0x1A,
        (
            "#840FNot at all. I've largely taken care of them\x01",
            "as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x1B,
        "Heh. You sure do fast work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x1B,
        (
            "Though I'm more surprised to see that obstinate\x01",
            "young lady finally came to her senses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x1B,
        (
            "When she was with the Zeiss branch, she was\x01",
            "more like a wild boar, always charging forward\x01",
            "without stopping to take a look around her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x1A,
        (
            "#841FHaha... I've always known she has what it takes\x01",
            "to be an excellent bracer.\x02\x03",

            "#840FShe'd merely lost sight of something important\x01",
            "and needed to be put back on track.\x02\x03",

            "Given the opportunity, she was always perfectly\x01",
            "capable of doing so.\x02\x03",

            "She'll be able to get much stronger than she is\x01",
            "now that she's righted herself. I'm sure of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x1B,
        "Ahhh, to be young again.\x02",
    )

    CloseMessageWindow()
    OP_43(0x14, 0x3, 0x0, 0x1A)
    OP_43(0x17, 0x3, 0x0, 0x1B)
    Sleep(500)
    OP_8C(0x15, 345, 500)
    Sleep(300)

    ChrTalk(    #108
        0x14,
        "Qu-Quit acting like we're not even here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x14,
        "#3SKill them both!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    Sleep(200)
    SetChrChipByIndex(0x17, 25)
    SetChrSubChip(0x17, 0)
    Sleep(50)
    SetChrChipByIndex(0x15, 25)
    SetChrSubChip(0x15, 0)
    Sleep(50)
    SetChrChipByIndex(0x14, 25)
    SetChrSubChip(0x14, 0)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_4561 end

    def Function_22_50AE(): pass

    label("Function_22_50AE")


    def lambda_50B4():
        OP_8E(0xFE, 0xFFFFF8A8, 0xFA, 0x113C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_50B4)
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x103, 500)
    Return()

    # Function_22_50AE end

    def Function_23_50D6(): pass

    label("Function_23_50D6")

    Sleep(300)
    OP_8C(0x103, 90, 500)
    Sleep(1000)

    def lambda_50ED():
        OP_8F(0xFE, 0xFFFFEB10, 0x0, 0xFF8C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50ED)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_23_50D6 end

    def Function_24_5108(): pass

    label("Function_24_5108")

    Sleep(500)
    OP_8C(0x151, 180, 500)
    Sleep(300)

    def lambda_511F():
        OP_8E(0xFE, 0xFFFFED90, 0x0, 0xF424, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_511F)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    def lambda_5144():
        OP_8F(0xFE, 0xFFFFEAAC, 0x0, 0xFADC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5144)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_24_5108 end

    def Function_25_515F(): pass

    label("Function_25_515F")


    ChrTalk(    #110 op#A
        0x103,
        "#1644F#3S#5AHah!\x02",
    )

    Sleep(200)
    SetChrChipByIndex(0x103, 11)
    SetChrSubChip(0x103, 0)

    def lambda_5189():
        OP_99(0xFE, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5189)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_25_515F end

    def Function_26_5199(): pass

    label("Function_26_5199")

    OP_8C(0x14, 30, 600)
    Sleep(300)
    OP_8C(0x14, 165, 600)
    Sleep(300)
    Return()

    # Function_26_5199 end

    def Function_27_51B2(): pass

    label("Function_27_51B2")

    Sleep(150)
    OP_8C(0x17, 345, 600)
    Sleep(500)
    OP_8C(0x17, 210, 600)
    Sleep(300)
    Return()

    # Function_27_51B2 end

    def Function_28_51D0(): pass

    label("Function_28_51D0")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_522F")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #111
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5285")

    label("loc_522F")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #112
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5285")

    OP_59()
    Fade(500)
    SetChrPos(0x103, -8900, 0, 19840, 0)
    SetChrPos(0x151, -8900, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_28_51D0 end

    def Function_29_52B6(): pass

    label("Function_29_52B6")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5315")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #113
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536B")

    label("loc_5315")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #114
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_536B")

    OP_59()
    Fade(500)
    SetChrPos(0x103, -3600, 0, 19840, 0)
    SetChrPos(0x151, -3600, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_29_52B6 end

    def Function_30_539C(): pass

    label("Function_30_539C")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_53FB")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #115
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5451")

    label("loc_53FB")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #116
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5451")

    OP_59()
    Fade(500)
    SetChrPos(0x103, 3600, 0, 19840, 0)
    SetChrPos(0x151, 3600, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_30_539C end

    def Function_31_5482(): pass

    label("Function_31_5482")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_54E1")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #117
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5537")

    label("loc_54E1")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #118
        0x103,
        (
            "#1642FWe don't have time to take any detours.\x02\x03",

            "To Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5537")

    OP_59()
    Fade(500)
    SetChrPos(0x103, 8900, 0, 19840, 0)
    SetChrPos(0x151, 8900, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_31_5482 end

    def Function_32_5568(): pass

    label("Function_32_5568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 0)), scpexpr(EXPR_END)), "loc_5A02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_57E5")

    def lambda_557C():
        OP_6D(27200, 0, 65239, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_557C)

    def lambda_5594():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_5594)

    def lambda_55AC():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_55AC)

    def lambda_55BC():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_55BC)
    WaitChrThread(0x2C, 0x0)
    Sleep(500)
    LoadEffect(0x3, "map\\\\mp032_00.eff")

    def lambda_55EA():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFDE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_55EA)
    WaitChrThread(0x1E, 0x1)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_564E():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_564E)
    WaitChrThread(0x1E, 0x1)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_56B2():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFBF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_56B2)
    WaitChrThread(0x1E, 0x1)

    NpcTalk(    #119
        0x1E,
        "Freckled Girl",
        "#1661FHeehee. Now that's a good expression! ♪\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #120
        0x16,
        (
            "I'm gonna wipe the smile off your face in\x01",
            "a minute!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Jump("loc_59FF")

    label("loc_57E5")


    def lambda_57EB():
        OP_6D(27200, 0, 65239, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_57EB)

    def lambda_5803():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_5803)

    def lambda_581B():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_581B)

    def lambda_582B():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_582B)
    WaitChrThread(0x2C, 0x0)
    Sleep(500)

    NpcTalk(    #121
        0x1E,
        "Freckled Girl",
        "#1660FAll right, then!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1E, 23)
    SetChrSubChip(0x1E, 0)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #122
        0x16,
        "I am SO going to beat the living daylights of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x17,
        "Woah now. Don't go leaving your post.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x17,
        (
            "It sounds like the one escorting her is pretty\x01",
            "tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        "Don't let your guard down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x16,
        "I-I know, but still...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x1)

    label("loc_59FF")

    Jump("loc_5E88")

    label("loc_5A02")

    OP_6D(27200, 0, 65239, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1E, 15020, 0, 64500, 90)

    def lambda_5A56():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFBF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5A56)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1E, 0x1)
    Sleep(300)

    NpcTalk(    #127
        0x1E,
        "Freckled Girl",
        (
            "#1662FWow! Your clothes are so black!\x02\x03",

            "They're really cute.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x1E, 0x3, 0x0, 0x22)

    def lambda_5ADB():

        label("loc_5ADB")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_5ADB")

    QueueWorkItem2(0x16, 0, lambda_5ADB)

    def lambda_5AEC():

        label("loc_5AEC")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_5AEC")

    QueueWorkItem2(0x17, 0, lambda_5AEC)
    Sleep(1000)

    ChrTalk(    #128
        0x16,
        "Wh-Who the hell are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x17,
        "You're in our way. Get lost!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x17,
        "Shoo! Shoo!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #131
        0x1E,
        "Freckled Girl",
        (
            "#1661FYou're both dressed the same, too! Is that your\x01",
            "uniform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x16,
        "Who is this kid?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 32740, 0, 62540, 270)

    def lambda_5BD2():
        OP_8E(0xFE, 0x607C, 0x0, 0xF44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5BD2)
    Sleep(2000)

    NpcTalk(    #133
        0x1D,
        "Unkempt Man",
        (
            "#145FUgh... My head... I must've had waaay too much to\x01",
            "drink...\x02\x03",

            "#142FI feel like I'm forgetting somethin' important, too...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1D, 0x1)
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x1E, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x1D)

    NpcTalk(    #134
        0x1D,
        "Unkempt Man",
        (
            "#145F#4P...Nope. Can't remember.\x02\x03",

            "I guess it can't have been anything too important...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D23():
        OP_8E(0xFE, 0x490C, 0x0, 0xF44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5D23)
    Sleep(2000)
    OP_44(0x1E, 0x2)
    OP_44(0x1E, 0x3)

    def lambda_5D4B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_5D4B)
    OP_8F(0x1E, 0x61BC, 0x0, 0xFBF4, 0x7D0, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    Fade(250)
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    OP_8C(0x16, 270, 0)
    OP_8C(0x17, 270, 0)
    Sleep(250)

    NpcTalk(    #135
        0x1E,
        "Freckled Girl",
        "#1660FCan I take a photo of you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x16,
        "Like hell you can!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x16,
        "Get out of our sight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x17,
        "We can't leave our posts!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x17,
        (
            "Consider yourself lucky, kiddo. We'll let you\x01",
            "leave this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x17,
        "So go play somewhere else!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x1D, 0xFF)
    SetChrFlags(0x1D, 0x80)
    OP_A2(0x2F58)

    label("loc_5E88")

    Return()

    # Function_32_5568 end

    def Function_33_5E89(): pass

    label("Function_33_5E89")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EED")

    def lambda_5E98():
        OP_8E(0xFE, 0x68BA, 0x0, 0xFD3E, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5E98)
    WaitChrThread(0x1E, 0x0)
    OP_8C(0x1E, 45, 500)
    Sleep(1500)

    def lambda_5EC4():
        OP_8E(0xFE, 0x6964, 0x0, 0xFA63, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5EC4)
    WaitChrThread(0x1E, 0x0)
    OP_8C(0x1E, 135, 500)
    Sleep(1800)
    Jump("Function_33_5E89")

    label("loc_5EED")

    Return()

    # Function_33_5E89 end

    def Function_34_5EEE(): pass

    label("Function_34_5EEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F80")

    def lambda_5EFD():

        label("loc_5EFD")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_5EFD")

    QueueWorkItem2(0x1E, 2, lambda_5EFD)
    OP_8F(0x1E, 0x661C, 0x0, 0xFEB0, 0x5DC, 0x0)
    Sleep(800)
    OP_8F(0x1E, 0x68D8, 0x0, 0xFBF4, 0x5DC, 0x0)
    Sleep(800)

    def lambda_5F40():

        label("loc_5F40")

        TurnDirection(0xFE, 0x17, 500)
        OP_48()
        Jump("loc_5F40")

    QueueWorkItem2(0x1E, 2, lambda_5F40)
    OP_8F(0x1E, 0x661C, 0x0, 0xF938, 0x5DC, 0x0)
    Sleep(800)
    OP_8F(0x1E, 0x68D8, 0x0, 0xFBF4, 0x5DC, 0x0)
    Sleep(800)
    Jump("Function_34_5EEE")

    label("loc_5F80")

    Return()

    # Function_34_5EEE end

    def Function_35_5F81(): pass

    label("Function_35_5F81")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-2940, 0, 52140, 0)
    OP_67(0, 9380, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -3900, 0, 56200, 180)
    SetChrChipByIndex(0x10E, 16)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, -3900, 0, 57200, 180)

    def lambda_6001():
        OP_8E(0xFE, 0xFFFFF0C4, 0x0, 0xC1C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6001)
    Sleep(50)

    def lambda_6021():
        OP_8E(0xFE, 0xFFFFF0C4, 0x0, 0xC79C, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_6021)

    def lambda_603C():
        OP_67(0, 6380, -10000, 4600)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_603C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #141
        0x10E,
        "Sister Ellen",
        "#5PWhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x26,
        (
            "It looks like your plan ended up working,\x01",
            "Julia.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #143
        0x10E,
        "Sister Ellen",
        "#5PF-Fortunately, yes...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x10E, 500)
    Sleep(300)

    NpcTalk(    #144
        0x10E,
        "Sister Ellen",
        "#5PI'm sorry for causing you trouble yet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x26,
        "Haha. Not to worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x26,
        (
            "You have my sympathies, even. Those seemed\x01",
            "to be some very fervent admirers back there.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, -23400, 0, 50100, 90)
    Fade(1000)
    OP_6D(-14740, 0, 50100, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(270000, 0)

    def lambda_61FA():
        OP_8E(0xFE, 0xFFFFC9B4, 0x0, 0xC3B4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_61FA)
    WaitChrThread(0x27, 0x1)
    SetChrPos(0x26, -5900, 0, 49600, 0)
    SetChrPos(0x10E, -5900, 0, 50980, 180)
    OP_62(0x27, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #147
        0x27,
        "#270F#5P...Hmm?\x02",
    )

    CloseMessageWindow()

    def lambda_6268():
        OP_6D(-7120, 0, 51280, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_6268)

    def lambda_6280():
        OP_67(0, 6900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_6280)

    def lambda_6298():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_6298)

    def lambda_62A8():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_62A8)

    def lambda_62B8():
        OP_8E(0xFE, 0xFFFFE1EC, 0x0, 0xC3B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_62B8)
    WaitChrThread(0x27, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6306():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x10E, 2, lambda_6306)
    Sleep(150)
    OP_8C(0x26, 270, 500)
    Sleep(300)

    NpcTalk(    #148
        0x10E,
        "Sister Ellen",
        "(M-Major Vander?!)\x02",
    )

    CloseMessageWindow()

    def lambda_634A():
        OP_8F(0xFE, 0xFFFFEBEC, 0x0, 0xC47C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_634A)
    Sleep(300)

    def lambda_636A():
        OP_8F(0xFE, 0xFFFFE8F4, 0x0, 0xC3B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_636A)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #149
        0x10E,
        "Sister Ellen",
        "(Wh-What is he doing here?!)\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #150
        0x10E,
        "Sister Ellen",
        "(I thought he had already left Liberl!)\x02",
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x27)
    Sleep(500)

    ChrTalk(    #151
        0x27,
        (
            "#277F#5PThis is quite a surprise.\x02\x03",

            "#278FI wasn't aware you were also a sister of the \x01",
            "church, Captain Schwarz.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #152
        0x10E,
        "Sister Ellen",
        "Y-You can tell?!\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10E, 0, 500)
    Sleep(600)

    NpcTalk(    #153
        0x10E,
        "Sister Ellen",
        "I-I... I... Umm... Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x27,
        (
            "#272F#5PI should be back in Erebonia, but I still\x01",
            "have a little cleaning up after that fool\x01",
            "to do.\x02\x03",

            "So I ended up having to come back here\x01",
            "again in the end.\x02\x03",

            "#277FI would have liked to take the time to go\x01",
            "and greet you, but the chance ultimately\x01",
            "never presented itself.\x02\x03",

            "#278FNevertheless, I'm pleased we were able to\x01",
            "meet again, Captain...\x02\x03",

            "#275F...or is it 'Sister Julia' now?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x10E, 0x27, 500)
    Sleep(300)

    NpcTalk(    #155
        0x10E,
        "Sister Julia",
        "M-Major!\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #156
        0x26,
        "#6PHmm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x10E, 500)
    Sleep(300)

    ChrTalk(    #157
        0x26,
        (
            "#5PIt appears to me that there is little point in\x01",
            "trying to disguise your identity from this man.\x01",
            "Perhaps you need needn't bother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x26,
        (
            "#5PRegardless, I've preparations to make for this\x01",
            "afternoon's mass, so I should excuse myself.\x01",
            "Good day to you both.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6806():

        label("loc_6806")

        TurnDirection(0xFE, 0x26, 500)
        OP_48()
        Jump("loc_6806")

    QueueWorkItem2(0x10E, 2, lambda_6806)

    def lambda_6817():

        label("loc_6817")

        TurnDirection(0xFE, 0x26, 500)
        OP_48()
        Jump("loc_6817")

    QueueWorkItem2(0x27, 2, lambda_6817)
    OP_43(0x26, 0x3, 0x0, 0x25)
    Sleep(400)

    NpcTalk(    #159 op#A op#5
        0x10E,
        "Sister Julia",
        "#20AA-Archbishop?!\x05\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x27, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    OP_63(0x27)
    Sleep(500)
    OP_44(0x10E, 0x2)
    OP_44(0x27, 0x2)

    ChrTalk(    #160
        0x27,
        (
            "#276F#11PSo that was the famous Archbishop Currant,\x01",
            "was it?\x02\x03",

            "#272FPerhaps I should have taken that chance to \x01",
            "introduce myself properly to him.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6930():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0xC418, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_6930)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #161
        0x10E,
        "Sister Julia",
        "#4PErm... Major?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x10E, 400)
    Sleep(500)

    NpcTalk(    #162
        0x10E,
        "Sister Julia",
        (
            "#4PI should probably explain how I ended up in\x01",
            "this situation... You see, umm...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x23, -5700, 0, 63140, 180)
    SetChrPos(0x25, -4640, 0, 62420, 180)
    SetChrPos(0x24, -4840, 0, 63800, 180)

    NpcTalk(    #163
        0x23,
        "Woman's Voice",
        (
            "Aww... I wish I could've stayed a while longer,\x01",
            "but I've really got to get going...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #164
        0x24,
        "Woman's Voice",
        (
            "I wish I could've gotten a close look at Julia,\x01",
            "though. I thought this was finally going to be\x01",
            "my chance...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #165
        0x25,
        "Girl's Voice",
        "Ahhh... She's so dreamy... ㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10E, 0, 500)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrPos(0x23, -3000, 0, 76060, 180)
    SetChrPos(0x24, -3700, 0, 76980, 180)
    SetChrPos(0x25, -2300, 0, 76980, 180)

    def lambda_6BA7():
        OP_6D(-3000, 0, 68980, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_6BA7)

    def lambda_6BBF():
        OP_67(0, 6900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_6BBF)

    def lambda_6BD7():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_6BD7)

    def lambda_6BE7():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_6BE7)
    Sleep(2000)

    def lambda_6BFC():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0xDE94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6BFC)
    Sleep(50)

    def lambda_6C1C():
        OP_8E(0xFE, 0xFFFFF18C, 0x0, 0xDE94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6C1C)
    Sleep(50)

    def lambda_6C3C():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xDAFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6C3C)
    Sleep(3000)
    SetChrPos(0x27, -7700, 0, 49900, 0)
    Fade(1000)
    OP_6D(-7120, 0, 51280, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_44(0x23, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x25, 0xFF)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(800)
    OP_8C(0x27, 90, 500)
    Sleep(1000)

    def lambda_6CDF():
        OP_8F(0xFE, 0xFFFFE890, 0x0, 0xC15C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_6CDF)
    WaitChrThread(0x10E, 0x1)
    OP_63(0x10E)
    Sleep(200)

    NpcTalk(    #166
        0x10E,
        "Sister Julia",
        "#6P(Argh. They're starting to make their way back!)\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #167
        0x10E,
        "Sister Julia",
        "#6P(If they find me here, I'm doomed...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1700)
    OP_63(0x27)
    Sleep(500)

    ChrTalk(    #168
        0x27,
        (
            "#276F#5P...Should you like, Captain, I would be happy to\x01",
            "help you disguise yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 270, 500)
    Sleep(300)

    NpcTalk(    #169
        0x10E,
        "Sister Julia",
        "#4PPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x27,
        (
            "#272F#5PI can't pretend to be familiar with your situation,\x01",
            "but I can see you aren't comfortable with being\x01",
            "discovered here.\x02\x03",

            "#277FIn these situations, your instinct may be to hide,\x01",
            "but I believe the best thing to do is the exact\x01",
            "opposite.\x02\x03",

            "If it works for you, I'd be happy to accompany you\x01",
            "somewhere a little safer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #171
        0x10E,
        "Sister Julia",
        "#4PO-Oh, my... Thank you.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x23, -5700, 0, 63140, 180)
    SetChrPos(0x24, -4640, 0, 62420, 180)
    SetChrPos(0x25, -4840, 0, 63800, 180)

    NpcTalk(    #172
        0x23,
        "Woman's Voice",
        "Ahhh... Juliaaa... ㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10E, 0, 500)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x10E, 270, 500)
    Sleep(300)

    NpcTalk(    #173
        0x10E,
        "Sister Julia",
        "#4PP-Please do! Right away!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x27,
        "#277F#5PMy pleasure.\x02",
    )

    CloseMessageWindow()

    def lambda_7083():

        label("loc_7083")

        TurnDirection(0xFE, 0x27, 500)
        OP_48()
        Jump("loc_7083")

    QueueWorkItem2(0x10E, 2, lambda_7083)
    OP_43(0x27, 0x3, 0x0, 0x26)
    Sleep(200)
    OP_43(0x10E, 0x3, 0x0, 0x27)
    Sleep(3000)
    SetChrPos(0x23, -3000, 0, 70060, 180)
    SetChrPos(0x24, -3700, 0, 70980, 180)
    SetChrPos(0x25, -2300, 0, 70980, 180)

    def lambda_70DF():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xB3EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_70DF)
    Sleep(50)

    def lambda_70FF():
        OP_8E(0xFE, 0xFFFFF18C, 0x0, 0xF71C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_70FF)
    Sleep(50)

    def lambda_711F():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0xB784, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_711F)
    Fade(1000)
    OP_6D(-3040, 0, 63960, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x24, 0x1)
    OP_62(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_719D():

        label("loc_719D")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_719D")

    QueueWorkItem2(0x24, 2, lambda_719D)

    ChrTalk(    #175 op#A op#5
        0x24,
        "#15A#6PHmm...?\x05\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x3)
    OP_44(0x24, 0x2)

    ChrTalk(    #176
        0x24,
        (
            "#6PNever mind. I suppose it was just my imagination.\x01",
            "It must have been!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x24, 180, 400)

    def lambda_7220():
        OP_8E(0xFE, 0xFFFFF18C, 0x0, 0xB590, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7220)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_5F81 end

    def Function_36_724D(): pass

    label("Function_36_724D")

    SetPlaceName(0xB4)
    Return()

    # Function_36_724D end

    def Function_37_7251(): pass

    label("Function_37_7251")

    OP_8C(0x26, 225, 500)

    def lambda_725E():
        OP_8E(0xFE, 0xFFFFE570, 0x0, 0xBF68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_725E)
    WaitChrThread(0x26, 0x1)

    def lambda_727E():
        OP_8E(0xFE, 0xFFFFBCD0, 0x0, 0xBF68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_727E)
    WaitChrThread(0x26, 0x1)
    Return()

    # Function_37_7251 end

    def Function_38_7299(): pass

    label("Function_38_7299")


    def lambda_729F():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0xC2EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_729F)
    WaitChrThread(0x27, 0x1)
    Sleep(400)

    def lambda_72C4():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_72C4)
    WaitChrThread(0x27, 0x1)

    def lambda_72E4():
        OP_8E(0xFE, 0x2328, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_72E4)
    WaitChrThread(0x27, 0x1)
    Return()

    # Function_38_7299 end

    def Function_39_72FF(): pass

    label("Function_39_72FF")


    def lambda_7305():
        OP_8F(0xFE, 0xFFFFE890, 0x0, 0xBFCC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_7305)
    WaitChrThread(0x10E, 0x1)
    OP_44(0x10E, 0x2)
    Sleep(400)
    Sleep(400)

    def lambda_7333():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_7333)
    WaitChrThread(0x10E, 0x1)

    def lambda_7353():
        OP_8E(0xFE, 0x2328, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_7353)
    WaitChrThread(0x10E, 0x1)
    Return()

    # Function_39_72FF end

    SaveToFile()

Try(main)
