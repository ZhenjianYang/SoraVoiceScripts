from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0810   ._SN',
        MapName             = 'Event',
        Location            = 'E0810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0810   ._SN',
            'ED6_DT21/E0810_1 ._SN',
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
        'Loewe',                                # 9
        'Captain Schwarz',                      # 10
        'General Morgan',                       # 11
        'Nial',                                 # 12
        'Dorothy',                              # 13
        'Ancient Dragon Ragnard',               # 14
        'Airship',                              # 15
        'Airship',                              # 16
        'Airship',                              # 17
        'Airship',                              # 18
        'Airship',                              # 19
        'Airship',                              # 20
        'Targeting Camera',                     # 21
        'Targeting Camera',                     # 22
        'Target',                               # 23
        'Target',                               # 24
        'Target',                               # 25
        'Target',                               # 26
        'Professor Weissmann',                  # 27
        'Gospel',                               # 28
        'Renne',                                # 29
        'Pater-Mater',                          # 30
        'Reverie Dragion',                      # 31
        'Estelle',                              # 32
        'Joshua',                               # 33
        'Cassius',                              # 34
        'Sieg',                                 # 35
        'Major Vander',                         # 36
        'Professor Russell',                    # 37
        'Don',                                  # 38
        'Kyle',                                 # 39
        'Agate',                                # 40
        'Scherazard',                           # 41
        'Olivier',                              # 42
        'Kloe',                                 # 43
        'Tita',                                 # 44
        'Zin',                                  # 45
        'Kevin',                                # 46
        'Josette',                              # 47
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
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT27/CH03580 ._CH',             # 01
        'ED6_DT07/CH02080 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH02070 ._CH',             # 04
        'ED6_DT27/CH04550 ._CH',             # 05
        'ED6_DT27/CH04558 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT27/CH04510 ._CH',             # 08
        'ED6_DT26/CH20363 ._CH',             # 09
        'ED6_DT27/CH03550 ._CH',             # 0A
        'ED6_DT26/CH20341 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
        'ED6_DT07/CH02080P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH02070P._CP',             # 04
        'ED6_DT27/CH04550P._CP',             # 05
        'ED6_DT27/CH04558P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT27/CH04510P._CP',             # 08
        'ED6_DT26/CH20363P._CP',             # 09
        'ED6_DT27/CH03550P._CP',             # 0A
        'ED6_DT26/CH20341P._CP',             # 0B
        'ED6_DT26/CH20341P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x84,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458759,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E2,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_5EE",          # 00, 0
        "Function_1_A3A",          # 01, 1
        "Function_2_B65",          # 02, 2
        "Function_3_1745",         # 03, 3
        "Function_4_185B",         # 04, 4
        "Function_5_18B1",         # 05, 5
        "Function_6_1A07",         # 06, 6
        "Function_7_1AFD",         # 07, 7
        "Function_8_1B79",         # 08, 8
        "Function_9_1CB5",         # 09, 9
        "Function_10_1DAB",        # 0A, 10
        "Function_11_1EC7",        # 0B, 11
        "Function_12_2093",        # 0C, 12
        "Function_13_2103",        # 0D, 13
        "Function_14_2178",        # 0E, 14
        "Function_15_21E8",        # 0F, 15
        "Function_16_225D",        # 10, 16
        "Function_17_2298",        # 11, 17
        "Function_18_27CC",        # 12, 18
        "Function_19_2B25",        # 13, 19
        "Function_20_2EE7",        # 14, 20
        "Function_21_2F65",        # 15, 21
        "Function_22_2FE3",        # 16, 22
        "Function_23_3061",        # 17, 23
        "Function_24_30DF",        # 18, 24
        "Function_25_327C",        # 19, 25
        "Function_26_33AA",        # 1A, 26
        "Function_27_344B",        # 1B, 27
        "Function_28_3BAE",        # 1C, 28
        "Function_29_3DCA",        # 1D, 29
        "Function_30_3FE0",        # 1E, 30
        "Function_31_401E",        # 1F, 31
        "Function_32_4A07",        # 20, 32
        "Function_33_4A3B",        # 21, 33
        "Function_34_4B17",        # 22, 34
        "Function_35_4BF3",        # 23, 35
        "Function_36_4E0C",        # 24, 36
        "Function_37_4FF4",        # 25, 37
        "Function_38_51CC",        # 26, 38
        "Function_39_53E5",        # 27, 39
        "Function_40_55C2",        # 28, 40
        "Function_41_5881",        # 29, 41
        "Function_42_5912",        # 2A, 42
        "Function_43_5A45",        # 2B, 43
        "Function_44_5BFF",        # 2C, 44
        "Function_45_5DB9",        # 2D, 45
        "Function_46_5F74",        # 2E, 46
        "Function_47_7619",        # 2F, 47
        "Function_48_7665",        # 30, 48
        "Function_49_76B3",        # 31, 49
        "Function_50_7719",        # 32, 50
        "Function_51_77D7",        # 33, 51
        "Function_52_787F",        # 34, 52
        "Function_53_7995",        # 35, 53
        "Function_54_7B2B",        # 36, 54
        "Function_55_7CC1",        # 37, 55
        "Function_56_7E57",        # 38, 56
        "Function_57_7FED",        # 39, 57
        "Function_58_8183",        # 3A, 58
        "Function_59_82A1",        # 3B, 59
        "Function_60_84B8",        # 3C, 60
        "Function_61_86F3",        # 3D, 61
        "Function_62_873B",        # 3E, 62
        "Function_63_8976",        # 3F, 63
        "Function_64_89BE",        # 40, 64
        "Function_65_92E0",        # 41, 65
        "Function_66_9343",        # 42, 66
        "Function_67_9466",        # 43, 67
        "Function_68_9570",        # 44, 68
        "Function_69_969E",        # 45, 69
        "Function_70_9729",        # 46, 70
        "Function_71_9A4A",        # 47, 71
        "Function_72_9AB1",        # 48, 72
        "Function_73_B372",        # 49, 73
        "Function_74_B3C7",        # 4A, 74
        "Function_75_B422",        # 4B, 75
        "Function_76_B459",        # 4C, 76
        "Function_77_B46F",        # 4D, 77
        "Function_78_B51B",        # 4E, 78
        "Function_79_B554",        # 4F, 79
        "Function_80_B5BA",        # 50, 80
        "Function_81_B62A",        # 51, 81
        "Function_82_B744",        # 52, 82
        "Function_83_B7E6",        # 53, 83
        "Function_84_B842",        # 54, 84
        "Function_85_B9EE",        # 55, 85
        "Function_86_BA36",        # 56, 86
        "Function_87_BBAC",        # 57, 87
        "Function_88_BBD6",        # 58, 88
        "Function_89_BBF1",        # 59, 89
        "Function_90_BCF3",        # 5A, 90
        "Function_91_BD8A",        # 5B, 91
        "Function_92_BDC7",        # 5C, 92
        "Function_93_BDEA",        # 5D, 93
        "Function_94_BE29",        # 5E, 94
        "Function_95_BEC4",        # 5F, 95
        "Function_96_C08A",        # 60, 96
        "Function_97_C13D",        # 61, 97
        "Function_98_C15C",        # 62, 98
        "Function_99_C1A9",        # 63, 99
        "Function_100_C1DB",       # 64, 100
        "Function_101_C251",       # 65, 101
    )


    def Function_0_5EE(): pass

    label("Function_0_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FD)
    OP_A3(0x10F0)
    Event(0, 24)
    Jump("loc_A39")

    label("loc_60F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_630")
    OP_A3(0x10FE)
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 0)
    Jump("loc_A39")

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_651")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F0)
    Event(0, 28)
    Jump("loc_A39")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_672")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F1)
    Event(0, 29)
    Jump("loc_A39")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F2)
    Event(0, 30)
    Jump("loc_A39")

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F3)
    Event(0, 31)
    Jump("loc_A39")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F4)
    Event(0, 35)
    Jump("loc_A39")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F6")
    OP_A3(0x10FF)
    OP_A3(0x10F5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 40)
    Jump("loc_A39")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_717")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F6)
    Event(0, 46)
    Jump("loc_A39")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F7)
    Event(0, 64)
    Jump("loc_A39")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F8)
    Event(0, 43)
    Jump("loc_A39")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F9)
    Event(0, 44)
    Jump("loc_A39")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10FA)
    Event(0, 70)
    Jump("loc_A39")

    label("loc_79B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BC")
    OP_A3(0x10FF)
    OP_A3(0x10FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 45)
    Jump("loc_A39")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10FC)
    Event(0, 72)
    Jump("loc_A39")

    label("loc_7DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_7FC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 2)
    Jump("loc_A39")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_81B")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 3)
    Jump("loc_A39")

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_83A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 4)
    Jump("loc_A39")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_859")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(1, 15)
    Jump("loc_A39")

    label("loc_859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_878")
    OP_A3(0x10F4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(1, 20)
    Jump("loc_A39")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_897")
    OP_A3(0x10F5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(1, 22)
    Jump("loc_A39")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_8FB")
    OP_A3(0x10F6)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_76(0xFF, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Event(1, 25)
    Jump("loc_A39")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_911")
    OP_A3(0x10F7)
    SetMapFlags(0x10000000)
    Event(1, 30)
    Jump("loc_A39")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_930")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F8)
    SetMapFlags(0x10000000)
    Event(0, 27)
    Jump("loc_A39")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_94A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    Event(0, 2)
    Jump("loc_A39")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_END)), "loc_964")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FA)
    Event(0, 17)
    Jump("loc_A39")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_END)), "loc_97E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FB)
    Event(0, 19)
    Jump("loc_A39")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_END)), "loc_9DD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FC)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    Event(0, 25)
    Jump("loc_A39")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_END)), "loc_A39")
    OP_A3(0x10FD)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFF, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 42)

    label("loc_A39")

    Return()

    # Function_0_5EE end

    def Function_1_A3A(): pass

    label("Function_1_A3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_A59")
    OP_B1("E0800_7")
    Jump("loc_A88")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_A6C")
    OP_B1("E0800_4")
    Jump("loc_A88")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 0)), scpexpr(EXPR_END)), "loc_A7F")
    OP_B1("E0800_6")
    Jump("loc_A88")

    label("loc_A7F")

    OP_B1("E0800_5")

    label("loc_A88")

    Jump("loc_B64")

    label("loc_A8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_END)), "loc_AAA")
    OP_B1("E0800_1")
    Jump("loc_ACE")

    label("loc_AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC5")
    OP_B1("E0800_2")
    Jump("loc_ACE")

    label("loc_AC5")

    OP_B1("E0800_2")

    label("loc_ACE")

    Jump("loc_B64")

    label("loc_AD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_AF0")
    OP_B1("E0800_4")
    Jump("loc_B25")

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B08")
    OP_B1("E0800_3")
    Jump("loc_B25")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1C")
    OP_B1("E0800_2")
    Jump("loc_B25")

    label("loc_B1C")

    OP_B1("E0800_1")

    label("loc_B25")

    Jump("loc_B64")

    label("loc_B28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 5)), scpexpr(EXPR_END)), "loc_B48")
    OP_B1("E0800_2y")
    Jump("loc_B58")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_END)), "loc_B58")
    OP_B1("E0800_2")

    label("loc_B58")

    Jump("loc_B64")

    label("loc_B5B")

    OP_B1("E0800_1")

    label("loc_B64")

    Return()

    # Function_1_A3A end

    def Function_2_B65(): pass

    label("Function_2_B65")

    EventBegin(0x0)
    OP_DB()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE2, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "monster\\\\msc0331.eff")
    LoadEffect(0x1, "map\\\\mp077_00.eff")
    LoadEffect(0x2, "map\\\\mp078_01.eff")
    OP_6D(-1460, 0, -1110, 0)
    OP_67(0, 6600, -10000, 0)
    OP_6B(4050, 0)
    OP_6C(315000, 0)
    OP_6E(416, 0)
    OP_D0(360000, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    OP_71(0x1, 0x4)
    OP_A1(0xE, 0x0)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xE, 0, -5000, 0, 270)
    SetChrPos(0x10, 136000, -5000, -50000, 270)
    SetChrPos(0x11, 136000, -5000, -50000, 270)
    SetChrPos(0x12, 136000, -5000, -50000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 30000, 0)
    OP_D1(17, 0, 270000, 30000, 0)
    OP_D1(18, 0, 270000, 30000, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x64)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    FadeToBright(1000, 0)

    def lambda_D62():
        OP_6D(-520, 0, -2050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D62)

    def lambda_D7A():
        OP_67(0, 2770, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D7A)
    WaitChrThread(0x101, 0x0)
    OP_43(0xE, 0x0, 0x0, 0x6)

    def lambda_D9E():
        OP_6D(-1790, 0, -9260, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D9E)

    def lambda_DB6():
        OP_67(0, 2060, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB6)

    def lambda_DCE():
        OP_6C(280000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DCE)

    def lambda_DDE():
        OP_D0(365000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DDE)
    Sleep(4000)

    def lambda_DF3():
        OP_67(0, 6060, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DF3)

    def lambda_E0B():
        OP_6C(75000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0B)

    def lambda_E1B():
        OP_D0(350000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E1B)
    WaitChrThread(0x101, 0x0)

    def lambda_E30():
        OP_67(0, 2060, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E30)
    WaitChrThread(0x101, 0x0)
    OP_E8(0x88, 0x13, 0x0, 0x0)
    PlayEffect(0x2, 0x0, 0x10, 100, 1000, -11000, 184, 0, -26, 950, 950, 950, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x11, 100, 1000, -11000, 184, 0, -26, 950, 950, 950, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x12, 0, 1000, -11500, 183, 0, -26, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0xC350, 0xFFFFEC78, 0x0)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFEC78, 0x1388)
    OP_43(0x0, 0x0, 0x0, 0x20)

    def lambda_F18():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F18)
    Sleep(1000)

    def lambda_F2D():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_F2D)
    Sleep(1000)
    OP_98(0x0, 0x11)
    OP_98(0x1, 0xC350, 0xFFFFEC78, 0x1388)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFEC78, 0x2710)

    def lambda_F6C():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F6C)
    Sleep(1000)

    def lambda_F81():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_F81)
    Sleep(1000)
    OP_98(0x0, 0x12)
    OP_98(0x1, 0xC350, 0xFFFFEC78, 0xFFFFEC78)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFEC78, 0x0)

    def lambda_FC0():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_FC0)
    Sleep(500)

    def lambda_FD5():
        OP_D1(254, 0, 270000, -30000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_FD5)
    Sleep(2500)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_24(0x235, 0x0)
    OP_44(0x0, 0x0)
    OP_23(0x235)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    SetChrPos(0xE, -25000, 0, 0, 270)
    SetChrPos(0x10, 125000, -6000, 0, 270)
    SetChrPos(0x11, 135000, -2000, 15000, 270)
    SetChrPos(0x12, 135000, -8000, -15000, 270)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 10000, 0)
    OP_D1(18, 0, 270000, -10000, 0)
    OP_B0(0x0, 0x3C)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFD8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_6D(88140, -3850, 0, 0)
    OP_67(0, 2000, -10000, 0)
    OP_6B(4050, 0)
    OP_6C(282000, 0)
    OP_6E(1045, 0)
    OP_D0(365000, 0)
    PlayEffect(0x2, 0x0, 0x10, -800, 1500, -12000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x11, 500, 500, -11000, 180, 2, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x12, 700, 400, -12000, 182, 3, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(500, 0)

    def lambda_11EE():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_11EE)

    def lambda_1209():
        OP_8F(0xFE, 0xC350, 0xFFFFE890, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1209)

    def lambda_1224():
        OP_8F(0xFE, 0xD6D8, 0xFFFFF830, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1224)

    def lambda_123F():
        OP_8F(0xFE, 0xD6D8, 0xFFFFE0C0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_123F)
    OP_43(0x0, 0x0, 0x0, 0x20)
    Sleep(6000)

    def lambda_1266():
        OP_6C(306000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1266)
    OP_82(0x2, 0x0)
    OP_82(0x5, 0x0)
    OP_43(0x12, 0x0, 0x0, 0x3)
    Sleep(1500)
    PlayEffect(0x1, 0xFF, 0xFF, 95000, -5000, -15000, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x4, 0x0)
    OP_44(0x0, 0x0)
    OP_23(0x235)
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(1000)
    Fade(500)
    OP_6D(430, -3850, 8540, 0)
    OP_6C(29000, 0)
    OP_D0(360000, 0)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    SetChrPos(0x10, 100000, -8000, 0, 270)
    SetChrPos(0x11, 105000, -6000, 15000, 270)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)

    def lambda_1359():
        OP_D1(254, 0, 245000, 20000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1359)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0x8AD4, 0x0, 0x689C)
    OP_98(0x1, 0xFFFF88B4, 0x0, 0x30C)

    def lambda_1393():
        OP_98(0x2, 0xFE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1393)

    def lambda_13A3():
        OP_D1(254, 0, 235000, 20000, 8000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_13A3)
    OP_98(0x0, 0x11)
    OP_98(0x1, 0x9E5C, 0x0, 0xB6BC)
    OP_98(0x1, 0xFFFFAFC4, 0x0, 0x3DA4)

    def lambda_13DD():
        OP_98(0x2, 0xFE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_13DD)

    def lambda_13ED():
        OP_6D(6320, -2850, 15060, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13ED)

    def lambda_1405():
        OP_6C(54000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1405)

    def lambda_1415():
        OP_D0(380000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1415)

    def lambda_1425():
        OP_67(0, 3150, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1425)
    SetChrPos(0xE, 0, 0, 0, 270)

    def lambda_144E():
        OP_D1(254, 0, 290000, 35000, 100)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_144E)
    OP_43(0xE, 0x0, 0x0, 0x7)
    WaitChrThread(0xE, 0x3)

    def lambda_1474():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_1474)
    Sleep(1000)

    def lambda_1493():
        OP_D1(254, 0, 250000, -35000, 1400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_1493)
    OP_43(0xE, 0x0, 0x0, 0x8)
    WaitChrThread(0xE, 0x3)

    def lambda_14B9():
        OP_D1(254, 0, 270000, 0, 6000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_14B9)
    Sleep(2000)
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x20)
    PlayEffect(0x2, 0x0, 0x10, 0, 1000, -12000, 160, 3, -30, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x2, 0x1, 0x11, 1300, 1200, -12000, 152, 0, -30, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_1558():
        OP_6D(-27950, -3850, -25800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1558)

    def lambda_1570():
        OP_6C(125000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1570)

    def lambda_1580():
        OP_67(0, 3800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1580)

    def lambda_1598():
        OP_D0(340000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1598)

    def lambda_15A8():
        OP_D1(254, 0, 270000, 20000, 5000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_15A8)
    OP_43(0xE, 0x0, 0x0, 0xA)
    WaitChrThread(0x101, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_72(0x2, 0x4)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_72(0x3, 0x4)
    PlayEffect(0x2, 0x0, 0x10, 500, 1000, -12000, 150, 0, -30, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0x1, 0x11, 500, 1000, -12000, 130, 0, -30, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    SetChrPos(0x12, 8000, -4000, -56000, 270)
    OP_71(0x4, 0x4)
    OP_D1(18, -5000, 300000, -30000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -17000, -5000, -41000, 280, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_72(0x4, 0x4)
    PlayEffect(0x2, 0x3, 0x12, 500, 1000, -9000, 210, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x5)
    Sleep(2000)
    OP_43(0xE, 0x0, 0x0, 0x9)
    Sleep(1000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_2_B65 end

    def Function_3_1745(): pass

    label("Function_3_1745")


    def lambda_174B():
        OP_D1(254, 0, 270000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_174B)

    def lambda_1765():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1765)
    Sleep(700)

    def lambda_1785():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1785)
    Sleep(600)

    def lambda_17A5():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17A5)
    Sleep(500)

    def lambda_17C5():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17C5)
    Sleep(400)

    def lambda_17E5():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17E5)
    Sleep(300)

    def lambda_1805():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1805)
    Sleep(200)

    def lambda_1825():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1825)
    Sleep(100)

    def lambda_1845():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1845)
    Return()

    # Function_3_1745 end

    def Function_4_185B(): pass

    label("Function_4_185B")


    def lambda_1861():
        OP_D1(254, 0, 300000, -20000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1861)

    def lambda_187B():
        OP_8F(0xFE, 0x61A8, 0xFFFFF830, 0xFFFFB1E0, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_187B)
    Sleep(1500)

    def lambda_189B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0x11170, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_189B)
    Return()

    # Function_4_185B end

    def Function_5_18B1(): pass

    label("Function_5_18B1")


    def lambda_18B7():
        OP_8F(0xFE, 0xBB8, 0xFFFFF830, 0xFFFF38C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_18B7)
    Sleep(2500)

    def lambda_18D7():
        OP_D1(254, -10000, 300000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_18D7)

    def lambda_18F1():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_18F1)
    Sleep(200)

    def lambda_1911():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1911)
    Sleep(200)

    def lambda_1931():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1931)
    Sleep(200)

    def lambda_1951():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1951)
    Sleep(200)

    def lambda_1971():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1971)
    Sleep(200)

    def lambda_1991():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1991)
    Sleep(200)

    def lambda_19B1():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_19B1)
    Sleep(200)

    def lambda_19D1():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_19D1)
    Sleep(200)

    def lambda_19F1():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_19F1)
    Return()

    # Function_5_18B1 end

    def Function_6_1A07(): pass

    label("Function_6_1A07")


    def lambda_1A0D():
        OP_D1(254, 0, 270000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A0D)

    def lambda_1A27():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A27)
    Sleep(200)

    def lambda_1A47():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A47)
    Sleep(200)

    def lambda_1A67():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A67)
    Sleep(200)

    def lambda_1A87():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A87)
    Sleep(200)

    def lambda_1AA7():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AA7)
    Sleep(200)

    def lambda_1AC7():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AC7)
    Sleep(200)

    def lambda_1AE7():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AE7)
    Return()

    # Function_6_1A07 end

    def Function_7_1AFD(): pass

    label("Function_7_1AFD")


    def lambda_1B03():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B03)
    Sleep(300)

    def lambda_1B23():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B23)
    Sleep(100)

    def lambda_1B43():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B43)
    Sleep(100)

    def lambda_1B63():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B63)
    Return()

    # Function_7_1AFD end

    def Function_8_1B79(): pass

    label("Function_8_1B79")


    def lambda_1B7F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B7F)
    Sleep(100)

    def lambda_1B9F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B9F)
    Sleep(100)

    def lambda_1BBF():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1BBF)
    Sleep(100)

    def lambda_1BDF():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1BDF)
    Sleep(100)

    def lambda_1BFF():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1BFF)
    Sleep(600)

    def lambda_1C1F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C1F)
    Sleep(100)

    def lambda_1C3F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C3F)
    Sleep(100)

    def lambda_1C5F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C5F)
    Sleep(100)

    def lambda_1C7F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C7F)
    Sleep(100)

    def lambda_1C9F():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C9F)
    Return()

    # Function_8_1B79 end

    def Function_9_1CB5(): pass

    label("Function_9_1CB5")


    def lambda_1CBB():
        OP_D1(254, 0, 250000, -40000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_1CBB)

    def lambda_1CD5():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CD5)
    Sleep(200)

    def lambda_1CF5():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CF5)
    Sleep(200)

    def lambda_1D15():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D15)
    Sleep(200)

    def lambda_1D35():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D35)
    Sleep(200)

    def lambda_1D55():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D55)
    Sleep(200)

    def lambda_1D75():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D75)
    Sleep(200)

    def lambda_1D95():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D95)
    Return()

    # Function_9_1CB5 end

    def Function_10_1DAB(): pass

    label("Function_10_1DAB")


    def lambda_1DB1():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DB1)
    Sleep(200)

    def lambda_1DD1():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DD1)
    Sleep(200)

    def lambda_1DF1():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DF1)
    Sleep(200)

    def lambda_1E11():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E11)
    Sleep(3600)

    def lambda_1E31():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E31)
    Sleep(200)

    def lambda_1E51():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E51)
    Sleep(200)

    def lambda_1E71():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E71)
    Sleep(200)

    def lambda_1E91():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E91)
    Sleep(200)

    def lambda_1EB1():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EB1)
    Return()

    # Function_10_1DAB end

    def Function_11_1EC7(): pass

    label("Function_11_1EC7")

    PlayEffect(0x0, 0x0, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, -5000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x1, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, 5000, 0)
    Sleep(200)
    PlayEffect(0x0, 0x2, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, 0, 10000, 0)
    Sleep(300)
    PlayEffect(0x0, 0x3, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -6000, 10000, 0)
    Sleep(500)
    PlayEffect(0x0, 0x4, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -14000, -4000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -12000, -6000, 0)
    Sleep(200)
    PlayEffect(0x0, 0x6, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -14000, -12000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x7, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -16000, -20000, 0)
    Return()

    # Function_11_1EC7 end

    def Function_12_2093(): pass

    label("Function_12_2093")

    PlayEffect(0x0, 0x0, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x1, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, 5000, 0)
    Return()

    # Function_12_2093 end

    def Function_13_2103(): pass

    label("Function_13_2103")

    Sleep(600)
    PlayEffect(0x0, 0x2, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x3, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -6000, 10000, 0)
    Return()

    # Function_13_2103 end

    def Function_14_2178(): pass

    label("Function_14_2178")

    PlayEffect(0x0, 0x4, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, -4000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, -6000, 0)
    Return()

    # Function_14_2178 end

    def Function_15_21E8(): pass

    label("Function_15_21E8")

    Sleep(600)
    PlayEffect(0x0, 0x6, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, -8000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x7, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -6000, -10000, 0)
    Return()

    # Function_15_21E8 end

    def Function_16_225D(): pass

    label("Function_16_225D")

    Sleep(1400)
    PlayEffect(0x0, 0x5, 0x12, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, -6000, 0)
    Return()

    # Function_16_225D end

    def Function_17_2298(): pass

    label("Function_17_2298")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    LoadEffect(0x1, "map\\\\mpsmk0.eff")
    LoadEffect(0x2, "map\\\\mp077_00.eff")
    OP_6D(81300, -9500, 23840, 0)
    OP_67(0, 4140, -10000, 0)
    OP_6B(5040, 0)
    OP_6C(71000, 0)
    OP_6E(869, 0)
    OP_D0(360000, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFD8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_A1(0xE, 0x0)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 250000, 10000, 15000, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    SetChrPos(0x10, 50000, 0, 0, 270)
    SetChrPos(0x11, 60000, 0, 15000, 270)
    SetChrPos(0x12, 60000, 0, -15000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x4, 0x4)
    OP_22(0x79, 0x1, 0x5A)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x11, 0x0, 0x0, 0x12)
    Sleep(3700)
    PlayEffect(0x2, 0xFF, 0xFF, 45000, -5000, 15000, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x11, 0x1)
    OP_72(0x1, 0x4)
    SetMapFlags(0x10)

    def lambda_253D():
        OP_6D(50100, -8000, 13150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_253D)

    def lambda_2555():
        OP_67(0, 2880, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2555)

    def lambda_256D():
        OP_D0(355000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_256D)

    def lambda_257D():
        OP_D1(254, 0, 270000, -30000, 4000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_257D)
    OP_98(0x0, 0xF)
    OP_98(0x1, 0x249F0, 0xFFFFE0C0, 0x3A98)
    OP_98(0x1, 0xC350, 0xFFFFE0C0, 0x3A98)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFE0C0, 0x3A98)

    def lambda_25C5():
        OP_98(0x2, 0xFE, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_25C5)
    Sleep(4800)
    OP_44(0xF, 0x1)
    Fade(1000)
    OP_6D(30780, -300, 10150, 0)
    OP_6B(2410, 0)
    OP_6C(50000, 0)
    OP_6E(869, 0)
    SetChrPos(0xE, 10000, 0, 0, 270)
    OP_D1(14, 0, 270000, -10000, 0)
    SetChrPos(0xF, 100000, -4000, 30000, 270)
    OP_D1(15, 0, 270000, 0, 0)

    def lambda_2657():
        OP_6D(-9720, 3450, 2950, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2657)

    def lambda_266F():
        OP_6C(47000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_266F)

    def lambda_267F():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_267F)

    def lambda_269A():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_269A)

    def lambda_26B4():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_26B4)
    Sleep(1500)

    def lambda_26D4():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_26D4)
    Sleep(400)

    def lambda_26F4():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_26F4)
    Sleep(400)

    def lambda_2714():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2714)
    Sleep(400)

    def lambda_2734():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2734)
    Sleep(400)

    def lambda_2754():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2754)
    Sleep(400)

    def lambda_2774():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2774)
    Sleep(400)

    def lambda_2794():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2794)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2298 end

    def Function_18_27CC(): pass

    label("Function_18_27CC")

    PlayEffect(0x1, 0x0, 0x11, 0, -5000, -3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1000, -3000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_283C():
        OP_91(0xFE, 0x7D0, 0xFFFFFC18, 0x7D0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_283C)
    OP_D1(254, 5000, 274000, 5000, 200)
    OP_D1(254, 5000, 270000, 0, 300)
    OP_D1(254, 5000, 272000, 3000, 300)
    PlayEffect(0x1, 0x1, 0x11, 0, -5000, 3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x11, 0, 3000, 4000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_28FA():
        OP_91(0xFE, 0xFFFFFC18, 0xFFFFFC18, 0xFFFFF830, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28FA)
    OP_D1(254, 8000, 262000, -8000, 200)
    OP_D1(254, 2000, 268000, 0, 300)
    OP_D1(254, 6000, 264000, -6000, 300)
    PlayEffect(0x1, 0x2, 0x11, -6000, -2000, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x11, 2000, -2000, -1000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_29B8():
        OP_91(0xFE, 0x3E8, 0xFFFFF060, 0x3E8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29B8)
    OP_D1(254, 8000, 284000, 10000, 200)
    OP_D1(254, 5000, 270000, -4000, 200)
    OP_D1(254, 7000, 280000, 6000, 200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2A15():
        OP_6D(50100, -10000, 13150, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A15)

    def lambda_2A2D():
        OP_67(0, 8029, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A2D)

    def lambda_2A45():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A45)

    def lambda_2A55():
        OP_D1(254, 7000, 280000, -30000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A55)

    def lambda_2A6F():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A6F)
    Sleep(500)

    def lambda_2A8F():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A8F)
    Sleep(400)

    def lambda_2AAF():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AAF)
    Sleep(300)

    def lambda_2ACF():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ACF)
    Sleep(200)

    def lambda_2AEF():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AEF)
    Sleep(100)

    def lambda_2B0F():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B0F)
    Return()

    # Function_18_27CC end

    def Function_19_2B25(): pass

    label("Function_19_2B25")

    EventBegin(0x0)
    OP_DB()
    OP_A1(0xE, 0x0)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    SetChrPos(0xF, 150000, -2000, 8000, 270)
    SetChrPos(0xE, 150000, 0, -8000, 270)
    SetChrPos(0x10, 300000, 0, -9300, 270)
    SetChrPos(0x11, 300000, 0, 6700, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x4)
    OP_22(0x79, 0x1, 0x5A)
    OP_6D(-68280, 2400, -1300, 0)
    OP_67(0, 2170, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(90000, 0)
    OP_6E(869, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF1, 0xFFFFFFFA, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)

    def lambda_2CCC():
        OP_67(0, -2830, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CCC)
    OP_43(0xE, 0x0, 0x0, 0x14)
    OP_43(0xF, 0x0, 0x0, 0x15)
    OP_43(0x10, 0x0, 0x0, 0x16)
    OP_43(0x11, 0x0, 0x0, 0x17)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(3000)
    OP_20(0xBB8)
    OP_21()
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    OP_1D(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0xE, 0, 0, 0, 270)
    OP_D1(14, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 700)
    OP_70(0x0, 0x30C)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_24(0x79, 0x46)
    OP_24(0x1C3, 0x5A)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_6D(-13440, -10000, -2430, 0)
    OP_67(0, 11980, -10000, 0)
    OP_6B(10090, 0)
    OP_6C(250000, 0)
    OP_6E(473, 0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x6F158, 0x0)
    FadeToBright(2000, 0)

    def lambda_2E29():
        OP_67(0, 12960, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E29)

    def lambda_2E41():
        OP_6B(5620, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E41)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0xE, 40000, 0, 0, 270)

    def lambda_2E67():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2E67)
    Fade(1000)
    OP_6D(24340, -10000, -15770, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(8039, 0)
    OP_6C(118000, 0)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2B25 end

    def Function_20_2EE7(): pass

    label("Function_20_2EE7")


    def lambda_2EED():
        OP_D1(254, 0, 260000, 30000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2EED)

    def lambda_2F07():
        OP_8F(0xFE, 0xFFFF3CB0, 0x0, 0xFFFFE0C0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F07)
    WaitChrThread(0xFE, 0x1)

    def lambda_2F27():
        OP_D1(254, 0, 250000, 40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F27)
    OP_97(0xFE, 0xFFFF3CB0, 0xFFFF63C0, 0xFFFEA070, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0xC350, 0x0)
    Return()

    # Function_20_2EE7 end

    def Function_21_2F65(): pass

    label("Function_21_2F65")


    def lambda_2F6B():
        OP_D1(254, 0, 280000, -30000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F6B)

    def lambda_2F85():
        OP_8F(0xFE, 0xFFFF3CB0, 0xFFFFF830, 0x1F40, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F85)
    WaitChrThread(0xFE, 0x1)

    def lambda_2FA5():
        OP_D1(254, 0, 290000, -40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FA5)
    OP_97(0xFE, 0xFFFF3CB0, 0x9C40, 0x15F90, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0xFFFFF830, 0x186A0, 0xC350, 0x0)
    Return()

    # Function_21_2F65 end

    def Function_22_2FE3(): pass

    label("Function_22_2FE3")


    def lambda_2FE9():
        OP_D1(254, 0, 260000, 30000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FE9)

    def lambda_3003():
        OP_8F(0xFE, 0xFFFF3CB0, 0x0, 0xFFFFDBAC, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3003)
    WaitChrThread(0xFE, 0x1)

    def lambda_3023():
        OP_D1(254, 0, 250000, 40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3023)
    OP_97(0xFE, 0xFFFF3CB0, 0xFFFF5EAC, 0xFFFEA070, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0xC350, 0x0)
    Return()

    # Function_22_2FE3 end

    def Function_23_3061(): pass

    label("Function_23_3061")


    def lambda_3067():
        OP_D1(254, 0, 280000, -30000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3067)

    def lambda_3081():
        OP_8F(0xFE, 0xFFFF3CB0, 0x0, 0x1A2C, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3081)
    WaitChrThread(0xFE, 0x1)

    def lambda_30A1():
        OP_D1(254, 0, 290000, -40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_30A1)
    OP_97(0xFE, 0xFFFF3CB0, 0x972C, 0x15F90, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0x0, 0x186A0, 0xC350, 0x0)
    Return()

    # Function_23_3061 end

    def Function_24_30DF(): pass

    label("Function_24_30DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    StopSound(0x4E20, 0xC3500, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    OP_6B(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 400)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x46)
    OP_A1(0xF, 0x1)
    SetChrPos(0xF, 10000, 20000, 0, 270)

    def lambda_318C():
        OP_6B(3130, 15000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_318C)

    def lambda_319C():
        OP_6E(282, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_319C)
    FadeToBright(2000, 0)

    def lambda_31B5():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_31B5)
    Sleep(500)

    def lambda_31D5():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_31D5)
    Sleep(500)

    def lambda_31F5():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_31F5)
    Sleep(500)

    def lambda_3215():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3215)
    Sleep(500)

    def lambda_3235():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3235)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_30DF end

    def Function_25_327C(): pass

    label("Function_25_327C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    StopSound(0x4E20, 0xC3500, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 400)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x64)
    OP_A1(0xF, 0x1)
    SetChrPos(0xF, -79470, -30000, -91440, 270)
    OP_6D(-98020, -10000, -92900, 0)
    OP_67(0, -6950, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(232000, 0)
    OP_6E(854, 0)
    FadeToBright(1000, 0)

    def lambda_3346():
        OP_6D(-101640, -10000, -90970, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3346)

    def lambda_335E():
        OP_67(0, -8000, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_335E)

    def lambda_3376():
        OP_6B(7000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3376)
    OP_43(0xF, 0x0, 0x0, 0x1A)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_327C end

    def Function_26_33AA(): pass

    label("Function_26_33AA")


    def lambda_33B0():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_33B0)
    Sleep(500)

    def lambda_33D0():
        OP_8F(0xFE, 0xFFFCF20C, 0x186A0, 0xFFFE9A8A, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_33D0)
    Sleep(500)

    def lambda_33F0():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_33F0)
    Sleep(500)

    def lambda_3410():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3410)
    Sleep(500)

    def lambda_3430():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3430)
    WaitChrThread(0xF, 0x1)
    Return()

    # Function_26_33AA end

    def Function_27_344B(): pass

    label("Function_27_344B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_A1(0xE, 0x2)
    OP_A1(0x1B, 0x7)
    SetChrPos(0xE, 0, 0, 0, 270)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x4)
    OP_48()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-32090, 3430, -1640, 0)
    OP_67(0, 8860, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(311000, 0)
    OP_6E(515, 0)
    OP_22(0x1C3, 0x0, 0x64)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    OP_89(0x1A, 3260, 3600, -510, 0)
    OP_89(0x1B, 3310, 3600, 1000, 0)
    SetChrChipByIndex(0x1A, 10)
    SetChrSubChip(0x1A, 0)
    SetChrFlags(0x1A, 0x800)
    ClearChrFlags(0x1A, 0x1)
    OP_22(0x79, 0x1, 0x3C)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "map\\\\mp085_00.eff")
    LoadEffect(0x2, "battle\\\\mgaria0.eff")
    LoadEffect(0x3, "map\\\\mp085_01.eff")

    def lambda_35A6():
        OP_6D(3000, 3450, -220, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35A6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(2780, 3510, 470, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_DC()
    Sleep(500)

    ChrTalk(    #0
        0x1A,
        (
            "#1154F#6PThe moment is upon us.\x02\x03",

            "#1150FLet us begin stage three of the plan.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)

    def lambda_3672():
        OP_99(0x1A, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_3672)
    PlayEffect(0x2, 0x0, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_36C1():
        OP_99(0x1A, 0x3, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_36C1)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(1000)

    def lambda_36DE():
        OP_99(0x1A, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_36DE)
    Sleep(1000)
    Fade(500)
    OP_6D(2450, 3520, -870, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(191000, 0)
    OP_6E(499, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 6)

    def lambda_3745():
        OP_99(0x1A, 0x0, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_3745)
    Sleep(300)
    OP_22(0xD8, 0x0, 0x64)
    WaitChrThread(0x1A, 0x0)
    Sleep(500)

    ChrTalk(    #1
        0x1A,
        (
            "#1151F#6PAureole, sealed in the darkness where\x01",
            "septium's light does not reach...\x02\x03",

            "May you gaze upon our poor material\x01",
            "world through your Gospel.\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_E8(0xB8, 0xB, 0x0, 0x0)
    Sleep(200)
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x1B, 0, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_20(0x7D0)
    Sleep(100)
    OP_24(0x1C3, 0x5A)
    Sleep(100)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x1C3, 0x46)
    Sleep(100)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x1C3, 0x32)
    Sleep(100)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_23(0x1C3)
    OP_21()
    OP_1D(0x70)
    Sleep(500)
    Fade(500)
    ClearMapFlags(0x10)
    OP_6D(2420, 6690, 3310, 0)
    OP_67(0, 1830, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(338000, 0)
    OP_6E(806, 0)
    ClearChrFlags(0x1A, 0x800)
    OP_0D()

    def lambda_38E5():
        OP_67(0, 700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38E5)

    def lambda_38FD():
        OP_6D(2420, 8690, 3310, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38FD)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x1, 0xFF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x0, 0x64)
    Sleep(2000)
    Sleep(2000)
    Fade(500)
    OP_6D(2450, 3520, -870, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(191000, 0)
    OP_6E(499, 0)
    OP_82(0x1, 0x0)
    SetChrFlags(0x1A, 0x800)
    OP_0D()
    OP_99(0x1A, 0x9, 0x0, 0x7D0)
    Sleep(500)
    OP_DC()

    ChrTalk(    #2
        0x1A,
        (
            "#1155F#6PGaze upon these four pillars!\x02\x03",

            "They are the final shackles that bind\x01",
            "you!\x02\x03",

            "Simple they may appear to be,\x01",
            "but know that their purpose was long\x01",
            "shrouded by the decree of man!\x02\x03",

            "With hands which bend the will of all,\x01",
            "reveal their true form!\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    PlayEffect(0x1, 0x1, 0xFF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(1500)
    OP_6D(2420, 8690, 3310, 0)
    OP_67(0, 700, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(338000, 0)
    OP_6E(806, 0)
    ClearChrFlags(0x1A, 0x800)
    OP_0D()
    PlayEffect(0x3, 0x2, 0xFF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x0, 0x64)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_344B end

    def Function_28_3BAE(): pass

    label("Function_28_3BAE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS240._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS241._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS240._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, -36000, -110000, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, -36000, -110000, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, -36000, -110000, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, -160000, 0, 1000)
    OP_C6(0x2, 0x0, -160000, 0, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    Call(0, 36)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3BAE end

    def Function_29_3DCA(): pass

    label("Function_29_3DCA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS242._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS243._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS242._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, -125000, 0, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, -125000, 0, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, -125000, 0, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, -90000, -110000, 1000)
    OP_C6(0x2, 0x0, -90000, -110000, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    Call(0, 37)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10FB)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3DCA end

    def Function_30_3FE0(): pass

    label("Function_30_3FE0")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToDark(0, 0, -1)
    Call(0, 38)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10FD)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_30_3FE0 end

    def Function_31_401E(): pass

    label("Function_31_401E")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "map\\\\mp078_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-37160, -10000, -21180, 0)
    OP_67(0, -10620, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(31000, 0)
    OP_6E(619, 0)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, 38760, -10000, -14790, 270)
    OP_A1(0xF, 0x2)
    SetChrPos(0xF, 50390, -10000, 4970, 90)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, 70850, -10000, -32060, 90)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 90000, 10000, 0)
    OP_D1(16, 0, 90000, -10000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 700)
    OP_70(0x1, 0x30C)

    def lambda_4138():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4138)
    Sleep(2000)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 470)
    OP_70(0x2, 0x23A)
    Sleep(100)
    OP_B0(0x3, 0x2D)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 470)
    OP_70(0x3, 0x23A)

    def lambda_418B():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_418B)
    Sleep(200)

    def lambda_41AB():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_41AB)
    Sleep(3000)
    Fade(500)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    SetChrPos(0xE, -8760, 0, -14790, 270)
    SetChrPos(0xF, 40390, 0, 4970, 90)
    SetChrPos(0x10, 55850, 0, -26060, 90)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 80000, 10000, 0)
    OP_D1(16, 0, 95000, -10000, 0)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_6D(-1430, 11270, -30440, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(6040, 0)
    OP_6C(46000, 0)
    OP_6E(619, 0)
    SetChrPos(0x0, -8340, 11270, -29600, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFF6, 0x0, 0x0, 0x0)
    OP_0D()

    def lambda_42F8():
        OP_6D(-9890, 11270, -27200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_42F8)

    def lambda_4310():
        OP_6C(63000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4310)

    def lambda_4320():
        OP_6B(7790, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4320)
    Sleep(2000)
    PlayEffect(0x0, 0x0, 0x10, 300, 3300, -8000, 95, 0, 350, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_43(0x0, 0x0, 0x0, 0x20)

    def lambda_4371():
        OP_D1(254, 0, 280000, -35000, 300)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4371)
    OP_43(0xE, 0x0, 0x0, 0x21)
    WaitChrThread(0xE, 0x3)

    def lambda_4397():
        OP_D1(254, 0, 270000, 0, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4397)

    def lambda_43B1():
        OP_D1(254, 0, 90000, 10000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_43B1)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_24(0x235, 0x0)
    OP_23(0x235)
    OP_43(0x0, 0x0, 0x0, 0x20)
    PlayEffect(0x0, 0x0, 0xF, 1000, 3300, -8300, 90, 0, 10, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_4420():
        OP_D1(254, 0, 260000, 35000, 300)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4420)
    OP_43(0xE, 0x0, 0x0, 0x22)
    WaitChrThread(0xE, 0x3)

    def lambda_4446():
        OP_D1(254, 0, 270000, 0, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4446)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_44(0x0, 0x0)
    OP_24(0x235, 0x0)
    OP_23(0x235)

    def lambda_447D():
        OP_D1(254, 0, 270000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_447D)

    def lambda_4497():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4497)
    Sleep(200)

    def lambda_44B7():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_44B7)
    Sleep(200)

    def lambda_44D7():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_44D7)
    Sleep(200)

    def lambda_44F7():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_44F7)
    Sleep(200)

    def lambda_4517():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4517)
    Sleep(200)

    def lambda_4537():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4537)
    Sleep(200)

    def lambda_4557():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4557)
    Sleep(200)

    def lambda_4577():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4577)
    Sleep(800)

    def lambda_4597():
        OP_D1(254, 0, 90000, -30000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_4597)

    def lambda_45B1():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_45B1)
    Sleep(200)

    def lambda_45D1():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_45D1)
    Sleep(200)

    def lambda_45F1():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_45F1)
    Sleep(200)

    def lambda_4611():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4611)
    Sleep(200)

    def lambda_4631():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4631)
    Sleep(200)

    def lambda_4651():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4651)

    def lambda_466C():
        OP_D1(254, 0, 90000, -30000, 4000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_466C)

    def lambda_4686():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4686)
    Sleep(200)

    def lambda_46A6():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_46A6)

    def lambda_46C1():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_46C1)
    Sleep(200)

    def lambda_46E1():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_46E1)

    def lambda_46FC():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_46FC)
    Sleep(200)

    def lambda_471C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_471C)
    Sleep(200)

    def lambda_473C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_473C)
    Sleep(200)

    def lambda_475C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_475C)
    Sleep(200)

    def lambda_477C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_477C)
    Sleep(200)

    def lambda_479C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_479C)
    Sleep(2500)
    Fade(500)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0xE, 0x3)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x3)
    OP_6D(54490, 3940, -20960, 0)
    OP_67(0, 2960, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(294000, 0)
    OP_6E(619, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFF6, 0x0, 0x0, 0x0)
    SetChrPos(0xE, -38760, 0, -14790, 270)
    SetChrPos(0xF, 40390, 0, 4970, 90)
    SetChrPos(0x10, 60850, 0, -32060, 90)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 84000, -10000, 0)
    OP_D1(16, 0, 96000, 10000, 0)
    OP_6F(0x2, 470)
    OP_70(0x2, 0x23A)
    OP_6F(0x3, 470)
    OP_70(0x3, 0x23A)
    OP_0D()
    OP_DC()
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #3
        (
            "\x07\x00#163FHmph. Making this hard on us,\x01",
            "are they?\x02\x03",

            "They may have an advantage in\x01",
            "terms of speed, but I won't let them\x01",
            "escape our net.\x02\x03",

            "#160FCorner them and seize their vessel!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #4
        "\x07\x00#5SYes, sir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E1D)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_401E end

    def Function_32_4A07(): pass

    label("Function_32_4A07")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3A")
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    Jump("Function_32_4A07")

    label("loc_4A3A")

    Return()

    # Function_32_4A07 end

    def Function_33_4A3B(): pass

    label("Function_33_4A3B")


    def lambda_4A41():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A41)
    Sleep(100)

    def lambda_4A61():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A61)
    Sleep(100)

    def lambda_4A81():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A81)
    Sleep(200)

    def lambda_4AA1():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4AA1)
    Sleep(200)

    def lambda_4AC1():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4AC1)
    Sleep(200)

    def lambda_4AE1():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4AE1)
    Sleep(200)

    def lambda_4B01():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B01)
    Return()

    # Function_33_4A3B end

    def Function_34_4B17(): pass

    label("Function_34_4B17")


    def lambda_4B1D():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B1D)
    Sleep(100)

    def lambda_4B3D():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B3D)
    Sleep(100)

    def lambda_4B5D():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B5D)
    Sleep(200)

    def lambda_4B7D():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B7D)
    Sleep(200)

    def lambda_4B9D():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B9D)
    Sleep(200)

    def lambda_4BBD():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4BBD)
    Sleep(200)

    def lambda_4BDD():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4BDD)
    Return()

    # Function_34_4B17 end

    def Function_35_4BF3(): pass

    label("Function_35_4BF3")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToDark(0, 0, -1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS246._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS247._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS246._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, 0, -144000, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, 0, -144000, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, 0, -144000, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, -94000, -16000, 1000)
    OP_C6(0x2, 0x0, -94000, -16000, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    Call(0, 39)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E1E)
    OP_DC()
    OP_A2(0x10FE)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_35_4BF3 end

    def Function_36_4E0C(): pass

    label("Function_36_4E0C")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(-24410, 4960, -25560, 0)
    OP_67(0, -5640, -10000, 0)
    OP_6B(5030, 0)
    OP_6C(44000, 0)
    OP_6E(561, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_4ED1():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4ED1)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_4F02():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4F02)

    def lambda_4F1D():
        OP_6D(-42500, 30000, -12940, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4F1D)

    def lambda_4F35():
        OP_67(0, 15420, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F35)

    def lambda_4F4D():
        OP_6B(5030, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F4D)

    def lambda_4F5D():
        OP_6E(464, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F5D)

    def lambda_4F6D():
        OP_6C(57000, 7000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4F6D)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x0)
    Return()

    # Function_36_4E0C end

    def Function_37_4FF4(): pass

    label("Function_37_4FF4")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(-4680, 30000, 7570, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(5750, 0)
    OP_6C(140000, 0)
    OP_6E(500, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_50B9():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_50B9)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_50EA():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_50EA)

    def lambda_5105():
        OP_6D(-21610, -2850, 5220, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5105)

    def lambda_511D():
        OP_67(0, 14310, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_511D)

    def lambda_5135():
        OP_6B(4500, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5135)

    def lambda_5145():
        OP_6C(224000, 7000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_5145)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_37_4FF4 end

    def Function_38_51CC(): pass

    label("Function_38_51CC")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_6D(-15370, 30000, 3100, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(5750, 0)
    OP_6C(236000, 0)
    OP_6E(500, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_52A5():
        OP_6D(13380, 30000, 4450, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_52A5)

    def lambda_52BD():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_52BD)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0x101, 0x0)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_52F3():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_52F3)

    def lambda_530E():
        OP_6D(-15600, -10000, 380, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_530E)

    def lambda_5326():
        OP_67(0, 6870, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5326)

    def lambda_533E():
        OP_6B(6430, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_533E)

    def lambda_534E():
        OP_6E(613, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_534E)

    def lambda_535E():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_535E)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_38_51CC end

    def Function_39_53E5(): pass

    label("Function_39_53E5")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_6D(5220, 28870, 190, 0)
    OP_67(0, -8260, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(103000, 0)
    OP_6E(646, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_54AA():
        OP_6B(7000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54AA)

    def lambda_54BA():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_54BA)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0x101, 0x0)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_54F0():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_54F0)

    def lambda_550B():
        OP_6D(-28550, -10000, -240, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_550B)

    def lambda_5523():
        OP_67(0, 15830, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5523)

    def lambda_553B():
        OP_6B(5900, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_553B)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_39_53E5 end

    def Function_40_55C2(): pass

    label("Function_40_55C2")

    EventBegin(0x0)
    OP_DB()
    ClearMapFlags(0x100000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_6D(-150870, 26810, -13480, 0)
    OP_67(0, -3250, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(262000, 0)
    OP_6E(742, 0)
    OP_A1(0x1D, 0x1)
    SetChrPos(0x1D, -100380, -10000, -13480, 270)
    OP_22(0x113, 0x0, 0x64)
    SetChrPos(0x1C, 0, 0, 0, 135)
    ClearChrFlags(0x1C, 0x80)
    OP_CF(0x1C, 0x1, "Frame85__ren")
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 281)
    OP_70(0x1, 0x12C)
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    PlayEffect(0x2, 0x1, 0x1D, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x1D, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x1D, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x1D, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x1D, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x1D, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_57F5():
        OP_67(0, -5540, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_57F5)

    def lambda_580D():
        OP_6B(2400, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_580D)

    def lambda_581D():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_581D)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_5837():
        OP_90(0xFE, 0xFFF9E580, 0x3D090, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5837)
    OP_43(0x1D, 0x3, 0x0, 0x29)
    Sleep(3000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_DC()
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_40_55C2 end

    def Function_41_5881(): pass

    label("Function_41_5881")

    Sleep(500)
    OP_24(0x113, 0x5F)
    Sleep(500)
    OP_24(0x113, 0x5A)
    Sleep(500)
    OP_24(0x113, 0x55)
    Sleep(500)
    OP_24(0x113, 0x50)
    Sleep(500)
    OP_24(0x113, 0x4B)
    Sleep(500)
    OP_24(0x113, 0x46)
    Sleep(500)
    OP_24(0x113, 0x41)
    Sleep(500)
    OP_24(0x113, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x37)
    Sleep(500)
    OP_24(0x113, 0x32)
    Sleep(500)
    OP_24(0x113, 0x2D)
    Sleep(500)
    OP_24(0x113, 0x28)
    Sleep(500)
    OP_24(0x113, 0x23)
    Sleep(500)
    OP_24(0x113, 0x1E)
    Sleep(500)
    OP_24(0x113, 0x19)
    Sleep(500)
    OP_24(0x113, 0x14)
    Return()

    # Function_41_5881 end

    def Function_42_5912(): pass

    label("Function_42_5912")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_A1(0xF, 0x1)
    OP_8C(0xF, 270, 0)
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x64)
    OP_6D(92340, 13360, 25280, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(247000, 0)
    OP_6E(437, 0)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_59AD():
        OP_6D(22320, 13360, 9400, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_59AD)

    def lambda_59C5():
        OP_67(0, 3320, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_59C5)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    def lambda_59F0():
        OP_6D(-45160, 13360, -800, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_59F0)

    def lambda_5A08():
        OP_6C(270000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5A08)

    def lambda_5A18():
        OP_6E(352, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5A18)
    Sleep(4000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_42_5912 end

    def Function_43_5A45(): pass

    label("Function_43_5A45")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-35180, -10000, -17880, 0)
    OP_67(0, -5970, -10000, 0)
    OP_6B(4660, 0)
    OP_6C(28000, 0)
    OP_6E(497, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_A1(0xE, 0x2)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xE, 38760, -5000, -10000, 270)
    SetChrPos(0xF, 48390, -5000, -3000, 270)
    SetChrPos(0x10, 58850, -5000, -17000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x2, 0x2D)
    OP_B0(0x3, 0x2D)
    OP_B0(0x4, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 700)
    OP_70(0x3, 0x30C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 700)
    OP_70(0x4, 0x30C)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_5B87():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B87)
    Sleep(1000)

    def lambda_5BA7():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5BA7)
    Sleep(1000)

    def lambda_5BC7():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5BC7)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_5A45 end

    def Function_44_5BFF(): pass

    label("Function_44_5BFF")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-35180, -10000, -17880, 0)
    OP_67(0, -5970, -10000, 0)
    OP_6B(4660, 0)
    OP_6C(28000, 0)
    OP_6E(497, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_A1(0xE, 0x2)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xE, 38760, -5000, -10000, 270)
    SetChrPos(0xF, 48390, -5000, -3000, 270)
    SetChrPos(0x10, 58850, -5000, -17000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x2, 0x2D)
    OP_B0(0x3, 0x2D)
    OP_B0(0x4, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 700)
    OP_70(0x3, 0x30C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 700)
    OP_70(0x4, 0x30C)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_5D41():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5D41)
    Sleep(1000)

    def lambda_5D61():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5D61)
    Sleep(1000)

    def lambda_5D81():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D81)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R4102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_44_5BFF end

    def Function_45_5DB9(): pass

    label("Function_45_5DB9")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -9020, 0, -61470, 0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    OP_6B(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0xAAE60, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 10000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_5E7F():
        OP_6B(3130, 15000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5E7F)

    def lambda_5E8F():
        OP_6E(282, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E8F)
    FadeToBright(2000, 0)

    def lambda_5EA8():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5EA8)
    Sleep(500)

    def lambda_5EC8():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5EC8)
    Sleep(500)

    def lambda_5EE8():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5EE8)
    Sleep(500)

    def lambda_5F08():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5F08)
    Sleep(500)

    def lambda_5F28():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5F28)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_45_5DB9 end

    def Function_46_5F74(): pass

    label("Function_46_5F74")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "monster\\\\msc0331.eff")
    LoadEffect(0x1, "battle\\\\btbomb00.eff")
    LoadEffect(0x2, "map\\\\mp077_00.eff")
    LoadEffect(0x3, "map\\\\mpsmk0.eff")
    LoadEffect(0x4, "map\\\\mp094_00.eff")
    LoadEffect(0x5, "map\\\\mp078_01.eff")
    OP_E8(0x88, 0x13, 0x0, 0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, 0, 0, 0, 270)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_6F(0x1, 200)
    OP_70(0x1, 0x258)
    OP_A1(0xF, 0x2)
    OP_A1(0x10, 0x3)
    OP_A1(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_A1(0x13, 0x6)
    SetChrPos(0xF, 56000, 0, -30000, 270)
    SetChrPos(0x10, 78000, 6000, -16000, 270)
    SetChrPos(0x11, 50000, 3000, 0, 270)
    SetChrPos(0x12, 78000, 6000, 16000, 270)
    SetChrPos(0x13, 56000, 0, 30000, 270)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    ClearChrFlags(0x13, 0x100)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 680)
    OP_70(0x2, 0x30C)
    OP_B0(0x3, 0x2D)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 680)
    OP_70(0x3, 0x30C)
    OP_B0(0x4, 0x2D)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 680)
    OP_70(0x4, 0x30C)
    OP_B0(0x5, 0x2D)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 680)
    OP_70(0x5, 0x30C)
    OP_B0(0x6, 0x2D)
    OP_71(0x6, 0x20)
    OP_6F(0x6, 680)
    OP_70(0x6, 0x30C)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_71(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_6D(8660, -10000, -10260, 0)
    OP_67(0, 13390, -10000, 0)
    OP_6B(6420, 0)
    OP_6C(134000, 0)
    OP_6E(626, 0)
    OP_22(0x12B, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x64)
    FadeToBright(2000, 0)

    def lambda_6274():
        OP_6D(8520, -3850, -19480, 12000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6274)

    def lambda_628C():
        OP_67(0, 3330, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_628C)

    def lambda_62A4():
        OP_6C(147000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_62A4)
    OP_43(0xF, 0x0, 0x0, 0x35)
    OP_43(0x10, 0x0, 0x0, 0x36)
    OP_43(0x11, 0x0, 0x0, 0x37)
    OP_43(0x12, 0x0, 0x0, 0x38)
    OP_43(0x13, 0x0, 0x0, 0x39)
    Sleep(19000)
    Fade(500)
    OP_44(0xF, 0x0)
    OP_44(0xF, 0x1)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x3)
    SetChrPos(0xF, 250000, -6000, 0, 270)
    SetChrPos(0x10, 350000, -6000, 10000, 270)
    SetChrPos(0x11, 450000, -6000, -10000, 270)
    SetChrPos(0x12, 550000, -6000, 14000, 270)
    SetChrPos(0x13, 650000, -6000, -14000, 270)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_6F(0x6, 800)
    OP_70(0x6, 0x384)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFCE, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_6D(30440, -6550, 0, 0)
    OP_67(0, 1450, -10000, 0)
    OP_6B(5720, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_D0(375000, 0)

    def lambda_64A2():
        OP_D1(254, 0, 270000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_64A2)

    def lambda_64BC():
        OP_D1(254, 0, 270000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_64BC)

    def lambda_64D6():
        OP_D1(254, 0, 270000, -35000, 5000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_64D6)

    def lambda_64F0():
        OP_D1(254, 0, 270000, 35000, 5000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_64F0)

    def lambda_650A():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x0, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_650A)

    def lambda_6525():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0xFFFFD8F0, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6525)

    def lambda_6540():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x2710, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6540)

    def lambda_655B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE890, 0xFFFFC950, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_655B)

    def lambda_6576():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE890, 0x36B0, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6576)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_43(0x15, 0x3, 0x0, 0x2F)
    OP_6D(-2080, -10000, 0, 0)
    OP_67(0, 14540, -10000, 0)
    OP_6B(8420, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_D0(360000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    Sleep(1000)
    OP_6F(0x1, 200)
    OP_70(0x1, 0x258)
    OP_43(0x15, 0x3, 0x0, 0x30)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_6685():
        OP_6D(20000, -10000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6685)

    def lambda_669D():
        OP_67(0, 1800, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_669D)

    def lambda_66B5():
        OP_6B(6160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_66B5)
    WaitChrThread(0x0, 0x0)
    OP_72(0x1, 0x20)
    OP_73(0x1)

    def lambda_66D2():
        OP_6D(4740, -8700, 19700, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_66D2)

    def lambda_66EA():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_66EA)

    def lambda_66FA():
        OP_6B(5780, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_66FA)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x1, 601)
    OP_70(0x1, 0x384)
    Sleep(1500)
    OP_22(0x111, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 901)
    OP_70(0x1, 0x5DC)
    Sleep(1000)

    def lambda_6742():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6742)
    Sleep(100)

    def lambda_6762():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6762)
    Sleep(100)

    def lambda_6782():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6782)
    Sleep(100)

    def lambda_67A2():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_67A2)
    Sleep(100)

    def lambda_67C2():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_67C2)
    Sleep(100)

    def lambda_67E2():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_67E2)
    Sleep(100)

    def lambda_6802():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0xDAC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6802)
    Sleep(1000)
    Fade(1000)
    OP_44(0xE, 0x1)
    OP_6D(20000, -10000, 0, 0)
    OP_67(0, 1800, -10000, 0)
    OP_6B(6160, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xE, 150000, 0, 0, 270)

    def lambda_6890():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x14820, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6890)
    Sleep(800)

    def lambda_68B0():
        OP_6D(-20000, 11800, 0, 2600)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_68B0)

    def lambda_68C8():
        OP_67(0, -4600, -10000, 2600)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_68C8)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_44(0xF, 0x1)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x3)
    SetChrPos(0x16, -300000, 0, 0, 90)
    SetChrPos(0xE, -500000, 0, 0, 90)
    SetChrPos(0xF, 10000, -8000, 0, 270)
    SetChrPos(0x10, 25000, -8000, 25000, 270)
    SetChrPos(0x11, 25000, -8000, -27000, 270)
    SetChrPos(0x12, 50000, -2000, 15000, 270)
    SetChrPos(0x13, 50000, -2000, -17000, 270)
    OP_D1(14, 0, 90000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 266000, -5000, 0)
    OP_D1(17, 0, 274000, 5000, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_6D(-60920, -6600, 8860, 0)
    OP_67(0, 1880, -10000, 0)
    OP_6B(7840, 0)
    OP_6C(106000, 0)
    OP_6E(536, 0)
    OP_D0(375000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFCE, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_43(0x15, 0x3, 0x0, 0x31)
    FadeToBright(1000, 0)

    def lambda_6ABF():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6ABF)

    def lambda_6ADA():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x3A98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6ADA)

    def lambda_6AF5():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0xFFFFBD98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6AF5)

    def lambda_6B10():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B10)

    def lambda_6B2B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0xFFFF7B30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6B2B)

    def lambda_6B46():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF830, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B46)

    def lambda_6B61():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF830, 0xFFFFE4A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6B61)

    label("loc_6B76")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B8C")
    Sleep(15)
    Jump("loc_6B76")

    label("loc_6B8C")

    OP_43(0x16, 0x0, 0x0, 0x3A)
    Sleep(500)
    StopSound(0x4E20, 0xB8538, 0x7D0)

    def lambda_6BAB():
        OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6BAB)

    def lambda_6BC6():
        OP_6D(-161860, -6600, 14140, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6BC6)

    def lambda_6BDE():
        OP_67(0, 4460, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6BDE)

    def lambda_6BF6():
        OP_6B(7650, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6BF6)

    def lambda_6C06():
        OP_6C(250000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6C06)

    def lambda_6C16():
        OP_D0(345000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_6C16)
    WaitChrThread(0x0, 0x1)

    def lambda_6C2B():
        OP_67(0, 2640, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6C2B)
    Sleep(1000)
    Fade(500)
    OP_24(0x79, 0x28)
    OP_24(0x125, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    SetChrPos(0x16, 150000, 0, 0, 90)
    SetChrPos(0xE, 0, 0, 0, 90)
    OP_D1(14, 0, 90000, 0, 0)
    OP_76(0xFF, 0x0, 0x1, 0xF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x14, 0x2, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x32, 0x5, 0x0, 0x0, 0x0)
    OP_6D(45680, -8500, -5700, 0)
    OP_67(0, 1840, -10000, 0)
    OP_6B(9750, 0)
    OP_6C(252000, 0)
    OP_6E(536, 0)
    OP_43(0x16, 0x0, 0x0, 0x3B)
    OP_43(0xE, 0x0, 0x0, 0x33)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    PlayEffect(0x4, 0x0, 0xE, 7000, -2000, 24000, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 0, 0)
    OP_22(0x2BA, 0x0, 0x64)
    OP_7C(0x190, 0x0, 0xBB8, 0x258)
    OP_83(0x0, 0x0)
    Sleep(400)
    PlayEffect(0x4, 0x0, 0xE, 7000, -2000, 24000, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 0, 0)
    OP_22(0x2BA, 0x0, 0x64)
    OP_7C(0x190, 0x0, 0xBB8, 0x258)
    OP_83(0x0, 0x2)
    Fade(500)
    OP_24(0x79, 0x64)
    OP_24(0x125, 0x3C)
    ClearMapFlags(0x10)
    OP_44(0xE, 0x3)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    SetChrPos(0xE, -300000, -4000, -20000, 90)
    SetChrPos(0xF, 0, -4000, 0, 270)
    SetChrPos(0x10, 0, -4000, 20000, 270)
    SetChrPos(0x11, 50000, -4000, 20000, 270)
    SetChrPos(0x12, 50000, -4000, 20000, 270)
    SetChrPos(0x13, 50000, -4000, 20000, 270)
    OP_D1(14, 0, 86000, 0, 0)
    OP_D1(15, 0, 270000, -5000, 0)
    OP_D1(16, 0, 270000, 5000, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFCE, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_6D(-54120, -10000, -5500, 0)
    OP_67(0, 1480, -10000, 0)
    OP_6B(9750, 0)
    OP_6C(252000, 0)
    OP_6E(536, 0)
    OP_43(0x10, 0x2, 0x0, 0x3F)
    Sleep(600)
    OP_43(0xF, 0x2, 0x0, 0x3D)
    Sleep(2000)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x26FC78, 0x0)
    SetMapFlags(0x10)
    StopSound(0x4E20, 0xB8538, 0xBB8)
    Sleep(1000)
    OP_43(0x0, 0x3, 0x0, 0x20)
    PlayEffect(0x5, 0x0, 0x11, 0, 1000, -12000, 176, 0, -26, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_701E():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_701E)
    Sleep(500)

    def lambda_703E():
        OP_D1(254, 0, 266000, 20000, 1000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_703E)
    Sleep(1000)
    Fade(500)
    OP_24(0x79, 0x64)
    OP_24(0x125, 0x64)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x3)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    SetChrPos(0xE, 0, 2000, 0, 90)
    SetChrPos(0xF, 150000, 0, -10000, 270)
    SetChrPos(0x10, 150000, 0, 40000, 270)
    SetChrPos(0x11, 150000, 5000, 20000, 270)
    OP_D1(14, 0, 90000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_76(0xFF, 0x0, 0x1, 0xF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x14, 0x2, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x32, 0x5, 0x0, 0x0, 0x0)
    OP_6D(79930, -8400, -24930, 0)
    OP_67(0, 1480, -10000, 0)
    OP_6B(12090, 0)
    OP_6C(120000, 0)
    OP_6E(536, 0)
    OP_D0(350000, 0)

    def lambda_71B1():
        OP_6D(13700, -4100, -18370, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_71B1)

    def lambda_71C9():
        OP_6C(192000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_71C9)
    PlayEffect(0x5, 0x0, 0xF, -500, 1000, -12000, 180, 0, 10, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_720E():
        OP_D1(254, 0, 270000, -20000, 1000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_720E)

    def lambda_7228():
        OP_8F(0xFE, 0xFFFCF2C0, 0x2710, 0xFFFFB1E0, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7228)

    def lambda_7243():
        OP_D1(254, 0, 90000, 25000, 1000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_7243)

    def lambda_725D():
        OP_8F(0xFE, 0x0, 0x7D0, 0x4E20, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_725D)
    WaitChrThread(0x0, 0x0)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_82(0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x34)
    Sleep(1000)
    PlayEffect(0x5, 0x0, 0x10, 500, 1000, -12000, 180, 0, -40, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_72CB():
        OP_D1(254, 0, 270000, 40000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_72CB)

    def lambda_72E5():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0xAFC8, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_72E5)
    WaitChrThread(0xE, 0x3)

    def lambda_7305():
        OP_D1(254, 0, 90000, 0, 10000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_7305)
    PlayEffect(0x4, 0x1, 0xE, 2000, -2000, 28000, 0, 0, 0, 3000, 3000, 3000, 0x11, 0, 0, 0, 0)
    OP_22(0x2BA, 0x0, 0x64)
    OP_7C(0x190, 0x0, 0xBB8, 0x258)
    OP_83(0x1, 0x2)
    OP_82(0x0, 0x2)
    OP_23(0x235)
    OP_44(0x0, 0x3)
    PlayEffect(0x1, 0xFF, 0x11, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_73AC():
        OP_D1(254, 20000, 270000, -60000, 4000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_73AC)

    def lambda_73C6():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFF8AD0, 0x4E20, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_73C6)
    Sleep(2500)
    OP_43(0x15, 0x3, 0x0, 0x2F)
    PlayEffect(0x2, 0xFF, 0xFF, 20000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 5000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, -10000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)

    def lambda_74A0():
        OP_6D(23830, -4100, -19830, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_74A0)

    def lambda_74B8():
        OP_67(0, 1580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_74B8)

    def lambda_74D0():
        OP_6C(243000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_74D0)

    def lambda_74E0():
        OP_D1(254, 0, 90000, 20000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_74E0)

    def lambda_74FA():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_74FA)
    Sleep(600)

    def lambda_751A():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_751A)
    Sleep(500)

    def lambda_753A():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_753A)
    Sleep(400)

    def lambda_755A():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_755A)
    Sleep(300)

    def lambda_757A():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_757A)
    Sleep(200)

    def lambda_759A():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_759A)
    Sleep(100)

    def lambda_75BA():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_75BA)
    Sleep(100)

    def lambda_75DA():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_75DA)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_DC()
    OP_DC()
    OP_A2(0x2200)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_46_5F74 end

    def Function_47_7619(): pass

    label("Function_47_7619")

    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x14)
    Sleep(100)
    OP_23(0x79)
    Return()

    # Function_47_7619 end

    def Function_48_7665(): pass

    label("Function_48_7665")

    OP_22(0x125, 0x1, 0x14)
    Sleep(100)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x125, 0x64)
    Return()

    # Function_48_7665 end

    def Function_49_76B3(): pass

    label("Function_49_76B3")

    OP_24(0x125, 0x5A)
    OP_22(0x79, 0x1, 0x14)
    Sleep(100)
    OP_24(0x125, 0x50)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x125, 0x46)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x125, 0x3C)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x125, 0x32)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x125, 0x28)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x64)
    Return()

    # Function_49_76B3 end

    def Function_50_7719(): pass

    label("Function_50_7719")

    Sleep(1000)

    def lambda_7724():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7724)
    Sleep(500)

    def lambda_7744():
        OP_D1(254, 0, 266000, 20000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_7744)
    Sleep(1000)

    def lambda_7763():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7763)
    Sleep(500)

    def lambda_7783():
        OP_D1(254, 0, 266000, 20000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_7783)
    Sleep(1000)

    def lambda_77A2():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_77A2)
    Sleep(500)

    def lambda_77C2():
        OP_D1(254, 0, 266000, 20000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_77C2)
    Return()

    # Function_50_7719 end

    def Function_51_77D7(): pass

    label("Function_51_77D7")

    OP_98(0x0, 0xE)
    OP_98(0x1, 0x9C40, 0x0, 0xFFFFB1E0)
    OP_98(0x1, 0x11170, 0x0, 0x4E20)
    OP_98(0x1, 0x11171, 0x0, 0x4E21)

    def lambda_780B():
        OP_98(0x2, 0xFE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_780B)

    def lambda_781B():
        OP_D1(254, 0, 90000, -20000, 1200)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_781B)
    WaitChrThread(0xE, 0x3)

    def lambda_783A():
        OP_D1(254, 0, 98000, 20000, 2400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_783A)

    def lambda_7854():
        OP_6D(45680, -10500, -5700, 2400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7854)

    def lambda_786C():
        OP_67(0, 1480, -10000, 2400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_786C)
    Return()

    # Function_51_77D7 end

    def Function_52_787F(): pass

    label("Function_52_787F")


    def lambda_7885():
        OP_D1(254, 0, 90000, -20000, 2400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_7885)

    def lambda_789F():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_789F)
    Sleep(300)

    def lambda_78BF():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_78BF)
    Sleep(300)

    def lambda_78DF():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_78DF)
    Sleep(300)

    def lambda_78FF():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_78FF)
    Sleep(300)

    def lambda_791F():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_791F)
    Sleep(800)

    def lambda_793F():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_793F)
    Sleep(300)

    def lambda_795F():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_795F)
    Sleep(300)

    def lambda_797F():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_797F)
    Return()

    # Function_52_787F end

    def Function_53_7995(): pass

    label("Function_53_7995")


    def lambda_799B():
        OP_8F(0xFE, 0xFFFFF830, 0xFA0, 0xFFFF9688, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_799B)
    Sleep(13000)

    def lambda_79BB():
        OP_8F(0xFE, 0xFFFFF830, 0xFA0, 0xFFFF9688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_79BB)
    Sleep(400)

    def lambda_79DB():
        OP_8F(0xFE, 0xFFFFF830, 0xFA0, 0xFFFF9688, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_79DB)
    Sleep(1500)

    def lambda_79FB():
        OP_D1(254, 0, 270000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_79FB)

    def lambda_7A15():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7A15)
    Sleep(100)

    def lambda_7A35():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7A35)
    Sleep(100)

    def lambda_7A55():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7A55)
    Sleep(100)

    def lambda_7A75():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7A75)
    Sleep(100)

    def lambda_7A95():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7A95)
    Sleep(100)

    def lambda_7AB5():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7AB5)
    Sleep(100)

    def lambda_7AD5():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7AD5)
    Sleep(100)

    def lambda_7AF5():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7AF5)
    Sleep(100)

    def lambda_7B15():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7B15)
    Return()

    # Function_53_7995 end

    def Function_54_7B2B(): pass

    label("Function_54_7B2B")


    def lambda_7B31():
        OP_8F(0xFE, 0x7148, 0x1770, 0xFFFFB5C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7B31)
    Sleep(12000)

    def lambda_7B51():
        OP_8F(0xFE, 0x7148, 0x1770, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7B51)
    Sleep(400)

    def lambda_7B71():
        OP_8F(0xFE, 0x7148, 0x1770, 0xFFFFB5C8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7B71)
    Sleep(3500)

    def lambda_7B91():
        OP_D1(254, 0, 270000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_7B91)

    def lambda_7BAB():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7BAB)
    Sleep(100)

    def lambda_7BCB():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7BCB)
    Sleep(100)

    def lambda_7BEB():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7BEB)
    Sleep(100)

    def lambda_7C0B():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C0B)
    Sleep(100)

    def lambda_7C2B():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C2B)
    Sleep(100)

    def lambda_7C4B():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C4B)
    Sleep(100)

    def lambda_7C6B():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C6B)
    Sleep(100)

    def lambda_7C8B():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C8B)
    Sleep(100)

    def lambda_7CAB():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7CAB)
    Return()

    # Function_54_7B2B end

    def Function_55_7CC1(): pass

    label("Function_55_7CC1")


    def lambda_7CC7():
        OP_8F(0xFE, 0x0, 0xBB8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7CC7)
    Sleep(12000)

    def lambda_7CE7():
        OP_8F(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7CE7)
    Sleep(400)

    def lambda_7D07():
        OP_8F(0xFE, 0x0, 0xBB8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D07)
    Sleep(2000)

    def lambda_7D27():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_7D27)

    def lambda_7D41():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D41)
    Sleep(100)

    def lambda_7D61():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D61)
    Sleep(100)

    def lambda_7D81():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D81)
    Sleep(100)

    def lambda_7DA1():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7DA1)
    Sleep(100)

    def lambda_7DC1():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7DC1)
    Sleep(100)

    def lambda_7DE1():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7DE1)
    Sleep(100)

    def lambda_7E01():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7E01)
    Sleep(100)

    def lambda_7E21():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7E21)
    Sleep(100)

    def lambda_7E41():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7E41)
    Return()

    # Function_55_7CC1 end

    def Function_56_7E57(): pass

    label("Function_56_7E57")


    def lambda_7E5D():
        OP_8F(0xFE, 0x6978, 0x1770, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7E5D)
    Sleep(12000)

    def lambda_7E7D():
        OP_8F(0xFE, 0x6978, 0x1770, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7E7D)
    Sleep(400)

    def lambda_7E9D():
        OP_8F(0xFE, 0x6978, 0x1770, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7E9D)
    Sleep(4200)

    def lambda_7EBD():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_7EBD)

    def lambda_7ED7():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7ED7)
    Sleep(100)

    def lambda_7EF7():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7EF7)
    Sleep(100)

    def lambda_7F17():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F17)
    Sleep(100)

    def lambda_7F37():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F37)
    Sleep(100)

    def lambda_7F57():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F57)
    Sleep(100)

    def lambda_7F77():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F77)
    Sleep(100)

    def lambda_7F97():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F97)
    Sleep(100)

    def lambda_7FB7():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7FB7)
    Sleep(100)

    def lambda_7FD7():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7FD7)
    Return()

    # Function_56_7E57 end

    def Function_57_7FED(): pass

    label("Function_57_7FED")


    def lambda_7FF3():
        OP_8F(0xFE, 0x1770, 0xFFFFF448, 0x36B0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7FF3)
    Sleep(12000)

    def lambda_8013():
        OP_8F(0xFE, 0x1770, 0xFFFFF448, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8013)
    Sleep(400)

    def lambda_8033():
        OP_8F(0xFE, 0x1770, 0xFFFFF448, 0x36B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8033)
    Sleep(3000)

    def lambda_8053():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_8053)

    def lambda_806D():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_806D)
    Sleep(100)

    def lambda_808D():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_808D)
    Sleep(100)

    def lambda_80AD():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_80AD)
    Sleep(100)

    def lambda_80CD():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_80CD)
    Sleep(100)

    def lambda_80ED():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_80ED)
    Sleep(100)

    def lambda_810D():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_810D)
    Sleep(100)

    def lambda_812D():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_812D)
    Sleep(100)

    def lambda_814D():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_814D)
    Sleep(100)

    def lambda_816D():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_816D)
    Return()

    # Function_57_7FED end

    def Function_58_8183(): pass

    label("Function_58_8183")

    PlayEffect(0x0, 0x0, 0xF, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 10000, 0)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, -5000, 0)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0x11, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 5000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x3, 0x12, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, -5000, 0)
    Sleep(200)
    PlayEffect(0x0, 0x4, 0x13, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 0, 0)
    Return()

    # Function_58_8183 end

    def Function_59_82A1(): pass

    label("Function_59_82A1")

    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, 15000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 10000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, 25000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 20000, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, 20000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 30000, 0)
    Sleep(400)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, 50000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 35000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, 30000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 40000, 0)
    Sleep(1200)
    SetChrPos(0x16, 160000, 0, 0, 90)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, -5000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -45000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, -25000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -35000, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, -10000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -40000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -6000, -20000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -25000, 0)
    Return()

    # Function_59_82A1 end

    def Function_60_84B8(): pass

    label("Function_60_84B8")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x3, 0x7, 0xFE, 1000, -1000, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0xFE, 3000, 0, -3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_8566():
        OP_91(0xFE, 0xFA0, 0xFFFFF448, 0xFFFFF830, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8566)
    OP_D1(254, 5000, 274000, -15000, 200)
    OP_D1(254, 0, 270000, 0, 300)
    OP_D1(254, 5000, 272000, -10000, 300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_85C3():
        OP_D1(254, 10000, 272000, -30000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_85C3)

    def lambda_85DD():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85DD)
    Sleep(200)

    def lambda_85FD():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85FD)
    Sleep(200)

    def lambda_861D():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_861D)
    Sleep(200)

    def lambda_863D():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_863D)
    Sleep(200)

    def lambda_865D():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_865D)
    Sleep(200)

    def lambda_867D():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_867D)
    Sleep(200)

    def lambda_869D():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_869D)
    Sleep(200)

    def lambda_86BD():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86BD)
    Sleep(200)

    def lambda_86DD():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0xCB20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86DD)
    Return()

    # Function_60_84B8 end

    def Function_61_86F3(): pass

    label("Function_61_86F3")

    OP_43(0xF, 0x0, 0x0, 0x3C)
    Sleep(1400)
    PlayEffect(0x2, 0xFF, 0xFF, 0, -10000, 0, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    Return()

    # Function_61_86F3 end

    def Function_62_873B(): pass

    label("Function_62_873B")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x3, 0x5, 0xFE, 0, -1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xFE, 3000, 0, -3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_87E9():
        OP_91(0xFE, 0xBB8, 0xFFFFF830, 0x7D0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87E9)
    OP_D1(254, -10000, 266000, 10000, 200)
    OP_D1(254, 5000, 270000, 0, 300)
    OP_D1(254, 0, 268000, 10000, 300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8846():
        OP_D1(254, 15000, 268000, 30000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8846)

    def lambda_8860():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8860)
    Sleep(200)

    def lambda_8880():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8880)
    Sleep(200)

    def lambda_88A0():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88A0)
    Sleep(200)

    def lambda_88C0():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88C0)
    Sleep(200)

    def lambda_88E0():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88E0)
    Sleep(200)

    def lambda_8900():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8900)
    Sleep(200)

    def lambda_8920():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8920)
    Sleep(200)

    def lambda_8940():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8940)
    Sleep(200)

    def lambda_8960():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0xCB20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8960)
    Return()

    # Function_62_873B end

    def Function_63_8976(): pass

    label("Function_63_8976")

    OP_43(0x10, 0x0, 0x0, 0x3E)
    Sleep(1400)
    PlayEffect(0x2, 0xFF, 0xFF, 0, -10000, 20000, 260, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    Return()

    # Function_63_8976 end

    def Function_64_89BE(): pass

    label("Function_64_89BE")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    LoadEffect(0x1, "battle\\\\btbomb00.eff")
    LoadEffect(0x2, "map\\\\mpsmk0.eff")
    LoadEffect(0x3, "map\\\\mp095_00.eff")
    LoadEffect(0x4, "monster\\\\ms30800c.eff")
    LoadEffect(0x5, "map\\\\mp106_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x8, 0x1)
    OP_6D(-84460, 1980, 25700, 0)
    OP_67(0, -2400, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(106000, 0)
    OP_6E(576, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, -40000, 0, 0, 90)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 90000, 20000, 0)
    OP_22(0x125, 0x1, 0x46)
    OP_22(0x158, 0x1, 0x64)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 100)
    OP_70(0x1, 0x96)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 3)
    SetChrPos(0x8, 0, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    OP_CF(0x8, 0x2, "Frame134_on_head")
    OP_A1(0x1E, 0x2)
    SetChrPos(0x1E, 200000, 80000, 80000, 270)
    ClearChrFlags(0x1E, 0x100)
    OP_D1(30, 0, 270000, 0, 0)
    OP_B0(0x2, 0x14)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    OP_6D(63620, -10000, 7720, 0)
    OP_67(0, 3450, -10000, 0)
    OP_6B(10700, 0)
    OP_6C(200000, 0)
    OP_6E(1448, 0)
    OP_D0(360000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xA, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xA, 0x2, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x19, 0x5, 0x0, 0x0, 0x0)
    StopSound(0x4E20, 0x1E8480, 0xBB8)

    def lambda_8C01():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8C01)
    OP_D1(30, 0, 225000, 0, 0)
    SetChrPos(0x1E, 100000, 20000, 100000, 270)
    FadeToBright(1000, 0)
    Sleep(2700)
    OP_22(0x159, 0x0, 0x64)
    Sleep(300)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8C66():
        OP_D1(254, 10000, 225000, 40000, 1500)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_8C66)

    def lambda_8C80():
        OP_D0(355000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8C80)

    def lambda_8C90():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8C90)
    Sleep(100)

    def lambda_8CB0():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8CB0)
    Sleep(100)

    def lambda_8CD0():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8CD0)
    Sleep(100)

    def lambda_8CF0():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8CF0)
    Sleep(100)

    def lambda_8D10():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8D10)
    Sleep(100)

    def lambda_8D30():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8D30)
    Sleep(100)

    def lambda_8D50():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8D50)
    Sleep(900)
    Fade(500)
    OP_44(0xE, 0x1)
    OP_44(0x0, 0x0)
    OP_44(0x1E, 0x3)
    OP_71(0x1, 0x4)
    OP_6D(-84460, 1980, 25700, 0)
    OP_67(0, -2400, -10000, 0)
    OP_6B(4050, 0)
    OP_6C(106000, 0)
    OP_6E(576, 0)
    OP_D0(340000, 0)
    SetChrPos(0x1E, 150000, 80000, 80000, 270)
    OP_D1(30, 0, 270000, 0, 0)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 5)
    SetChrFlags(0x8, 0x8)

    def lambda_8DFF():
        OP_D0(360000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8DFF)
    OP_98(0x0, 0x1E)
    OP_98(0x1, 0x11170, 0x9C40, 0xFFFF63C0)
    OP_98(0x1, 0x0, 0x2710, 0x88B8)
    OP_98(0x1, 0xFFFE2B40, 0xFFFFD8F0, 0x61A8)

    def lambda_8E3D():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8E3D)
    OP_43(0x1E, 0x0, 0x0, 0x45)
    Sleep(5000)
    WaitChrThread(0x1E, 0x1)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    ClearChrFlags(0x8, 0x8)
    OP_6D(-1030, 3860, -600, 0)
    OP_67(0, 8810, -10000, 0)
    OP_6B(2090, 0)
    OP_6C(137000, 0)
    OP_6E(362, 0)
    SetChrPos(0x1E, 0, 0, 0, 270)
    OP_D1(30, 0, 270000, 0, 0)
    OP_0D()
    SetChrPos(0x0, 1310, 3860, -1340, 0)
    Sleep(500)
    OP_DC()

    ChrTalk(    #5
        0x8,
        (
            "#124F#6PLet us see, then.\x02\x03",

            "#123FWhat will you do when your wings\x01",
            "of hope are ripped from your back?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_DB()
    OP_1D(0x84)
    Sleep(500)
    Play3DEffect(0x3, 0x0, 0x2, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x3, 0x1, 0x2, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x159, 0x0, 0x64)

    def lambda_9029():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_9029)

    def lambda_9043():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9043)
    Sleep(100)

    def lambda_905E():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_905E)
    Sleep(100)

    def lambda_9079():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9079)
    Sleep(100)

    def lambda_9094():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9094)
    Sleep(100)

    def lambda_90AF():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_90AF)
    Sleep(100)

    def lambda_90CA():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_90CA)
    Sleep(100)

    def lambda_90E5():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_90E5)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x1E, 0x1)
    OP_44(0x1E, 0x3)
    OP_72(0x1, 0x4)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF1, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFD8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    SetChrPos(0x1E, -120000, 0, -20000, 90)
    OP_D1(30, 0, 90000, 0, 0)
    SetChrPos(0xE, 0, 6000, 0, 270)
    OP_D1(14, 0, 270000, 0, 0)
    OP_6D(-12820, 5000, -13570, 0)
    OP_67(0, 1270, -10000, 0)
    OP_6B(7550, 0)
    OP_6C(294000, 0)
    OP_6E(548, 0)
    OP_43(0x1E, 0x0, 0x0, 0x42)
    OP_0D()

    def lambda_91F6():
        OP_6D(520, 3000, 12000, 1900)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_91F6)

    def lambda_920E():
        OP_6C(354000, 1900)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_920E)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_23(0x125)
    OP_23(0x158)
    OP_23(0x1C3)
    Sleep(1000)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT45.dat", 0x0, 0x1)

    label("loc_926C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9286")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_9283")
    Jump("loc_9286")

    label("loc_9283")

    Jump("loc_926C")

    label("loc_9286")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_AD(0x2400AC, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x22AF)
    OP_DC()
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_64_89BE end

    def Function_65_92E0(): pass

    label("Function_65_92E0")

    OP_8F(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xE290, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0, 0, 0, 270, 0, 0, 10000, 10000, 10000, 0xFF, 0, 0, 0, 0)
    OP_22(0x9B, 0x0, 0x64)
    OP_8F(0xFE, 0x186A0, 0x0, 0xFFFFD8F0, 0xE290, 0x0)
    Return()

    # Function_65_92E0 end

    def Function_66_9343(): pass

    label("Function_66_9343")

    OP_72(0x2, 0x20)
    OP_B0(0x2, 0x2)
    OP_6F(0x2, 412)
    OP_70(0x2, 0x1A0)

    def lambda_9360():
        OP_D1(254, 0, 90000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_9360)
    OP_8F(0xFE, 0xFFFFF830, 0x0, 0xFFFFC950, 0xE290, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x258, 0x0, 0x1388, 0x3E8)
    OP_43(0xFE, 0x2, 0x0, 0x43)
    OP_8F(0xFE, 0x1F40, 0x0, 0xFFFFC950, 0x4E20, 0x0)
    OP_22(0x9B, 0x0, 0x64)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 416)
    OP_70(0x2, 0x1AB)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(6520, 3000, -5000, 0)
    OP_6C(72000, 0)

    def lambda_9402():
        OP_D1(254, 0, 90000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9402)
    OP_98(0x0, 0x1E)
    OP_98(0x1, 0x249F0, 0xFA0, 0xFFFFEC78)
    OP_98(0x1, 0x493E0, 0x1F40, 0x7530)

    def lambda_943C():
        OP_98(0x2, 0xFE, 0xE290, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_943C)
    OP_73(0x2)
    OP_22(0x15A, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x14)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    Return()

    # Function_66_9343 end

    def Function_67_9466(): pass

    label("Function_67_9466")

    PlayEffect(0x4, 0xFF, 0xFF, -2000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 2000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 4000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 6000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_67_9466 end

    def Function_68_9570(): pass

    label("Function_68_9570")

    PlayEffect(0x2, 0x7, 0xE, 3000, 0, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0xE, -3000, 0, 3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0, 0, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_9615():
        OP_8F(0xFE, 0x0, 0xFA0, 0x2710, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9615)
    OP_D1(254, 5000, 270000, -25000, 200)
    OP_D1(254, 0, 270000, -15000, 400)
    OP_D1(254, 5000, 270000, -20000, 600)
    WaitChrThread(0xFE, 0x1)

    def lambda_966E():
        OP_D1(254, 10000, 270000, -25000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_966E)

    def lambda_9688():
        OP_8F(0xFE, 0xFFFFD8F0, 0xFFFFB1E0, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9688)
    Return()

    # Function_68_9570 end

    def Function_69_969E(): pass

    label("Function_69_969E")

    OP_D1(30, 10000, 270000, 40000, 2000)

    def lambda_96B7():
        OP_D1(254, 10000, 270000, -40000, 2000)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_96B7)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 350)
    OP_70(0x2, 0x172)
    OP_73(0x2)
    OP_B0(0x2, 0x5)
    OP_6F(0x2, 370)
    OP_70(0x2, 0x177)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x14)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    OP_44(0x1E, 0x3)
    OP_D1(30, 0, 270000, 0, 1000)
    Return()

    # Function_69_969E end

    def Function_70_9729(): pass

    label("Function_70_9729")

    EventBegin(0x0)
    OP_DB()
    OP_E8(0x88, 0x13, 0x0, 0x0)
    OP_D2(0x2701C7, 0x2701CC, 0xA)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-183060, 30000, 22680, 0)
    OP_67(0, -5630, -10000, 0)
    OP_6B(6120, 0)
    OP_6C(325000, 0)
    OP_6E(343, 0)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, -183080, -50000, -10000, 270)
    OP_A1(0x1D, 0x1)
    SetChrPos(0x1D, -183080, 15000, -10000, 270)
    OP_22(0x113, 0x1, 0x5F)
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    PlayEffect(0x2, 0x0, 0x1D, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1D, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x1D, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x1D, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x1D, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x1D, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 281)
    OP_70(0x1, 0x12C)
    SetChrPos(0x1C, 0, 0, 0, 315)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 10)
    SetChrSubChip(0x1C, 0)
    OP_CF(0x1C, 0x1, "Frame85__ren")
    OP_8C(0x1C, 315, 0)
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-183060, 30000, 22680, 0)
    OP_67(0, -5630, -10000, 0)
    OP_6B(6120, 0)
    OP_6C(315000, 0)
    OP_6E(343, 0)

    def lambda_99CF():
        OP_67(0, -2500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99CF)

    def lambda_99E7():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_99E7)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_9A01():
        OP_90(0xFE, 0x0, 0xAFC8, 0x249F0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9A01)
    OP_43(0x1D, 0x3, 0x0, 0x47)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x1D, 0x3)
    Sleep(1000)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_70_9729 end

    def Function_71_9A4A(): pass

    label("Function_71_9A4A")

    OP_24(0x113, 0x5A)
    Sleep(500)
    OP_24(0x113, 0x55)
    Sleep(500)
    OP_24(0x113, 0x50)
    Sleep(500)
    OP_24(0x113, 0x4B)
    Sleep(500)
    OP_24(0x113, 0x46)
    Sleep(500)
    OP_24(0x113, 0x41)
    Sleep(500)
    OP_24(0x113, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x37)
    Sleep(500)
    OP_24(0x113, 0x32)
    Sleep(500)
    OP_24(0x113, 0x28)
    Sleep(500)
    OP_24(0x113, 0x1E)
    Sleep(500)
    OP_23(0x113)
    Return()

    # Function_71_9A4A end

    def Function_72_9AB1(): pass

    label("Function_72_9AB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    LoadEffect(0x0, "map\\mp077_00.eff")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_D2(0x70061, 0x70069, 0xA)
    OP_D2(0x270399, 0x27039D, 0xB)
    OP_D2(0x260240, 0x260245, 0xC)
    OP_D2(0x70180, 0x70184, 0xD)
    OP_D2(0x2701D2, 0x2701D7, 0xE)
    OP_D2(0x70142, 0x70146, 0xF)
    OP_D2(0x70153, 0x70157, 0x10)
    OP_D2(0x70158, 0x7015C, 0x11)
    OP_D2(0x70020, 0x70028, 0x12)
    OP_D2(0x70030, 0x70038, 0x13)
    OP_D2(0x270398, 0x27039C, 0x14)
    OP_D2(0x70050, 0x70058, 0x15)
    OP_D2(0x70060, 0x70068, 0x16)
    OP_D2(0x70070, 0x70078, 0x17)
    OP_D2(0x270080, 0x270084, 0x18)
    OP_D2(0x2700A0, 0x2700A4, 0x19)
    OP_D2(0x26023E, 0x260243, 0x1A)
    OP_D2(0x26023F, 0x260244, 0x1B)
    OP_D2(0x26019D, 0x2601A2, 0x1C)
    OP_D2(0x26019E, 0x2601A3, 0x1D)
    SetChrChipByIndex(0x1F, 26)
    SetChrChipByIndex(0x20, 27)
    SetChrChipByIndex(0x21, 12)
    SetChrChipByIndex(0x22, 13)
    SetChrChipByIndex(0x23, 14)
    SetChrChipByIndex(0x24, 15)
    SetChrChipByIndex(0x25, 16)
    SetChrChipByIndex(0x26, 17)
    SetChrChipByIndex(0x28, 18)
    SetChrChipByIndex(0x29, 19)
    SetChrChipByIndex(0x2A, 20)
    SetChrChipByIndex(0x27, 21)
    SetChrChipByIndex(0x2B, 22)
    SetChrChipByIndex(0x2C, 23)
    SetChrChipByIndex(0x2D, 24)
    SetChrChipByIndex(0x2E, 25)
    OP_6D(190000, 32299, -15160, 0)
    OP_67(0, -520, -10000, 0)
    OP_6B(1300, 0)
    OP_6C(360000, 0)
    OP_6E(750, 0)
    OP_D0(360000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrPos(0x22, 200000, 32299, -15160, 270)
    SetChrPos(0x14, 197920, 33120, -15080, 0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_A1(0xE, 0x1)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xE, 200000, 0, 0, 270)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_A1(0xF, 0x2)
    ClearChrFlags(0xF, 0x100)
    OP_D1(15, 4000, 270000, 0, 0)
    SetChrPos(0xF, 200000, 30000, 0, 270)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)
    OP_A1(0xD, 0x0)
    ClearChrFlags(0xD, 0x100)
    SetChrPos(0x1F, 0, 0, 0, 0)
    SetChrPos(0x20, 0, 0, 0, 0)
    SetChrPos(0x21, 0, 0, 0, 0)
    OP_CF(0x1F, 0x0, "Frame144_back_Null2")
    OP_CF(0x20, 0x0, "Frame145_back_Null3")
    OP_CF(0x21, 0x0, "Frame143_back_Null1")
    OP_71(0x0, 0x20)
    OP_71(0x0, 0x8)
    OP_6F(0x0, 30)
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0xD, 0x7)
    OP_71(0x1, 0x4)
    OP_71(0x0, 0x4)
    OP_22(0x125, 0x1, 0x46)
    FadeToBright(2000, 0)
    OP_6A(0x14)

    def lambda_9DE2():
        OP_8F(0xFE, 0xFFFB6C20, 0x7E2B, 0xFFFFC4C8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9DE2)
    OP_43(0x14, 0x0, 0x0, 0x5F)
    OP_43(0x14, 0x3, 0x0, 0x60)
    OP_22(0x155, 0x1, 0x64)
    Sleep(5000)
    OP_43(0x21, 0x3, 0x0, 0x63)
    Sleep(13500)
    OP_43(0x22, 0x3, 0x0, 0x62)
    Sleep(1500)
    OP_6A(0xFF)

    def lambda_9E30():
        OP_6D(-202480, -120, -15440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9E30)

    def lambda_9E48():
        OP_67(0, 2280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E48)

    def lambda_9E60():
        OP_6B(1900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E60)

    def lambda_9E70():
        OP_6C(702000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9E70)

    def lambda_9E80():
        OP_D0(360000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_9E80)
    WaitChrThread(0x101, 0x0)
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x1)
    ClearChrFlags(0x1F, 0x1)
    ClearChrFlags(0x20, 0x1)
    OP_23(0x155)
    OP_23(0x125)
    SetChrPos(0xD, -270000, -30000, -5080, 90)
    OP_D1(13, -5000, 90000, 0, 0)

    def lambda_9EF5():
        OP_8F(0xFE, 0xFFFEA070, 0x7530, 0xFFFFEC28, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9EF5)
    Sleep(300)
    OP_1D(0x76)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -200000, -5000, -15080, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -200000, -5000, -5080, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -200000, -5000, -25080, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x102, 0x3, 0x0, 0x64)

    def lambda_9FC2():
        OP_6D(-200300, -5320, -13480, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9FC2)

    def lambda_9FDA():
        OP_67(0, -4420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FDA)

    def lambda_9FF2():
        OP_6C(785000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FF2)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xD, 0x1)
    OP_44(0x22, 0x1)
    SetChrFlags(0x22, 0x80)
    OP_6D(21490, 30000, 11030, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(4480, 0)
    OP_6C(230000, 0)
    OP_6E(262, 0)
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x6F158, 0x0)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xD, 0, 15000, 0, 90)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    Sleep(1000)
    FadeToBright(2000, 0)

    def lambda_A0E6():
        OP_6B(4000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0E6)
    OP_6C(237000, 8000)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(-1420, 30000, 5980, 0)
    OP_67(0, 7720, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #6
        0x1F,
        (
            "#1004FWhoa! Ragnard! Why are you here?\x02\x03",

            "#1019FAnd what in the heck are you doing\x01",
            "here, Dad?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x21, 0x10)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 1)
    Sleep(300)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 8)
    Sleep(100)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 9)
    Sleep(500)

    ChrTalk(    #7
        0x21,
        (
            "#080F#6PWell, you DID restore power to the\x01",
            "entire country and avert a war.\x02\x03",

            "#081FI shoved the details off on Morgan and\x01",
            "decided to ask an old friend for a ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x1F,
        "#1007FAn old friend, uh huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x20,
        (
            "#1054FAdmit it, Dad, you just wanted to\x01",
            "surprise us.\x02\x03",

            "#1053FAnd it's a pleasure to meet you,\x01",
            "Ragnard. Estelle told me about you.\x02\x03",

            "#1040FThank you for saving our lives.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #10
        (
            "\x07\x05Thou needst not thank me, child of Man.\x02\x03",

            "A new wind swirls about us. I simply spread\x01",
            "my wings and sailed upon that fresh current.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #11
        0x1F,
        (
            "#1016FHaha... Still, though, you really saved us.\x02\x03",

            "#1004FBut, hang on a second.\x02\x03",

            "#1015FI thought, um, Aidios Herself told you\x01",
            "to only watch over people.\x02\x03",

            "Won't you get in trouble for saving us?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #12
        (
            "\x07\x05The charge given me was to watch over\x01",
            "Man until an answer--a true answer--was\x01",
            "given unto the Shining Ring.\x02\x03",

            "And such an answer has now been offered\x01",
            "up. The ancient contract stands fulfilled.\x02\x03",

            "Thus, upon hearing the Divine Blade's plea\x01",
            "for a boon, I myself answered in kind.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #13
        0x20,
        "#1044FThe ancient contract?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x1F,
        (
            "#1019FAnother little mystery, but I can\x01",
            "let it slide. I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x21, 0x9, 0xB, 0x7D0)
    Sleep(100)
    OP_43(0x21, 0x0, 0x0, 0x4A)
    WaitChrThread(0x21, 0x0)

    ChrTalk(    #15
        0x21,
        (
            "#083F#6PI haven't the foggiest what he's going\x01",
            "on about, either.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x21, 0x0)
    OP_99(0x21, 0xD, 0x9, 0x3E8)
    Fade(100)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x21,
        (
            "#080FAfter all, hard-head here seems to\x01",
            "enjoy holding back the details.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #17
        (
            "\x07\x05Forgive me, friends. We of the wing and\x01",
            "scale possesseth our own laws and statues.\x02\x03",

            "So it is I say unto you: know that the gears of\x01",
            "fate have finally begun their inexorable churn.\x02\x03",

            "And in their ponderous cycling, no force\x01",
            "can stop them.\x02\x03",

            "The quest is done, but the campaign yet lies\x01",
            "before thee. Gird thyself with wisdom, you who\x01",
            "hear me now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #18
        0x21,
        "#082FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x1F,
        "#1020FWait, no way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x20,
        "#1042FIs Liberl going to be attacked again?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(100)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 9)
    OP_0D()
    OP_99(0x21, 0x9, 0xB, 0x3E8)
    Sleep(500)

    ChrTalk(    #21
        0x21,
        (
            "#085F#6PNo. Those battles are destined to be\x01",
            "fought elsewhere, and by different people.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x21, 0xB, 0x9, 0x3E8)
    Sleep(500)

    ChrTalk(    #22
        0x21,
        (
            "#080F#6PBut those are concerns for another time.\x01",
            "You two have worked a genuine miracle\x01",
            "today.\x02\x03",

            "Don't worry about what's to come for now.\x01",
            "You have earned your rest.\x02\x03",

            "Alongside your irreplaceable friends...\x01",
            "who, I think, will be very happy to see\x01",
            "you alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1F,
        "#1008FYeah...\x02",
    )

    CloseMessageWindow()
    OP_DB()
    OP_43(0x20, 0x3, 0x0, 0x49)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x8)
    Sleep(500)
    OP_A2(0x2)
    OP_72(0x2, 0x4)
    OP_D1(15, 0, 270000, 0, 0)
    SetChrPos(0xF, 120000, 10000, 0, 270)
    OP_48()
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x2B, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0x2A, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x27, 0x1)
    ClearChrFlags(0x28, 0x1)
    ClearChrFlags(0x29, 0x1)
    ClearChrFlags(0x23, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x2D, 0x1)
    ClearChrFlags(0x2C, 0x1)
    ClearChrFlags(0x24, 0x1)
    SetChrBattleFlags(0x2B, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0x2A, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0x27, 0x20)
    SetChrBattleFlags(0x28, 0x20)
    SetChrBattleFlags(0x29, 0x20)
    SetChrBattleFlags(0x23, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0x2D, 0x20)
    SetChrBattleFlags(0x2C, 0x20)
    SetChrBattleFlags(0x24, 0x20)
    SetChrFlags(0x2B, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    OP_89(0x2B, 104080, 11860, 60, 270)
    OP_89(0xC, 104670, 11950, 840, 270)
    OP_89(0x2A, 104430, 12360, -900, 270)
    OP_89(0xB, 105220, 12330, 930, 270)
    OP_89(0x27, 104890, 12270, -480, 270)
    OP_89(0x28, 105150, 12350, -1520, 270)
    OP_89(0x29, 106610, 11480, 1420, 270)
    OP_89(0x9, 106600, 11650, 150, 270)
    OP_89(0x2D, 106770, 12050, -1460, 270)
    OP_89(0x2C, 107810, 11410, -220, 270)
    OP_89(0x23, 107450, 11320, 910, 270)
    OP_89(0x24, 107670, 12010, -1810, 270)
    SetChrChipByIndex(0x2B, 10)
    SetChrSubChip(0x2B, 0)
    SetChrChipByIndex(0x2A, 11)
    SetChrSubChip(0x2A, 0)
    SetChrPos(0xF, 220000, 10000, -30000, 270)
    OP_D1(15, 0, 270000, 0, 0)

    def lambda_AD03():
        OP_8F(0xFE, 0x0, 0x2710, 0xFFFFB1E0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AD03)
    OP_22(0x125, 0x1, 0x14)

    def lambda_AD23():
        OP_6D(51560, 15660, -17500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AD23)

    def lambda_AD3B():
        OP_67(0, 8200, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD3B)

    def lambda_AD53():
        OP_6C(102000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD53)

    def lambda_AD63():
        OP_6E(792, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AD63)
    WaitChrThread(0x101, 0x1)

    def lambda_AD78():
        OP_67(0, 2200, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD78)
    WaitChrThread(0x101, 0x1)
    OP_24(0x125, 0x1E)
    Sleep(1000)
    OP_24(0x125, 0x28)
    Sleep(1000)
    OP_24(0x125, 0x32)
    Sleep(1000)
    OP_44(0xF, 0x1)
    SetChrPos(0xF, -90000, 10000, -25000, 90)
    OP_D1(15, 0, 90000, 0, 0)
    LoadEffect(0x1, "map\\\\mp032_00.eff")
    Fade(1000)
    OP_71(0x0, 0x4)
    OP_6D(-74360, 12520, -24750, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(246000, 0)
    OP_6E(528, 0)
    OP_8C(0x2B, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_8C(0x2A, 90, 0)
    OP_8C(0xB, 90, 0)
    OP_8C(0x27, 90, 0)
    OP_8C(0x28, 90, 0)
    OP_8C(0x29, 90, 0)
    OP_8C(0x23, 90, 0)
    OP_8C(0x9, 90, 0)
    OP_8C(0x2D, 90, 0)
    OP_8C(0x2C, 90, 0)
    OP_8C(0x24, 90, 0)
    OP_43(0x2C, 0x0, 0x0, 0x4D)
    OP_43(0x9, 0x0, 0x0, 0x4E)
    OP_43(0x27, 0x0, 0x0, 0x4F)
    OP_43(0x28, 0x0, 0x0, 0x50)
    OP_43(0xB, 0x0, 0x0, 0x51)
    OP_43(0x29, 0x0, 0x0, 0x52)
    OP_43(0x2A, 0x0, 0x0, 0x53)
    OP_43(0x2B, 0x0, 0x0, 0x54)
    OP_43(0x2D, 0x0, 0x0, 0x55)
    OP_43(0xC, 0x0, 0x0, 0x56)
    OP_43(0x23, 0x0, 0x0, 0x57)
    OP_43(0x24, 0x0, 0x0, 0x58)
    OP_24(0x125, 0x3C)
    OP_0D()
    Sleep(1000)
    OP_24(0x125, 0x46)

    def lambda_AEE9():
        OP_6D(-70360, 16370, -24750, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AEE9)

    def lambda_AF01():
        OP_67(0, 3800, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF01)

    def lambda_AF19():
        OP_6C(206000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AF19)
    OP_72(0x1, 0x4)
    OP_D1(14, 0, 90000, 10000, 0)
    SetChrPos(0xE, -120000, 5000, -50000, 90)
    SetChrBattleFlags(0x2E, 0x20)
    SetChrBattleFlags(0x25, 0x20)
    SetChrBattleFlags(0x26, 0x20)
    OP_48()
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x2E, 0x1)
    ClearChrFlags(0x25, 0x1)
    ClearChrFlags(0x26, 0x1)
    OP_89(0x2E, -119350, 11040, -46600, 75)
    OP_89(0x25, -120480, 11010, -46460, 75)
    OP_89(0x26, -116240, 15200, -48160, 75)
    OP_E5(0x2E, 0x0, 0x0)
    OP_E5(0x25, 0x0, 0x0)
    OP_E5(0x26, 0x0, 0x0)
    SetChrFlags(0x2E, 0x2)
    SetChrFlags(0x25, 0x2)
    SetChrChipByIndex(0x2E, 29)
    SetChrSubChip(0x2E, 24)
    SetChrChipByIndex(0x25, 29)
    SetChrSubChip(0x25, 48)
    OP_43(0x2E, 0x0, 0x0, 0x59)
    OP_43(0x25, 0x0, 0x0, 0x5A)
    OP_9F(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x79, 0x1, 0x32)

    def lambda_AFFB():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AFFB)
    Sleep(4200)

    def lambda_B01B():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B01B)
    Sleep(200)

    def lambda_B03B():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B03B)
    Sleep(200)

    def lambda_B05B():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B05B)
    Sleep(200)

    def lambda_B07B():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B07B)
    Sleep(200)

    def lambda_B09B():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B09B)
    Sleep(200)

    def lambda_B0BB():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B0BB)
    Sleep(200)

    def lambda_B0DB():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B0DB)
    OP_72(0x1, 0x20)
    OP_43(0x26, 0x0, 0x0, 0x61)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x26, 0x0)
    Sleep(2000)
    Fade(500)
    OP_44(0x2B, 0x0)
    OP_44(0xC, 0x0)
    OP_44(0x2E, 0x0)
    SetChrPos(0xE, 100000, 0, 0, 90)
    SetChrPos(0xF, 100000, 0, -20000, 90)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 5)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 5)
    ClearChrFlags(0x21, 0x2)
    SetChrSubChip(0x21, 0)
    OP_8C(0x21, 0, 0)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_A3(0x2)
    OP_43(0x102, 0x3, 0x0, 0x65)
    OP_6D(6010, 29000, -1560, 0)
    OP_67(0, 7440, -10000, 0)
    OP_6B(650, 0)
    OP_6C(297000, 0)
    OP_6E(750, 0)
    OP_24(0x125, 0x14)
    OP_24(0x79, 0x14)
    OP_0D()
    Sleep(600)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 8)
    Sleep(100)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 9)
    Sleep(200)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 8)
    Sleep(100)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 9)
    Sleep(600)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 10)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 10)
    Sleep(150)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 11)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 11)
    Sleep(150)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 10)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 10)
    Sleep(150)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 9)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 9)
    Sleep(1000)
    Fade(100)
    OP_43(0x1F, 0x0, 0x0, 0x4B)
    Sleep(50)
    OP_43(0x20, 0x0, 0x0, 0x4C)
    OP_0D()

    def lambda_B2AC():
        OP_6E(600, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2AC)
    Sleep(4500)
    OP_A2(0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_23(0x1C3)
    OP_23(0x125)
    OP_23(0x79)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    OP_EA(0x16, 0x0, 0x0, 0x0)
    PlayMovie(0x0, "ED6_DT47.dat", 0x8, 0x0)
    OP_21()
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T5200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_72_9AB1 end

    def Function_73_B372(): pass

    label("Function_73_B372")

    OP_24(0x1C3, 0x5A)
    Sleep(300)
    OP_24(0x1C3, 0x50)
    Sleep(300)
    OP_24(0x1C3, 0x46)
    Sleep(300)
    OP_24(0x1C3, 0x3C)
    Sleep(300)
    OP_24(0x1C3, 0x32)
    Sleep(300)
    OP_24(0x1C3, 0x28)
    Sleep(300)
    OP_24(0x1C3, 0x1E)
    Sleep(300)
    OP_24(0x1C3, 0x14)
    Sleep(300)
    OP_24(0x1C3, 0xA)
    Sleep(300)
    OP_23(0x1C3)
    Return()

    # Function_73_B372 end

    def Function_74_B3C7(): pass

    label("Function_74_B3C7")

    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 12)
    Sleep(200)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 13)
    Sleep(200)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 14)
    Sleep(300)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 13)
    Sleep(80)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 15)
    Sleep(300)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 13)
    Sleep(200)
    Return()

    # Function_74_B3C7 end

    def Function_75_B422(): pass

    label("Function_75_B422")

    OP_99(0xFE, 0x10, 0x11, 0x5DC)
    OP_99(0xFE, 0xD, 0xF, 0x5DC)
    Sleep(50)
    SetChrSubChip(0xFE, 21)
    Sleep(50)

    label("loc_B443")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B458")
    OP_99(0xFE, 0x10, 0x15, 0x5DC)
    Jump("loc_B443")

    label("loc_B458")

    Return()

    # Function_75_B422 end

    def Function_76_B459(): pass

    label("Function_76_B459")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B46E")
    OP_99(0xFE, 0x10, 0x15, 0x5DC)
    Jump("Function_76_B459")

    label("loc_B46E")

    Return()

    # Function_76_B459 end

    def Function_77_B46F(): pass

    label("Function_77_B46F")

    OP_48()
    Sleep(400)
    OP_91(0xFE, 0x834, 0x0, 0x0, 0x1C2, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 56)
    Sleep(2000)
    SetChrSubChip(0xFE, 56)
    Sleep(100)
    SetChrSubChip(0xFE, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 58)
    Sleep(150)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 60)
    Sleep(200)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 58)
    Sleep(150)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 60)
    Sleep(200)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 58)
    Sleep(100)
    SetChrSubChip(0xFE, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 56)
    Return()

    # Function_77_B46F end

    def Function_78_B51B(): pass

    label("Function_78_B51B")

    OP_48()
    Sleep(250)
    OP_91(0xFE, 0x8FC, 0x0, 0x0, 0x2BC, 0x0)
    Sleep(1500)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 32)
    Sleep(100)
    SetChrSubChip(0xFE, 33)
    Return()

    # Function_78_B51B end

    def Function_79_B554(): pass

    label("Function_79_B554")

    OP_48()
    Sleep(350)
    OP_91(0xFE, 0xA28, 0x0, 0x0, 0x258, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 8)
    Sleep(1000)
    SetChrSubChip(0xFE, 9)
    Sleep(100)
    SetChrSubChip(0xFE, 10)
    Sleep(1000)
    SetChrSubChip(0xFE, 9)
    Sleep(100)
    SetChrSubChip(0xFE, 8)
    Sleep(1000)
    SetChrSubChip(0xFE, 11)
    Sleep(200)
    SetChrSubChip(0xFE, 12)
    Return()

    # Function_79_B554 end

    def Function_80_B5BA(): pass

    label("Function_80_B5BA")

    OP_48()
    Sleep(300)
    OP_91(0xFE, 0xA28, 0x0, 0x0, 0x28A, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 6)
    Sleep(500)
    SetChrSubChip(0xFE, 6)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_80_B5BA end

    def Function_81_B62A(): pass

    label("Function_81_B62A")

    OP_48()
    Sleep(200)
    OP_91(0xFE, 0x9C4, 0x0, 0x0, 0x2EE, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 13)
    Sleep(1000)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(1000)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(1000)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Return()

    # Function_81_B62A end

    def Function_82_B744(): pass

    label("Function_82_B744")

    OP_48()
    Sleep(300)
    OP_91(0xFE, 0x8FC, 0x0, 0x0, 0x1F4, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 16)
    Sleep(1000)
    SetChrSubChip(0xFE, 17)
    Sleep(200)
    SetChrSubChip(0xFE, 18)
    Sleep(200)
    SetChrSubChip(0xFE, 19)
    Sleep(200)
    SetChrSubChip(0xFE, 20)
    Sleep(200)
    SetChrSubChip(0xFE, 21)
    Sleep(200)
    SetChrSubChip(0xFE, 22)
    Sleep(1500)
    SetChrSubChip(0xFE, 21)
    Sleep(200)
    SetChrSubChip(0xFE, 20)
    Sleep(200)
    SetChrSubChip(0xFE, 19)
    Sleep(200)
    SetChrSubChip(0xFE, 18)
    Sleep(200)
    SetChrSubChip(0xFE, 17)
    Sleep(200)
    SetChrSubChip(0xFE, 16)
    Return()

    # Function_82_B744 end

    def Function_83_B7E6(): pass

    label("Function_83_B7E6")

    OP_48()
    Sleep(200)
    OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 37)
    SetChrChipByIndex(0xFE, 29)
    Sleep(2000)
    SetChrSubChip(0xFE, 37)
    Sleep(100)
    SetChrSubChip(0xFE, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 39)
    Sleep(2000)
    SetChrSubChip(0xFE, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 37)
    Return()

    # Function_83_B7E6 end

    def Function_84_B842(): pass

    label("Function_84_B842")

    OP_48()
    OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 8)
    Sleep(200)
    SetChrSubChip(0xFE, 9)
    Sleep(300)
    SetChrSubChip(0xFE, 6)
    Sleep(400)
    SetChrSubChip(0xFE, 7)
    Sleep(500)
    OP_9E(0xFE, 0x8, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    SetChrSubChip(0xFE, 15)
    Sleep(300)
    SetChrSubChip(0xFE, 13)
    Sleep(150)

    label("loc_B9A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9ED")
    SetChrSubChip(0xFE, 8)
    Sleep(150)
    SetChrSubChip(0xFE, 9)
    Sleep(150)
    SetChrSubChip(0xFE, 10)
    Sleep(150)
    SetChrSubChip(0xFE, 11)
    Sleep(150)
    SetChrSubChip(0xFE, 12)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    Jump("loc_B9A5")

    label("loc_B9ED")

    Return()

    # Function_84_B842 end

    def Function_85_B9EE(): pass

    label("Function_85_B9EE")

    OP_48()
    Sleep(350)
    OP_91(0xFE, 0x8FC, 0x0, 0x0, 0x226, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 30)
    Sleep(150)
    SetChrSubChip(0xFE, 31)
    Sleep(150)
    SetChrSubChip(0xFE, 23)
    Return()

    # Function_85_B9EE end

    def Function_86_BA36(): pass

    label("Function_86_BA36")

    OP_48()
    Sleep(250)
    OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 46)
    Sleep(500)

    label("loc_BA64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBAB")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Jump("loc_BA64")

    label("loc_BBAB")

    Return()

    # Function_86_BA36 end

    def Function_87_BBAC(): pass

    label("Function_87_BBAC")

    OP_48()
    Sleep(450)
    OP_91(0xFE, 0x834, 0x0, 0x0, 0x190, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 7)
    Return()

    # Function_87_BBAC end

    def Function_88_BBD6(): pass

    label("Function_88_BBD6")

    OP_48()
    Sleep(450)
    OP_91(0xFE, 0x834, 0x0, 0x0, 0x190, 0x0)
    Return()

    # Function_88_BBD6 end

    def Function_89_BBF1(): pass

    label("Function_89_BBF1")

    Sleep(2500)
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 26)
    Sleep(150)
    SetChrSubChip(0xFE, 27)
    Sleep(150)
    SetChrSubChip(0xFE, 28)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 26)
    Sleep(150)
    SetChrSubChip(0xFE, 27)
    Sleep(150)
    SetChrSubChip(0xFE, 28)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 34)
    Sleep(150)
    SetChrSubChip(0xFE, 35)
    Sleep(150)
    SetChrSubChip(0xFE, 36)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)

    label("loc_BCAA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BCF2")
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 26)
    Sleep(150)
    SetChrSubChip(0xFE, 27)
    Sleep(150)
    SetChrSubChip(0xFE, 28)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)
    Jump("loc_BCAA")

    label("loc_BCF2")

    Return()

    # Function_89_BBF1 end

    def Function_90_BCF3(): pass

    label("Function_90_BCF3")

    Sleep(2500)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 43)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 41)
    Sleep(150)
    SetChrSubChip(0xFE, 40)
    Sleep(150)
    SetChrSubChip(0xFE, 41)
    Sleep(150)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 43)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 45)
    Sleep(150)
    SetChrSubChip(0xFE, 48)
    Return()

    # Function_90_BCF3 end

    def Function_91_BD8A(): pass

    label("Function_91_BD8A")

    OP_8F(0xFE, 0xB82E, 0x7530, 0xFFFFE3EA, 0x1F40, 0x0)
    OP_8F(0xFE, 0xFFFFE6EC, 0x3F5B, 0xFFFFA588, 0x2EE0, 0x0)
    OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0xFA0, 0x0)
    Return()

    # Function_91_BD8A end

    def Function_92_BDC7(): pass

    label("Function_92_BDC7")


    def lambda_BDCD():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_BDCD)
    OP_8F(0xFE, 0x27100, 0x249F0, 0x0, 0x1F40, 0x0)
    Return()

    # Function_92_BDC7 end

    def Function_93_BDEA(): pass

    label("Function_93_BDEA")

    OP_98(0x0, 0x22)
    OP_98(0x1, 0xFFFF63C0, 0x84D0, 0xFFFFC4C8)
    OP_98(0x1, 0xFFFF15A0, 0x9470, 0x4E20)
    OP_98(0x1, 0xFFFE2B40, 0x4E20, 0x4E20)

    def lambda_BE1E():
        OP_98(0x2, 0xFE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_BE1E)
    Return()

    # Function_93_BDEA end

    def Function_94_BE29(): pass

    label("Function_94_BE29")


    def lambda_BE2F():
        OP_6D(-28420, 33660, -15760, 3400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BE2F)

    def lambda_BE47():
        OP_67(0, -2320, -10000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE47)

    def lambda_BE5F():
        OP_6C(312000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE5F)
    WaitChrThread(0x101, 0x1)

    def lambda_BE74():
        OP_6D(-16840, 34860, 10260, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BE74)

    def lambda_BE8C():
        OP_67(0, 1060, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE8C)

    def lambda_BEA4():
        OP_6C(270000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEA4)

    def lambda_BEB4():
        OP_D0(10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BEB4)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_94_BE29 end

    def Function_95_BEC4(): pass

    label("Function_95_BEC4")


    def lambda_BECA():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BECA)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x5A)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x50)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x46)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x3C)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x32)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x28)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x1E)
    Sleep(1000)

    def lambda_BF4C():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4D58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BF4C)
    Sleep(400)

    def lambda_BF6C():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4BC8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BF6C)
    Sleep(400)
    OP_24(0x79, 0x14)

    def lambda_BF90():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BF90)
    Sleep(400)

    def lambda_BFB0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x48A8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BFB0)
    Sleep(400)

    def lambda_BFD0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4718, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BFD0)
    Sleep(400)

    def lambda_BFF0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x44C0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BFF0)
    Sleep(400)
    OP_24(0x79, 0xA)

    def lambda_C014():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C014)
    Sleep(400)

    def lambda_C034():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x3F48, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C034)
    Sleep(400)

    def lambda_C054():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x3CF0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C054)
    Sleep(400)

    def lambda_C074():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x3908, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C074)
    Return()

    # Function_95_BEC4 end

    def Function_96_C08A(): pass

    label("Function_96_C08A")


    def lambda_C090():
        OP_6C(680000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C090)

    def lambda_C0A0():
        OP_67(0, 3080, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C0A0)

    def lambda_C0B8():
        OP_6B(720, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C0B8)

    def lambda_C0C8():
        OP_D0(355000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C0C8)
    WaitChrThread(0x101, 0x1)

    def lambda_C0DD():
        OP_67(0, 5580, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C0DD)

    def lambda_C0F5():
        OP_6B(1640, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C0F5)

    def lambda_C105():
        OP_D0(370000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C105)
    WaitChrThread(0x101, 0x1)

    def lambda_C11A():
        OP_67(0, 8820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C11A)

    def lambda_C132():
        OP_6B(720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C132)
    Return()

    # Function_96_C08A end

    def Function_97_C13D(): pass

    label("Function_97_C13D")

    OP_6F(0x1, 61)
    OP_70(0x1, 0x5F)
    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
    Return()

    # Function_97_C13D end

    def Function_98_C15C(): pass

    label("Function_98_C15C")

    OP_24(0x155, 0x5A)
    Sleep(300)
    OP_24(0x155, 0x50)
    Sleep(300)
    OP_24(0x155, 0x46)
    Sleep(300)
    OP_24(0x155, 0x3C)
    Sleep(300)
    OP_24(0x155, 0x32)
    Sleep(300)
    OP_24(0x155, 0x28)
    Sleep(300)
    OP_24(0x155, 0x1E)
    Sleep(300)
    OP_24(0x155, 0x14)
    Sleep(300)
    OP_24(0x155, 0xA)
    Return()

    # Function_98_C15C end

    def Function_99_C1A9(): pass

    label("Function_99_C1A9")

    OP_24(0x125, 0x3C)
    Sleep(500)
    OP_24(0x125, 0x32)
    Sleep(500)
    OP_24(0x125, 0x28)
    Sleep(500)
    OP_24(0x125, 0x1E)
    Sleep(500)
    OP_24(0x125, 0x14)
    Sleep(500)
    OP_24(0x125, 0xA)
    Return()

    # Function_99_C1A9 end

    def Function_100_C1DB(): pass

    label("Function_100_C1DB")

    Sleep(800)
    OP_22(0x120, 0x0, 0x50)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(2400)

    label("loc_C208")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C21B")
    Jump("loc_C228")

    label("loc_C21B")

    OP_22(0x120, 0x0, 0x5A)
    Sleep(2000)
    Jump("loc_C208")

    label("loc_C228")

    OP_22(0x120, 0x0, 0x55)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x41)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x2D)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x19)
    Sleep(2000)
    Return()

    # Function_100_C1DB end

    def Function_101_C251(): pass

    label("Function_101_C251")

    Sleep(1100)

    label("loc_C256")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C269")
    Jump("loc_C276")

    label("loc_C269")

    OP_22(0x120, 0x0, 0x50)
    Sleep(2000)
    Jump("loc_C256")

    label("loc_C276")

    OP_22(0x120, 0x0, 0x46)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x28)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x14)
    Sleep(2000)
    Return()

    # Function_101_C251 end

    SaveToFile()

Try(main)
