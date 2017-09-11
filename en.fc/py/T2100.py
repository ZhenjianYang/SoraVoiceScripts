from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2100   ._SN',
            'ED6_DT01/T2100_1 ._SN',
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
        'Nial',                                 # 9
        'Clem',                                 # 10
        'Murray',                               # 11
        'Matron Theresa',                       # 12
        'Sieg',                                 # 13
        'Lytton',                               # 14
        'Ciel',                                 # 15
        'Rutherford',                           # 16
        'Randall',                              # 17
        'Muriel',                               # 18
        "Man's Voice",                          # 19
        'Melvin',                               # 20
        'Hardt',                                # 21
        'Percy',                                # 22
        'Seagaro',                              # 23
        'Edel',                                 # 24
        'Legaro',                               # 25
        'Sylvie',                               # 26
        'Ruvie',                                # 27
        'Atget',                                # 28
        'Matilda',                              # 29
        'Mayor Dalmore',                        # 30
        'Boat',                                 # 31
        'Boat',                                 # 32
        'Gull Seaside Way',                     # 33
        'Ruan - South Block',                   # 34
        'Ruan Landing Port',                    # 35
    )

    DeclEntryPoint(
        Unknown_00              = 26000,
        Unknown_04              = 0,
        Unknown_08              = 112000,
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02320 ._CH',             # 04
        'ED6_DT07/CH01290 ._CH',             # 05
        'ED6_DT07/CH01540 ._CH',             # 06
        'ED6_DT07/CH01760 ._CH',             # 07
        'ED6_DT06/CH20159 ._CH',             # 08
        'ED6_DT07/CH01050 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH00005 ._CH',             # 0D
        'ED6_DT07/CH00015 ._CH',             # 0E
        'ED6_DT07/CH00045 ._CH',             # 0F
        'ED6_DT07/CH02323 ._CH',             # 10
        'ED6_DT07/CH00005 ._CH',             # 11
        'ED6_DT07/CH00015 ._CH',             # 12
        'ED6_DT07/CH00045 ._CH',             # 13
        'ED6_DT07/CH02410 ._CH',             # 14
        'ED6_DT07/CH01220 ._CH',             # 15
        'ED6_DT07/CH02490 ._CH',             # 16
        'ED6_DT07/CH01030 ._CH',             # 17
        'ED6_DT07/CH01070 ._CH',             # 18
        'ED6_DT07/CH01153 ._CH',             # 19
        'ED6_DT07/CH01003 ._CH',             # 1A
        'ED6_DT07/CH01053 ._CH',             # 1B
        'ED6_DT07/CH01023 ._CH',             # 1C
        'ED6_DT07/CH01120 ._CH',             # 1D
        'ED6_DT06/CH20160 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02320P._CP',             # 04
        'ED6_DT07/CH01290P._CP',             # 05
        'ED6_DT07/CH01540P._CP',             # 06
        'ED6_DT07/CH01760P._CP',             # 07
        'ED6_DT06/CH20159P._CP',             # 08
        'ED6_DT07/CH01050P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH00005P._CP',             # 0D
        'ED6_DT07/CH00015P._CP',             # 0E
        'ED6_DT07/CH00045P._CP',             # 0F
        'ED6_DT07/CH02323P._CP',             # 10
        'ED6_DT07/CH00005P._CP',             # 11
        'ED6_DT07/CH00015P._CP',             # 12
        'ED6_DT07/CH00045P._CP',             # 13
        'ED6_DT07/CH02410P._CP',             # 14
        'ED6_DT07/CH01220P._CP',             # 15
        'ED6_DT07/CH02490P._CP',             # 16
        'ED6_DT07/CH01030P._CP',             # 17
        'ED6_DT07/CH01070P._CP',             # 18
        'ED6_DT07/CH01153P._CP',             # 19
        'ED6_DT07/CH01003P._CP',             # 1A
        'ED6_DT07/CH01053P._CP',             # 1B
        'ED6_DT07/CH01023P._CP',             # 1C
        'ED6_DT07/CH01120P._CP',             # 1D
        'ED6_DT06/CH20160P._CP',             # 1E
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
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
        X                   = 37220,
        Z                   = 1700,
        Y                   = -36830,
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
        X                   = 2420,
        Z                   = -250,
        Y                   = 94980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
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
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4300,
        Z                   = 4000,
        Y                   = 3300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1700,
        Z                   = 0,
        Y                   = 5200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 21800,
        Z                   = 0,
        Y                   = 73300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 21000,
        Z                   = 0,
        Y                   = 74300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 20400,
        Z                   = 0,
        Y                   = 72900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        X                   = 16600,
        Z                   = -1800,
        Y                   = 111000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 41290,
        Z                   = -1970,
        Y                   = 66200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 16430,
        Z                   = -1800,
        Y                   = 111960,
        Direction           = 280,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 47400,
        Z                   = 0,
        Y                   = 81500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 45940,
        Z                   = 0,
        Y                   = 80850,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 49870,
        Z                   = 0,
        Y                   = 79770,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 49320,
        Z                   = 0,
        Y                   = 81240,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 31510,
        Z                   = 0,
        Y                   = 89810,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 29470,
        Z                   = 0,
        Y                   = 87520,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 23580,
        Z                   = 2160,
        Y                   = 102820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        X                   = 25260,
        Z                   = 0,
        Y                   = 128199,
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
        X                   = 51060,
        Z                   = 400,
        Y                   = 27190,
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
        X                   = 81750,
        Z                   = 0,
        Y                   = 80640,
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
        X                   = 52790,
        Y                   = 2000,
        Z                   = 67850,
        Range               = 49030,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFD8E,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 47550,
        Y                   = 2000,
        Z                   = 53890,
        Range               = 55410,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xC33C,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 35920,
        Y                   = 5000,
        Z                   = 88550,
        Range               = 99180,
        Unknown_10          = 0xFFFFEC78,
        Unknown_14          = 0xFCEE,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 27150,
        Y                   = 2000,
        Z                   = 78400,
        Range               = 25490,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x11F80,
        Unknown_18          = 0x0,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 44990,
        Y                   = 0,
        Z                   = 89330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 44,
    )

    DeclEvent(
        X                   = 38080,
        Y                   = 0,
        Z                   = 78540,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = 37930,
        Y                   = 0,
        Z                   = 89380,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 46,
    )

    DeclEvent(
        X                   = 30610,
        Y                   = 0,
        Z                   = 96060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 46,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 108200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 47,
    )

    DeclEvent(
        X                   = 20930,
        Y                   = -1500,
        Z                   = 93960,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = 61000,
        Y                   = 0,
        Z                   = 78900,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 49,
    )

    DeclEvent(
        X                   = 66890,
        Y                   = -500,
        Z                   = 93800,
        Range               = 2200,
        Unknown_10          = 0x898,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 50,
    )

    DeclEvent(
        X                   = 73630,
        Y                   = 0,
        Z                   = 80790,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 51,
    )


    DeclActor(
        TriggerX            = 13500,
        TriggerZ            = 0,
        TriggerY            = 73400,
        TriggerRange        = 1000,
        ActorX              = 13500,
        ActorZ              = 1500,
        ActorY              = 73400,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23750,
        TriggerZ            = 1000,
        TriggerY            = 102860,
        TriggerRange        = 1000,
        ActorX              = 23580,
        ActorZ              = 4000,
        ActorY              = 102820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6EA",          # 00, 0
        "Function_1_B4B",          # 01, 1
        "Function_2_C83",          # 02, 2
        "Function_3_E00",          # 03, 3
        "Function_4_E4D",          # 04, 4
        "Function_5_E71",          # 05, 5
        "Function_6_EE2",          # 06, 6
        "Function_7_1946",         # 07, 7
        "Function_8_1C1B",         # 08, 8
        "Function_9_1E1C",         # 09, 9
        "Function_10_1FD4",        # 0A, 10
        "Function_11_20E0",        # 0B, 11
        "Function_12_293D",        # 0C, 12
        "Function_13_2C28",        # 0D, 13
        "Function_14_2D0B",        # 0E, 14
        "Function_15_2E97",        # 0F, 15
        "Function_16_2FA3",        # 10, 16
        "Function_17_309A",        # 11, 17
        "Function_18_3378",        # 12, 18
        "Function_19_3607",        # 13, 19
        "Function_20_3A7B",        # 14, 20
        "Function_21_3D89",        # 15, 21
        "Function_22_3D8E",        # 16, 22
        "Function_23_438E",        # 17, 23
        "Function_24_47C5",        # 18, 24
        "Function_25_495E",        # 19, 25
        "Function_26_4DEF",        # 1A, 26
        "Function_27_5434",        # 1B, 27
        "Function_28_5467",        # 1C, 28
        "Function_29_549F",        # 1D, 29
        "Function_30_54D9",        # 1E, 30
        "Function_31_5DF6",        # 1F, 31
        "Function_32_6080",        # 20, 32
        "Function_33_6513",        # 21, 33
        "Function_34_6613",        # 22, 34
        "Function_35_6B0B",        # 23, 35
        "Function_36_6B34",        # 24, 36
        "Function_37_79FE",        # 25, 37
        "Function_38_8091",        # 26, 38
        "Function_39_8564",        # 27, 39
        "Function_40_916A",        # 28, 40
        "Function_41_92C7",        # 29, 41
        "Function_42_949D",        # 2A, 42
        "Function_43_9671",        # 2B, 43
        "Function_44_9718",        # 2C, 44
        "Function_45_971C",        # 2D, 45
        "Function_46_9720",        # 2E, 46
        "Function_47_9724",        # 2F, 47
        "Function_48_9728",        # 30, 48
        "Function_49_972C",        # 31, 49
        "Function_50_9730",        # 32, 50
        "Function_51_9734",        # 33, 51
    )


    def Function_0_6EA(): pass

    label("Function_0_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_727")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    SetChrPos(0x18, 45320, 0, 82680, 270)
    SetChrPos(0x19, 43580, 0, 82680, 90)
    Jump("loc_A73")

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_764")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    SetChrPos(0x18, 51500, 1000, 103610, 270)
    SetChrPos(0x19, 51500, 1000, 102530, 270)
    Jump("loc_A73")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_7CD")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 13750, 0, 69100, 180)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 12090, 0, 69000, 180)
    SetChrPos(0x18, 64440, 0, 89630, 280)
    SetChrPos(0x19, 65900, 0, 99540, 0)
    Jump("loc_A73")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_885")
    SetChrPos(0x15, 14980, 0, 68500, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 26)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 42710, -1800, 69570, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 27)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 39480, -1800, 69500, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 28)
    OP_44(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xF, 36220, -1800, 69550, 180)
    SetChrPos(0x18, 45320, 0, 82680, 270)
    SetChrPos(0x19, 43580, 0, 82680, 90)
    Jump("loc_A73")

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_935")
    SetChrPos(0x15, 10810, 0, 72960, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 46060, 0, 79390, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 17800, 0, 73500, 90)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 48870, 0, 80920, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 48270, 0, 78680, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 49650, 0, 78980, 180)
    SetChrPos(0x18, 24590, 0, 69200, 135)
    SetChrPos(0x19, 22240, 0, 68440, 180)
    Jump("loc_A73")

    label("loc_935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_9F6")
    SetChrPos(0x15, 10810, 0, 72960, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 45860, 0, 78450, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 17800, 0, 73500, 90)
    ClearChrFlags(0x13, 0x80)
    OP_43(0x13, 0x0, 0x0, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 18050, -1800, 111280, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 18320, -1800, 113600, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 18190, -1800, 110060, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x18, 19630, 0, 72720, 270)
    SetChrPos(0x19, 20110, 0, 74150, 270)
    Jump("loc_A73")

    label("loc_9F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_A22")
    SetChrPos(0x18, 47130, 0, 78430, 180)
    SetChrPos(0x19, 45970, 0, 78440, 180)
    Jump("loc_A73")

    label("loc_A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_A73")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 47840, 0, 78500, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 17800, 0, 73500, 90)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_A73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A91")
    OP_64(0x0, 0x1)

    label("loc_A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_A9F")
    OP_A3(0x3FA)
    Event(0, 26)

    label("loc_A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_AAD")
    OP_A3(0x3FB)
    Event(0, 30)

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_ABB")
    OP_A3(0x3FC)
    Event(0, 31)

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_AD2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 32)

    label("loc_AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 6)), scpexpr(EXPR_END)), "loc_AE0")
    OP_A3(0x3FE)
    Event(0, 36)

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 7)), scpexpr(EXPR_END)), "loc_AF1")
    OP_A3(0x3FF)
    Event(0, 39)
    OP_A2(0x412)

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_B08")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3F0)
    Event(0, 38)

    label("loc_B08")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_B14"),
        (SWITCH_DEFAULT, "loc_B39"),
    )


    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")
    OP_A2(0x412)
    Event(0, 23)

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B36")
    OP_A2(0x429)
    Event(0, 33)

    label("loc_B36")

    Jump("loc_B39")

    label("loc_B39")

    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_6EA end

    def Function_1_B4B(): pass

    label("Function_1_B4B")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFF5420, 0x30047)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")
    OP_B1("t2100_y")
    Jump("loc_B87")

    label("loc_B7E")

    OP_B1("t2100_n")

    label("loc_B87")

    SetChrBattleFlags(0xA, 0x20)
    OP_89(0xA, -960, -2780, 92980, 135)
    OP_72(0x12, 0x2)
    OP_71(0x12, 0x400)
    OP_71(0x12, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCA")
    OP_64(0x0, 0x1)

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_BD4")
    Jump("loc_C71")

    label("loc_BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_BEA")
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_BF4")
    Jump("loc_C71")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_C0F")
    OP_1B(0x0, 0x0, 0x2B)
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_END)), "loc_C25")
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_C2F")
    Jump("loc_C71")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_C3E")
    OP_1B(0x0, 0x0, 0x2A)
    Jump("loc_C71")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_END)), "loc_C59")
    OP_1B(0x0, 0x0, 0x29)
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)
    Jump("loc_C71")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_C71")
    OP_1B(0x0, 0x0, 0x28)
    OP_6F(0x11, 1020)
    OP_72(0x1A, 0x2)

    label("loc_C71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C82")
    OP_22(0x1C5, 0x1, 0x64)

    label("loc_C82")

    Return()

    # Function_1_B4B end

    def Function_2_C83(): pass

    label("Function_2_C83")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_DEA")

    label("loc_CA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_DEA")

    label("loc_CC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_DEA")

    label("loc_CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_DEA")

    label("loc_CF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_DEA")

    label("loc_D0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_DEA")

    label("loc_D25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_DEA")

    label("loc_D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D57")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_DEA")

    label("loc_D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D70")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_DEA")

    label("loc_D70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D89")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_DEA")

    label("loc_D89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_DEA")

    label("loc_DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_DEA")

    label("loc_DBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_DEA")

    label("loc_DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_DEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DFF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_DEA")

    label("loc_DFF")

    Return()

    # Function_2_C83 end

    def Function_3_E00(): pass

    label("Function_3_E00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E4C")
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2B")
    Sleep(1000)
    Jump("loc_E49")

    label("loc_E2B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E44")
    Sleep(2000)
    Jump("loc_E49")

    label("loc_E44")

    Sleep(3000)

    label("loc_E49")

    Jump("Function_3_E00")

    label("loc_E4C")

    Return()

    # Function_3_E00 end

    def Function_4_E4D(): pass

    label("Function_4_E4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E70")
    OP_8D(0xFE, 28870, 90550, 28960, 83580, 4000)
    Jump("Function_4_E4D")

    label("loc_E70")

    Return()

    # Function_4_E4D end

    def Function_5_E71(): pass

    label("Function_5_E71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE1")
    OP_8E(0xFE, 0x4038, 0xFFFFF8F8, 0x1AC20, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_8E(0xFE, 0x4092, 0xFFFFF8F8, 0x1B9C2, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    Jump("Function_5_E71")

    label("loc_EE1")

    Return()

    # Function_5_E71 end

    def Function_6_EE2(): pass

    label("Function_6_EE2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_103E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB2")
    OP_A2(0x7)

    ChrTalk(    #0
        0xFE,
        (
            "War...the mayor getting\x01",
            "arrested...doesn't matter.\x01",
            "I'm still always working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I don't know what's going on\x01",
            "right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "No point getting all worked up\x01",
            "over it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103B")

    label("loc_FB2")


    ChrTalk(    #3
        0xFE,
        (
            "War...the mayor getting\x01",
            "arrested...doesn't matter.\x01",
            "I'm still always working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "No point getting all worked up\x01",
            "over it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103B")

    Jump("loc_1942")

    label("loc_103E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1101")
    OP_A2(0x7)

    ChrTalk(    #5
        0xFE,
        (
            "There've been boys running\x01",
            "all over the place, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I don't know what the world's\x01",
            "coming to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I've been around for quite some\x01",
            "time, so I know what's what.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113E")

    label("loc_1101")


    ChrTalk(    #8
        0xFE,
        (
            "There've been boys running\x01",
            "all over the place lately...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113E")

    Jump("loc_1942")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_121E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F7")
    OP_A2(0x7)

    ChrTalk(    #9
        0xFE,
        "The water's very mysterious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Any time you look at it, it always\x01",
            "makes your face look different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "In all my years, I've never\x01",
            "gotten tired of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_11F7")


    ChrTalk(    #12
        0xFE,
        "The water's very mysterious...\x02",
    )

    CloseMessageWindow()

    label("loc_121B")

    Jump("loc_1942")

    label("loc_121E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_END)), "loc_12FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B2")
    OP_A2(0x7)

    ChrTalk(    #13
        0xFE,
        "Oh, it's you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Ha ha...looks like that boat\x01",
            "proved useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Maybe next time you can stay\x01",
            "and visit for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_12B2")


    ChrTalk(    #16
        0xFE,
        (
            "You kids...maybe next time, you\x01",
            "can stay and visit for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F7")

    Jump("loc_1942")

    label("loc_12FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184F")
    OP_A2(0x42B)
    OP_28(0x3C, 0x1, 0x10)
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)

    ChrTalk(    #17
        0xFE,
        "Hmm...? Whaddya want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#002FCan we rent your boat? We\x01",
            "need to get across as quickly\x01",
            "as possible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I'm afraid not. That duke fellow's\x01",
            "already reserved it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Maybe come back later...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#003FOh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x136,
        (
            "#043FPlease...won't you help us?\x02\x03",

            "There's a little boy in\x01",
            "grave danger!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x136, 400)

    ChrTalk(    #23
        0xFE,
        (
            "Now, don't go shedding tears like that.\x01",
            "You remind me of my granddaughter,\x01",
            "and I don't like to see her upset, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Well, all right.\x01",
            "I suppose it can't hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Go ahead and hop aboard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x136,
        "#048FTh-Thank you, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#006FYou're a lifesaver, mister!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Ha ha... I'll just tell that duke\x01",
            "fellow that the boat's being\x01",
            "repaired.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #29
        0xFE,
        (
            "Do you know how to handle a\x01",
            "boat, boy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#012FYes, sir... I'll manage.\x02\x03",

            "Come on, both of you!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6C(45000, 0)
    OP_6D(-740, -2260, 92790, 0)
    SetChrPos(0x1E, -810, -2850, 92590, 90)
    SetChrFlags(0x1E, 0x40)
    OP_A1(0x1E, 0x12)
    OP_72(0x12, 0x4)
    OP_72(0x12, 0x2)
    OP_71(0x12, 0x400)
    OP_71(0x12, 0x40)
    OP_48()
    Sleep(1)
    SetChrBattleFlags(0x0, 0x20)
    SetChrBattleFlags(0x1, 0x20)
    SetChrBattleFlags(0x2, 0x20)
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    SetChrPos(0x102, 300, -2760, 92400, 45)
    SetChrPos(0x101, -980, -2750, 92300, 270)
    SetChrPos(0x136, -1000, -2750, 93000, 270)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    ClearChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, -760, -2260, 94400, 180)

    def lambda_16E2():

        label("loc_16E2")

        TurnDirection(0xFE, 0x136, 0)
        OP_48()
        Jump("loc_16E2")

    QueueWorkItem2(0xA, 1, lambda_16E2)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0x92, 0x0, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0x1E, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x1E, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_179E():
        OP_8F(0xFE, 0xFFFFB334, 0xFFFFF63C, 0x16C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_179E)
    Sleep(500)

    def lambda_17BE():
        OP_8F(0xFE, 0xFFFFB334, 0xFFFFF63C, 0x16C2E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_17BE)
    Sleep(500)

    def lambda_17DE():
        OP_8F(0xFE, 0xFFFFB334, 0xFFFFF63C, 0x16C2E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_17DE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x92, 0x5A)
    Sleep(100)
    OP_24(0x92, 0x50)
    Sleep(100)
    OP_24(0x92, 0x46)
    Sleep(100)
    OP_24(0x92, 0x3C)
    Sleep(100)
    OP_24(0x92, 0x32)
    Sleep(100)
    OP_24(0x92, 0x28)
    Sleep(100)
    OP_24(0x92, 0x1E)
    Sleep(100)
    OP_23(0x92)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1942")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_18AD")

    ChrTalk(    #31
        0xFE,
        (
            "Ruan's been called the Seaside\x01",
            "City for ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Anyone can see why, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1917")

    ChrTalk(    #33
        0xFE,
        (
            "We've got another gorgeous\x01",
            "sunset this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "No other city has sunsets\x01",
            "like we do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_1917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1942")

    ChrTalk(    #35
        0xFE,
        "Hmm? You want to use the boat?\x02",
    )

    CloseMessageWindow()

    label("loc_1942")

    TalkEnd(0xA)
    Return()

    # Function_6_EE2 end

    def Function_7_1946(): pass

    label("Function_7_1946")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FB")
    OP_A2(0x0)

    ChrTalk(    #36
        0xFE,
        (
            "We often conduct boat tours of Ruan\x01",
            "from the ferry port behind the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "If that's about what you had in mind,\x01",
            "it can certainly be arranged.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1A38")

    label("loc_19FB")


    ChrTalk(    #38
        0xFE,
        (
            "I'm sorry, but I must show\x01",
            "the guests around right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A38")

    Jump("loc_1C17")

    label("loc_1A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABB")
    OP_A2(0x0)

    ChrTalk(    #39
        0xFE,
        (
            "Let me see...this afternoon,\x01",
            "we'll be going to Air-Letten...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "The Lavantar serves seafood...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1AEC")

    label("loc_1ABB")


    ChrTalk(    #41
        0xFE,
        (
            "I'm sorry, but I'm very busy at\x01",
            "the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEC")

    Jump("loc_1C17")

    label("loc_1AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDA")
    OP_A2(0x0)

    ChrTalk(    #42
        0xFE,
        "If everyone would look...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "To your left is Ruan's iconic\x01",
            "Langland Bridge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "When the bridge is down,\x01",
            "it spans roughly 109 arge\x01",
            "in length.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "A custom Zeissian orbal engine\x01",
            "is used to raise it.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1C17")

    label("loc_1BDA")


    ChrTalk(    #46
        0xFE,
        (
            "I'm sorry, but I must show\x01",
            "the guests around right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C17")

    TalkEnd(0xD)
    Return()

    # Function_7_1946 end

    def Function_8_1C1B(): pass

    label("Function_8_1C1B")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1C9E")

    ChrTalk(    #47
        0xFE,
        (
            "My son's campus festival is soon,\x01",
            "so business has picked up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I'd love to be able to take some\x01",
            "time off...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E18")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D60")
    OP_A2(0x1)

    ChrTalk(    #49
        0xFE,
        (
            "Our lighthouse was built around\x01",
            "forty years ago, roughly the same\x01",
            "time as the Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "It's one of the few structures that\x01",
            "wasn't damaged in the war.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    Jump("loc_1DC7")

    label("loc_1D60")


    ChrTalk(    #51
        0xFE,
        "I gave up my day off to work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I'm so busy that my daughter's\x01",
            "helping out back at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC7")

    Jump("loc_1E18")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E18")

    ChrTalk(    #53
        0xFE,
        (
            "Let's see... I guess I should escort\x01",
            "everyone to the hotel now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E18")

    TalkEnd(0xE)
    Return()

    # Function_8_1C1B end

    def Function_9_1E1C(): pass

    label("Function_9_1E1C")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8A")
    OP_A2(0x2)
    OP_A2(0x3)

    ChrTalk(    #54
        0x13,
        (
            "Ummm...did you drop your dentures\x01",
            "somewhere around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "Has hoh ih ah aww. Hah yuss\x01",
            "hanneh hoo hay han oo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x13,
        (
            "Err...you wanted to play\x01",
            "with bangles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "Hah hanneh hoon heen hy hoonana?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #58
        0x13,
        (
            "I...I'm sorry. All I'm getting from\x01",
            "that is, 'Has anyone seen my banana?'\x01",
            "Surely that's not quite right...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_1FD0")

    label("loc_1F8A")


    ChrTalk(    #59
        0xFE,
        (
            "We'll collect every possible thing\x01",
            "that anyone may have dropped!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD0")

    TalkEnd(0x13)
    Return()

    # Function_9_1E1C end

    def Function_10_1FD4(): pass

    label("Function_10_1FD4")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A3")
    OP_A2(0x6)

    ChrTalk(    #60
        0xFE,
        (
            "Ahh...no work to be done.\x01",
            "Now I can really relax...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I don't get much of a chance\x01",
            "to do so, usually...what with\x01",
            "being a merchant in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Definitely not good for one's health.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20DC")

    label("loc_20A3")


    ChrTalk(    #63
        0xFE,
        (
            "Ahh...no work to be done.\x01",
            "Now I can really relax...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DC")

    TalkEnd(0x14)
    Return()

    # Function_10_1FD4 end

    def Function_11_20E0(): pass

    label("Function_11_20E0")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_216A")

    ChrTalk(    #64
        0xFE,
        (
            "I think I'll go to Zeiss for some\x01",
            "fishing next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I've never been there before, but\x01",
            "I hear it's a fisherman's dream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_216A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2301")
    OP_A2(0x8)

    ChrTalk(    #66
        0xFE,
        (
            "Ain't no such thing as a sure-fire\x01",
            "fishing spot, where the fish will\x01",
            "always bite without fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Gotta see how the day looks\x01",
            "and figure out how to handle\x01",
            "it for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "No one's going to just hand\x01",
            "you the answers. Got to find\x01",
            "'em on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "That's what a good fishing spot\x01",
            "is all about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Now, that doesn't mean that\x01",
            "there's ever a good excuse\x01",
            "for NOT fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234E")

    label("loc_2301")


    ChrTalk(    #71
        0xFE,
        (
            "Now, that doesn't mean that\x01",
            "there's ever a good excuse\x01",
            "for NOT fishing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234E")

    Jump("loc_2939")

    label("loc_2351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_23CB")

    ChrTalk(    #72
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "No matter how good a fisherman you\x01",
            "may be...when they ain't bitin',\x01",
            "they just ain't bitin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_23CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2475")
    OP_A2(0x8)

    ChrTalk(    #74
        0xFE,
        (
            "It's important to try out different\x01",
            "spots when you're fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "If you're where the fish aren't biting,\x01",
            "you just have to go someplace else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B9")

    label("loc_2475")


    ChrTalk(    #76
        0xFE,
        (
            "It's important to try out different\x01",
            "spots when you're fishing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B9")

    Jump("loc_2939")

    label("loc_24BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_2549")

    ChrTalk(    #77
        0xFE,
        "Ssshhh! I need quiet here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "The fish are really sensitive to sound.\x01",
            "They're like the government...they\x01",
            "hear EVERYTHING...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_2549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_25F9")

    ChrTalk(    #79
        0xFE,
        (
            "I don't know what you're all excited\x01",
            "about, but I need quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "The fish are really sensitive to sound.\x01",
            "They're like the government...they\x01",
            "hear EVERYTHING...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_25F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E5")
    OP_A2(0x8)

    ChrTalk(    #81
        0xFE,
        "I've caught a few today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "But these aren't big enough\x01",
            "catches to satisfy me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "I'm going to catch a real whopper!\x01",
            "One for the record books!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "In the name of the holy order\x01",
            "of the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2764")

    label("loc_26E5")


    ChrTalk(    #85
        0xFE,
        (
            "I'm going to catch a real whopper!\x01",
            "One for the record books!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "In the name of the holy order\x01",
            "of the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2764")

    Jump("loc_2939")

    label("loc_2767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2822")
    OP_A2(0x8)

    ChrTalk(    #87
        0xFE,
        (
            "The fish are the most active\x01",
            "around now, in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Naturally, that's when it's easiest\x01",
            "to catch 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Heh heh heh...\x01",
            "Come to me little fishies...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2860")

    label("loc_2822")


    ChrTalk(    #90
        0xFE,
        (
            "The fish are the most active\x01",
            "around now, in the evening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2860")

    Jump("loc_2939")

    label("loc_2863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F4")
    OP_A2(0x8)

    ChrTalk(    #91
        0xFE,
        (
            "Oh, I've come from afar to the\x01",
            "Seaside City... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Ol' Azelia Bay stretches on, and\x01",
            "the fish are sure pretty... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_28F4")


    ChrTalk(    #93
        0xFE,
        (
            "Ol' Azelia Bay stretches on, and\x01",
            "the fish are sure pretty... ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2939")

    TalkEnd(0x15)
    Return()

    # Function_11_20E0 end

    def Function_12_293D(): pass

    label("Function_12_293D")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_29D2")

    ChrTalk(    #94
        0xFE,
        (
            "The guide put a lot of work into\x01",
            "finding out what's good to eat\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "My dad and my daughter both\x01",
            "liked it, so that's great.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C24")

    label("loc_29D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_2A38")

    ChrTalk(    #96
        0xFE,
        (
            "I look at this bridge and I think,\x01",
            "'Now, that's an amazing use of\x01",
            "orbment technology.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C24")

    label("loc_2A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2AAE")

    ChrTalk(    #97
        0xFE,
        "What's got you in such a hurry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I don't suppose it has anything\x01",
            "to do with that boy from earlier?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C24")

    label("loc_2AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2B45")

    ChrTalk(    #99
        0xFE,
        (
            "My dad dropped his dentures into the water.\x01",
            "We don't have a spare set, so I'm guessing the\x01",
            "rest of the day we'll be playing charades...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C24")

    label("loc_2B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD6")
    OP_A2(0x4)

    ChrTalk(    #100
        0xFE,
        (
            "I brought my father and my\x01",
            "daughter here to Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Ha ha...fortunately, everyone's\x01",
            "been getting along very well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C24")

    label("loc_2BD6")


    ChrTalk(    #102
        0xFE,
        (
            "If something does start up\x01",
            "though...I'm keeping out of\x01",
            "the line of fire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C24")

    TalkEnd(0xF)
    Return()

    # Function_12_293D end

    def Function_13_2C28(): pass

    label("Function_13_2C28")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2C4A")

    ChrTalk(    #103
        0xFE,
        "Hey, box seats!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D07")

    label("loc_2C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2C71")

    ChrTalk(    #104
        0xFE,
        "That bridge is amazing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D07")

    label("loc_2C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8A")
    TalkEnd(0x10)
    Call(0, 9)
    Jump("loc_2CC3")

    label("loc_2C8A")


    ChrTalk(    #105
        0xFE,
        "Haas hees ho hembahaassing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Haalb meeeeeh...\x02",
    )

    CloseMessageWindow()

    label("loc_2CC3")

    Jump("loc_2D07")

    label("loc_2CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2D07")

    ChrTalk(    #107
        0xFE,
        (
            "Ahh, yes, I see. The Royal Army\x01",
            "is quite impressive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D07")

    TalkEnd(0x10)
    Return()

    # Function_13_2C28 end

    def Function_14_2D0B(): pass

    label("Function_14_2D0B")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2D7D")

    ChrTalk(    #108
        0xFE,
        (
            "Oh, this is great! \x01",
            "We get to eat here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I'm impressed that my dad found\x01",
            "a place like this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2D9A")

    ChrTalk(    #110
        0xFE,
        "It's so cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2E56")

    ChrTalk(    #111
        0xFE,
        (
            "If you get in trouble, who do you call?\x01",
            "That's right... You call bracers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "At home or abroad, it doesn't matter...\x01",
            "Bracers are always around to help. I love\x01",
            "those guys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(    #113
        0xFE,
        (
            "I don't know why my dad has to\x01",
            "be so stubborn...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E93")

    TalkEnd(0x11)
    Return()

    # Function_14_2D0B end

    def Function_15_2E97(): pass

    label("Function_15_2E97")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2F42")

    ChrTalk(    #114
        0xFE,
        (
            "I wasn't so sure about it to begin\x01",
            "with, but the festival turned out\x01",
            "to be quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "The food was really good and it\x01",
            "wasn't even overpriced.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2F9F")

    ChrTalk(    #116
        0xFE,
        (
            "I've seen postcards of it before,\x01",
            "but this is my first time seeing\x01",
            "it in person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9F")

    TalkEnd(0x16)
    Return()

    # Function_15_2E97 end

    def Function_16_2FA3(): pass

    label("Function_16_2FA3")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_306F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_304A")
    OP_A2(0x9)

    ChrTalk(    #117
        0xFE,
        "That play was a masterpiece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I had my doubts about casting \x01",
            "the boys as girls and vice\x01",
            "versa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "...but it gradually drew me in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_304A")


    ChrTalk(    #120
        0xFE,
        "That play was a masterpiece.\x02",
    )

    CloseMessageWindow()

    label("loc_306C")

    Jump("loc_3096")

    label("loc_306F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3096")

    ChrTalk(    #121
        0xFE,
        "This is an amazing view...\x02",
    )

    CloseMessageWindow()

    label("loc_3096")

    TalkEnd(0x17)
    Return()

    # Function_16_2FA3 end

    def Function_17_309A(): pass

    label("Function_17_309A")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_30C6")

    ChrTalk(    #122
        0xFE,
        "The city sure is noisy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3118")

    ChrTalk(    #123
        0xFE,
        (
            "If anyone just goes and takes\x01",
            "that boat, I'm going to be so\x01",
            "angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_31C6")

    ChrTalk(    #124
        0xFE,
        "A duke came to Ruan today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I was really impressed with how composed\x01",
            "and dignified he was. And to manage such\x01",
            "poise with a bowl-cut like that! Incredible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_31C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_31F5")

    ChrTalk(    #126
        0xFE,
        "I wonder where we'll go next...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_31F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3282")

    ChrTalk(    #127
        0xFE,
        (
            "The white streets, floating\x01",
            "between the blue sky and\x01",
            "the water...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "...I really just can't get over\x01",
            "how beautiful Ruan is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_3282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_32CF")

    ChrTalk(    #129
        0xFE,
        (
            "All that's left to see are the\x01",
            "historical sites from the war.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_32CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_3351")

    ChrTalk(    #130
        0xFE,
        (
            "Phew, we made it just in time to\x01",
            "see the bridge being raised.\x01",
            "What a spectacle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "The size of it is astounding.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3374")

    label("loc_3351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3374")

    ChrTalk(    #132
        0xFE,
        "Hmm...this is amazing!\x02",
    )

    CloseMessageWindow()

    label("loc_3374")

    TalkEnd(0x18)
    Return()

    # Function_17_309A end

    def Function_18_3378(): pass

    label("Function_18_3378")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_33B3")

    ChrTalk(    #133
        0xFE,
        (
            "Did something major\x01",
            "happen, I wonder...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_33B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_344D")

    ChrTalk(    #134
        0xFE,
        (
            "If I could just take out a boat,\x01",
            "where would be the best\x01",
            "place to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I wonder if the Bracer Guild could\x01",
            "recommend anything to see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_344D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_349F")

    ChrTalk(    #136
        0xFE,
        (
            "The bridge is just as\x01",
            "impressive as I'd heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "So romantic...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_349F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_34D4")

    ChrTalk(    #138
        0xFE,
        (
            "Ruan has so many great\x01",
            "sights to see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_34D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_353C")

    ChrTalk(    #139
        0xFE,
        "A marvel over the water...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "The air here just smells so\x01",
            "clean... It's so refreshing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_353C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3583")

    ChrTalk(    #141
        0xFE,
        (
            "The scenery is gorgeous,\x01",
            "but the history is really sad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_3583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_35D1")

    ChrTalk(    #142
        0xFE,
        (
            "It's great to just stand and watch\x01",
            "the sunset over the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_35D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3603")

    ChrTalk(    #143
        0xFE,
        "It's much bigger than I'd expected...\x02",
    )

    CloseMessageWindow()

    label("loc_3603")

    TalkEnd(0x19)
    Return()

    # Function_18_3378 end

    def Function_19_3607(): pass

    label("Function_19_3607")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36BD")

    ChrTalk(    #144
        0xFE,
        (
            "Is it true, what the Liberl\x01",
            "News wrote?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "It's just so hard to believe that\x01",
            "the mayor was a criminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Although, I really never liked\x01",
            "him all that much...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_36BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3701")

    ChrTalk(    #147
        0xFE,
        (
            "The harbormaster, Portos, is\x01",
            "quite a popular fellow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3756")

    ChrTalk(    #148
        0xFE,
        "It's so late already...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I should go home and get\x01",
            "dinner started.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_37E7")

    ChrTalk(    #150
        0xFE,
        (
            "The story about the arson at Mercia\x01",
            "Orphanage is just horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "All the boys and girls there\x01",
            "are pretty close in age, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_37E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_3881")

    ChrTalk(    #152
        0xFE,
        (
            "You know that little boy from\x01",
            "before? Apparently, the matron\x01",
            "came to get him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I don't know what was going\x01",
            "on, but at least he's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_3881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_38E6")

    ChrTalk(    #154
        0xFE,
        (
            "That little boy was running\x01",
            "like his life depended on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "I wonder what's wrong.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_38E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_397F")

    ChrTalk(    #156
        0xFE,
        (
            "There's been a big increase\x01",
            "in tourist traffic lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I hope those people by the\x01",
            "dockside warehouse don't\x01",
            "go causing any trouble...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_397F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_39DB")

    ChrTalk(    #158
        0xFE,
        "Oh...is it this late already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "I should finish my shopping\x01",
            "and get home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A77")

    label("loc_39DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3A77")

    ChrTalk(    #160
        0xFE,
        (
            "The sky bandits held me prisoner\x01",
            "for so long... It's been ages since\x01",
            "I've seen my hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Ruan's still my favorite place\x01",
            "in the world...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A77")

    TalkEnd(0x1A)
    Return()

    # Function_19_3607 end

    def Function_20_3A7B(): pass

    label("Function_20_3A7B")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AC4")

    ChrTalk(    #162
        0xFE,
        "The mayor did something bad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "He's not a nice man?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3B33")

    ChrTalk(    #164
        0xFE,
        (
            "I can't wait to go back to\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I get to see my friends and\x01",
            "the priest is funny.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3B64")
    OP_A2(0xE)

    ChrTalk(    #166
        0xFE,
        "Hee hee. I played a lot today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFA")
    OP_A2(0xE)

    ChrTalk(    #167
        0xFE,
        (
            "I love your uniform, ma'am...\x01",
            "It's really cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        "#041FHa ha...thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "I wish we had uniforms for\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C5E")

    label("loc_3BFA")


    ChrTalk(    #170
        0xFE,
        (
            "I love your uniform, ma'am...\x01",
            "It's really cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I wish we had uniforms for\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5E")

    Jump("loc_3D85")

    label("loc_3C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_3C8C")

    ChrTalk(    #172
        0xFE,
        "I don't wanna worry my mom.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD5")
    OP_A2(0xE)

    ChrTalk(    #173
        0xFE,
        "...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "It's dangerous to run in the street.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CFF")

    label("loc_3CD5")


    ChrTalk(    #175
        0xFE,
        "It's dangerous to run in the street.\x02",
    )

    CloseMessageWindow()

    label("loc_3CFF")

    Jump("loc_3D85")

    label("loc_3D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3D37")

    ChrTalk(    #176
        0xFE,
        (
            "No one should cross the\x01",
            "bridge alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_3D57")

    ChrTalk(    #177
        0xFE,
        "I'm sooo hungry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3D85")

    ChrTalk(    #178
        0xFE,
        "I've been playing with my mom. ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_3D85")

    TalkEnd(0x1B)
    Return()

    # Function_20_3A7B end

    def Function_21_3D89(): pass

    label("Function_21_3D89")

    Call(0, 22)
    Return()

    # Function_21_3D89 end

    def Function_22_3D8E(): pass

    label("Function_22_3D8E")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E11")

    ChrTalk(    #179
        0x1C,
        (
            "If you've got a smile on your\x01",
            "face all your life, it kinda\x01",
            "loses its meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1C,
        "But the fact is, we're alive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_3E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3E71")

    ChrTalk(    #181
        0x1C,
        (
            "I wonder why we have the\x01",
            "fondest memories of times\x01",
            "that we'll never see again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_3E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6A")
    OP_A2(0x4CB)

    ChrTalk(    #182
        0x1C,
        (
            "Well, that settles it. I'm going\x01",
            "to have to give you this book.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x216, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #183
        "\x07\x00Received \x07\x02Carnelia - Chapter 5\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #184
        0x1C,
        "What do you mean, 'Why?'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x1C,
        (
            "Because life is full of\x01",
            "contradictions...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9A")

    label("loc_3F6A")


    ChrTalk(    #186
        0x1C,
        (
            "The light from the sunset\x01",
            "hurts my eyes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9A")

    Jump("loc_438A")

    label("loc_3F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4123")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4082")
    OP_A2(0xF)

    ChrTalk(    #187
        0x1C,
        "Ruan is a big place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x1C,
        (
            "Lots of people come and go,\x01",
            "and it all sort of blurs together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x1C,
        (
            "Sometimes, I think I'm about\x01",
            "as significant as a pebble\x01",
            "that someone tossed aside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x1C,
        "Why, I wonder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_4082")


    ChrTalk(    #191
        0x1C,
        (
            "Lots of people come and go,\x01",
            "and it all sort of blurs together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1C,
        (
            "Sometimes, I think I'm about\x01",
            "as significant as a pebble\x01",
            "that someone tossed aside...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4120")

    Jump("loc_438A")

    label("loc_4123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4187")

    ChrTalk(    #193
        0x1C,
        (
            "I wonder if the stars shine,\x01",
            "beyond the blue sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x1C,
        "It's too far away to see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_4187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_42B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426B")
    OP_A2(0xF)

    ChrTalk(    #195
        0x1C,
        "Where did the birds go...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x1C,
        (
            "They spread their wings and\x01",
            "fly off, to unknown lands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x1C,
        (
            "They look so small, up in the sky,\x01",
            "but they're strong creatures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x1C,
        "I wish I could live like they do...\x02",
    )

    CloseMessageWindow()
    Jump("loc_42B4")

    label("loc_426B")


    ChrTalk(    #199
        0x1C,
        "Where did the birds go...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x1C,
        "I wish I could live like they do...\x02",
    )

    CloseMessageWindow()

    label("loc_42B4")

    Jump("loc_438A")

    label("loc_42B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_4351")

    ChrTalk(    #201
        0x1C,
        (
            "Ahh...the setting sun peers down\x01",
            "upon me from its heavenly perch,\x01",
            "warming all the cockles of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x1C,
        "But it's...a bit too bright...\x02",
    )

    CloseMessageWindow()
    Jump("loc_438A")

    label("loc_4351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_438A")

    ChrTalk(    #203
        0x1C,
        (
            "Ha ha...welcome to the seaside\x01",
            "city of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_438A")

    TalkEnd(0x1C)
    Return()

    # Function_22_3D8E end

    def Function_23_438E(): pass

    label("Function_23_438E")

    EventBegin(0x0)
    OP_67(0, 5600, -10000, 0)
    OP_6C(315000, 0)
    OP_6B(6800, 0)
    OP_6D(52424, 0, 68700, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    SetChrPos(0x101, 25470, 0, 115060, 180)
    SetChrPos(0x102, 24790, 0, 116060, 180)
    SetChrPos(0x136, 26160, 0, 116640, 180)

    def lambda_440A():
        OP_6C(45000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_440A)
    Sleep(5000)

    def lambda_441F():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_441F)

    def lambda_4437():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4437)

    def lambda_4447():
        OP_6D(25850, 0, 115000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4447)
    StopSound(0x9470, 0x14C08, 0x1F40)
    Sleep(8000)

    ChrTalk(    #204
        0x101,
        (
            "#501FWow...so this is Ruan!\x02\x03",

            "This is one gorgeous city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#010FThe blue water and white buildings\x01",
            "do make for a nice contrast.\x02\x03",

            "It certainly feels like a port city.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(    #206
        0x136,
        (
            "#041FHa ha...well, it promises many\x01",
            "varied things.\x02\x03",

            "There's a lighthouse not far from here,\x01",
            "in a little park on the coast.\x02\x03",

            "On the other side of town, there's\x01",
            "a pretty neat-looking church, too.\x02\x03",

            "#040FBut the biggest attraction of all\x01",
            "has to be Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_462F():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_462F)
    Sleep(200)

    def lambda_4642():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4642)
    Sleep(400)

    ChrTalk(    #207
        0x101,
        "#000F#4PWhat's so special about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x136,
        (
            "#040FIt connects the north and south\x01",
            "districts of the city.\x02\x03",

            "And more importantly, it's a\x01",
            "drawbridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#010F#3PA drawbridge, huh? Yeah, that\x01",
            "might be interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x136,
        (
            "#040FThe Bracer Guild is just past there,\x01",
            "in the middle of the main street.\x02\x03",

            "Just in front of the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#006F#4POkay, then. Let's go there first.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_23_438E end

    def Function_24_47C5(): pass

    label("Function_24_47C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x445)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(    #212
        0x136,
        (
            "#040FOh, the Bracer Guild branch is\x01",
            "just down this way.\x02\x03",

            "There. That building there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x136, 0, 400)

    def lambda_4854():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4854)

    def lambda_4862():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4862)

    def lambda_4870():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4870)
    OP_6D(44460, 0, 92190, 4000)

    ChrTalk(    #213
        0x101,
        "#501F#1POh, okay.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_69(0x0, 0x0)
    OP_4F(0x64, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #214
        0x102,
        "#010FWell, let's check it out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4942")

    label("loc_48E2")

    EventBegin(0x1)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(    #215
        0x136,
        (
            "#040FThe Bracer Guild branch is just\x01",
            "down this way.\x02\x03",

            "It's that building up ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4942")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_495D")

    Return()

    # Function_24_47C5 end

    def Function_25_495E(): pass

    label("Function_25_495E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DEE")
    OP_A2(0x415)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #216
        0x101,
        (
            "#004FWhoa...\x01",
            "This is the Langland Bridge?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_49DE():
        OP_6C(90000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49DE)

    def lambda_49EE():
        OP_67(0, 6115, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49EE)

    def lambda_4A06():
        OP_6B(7760, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A06)

    def lambda_4A16():
        OP_6D(51680, 400, 52400, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A16)
    StopSound(0x9470, 0x3D090, 0x1770)
    OP_8C(0x102, 270, 400)

    def lambda_4A42():
        OP_8C(0x136, 270, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4A42)
    Sleep(9000)
    Fade(1000)
    OP_6C(45000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6D(48350, 400, 52340, 0)
    StopSound(0x9470, 0x14C08, 0x0)
    SetChrPos(0x101, 49512, 400, 51770, 270)
    SetChrPos(0x102, 49512, 400, 50400, 270)
    SetChrPos(0x136, 49512, 400, 53040, 270)
    OP_0D()

    ChrTalk(    #217
        0x101,
        (
            "#501FIt sure is huge. It's gotta be twice\x01",
            "as big as the Verte Bridge.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(    #218
        0x136,
        (
            "#040FIt was built more than forty years\x01",
            "ago.\x02\x03",

            "Before then, people used to have\x01",
            "to take a ferry from one shore to\x01",
            "the other.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #219
        0x101,
        (
            "#004FWhy didn't they build a bridge\x01",
            "sooner?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #220
        0x102,
        (
            "#010FThe Roubine River is the only body of\x01",
            "water linking the lake to the ocean.\x02\x03",

            "Ships have to be able to reach\x01",
            "Grancel, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x136,
        (
            "#041FVery astute.\x02\x03",

            "It wasn't possible to build the bridge\x01",
            "until after the Orbal Revolution, fifty\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#501FI get it... Orbment power, right?\x02\x03",

            "#001FBut it looks almost like it just\x01",
            "popped up out of nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x136,
        (
            "#040FThe drawbridge is raised three\x01",
            "times a day.\x02\x03",

            "The next time should be...sometime\x01",
            "this evening, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#006FCool! We need to see that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x102,
        "#019FAgreed.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_4DEE")

    Return()

    # Function_25_495E end

    def Function_26_4DEF(): pass

    label("Function_26_4DEF")

    EventBegin(0x0)
    OP_6D(45290, 0, 87610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 45000, 500, 91157, 0)
    SetChrPos(0x102, 45000, 500, 91157, 0)
    SetChrPos(0x136, 45000, 500, 91157, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_43(0x101, 0x1, 0x0, 0x1B)
    OP_43(0x102, 0x1, 0x0, 0x1C)
    OP_43(0x136, 0x1, 0x0, 0x1D)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x136, 0x1)

    ChrTalk(    #226
        0x101,
        (
            "#501FWow, it's already evening.\x02\x03",

            "#001FLook at that gorgeous sunset!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x102,
        (
            "#010FThat it is. All the light shines\x01",
            "off of the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x136,
        (
            "#041FHa ha... I've always loved it,\x01",
            "too.\x02\x03",

            "#040FOh, yes...it's almost time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #229
        0x101,
        "#004F...For what?\x02",
    )

    CloseMessageWindow()
    OP_22(0x94, 0x1, 0x64)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x11, 0)
    Fade(1000)
    OP_67(0, 6115, -10000, 0)
    OP_6B(7760, 0)
    OP_6D(51680, 400, 52400, 0)
    OP_6C(36000, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    Sleep(1500)
    OP_22(0x93, 0x1, 0x64)
    OP_70(0x11, 0x3E8)
    OP_6C(315000, 18000)
    OP_73(0x11)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x93)
    OP_23(0x94)
    OP_6F(0x11, 1000)
    OP_70(0x11, 0x3FC)
    Sleep(1000)
    Fade(1000)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    StopSound(0x9470, 0x14C08, 0x1F40)
    OP_6D(58250, -1800, 70690, 0)
    SetChrPos(0x101, 59330, -1800, 70537, 180)
    SetChrPos(0x102, 58480, -1800, 70537, 180)
    SetChrPos(0x136, 60300, -1800, 70537, 180)
    OP_0D()

    ChrTalk(    #230
        0x101,
        (
            "#501F#6P*sigh*...\x01",
            "That really is a masterpiece.\x02\x03",

            "Err...how long does it stay up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x136,
        (
            "#040F#2PThirty minutes, I believe.\x02\x03",

            "It's raised in the early morning, just before\x01",
            "noon, and in the evening, and it isn't lowered\x01",
            "again until all the ships have passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x102,
        (
            "#010F#3PI see... So, when there's usually\x01",
            "no foot traffic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x136,
        (
            "#041F#2PHa ha... I admit, it's easy for a\x01",
            "first-timer to get confused.\x02\x03",

            "#044FOh, that reminds me...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)
    Sleep(400)

    ChrTalk(    #234
        0x136,
        (
            "#040F#2PWhat are you guys planning to do\x01",
            "about lodging?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #235
        0x101,
        (
            "#000F#6PHmmm... Well, the second floor\x01",
            "of the guild is always an option.\x02\x03",

            "Although...I could really go for\x01",
            "a luxurious hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x136,
        (
            "#040F#2PWell, then I think you might\x01",
            "want to hurry and get a room.\x02\x03",

            "This is tourist season, so they\x01",
            "tend to fill up pretty quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x102,
        (
            "#010F#3PAll right... No time like the present,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#000F#6PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_72(0x1A, 0x2)
    EventEnd(0x0)
    Return()

    # Function_26_4DEF end

    def Function_27_5434(): pass

    label("Function_27_5434")

    OP_8E(0xFE, 0xB0B8, 0x0, 0x158F6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xB3EC, 0x0, 0x154B4, 0xBB8, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_27_5434 end

    def Function_28_5467(): pass

    label("Function_28_5467")

    Sleep(300)
    OP_8E(0xFE, 0xB0B8, 0x0, 0x158F6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xAEE2, 0x0, 0x154B4, 0xBB8, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_28_5467 end

    def Function_29_549F(): pass

    label("Function_29_549F")

    Sleep(600)
    OP_8E(0xFE, 0xB0B8, 0x0, 0x158F6, 0xBB8, 0x0)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 30)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_71(0x5, 0x800)
    Return()

    # Function_29_549F end

    def Function_30_54D9(): pass

    label("Function_30_54D9")

    EventBegin(0x0)
    OP_6D(24380, 0, 94810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 24040, 0, 94400, 90)
    SetChrPos(0x102, 23870, 0, 93300, 90)
    SetChrPos(0x136, 25410, 0, 93880, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #239
        0x136,
        (
            "#040F#2PThanks for letting me come with\x01",
            "you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#008F#3PHa ha! Oh, come on. We should be\x01",
            "thanking you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#019F#3PYeah. We really appreciate you\x01",
            "playing tour guide for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x136,
        (
            "#045F#2POh, it's no big deal.\x02\x03",

            "#040FAnd...you two are going to be in\x01",
            "Ruan for a while, right?\x02\x03",

            "If you are, I was hoping you'd\x01",
            "come to the campus festival\x01",
            "at the end of next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x101,
        "#004F#3PA festival?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x102,
        (
            "#010F#3PGiven the royal academy's reputation,\x01",
            "I'm betting it's more than just balloons\x01",
            "and party games...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x136,
        (
            "#041F#2PYes, it's an independent, academy-\x01",
            "sanctioned student celebration.\x02\x03",

            "It's a major tradition, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#004F#3POkay, now you've got my attention!\x02\x03",

            "#001FWill it have stage skits and food\x01",
            "stands? Will it have chocolate-\x01",
            "covered Poms?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x136,
        (
            "#041F#2PHa ha, maybe. They really pull\x01",
            "out all the stops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#001F#3POh, yeah. I'm so there!\x02\x03",

            "Umm, I mean, I'd love to join you\x01",
            "for the preparations!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #249
        0x102,
        (
            "#018F#3PNow, hold on, Estelle...\x02\x03",

            "Did you forget how busy we heard\x01",
            "the guild is?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #250
        0x101,
        (
            "#007F#4PMan...that again...?\x01",
            "Awww...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        (
            "#019F#3PStill, I guess it can't hurt to\x01",
            "take a break on the day of the\x01",
            "festival...\x02\x03",

            "But until then, we've got work\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        "#007F#4P*siiiigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x136,
        (
            "#045F#2PHa ha...\x02\x03",

            "#048FWell, if you'll both pardon me,\x01",
            "then.\x02\x03",

            "I'll see you again soon...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #254
        0x101,
        "#006F#3PSure! See ya later!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)

    ChrTalk(    #255
        0x102,
        "#010F#3PBe safe.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x136, 0, 400)

    def lambda_5AF1():
        OP_6D(25200, 0, 97530, 2000)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_5AF1)

    def lambda_5B09():

        label("loc_5B09")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5B09")

    QueueWorkItem2(0x101, 2, lambda_5B09)

    def lambda_5B1A():

        label("loc_5B1A")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5B1A")

    QueueWorkItem2(0x102, 2, lambda_5B1A)
    OP_8E(0x136, 0x6608, 0x0, 0x1AB94, 0xBB8, 0x0)
    SetChrFlags(0x136, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_5B4C():
        OP_6D(23990, 0, 93830, 1500)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_5B4C)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x136, 0x2)

    ChrTalk(    #256
        0x101,
        (
            "#501F#4PHmmm...she's such a sweetie,\x01",
            "yet she's all dignified...\x02\x03",

            "If I were a guy, I'd be completely\x01",
            "wrapped around her finger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x102,
        (
            "#015FYour painfully obvious allusions\x01",
            "aside...\x02\x03",

            "#010FShe certainly seems to be a genuinely\x01",
            "nice, guileless girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#007F#4PDefinitely not like some sneaky\x01",
            "sky bandit I could mention...\x02\x03",

            "#000FMeeting her sure was lucky.\x01",
            "We even got a sweet room\x01",
            "here thanks to her advice!\x02\x03",

            "#001FI'll bet we could even spot Sieg\x01",
            "with the view we have up there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x102,
        (
            "#019FHa ha. You might be right.\x02\x03",

            "#010FWell, how about we take our bags\x01",
            "up to the room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#001F#4PThe penthouse room, you mean!♪\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x136, 0x80)
    SetChrPos(0x136, 27020, 0, 94830, 180)
    EventEnd(0x0)
    RemoveParty(0x35, 0xFF)
    Return()

    # Function_30_54D9 end

    def Function_31_5DF6(): pass

    label("Function_31_5DF6")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 9880, 4200, 91480, 270)
    SetChrPos(0x102, 10260, 4200, 92590, 270)
    OP_6D(-10010, 4200, 90430, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x186A0, 0x0)
    FadeToBright(2000, 0)
    OP_6D(10690, 4200, 93000, 5000)

    ChrTalk(    #261
        0x102,
        "#014F#6PWow... It even has a balcony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#501F#2PYep... And check out this view!\x02\x03",

            "#007FI just hate that we're the only\x01",
            "ones who get to enjoy it.\x02\x03",

            "#003FI was hoping that Dad would\x01",
            "be here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x102,
        (
            "#013F#6PYeah...\x02\x03",

            "#015FI wonder where he is,\x01",
            "and what he's doing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x12, 12770, 4200, 93110, 0)

    NpcTalk(    #264
        0x12,
        "Man's Voice",
        "#3PWell, well...isn't this all posh!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #265
        0x101,
        "#004F#2PWhat was that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #266
        0x102,
        (
            "#012F#6PSounded like it came from\x01",
            "inside...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5DF6 end

    def Function_32_6080(): pass

    label("Function_32_6080")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(24130, 0, 93980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23540, 0, 94500, 90)
    SetChrPos(0x102, 23610, 0, 93330, 45)
    SetChrPos(0x8, 25170, 0, 94000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    FadeToDark(0, 0, -1)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #267
        "\x07\x05Ruan, the following morning...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_1D(0xC)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x1C5, 0x1, 0x64)

    ChrTalk(    #268
        0x8,
        (
            "#145F*yaaaaaaawn*\x02\x03",

            "Oh, man...my poor, aching head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#006FThat must be one heck of a\x01",
            "hangover.\x02\x03",

            "It was kinda impressive the way\x01",
            "you drank the whole bar, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#010FSure you're okay?\x01",
            "You want some water?\x01",
            "Or the bucket again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x8,
        (
            "#142FNo...I'm good.\x02\x03",

            "I've got an event to cover...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        (
            "#501FOh, really? Well, thanks for taking\x01",
            "us in yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x102,
        "#010FWe're both very grateful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x8,
        (
            "#141FJust pass on anything interesting\x01",
            "you hear to me...\x02\x03",

            "I'll be in Ruan for a while, too.\x02\x03",

            "#145FOkay, see you later...\x01",
            "...\x01",
            "Oh, Goddess...why is light so bright?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)

    def lambda_63DE():
        OP_6D(25330, 0, 91170, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_63DE)

    def lambda_63F6():

        label("loc_63F6")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_63F6")

    QueueWorkItem2(0x101, 2, lambda_63F6)

    def lambda_6407():

        label("loc_6407")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_6407")

    QueueWorkItem2(0x102, 2, lambda_6407)
    OP_8E(0x8, 0x6662, 0x0, 0x16058, 0x7D0, 0x0)
    OP_8E(0x8, 0x7814, 0x0, 0x14E92, 0x7D0, 0x0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(200)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Sleep(300)

    def lambda_6462():
        OP_6D(23600, 0, 93950, 1200)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6462)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #275
        0x102,
        (
            "#010FWell, then...what say we head\x01",
            "to the guild?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #276
        0x101,
        (
            "#006FFine by me.\x02\x03",

            "We can see if Jean has any work\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x8)
    EventEnd(0x0)
    Return()

    # Function_32_6080 end

    def Function_33_6513(): pass

    label("Function_33_6513")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 25470, 0, 115060, 180)
    SetChrPos(0x102, 24790, 0, 116060, 180)
    SetChrPos(0x136, 26160, 0, 116640, 180)
    OP_6C(45000, 0)
    OP_6D(25850, 0, 115000, 0)
    OP_0D()

    ChrTalk(    #277
        0x101,
        (
            "#003F#6PNo sign of him on the way...\x02\x03",

            "You don't suppose he's already\x01",
            "there...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x136,
        "#043F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x102,
        (
            "#012FCome on. We'll check out that\x01",
            "warehouse to the south.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3C, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_33_6513 end

    def Function_34_6613(): pass

    label("Function_34_6613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B0A")
    OP_A2(0x42A)
    OP_28(0x3C, 0x1, 0x4)
    OP_28(0x3C, 0x1, 0x8)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_22(0x94, 0x1, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #280
        0x102,
        "#012FDamn, it's almost noon already?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    ClearChrFlags(0x9, 0x80)
    Fade(1000)
    SetChrPos(0x9, 50820, 400, 57120, 0)
    OP_6C(45000, 0)
    OP_6D(50820, 400, 50000, 0)

    def lambda_66EE():
        OP_6D(50820, 200, 35000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66EE)
    OP_8E(0x9, 0xC684, 0xC8, 0x922C, 0x1770, 0x0)
    OP_43(0x9, 0x3, 0x0, 0x23)

    def lambda_6721():
        OP_8E(0x9, 0xC684, 0xC8, 0x6590, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6721)
    Sleep(2000)

    def lambda_6741():
        OP_6D(50890, 0, 70000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6741)
    Sleep(1000)
    SetChrPos(0x101, 50210, 0, 90000, 180)
    SetChrPos(0x102, 51440, 0, 90000, 180)
    SetChrPos(0x136, 50920, 0, 90000, 225)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x136, 0x40)

    def lambda_67A0():
        OP_8E(0xFE, 0xC6E8, 0x0, 0x1145E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_67A0)
    Sleep(200)

    def lambda_67C0():
        OP_8E(0xFE, 0xC422, 0x0, 0x119AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67C0)
    Sleep(200)

    def lambda_67E0():
        OP_8E(0xFE, 0xC8F0, 0x0, 0x11986, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67E0)
    OP_6C(135000, 3600)
    SetChrFlags(0x9, 0x80)

    ChrTalk(    #281
        0x136,
        (
            "#043F#6PNo...!\x02\x03",

            "Clem, please wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x102,
        (
            "#013F#1PIt's no use... I guess he can't\x01",
            "hear you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#005F#5PCrap! Why does the bridge have\x01",
            "to go up NOW, of all times?\x02\x03",

            "It couldn't wait thirty minutes?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x136,
        (
            "#049F#6POh, no... If we don't do something...!\x02\x03",

            "What do we do...?\x01",
            "What CAN we do...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)

    ChrTalk(    #285
        0x102,
        (
            "#012F#1PPlease, Kloe, try to calm down.\x02\x03",

            "You haven't forgotten what you\x01",
            "told us about the bridge already,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #286
        0x136,
        "#044F#4P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x102,
        (
            "#010F#1PNow, how did people get across\x01",
            "before the bridge was built?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #288
        0x101,
        "#004F#2POh, a boat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x136,
        (
            "#042F#4PThat's right!\x02\x03",

            "If I remember correctly, there's a\x01",
            "boat you can rent behind the hotel!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #290
        0x101,
        "#006F#5PAll right! We'll use that, then!\x02",
    )

    CloseMessageWindow()
    OP_72(0x1A, 0x2)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x136, 0x40)
    EventEnd(0x0)

    label("loc_6B0A")

    Return()

    # Function_34_6613 end

    def Function_35_6B0B(): pass

    label("Function_35_6B0B")

    OP_22(0x93, 0x1, 0x64)
    OP_70(0x11, 0x3E8)
    OP_73(0x11)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x93)
    OP_23(0x94)
    OP_6F(0x11, 1000)
    OP_70(0x11, 0x3FC)
    Return()

    # Function_35_6B0B end

    def Function_36_6B34(): pass

    label("Function_36_6B34")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 24790, 0, 116060, 180)
    SetChrPos(0x9, 26160, 0, 116640, 180)
    SetChrPos(0x101, 24790, 0, 114060, 0)
    SetChrPos(0x105, 26160, 0, 114640, 0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 26225, 0, 104380, 0)
    OP_6C(45000, 0)
    OP_6D(25850, 0, 115000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #291
        0xB,
        (
            "#750F#3PThank you so very much. I wish\x01",
            "I had the words to express my\x01",
            "gratitude...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#001F#2PYou really don't need to thank\x01",
            "us. We're just doing our jobs.\x02\x03",

            "#000FStill, are you sure you don't want\x01",
            "us to escort you back to Manoria?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xB,
        (
            "#751FYes, it's fine. The Gull Seaside Way\x01",
            "is like my backyard, after all.\x02\x03",

            "More importantly, I don't want to get\x01",
            "Kloe in trouble at the school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        "#008F#2PNo need to worry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x105,
        (
            "#043FI will accept full responsibility,\x01",
            "Matron.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xB,
        (
            "#750FHa ha... Thank you, Kloe, but it's\x01",
            "fine, really. I want you to focus on\x01",
            "preparing for the campus festival.\x02\x03",

            "All of the children are looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x105,
        "#040FYes, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x102,
        "#1PWhew...made it just in time!\x02",
    )

    CloseMessageWindow()

    def lambda_6E81():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E81)

    def lambda_6E8F():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E8F)
    OP_8E(0x102, 0x6504, 0x0, 0x1B968, 0xFA0, 0x0)
    ClearChrFlags(0x102, 0x4)

    ChrTalk(    #299
        0x102,
        "#010F#2PI brought back the boat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        "#001FThanks! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x105,
        (
            "#040F#6PSorry for making you do that\x01",
            "on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        (
            "#010F#2PDon't worry about it.\x01",
            "It wasn't a tough job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xB,
        (
            "#750FI owe you my gratitude as well,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F94():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F94)
    TurnDirection(0x105, 0x9, 400)

    ChrTalk(    #304
        0x9,
        (
            "#775FMiss Kloe...\x02\x03",

            "All you guys, actually...\x02\x03",

            "Thanks for helping me today.\x02\x03",

            "I was stupid. Really stupid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x105,
        "#043FClem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x9,
        (
            "#773FI thought maybe I could get\x01",
            "back at them...\x02\x03",

            "And then, you had to come to\x01",
            "save me...\x02\x03",

            "#777FYou must think I'm a complete loser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        "#004F#2PW-We don't think that at all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        "#015FYou're not a loser.\x02",
    )

    CloseMessageWindow()

    def lambda_7100():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7100)

    def lambda_710E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_710E)

    def lambda_711C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_711C)

    def lambda_712A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_712A)

    ChrTalk(    #309
        0x9,
        "#777FWha...\x02",
    )

    CloseMessageWindow()

    def lambda_7149():
        OP_6D(25850, 0, 117000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7149)

    def lambda_7161():

        label("loc_7161")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7161")

    QueueWorkItem2(0x9, 1, lambda_7161)

    def lambda_7172():

        label("loc_7172")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7172")

    QueueWorkItem2(0xB, 1, lambda_7172)

    def lambda_7183():

        label("loc_7183")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7183")

    QueueWorkItem2(0x101, 1, lambda_7183)

    def lambda_7194():

        label("loc_7194")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7194")

    QueueWorkItem2(0x105, 1, lambda_7194)
    OP_8E(0x102, 0x6A2C, 0x0, 0x1BE04, 0xBB8, 0x0)
    OP_8E(0x102, 0x6932, 0x0, 0x1C642, 0xBB8, 0x0)
    OP_8C(0x102, 270, 400)

    ChrTalk(    #310
        0x102,
        (
            "#010FYou risked life and limb to protect\x01",
            "something that's important to you.\x02\x03",

            "That's no mean feat, even for\x01",
            "grownups.\x02\x03",

            "#019FPersonally, I thought you were\x01",
            "pretty awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x9,
        "#775F#3PMister Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x102,
        (
            "#012FHowever, you need to leave fighting\x01",
            "the criminals to us.\x02\x03",

            "Your job is to protect the matron\x01",
            "and the other kids. No one else\x01",
            "can do it.\x02\x03",

            "You have to stay with them,\x01",
            "encourage and support them.\x02\x03",

            "#011FYou're the only one who can\x01",
            "do it, Clem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        (
            "#774F#3P...\x02\x03",

            "Only I can do it...?\x02\x03",

            "#770FOkay, I think I get what you're\x01",
            "saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        "#010FYou think you're up to it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x9,
        "#771F#3PYou bet'cha! You can count on me!\x02",
    )

    CloseMessageWindow()

    def lambda_7443():

        label("loc_7443")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7443")

    QueueWorkItem2(0x102, 1, lambda_7443)

    def lambda_7454():

        label("loc_7454")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7454")

    QueueWorkItem2(0x101, 1, lambda_7454)

    def lambda_7465():

        label("loc_7465")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7465")

    QueueWorkItem2(0x105, 1, lambda_7465)

    ChrTalk(    #316
        0xB,
        "#751FHa ha... Thank you, yet again.\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0xFF)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #317
        0xB,
        (
            "#750FTake care, everyone.\x01",
            "If you'll pardon us...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    TurnDirection(0x9, 0x105, 400)

    ChrTalk(    #318
        0x9,
        (
            "#770F#3POh, Miss Kloe! I can't wait to\x01",
            "see the play!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x105,
        (
            "#041FGreat! I've been working hard\x01",
            "on it, so I hope everyone will\x01",
            "be there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x9,
        (
            "#770F#3PYou can count on it!\x02\x03",

            "#771FSee ya later!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)

    def lambda_75B3():
        OP_8E(0xFE, 0x60E0, 0x0, 0x207C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_75B3)
    OP_8C(0x9, 0, 400)

    def lambda_75D5():
        OP_8E(0xFE, 0x6590, 0x0, 0x207C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_75D5)
    Sleep(4000)

    ChrTalk(    #321
        0x101,
        (
            "#007F#2PWhew... I'm glad to see he's\x01",
            "feeling better.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #322
        0x101,
        (
            "#006F#2PSometimes you know JUST the thing to say,\x01",
            "don't you, Joshua. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)

    def lambda_768B():

        label("loc_768B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_768B")

    QueueWorkItem2(0x105, 1, lambda_768B)

    ChrTalk(    #323
        0x105,
        (
            "#048FHa ha. I couldn't believe my eyes, seeing how\x01",
            "quickly Clem cheered up.\x02\x03",

            "#041FThank you, Joshua...so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x102,
        (
            "#015F#3PNo, no... I didn't say anything\x01",
            "special.\x02\x03",

            "#013FYou've got to protect what's\x01",
            "important to you, that's all...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 270, 400)

    def lambda_77C3():
        OP_6D(25400, 0, 115000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77C3)
    OP_8E(0x102, 0x61A8, 0x0, 0x1C3E0, 0x7D0, 0x0)
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 180, 400)
    OP_44(0x105, 0xFF)
    OP_8C(0x105, 270, 0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #325
        0x102,
        (
            "#010F#3PAnyway, I'm just glad that\x01",
            "he's okay.\x02\x03",

            "Thanks for your help, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x105,
        (
            "#045FI should be thanking you.\x02\x03",

            "#044FOh, by the way...\x02\x03",

            "What came of your investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x101,
        (
            "#501FAh, well, that red-headed dude\x01",
            "butted his spiky head in now,\x01",
            "so...\x02\x03",

            "I wonder if he's done yet...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x102,
        (
            "#010F#3PFor now, let's get back to\x01",
            "the guild.\x02\x03",

            "Are you coming with us, Kloe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x105,
        (
            "#042FYes. I'd like to find out what's\x01",
            "really going on.\x02\x03",

            "Not to mention the identity of\x01",
            "the arsonist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        "#006FWell, let's go then!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_36_6B34 end

    def Function_37_79FE(): pass

    label("Function_37_79FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8090")
    OP_A2(0x450)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8090")
    EventBegin(0x0)
    OP_44(0xE, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0xF, 0)

    def lambda_7A3D():
        OP_6D(18500, 0, 73800, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A3D)

    def lambda_7A55():
        OP_6C(225000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A55)
    Sleep(3000)
    CloseMessageWindow()

    ChrTalk(    #331
        0xE,
        (
            "#4PThis way is the park, built to commemorate\x01",
            "the end of the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xE,
        "#4POkay, I have a question for everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xE,
        (
            "#4PAs you know, you'll be right in\x01",
            "front of the Royal Palace if you\x01",
            "cross the Roubine River.\x02\x03",

            "That's where the ships of the\x01",
            "Imperial Navy were defeated,\x01",
            "during the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xE,
        "#4PHow was it done?\x02",
    )

    CloseMessageWindow()
    OP_95(0x10, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #335
        0x10,
        "I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xE,
        "#4PGo ahead...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x10,
        (
            "Heh. I've got it. Too easy.\x02\x03",

            "They used the cannons that are\x01",
            "all over Ruan City, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xE,
        "#4PHmmm...not quite.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xE,
        (
            "#4PThere certainly is plenty of artillery\x01",
            "here, but we still can't withstand a\x01",
            "heavy Imperial attack on that alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xE,
        (
            "#4PI'll give you a hint. They employed\x01",
            "a much more...dynamic method.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D4A():
        OP_95(0x11, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D4A)
    Sleep(10)
    OP_8C(0x11, 30, 2200)
    OP_8C(0x11, 150, 2200)
    OP_8C(0x11, 270, 2200)
    OP_8C(0x11, 30, 2200)
    OP_8C(0x11, 150, 2200)
    OP_8C(0x11, 270, 2200)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #341
        0x11,
        "I know! I KNOOOOW!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xE,
        (
            "#4PAaaaaaand GO! What's the answer,\x01",
            "miss?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x11,
        "They lowered the Langland Bridge?\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #344
        0xE,
        (
            "#4POh, so sorry! That's incorrect!\x02\x03",

            "Power to the city had been knocked\x01",
            "out at the time, so the bridge was\x01",
            "stuck in the raised position.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #345
        0x11,
        "Hmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xE,
        "#4PHere is the answer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xE,
        (
            "#4PMany old and decommissioned ships\x01",
            "were sent from upriver to be\x01",
            "detonated and sunk.\x02\x03",

            "Since the mouth of the river is\x01",
            "so shallow, the Imperial ships\x01",
            "couldn't break through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x11,
        (
            "Wow...that's cool, but it seems\x01",
            "a little bit much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x10,
        "Extreme, if you ask me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xE,
        (
            "#4PWell, we're done for the day now,\x01",
            "so you're free to do as you wish\x01",
            "for a while.\x02\x03",

            "Please have fun until it's time.\x02",
        )
    )

    CloseMessageWindow()
    OP_85(0xE)
    OP_85(0x10)
    OP_85(0x11)
    OP_85(0xF)
    EventEnd(0x0)

    label("loc_8090")

    Return()

    # Function_37_79FE end

    def Function_38_8091(): pass

    label("Function_38_8091")

    EventBegin(0x0)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    OP_22(0x94, 0x1, 0x64)
    PlayEffect(0x4, 0x4, 0x1F, 0, 50, 2700, 180, 0, 0, 2500, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x1E, 0, 50, 2400, 180, 0, 0, 1600, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x1F, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x1E, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x18, 0x2)
    OP_71(0x18, 0x20)
    OP_71(0x18, 0x40)
    OP_6F(0x18, 301)
    OP_70(0x18, 0x168)
    OP_72(0x19, 0x2)
    OP_71(0x19, 0x20)
    OP_71(0x19, 0x40)
    OP_6F(0x19, 301)
    OP_70(0x19, 0x168)
    ClearChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x20)
    OP_89(0x1D, 89820, -2850, 52390, 270)
    SetChrPos(0x101, 98260, -1000, 52020, 270)
    SetChrPos(0x102, 100490, -1000, 51980, 90)
    SetChrPos(0x105, 99510, -1000, 52230, 270)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x101, 17)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0x105, 19)
    OP_A1(0x1F, 0x18)
    OP_A1(0x1E, 0x19)
    SetChrPos(0x1F, 90000, -3000, 53000, 90)
    SetChrPos(0x1E, 100000, -3000, 52000, 90)
    FadeToBright(2000, 0)
    OP_6D(50010, 400, 40640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(336000, 0)
    OP_6E(371, 0)
    SetChrPos(0x11, 52500, 400, 59820, 90)
    SetChrPos(0xF, 51400, 400, 60600, 90)
    SetChrPos(0x10, 52190, 400, 58970, 90)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    def lambda_82F4():
        OP_6C(322000, 5500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_82F4)
    OP_6D(51480, 400, 59800, 4000)
    OP_44(0xF, 0xFF)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_44(0x10, 0xFF)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_44(0x11, 0xFF)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    StopSound(0x9470, 0x3D090, 0x2710)
    Sleep(700)
    OP_22(0x93, 0x0, 0x64)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x3FC)
    Sleep(300)

    ChrTalk(    #351 op#A op#5
        0x10,
        "#10A#3PWhoooaaaa!!\x05\x02",
    )

    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_83C4():
        OP_8E(0xFE, 0xC6A2, 0x0, 0x108EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_83C4)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_83F6():
        OP_8E(0xFE, 0xC6A2, 0x0, 0x108EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_83F6)

    ChrTalk(    #352 op#A op#5
        0x11,
        "#10A#4PEeeeeeekk!\x05\x02",
    )

    Sleep(100)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_843F():
        OP_8E(0xFE, 0xC6A2, 0x0, 0x108EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_843F)

    def lambda_845A():
        OP_6D(51130, 400, 52010, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_845A)

    def lambda_8472():
        OP_67(0, 6250, -10000, 8600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8472)

    def lambda_848A():
        OP_6C(270000, 8600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_848A)

    def lambda_849A():
        OP_6E(729, 8600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_849A)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0xF)
    OP_63(0x11)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    Sleep(1800)

    def lambda_84E0():
        OP_8F(0xFE, 0xFFFFE9EE, 0x190, 0xCF08, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_84E0)
    Sleep(1800)
    OP_22(0xD9, 0x0, 0x64)

    def lambda_8505():
        OP_8F(0xFE, 0xFFFFE9EE, 0x190, 0xCADA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8505)
    Sleep(3000)

    def lambda_8525():
        OP_6D(26670, -810, 52180, 3500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8525)

    def lambda_853D():
        OP_6B(1750, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_853D)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_8091 end

    def Function_39_8564(): pass

    label("Function_39_8564")

    OP_A2(0x500)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(51000, 400, 61600, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(21000, 0)
    FadeToBright(2000, 0)
    SetChrPos(0xC, 62600, 6000, 68000, 0)
    SetChrPos(0x105, 50500, 0, 67700, 0)
    SetChrPos(0x101, 50500, 0, 67700, 0)
    SetChrPos(0x102, 50500, 0, 67700, 0)

    def lambda_85F5():
        OP_8E(0xFE, 0xC6D4, 0x190, 0xCB84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85F5)

    def lambda_8610():
        OP_6D(50900, 400, 52100, 4800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8610)

    def lambda_8628():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8628)
    Sleep(500)

    def lambda_863D():
        OP_8E(0xFE, 0xCB84, 0x190, 0xCE40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_863D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #353
        0x101,
        (
            "#501F#3PGuess she's not here yet...\x02\x03",

            "Did we get here that early?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #354
        0x102,
        (
            "#010FCould be. Want to kill some\x01",
            "time at the tavern?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #355
        0x101,
        (
            "#001F#3PNah... It's nice out, so I think\x01",
            "I'd rather just wait here.\x02\x03",

            "I doubt I could ever get tired\x01",
            "of the view of the river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        "#019FYeah, no kidding.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    def lambda_8791():
        OP_6D(49130, 400, 51740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8791)

    def lambda_87A9():
        OP_8E(0xFE, 0xC15C, 0x190, 0xC800, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87A9)
    OP_8C(0x102, 270, 400)

    def lambda_87CB():
        OP_8E(0xFE, 0xC15C, 0x190, 0xCC4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87CB)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 0)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #357
        0x101,
        (
            "#006F#4PI even get the feeling that Ruan's\x01",
            "finally back to normal.\x02\x03",

            "Pretty amazing considering the uproar\x01",
            "after Mayor Dalmore's arrest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x102,
        (
            "#015F#3PWell, a seated mayor has never\x01",
            "been arrested before.\x02\x03",

            "Try to imagine if Mayor Klaus\x01",
            "was arrested in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        (
            "#004F#4PYeah...that would be a real shock...\x02\x03",

            "#000FBut when I think of it that way,\x01",
            "the people of Ruan almost seem...\x01",
            "Cold.\x02\x03",

            "I mean, they were clearly surprised by\x01",
            "what happened...but not a single person\x01",
            "was truly shocked, far as I can tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x102,
        (
            "#010F#3PWell, you have to remember, the mayor\x01",
            "of Ruan has always been selected by\x01",
            "bloodline alone.\x02\x03",

            "He wasn't elected to his position by\x01",
            "the Ruanians. And that probably makes\x01",
            "all the difference in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#007F#4PYeah, that's true. The people of Rolent\x01",
            "appointed Klaus mayor because they liked\x01",
            "him, and trusted him...\x02\x03",

            "Dalmore's getting what he deserves,\x01",
            "but I still feel kinda bad for him.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x105, 300)

    ChrTalk(    #362
        0x102,
        "#010F#3PHey, look who's here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #363
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    def lambda_8BE4():
        OP_6D(51540, 400, 57590, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BE4)

    def lambda_8BFC():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8BFC)
    ClearChrFlags(0xC, 0x80)
    OP_22(0x8C, 0x0, 0x64)
    OP_8E(0xC, 0xD28C, 0x514, 0xDEA8, 0xFA0, 0x0)
    SetChrFlags(0xC, 0x20)

    def lambda_8C2F():

        label("loc_8C2F")

        OP_99(0xFE, 0x0, 0x7, 0x1388)
        OP_48()
        Jump("loc_8C2F")

    QueueWorkItem2(0xC, 2, lambda_8C2F)
    TurnDirection(0x102, 0xC, 400)
    TurnDirection(0x101, 0xC, 400)

    def lambda_8C50():
        OP_8C(0xFE, 270, 100)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_8C50)
    OP_8F(0xC, 0xD228, 0x44C, 0xDEA8, 0x1F4, 0x0)
    OP_44(0xC, 0x2)
    SetChrChipByIndex(0xC, 16)
    SetChrSubChip(0xC, 3)
    Sleep(100)
    SetChrSubChip(0xC, 4)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xC, 0x20)

    ChrTalk(    #364
        0x101,
        "#001FOh, Sieg!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 1)
    Sleep(300)

    ChrTalk(    #365
        0xC,
        "#310F#3PScreeeee!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #366
        0x105,
        "Girl's Voice",
        "#4PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x105, 0xC738, 0x190, 0xE164, 0x1388, 0x0)

    ChrTalk(    #367
        0x105,
        (
            "#045F#3PHey...! *huff* *huff*\x02\x03",

            "I'm sorry... *huff* ...that I'm late.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D52():
        OP_8E(0xFE, 0xC4E0, 0x190, 0xDB24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D52)
    Sleep(200)

    def lambda_8D72():
        OP_8E(0xFE, 0xC864, 0x190, 0xDA5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D72)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #368
        0x102,
        (
            "#010F#6PNo problem. We just got here,\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#004FDon't tell us you ran all the\x01",
            "way here...\x02\x03",

            "You really didn't need to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x105,
        (
            "#048F#3PI couldn't let you two go without\x01",
            "seeing you off.\x02\x03",

            "Thank you very much for\x01",
            "contacting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        (
            "#008FKloe...I keep telling you,\x01",
            "you don't have to thank us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #372
        0x101,
        (
            "#001FYou too, Sieg.\x01",
            "Thanks for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xC,
        "#311F#4PScreeee! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x102,
        "#019F#6PHa ha. Well, then...shall we be off?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #375
        0x101,
        (
            "#006FOkay...\x02\x03",

            "We need to use the south exit\x01",
            "to reach Zeiss, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9061")

    ChrTalk(    #376
        0x105,
        (
            "#040F#3PYes. There's a checkpoint on\x01",
            "the southern road there called\x01",
            "Air-Letten.\x02\x03",

            "You can see a famous waterfall\x01",
            "from that point, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#501FHey, that might be fun.\x02\x03",

            "#001FLet's go check it out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FE")

    label("loc_9061")


    ChrTalk(    #378
        0x105,
        (
            "#040F#3PYes, on the southern road is a\x01",
            "checkpoint called Air-Letten.\x02\x03",

            "You can set out for Zeiss from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x101,
        (
            "#006FRoger that.\x02\x03",

            "#001FOkay, let's go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FE")


    ChrTalk(    #380
        0xC,
        "#311F#4PScreeee!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    SetChrSubChip(0xC, 4)
    Sleep(100)
    SetChrSubChip(0xC, 3)
    Sleep(100)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_9144():
        OP_8E(0xFE, 0xC864, 0x1770, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9144)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    SetChrFlags(0xC, 0x80)
    Return()

    # Function_39_8564 end

    def Function_40_916A(): pass

    label("Function_40_916A")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9229")
    OP_A2(0xA)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(    #381
        0x136,
        (
            "#040FUm, I think you might want to\x01",
            "hurry and get a room.\x02\x03",

            "This is tourist season, so they\x01",
            "tend to fill up pretty quickly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9203():
        TurnDirection(0x102, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9203)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #382
        0x101,
        "#000FOh, okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_92AB")

    label("loc_9229")

    TurnDirection(0x136, 0x0, 400)

    ChrTalk(    #383
        0x136,
        (
            "#040FI think you might want to hurry\x01",
            "and get a room.\x02\x03",

            "This is tourist season, so they\x01",
            "tend to fill up pretty quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92AB")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_40_916A end

    def Function_41_92C7(): pass

    label("Function_41_92C7")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D8")
    OP_A2(0xA)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #384
        0x102,
        (
            "#010FIt's already evening, Estelle. We shouldn't\x01",
            "be going out too far.\x02\x03",

            "Let's put our bags in the room first and get\x01",
            "settled. We can walk around after that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #385
        0x101,
        (
            "#000FOh, you've got a point.\x02\x03",

            "We're on the top floor,\x01",
            "the penthouse, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9481")

    label("loc_93D8")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #386
        0x102,
        (
            "#010FIt's already evening, Estelle. We shouldn't\x01",
            "be going out too far.\x02\x03",

            "Let's put our bags in the room first and get\x01",
            "settled. We can walk around after that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9481")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_41_92C7 end

    def Function_42_949D(): pass

    label("Function_42_949D")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95ED")
    OP_A2(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9540")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #387
        0x102,
        (
            "#010FLet's stop by the guild before\x01",
            "we head out.\x02\x03",

            "Jean will probably have some\x01",
            "work for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #388
        0x101,
        "#000FYou're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_95EA")

    label("loc_9540")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #389
        0x101,
        "#000FOh...are we leaving already?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #390
        0x102,
        (
            "#010FNo, we need to stop by the guild\x01",
            "first.\x02\x03",

            "Jean will probably have some\x01",
            "work for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x101,
        "#006FYou're right.\x02",
    )

    CloseMessageWindow()

    label("loc_95EA")

    Jump("loc_9655")

    label("loc_95ED")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #392
        0x102,
        (
            "#010FLet's stop by the guild before we\x01",
            "head out.\x02\x03",

            "Jean will probably have some\x01",
            "work for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9655")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_42_949D end

    def Function_43_9671(): pass

    label("Function_43_9671")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9689")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_9690")

    label("loc_9689")

    TurnDirection(0x102, 0x0, 400)

    label("loc_9690")


    ChrTalk(    #393
        0x102,
        (
            "#010FLet's go back to the guild for\x01",
            "a second.\x02\x03",

            "They may want to know the results\x01",
            "of our investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_43_9671 end

    def Function_44_9718(): pass

    label("Function_44_9718")

    SetPlaceName(0x48)
    Return()

    # Function_44_9718 end

    def Function_45_971C(): pass

    label("Function_45_971C")

    SetPlaceName(0x4D)
    Return()

    # Function_45_971C end

    def Function_46_9720(): pass

    label("Function_46_9720")

    SetPlaceName(0x4C)
    Return()

    # Function_46_9720 end

    def Function_47_9724(): pass

    label("Function_47_9724")

    SetPlaceName(0x4A)
    Return()

    # Function_47_9724 end

    def Function_48_9728(): pass

    label("Function_48_9728")

    SetPlaceName(0x4E)
    Return()

    # Function_48_9728 end

    def Function_49_972C(): pass

    label("Function_49_972C")

    SetPlaceName(0x4B)
    Return()

    # Function_49_972C end

    def Function_50_9730(): pass

    label("Function_50_9730")

    SetPlaceName(0x49)
    Return()

    # Function_50_9730 end

    def Function_51_9734(): pass

    label("Function_51_9734")

    SetPlaceName(0x4F)
    Return()

    # Function_51_9734 end

    SaveToFile()

Try(main)
