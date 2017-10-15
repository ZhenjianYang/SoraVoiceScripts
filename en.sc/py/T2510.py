from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2510   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2510.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Dean Collins',                         # 9
        'Jill',                                 # 10
        'Hans',                                 # 11
        'Fauna',                                # 12
        'Mr. Ratio',                            # 13
        'Ms. Wiola',                            # 14
        'Ms. Millia',                           # 15
        'Scherazard',                           # 16
        'Agate',                                # 17
        'Rhody',                                # 18
        'Alice',                                # 19
        'Taylor',                               # 20
        'Logic',                                # 21
        'Thelma',                               # 22
        'Richelle',                             # 23
        'Patrick',                              # 24
        'Gerome',                               # 25
        'Nikita',                               # 26
        'Argyle',                               # 27
        'Mickey',                               # 28
        'Monica',                               # 29
        'Dennis',                               # 30
        'Reina',                                # 31
        'Gilbert',                              # 32
        'Kaden',                                # 33
        'Purity',                               # 34
        'Enhanced Jaeger',                      # 35
        'Enhanced Jaeger',                      # 36
        'Enhanced Jaeger',                      # 37
        'Enhanced Jaeger',                      # 38
        'Targeting Camera',                     # 39
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
        'ED6_DT07/CH02600 ._CH',             # 00
        'ED6_DT07/CH02603 ._CH',             # 01
        'ED6_DT07/CH02390 ._CH',             # 02
        'ED6_DT07/CH02550 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01663 ._CH',             # 05
        'ED6_DT07/CH01210 ._CH',             # 06
        'ED6_DT07/CH01213 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
        'ED6_DT07/CH01433 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH00050 ._CH',             # 0B
        'ED6_DT07/CH01360 ._CH',             # 0C
        'ED6_DT07/CH01590 ._CH',             # 0D
        'ED6_DT07/CH01370 ._CH',             # 0E
        'ED6_DT07/CH01080 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
        'ED6_DT07/CH01590 ._CH',             # 11
        'ED6_DT07/CH01580 ._CH',             # 12
        'ED6_DT27/CH03750 ._CH',             # 13
        'ED6_DT07/CH01580 ._CH',             # 14
        'ED6_DT07/CH01090 ._CH',             # 15
        'ED6_DT27/CH03610 ._CH',             # 16
        'ED6_DT07/CH01370 ._CH',             # 17
        'ED6_DT07/CH01360 ._CH',             # 18
        'ED6_DT07/CH01370 ._CH',             # 19
        'ED6_DT26/CH20501 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH02600P._CP',             # 00
        'ED6_DT07/CH02603P._CP',             # 01
        'ED6_DT07/CH02390P._CP',             # 02
        'ED6_DT07/CH02550P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01663P._CP',             # 05
        'ED6_DT07/CH01210P._CP',             # 06
        'ED6_DT07/CH01213P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
        'ED6_DT07/CH01433P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH00050P._CP',             # 0B
        'ED6_DT07/CH01360P._CP',             # 0C
        'ED6_DT07/CH01590P._CP',             # 0D
        'ED6_DT07/CH01370P._CP',             # 0E
        'ED6_DT07/CH01080P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
        'ED6_DT07/CH01590P._CP',             # 11
        'ED6_DT07/CH01580P._CP',             # 12
        'ED6_DT27/CH03750P._CP',             # 13
        'ED6_DT07/CH01580P._CP',             # 14
        'ED6_DT07/CH01090P._CP',             # 15
        'ED6_DT27/CH03610P._CP',             # 16
        'ED6_DT07/CH01370P._CP',             # 17
        'ED6_DT07/CH01360P._CP',             # 18
        'ED6_DT07/CH01370P._CP',             # 19
        'ED6_DT26/CH20501P._CP',             # 1A
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 30700,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 41200,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 87640,
        Z                   = 200,
        Y                   = 2820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 89300,
        Z                   = 0,
        Y                   = 1960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 86880,
        Z                   = 0,
        Y                   = 4250,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 85540,
        Z                   = 0,
        Y                   = 4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 85540,
        Z                   = 0,
        Y                   = 4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 29880,
        Z                   = 0,
        Y                   = -280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 2630,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 37090,
        Z                   = 0,
        Y                   = 1590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 4800,
        Z                   = 250,
        Y                   = 28940,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 43890,
        Z                   = 0,
        Y                   = 34970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 36990,
        Z                   = 0,
        Y                   = 30690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 47460,
        Z                   = 0,
        Y                   = 32880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 93000,
        Z                   = 0,
        Y                   = 31990,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 95320,
        Z                   = 250,
        Y                   = 33480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 44150,
        Z                   = 0,
        Y                   = 270,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -4120,
        Z                   = 0,
        Y                   = 5200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        X                   = 51000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 83,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 84,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 85,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )


    DeclActor(
        TriggerX            = 41150,
        TriggerZ            = 0,
        TriggerY            = 5500,
        TriggerRange        = 400,
        ActorX              = 41200,
        ActorZ              = 1700,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 116010,
        TriggerZ            = 0,
        TriggerY            = 2750,
        TriggerRange        = 400,
        ActorX              = 116010,
        ActorZ              = 1700,
        ActorY              = 4800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 82,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_66E",          # 00, 0
        "Function_1_DB4",          # 01, 1
        "Function_2_E4E",          # 02, 2
        "Function_3_E72",          # 03, 3
        "Function_4_E96",          # 04, 4
        "Function_5_EBA",          # 05, 5
        "Function_6_EDE",          # 06, 6
        "Function_7_FB3",          # 07, 7
        "Function_8_FD7",          # 08, 8
        "Function_9_18C6",         # 09, 9
        "Function_10_1A29",        # 0A, 10
        "Function_11_1DB5",        # 0B, 11
        "Function_12_218D",        # 0C, 12
        "Function_13_24EE",        # 0D, 13
        "Function_14_3182",        # 0E, 14
        "Function_15_37D4",        # 0F, 15
        "Function_16_3C1E",        # 10, 16
        "Function_17_4616",        # 11, 17
        "Function_18_493A",        # 12, 18
        "Function_19_4C93",        # 13, 19
        "Function_20_4E91",        # 14, 20
        "Function_21_5178",        # 15, 21
        "Function_22_524A",        # 16, 22
        "Function_23_531B",        # 17, 23
        "Function_24_56BF",        # 18, 24
        "Function_25_5F6B",        # 19, 25
        "Function_26_62F5",        # 1A, 26
        "Function_27_6686",        # 1B, 27
        "Function_28_6FFD",        # 1C, 28
        "Function_29_70A0",        # 1D, 29
        "Function_30_7119",        # 1E, 30
        "Function_31_7276",        # 1F, 31
        "Function_32_72DC",        # 20, 32
        "Function_33_746D",        # 21, 33
        "Function_34_7695",        # 22, 34
        "Function_35_81BA",        # 23, 35
        "Function_36_88F4",        # 24, 36
        "Function_37_8994",        # 25, 37
        "Function_38_8A1C",        # 26, 38
        "Function_39_8C61",        # 27, 39
        "Function_40_8F7C",        # 28, 40
        "Function_41_9534",        # 29, 41
        "Function_42_953D",        # 2A, 42
        "Function_43_9990",        # 2B, 43
        "Function_44_9B17",        # 2C, 44
        "Function_45_9B20",        # 2D, 45
        "Function_46_9F33",        # 2E, 46
        "Function_47_A09A",        # 2F, 47
        "Function_48_A0A3",        # 30, 48
        "Function_49_A46B",        # 31, 49
        "Function_50_A5D2",        # 32, 50
        "Function_51_A621",        # 33, 51
        "Function_52_A675",        # 34, 52
        "Function_53_A6C9",        # 35, 53
        "Function_54_A71D",        # 36, 54
        "Function_55_AEE9",        # 37, 55
        "Function_56_AF4C",        # 38, 56
        "Function_57_AFB4",        # 39, 57
        "Function_58_B01C",        # 3A, 58
        "Function_59_B070",        # 3B, 59
        "Function_60_BA77",        # 3C, 60
        "Function_61_BABF",        # 3D, 61
        "Function_62_BB0C",        # 3E, 62
        "Function_63_BB59",        # 3F, 63
        "Function_64_BBA6",        # 40, 64
        "Function_65_BBAF",        # 41, 65
        "Function_66_C122",        # 42, 66
        "Function_67_C286",        # 43, 67
        "Function_68_C2D1",        # 44, 68
        "Function_69_C330",        # 45, 69
        "Function_70_C37B",        # 46, 70
        "Function_71_C3DA",        # 47, 71
        "Function_72_CB88",        # 48, 72
        "Function_73_CBD7",        # 49, 73
        "Function_74_CC2B",        # 4A, 74
        "Function_75_CC7F",        # 4B, 75
        "Function_76_CCD3",        # 4C, 76
        "Function_77_D492",        # 4D, 77
        "Function_78_D4E1",        # 4E, 78
        "Function_79_D535",        # 4F, 79
        "Function_80_D589",        # 50, 80
        "Function_81_D5DD",        # 51, 81
        "Function_82_D675",        # 52, 82
        "Function_83_D6CD",        # 53, 83
        "Function_84_D6D1",        # 54, 84
        "Function_85_D6D5",        # 55, 85
        "Function_86_D6D9",        # 56, 86
        "Function_87_D6DD",        # 57, 87
    )


    def Function_0_66E(): pass

    label("Function_0_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_72E")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x20, -1060, 0, 2530, 180)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x21, -1080, 0, 1310, 0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x15, -3670, 0, 33860, 90)
    SetChrPos(0x16, 2300, 0, 34190, 180)
    ClearChrFlags(0x16, 0x80)
    OP_43(0x16, 0x0, 0x6, 0x2)
    SetChrPos(0x18, 92160, 0, 34030, 0)
    SetChrPos(0x19, 92160, 0, 35490, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F")
    SetChrFlags(0x18, 0x10)
    Jump("loc_726")

    label("loc_71F")

    OP_8C(0x19, 0, 0)

    label("loc_726")

    SetChrFlags(0x19, 0x10)
    Jump("loc_C31")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_A47")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0xB, 114760, 0, 5010, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_79A")
    SetChrPos(0xA, 3470, 0, 2580, 180)
    SetChrPos(0x9, 3500, 0, 1470, 0)
    Jump("loc_7BC")

    label("loc_79A")

    SetChrPos(0xA, 3470, 0, 2580, 270)
    SetChrPos(0x9, 3500, 0, 1470, 270)

    label("loc_7BC")

    SetChrPos(0x20, -240, 0, 3050, 90)
    SetChrPos(0x12, -550, 0, 1740, 90)
    SetChrPos(0x21, 350, 0, 1140, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_43(0x12, 0x0, 0x6, 0x2)
    SetChrPos(0x14, 260, 0, 32820, 225)
    SetChrPos(0x1A, 170, 0, 30840, 0)
    SetChrPos(0x15, -1090, 0, 33310, 180)
    SetChrPos(0x1C, -1100, 0, 31200, 45)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x18, 92640, 0, 35500, 0)
    SetChrPos(0x17, 91490, 0, 35490, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x1D, 94990, 250, 35500, 233)
    SetChrPos(0x1E, 94520, 250, 33430, 270)
    Jump("loc_8D2")

    label("loc_8B0")

    SetChrPos(0x1D, 94550, 250, 34350, 180)
    SetChrPos(0x1E, 94520, 250, 33430, 0)

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 7)), scpexpr(EXPR_END)), "loc_930")
    SetChrPos(0x22, 42290, 0, 3240, 180)
    SetChrPos(0x23, 39710, 0, 1520, 180)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 13)
    Jump("loc_9E9")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 0)), scpexpr(EXPR_END)), "loc_98E")
    SetChrPos(0x22, 54400, 0, 970, 90)
    SetChrPos(0x23, 55400, 0, -1460, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 9)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)
    Jump("loc_9E9")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 1)), scpexpr(EXPR_END)), "loc_9E9")
    SetChrPos(0x22, 28800, 0, 700, 270)
    SetChrPos(0x23, 29240, 0, -1490, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)

    label("loc_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 7)), scpexpr(EXPR_END)), "loc_A44")
    SetChrPos(0x24, 39960, 0, 29850, 0)
    SetChrPos(0x25, 42350, 0, 29860, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x24, 0x1)
    SetChrFlags(0x24, 0x2)
    SetChrChipByIndex(0x24, 26)
    SetChrSubChip(0x24, 10)
    ClearChrFlags(0x25, 0x1)
    SetChrFlags(0x25, 0x2)
    SetChrChipByIndex(0x25, 26)
    SetChrSubChip(0x25, 13)

    label("loc_A44")

    Jump("loc_C31")

    label("loc_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_AF2")
    SetChrPos(0xD, 5370, 250, 33230, 90)
    SetChrPos(0xE, 84100, 0, 4951, 0)
    SetChrPos(0x14, -3980, 0, 35495, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrPos(0x13, 43530, 0, 1620, 270)
    OP_43(0x13, 0x0, 0x0, 0x2)
    SetChrPos(0x1A, 38230, 0, 1730, 180)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x19, 86480, 0, 28510, 270)
    SetChrPos(0x18, 85350, 0, 28510, 90)
    SetChrFlags(0x19, 0x10)
    Jump("loc_C31")

    label("loc_AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_AFC")
    Jump("loc_C31")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_BBA")
    SetChrPos(0x18, 88900, 0, 34610, 180)
    SetChrPos(0x19, 88910, 0, 33380, 0)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x18, 0x10)
    SetChrPos(0x17, 92170, 0, 30030, 270)
    SetChrPos(0x15, 42770, 0, 5270, 0)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, 84430, 200, 1120, 90)
    SetChrFlags(0xD, 0x10)
    OP_44(0xD, 0x0)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0xE, 84510, 200, 2890, 90)
    SetChrFlags(0xE, 0x10)
    OP_44(0xE, 0x0)
    SetChrChipByIndex(0xE, 9)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_C31")

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BD0")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_BD5")

    label("loc_BD0")

    ClearChrFlags(0x10, 0x80)

    label("loc_BD5")

    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x9, 82950, 0, 4700, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x6, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x6)
    OP_43(0x18, 0x0, 0x0, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C")
    SetChrFlags(0x17, 0x10)

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C")
    SetChrFlags(0x1B, 0x10)
    Jump("loc_C31")

    label("loc_C2C")

    SetChrFlags(0x1B, 0x80)

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_C47")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 34)
    Jump("loc_DB3")

    label("loc_C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_C5D")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_DB3")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_C73")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_DB3")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_C89")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 37)
    Jump("loc_DB3")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_C9F")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_DB3")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_CB5")
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_DB3")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_CCB")
    OP_A3(0x10F6)
    SetMapFlags(0x10000000)
    Event(0, 40)
    Jump("loc_DB3")

    label("loc_CCB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_CF3"),
        (103, "loc_D0B"),
        (106, "loc_D23"),
        (111, "loc_D3B"),
        (114, "loc_D53"),
        (116, "loc_D6B"),
        (123, "loc_D83"),
        (121, "loc_D9B"),
        (SWITCH_DEFAULT, "loc_DB3"),
    )


    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D08")
    SetMapFlags(0x10000000)
    Event(0, 47)

    label("loc_D08")

    Jump("loc_DB3")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D20")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_D20")

    Jump("loc_DB3")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    SetMapFlags(0x10000000)
    Event(0, 41)

    label("loc_D38")

    Jump("loc_DB3")

    label("loc_D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D50")
    SetMapFlags(0x10000000)
    Event(0, 59)

    label("loc_D50")

    Jump("loc_DB3")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D68")
    SetMapFlags(0x10000000)
    Event(0, 54)

    label("loc_D68")

    Jump("loc_DB3")

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D80")
    SetMapFlags(0x10000000)
    Event(0, 64)

    label("loc_D80")

    Jump("loc_DB3")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D98")
    SetMapFlags(0x10000000)
    Event(0, 71)

    label("loc_D98")

    Jump("loc_DB3")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB0")
    SetMapFlags(0x10000000)
    Event(0, 76)

    label("loc_DB0")

    Jump("loc_DB3")

    label("loc_DB3")

    Return()

    # Function_0_66E end

    def Function_1_DB4(): pass

    label("Function_1_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_DBE")
    Jump("loc_DF5")

    label("loc_DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_DCC")
    OP_64(0x0, 0x1)
    Jump("loc_DF5")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_DDA")
    OP_64(0x1, 0x1)
    Jump("loc_DF5")

    label("loc_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_DE4")
    Jump("loc_DF5")

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_DEE")
    Jump("loc_DF5")

    label("loc_DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_DF5")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E0D")
    OP_B1("t2510_y")
    Jump("loc_E16")

    label("loc_E0D")

    OP_B1("t2510_n")

    label("loc_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_E20")
    Jump("loc_E4D")

    label("loc_E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_E38")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_E4D")

    label("loc_E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_E4D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_E4D")

    Return()

    # Function_1_DB4 end

    def Function_2_E4E(): pass

    label("Function_2_E4E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E71")
    OP_8D(0xFE, 39890, 1860, 43300, -1658, 2000)
    Jump("Function_2_E4E")

    label("loc_E71")

    Return()

    # Function_2_E4E end

    def Function_3_E72(): pass

    label("Function_3_E72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E95")
    OP_8D(0xFE, 36600, 27090, 39800, 31770, 1500)
    Jump("Function_3_E72")

    label("loc_E95")

    Return()

    # Function_3_E72 end

    def Function_4_E96(): pass

    label("Function_4_E96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EB9")
    OP_8D(0xFE, 2080, 5500, 3800, -580, 2000)
    Jump("Function_4_E96")

    label("loc_EB9")

    Return()

    # Function_4_E96 end

    def Function_5_EBA(): pass

    label("Function_5_EBA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDD")
    OP_8D(0xFE, 28190, -1470, 31790, 1270, 1000)
    Jump("Function_5_EBA")

    label("loc_EDD")

    Return()

    # Function_5_EBA end

    def Function_6_EDE(): pass

    label("Function_6_EDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FB2")
    OP_8C(0xFE, 90, 400)

    label("loc_EEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F37")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F34")
    OP_63(0xFE)
    OP_8C(0xFE, 180, 400)
    Jump("loc_F37")

    label("loc_F34")

    Jump("loc_EEE")

    label("loc_F37")

    OP_8E(0xFE, 0x17458, 0xFA, 0x7814, 0x3E8, 0x0)
    OP_8C(0xFE, 90, 400)

    label("loc_F52")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F9B")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F98")
    OP_63(0xFE)
    OP_8C(0xFE, 0, 400)
    Jump("loc_F9B")

    label("loc_F98")

    Jump("loc_F52")

    label("loc_F9B")

    OP_8E(0xFE, 0x17458, 0xFA, 0x82C8, 0x3E8, 0x0)
    Jump("Function_6_EDE")

    label("loc_FB2")

    Return()

    # Function_6_EDE end

    def Function_7_FB3(): pass

    label("Function_7_FB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FD6")
    OP_8D(0xFE, 92190, 29990, 93420, 33800, 1000)
    Jump("Function_7_FB3")

    label("loc_FD6")

    Return()

    # Function_7_FB3 end

    def Function_8_FD7(): pass

    label("Function_8_FD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_100A")

    ChrTalk(    #0
        0xFE,
        "Ahhh, another dull day...\x02",
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_100A")

    OP_A2(0x12)

    ChrTalk(    #1
        0xFE,
        "Hey, did you find anything out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "All right! Food time.\x02",
    )

    CloseMessageWindow()

    label("loc_104D")

    Jump("loc_18C2")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_18C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_END)), "loc_1135")

    ChrTalk(    #3
        0xFE,
        (
            "I used to use the back of the schoolhouse\x01",
            "as a place to skip class, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Thinking about it, I guess that's exactly\x01",
            "where you'd expect to see ghosts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "D-Damn it! How am I supposed to\x01",
            "enjoy it now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C2")

    label("loc_1135")

    OP_A2(0x1233)
    OP_28(0x83, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -3000, 0, 4850, 270)
    SetChrPos(0x105, -2500, 0, 5500, 270)
    ClearChrFlags(0xFE, 0x10)
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x26, 0x0)
    OP_0D()

    ChrTalk(    #6
        0xFE,
        "*yaaaaaawn* Man, I'm hungry.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #7
        0xFE,
        "Huh? You want something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000FAh, yeah...\x02\x03",

            "Actually, we had a question.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #10
        0xFE,
        "Strange events...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1002FLike, did you see anything weird,\x01",
            "or hear any odd sounds?\x02\x03",

            "Anything you might have noticed\x01",
            "would be helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Odd sounds...?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0xFE,
        (
            "D-D-Don't make me remember\x01",
            "all that creepy stuff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#044F#6PDid you see something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Yeah... Haven't actually told anyone\x01",
            "before you guys, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I...saw someone suspicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1002FReally?!\x02\x03",

            "Could you give us the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "O-Okay, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I was hangin' out behind the\x01",
            "schoolhouse on my way back\x01",
            "home, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "It's a great place to chill during tests.\x01",
            "No one's ever there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "So, I was walking around near\x01",
            "the rear gate on my way back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "...when this white, floating person\x01",
            "suddenly flew past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I'm sure it looked like a person.\x01",
            "No way I could have seen it wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F(A white, human form? That matches\x01",
            "what the other witnesses have said.)\x02\x03",

            "#1002FSo, what happened after that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "He floated off towards the rear gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "After that, I didn't see him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1002FI see... So he disappeared towards\x01",
            "the rear gate.\x02\x03",

            "Yeah, this is good intel. I should write\x01",
            "this down in my notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        "#040F#6PI agree. This is valuable testimony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "...So, is that enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I'm starving and I wanna grab some food.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1004FHaha, sorry. You're all good.\x02\x03",

            "#1006FThanks for the help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Well, not sure what's going on,\x01",
            "but good luck or whatever.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1854():

        label("loc_1854")

        TurnDirection(0x101, 0x1B, 400)
        OP_48()
        Jump("loc_1854")

    QueueWorkItem2(0x101, 1, lambda_1854)

    def lambda_1865():

        label("loc_1865")

        TurnDirection(0x105, 0x1B, 400)
        OP_48()
        Jump("loc_1865")

    QueueWorkItem2(0x105, 1, lambda_1865)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFF01A, 0x0, 0x50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF380, 0x0, 0xFFFFFA6A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDB2, 0x0, 0xFFFFFA42, 0x7D0, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    SetChrFlags(0xFE, 0x80)
    EventEnd(0x0)

    label("loc_18C2")

    TalkEnd(0xFE)
    Return()

    # Function_8_FD7 end

    def Function_9_18C6(): pass

    label("Function_9_18C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_1922")

    ChrTalk(    #33
        0xFE,
        "Logic's totally freaked out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Heh heh heh... Seriously, how pathetic!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A25")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_199D")

    ChrTalk(    #35
        0xFE,
        (
            "Apparently, someone was hiding in\x01",
            "the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Maybe that's what caused this whole\x01",
            "ghost fuss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A25")

    label("loc_199D")

    OP_A2(0x11)

    ChrTalk(    #37
        0xFE,
        (
            "Apparently, someone was hiding in\x01",
            "the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Maybe that's what caused this whole\x01",
            "ghost fuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Hee hee hee...\x02",
    )

    CloseMessageWindow()

    label("loc_1A25")

    TalkEnd(0xFE)
    Return()

    # Function_9_18C6 end

    def Function_10_1A29(): pass

    label("Function_10_1A29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A42")
    Call(0, 12)
    Jump("loc_1AB9")

    label("loc_1A42")


    ChrTalk(    #40
        0xFE,
        "Why are boys SO STUPID?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "No thought at all to how much they\x01",
            "make other people worry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "*mutter* *mutter*\x02",
    )

    CloseMessageWindow()

    label("loc_1AB9")

    Jump("loc_1DB1")

    label("loc_1ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(    #43
        0xFE,
        "Why'd you say yes so easily?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "You can't take it back now,\x01",
            "so no point in getting scared\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC6")

    label("loc_1B3D")

    OP_A2(0x10)

    ChrTalk(    #45
        0xFE,
        (
            "A private tutor? And for the entrance\x01",
            "exams on top of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Are you really okay with accepting\x01",
            "that kind of responsibility?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC6")

    Jump("loc_1DB1")

    label("loc_1BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1C74")

    ChrTalk(    #47
        0xFE,
        (
            "The right answer's number one, isn't it?\x01",
            "Number three's a trick, come on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "If you're gonna mess up on something\x01",
            "this easy, you'll never beat me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD9")

    label("loc_1C74")

    OP_A2(0x10)

    ChrTalk(    #49
        0xFE,
        (
            "No, it's a trick question. It's obviously\x01",
            "the first one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Geez, use your brain a little!\x02",
    )

    CloseMessageWindow()

    label("loc_1CD9")

    Jump("loc_1DB1")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1DB1")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1D49")

    ChrTalk(    #51
        0xFE,
        "Nothing really happened during exams.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "Everyone was busy with studying, anyway.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB1")

    label("loc_1D49")

    OP_A2(0x10)

    ChrTalk(    #53
        0xFE,
        "Huh, do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Odd events, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "I don't think there was anything, no.\x02",
    )

    CloseMessageWindow()

    label("loc_1DB1")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A29 end

    def Function_11_1DB5(): pass

    label("Function_11_1DB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCE")
    Call(0, 12)
    Jump("loc_1E44")

    label("loc_1DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1E06")

    ChrTalk(    #56
        0xFE,
        "H-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Did I say something wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E44")

    label("loc_1E06")


    ChrTalk(    #58
        0xFE,
        "Why's Nikita so mad...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Hmm... I'm not really sure.\x02",
    )

    CloseMessageWindow()

    label("loc_1E44")

    Jump("loc_2189")

    label("loc_1E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_END)), "loc_1EBE")

    ChrTalk(    #60
        0xFE,
        (
            "It's hard just sitting here, but\x01",
            "we'll do what the pros say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "You go and rescue the other students.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2189")

    label("loc_1EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(    #62
        0xFE,
        (
            "Being a tutor's a big deal, especially\x01",
            "if it's for the entrance exams. If I screw\x01",
            "up, I screw him over too, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Yeah, it was easy enough to accept\x01",
            "at the time, but now I'm freaking out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2014")

    label("loc_1F99")

    OP_A2(0xE)

    ChrTalk(    #64
        0xFE,
        (
            "I got roped into tutoring my\x01",
            "neighbor over break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "It's for his entrance exams, too.\x01",
            "Man, the pressure's on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2014")

    Jump("loc_2189")

    label("loc_2017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_20BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2086")

    ChrTalk(    #66
        0xFE,
        (
            "I was feeling confident back when\x01",
            "I first agreed to be a tutor. Why am\x01",
            "I so nervous now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B9")

    label("loc_2086")

    OP_A2(0xE)

    ChrTalk(    #67
        0xFE,
        "Whaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "Wait, it isn't number three?\x02",
    )

    CloseMessageWindow()

    label("loc_20B9")

    Jump("loc_2189")

    label("loc_20BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_2189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2114")

    ChrTalk(    #69
        0xFE,
        "Strange events during exams?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Don't think there was anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2189")

    label("loc_2114")

    OP_A2(0xE)

    ChrTalk(    #71
        0xFE,
        "Hmm? You want something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "...Strange events during exam the period?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "No, I can't think of anything. \x02",
    )

    CloseMessageWindow()

    label("loc_2189")

    TalkEnd(0xFE)
    Return()

    # Function_11_1DB5 end

    def Function_12_218D(): pass

    label("Function_12_218D")

    OP_4A(0x18, 255)
    OP_4A(0x19, 255)

    ChrTalk(    #74
        0x18,
        "*sigh* It's weirdly tiring being a hostage.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x18,
        (
            "Maybe it's because I was so nervous,\x01",
            "but my shoulder's all tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x19,
        (
            "Well, that's no big deal in the long run,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x19,
        (
            "The two of us ended up safe,\x01",
            "and that's what matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x18,
        "True, but even so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x18,
        (
            "But I wish we could have helped\x01",
            "with the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x18,
        (
            "If we'd attacked all at once, we probably\x01",
            "could have gotten at least one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x19,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x18,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x18,
        "Nikita... What...?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #84
        0x19,
        (
            "#3SYou IDIOT! What the heck is that\x01",
            "mouth of yours spewing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #85
        0x18,
        "Wh-Whoa...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x19,
        "A janitor got SHOT, you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x19,
        (
            "If you know how dangerous things are,\x01",
            "why would you even bring up something\x01",
            "like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x18,
        "W-Well, yeah, I know. Still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x18,
        "H-Hey, Nikita. Why are you so angry?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x19, 0, 400)

    ChrTalk(    #90
        0x19,
        "Don't ask ME!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x19,
        "Why don't you think about it yourself?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_A2(0x20C4)
    ClearChrFlags(0x18, 0x10)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    Return()

    # Function_12_218D end

    def Function_13_24EE(): pass

    label("Function_13_24EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_END)), "loc_25D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2584")

    ChrTalk(    #92
        0xFE,
        "All I can say is that Mickey is one lucky guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "If he hadn't met you all, who knows\x01",
            "what would have happened to him.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_25D5")

    label("loc_2584")


    ChrTalk(    #94
        0xFE,
        "All I can say is that Mickey is one lucky guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "We owe him one, though.\x02",
    )

    CloseMessageWindow()

    label("loc_25D5")

    Jump("loc_317E")

    label("loc_25D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2791")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_26BF")

    ChrTalk(    #96
        0xFE,
        (
            "Oh, yeah. I heard you were taking vacation\x01",
            "early, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I'll be working on my swordsmanship\x01",
            "as best I can, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I hope that you're up for a\x01",
            "duel once vacation's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        "#040FSure. I'd like that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_278E")

    label("loc_26BF")

    OP_A2(0xD)

    ChrTalk(    #100
        0xFE,
        "I've heard rumors about the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "There was some suspicious person\x01",
            "in the old schoolhouse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Still, why the heck would anyone be\x01",
            "hiding out there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Totally bizarre, if you ask me.\x02",
    )

    CloseMessageWindow()

    label("loc_278E")

    Jump("loc_317E")

    label("loc_2791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_2852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_27ED")

    ChrTalk(    #104
        0xFE,
        "The sun's mostly gone down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Guess it's about time I headed home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_284F")

    label("loc_27ED")

    OP_A2(0xD)

    ChrTalk(    #106
        0xFE,
        "I've finally finished checking my test answers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "Don't think I did too bad, actually!\x02",
    )

    CloseMessageWindow()

    label("loc_284F")

    Jump("loc_317E")

    label("loc_2852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_317E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_28D7")

    ChrTalk(    #108
        0xFE,
        (
            "If there's anything else I can help\x01",
            "you with, just let me know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #109
        0xFE,
        "Well, see you later at club, Kloe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_317E")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 2)), scpexpr(EXPR_END)), "loc_299C")

    ChrTalk(    #110
        0xFE,
        (
            "I still haven't talked to anyone about\x01",
            "that white, humanoid shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Attempting to explain events based only on\x01",
            "supposition can hardly be called a scientific\x01",
            "attitude, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317E")

    label("loc_299C")

    OP_A2(0x1232)
    OP_28(0x83, 0x1, 0x8)
    OP_A2(0xD)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 46020, 0, 32509, 90)
    SetChrPos(0x105, 46140, 0, 33370, 90)
    ClearChrFlags(0xFE, 0x10)
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x26, 0x0)
    OP_0D()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(400)

    ChrTalk(    #112
        0xFE,
        "Oh, Kloe. How'd your tests go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x105,
        (
            "#045FOh, well enough, I guess.\x02\x03",

            "#040FMore importantly, Patrick, may we have a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Sure, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1015FErr, so actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #117
        0xFE,
        "Strange events, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I do have something that might be\x01",
            "along that line, sort of, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1011FIt's fine if you don't know the exact\x01",
            "details.\x02\x03",

            "Just tell us everything that happened\x01",
            "at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "All right.\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #121
        0xFE,
        "Well, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "I saw this humanoid form flying in the sky.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(20)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #123
        0x105,
        "#042F...Oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1002FCould you tell us everything you remember\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "Sure. It was on one of the exam nights.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I had stayed behind in the classroom\x01",
            "to study...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "I thought I noticed something move\x01",
            "outside the window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I thought, maybe the wind had picked up or\x01",
            "something, so I went to close the window...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "...when I saw this white, shadowy form\x01",
            "floating outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1015FA white, shadowy form...\x02\x03",

            "#1002FSo, what happened next?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Unfortunately, I lost sight of it immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "It sort of just disappeared towards the east.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        (
            "#042FEast would mean it disappeared towards\x01",
            "the back of the schoolhouse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1002FYeah...\x02\x03",

            "Still, you remembered a lot of details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Well, it was quite an interesting phenomenon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I wrote some simple notes down thinking\x01",
            "I'd research it later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1004FR-Research?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #138
        0x105,
        "#041FPatrick is a student of the sciences, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1001FAhaha, I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xFE, 400)

    ChrTalk(    #140
        0xFE,
        "Was I of any help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1000FYeah, definitely. That was valuable testimony.\x02\x03",

            "I'll get that down in my notebook right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x105,
        "#040FPatrick, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "Not at all. It was a minor request.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    EventEnd(0x0)

    label("loc_317E")

    TalkEnd(0xFE)
    Return()

    # Function_13_24EE end

    def Function_14_3182(): pass

    label("Function_14_3182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_33AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EE")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #144
        0xFE,
        "Hey, Estelle, Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Umm, thank you so much for saving us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1000FNo, we're just glad you're safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        "#1040FQuite the disaster, huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #148
        0xFE,
        "Seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "Still, to think that Kloe is actually\x01",
            "Princess Klaudia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I think that surprises me more than\x01",
            "the whole hostage thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x20C3)
    Jump("loc_33A8")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_33A8")

    ChrTalk(    #151
        0xFE,
        (
            "To think that Kloe is actually\x01",
            "Princess Klaudia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "We've been in the same club together\x01",
            "for AGES! How did I not notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "*siiigh* I guess I really am an airhead...\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()

    label("loc_33A8")

    Jump("loc_37D0")

    label("loc_33AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_34DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_343E")

    ChrTalk(    #154
        0xFE,
        (
            "I worked really hard this time to\x01",
            "get decent grades for a change!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Heehee. I know I won't match up to you,\x01",
            "though, Kloe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_343E")

    OP_A2(0xC)

    ChrTalk(    #156
        0xFE,
        "Exams are FINALLY over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I worked really hard this time to\x01",
            "get decent grades for a change!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #158
        0xFE,
        "I know I won't match up to Kloe, though.\x02",
    )

    CloseMessageWindow()

    label("loc_34DA")

    Jump("loc_37D0")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_37D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 6)), scpexpr(EXPR_END)), "loc_3551")

    ChrTalk(    #159
        0xFE,
        (
            "I don't think there was anything\x01",
            "out of the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Sorry I can't be of any use, Kloe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D0")

    label("loc_3551")

    OP_A2(0x1236)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x105, 0)
    Sleep(400)

    ChrTalk(    #161
        0xFE,
        "Huh? Did you forget something, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        (
            "#040FNo, I had some stuff I had to do, so\x01",
            "I was walking around the schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "Oh, what kind of stuff?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1015FSo actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #165
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #166
        0xFE,
        "Huh, strange events?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "Hmm... I don't think there was anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "Aww, I'm sorry. I'm of no help whatsoever...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1000FNo, don't let it bother you.\x02\x03",

            "Well, let's go check with other people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x105,
        "#040FThanks, Richelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #171
        0xFE,
        "No problem.\x02",
    )

    CloseMessageWindow()

    label("loc_37D0")

    TalkEnd(0xFE)
    Return()

    # Function_14_3182 end

    def Function_15_37D4(): pass

    label("Function_15_37D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3987")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E2")

    ChrTalk(    #172
        0xFE,
        (
            "The case is settled, but this is where\x01",
            "the real challenge starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "This is, after all, our first experience\x01",
            "with a life without orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "I'm sure it won't be easy, but we're\x01",
            "all just going to have to suck it up and\x01",
            "get used to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3984")

    label("loc_38E2")


    ChrTalk(    #175
        0xFE,
        (
            "This is my first time experiencing\x01",
            "life without orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I'm sure it won't be easy, but we're\x01",
            "all just going to have to suck it up and\x01",
            "get used to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3984")

    Jump("loc_3C1A")

    label("loc_3987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_39E9")

    ChrTalk(    #177
        0xFE,
        "I wonder if everyone else is safe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "You be careful too, Estelle. All of you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C1A")

    label("loc_39E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_3B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3A7E")

    ChrTalk(    #179
        0xFE,
        (
            "I was going to meet my uncle from the\x01",
            "capital who'd come to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "I'm worried if he'll be where he said\x01",
            "he would, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B49")

    label("loc_3A7E")

    OP_A2(0xB)

    ChrTalk(    #181
        0xFE,
        "My uncle's come to visit from the capital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "It's been a while, so I was going\x01",
            "to meet him in Ruan, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "My uncle is on the quirky side, though,\x01",
            "so I wonder if he'll actually BE there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B49")

    Jump("loc_3C1A")

    label("loc_3B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_3C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3BA0")

    ChrTalk(    #184
        0xFE,
        (
            "Nothing really happened during the exam\x01",
            "period that I recall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1A")

    label("loc_3BA0")

    OP_A2(0xB)

    ChrTalk(    #185
        0xFE,
        "Yes...? Odd events...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "No, sorry. Nothing weird happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "You might have better luck with\x01",
            "someone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1A")

    TalkEnd(0xFE)
    Return()

    # Function_15_37D4 end

    def Function_16_3C1E(): pass

    label("Function_16_3C1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5F")

    ChrTalk(    #188
        0xFE,
        "Oh! Sup, bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "Nice work with that case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "I can hardly even find words to thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1001FNo, no, you're welcome.\x02\x03",

            "#1011FSo, how about it? Feeling a bit better?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #192
        0xFE,
        "Ha...haha, o-of course...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "Calm and controlled is my motto.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1028FI...see.\x02\x03",

            "#1015F#1SYou sure seemed pretty scared...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #195
        0xFE,
        "Ghkt...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#1035F(Estelle, don't poke the sensitive\x01",
            "bits more than you need to.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#1008F(...Oops. Duly noted.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "A-Anyway, I'm glad everyone is safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "Okay, i-i-if you'll excuse me...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20C2)
    Jump("loc_3EC8")

    label("loc_3E5F")


    ChrTalk(    #200
        0xFE,
        (
            "Wh-When it all went down I was just, uh,\x01",
            "simply overly protective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "I-I swear, I wasn't scared!\x02",
    )

    CloseMessageWindow()

    label("loc_3EC8")

    Jump("loc_4612")

    label("loc_3ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_3F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F44")

    ChrTalk(    #202
        0xFE,
        "W-We'll be on standby here as ordered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "So come rescue us as s-s-soon as possible,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_3F93")

    label("loc_3F44")


    ChrTalk(    #204
        0xFE,
        (
            "Come rescue us as soon as possible,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "W-We're counting on you!\x02",
    )

    CloseMessageWindow()

    label("loc_3F93")

    Jump("loc_4612")

    label("loc_3F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3FF3")

    ChrTalk(    #206
        0xFE,
        "Well, time to get to club.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "I'm sure everyone's getting impatient.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4143")

    label("loc_3FF3")

    TurnDirection(0xFE, 0x105, 0)
    OP_A2(0xA)

    ChrTalk(    #208
        0xFE,
        (
            "Heard you'll be heading off on vacation\x01",
            "early, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x105,
        (
            "#040FYes, I thought about it a bit,\x01",
            "and that's what I decided.\x02\x03",

            "I'll see you all next after vacation ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I pray that we'll meet again\x01",
            "in good health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "I intend to go off and help with\x01",
            "the election myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "All right, see you when school's back on.\x02",
    )

    CloseMessageWindow()

    label("loc_4143")

    Jump("loc_4612")

    label("loc_4146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_4393")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_41FF")

    ChrTalk(    #213
        0xFE,
        (
            "From my perspective, both candidates'\x01",
            "political plans have their issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "When you start comparing the details,\x01",
            "though, Norman has a slight advantage\x01",
            "overall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4390")

    label("loc_41FF")

    OP_A2(0xA)

    ChrTalk(    #215
        0xFE,
        (
            "Everyone in Ruan can't stop talking about\x01",
            "the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "However, if you were to ask me,\x01",
            "both candidates have some holes\x01",
            "in their political plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "Norman's camp has little idea what to do with\x01",
            "the harbor, and my dad, Portos, hasn't been\x01",
            "giving enough thought to the the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "I've been trying to point it out to Dad\x01",
            "a number of times, but...he's as stubborn\x01",
            "as ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4390")

    Jump("loc_4612")

    label("loc_4393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x247, 0)), scpexpr(EXPR_END)), "loc_4405")

    ChrTalk(    #219
        0xFE,
        "As far as I'm aware, nothing strange happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "You should probably ask other students.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4612")

    label("loc_4405")

    OP_A2(0x1238)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #221
        0xFE,
        "Hello, Kloe. Do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x105,
        "#040FActually, yes. We'd like to ask you a question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "Oh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1002FEr, so...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #225
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #226
        0xFE,
        "Strange events...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "No, there wasn't anything in particular.\x01",
            "Sorry I couldn't be of more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1000FNah, no worries.\x02\x03",

            "Well, thanks for your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "If anything else comes up,\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4612")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C1E end

    def Function_17_4616(): pass

    label("Function_17_4616")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4672")

    ChrTalk(    #230
        0xFE,
        "Logic sure is late...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "Maybe I should go on ahead to practice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4702")

    label("loc_4672")

    OP_A2(0x9)

    ChrTalk(    #232
        0xFE,
        "I've got music practice soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "It's almost time to meet up, but\x01",
            "some people haven't come yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "Even Argyle's made it on time...\x02",
    )

    CloseMessageWindow()

    label("loc_4702")

    Jump("loc_4936")

    label("loc_4705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_483F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_47A5")

    ChrTalk(    #235
        0xFE,
        (
            "We'll be busy with club activities\x01",
            "again starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "I should at least head home early on\x01",
            "days I've got nothing better to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483C")

    label("loc_47A5")

    OP_A2(0x9)

    ChrTalk(    #237
        0xFE,
        "Wow, is it already this late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "I'll be busy with the Music Club again\x01",
            "starting tomorrow, so I should probably\x01",
            "head home early for the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_483C")

    Jump("loc_4936")

    label("loc_483F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4936")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_48B7")

    ChrTalk(    #239
        0xFE,
        "It was no different than any other exam period.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "I was busy from morning till night studying.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4936")

    label("loc_48B7")

    OP_A2(0x9)

    ChrTalk(    #241
        0xFE,
        "Strange events?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "It was no different than any other\x01",
            "exam period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "I was busy from morning till night studying.\x02",
    )

    CloseMessageWindow()

    label("loc_4936")

    TalkEnd(0xFE)
    Return()

    # Function_17_4616 end

    def Function_18_493A(): pass

    label("Function_18_493A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_49ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AD")

    ChrTalk(    #244
        0xFE,
        "T-Take care of everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "I-I'm a little scared, but I'll hang in\x01",
            "there and wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_49EA")

    label("loc_49AD")


    ChrTalk(    #246
        0xFE,
        (
            "I-I'm a little scared, but I'll hang in\x01",
            "there and wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49EA")

    Jump("loc_4C8F")

    label("loc_49ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4ADB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4A5E")

    ChrTalk(    #247
        0xFE,
        (
            "Awww, before vacation we get our\x01",
            "tests back, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "I don't think I wanna see mine...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AD8")

    label("loc_4A5E")

    OP_A2(0x8)

    ChrTalk(    #249
        0xFE,
        "Ahaha, classes end today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "Thinking that we'll be on vacation soon\x01",
            "means we can take it easy on the studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD8")

    Jump("loc_4C8F")

    label("loc_4ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_4B31")

    ChrTalk(    #251
        0xFE,
        "Okay, what shall I do today...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "Maybe I should revamp my decor...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C8F")

    label("loc_4B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4BD5")

    ChrTalk(    #253
        0xFE,
        (
            "Only gotta wait a liiittle longer until\x01",
            "vacation starts. Exams can't end soon\x01",
            "enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "My mom and I are gonna\x01",
            "go shopping in the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C8F")

    label("loc_4BD5")

    OP_A2(0x8)

    ChrTalk(    #255
        0xFE,
        "Strange events during the exam period?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "Sorry, weird stuff's not on my radar.\x01",
            "I've only got my eye on cute stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "So I don't remember seeing anything\x01",
            "weird. Nope, nope!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8F")

    TalkEnd(0xFE)
    Return()

    # Function_18_493A end

    def Function_19_4C93(): pass

    label("Function_19_4C93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_4D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4D2A")

    ChrTalk(    #258
        0xFE,
        "The school festival was so fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "Well, guess I'll fill that hole in my life\x01",
            "with club activities until the next festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D91")

    label("loc_4D2A")

    OP_A2(0x7)

    ChrTalk(    #260
        0xFE,
        "The school festival was so fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "I wonder when our next chance to\x01",
            "party like that will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D91")

    Jump("loc_4E8D")

    label("loc_4D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4E0B")

    ChrTalk(    #262
        0xFE,
        "Finally... Finally exams are ooooover!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "P-Please, Aidios, grant me at least\x01",
            "a passing grade!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8D")

    label("loc_4E0B")

    OP_A2(0x7)

    ChrTalk(    #264
        0xFE,
        "Fiiiiiinally. Finally exams are over!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        "Huh...? What? Strange events during exams?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "No, don't remember anything...\x02",
    )

    CloseMessageWindow()

    label("loc_4E8D")

    TalkEnd(0xFE)
    Return()

    # Function_19_4C93 end

    def Function_20_4E91(): pass

    label("Function_20_4E91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_4FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F53")

    ChrTalk(    #267
        0x9,
        (
            "#640FIt's okay, I understand.\x02\x03",

            "I'm not going to run around like an\x01",
            "idiot and make things harder on you.\x02\x03",

            "#648FYou go show those criminals the right\x01",
            "hook of justice!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_4FAF")

    label("loc_4F53")


    ChrTalk(    #268
        0x9,
        (
            "#645FI-I told you, I'm fine.\x02\x03",

            "Even I wouldn't try something\x01",
            "crazy at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAF")

    Jump("loc_5174")

    label("loc_4FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_50F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5032")

    ChrTalk(    #269
        0xFE,
        (
            "#642FStill, though...\x02\x03",

            "Scherazard's got a rockin' bod.\x02\x03",

            "#645F*siiigh* I wish I had that much to show off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50F2")

    label("loc_5032")


    ChrTalk(    #270
        0xFE,
        (
            "#642FStill, though...\x02\x03",

            "Agate sure is strong, isn't he?\x02\x03",

            "#647FLithe, handsome young men are nice and all,\x01",
            "but the muscles of a real man are... Mmmmm...\x02\x03",

            "The world of beauty truly is deep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50F2")

    Jump("loc_5174")

    label("loc_50F5")

    OP_A2(0x5)

    ChrTalk(    #271
        0xFE,
        (
            "#640FOh, hello, you two.\x01",
            "How goes the investigation?\x02\x03",

            "#648FWe'll handle this part, so we'll\x01",
            "leave the students to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5174")

    TalkEnd(0xFE)
    Return()

    # Function_20_4E91 end

    def Function_21_5178(): pass

    label("Function_21_5178")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_51E6")

    ChrTalk(    #272
        0xFE,
        (
            "#050FHave you heard any kinda rumors\x01",
            "like that from people?\x02\x03",

            "Any little details could help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5246")

    label("loc_51E6")

    OP_A2(0x4)

    ChrTalk(    #273
        0xFE,
        (
            "#050FDid anything weird happen?\x02\x03",

            "Anything you noticed that struck you,\x01",
            "anything at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5246")

    TalkEnd(0xFE)
    Return()

    # Function_21_5178 end

    def Function_22_524A(): pass

    label("Function_22_524A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_52B5")

    ChrTalk(    #274
        0xFE,
        (
            "#020FHave you heard any rumors like that?\x02\x03",

            "Even the most minor thing could be important.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5317")

    label("loc_52B5")

    OP_A2(0x4)

    ChrTalk(    #275
        0xFE,
        (
            "#020FDid anything strange happen?\x02\x03",

            "Anything you noticed that struck you,\x01",
            "anything at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5317")

    TalkEnd(0xFE)
    Return()

    # Function_22_524A end

    def Function_23_531B(): pass

    label("Function_23_531B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_5421")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5385")

    ChrTalk(    #276
        0xFE,
        "Our class did pretty well this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        "That surprise test sure did the trick!\x02",
    )

    CloseMessageWindow()
    Jump("loc_541E")

    label("loc_5385")

    OP_A2(0x3)

    ChrTalk(    #278
        0xFE,
        "All right, grading is finally complete.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "Our class did pretty well this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "Just a tiiiny more to go until we can beat\x01",
            "Wiola's class.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_541E")

    Jump("loc_56BB")

    label("loc_5421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_55F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_54FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_54B1")

    ChrTalk(    #281
        0xFE,
        (
            "Well, I suppose it isn't really the time\x01",
            "to be focusing on that, is it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "I should be getting to work, WORK.\x02",
    )

    CloseMessageWindow()
    Jump("loc_54F9")

    label("loc_54B1")


    ChrTalk(    #283
        0xFE,
        "For now, men don't matter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "I should be getting to work, WORK.\x02",
    )

    CloseMessageWindow()

    label("loc_54F9")

    Jump("loc_55F0")

    label("loc_54FC")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5576")

    ChrTalk(    #285
        0xFE,
        (
            "That bracer has quite\x01",
            "an amazing figure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "What's she's trying to pull,\x01",
            "showing all that off, hmm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55F0")

    label("loc_5576")


    ChrTalk(    #287
        0xFE,
        (
            "That bracer who came by...\x01",
            "What a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "Those violet eyes, those sculpted biceps...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "How very...distracting.\x02",
    )

    CloseMessageWindow()

    label("loc_55F0")

    Jump("loc_56BB")

    label("loc_55F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_56BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5677")

    ChrTalk(    #290
        0xFE,
        (
            "I haven't heard any rumors like\x01",
            "that from the students, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "Maybe you could try asking someone else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_56BB")

    label("loc_5677")

    OP_A2(0x3)

    ChrTalk(    #292
        0xFE,
        "Huh? Strange events?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "Sorry, but there wasn't anything.\x02",
    )

    CloseMessageWindow()

    label("loc_56BB")

    TalkEnd(0xFE)
    Return()

    # Function_23_531B end

    def Function_24_56BF(): pass

    label("Function_24_56BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_59F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598D")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #294
        0xFE,
        "Estelle, Joshua. You did most amazingly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "Of course, that's no surprise.\x01",
            "You WERE my students!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        (
            "#1040FYou took very good care of us during\x01",
            "our stay at the academy.\x02\x03",

            "I still remember your classes very well\x01",
            "even now.\x02\x03",

            "Even Estelle was motivated for once.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #297
        0x101,
        (
            "#1004FUh...\x02\x03",

            "#1016F...Ah, y-yeah! I was! I totally was!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)
    Sleep(400)

    ChrTalk(    #298
        0x102,
        (
            "#1048F(You...can't remember anything,\x01",
            "can you?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #299
        0x101,
        (
            "#1008F(N-No! I just blanked, that's all.)\x02\x03",

            "(D-Don't bring up such an old topic\x01",
            "out of nowhere, okay?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "Oh, what are you whispering about?\x01",
            "Let your teacher hear, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #301
        0x101,
        "#1016FAhaha... N-Nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        "#1052F(Oh, boy...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20C8)
    Jump("loc_59F5")

    label("loc_598D")


    ChrTalk(    #303
        0xFE,
        "Estelle, Joshua. You did most amazingly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "Of course, that's no surprise.\x01",
            "You WERE my students!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59F5")

    Jump("loc_5F67")

    label("loc_59F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_5B96")
    TurnDirection(0xFE, 0x105, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5A98")

    ChrTalk(    #305
        0xFE,
        (
            "Make sure to come back bright and\x01",
            "cheery again once vacation is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Well, then, I pray you spend\x01",
            "your vacation effectively.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B93")

    label("loc_5A98")

    OP_A2(0x2)

    ChrTalk(    #307
        0xFE,
        "Ah, Kloe. I thought you left ages ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "Make sure to come back bright and\x01",
            "cheery again once vacation is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "Understood? Promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x105,
        (
            "#040FYes, I promise.\x02\x03",

            "You take care too, Ms. Wiola.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        "Yes, do spend your vacation effectively.\x02",
    )

    CloseMessageWindow()

    label("loc_5B93")

    Jump("loc_5F67")

    label("loc_5B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_5CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5C46")

    ChrTalk(    #312
        0xFE,
        (
            "Exams are just as much a trial for\x01",
            "teachers as they are students.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "Those taking them and those executing\x01",
            "them both end up deprived of precious\x01",
            "sleep.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB9")

    label("loc_5C46")

    OP_A2(0x2)

    ChrTalk(    #314
        0xFE,
        (
            "Ooh... It's so late, but I'm still not done\x01",
            "grading...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        "I just want to finish this and go get a drink!\x02",
    )

    CloseMessageWindow()

    label("loc_5CB9")

    Jump("loc_5F67")

    label("loc_5CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_5F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5D32")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #316
        0xFE,
        "It's good to be social once in a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        "Good luck. Your teacher's cheering for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F67")

    label("loc_5D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 7)), scpexpr(EXPR_END)), "loc_5DB9")

    ChrTalk(    #318
        0xFE,
        (
            "Nooow, then, once I take a short breather\x01",
            "I'd best be back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        "*siiigh* Why is grading such a depressing job?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F67")

    label("loc_5DB9")

    OP_A2(0x2)
    OP_A2(0x1237)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #320
        0xFE,
        "Oh, Kloe. Did you have a question?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x105,
        "#040FNo, actually...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #322
        0xFE,
        (
            "Ah, is it about that thing Jill mentioned\x01",
            "a bit ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "Something about searching for people\x01",
            "who saw something suspicious or...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x105,
        "#040FYes, I'm assisting in the investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "It's good to go out and be social once\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "Good luck. Your teacher's cheering for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x105,
        "#041FYes, thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_5F67")

    TalkEnd(0xFE)
    Return()

    # Function_24_56BF end

    def Function_25_5F6B(): pass

    label("Function_25_5F6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6003")

    ChrTalk(    #328
        0xFE,
        "The janitor's condition has stabilized.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        "I'm really glad it was nothing serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "Perhaps I'll go visit him later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_605D")

    label("loc_6003")


    ChrTalk(    #331
        0xFE,
        "The janitor's condition has stabilized.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "I'm really glad it was nothing serious.\x02",
    )

    CloseMessageWindow()

    label("loc_605D")

    Jump("loc_62F1")

    label("loc_6060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_6109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_60A3")

    ChrTalk(    #333
        0xFE,
        "The overall state of the exams is very good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6106")

    label("loc_60A3")

    OP_A2(0x1)

    ChrTalk(    #334
        0xFE,
        "The overall state of the exams is very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        "The students must have worked very hard.\x02",
    )

    CloseMessageWindow()

    label("loc_6106")

    Jump("loc_62F1")

    label("loc_6109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_6209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6189")

    ChrTalk(    #336
        0xFE,
        "Mickey is actually a very intelligent student.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "His only real barrier is his nihilistic\x01",
            "view of life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6206")

    label("loc_6189")

    OP_A2(0x1)

    ChrTalk(    #338
        0xFE,
        (
            "Oh...? This exam paper doesn't seem\x01",
            "to have a name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "Let's see, seat number... Ah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        "...Seems to be Mickey's.\x02",
    )

    CloseMessageWindow()

    label("loc_6206")

    Jump("loc_62F1")

    label("loc_6209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_62F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_627B")

    ChrTalk(    #341
        0xFE,
        (
            "The students are acquitted of everything\x01",
            "once exams end, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        "How I envy them...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62F1")

    label("loc_627B")

    OP_A2(0x1)

    ChrTalk(    #343
        0xFE,
        (
            "I still have a tremendous stack of\x01",
            "exam papers I haven't looked at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        "I hope I can finish grading today...\x02",
    )

    CloseMessageWindow()

    label("loc_62F1")

    TalkEnd(0xFE)
    Return()

    # Function_25_5F6B end

    def Function_26_62F5(): pass

    label("Function_26_62F5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BC")

    ChrTalk(    #345
        0xB,
        (
            "The students have all already moved on,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xB,
        (
            "They've totally forgotten the tremendous\x01",
            "events that just happened here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xB,
        "Truly, the young are very resilient.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6413")

    label("loc_63BC")


    ChrTalk(    #348
        0xB,
        "The students have completely recovered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xB,
        "Truly, the young are very resilient.\x02",
    )

    CloseMessageWindow()

    label("loc_6413")

    Jump("loc_6682")

    label("loc_6416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_END)), "loc_6478")

    ChrTalk(    #350
        0xB,
        (
            "There should be armed criminals\x01",
            "all over the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xB,
        "Everyone, be careful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6682")

    label("loc_6478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_6566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_64E7")

    ChrTalk(    #352
        0xB,
        "The dean left a while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xB,
        (
            "He said something about business\x01",
            "he needed to attend to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6563")

    label("loc_64E7")

    OP_A2(0x0)

    ChrTalk(    #354
        0xB,
        (
            "Hello there, Kloe. I believe you're already\x01",
            "going off on vacation, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xB,
        "Take care, and do enjoy your time off.\x02",
    )

    CloseMessageWindow()

    label("loc_6563")

    Jump("loc_6682")

    label("loc_6566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_657D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6577")
    Jump("loc_657A")

    label("loc_6577")

    OP_A2(0x0)

    label("loc_657A")

    Jump("loc_6682")

    label("loc_657D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_65B3")

    ChrTalk(    #356
        0xB,
        "Good work. How goes the investigation?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6682")

    label("loc_65B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_6682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_660F")

    ChrTalk(    #357
        0xB,
        (
            "I have already been informed of your task.\x01",
            "Please investigate freely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6682")

    label("loc_660F")

    OP_A2(0x0)

    ChrTalk(    #358
        0xB,
        "Oh! You're bracers, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xB,
        (
            "I have already been informed of your task.\x01",
            "Please investigate freely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6682")

    TalkEnd(0xB)
    Return()

    # Function_26_62F5 end

    def Function_27_6686(): pass

    label("Function_27_6686")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B6")
    SetChrSubChip(0x8, 1)
    Jump("loc_66DC")

    label("loc_66B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66D7")
    SetChrSubChip(0x8, 2)
    Jump("loc_66DC")

    label("loc_66D7")

    SetChrSubChip(0x8, 0)

    label("loc_66DC")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5F")

    ChrTalk(    #360
        0x8,
        (
            "#783FEstelle, Joshua, you've done exceedingly\x01",
            "well.\x02\x03",

            "#780FThanks to you, we were able to rescue\x01",
            "all our precious students.\x02\x03",

            "As a representative of the academy,\x01",
            "allow me to offer my most sincere thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1025FI'm just relieved we were able to sort\x01",
            "everything out without things going from\x01",
            "bad to worse.\x02\x03",

            "I never dreamed the academy might\x01",
            "get attacked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x102,
        (
            "#1043FYes... We may have been a bit\x01",
            "naive in our judgments.\x02\x03",

            "#1035FThere really isn't anywhere safe\x01",
            "in the current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x8,
        (
            "#782FThis society you're after...\x02\x03",

            "They seem to be the unknown\x01",
            "masterminds behind this case.\x02\x03",

            "If not for you bracers, we would\x01",
            "have been unable to overcome this\x01",
            "danger.\x02\x03",

            "I hope you will continue your efforts\x01",
            "to restore order as soon as possible.\x02\x03",

            "For the sake of Kloe, too, who strives\x01",
            "alone in the capital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x101,
        "#1006FYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x102,
        "#1040FWe'll do whatever we can.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20F3)
    Jump("loc_6B4C")

    label("loc_6A5F")


    ChrTalk(    #366
        0x8,
        (
            "#780FIt seems those behind this case are truly\x01",
            "something we do not comprehend.\x02\x03",

            "I hope you bracers will continue to\x01",
            "lend us your aid.\x02\x03",

            "So we may restore order as soon as\x01",
            "possible... I'm sure Kloe in the capital\x01",
            "wishes for that too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4C")

    Jump("loc_6FF4")

    label("loc_6B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_END)), "loc_6CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C40")

    ChrTalk(    #367
        0x8,
        (
            "#780FThe criminal is searching for the royal\x01",
            "princess but hasn't realized Kloe is in\x01",
            "the capital.\x02\x03",

            "In which case, it's conceivable that the\x01",
            "other female students are at risk.\x02\x03",

            "Please do your best to keep them safe.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_6CCF")

    label("loc_6C40")


    ChrTalk(    #368
        0x8,
        (
            "#780FThe criminal is searching for the royal\x01",
            "princess but hasn't realized Kloe is in\x01",
            "the capital.\x02\x03",

            "Please do your best to keep them safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CCF")

    Jump("loc_6FF4")

    label("loc_6CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_6E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6D5C")

    ChrTalk(    #369
        0x8,
        (
            "#780FYou should return to the Student\x01",
            "Council room soon.\x02\x03",

            "It would be inconvenient after the sun\x01",
            "is set, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E51")

    label("loc_6D5C")

    OP_A2(0x6)

    ChrTalk(    #370
        0x8,
        (
            "#780FHas there been any progress in\x01",
            "your investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x105,
        (
            "#040FYeah, we were just about to go back\x01",
            "to the Student Council room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x8,
        (
            "#780FAll right, you should hurry.\x02\x03",

            "It would be difficult to investigate once\x01",
            "the sun sets, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E51")

    Jump("loc_6FF4")

    label("loc_6E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_6FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 4)), scpexpr(EXPR_END)), "loc_6EC8")

    ChrTalk(    #373
        0x8,
        (
            "#780FShould you need anything,\x01",
            "don't hesitate to ask.\x02\x03",

            "I won't hold back any aid I can offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FF4")

    label("loc_6EC8")

    OP_A2(0x1264)

    ChrTalk(    #374
        0x8,
        (
            "#780FYou've begun your investigation,\x01",
            "have you?\x02\x03",

            "And I see that Kloe is helping, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x105,
        (
            "#040FYes. This case relates to our academy, so...\x02\x03",

            "As a student here, I'd like to help\x01",
            "however I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x8,
        (
            "#780FShould you need anything,\x01",
            "don't hesitate to ask.\x02\x03",

            "I won't hold back any aid I can offer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF4")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_27_6686 end

    def Function_28_6FFD(): pass

    label("Function_28_6FFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_709C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7083")

    ChrTalk(    #377
        0xFE,
        "If I'd taken archery, I'd fight too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "Guess I'll have to leave it to the pros!\x01",
            "Good luck, bracers!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_709C")

    label("loc_7083")


    ChrTalk(    #379
        0xFE,
        "Good luck, bracers!\x02",
    )

    CloseMessageWindow()

    label("loc_709C")

    TalkEnd(0xFE)
    Return()

    # Function_28_6FFD end

    def Function_29_70A0(): pass

    label("Function_29_70A0")

    TalkBegin(0xFE)

    ChrTalk(    #380
        0xFE,
        (
            "Mickey's ultimately just talking\x01",
            "from a results perspective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "H-Hmph... I'm not saying thanks,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_70A0 end

    def Function_30_7119(): pass

    label("Function_30_7119")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71FD")

    ChrTalk(    #382
        0xFE,
        (
            "It is my duty to confirm the\x01",
            "mistress' safety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "However, what matters most now\x01",
            "is freeing the academy as a whole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        "I will leave this matter to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        "...Please take care of the other students.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_7272")

    label("loc_71FD")


    ChrTalk(    #386
        0xFE,
        (
            "Right now, what matters most is\x01",
            "freeing the academy as a whole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        "...Please take care of the other students.\x02",
    )

    CloseMessageWindow()

    label("loc_7272")

    TalkEnd(0xFE)
    Return()

    # Function_30_7119 end

    def Function_31_7276(): pass

    label("Function_31_7276")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_72D8")

    ChrTalk(    #388
        0xA,
        (
            "#732FOkay, come on back once you've\x01",
            "settled things.\x02\x03",

            "Estelle, Joshua...be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72D8")

    TalkEnd(0xFE)
    Return()

    # Function_31_7276 end

    def Function_32_72DC(): pass

    label("Function_32_72DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_73FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_739D")

    ChrTalk(    #389
        0xFE,
        "Thanks for what you guys did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        "I'm so glad things were settled safely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "Now's where things get hard, but I'm sure\x01",
            "we can handle it if we all work together.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_73FB")

    label("loc_739D")


    ChrTalk(    #392
        0xFE,
        "Hey, it's the bracers! Thank you for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        "I'm so glad things were settled safely.\x02",
    )

    CloseMessageWindow()

    label("loc_73FB")

    Jump("loc_7469")

    label("loc_73FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_7469")

    ChrTalk(    #394
        0xFE,
        "*sigh* Seriously, give me a break...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xFE,
        (
            "Why did I have to be treated so\x01",
            "horribly by them...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7469")

    TalkEnd(0xFE)
    Return()

    # Function_32_72DC end

    def Function_33_746D(): pass

    label("Function_33_746D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_761D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A0")

    ChrTalk(    #396
        0xFE,
        "Estelle, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "Here. It's not much, but it's\x01",
            "the least thanks I can offer.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #398
        "\x07\x00Received #581i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x245, 1)
    OP_A2(0x10C0)
    OP_0D()

    ChrTalk(    #399
        0xFE,
        (
            "Someday, I'd like to turn this case\x01",
            "into a novel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "Of course, that's once we go back\x01",
            "to normal life, if we do...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761A")

    label("loc_75A0")


    ChrTalk(    #401
        0xFE,
        (
            "Someday, I'd like to turn this case\x01",
            "into a novel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xFE,
        (
            "Of course, that's once we go back\x01",
            "to normal life, if we do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761A")

    Jump("loc_7691")

    label("loc_761D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_7691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7670")

    ChrTalk(    #403
        0xFE,
        "I'll be waiting right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xFE,
        "Everyone, be careful...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    Jump("loc_7691")

    label("loc_7670")


    ChrTalk(    #405
        0xFE,
        "I'll be waiting right here.\x02",
    )

    CloseMessageWindow()

    label("loc_7691")

    TalkEnd(0xFE)
    Return()

    # Function_33_746D end

    def Function_34_7695(): pass

    label("Function_34_7695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76A6")
    Call(0, 81)

    label("loc_76A6")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x101, 116390, 0, 2740, 0)
    SetChrPos(0xF7, 115500, 0, 2730, 0)
    SetChrPos(0x105, 117550, 0, 3240, 270)
    SetChrPos(0x104, 116430, 0, 1630, 0)
    SetChrPos(0x127, 115580, 0, 1650, 0)
    SetChrPos(0x9, 117660, 0, 4320, 270)
    SetChrPos(0xA, 118370, 0, 3940, 270)
    OP_6D(116710, 0, 460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(116480, 0, 3910, 2000)
    OP_0D()

    ChrTalk(    #406
        0x8,
        (
            "#783F#6PYes... I see.\x02\x03",

            "#780FSo you suspect this 'white shadow' is\x01",
            "originating from the academy grounds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        "#1002F#4PYes, sir, it seems like it is.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_78CA")

    ChrTalk(    #408
        0x106,
        (
            "#050F#1PSo, the guild'd like permission to\x01",
            "investigate inside the academy.\x02\x03",

            "You cool if we have a look around and\x01",
            "ask the students some questions?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7973")

    label("loc_78CA")


    ChrTalk(    #409
        0x103,
        (
            "#020F#1PThe guild would like permission to\x01",
            "investigate the academy grounds, sir.\x02\x03",

            "May we have permission to check\x01",
            "the campus thoroughly and interview\x01",
            "the students?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7973")


    ChrTalk(    #410
        0x8,
        (
            "#782F#6PCertainly. Given the circumstances,\x01",
            "I would ASK you to investigate, in truth.\x02\x03",

            "While I've little idea what this\x01",
            "'white shadow' could be...\x02\x03",

            "If it is affecting the election,\x01",
            "we cannot simply sit idle and\x01",
            "let it be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        (
            "#1016F#4PThanks, sir!\x02\x03",

            "#1015FSo, um, you mentioned not knowing\x01",
            "what the white shadow might be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x8,
        (
            "#780F#6PAlas, no. No one's reported anything\x01",
            "of the sort to me.\x02\x03",

            "Jill, has anyone come to the Student\x01",
            "Council about such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x9,
        (
            "#645F#4PMmmph... No, not a peep.\x02\x03",

            "#640FIt was exam crunch time, though.\x02\x03",

            "Nobody really had time to come\x01",
            "say so much as 'hi' to us anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x8,
        "#782F#6PI see... That would make sense.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)

    def lambda_7C0C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7C0C)
    Sleep(50)

    def lambda_7C1F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C1F)
    Sleep(50)

    def lambda_7C32():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_7C32)

    ChrTalk(    #415
        0x101,
        "#1004F#6PHuh? Uh, I think I'm lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x105,
        (
            "#542F#4PHere at the royal academy, there\x01",
            "are periodic exams which determine\x01",
            "if you proceed to the next grade.\x02\x03",

            "Even if the students saw something,\x01",
            "they might just choose to ignore it\x01",
            "and focus on studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xA,
        (
            "#734F#4PI have to admit, I'd probably be one of them.\x02\x03",

            "I know I'd rather get one more formula in my head\x01",
            "than focus on something that might just be my\x01",
            "sleep-deprived mind playing tricks on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        (
            "#1007F#6PWhoa... Are the exams really\x01",
            "that intense?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x127,
        (
            "#153F#5PWow, they work you students\x01",
            "to the bone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xA,
        (
            "#732F#4PBut as of today, the exams are done\x01",
            "(sweet mercy of Aidios!) and people\x01",
            "are going to be a lot more relaxed.\x02\x03",

            "If people WERE going to start talking\x01",
            "about ghost stories, today's the day\x01",
            "for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x104,
        (
            "#035F#2PThere is a converse to this.\x01",
            "If rumors spread too far, it will\x01",
            "be hard to divine the truth...\x02\x03",

            "#030FIf we wish to hear the stories\x01",
            "from the witnesses themselves,\x01",
            "we must act today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x8,
        (
            "#780F#6PWell, then. You may begin your\x01",
            "investigation immediately.\x02\x03",

            "Jill, Hans, Kloe. I expect you\x01",
            "to give them your full support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x105,
        "#041F#4PYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xA,
        "#730F#4PUnderstood, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 225, 400)

    ChrTalk(    #425
        0x9,
        (
            "#644F#6PSo! First off, if we're investigating\x01",
            "something, we need a headquarters.\x02\x03",

            "Someone might come to the Student\x01",
            "Council with information, so you can\x01",
            "use our meeting room!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x101,
        "#1006F#6PThat'll be perfect! Let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2511   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_34_7695 end

    def Function_35_81BA(): pass

    label("Function_35_81BA")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x1F, 115970, 0, 2750, 0)
    ClearChrFlags(0x1F, 0x80)
    OP_6D(116530, 0, 4170, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #427
        0x8,
        (
            "#782F#6PGilbert... My boy, what do you\x01",
            "think you're doing?\x02\x03",

            "What would drive you to such violence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x1F,
        (
            "#1226F#4PHeh. Two reasons, really.\x02\x03",

            "#1220FThe first is that my orders are to simply\x01",
            "cause further chaos in this pissant little\x01",
            "kingdom at my discretion.\x02\x03",

            "My beloved alma mater seemed a perfect\x01",
            "candidate for a little shake-up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x8,
        (
            "#783F#6P...What happened to you, Gilbert?\x02\x03",

            "#782FYou were so dedicated to peace and your\x01",
            "political aspirations as a student...\x02\x03",

            "When did you lose that passion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x1F,
        (
            "#1221F#4PIdeals are just that--ideals. A little\x01",
            "thing called reality has a way of\x01",
            "trampling them in the mud.\x02\x03",

            "Money and privilege are everything... It became\x01",
            "so obvious, serving as Dalmore's steward.\x02\x03",

            "#1226FI'd intended to eventually depose that doddering\x01",
            "old fool and take over as his successor...\x02\x03",

            "Thanks to everyone's beloved 'Bracer Guild,'\x01",
            "however, that goal was smashed to dust.\x02\x03",

            "#1220FSo I decided to take a different\x01",
            "route to wealth and power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x8,
        "#783F#6PHow foolish...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x1F,
        (
            "#1226F#4PHeheh. Say whatever you wish.\x02\x03",

            "#1221FAs for my other goal...\x01",
            "That, Dean Collins,\x01",
            "would be the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x8,
        "#782F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x1F,
        (
            "#1221F#4PAccording to 'rumors'...which I know to be\x01",
            "fact, old man...she's studying at this academy.\x02\x03",

            "I don't suppose you'd be willing to tell\x01",
            "me who she's pretending to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x8,
        (
            "#783F#6PI have no idea what you're talking about.\x02\x03",

            "#782FAll I can say for certain is that no such\x01",
            "girl is present at this academy.\x02\x03",

            "You're looking in the wrong place,\x01",
            "Gilbert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x1F,
        (
            "#1221F#4PHah. Trying to play the fool\x01",
            "until the bitter end?\x02\x03",

            "#1226FSo be it, then. With the phones dead,\x01",
            "I have all the time in the world.\x02\x03",

            "I'll just have to look over the\x01",
            "students myself until I find her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x8,
        "#782F#6PGh...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2500   ._SN", 129, 0, 0)
    IdleLoop()
    Return()

    # Function_35_81BA end

    def Function_36_88F4(): pass

    label("Function_36_88F4")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_6D(87050, 0, 7080, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_8951():
        OP_6D(86660, 0, 2460, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8951)
    OP_67(0, 6180, -10000, 3000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T2500   ._SN", 129, 0, 0)
    IdleLoop()
    Return()

    # Function_36_88F4 end

    def Function_37_8994(): pass

    label("Function_37_8994")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_6D(41510, -250, -3520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(41760, 0, 9240, 4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/T2500   ._SN", 129, 0, 0)
    IdleLoop()
    Return()

    # Function_37_8994 end

    def Function_38_8A1C(): pass

    label("Function_38_8A1C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x102, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 3470, 0, 2580, 180)
    SetChrPos(0x9, 3500, 0, 1470, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(-3290, 0, 2710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_8AED():
        OP_6D(4140, 0, 2560, 3000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_8AED)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 0x0)
    OP_22(0x71, 0x0, 0x5F)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #438
        0xA,
        "#732F#6PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x9,
        "#642F#4PDid I...hear something?\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x5F)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #440
        0xA,
        "#732F#4POver here...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)

    def lambda_8BD3():

        label("loc_8BD3")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_8BD3")

    QueueWorkItem2(0x9, 1, lambda_8BD3)
    Sleep(100)

    def lambda_8BE9():
        OP_6D(2420, 0, 5620, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BE9)
    OP_8E(0xA, 0x820, 0x0, 0x157C, 0x7D0, 0x0)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x102, 0x1)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #441
        0xA,
        "#733F#4PWha--?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10FE)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/T2500   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_38_8A1C end

    def Function_39_8C61(): pass

    label("Function_39_8C61")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_D2(0x7036E, 0x70373, 0x1B)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 2080, 0, 5500, 0)
    SetChrPos(0x9, 2600, 0, 4850, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(2170, 0, 5050, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_8D32():
        OP_8F(0xFE, 0x74E, 0x0, 0x15E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8D32)
    Sleep(100)
    OP_8F(0xA, 0x4B0, 0x0, 0x1612, 0x3E8, 0x0)
    OP_8C(0xA, 45, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #442
        0x9,
        (
            "#646F#4P(Heeeeeey, Hans, is someone\x01",
            "at the window?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xA,
        (
            "#732F#6P(Oof, Jill, stop pushing.)\x02\x03",

            "#730F(Okay, just...don't yell or\x01",
            "anything, got it?)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)

    def lambda_8E0F():
        OP_8F(0xFE, 0x97E, 0x0, 0x1504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E0F)
    Sleep(50)
    OP_8F(0xA, 0x6D6, 0x0, 0x1554, 0x3E8, 0x0)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #444
        0x9,
        (
            "#644F#4P(Oh, come on!)\x02\x03",

            "(You think the great Jill, head of the\x01",
            "Student Council, would scream over\x01",
            "litt...le...th--)\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 45, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #445
        "\x07\x05Hans quickly covered Jill's mouth.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #446
        0x9,
        "#643F#4S#4P(JMMH-MMH-AMH!)\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x10FE)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/T2500   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_39_8C61 end

    def Function_40_8F7C(): pass

    label("Function_40_8F7C")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 1750, 0, 5460, 0)
    SetChrPos(0x9, 2430, 0, 5380, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(2170, 0, 5050, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrTalk(    #447
        0xA,
        (
            "#730F#2P(I see now...)\x02\x03",

            "(So basically, you guys are looking\x01",
            "for a way to get us out of this?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #448
        (
            "\x07\x00#1040F(Exactly.)\x02\x03",

            "(I thought I'd let you know so\x01",
            "you can keep the others calm.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #449
        0x9,
        (
            "#644F#4P(Yeah, good call.\x01",
            "We'll do what we can!)\x02\x03",

            "(Can we do anything else to help?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #450
        (
            "#1043F(Let me think...)\x02\x03",

            "#1042F(I could use a list of all students and\x01",
            "faculty currently present on the grounds.)\x02\x03",

            "(It would help a lot when we move in.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #451
        0x9,
        "#647F#4P(Right, of course.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xA,
        (
            "#730F#2P(Yeah, okay. We'll write\x01",
            "a list up right now.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #453
        (
            "\x07\x05Jill and Hans compiled a list of the staff and\x01",
            "students on the grounds, and slipped the paper\x01",
            "through the window.\x02\x03",

            "Joshua added the list of hostages to the Bracer Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_28(0xC1, 0x4, 0x2)
    OP_28(0xC1, 0x4, 0x8)
    OP_28(0xC1, 0x1, 0x1)
    OP_28(0xC1, 0x1, 0x4)
    OP_28(0xC1, 0x1, 0x10)
    OP_28(0xC1, 0x1, 0x40)
    OP_28(0xC1, 0x1, 0x100)
    OP_28(0xC1, 0x1, 0x400)
    OP_28(0xC1, 0x1, 0x1000)
    OP_28(0xC1, 0x1, 0x4000)
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #454
        (
            "\x07\x00#1053F(Thank you.)\x02\x03",

            "#1040F(We'll be moving in within the hour.)\x02\x03",

            "(Just hold on until then.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #455
        0x9,
        "#644F#4P(Yeah, we will.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xA,
        (
            "#732F#2P(You guys be careful, okay?)\x02\x03",

            "#734F(And...once things are over, let's\x01",
            "get something to eat at the cafeteria.)\x02\x03",

            "#730F(I've got to hear about what\x01",
            "you've been up to.)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #457
        (
            "#1054F(Haha... All right, then.\x01",
            "Go easy on me, okay?)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FA)
    NewScene("ED6_DT21/T2500   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_40_8F7C end

    def Function_41_9534(): pass

    label("Function_41_9534")

    Call(0, 42)
    Call(0, 43)
    Return()

    # Function_41_9534 end

    def Function_42_953D(): pass

    label("Function_42_953D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270326, 0x270330, 0x27)
    OP_D2(0x270312, 0x27031C, 0x28)
    SetChrPos(0x101, 59470, 0, -750, 270)
    SetChrPos(0x102, 59520, 0, 670, 270)
    SetChrPos(0x10A, 60580, 0, -780, 270)
    SetChrPos(0x10E, 60740, 0, 980, 270)
    OP_6D(61210, 0, 1040, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(45000, 0)
    OP_6E(388, 0)
    SetChrPos(0x22, 50890, 0, 160, 0)
    SetChrPos(0x23, 46610, 0, -730, 90)
    ClearChrFlags(0x23, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #458
        0x22,
        "#2PSon of a...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x22, 46610, 0, 600, 90)
    ClearChrFlags(0x22, 0x80)

    def lambda_9728():
        OP_6D(57420, 0, 710, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9728)

    def lambda_9740():
        OP_67(0, 6150, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9740)

    def lambda_9758():
        OP_6B(1560, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9758)

    def lambda_9768():
        OP_6E(530, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9768)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_9782():
        OP_8E(0xFE, 0xCE9A, 0x0, 0x258, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9782)
    Sleep(100)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_97AC():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFFD26, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_97AC)
    WaitChrThread(0x22, 0x1)
    SetChrChipByIndex(0x22, 39)
    WaitChrThread(0x23, 0x1)
    SetChrChipByIndex(0x23, 40)
    WaitChrThread(0x23, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #459
        0x22,
        "#1PBracers?! HERE?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 28)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x10A, 32)
    SetChrChipByIndex(0x10E, 34)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #460
        0x101,
        "#1005F#4PCOME ON!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x102,
        "#1042F#4PAttack!\x02",
    )

    CloseMessageWindow()

    def lambda_986D():
        OP_6D(57500, 0, 830, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_986D)

    def lambda_9885():
        OP_6B(1300, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9885)

    def lambda_9895():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9895)
    Sleep(30)

    def lambda_98B5():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98B5)
    Sleep(30)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_98DF():
        OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_98DF)

    def lambda_98FA():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_98FA)
    Sleep(30)

    def lambda_991A():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_991A)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_993F():
        OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_993F)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_998A"),
        (SWITCH_DEFAULT, "loc_998F"),
    )


    label("loc_998A")

    OP_B4(0x0)
    Jump("loc_998F")

    label("loc_998F")

    Return()

    # Function_42_953D end

    def Function_43_9990(): pass

    label("Function_43_9990")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(57200, 0, 140, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x22, 54400, 0, 970, 90)
    SetChrPos(0x23, 55400, 0, -1460, 90)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 57200, 0, 140, 270)
    SetChrPos(0x1, 57200, 0, 140, 270)
    SetChrPos(0x2, 57200, 0, 140, 270)
    SetChrPos(0x3, 57200, 0, 140, 270)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 9)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)
    OP_A2(0x2024)
    OP_A2(0x20B8)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_72(0x0, 0x2)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_43_9990 end

    def Function_44_9B17(): pass

    label("Function_44_9B17")

    Call(0, 45)
    Call(0, 46)
    Return()

    # Function_44_9B17 end

    def Function_45_9B20(): pass

    label("Function_45_9B20")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270326, 0x270330, 0x27)
    OP_D2(0x270312, 0x27031C, 0x28)
    SetChrPos(0x101, 24400, 0, -750, 90)
    SetChrPos(0x102, 24400, 0, 540, 90)
    SetChrPos(0x10A, 22950, 0, -1000, 90)
    SetChrPos(0x10E, 22950, 0, 390, 90)
    OP_6D(24680, 0, 950, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    SetChrPos(0x22, 36490, 0, 600, 270)
    SetChrPos(0x23, 36490, 0, -730, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #462
        0x22,
        "Son of a...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_9CF7():
        OP_6D(27430, 0, 790, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9CF7)

    def lambda_9D0F():
        OP_6B(2050, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D0F)

    def lambda_9D1F():
        OP_6E(416, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9D1F)
    SetChrChipByIndex(0x22, 27)

    def lambda_9D34():
        OP_8E(0xFE, 0x7602, 0x0, 0x258, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9D34)
    Sleep(100)
    SetChrChipByIndex(0x23, 38)

    def lambda_9D59():
        OP_8E(0xFE, 0x7602, 0x0, 0xFFFFFD26, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9D59)
    WaitChrThread(0x22, 0x1)
    SetChrChipByIndex(0x22, 39)
    WaitChrThread(0x23, 0x1)
    SetChrChipByIndex(0x23, 40)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #463
        0x23,
        "#4PBracers?! HERE?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 28)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x10A, 32)
    SetChrChipByIndex(0x10E, 34)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #464
        0x101,
        "#1005F#1PCOME ON!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x102,
        "#1042F#1PAttack!\x02",
    )

    CloseMessageWindow()

    def lambda_9E10():
        OP_6D(27140, 0, 340, 250)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E10)

    def lambda_9E28():
        OP_6B(1800, 250)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9E28)

    def lambda_9E38():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E38)
    Sleep(30)

    def lambda_9E58():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E58)
    Sleep(30)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_9E82():
        OP_90(0xFE, 0xFFFFF63C, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9E82)

    def lambda_9E9D():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9E9D)
    Sleep(30)

    def lambda_9EBD():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_9EBD)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_9EE2():
        OP_90(0xFE, 0xFFFFF63C, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9EE2)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_9F2D"),
        (SWITCH_DEFAULT, "loc_9F32"),
    )


    label("loc_9F2D")

    OP_B4(0x0)
    Jump("loc_9F32")

    label("loc_9F32")

    Return()

    # Function_45_9B20 end

    def Function_46_9F33(): pass

    label("Function_46_9F33")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(28050, 0, -20, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x22, 28800, 0, 700, 270)
    SetChrPos(0x23, 29240, 0, -1490, 270)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 27220, 0, -10, 90)
    SetChrPos(0x1, 27220, 0, -10, 90)
    SetChrPos(0x2, 27220, 0, -10, 90)
    SetChrPos(0x3, 27220, 0, -10, 90)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)
    OP_A2(0x2024)
    OP_A2(0x20B9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_46_9F33 end

    def Function_47_A09A(): pass

    label("Function_47_A09A")

    Call(0, 48)
    Call(0, 49)
    Return()

    # Function_47_A09A end

    def Function_48_A0A3(): pass

    label("Function_48_A0A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270326, 0x270330, 0x27)
    OP_D2(0x270312, 0x27031C, 0x28)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x22, 41170, 0, 4220, 90)
    SetChrPos(0x23, 42610, 0, 4220, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x22, 37)
    SetChrSubChip(0x22, 0)
    SetChrChipByIndex(0x23, 36)
    SetChrSubChip(0x23, 0)
    OP_6D(42710, 0, 5190, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_A1EB():
        OP_6D(42460, 0, 490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A1EB)

    def lambda_A203():
        OP_6E(302, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A203)
    SetChrChipByIndex(0x101, 28)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x10A, 32)
    SetChrChipByIndex(0x10E, 34)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_43(0x101, 0x1, 0x0, 0x32)
    OP_43(0x102, 0x1, 0x0, 0x33)
    OP_43(0x10A, 0x1, 0x0, 0x34)
    OP_43(0x10E, 0x1, 0x0, 0x35)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_A273():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A273)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_A29D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A29D)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #466
        0x22,
        "#6PSon of a...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x23,
        "#6PBracers?! HERE?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x22, 39)
    SetChrSubChip(0x22, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x23, 40)
    SetChrSubChip(0x23, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #468
        0x101,
        "#1006F#2PGot'cha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x102,
        "#1046F#2PAttack!\x02",
    )

    CloseMessageWindow()

    def lambda_A348():
        OP_6D(42680, 0, 1100, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A348)

    def lambda_A360():
        OP_6B(2420, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A360)

    def lambda_A370():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A370)
    Sleep(30)

    def lambda_A390():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A390)
    Sleep(30)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_A3BA():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A3BA)

    def lambda_A3D5():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A3D5)
    Sleep(30)

    def lambda_A3F5():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_A3F5)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_A41A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A41A)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_A465"),
        (SWITCH_DEFAULT, "loc_A46A"),
    )


    label("loc_A465")

    OP_B4(0x0)
    Jump("loc_A46A")

    label("loc_A46A")

    Return()

    # Function_48_A0A3 end

    def Function_49_A46B(): pass

    label("Function_49_A46B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(41790, 0, 1060, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x22, 42290, 0, 3240, 180)
    SetChrPos(0x23, 39710, 0, 1520, 180)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 41790, 0, 1060, 0)
    SetChrPos(0x1, 41790, 0, 1060, 0)
    SetChrPos(0x2, 41790, 0, 1060, 0)
    SetChrPos(0x3, 41790, 0, 1060, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 13)
    OP_A2(0x2024)
    OP_A2(0x20B7)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_49_A46B end

    def Function_50_A5D2(): pass

    label("Function_50_A5D2")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 41710, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A5F9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A5F9)
    OP_8E(0xFE, 0xA2EE, 0xFFFFFF06, 0xFFFFF4D4, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_50_A5D2 end

    def Function_51_A621(): pass

    label("Function_51_A621")

    Sleep(80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 42810, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A64D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A64D)
    OP_8E(0xFE, 0xA73A, 0xFFFFFF06, 0xFFFFF4D4, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_51_A621 end

    def Function_52_A675(): pass

    label("Function_52_A675")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 41090, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A6A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A6A1)
    OP_8E(0xFE, 0xA082, 0xFFFFFF06, 0xFFFFEF98, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_52_A675 end

    def Function_53_A6C9(): pass

    label("Function_53_A6C9")

    Sleep(350)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 42620, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A6F5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A6F5)
    OP_8E(0xFE, 0xA67C, 0xFFFFFF06, 0xFFFFEFC0, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_53_A6C9 end

    def Function_54_A71D(): pass

    label("Function_54_A71D")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(116200, 10, 5150, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_A793():
        OP_6D(117060, 0, 4540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A793)

    def lambda_A7AB():
        OP_6E(282, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A7AB)
    OP_43(0x101, 0x1, 0x0, 0x37)
    OP_43(0x102, 0x1, 0x0, 0x38)
    OP_43(0x10A, 0x1, 0x0, 0x39)
    OP_43(0x10E, 0x1, 0x0, 0x3A)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A80F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A80F)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #470
        0x8,
        "#780F#6PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xB,
        "#5PEveryone!...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        (
            "#1006F#2PGooooood afternoon!\x01",
            "Someone order a rescue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x102,
        "#1035F#2P...We're glad you're safe, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x8,
        (
            "#783F#6PEstelle, Joshua, to have YOU come...\x02\x03",

            "#780FThose are your fellow bracers\x01",
            "behind you, I take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x10E,
        "#843F#2PWe are. I am Kurt Nardin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x10A,
        (
            "#1310F#2PAnd I'm Anelace Elfead!\x01",
            "Nice to meet'cha!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #477
        "\x07\x05The team explained their plan to free the academy.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #478
        0x8,
        (
            "#783F#6PI see... Thank you.\x02\x03",

            "#782FYou are aware of who...commands\x01",
            "these men, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x101,
        (
            "#1007F#2PGilbert, Dalmore's old steward, right?\x02\x03",

            "#1019FI heard he was trying to\x01",
            "kidnap Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x8,
        (
            "#782F#6PYes. He does not seem to know that\x01",
            "'Kloe' is the princess, however.\x02\x03",

            "He only knows that the 'princess'\x01",
            "can be found at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        (
            "#1015F#2PI see...\x02\x03",

            "Sorta weird, though, given that the masked\x01",
            "pervert knew exactly who she was.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #482
        0x102,
        (
            "#1035F#2PThe jaegers the society utilizes don't have\x01",
            "nearly as much access to information as\x01",
            "Enforcers do, for security purposes.\x02\x03",

            "#1040FI doubt he's been told anything that\x01",
            "wasn't strictly critical to their mission.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #483
        0x101,
        "#1016F#5PAh, good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0x10A,
        (
            "#817F#2PThat's kinda bad news, though, isn't it?\x02\x03",

            "#812FIf he's really that clueless, he might\x01",
            "try and snatch some other girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x10E,
        "#842F#2PA distinct possibility.\x02",
    )

    CloseMessageWindow()

    def lambda_AD3A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD3A)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #486
        0x8,
        (
            "#783F#6PI am also worried about that...\x02\x03",

            "#782FPlease, hurry and stop him, before\x01",
            "he does something terribly foolish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x101,
        "#1002F#2PWe will!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #488
        (
            "\x07\x05Estelle checked the names of Dean Collins\x01",
            "and Fauna off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2025)
    OP_28(0xC0, 0x1, 0x100)
    OP_28(0xC1, 0x2, 0x1)
    OP_28(0xC1, 0x1, 0x2)
    Fade(500)
    OP_6D(116280, 0, 2740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 116280, 0, 2740, 0)
    SetChrPos(0x1, 116280, 0, 2740, 0)
    SetChrPos(0x2, 116280, 0, 2740, 0)
    SetChrPos(0x3, 116280, 0, 2740, 0)
    OP_4B(0xB, 255)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_54_A71D end

    def Function_55_AEE9(): pass

    label("Function_55_AEE9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AF10():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF10)
    OP_8E(0xFE, 0x1C93A, 0x0, 0x546, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C322, 0x0, 0xABE, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_55_AEE9 end

    def Function_56_AF4C(): pass

    label("Function_56_AF4C")

    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AF78():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF78)
    OP_8E(0xFE, 0x1C93A, 0x0, 0x546, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C764, 0x0, 0xA78, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_56_AF4C end

    def Function_57_AFB4(): pass

    label("Function_57_AFB4")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AFE0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFE0)
    OP_8E(0xFE, 0x1C93A, 0x0, 0x2E4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C64C, 0x0, 0x690, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_57_AFB4 end

    def Function_58_B01C(): pass

    label("Function_58_B01C")

    Sleep(1200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_B048():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B048)
    OP_8E(0xFE, 0x1CA8E, 0x0, 0x622, 0xFA0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_58_B01C end

    def Function_59_B070(): pass

    label("Function_59_B070")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(2620, 0, 5110, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(45000, 0)
    OP_6E(295, 0)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 1470, 0, 5490, 0)
    SetChrPos(0x9, 2500, 0, 5490, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_B15F():
        OP_6D(3110, 0, 3980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B15F)

    def lambda_B177():
        OP_6E(327, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B177)
    OP_43(0x101, 0x1, 0x0, 0x3C)
    OP_43(0x102, 0x1, 0x0, 0x3D)
    OP_43(0x10A, 0x1, 0x0, 0x3E)
    OP_43(0x10E, 0x1, 0x0, 0x3F)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B1BA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B1BA)
    Sleep(100)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B1E4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B1E4)
    Sleep(100)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B20E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B20E)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B238():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B238)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B262():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B262)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #489
        0x9,
        "#641F#6POur legendary heroes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xA,
        (
            "#731F#6PHey! Was wondering if you'd\x01",
            "forgotten about us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x101,
        "#1008F#4PAhaha... Sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x102,
        (
            "#1040F#4PHas the situation here changed\x01",
            "at all since I came by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x9,
        "#645F#6PYeah, actually...\x02",
    )

    CloseMessageWindow()

    def lambda_B370():
        OP_6D(3880, 0, 3670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B370)

    def lambda_B388():
        OP_8F(0xFE, 0xD34, 0x0, 0x1108, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B388)
    Sleep(100)
    OP_8E(0xA, 0x956, 0x0, 0x14AA, 0xBB8, 0x0)
    OP_8E(0xA, 0x988, 0x0, 0x116C, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #494
        0x9,
        (
            "#642F#6P(That Gilbert bozo just came by,\x01",
            "demanding to know if the 'princess'\x01",
            "was here.)\x02\x03",

            "(Said she'd receive special treatment\x01",
            "if she named herself.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        "#1019F#4P(Urge to kill, RISING.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x102,
        "#1035F#4P(What a wild goose chase.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0xA,
        (
            "#734F#6P(Yeah, we told him to go stuff himself.)\x02\x03",

            "#732F(He looked pretty desperate, though.\x01",
            "I dunno what he'll do if he really loses it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x101,
        "#1002F#4P(Don't worry, we can handle him.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x20,
        "#1PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x21,
        "#5PSo, um, what should we do?\x02",
    )

    CloseMessageWindow()

    def lambda_B5B2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5B2)

    def lambda_B5C0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B5C0)
    Sleep(80)

    def lambda_B5D3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5D3)

    def lambda_B5E1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_B5E1)
    Sleep(80)

    def lambda_B5F4():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B5F4)
    OP_8C(0xA, 225, 400)

    ChrTalk(    #501
        0x101,
        (
            "#1004F#4POh, right, sorry.\x02\x03",

            "#1006FCould you guys stay in here\x01",
            "until it's safe?\x02\x03",

            "Our friends are still fighting\x01",
            "the jaeger goons outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x21,
        "#5PAll right, we will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0x20,
        "#1PWhen will this end?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x12,
        (
            "#5PI-It's a little nerve-racking,\x01",
            "but we'll wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x102,
        (
            "#1040F#4PWe'll try to settle things\x01",
            "as fast as we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #506
        0x102,
        "#1042F#4PHans, Jill...\x02",
    )

    CloseMessageWindow()

    def lambda_B766():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B766)
    Sleep(50)

    def lambda_B779():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B779)
    Sleep(50)

    def lambda_B78C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B78C)
    Sleep(50)

    def lambda_B79F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B79F)
    Sleep(50)

    def lambda_B7B2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B7B2)
    Sleep(50)
    OP_8C(0x10E, 0, 400)

    ChrTalk(    #507
        0x9,
        (
            "#644F#6PYeah, yeah, we get it.\x02\x03",

            "#648FGetting shot at isn't really my 'thing,'\x01",
            "anyway. We'll leave it to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xA,
        (
            "#730F#6PCome back once you take\x01",
            "care of them.\x02\x03",

            "We'll handle everything else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0x102,
        "#1049F#4PThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x101,
        "#1006F#4PSee ya soooon!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #511
        (
            "\x07\x05Estelle checked the names of Jill, Hans, Kaden,\x01",
            "Alice, and Purity off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2026)
    OP_28(0xC0, 0x1, 0x200)
    OP_28(0xC1, 0x2, 0x4000)
    OP_28(0xC1, 0x1, 0x8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2970, 0, 170, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 3470, 0, 2580, 180)
    SetChrPos(0x9, 3500, 0, 1470, 0)
    SetChrPos(0x20, -240, 0, 3050, 90)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 90)
    SetChrPos(0x0, 2970, 0, 170, 180)
    SetChrPos(0x1, 2970, 0, 170, 180)
    SetChrPos(0x2, 2970, 0, 170, 180)
    SetChrPos(0x3, 2970, 0, 170, 180)
    OP_69(0x0, 0x0)
    OP_4B(0xA, 255)
    OP_4B(0x9, 255)
    OP_4B(0x20, 255)
    OP_4B(0x12, 255)
    OP_4B(0x21, 255)
    OP_8C(0x20, 180, 0)
    OP_8C(0x12, 90, 0)
    OP_8C(0x21, 0, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_59_B070 end

    def Function_60_BA77(): pass

    label("Function_60_BA77")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BA9E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA9E)
    OP_8E(0xFE, 0x97E, 0x0, 0xAD2, 0xFA0, 0x0)
    Return()

    # Function_60_BA77 end

    def Function_61_BABF(): pass

    label("Function_61_BABF")

    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BAEB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAEB)
    OP_8E(0xFE, 0xD98, 0x0, 0xA6E, 0xFA0, 0x0)
    Return()

    # Function_61_BABF end

    def Function_62_BB0C(): pass

    label("Function_62_BB0C")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BB38():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB38)
    OP_8E(0xFE, 0x884, 0x0, 0x53C, 0xFA0, 0x0)
    Return()

    # Function_62_BB0C end

    def Function_63_BB59(): pass

    label("Function_63_BB59")

    Sleep(1200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BB85():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB85)
    OP_8E(0xFE, 0xD48, 0x0, 0x546, 0xFA0, 0x0)
    Return()

    # Function_63_BB59 end

    def Function_64_BBA6(): pass

    label("Function_64_BBA6")

    Call(0, 65)
    Call(0, 66)
    Return()

    # Function_64_BBA6 end

    def Function_65_BBAF(): pass

    label("Function_65_BBAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270327, 0x270331, 0x27)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(44540, 0, 38690, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x24, 36)
    SetChrChipByIndex(0x25, 37)
    SetChrPos(0x24, 32720, 0, 29970, 90)
    SetChrPos(0x25, 51040, 0, 29970, 270)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    FadeToBright(1000, 0)

    def lambda_BCD3():
        OP_6D(41850, 0, 30040, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCD3)

    def lambda_BCEB():
        OP_8E(0xFE, 0x9FBA, 0x0, 0x7512, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BCEB)

    def lambda_BD06():
        OP_8E(0xFE, 0xA6EA, 0x0, 0x7512, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_BD06)
    WaitChrThread(0x24, 0x1)
    WaitChrThread(0x25, 0x1)
    SetChrSubChip(0x24, 0)
    SetChrSubChip(0x25, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #512
        0x24,
        "#6PDamn, is that gunfire still going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x25,
        "#4PSounds like it.\x02",
    )

    CloseMessageWindow()

    def lambda_BD7D():
        OP_6D(42070, 0, 27750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BD7D)

    def lambda_BD95():
        OP_8E(0xFE, 0x9E7A, 0x0, 0x6874, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BD95)
    Sleep(100)

    def lambda_BDB5():
        OP_8E(0xFE, 0xA5BE, 0x0, 0x6892, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_BDB5)
    WaitChrThread(0x24, 0x1)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #514
        0x24,
        (
            "#5PDoesn't look like they've broken\x01",
            "through the gate yet...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 46770, -2000, 38650, 270)

    ChrTalk(    #515
        0x101,
        "#4PThat'd be because that's a diversion.\x02",
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_BE97():
        OP_6D(42800, 0, 31350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE97)

    def lambda_BEAF():
        OP_67(0, 6030, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BEAF)

    def lambda_BEC7():
        OP_6E(337, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BEC7)

    def lambda_BED7():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_BED7)

    def lambda_BEE7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BEE7)
    OP_43(0x101, 0x1, 0x0, 0x43)
    Sleep(250)

    def lambda_BF01():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_BF01)
    OP_43(0x102, 0x1, 0x0, 0x44)
    Sleep(250)
    OP_43(0x10A, 0x1, 0x0, 0x45)
    Sleep(250)
    OP_43(0x10E, 0x1, 0x0, 0x46)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #516
        0x25,
        "#2PWha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0x24,
        (
            "#2PINTRUDERS?! What the hell?!\x01",
            "What are they doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x101,
        "#1029F#6PElementary, my dear jaegers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x10A,
        "#816F#3PWe're here because we're bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x102,
        (
            "#1048F#6P(I'm not sure that's really\x01",
            "much of an answer...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C01C():
        OP_6D(42340, 0, 30650, 280)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C01C)

    def lambda_C034():
        OP_6B(2320, 280)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C034)
    OP_0D()

    def lambda_C045():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C045)
    Sleep(30)
    SetChrChipByIndex(0x24, 38)
    SetChrFlags(0x24, 0x1000)

    def lambda_C06A():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_C06A)

    def lambda_C080():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C080)
    Sleep(30)
    SetChrChipByIndex(0x25, 39)
    SetChrFlags(0x25, 0x1000)

    def lambda_C0A5():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_C0A5)

    def lambda_C0BB():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C0BB)
    Sleep(30)

    def lambda_C0D6():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_C0D6)
    Sleep(150)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x25, 0xFF)
    Battle(0x79F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C11C"),
        (SWITCH_DEFAULT, "loc_C121"),
    )


    label("loc_C11C")

    OP_B4(0x0)
    Jump("loc_C121")

    label("loc_C121")

    Return()

    # Function_65_BBAF end

    def Function_66_C122(): pass

    label("Function_66_C122")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    OP_44(0x24, 0x0)
    OP_44(0x25, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(41850, 0, 31500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x24, 39960, 0, 29850, 0)
    SetChrPos(0x25, 42350, 0, 29860, 0)
    ClearChrFlags(0x24, 0x1)
    SetChrFlags(0x24, 0x2)
    SetChrChipByIndex(0x24, 26)
    SetChrSubChip(0x24, 12)
    ClearChrFlags(0x25, 0x1)
    SetChrFlags(0x25, 0x2)
    SetChrChipByIndex(0x25, 26)
    SetChrSubChip(0x25, 10)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 41850, 0, 31500, 180)
    SetChrPos(0x1, 41850, 0, 31500, 180)
    SetChrPos(0x2, 41850, 0, 31500, 180)
    SetChrPos(0x3, 41850, 0, 31500, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x2027)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_66_C122 end

    def Function_67_C286(): pass

    label("Function_67_C286")

    SetChrChipByIndex(0x101, 28)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9FA6, 0x0, 0x834A, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_67_C286 end

    def Function_68_C2D1(): pass

    label("Function_68_C2D1")

    SetChrChipByIndex(0x102, 30)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9F1A, 0x0, 0x8912, 0x1770, 0x0)
    OP_8E(0xFE, 0xA4C4, 0x0, 0x8318, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_68_C2D1 end

    def Function_69_C330(): pass

    label("Function_69_C330")

    SetChrChipByIndex(0x10A, 32)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9FD8, 0x0, 0x8836, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_69_C330 end

    def Function_70_C37B(): pass

    label("Function_70_C37B")

    SetChrChipByIndex(0x10E, 34)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9F24, 0x0, 0x8E94, 0x1770, 0x0)
    OP_8E(0xFE, 0xA56E, 0x0, 0x88E0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_70_C37B end

    def Function_71_C3DA(): pass

    label("Function_71_C3DA")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(500, 0, 33070, 0)
    OP_67(0, 6800, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(272, 0)
    OP_4A(0x14, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x15, 255)
    OP_4A(0x1C, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_C45C():
        OP_6D(2270, 0, 33520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C45C)

    def lambda_C474():
        OP_67(0, 6160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C474)

    def lambda_C48C():
        OP_6B(3040, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C48C)

    def lambda_C49C():
        OP_6E(267, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_C49C)
    OP_43(0x101, 0x1, 0x0, 0x48)
    OP_43(0x10A, 0x1, 0x0, 0x49)
    OP_43(0x102, 0x1, 0x0, 0x4A)
    OP_43(0x10E, 0x1, 0x0, 0x4B)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C4DF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C4DF)
    Sleep(100)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C509():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_C509)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C533():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C533)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C55D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C55D)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #521
        0x14,
        "#6PYou guys...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x15,
        "#3PEstelle and Joshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0x101,
        "#1008F#4PHaha! Hi, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x102,
        "#1054F#4PLong time no see.\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #525
        0x14,
        (
            "#6PWhy the heck are YOU guys here?!\x02\x03",

            "Wait, you aren't with THOSE guys, are you?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x14, 400)

    ChrTalk(    #526
        0x1C,
        (
            "#5POh, come on, Logic.\x01",
            "How does that make any sense?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x1A,
        (
            "#5PI bet the bracers are\x01",
            "here to rescue us!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 90, 400)

    ChrTalk(    #528
        0x101,
        "#1006F#4PExactly!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #529
        (
            "\x07\x05Estelle explained the group's plan\x01",
            "and how they're freeing people.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #530
        0x14,
        (
            "#6PO-Okay... Sorry I rushed to\x01",
            "conclusions there.\x02\x03",

            "So, you guys!\x01",
            "What do we do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x10E,
        (
            "#843F#4PUntil we are sure the grounds are\x01",
            "secure, you should remain here.\x02\x03",

            "#840FIt's possible you could be injured if you\x01",
            "wander outside in the middle of combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x14,
        (
            "#6PB-B-But, if we stay here, they'll come\x01",
            "back and capture us again...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x10A,
        (
            "#818F#4PHmmm, I guess it's possible, but\x01",
            "leaving is still more dangerous.\x02\x03",

            "#819FYou don't wanna get shot by a stray round\x01",
            "or nommed on by a beast, do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #534
        0x14,
        "#6PU-Umm-ummm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #535
        0x101,
        (
            "#1016F#4PAnelace... Don't scare them more\x01",
            "than they are already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0x102,
        (
            "#1040F#4PAnyway, that's the idea.\x01",
            "Will you stay here for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0x15,
        "#3PYes... We'll keep our heads down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0x1C,
        "#5PGood luck, you guys!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #539
        (
            "\x07\x05Estelle checked the names of Logic, Argyle, Monika,\x01",
            "and Thelma off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2028)
    OP_28(0xC0, 0x1, 0x400)
    OP_28(0xC1, 0x2, 0x400)
    OP_28(0xC1, 0x1, 0x800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2880, 0, 31810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2880, 0, 31810, 180)
    SetChrPos(0x1, 2880, 0, 31810, 180)
    SetChrPos(0x2, 2880, 0, 31810, 180)
    SetChrPos(0x3, 2880, 0, 31810, 180)
    OP_69(0x0, 0x0)
    OP_8C(0x14, 225, 0)
    OP_8C(0x1A, 0, 0)
    OP_8C(0x15, 180, 0)
    OP_8C(0x1C, 45, 0)
    OP_4B(0x14, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x15, 255)
    OP_4B(0x1C, 255)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_71_C3DA end

    def Function_72_CB88(): pass

    label("Function_72_CB88")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_CBAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CBAF)
    OP_8E(0xFE, 0x870, 0x0, 0x7F76, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_72_CB88 end

    def Function_73_CBD7(): pass

    label("Function_73_CBD7")

    Sleep(300)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_CC03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CC03)
    OP_8E(0xFE, 0xD34, 0x0, 0x80DE, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_73_CBD7 end

    def Function_74_CC2B(): pass

    label("Function_74_CC2B")

    Sleep(600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_CC57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CC57)
    OP_8E(0xFE, 0x87A, 0x0, 0x7AE4, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_74_CC2B end

    def Function_75_CC7F(): pass

    label("Function_75_CC7F")

    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_CCAB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CCAB)
    OP_8E(0xFE, 0xCE4, 0x0, 0x7B84, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_75_CC7F end

    def Function_76_CCD3(): pass

    label("Function_76_CCD3")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(94250, 0, 35630, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(268, 0)
    OP_4A(0x18, 255)
    OP_4A(0x17, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_CD55():
        OP_6D(94080, 0, 35020, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CD55)

    def lambda_CD6D():
        OP_6E(277, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_CD6D)
    OP_43(0x101, 0x1, 0x0, 0x4D)
    OP_43(0x10A, 0x1, 0x0, 0x4F)
    OP_43(0x102, 0x1, 0x0, 0x4E)
    OP_43(0x10E, 0x1, 0x0, 0x50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_CDB0():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_CDB0)
    Sleep(100)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_CDDA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CDDA)
    Sleep(100)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_CE04():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CE04)
    Sleep(100)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_CE2E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_CE2E)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #540
        0x1E,
        "#4PIt's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0x101,
        "#2P#1002FEveryone, are you okay?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0x102,
        (
            "#1040F#4PIs anyone... No, no one\x01",
            "looks injured. Good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x18,
        (
            "#6PEstelle...and JOSHUA?!\x02\x03",

            "Why are you two here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x101,
        "#2P#1006FY'know, funny story...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #545
        "\x07\x05Estelle explained events up to now and the plan of attack.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #546
        0x17,
        (
            "#5PSo that's what all the noise is!\x02\x03",

            "I guess I owe Mickey a Royal Crepe or something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0x1D,
        (
            "#6PHmph! All he did was ditch class and\x01",
            "then get lucky enough to run off.\x02\x03",

            "About all slackers are good for...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1D, 400)

    ChrTalk(    #548
        0x18,
        "#6PNot NOW, Dennis!\x02",
    )

    CloseMessageWindow()

    def lambda_D06B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D06B)
    Sleep(100)

    def lambda_D07E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_D07E)
    Sleep(100)

    def lambda_D091():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D091)
    Sleep(100)

    def lambda_D0A4():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D0A4)
    Sleep(100)
    OP_8C(0x10A, 45, 400)

    ChrTalk(    #549
        0x1E,
        (
            "#4PIn this case, his actions were\x01",
            "appropriate and life-saving.\x02\x03",

            "Thanks to him, everyone knew\x01",
            "to come and save us.\x02\x03",

            "Contempt for your savior only makes\x01",
            "you look like a churl, Dennis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x1D,
        "#6PMrgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #551
        0x101,
        (
            "#1016F#5PUh, guys, I dunno if this\x01",
            "is the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0x102,
        (
            "#1040F#4PAnyway, we'd like for you to remain\x01",
            "here until we're certain it's safe.\x02\x03",

            "Can you stay put?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 180, 400)

    ChrTalk(    #553
        0x18,
        "#6PWell, I...\x02",
    )

    CloseMessageWindow()

    def lambda_D243():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D243)
    Sleep(100)

    def lambda_D256():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D256)
    Sleep(100)

    def lambda_D269():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D269)
    Sleep(100)

    def lambda_D27C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_D27C)
    Sleep(100)

    def lambda_D28F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_D28F)
    Sleep(500)

    ChrTalk(    #554
        0x18,
        "#6P...I understand. All right.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)
    OP_8C(0x1E, 225, 400)

    ChrTalk(    #555
        0x1E,
        "#4PPlease...make sure everyone is safe!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)

    ChrTalk(    #556
        0x101,
        "#1006F#5PLeave it to us!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #557
        (
            "\x07\x05Estelle checked the names of Gerome, Patrick, Dennis,\x01",
            "and Reina off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2029)
    OP_28(0xC0, 0x1, 0x800)
    OP_28(0xC1, 0x2, 0x1000)
    OP_28(0xC1, 0x1, 0x2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(92940, 0, 32090, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 92940, 0, 32090, 180)
    SetChrPos(0x1, 92940, 0, 32090, 180)
    SetChrPos(0x2, 92940, 0, 32090, 180)
    SetChrPos(0x3, 92940, 0, 32090, 180)
    OP_69(0x0, 0x0)
    OP_8C(0x17, 90, 0)
    OP_8C(0x18, 270, 0)
    SetChrPos(0x1D, 94990, 250, 35500, 233)
    SetChrPos(0x1E, 94520, 250, 33430, 270)
    OP_4B(0x18, 255)
    OP_4B(0x17, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_76_CCD3 end

    def Function_77_D492(): pass

    label("Function_77_D492")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_D4B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D4B9)
    OP_8E(0xFE, 0x168B4, 0x0, 0x821E, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_77_D492 end

    def Function_78_D4E1(): pass

    label("Function_78_D4E1")

    Sleep(300)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_D50D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D50D)
    OP_8E(0xFE, 0x16CBA, 0x0, 0x81C4, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_78_D4E1 end

    def Function_79_D535(): pass

    label("Function_79_D535")

    Sleep(600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_D561():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D561)
    OP_8E(0xFE, 0x16800, 0x0, 0x7D31, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_79_D535 end

    def Function_80_D589(): pass

    label("Function_80_D589")

    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_D5B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D5B5)
    OP_8E(0xFE, 0x16D00, 0x0, 0x7D31, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_80_D589 end

    def Function_81_D5DD(): pass

    label("Function_81_D5DD")

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
        (0, "loc_D656"),
        (1, "loc_D65C"),
        (SWITCH_DEFAULT, "loc_D662"),
    )


    label("loc_D656")

    OP_A2(0x1200)
    Jump("loc_D662")

    label("loc_D65C")

    OP_A2(0x1201)
    Jump("loc_D662")

    label("loc_D662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D670")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_D674")

    label("loc_D670")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_D674")

    Return()

    # Function_81_D5DD end

    def Function_82_D675(): pass

    label("Function_82_D675")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #558
        "\x07\x05Quiet in the halls! --Student Council\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_82_D675 end

    def Function_83_D6CD(): pass

    label("Function_83_D6CD")

    SetPlaceName(0x6F)
    Return()

    # Function_83_D6CD end

    def Function_84_D6D1(): pass

    label("Function_84_D6D1")

    SetPlaceName(0x5E)
    Return()

    # Function_84_D6D1 end

    def Function_85_D6D5(): pass

    label("Function_85_D6D5")

    SetPlaceName(0x6E)
    Return()

    # Function_85_D6D5 end

    def Function_86_D6D9(): pass

    label("Function_86_D6D9")

    SetPlaceName(0x74)
    Return()

    # Function_86_D6D9 end

    def Function_87_D6DD(): pass

    label("Function_87_D6DD")

    SetPlaceName(0x73)
    Return()

    # Function_87_D6DD end

    SaveToFile()

Try(main)
