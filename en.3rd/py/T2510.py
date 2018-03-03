from ED63RDScenarioHelper import *

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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Logic',                                # 9
        'Thelma',                               # 10
        'Hans',                                 # 11
        'Patrick',                              # 12
        'Freyja',                               # 13
        'Jill',                                 # 14
        'Rhody',                                # 15
        'Mickey',                               # 16
        'Ms. Wiola',                            # 17
        'Anton',                                # 18
        'Ricky',                                # 19
        'Roy',                                  # 20
        'Monika',                               # 21
        'Clara',                                # 22
        'Lechter',                              # 23
        'Leo',                                  # 24
        'Dean Collins',                         # 25
        'Mr. Ratio',                            # 26
        'Ms. Millia',                           # 27
        'Felicity',                             # 28
        'Reina',                                # 29
        'Dennis',                               # 30
        'Rigel',                                # 31
        'Lucy',                                 # 32
        'Kaden',                                # 33
        'Alice',                                # 34
        'Fauna',                                # 35
        'Visitor',                              # 36
        'Printout',                             # 37
        'Target Camera',                        # 38
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
        'ED6_DT07/CH01580 ._CH',             # 00
        'ED6_DT07/CH01590 ._CH',             # 01
        'ED6_DT07/CH01090 ._CH',             # 02
        'ED6_DT07/CH01360 ._CH',             # 03
        'ED6_DT07/CH01370 ._CH',             # 04
        'ED6_DT07/CH01080 ._CH',             # 05
        'ED6_DT07/CH02670 ._CH',             # 06
        'ED6_DT07/CH02680 ._CH',             # 07
        'ED6_DT07/CH02600 ._CH',             # 08
        'ED6_DT07/CH02603 ._CH',             # 09
        'ED6_DT07/CH02550 ._CH',             # 0A
        'ED6_DT07/CH02390 ._CH',             # 0B
        'ED6_DT07/CH01210 ._CH',             # 0C
        'ED6_DT07/CH02900 ._CH',             # 0D
        'ED6_DT07/CH02910 ._CH',             # 0E
        'ED6_DT07/CH01083 ._CH',             # 0F
        'ED6_DT07/CH01583 ._CH',             # 10
        'ED6_DT07/CH01363 ._CH',             # 11
        'ED6_DT07/CH01373 ._CH',             # 12
        'ED6_DT07/CH01593 ._CH',             # 13
        'ED6_DT07/CH01093 ._CH',             # 14
        'ED6_DT07/CH02393 ._CH',             # 15
        'ED6_DT07/CH02553 ._CH',             # 16
        'ED6_DT07/CH00043 ._CH',             # 17
        'ED6_DT26/CH20782 ._CH',             # 18
        'ED6_DT26/CH20783 ._CH',             # 19
        'ED6_DT26/CH20777 ._CH',             # 1A
        'ED6_DT26/CH20779 ._CH',             # 1B
        'ED6_DT26/CH20780 ._CH',             # 1C
        'ED6_DT26/CH20783 ._CH',             # 1D
        'ED6_DT07/CH01430 ._CH',             # 1E
        'ED6_DT07/CH01660 ._CH',             # 1F
        'ED6_DT07/CH02490 ._CH',             # 20
        'ED6_DT07/CH01663 ._CH',             # 21
        'ED6_DT07/CH01213 ._CH',             # 22
        'ED6_DT07/CH01433 ._CH',             # 23
        'ED6_DT07/CH02690 ._CH',             # 24
        'ED6_DT07/CH02700 ._CH',             # 25
        'ED6_DT07/CH01200 ._CH',             # 26
        'ED6_DT26/CH20278 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT07/CH01580P._CP',             # 00
        'ED6_DT07/CH01590P._CP',             # 01
        'ED6_DT07/CH01090P._CP',             # 02
        'ED6_DT07/CH01360P._CP',             # 03
        'ED6_DT07/CH01370P._CP',             # 04
        'ED6_DT07/CH01080P._CP',             # 05
        'ED6_DT07/CH02670P._CP',             # 06
        'ED6_DT07/CH02680P._CP',             # 07
        'ED6_DT07/CH02600P._CP',             # 08
        'ED6_DT07/CH02603P._CP',             # 09
        'ED6_DT07/CH02550P._CP',             # 0A
        'ED6_DT07/CH02390P._CP',             # 0B
        'ED6_DT07/CH01210P._CP',             # 0C
        'ED6_DT07/CH02900P._CP',             # 0D
        'ED6_DT07/CH02910P._CP',             # 0E
        'ED6_DT07/CH01083P._CP',             # 0F
        'ED6_DT07/CH01583P._CP',             # 10
        'ED6_DT07/CH01363P._CP',             # 11
        'ED6_DT07/CH01373P._CP',             # 12
        'ED6_DT07/CH01593P._CP',             # 13
        'ED6_DT07/CH01093P._CP',             # 14
        'ED6_DT07/CH02393P._CP',             # 15
        'ED6_DT07/CH02553P._CP',             # 16
        'ED6_DT07/CH00043P._CP',             # 17
        'ED6_DT26/CH20782P._CP',             # 18
        'ED6_DT26/CH20783P._CP',             # 19
        'ED6_DT26/CH20777P._CP',             # 1A
        'ED6_DT26/CH20779P._CP',             # 1B
        'ED6_DT26/CH20780P._CP',             # 1C
        'ED6_DT26/CH20783P._CP',             # 1D
        'ED6_DT07/CH01430P._CP',             # 1E
        'ED6_DT07/CH01660P._CP',             # 1F
        'ED6_DT07/CH02490P._CP',             # 20
        'ED6_DT07/CH01663P._CP',             # 21
        'ED6_DT07/CH01213P._CP',             # 22
        'ED6_DT07/CH01433P._CP',             # 23
        'ED6_DT07/CH02690P._CP',             # 24
        'ED6_DT07/CH02700P._CP',             # 25
        'ED6_DT07/CH01200P._CP',             # 26
        'ED6_DT26/CH20278P._CP',             # 27
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        TalkScenaIndex      = 17,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 86720,
        Z                   = 0,
        Y                   = 4320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 95280,
        Z                   = 250,
        Y                   = 30600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48590,
        Z                   = 0,
        Y                   = 31310,
        Direction           = 90,
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
        X                   = 49940,
        Z                   = 0,
        Y                   = 31300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 37390,
        Z                   = 0,
        Y                   = 950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 2150,
        Z                   = 0,
        Y                   = 4260,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 41720,
        Z                   = 0,
        Y                   = 39400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3930,
        Z                   = 0,
        Y                   = 5390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        X                   = 41200,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 131111,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
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
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51030,
        TriggerZ            = 0,
        TriggerY            = 2090,
        TriggerRange        = 400,
        ActorX              = 51030,
        ActorZ              = 800,
        ActorY              = 2090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36970,
        TriggerZ            = 0,
        TriggerY            = 2040,
        TriggerRange        = 800,
        ActorX              = 36970,
        ActorZ              = 1000,
        ActorY              = 2040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 113820,
        TriggerZ            = 0,
        TriggerY            = 500,
        TriggerRange        = 800,
        ActorX              = 113820,
        ActorZ              = 600,
        ActorY              = 500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 49,
        Unknown_22          = 0,
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
        TalkFunctionIndex   = 11,
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
        TalkFunctionIndex   = 50,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_682",          # 00, 0
        "Function_1_AF5",          # 01, 1
        "Function_2_BC2",          # 02, 2
        "Function_3_D3F",          # 03, 3
        "Function_4_D63",          # 04, 4
        "Function_5_D87",          # 05, 5
        "Function_6_1102",         # 06, 6
        "Function_7_14D1",         # 07, 7
        "Function_8_24E9",         # 08, 8
        "Function_9_2BE7",         # 09, 9
        "Function_10_30D0",        # 0A, 10
        "Function_11_34FF",        # 0B, 11
        "Function_12_3B22",        # 0C, 12
        "Function_13_3E02",        # 0D, 13
        "Function_14_4296",        # 0E, 14
        "Function_15_46F9",        # 0F, 15
        "Function_16_5070",        # 10, 16
        "Function_17_52F7",        # 11, 17
        "Function_18_5467",        # 12, 18
        "Function_19_562C",        # 13, 19
        "Function_20_57F7",        # 14, 20
        "Function_21_5A60",        # 15, 21
        "Function_22_5B92",        # 16, 22
        "Function_23_5E94",        # 17, 23
        "Function_24_6008",        # 18, 24
        "Function_25_6178",        # 19, 25
        "Function_26_70AC",        # 1A, 26
        "Function_27_712D",        # 1B, 27
        "Function_28_7183",        # 1C, 28
        "Function_29_7222",        # 1D, 29
        "Function_30_7FE7",        # 1E, 30
        "Function_31_8119",        # 1F, 31
        "Function_32_8227",        # 20, 32
        "Function_33_82C8",        # 21, 33
        "Function_34_8389",        # 22, 34
        "Function_35_846F",        # 23, 35
        "Function_36_8530",        # 24, 36
        "Function_37_8AA4",        # 25, 37
        "Function_38_8AE5",        # 26, 38
        "Function_39_901E",        # 27, 39
        "Function_40_A468",        # 28, 40
        "Function_41_A4CE",        # 29, 41
        "Function_42_A51F",        # 2A, 42
        "Function_43_A53A",        # 2B, 43
        "Function_44_A59B",        # 2C, 44
        "Function_45_A5FC",        # 2D, 45
        "Function_46_A64C",        # 2E, 46
        "Function_47_AC78",        # 2F, 47
        "Function_48_AD12",        # 30, 48
        "Function_49_AF41",        # 31, 49
        "Function_50_B02D",        # 32, 50
    )


    def Function_0_682(): pass

    label("Function_0_682")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_72D")
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 83020, 0, 4760, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 52560, 0, 1300, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 53740, 0, 1300, 270)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 42100, 0, 32000, 0)
    OP_43(0x1B, 0x0, 0x0, 0x3)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 85660, 0, 34110, 270)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 87380, 0, 35160, 270)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_A7A")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_759")
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 40990, 0, 5500, 0)
    Jump("loc_78A")

    label("loc_759")

    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x10)
    SetChrPos(0x1E, 43110, 0, 4420, 270)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2B, 41740, 0, 4420, 90)

    label("loc_78A")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 87640, 200, 2820, 270)
    SetChrFlags(0x21, 0x10)
    SetChrFlags(0x21, 0x4)
    OP_4A(0x21, 255)
    SetChrChipByIndex(0x21, 33)
    SetChrSubChip(0x21, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45220, 0, 33500, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 36840, 0, 1520, 0)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 93410, 0, 33000, 180)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 92900, 0, 34100, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 83550, 0, -1490, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 93410, 0, 31740, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -2750, 100, 4100, 90)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x16, 0x4)
    OP_4A(0x16, 255)
    SetChrChipByIndex(0x16, 17)
    SetChrSubChip(0x16, 0)
    Jump("loc_A7A")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_945")
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 89300, 0, 2340, 90)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 85410, 0, 4250, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 36770, 0, 1580, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 5080, 250, 30340, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3730, 0, 32759, 180)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 85660, 0, 30050, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x14, -3880, 0, 31380, 0)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 4800, 250, -1060, 90)
    Jump("loc_A7A")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_A7A")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7140, 0, 34280, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -7140, 0, 33020, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A")
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x1B, 0x10)

    label("loc_98A")

    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 84100, 100, 30000, 90)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    OP_4A(0x13, 255)
    SetChrChipByIndex(0x13, 16)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x2C, 1300, 180, 34060, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x800)
    OP_51(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7A")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 84400, 200, 1000, 90)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x4)
    OP_4A(0x18, 255)
    SetChrChipByIndex(0x18, 34)
    SetChrSubChip(0x18, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 87690, 0, 4200, 270)

    label("loc_A7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_AA9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 39)

    label("loc_AA9")

    Jump("loc_AF4")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_AD2")
    OP_A3(0x2504)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 38)

    label("loc_AD2")

    Jump("loc_AF4")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_AEB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 29)
    Jump("loc_AF4")

    label("loc_AEB")

    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_AF4")

    Return()

    # Function_0_682 end

    def Function_1_AF5(): pass

    label("Function_1_AF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B14")
    OP_B1("T2510_y")
    Jump("loc_B1D")

    label("loc_B14")

    OP_B1("T2510_n")

    label("loc_B1D")

    OP_A3(0x0)
    Jump("loc_B2C")

    label("loc_B23")

    OP_B1("T2510_n")

    label("loc_B2C")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_B5B")
    OP_65(0x2, 0x1)
    OP_64(0x4, 0x1)

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7C")
    OP_63(0x1E)
    OP_62(0x1E, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    label("loc_B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B97")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 3)), scpexpr(EXPR_END)), "loc_B97")
    OP_65(0x3, 0x1)

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    OP_71(0x1004, 0x0)
    ExitThread()
    OP_64(0x1, 0x1)
    Jump("loc_BC1")

    label("loc_BB7")

    OP_72(0x1004, 0x0)
    ExitThread()
    OP_65(0x1, 0x1)

    label("loc_BC1")

    Return()

    # Function_1_AF5 end

    def Function_2_BC2(): pass

    label("Function_2_BC2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D29")

    label("loc_BE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C00")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D29")

    label("loc_C00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C19")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D29")

    label("loc_C19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C32")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D29")

    label("loc_C32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D29")

    label("loc_C4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C64")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D29")

    label("loc_C64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D29")

    label("loc_C7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D29")

    label("loc_C96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D29")

    label("loc_CAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D29")

    label("loc_CC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE1")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D29")

    label("loc_CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFA")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D29")

    label("loc_CFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D13")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D29")

    label("loc_D13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D29")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D29")

    label("loc_D3E")

    Return()

    # Function_2_BC2 end

    def Function_3_D3F(): pass

    label("Function_3_D3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D62")
    OP_8D(0xFE, 42880, 32770, 40420, 30320, 2000)
    Jump("Function_3_D3F")

    label("loc_D62")

    Return()

    # Function_3_D3F end

    def Function_4_D63(): pass

    label("Function_4_D63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D86")
    OP_8D(0xFE, 4950, 5500, 2160, 1980, 2000)
    Jump("Function_4_D63")

    label("loc_D86")

    Return()

    # Function_4_D63 end

    def Function_5_D87(): pass

    label("Function_5_D87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_D94")
    Jump("loc_10FE")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_D9E")
    Jump("loc_10FE")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_E22")

    ChrTalk(    #0
        0xFE,
        "I see practice is starting tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "So I'll bet everyone'll want to rest up\x01",
            "today while they still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_E22")


    ChrTalk(    #2
        0xFE,
        "I've decided to join the Archery Club!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I have some experience with the sport,\x01",
            "you see. I think it'd be good to go back\x01",
            "to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_EAD")

    Jump("loc_10FE")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_FAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_F31")

    ChrTalk(    #4
        0xFE,
        (
            "What? You're looking for the Student Council \x01",
            "president?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "I'm sorry. I haven't seen him, I'm afraid...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA9")

    label("loc_F31")


    ChrTalk(    #6
        0xFE,
        (
            "I'm on cleaning duty today, so I'm hard at\x01",
            "work right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Time to get this blackboard as clean as\x01",
            "can be!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_FA9")

    Jump("loc_10FE")

    label("loc_FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_10FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_END)), "loc_10FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1054")

    ChrTalk(    #8
        0xFE,
        "Did you know that Roy's from Calvard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "As someone interested in social studies,\x01",
            "I find what he has to say about the place\x01",
            "fascinating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F7")

    label("loc_1054")


    ChrTalk(    #10
        0xFE,
        "Did you know that Roy's from Calvard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "So he knows all kinds of interesting facts\x01",
            "about the country that I wouldn't have the\x01",
            "chance to hear otherwise.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_10F7")

    Jump("loc_10FE")

    label("loc_10FA")

    Call(0, 36)

    label("loc_10FE")

    TalkEnd(0xFE)
    Return()

    # Function_5_D87 end

    def Function_6_1102(): pass

    label("Function_6_1102")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_12C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_121C")

    ChrTalk(    #12
        0xFE,
        (
            "The captain of our club doesn't exactly get\x01",
            "along very well with Lechter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Apparently they were rivals for the position of\x01",
            "president last year, and we all know how THAT\x01",
            "went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "...I still feel like Rigel would've been far more\x01",
            "suited for it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C2")

    label("loc_121C")


    ChrTalk(    #15
        0x105,
        (
            "#042FOh, Roy.\x02\x03",

            "You haven't seen Lechter around here,\x01",
            "have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Lechter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "I'm afraid not, no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        (
            "#047FI see...\x02\x03",

            "#040FSorry for troubling you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_12C2")

    Jump("loc_14CD")

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_12CF")
    Jump("loc_14CD")

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_12D9")
    Jump("loc_14CD")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_12E3")
    Jump("loc_14CD")

    label("loc_12E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_END)), "loc_14C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(    #19
        0xFE,
        (
            "I should probably be thinking about heading\x01",
            "over to club practice, myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I think everyone's about ready to start.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C6")

    label("loc_1379")


    ChrTalk(    #21
        0xFE,
        (
            "I can't tell you exactly where all the other\x01",
            "social studies students could have gone,\x01",
            "but, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "...it's about time for club activities to start.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I think you're fairly likely to find the ones\x01",
            "who've joined clubs there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#542FYou're probably right.\x02\x03",

            "#543FThank you for the advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "O-Oh, it was nothing...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_14C6")

    Jump("loc_14CD")

    label("loc_14C9")

    Call(0, 36)

    label("loc_14CD")

    TalkEnd(0xFE)
    Return()

    # Function_6_1102 end

    def Function_7_14D1(): pass

    label("Function_7_14D1")

    TalkBegin(0x20)
    ClearChrFlags(0x20, 0x10)
    TurnDirection(0x20, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1501")
    SetChrSubChip(0x20, 1)
    Jump("loc_1527")

    label("loc_1501")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1522")
    SetChrSubChip(0x20, 2)
    Jump("loc_1527")

    label("loc_1522")

    SetChrSubChip(0x20, 0)

    label("loc_1527")

    OP_8C(0x20, 180, 0)
    SetChrFlags(0x20, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 4)), scpexpr(EXPR_END)), "loc_164A")

    ChrTalk(    #26
        0x20,
        (
            "#780FLechter often comes to this room and lies down\x01",
            "on the sofa over there.\x02\x03",

            "Haha. He really seems to enjoy the atmosphere\x01",
            "of this academy, from what I've seen.\x02\x03",

            "Regardless of how his behavior is on the outside,\x01",
            "I truly believe he's enjoying his time here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA2")

    label("loc_164A")


    ChrTalk(    #27
        0x20,
        "#780FOh, dear. Are you looking for Lechter again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#040FY-Yes...\x02\x03",

            "#045FI'm afraid so.\x02\x03",

            "Tomorrow's the general meeting of the Student \x01",
            "Council, but he's run away and we can't find him.\x02\x03",

            "Which is a problem, as we don't have all of the\x01",
            "necessary documents to conduct it as it stands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x20,
        "#781FHaha. He's a born troublemaker, that one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x105,
        (
            "#040FSir, umm...\x02\x03",

            "If you don't mind me saying, I'm a little surprised\x01",
            "by just how much you seem to trust him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x20,
        (
            "#780F...I suppose you would be.\x02\x03",

            "#783FStill, he knows exactly what he's doing.\x02\x03",

            "He knows exactly what the potential of his\x01",
            "actions are, too, and fully accepts them.\x02\x03",

            "#780FHe still acts however he likes...\x02\x03",

            "...but he's more than willing to face the\x01",
            "consequences of his actions.\x02\x03",

            "#781FHaha. I'm not sure 'trust' is the most appropriate\x01",
            "word for what I have for him, but at the very least,\x01",
            "I think he makes for an interesting president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        (
            "#047F...Admittedly, he does do his work properly\x01",
            "when we do manage to capture him.\x02\x03",

            "And I know from experience that it may\x01",
            "seem like he never takes anything seriously,\x01",
            "but that's absolutely not the case.\x02\x03",

            "#042FI just wish he'd actually do his work seriously\x01",
            "from the beginning instead of requiring us to \x01",
            "capture him before he does it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x20,
        (
            "#780FQuite understandable.\x02\x03",

            "Perhaps you should tell him that yourself\x01",
            "next time you see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#041FI think I will.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F74)

    label("loc_1BA2")

    Jump("loc_24E0")

    label("loc_1BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1BAF")
    Jump("loc_24E0")

    label("loc_1BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_1D4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C56")

    ChrTalk(    #35
        0x20,
        (
            "#780FTo reach Ruan, you'll need to go through\x01",
            "the forest outside the grounds and follow\x01",
            "the highway to the south.\x02\x03",

            "Be careful on the way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D49")

    label("loc_1C56")


    ChrTalk(    #36
        0x20,
        (
            "#780FBeing cooped up inside the academy grounds\x01",
            "must get quite boring at times.\x02\x03",

            "You've got the opportunity to leave them\x01",
            "and step outside. Why not use it to have a\x01",
            "nice, relaxing walk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        "#045FAhaha... Thank you, sir. Maybe I will.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1D49")

    Jump("loc_1D50")

    label("loc_1D4C")

    Call(0, 46)

    label("loc_1D50")

    Jump("loc_24E0")

    label("loc_1D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_212A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 3)), scpexpr(EXPR_END)), "loc_1DF1")

    ChrTalk(    #38
        0x20,
        (
            "#780FLechter was sleeping on that sofa until not long\x01",
            "ago, but as you can see, he's gone now.\x02\x03",

            "He was busy reading a book of some sort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2127")

    label("loc_1DF1")


    ChrTalk(    #39
        0x13B,
        (
            "#647FExcuse me, sir.\x02\x03",

            "You wouldn't have happened to see our president\x01",
            "anywhere, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        (
            "#045FWe're having a little bit of trouble finding him,\x01",
            "you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x20,
        (
            "#783FActually, I have.\x02\x03",

            "#780FHe was sleeping over on the sofa there until not\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x152, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x152,
        "#733FH-He was sleeping around in your office?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x105,
        "#047F(I swear...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13B,
        (
            "#646FUnbelievable... He doesn't even fear the dean...\x02\x03",

            "We're really going to have to take GOOD care\x01",
            "of him when we find him.\x02\x03",

            "#645FI'm terribly sorry for the trouble he caused you,\x01",
            "sir.\x02\x03",

            "We'll make sure that he answers for his crimes!\x01",
            "We promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x20,
        (
            "#781FHaha! Please, don't worry about it.\x02\x03",

            "He seems to have taken quite a liking to this\x01",
            "place. I'm rather used to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x105,
        "#044FI-I see...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F73)
    OP_65(0x3, 0x1)

    label("loc_2127")

    Jump("loc_24E0")

    label("loc_212A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_24E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 2)), scpexpr(EXPR_END)), "loc_2317")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_21E7")

    ChrTalk(    #47
        0x20,
        (
            "#780FThe Student Council room is on the second floor\x01",
            "of the clubhouse.\x02\x03",

            "If there's anything you need help with, I'm sure\x01",
            "they would be delighted to assist you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2314")

    label("loc_21E7")


    ChrTalk(    #48
        0x20,
        (
            "#780FI don't believe you've been given a full tour of\x01",
            "the academy facilities yet, come to think of it?\x02\x03",

            "If there is anything you need explaining to you,\x01",
            "be sure to ask the Student Council. I'm sure they\x01",
            "will be only too happy to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x105,
        (
            "#040FThank you, sir.\x02\x03",

            "#543FI will bear that in mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2314")

    Jump("loc_24E0")

    label("loc_2317")


    ChrTalk(    #50
        0x20,
        (
            "#780FOh, hello there, Kloe.\x02\x03",

            "Are you finally starting to get used to life here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        (
            "#043FSir... Umm...\x02\x03",

            "#047FI want to thank you again for permitting me to\x01",
            "transfer here on such short notice.\x02\x03",

            "#049FI really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x20,
        (
            "#783F...Kloe.\x02\x03",

            "You undertook our official transfer student exam,\x01",
            "and you passed it.\x02\x03",

            "#780FYou needn't feel at all indebted to me or feel as\x01",
            "though you're being granted special treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        "#542FI... If you say so, sir. Thank you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F72)

    label("loc_24E0")

    SetChrSubChip(0x20, 0)
    TalkEnd(0x20)
    Return()

    # Function_7_14D1 end

    def Function_8_24E9(): pass

    label("Function_8_24E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_267F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_25AA")

    ChrTalk(    #54
        0xFE,
        (
            "I'm intending to try a new approach towards\x01",
            "teaching in tomorrow's lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Just using textbooks all the time is a little\x01",
            "boring, both for myself and the students.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_25AA")


    ChrTalk(    #56
        0xFE,
        (
            "I'm intending to try a new approach towards\x01",
            "teaching in tomorrow's lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I haven't decided what to go with, however.\x01",
            "Maybe using short stories to test reading\x01",
            "comprehension would be a good idea?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_267C")

    Jump("loc_2BD3")

    label("loc_267F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_2689")
    Jump("loc_2BD3")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_272D")

    ChrTalk(    #58
        0xFE,
        (
            "You usually find Ms. Millia excitedly grading\x01",
            "papers after exams end, but there's no sign\x01",
            "of her at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "I wonder where she went?\x02",
    )

    CloseMessageWindow()
    Jump("loc_286A")

    label("loc_272D")


    ChrTalk(    #60
        0xFE,
        (
            "Well, the exams fortunately ended without any\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "That marks the first major examination period\x01",
            "for you first-year students...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "...but you'll get used to them. You've got plenty\x01",
            "more to look forward to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "So don't beat yourself up too much if this one\x01",
            "didn't go quite as planned. It happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_286A")

    Jump("loc_2BD3")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2949")

    ChrTalk(    #64
        0xFE,
        (
            "Lechter seems to enjoy teasing Ms. Millia far\x01",
            "too much. He makes a hobby out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "You'd think she would've gotten used to it and\x01",
            "stop giving him the reactions he wants by now,\x01",
            "but sadly not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A38")

    label("loc_2949")


    ChrTalk(    #66
        0xFE,
        "What? You're trying to find Lechter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "He was there sitting in Ms. Millia's seat till\x01",
            "not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "He was reading some book,\x01",
            "but I didn't see the title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I was going to call out to him, but he vanished\x01",
            "before I could.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2A38")

    Jump("loc_2BD3")

    label("loc_2A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B22")

    ChrTalk(    #70
        0xFE,
        (
            "I've been asked to be the Music Club's\x01",
            "adviser, which is fine and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "...but I'm totally tone-deaf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I'm not sure why anyone would want me, of all\x01",
            "people, to be the adviser for a club like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD3")

    label("loc_2B22")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #73
        0xFE,
        "You want me to be the Music Club's adviser?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Well, I've certainly got no problem with that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "...but I know next to nothing about music and\x01",
            "instruments.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2BD3")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE6")
    OP_4A(0x21, 255)

    label("loc_2BE6")

    Return()

    # Function_8_24E9 end

    def Function_9_2BE7(): pass

    label("Function_9_2BE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(    #76
        0xFE,
        (
            "How can his grades be so good when he never\x01",
            "acts like he gives a flyin' hoot about anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I wish I could make the exams much harder just\x01",
            "so I could see him suffer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "But if I did that, all the other students would\x01",
            "suffer, too... Decisions, decisions...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB2")

    label("loc_2D08")


    ChrTalk(    #79
        0xFE,
        (
            "Lechter became president instead of all the\x01",
            "other much more fitting candidates, and I still\x01",
            "can't bring myself to accept that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "It's just not right! Rrrgh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2DB2")

    Jump("loc_30CC")

    label("loc_2DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_2DBF")
    Jump("loc_30CC")

    label("loc_2DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2DC9")
    Jump("loc_30CC")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2E43")

    ChrTalk(    #81
        0xFE,
        "He just wanted to skip class, didn't he?\x02",
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0xFE,
        "He is truly unbelievable!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F96")

    label("loc_2E43")


    ChrTalk(    #83
        0xFE,
        (
            "Lechter actually showed up to class today!\x01",
            "You don't understand how rare that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "But he was being such a little butthead that\x01",
            "I made him go stand in the corridor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "You know what makes the situation even worse,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "Mr. Ratio says he was sitting in MY chair!\x02",
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #87
        0xFE,
        "I cannot BELIEVE him!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2F96")

    Jump("loc_30CC")

    label("loc_2F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_30CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3049")

    ChrTalk(    #88
        0xFE,
        (
            "The social studies schedule isn't finished yet,\x01",
            "though. That's Ms. Wiola's territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "She somehow manages to finish her schedule\x01",
            "last a lot. A. Lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_3049")


    ChrTalk(    #90
        0xFE,
        "Next month's schedule is all ready to go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I'll write it up here, so make sure you all\x01",
            "come and check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Got it?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_30CC")

    TalkEnd(0xFE)
    Return()

    # Function_9_2BE7 end

    def Function_10_30D0(): pass

    label("Function_10_30D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_32E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3212")

    ChrTalk(    #93
        0xFE,
        (
            "If there's one thing Lechter is bizarrely good at,\x01",
            "it's speeches. Every time he starts one, I can't\x01",
            "help but be enraptured by it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "It's weird how most of the time he messes around,\x01",
            "but at times like those, everything he says makes\x01",
            "perfect sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Maybe he'd actually be a good politician.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32E2")

    label("loc_3212")

    OP_8C(0xFE, 270, 0)

    ChrTalk(    #96
        0xFE,
        "Come on, now, Millia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "The only two candidates running were Lechter and\x01",
            "Rigel, and Rigel was off on the actual day due to\x01",
            "stomach pains!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "It couldn't have really ended any other way.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_32E2")

    Jump("loc_34EB")

    label("loc_32E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_32EF")
    Jump("loc_34EB")

    label("loc_32EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_32F9")
    Jump("loc_34EB")

    label("loc_32F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3402")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3369")

    ChrTalk(    #99
        0xFE,
        (
            "Wait. His name rings a bell, actually...\x01",
            "Maybe I did?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "I'm really not sure, though...\x02",
    )

    CloseMessageWindow()
    Jump("loc_33FF")

    label("loc_3369")


    ChrTalk(    #101
        0x105,
        (
            "#040FUmm... Excuse me?\x02\x03",

            "You wouldn't have happened to see Lechter\x01",
            "around here, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "Hmm? Lechter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "I don't think I have, no...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_33FF")

    Jump("loc_34EB")

    label("loc_3402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_34EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_347B")

    ChrTalk(    #104
        0xFE,
        "Oh, wait. I'm actually an hour short.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Ugh... I never was any good at these kinds of\x01",
            "things...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EB")

    label("loc_347B")


    ChrTalk(    #106
        0xFE,
        "What's wrong with this schedule, anyway?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "It looks great to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x105,
        "#047F(She seems very busy...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_34EB")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34FE")
    OP_4A(0x18, 255)

    label("loc_34FE")

    Return()

    # Function_10_30D0 end

    def Function_11_34FF(): pass

    label("Function_11_34FF")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_350C")
    Jump("loc_3B1E")

    label("loc_350C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3516")
    Jump("loc_3B1E")

    label("loc_3516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_36C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_35A8")
    OP_8C(0x2A, 180, 0)

    ChrTalk(    #109
        0x2A,
        (
            "Why not take a look through this pamphlet,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x2A,
        (
            "I think you'll find it has a lot of useful \x01",
            "information in it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C0")

    label("loc_35A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3658")

    ChrTalk(    #111
        0x2A,
        (
            "We get quite a lot of visitors here at the\x01",
            "academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x2A,
        (
            "The Student Council president's rather good\x01",
            "at seeing to them, too. It takes quite a load \x01",
            "off my mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C0")

    label("loc_3658")


    ChrTalk(    #113
        0x2A,
        "We've got a visitor in the academy at the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x2A,
        "We get them more often than you'd think.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_36C0")

    Jump("loc_3B1E")

    label("loc_36C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_37EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_37B3")

    ChrTalk(    #115
        0x2A,
        (
            "The Student Council's vice president came\x01",
            "to ask me the same question not long ago,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x2A,
        (
            "She went up to the second floor rather\x01",
            "disappointed when I gave her the same\x01",
            "answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x2A,
        "Poor girl looked so tired...\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_37B3")


    ChrTalk(    #118
        0x2A,
        "Hmm? Lechter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x2A,
        "I haven't seen him today, no.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_37EC")

    Jump("loc_3B1E")

    label("loc_37EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 5)), scpexpr(EXPR_END)), "loc_393E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_38B3")

    ChrTalk(    #120
        0x2A,
        (
            "This year's Student Council president is mature\x01",
            "beyond his years, by the looks of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x2A,
        (
            "I've never seen a student like him in all my years\x01",
            "working at this academy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393B")

    label("loc_38B3")


    ChrTalk(    #122
        0x2A,
        (
            "I actually saw the current Student Council\x01",
            "president here not long ago, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x2A,
        (
            "Heehee. He was so mature for someone his\x01",
            "age!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_393B")

    Jump("loc_3B1E")

    label("loc_393E")


    ChrTalk(    #124
        0x2A,
        "Oh, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x2A,
        "How are you doing? Have you settled in here yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#044FWell...I'd like to think so, yes.\x02\x03",

            "#047FBy the way, thank you very much for your\x01",
            "help during the enrollment process.\x02\x03",

            "#542FThanks to you, I was able to begin my new life\x01",
            "here without any problems at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x2A,
        "I'm just glad to have been of assistance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x2A,
        (
            "If there's anything else you need help with,\x01",
            "you need only to ask. I'll do what I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        "#542FI'll bear that in mind. Thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F75)

    label("loc_3B1E")

    TalkEnd(0x2A)
    Return()

    # Function_11_34FF end

    def Function_12_3B22(): pass

    label("Function_12_3B22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3B2F")
    Jump("loc_3DFE")

    label("loc_3B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3B39")
    Jump("loc_3DFE")

    label("loc_3B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_3CC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3BCC")

    ChrTalk(    #130
        0xFE,
        (
            "If you're not aware, our exam results will \x01",
            "eventually be displayed on this very notice\x01",
            "board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Haha. I can hardly wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CBD")

    label("loc_3BCC")


    ChrTalk(    #132
        0xFE,
        "Hello, Kloe. How do you feel about the exams?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        (
            "#044FWell...\x02\x03",

            "#045F...I thought they were a little difficult,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Really? I'm rather confident in my performance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "I can hardly wait for the results to be issued!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3CBD")

    Jump("loc_3DFE")

    label("loc_3CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3DF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3D7A")

    ChrTalk(    #136
        0xFE,
        (
            "I prefer to devote myself fully to my studies\x01",
            "instead of having club activities stealing my\x01",
            "time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "She doesn't seem to want to take no for an\x01",
            "answer, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF4")

    label("loc_3D7A")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #138
        0xFE,
        (
            "I'm not really much of a club activities person,\x01",
            "you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "I prefer to devote my time to my studies.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3DF4")

    Jump("loc_3DFE")

    label("loc_3DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3DFE")

    label("loc_3DFE")

    TalkEnd(0xFE)
    Return()

    # Function_12_3B22 end

    def Function_13_3E02(): pass

    label("Function_13_3E02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3EEB")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #140
        0xFE,
        (
            "We'll technically be on vacation, so there's\x01",
            "no reason to start practice too early in the\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "So I can start a bit later, and then move lunch\x01",
            "time back a little, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "La la laaa... ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FBB")

    label("loc_3EEB")


    ChrTalk(    #143
        0xFE,
        (
            "I've drawn up a plan for our club activities\x01",
            "during the holidays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "It can be a pain at times, but this position is\x01",
            "turning out to be a lot more fun than I expected\x01",
            "it to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "La la laaa... ♪\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3FBB")

    Jump("loc_4292")

    label("loc_3FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3FC8")
    Jump("loc_4292")

    label("loc_3FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_406E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_401B")

    ChrTalk(    #146
        0xFE,
        (
            "*sigh* I wouldn't even be doing this job if not\x01",
            "for Reina...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_406B")

    label("loc_401B")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #147
        0xFE,
        "Y-Yes. That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "So I just have to fill this out, then?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_406B")

    Jump("loc_4292")

    label("loc_406E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_4078")
    Jump("loc_4292")

    label("loc_4078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_4292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 3)), scpexpr(EXPR_END)), "loc_41A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_40FD")

    ChrTalk(    #149
        0xFE,
        (
            "I've heard all kinds of rumors about how \x01",
            "smart you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "*sigh* I wish I could be more like you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A2")

    label("loc_40FD")


    ChrTalk(    #151
        0xFE,
        (
            "You're Kloe, right? I've heard all kinds of\x01",
            "rumors about how smart you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "My name is Felicity Baeren.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "It's a pleasure to make your acquaintance.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_41A2")

    Jump("loc_4292")

    label("loc_41A5")


    ChrTalk(    #154
        0x105,
        (
            "#542FExcuse me...\x02\x03",

            "You aren't a social studies student, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Sorry, but no. I'm a natural sciences student,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x105,
        (
            "#044F...Oh.\x02\x03",

            "(O-Oops.)\x02\x03",

            "#043FI-I see. Sorry for troubling you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x2F7B)

    label("loc_4292")

    TalkEnd(0xFE)
    Return()

    # Function_13_3E02 end

    def Function_14_4296(): pass

    label("Function_14_4296")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4326")

    ChrTalk(    #157
        0xFE,
        (
            "It's probably about time for Felicity to return\x01",
            "home for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "The holidays will be beginning soon, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4405")

    label("loc_4326")


    ChrTalk(    #159
        0xFE,
        (
            "She finally seems to have seriously developed\x01",
            "some enthusiasm for her new position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Now the exam results are all finally out, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "So it's probably about time for her to be \x01",
            "returning home for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_4405")

    Jump("loc_46F5")

    label("loc_4408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_4412")
    Jump("loc_46F5")

    label("loc_4412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_44FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4496")

    ChrTalk(    #162
        0xFE,
        (
            "This is Felicity's first major task since taking\x01",
            "over the club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "Heehee. Let's see how she fares with it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_44F7")

    label("loc_4496")


    ChrTalk(    #164
        0xFE,
        (
            "I see she's busy with club-related work right\x01",
            "off the bat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "Heehee. Just as planned.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_44F7")

    Jump("loc_46F5")

    label("loc_44FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_4504")
    Jump("loc_46F5")

    label("loc_4504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_46F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_45CF")

    ChrTalk(    #166
        0xFE,
        (
            "Felicity doesn't seem to have any interest in\x01",
            "becoming our club's new captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I'm not going to let that stop me, though.\x01",
            "I'm sure I can think of something to change\x01",
            "her mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F5")

    label("loc_45CF")


    ChrTalk(    #168
        0xFE,
        (
            "It's almost time for our club to decide on a\x01",
            "new captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Personally, I'm backing Felicity--naturally!--\x01",
            "but she doesn't seem to have any interest\x01",
            "in the position, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I'm not going to let that stop me, though.\x01",
            "I'm sure I can think of something to change\x01",
            "her mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_46F5")

    TalkEnd(0xFE)
    Return()

    # Function_14_4296 end

    def Function_15_46F9(): pass

    label("Function_15_46F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4706")
    Jump("loc_505C")

    label("loc_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_4710")
    Jump("loc_505C")

    label("loc_4710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_481E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_479B")

    ChrTalk(    #171
        0xFE,
        (
            "I came to ask Ms. Millia a question, but she's\x01",
            "not here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I suppose I'll just have to wait for her to come\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481B")

    label("loc_479B")


    ChrTalk(    #173
        0xFE,
        "Hey, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "What am I doing here? I wanted to ask\x01",
            "Ms. Millia a question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "She's not here at the moment, though.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_481B")

    Jump("loc_505C")

    label("loc_481E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_4E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 5)), scpexpr(EXPR_END)), "loc_49FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_4890")

    ChrTalk(    #176
        0xFE,
        (
            "I've always seen Lechter as something of an\x01",
            "oddball...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Maybe I'm wrong, though?\x02",
    )

    CloseMessageWindow()
    Jump("loc_49FC")

    label("loc_4890")


    ChrTalk(    #178
        0xFE,
        (
            "I've always seen Lechter as something of an\x01",
            "oddball...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "...but I guess if he's the president and not Leo,\x01",
            "he's actually the more capable one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x13B,
        "#645FNot...really, no. Definitely not. Uh-uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x152,
        (
            "#734FHonestly, just think of his presidency as one of\x01",
            "the school's seven mysteries. That's about the\x01",
            "only way it makes sense.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0xE)

    label("loc_49FC")

    Jump("loc_4E9A")

    label("loc_49FF")


    ChrTalk(    #182
        0x13B,
        (
            "#640FExcuse me?\x02\x03",

            "You wouldn't have happened to see the Student \x01",
            "Council president anywhere, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "Oh, you're looking for Leo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "He headed straight to the council room as soon\x01",
            "as class finished, isn't he there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x105,
        (
            "#045FOh, no...\x02\x03",

            "We're actually looking for Lechter...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #186
        0x152,
        (
            "#732FLechter's the president, not Leo.\x02\x03",

            "People do make that mistake a lot...\x02\x03",

            "#734F...but it's true. However impossible it sounds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "Wait. You're not pulling my leg?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "S-Sorry. My bad, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "All this time, I thought Leo was the president.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x152,
        (
            "#735F(I shouldn't be surprised there are still people\x01",
            "making that mistake...)\x02\x03",

            "(I've lost count of the amount of times I've had\x01",
            "to explain Lechter's our leader to people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x13B,
        (
            "#645F(No surprise people feel that way, either.)\x02\x03",

            "(I mean, Leo IS the one who does most of the\x01",
            "work... He might as well be the head honcho.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x105,
        "#047F(I thought so...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "Still, Lechter's the, um, slightly strange one,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "I don't see him around all that often, so I think\x01",
            "I'd notice him if he did pass me by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "I don't believe I've seen him today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x13B,
        "#645FO-Oh, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x152,
        "#734FSorry for troubling you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F7D)

    label("loc_4E9A")

    Jump("loc_505C")

    label("loc_4E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_505C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_4F13")

    ChrTalk(    #198
        0xFE,
        (
            "Leo's observations are always worth paying\x01",
            "attention to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "He really never stops amazing me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_505C")

    label("loc_4F13")


    ChrTalk(    #200
        0xFE,
        (
            "In my experience, Leo's observations are always \x01",
            "worth keeping a close eye on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "I can't believe he was able to work out the\x01",
            "properties of this material from so little data,\x01",
            "but that's just what he does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "He didn't rely on guesswork, either. His evidence\x01",
            "for his beliefs is sound, too. I really do look up to\x01",
            "him!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_505C")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_506F")
    OP_4A(0xFE, 255)

    label("loc_506F")

    Return()

    # Function_15_46F9 end

    def Function_16_5070(): pass

    label("Function_16_5070")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_507D")
    Jump("loc_52F3")

    label("loc_507D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_5087")
    Jump("loc_52F3")

    label("loc_5087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_5091")
    Jump("loc_52F3")

    label("loc_5091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5175")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_50CF")

    ChrTalk(    #203
        0xFE,
        "It'll be fun! Come on, what do you say?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5172")

    label("loc_50CF")


    ChrTalk(    #204
        0xFE,
        "It'll be fine, it'll be fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "It's not like joining a club suddenly makes your\x01",
            "grades worse! Loads of people join them, and\x01",
            "they don't suffer for it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_5172")

    Jump("loc_52F3")

    label("loc_5175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_52F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_51E2")

    ChrTalk(    #206
        0xFE,
        "All right! The Music Club is back in business. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Heehee. I'm all excited now! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_52F3")

    label("loc_51E2")


    ChrTalk(    #208
        0xFE,
        "Hey, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I decided I wanted to join the academy's \x01",
            "Music Club, but guess what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "It turns out that the club doesn't have any\x01",
            "members. In fact, it hasn't since last year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "So I have to rebuild it from scratch! That's why\x01",
            "I'm here talking to Mr. Ratio.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_52F3")

    TalkEnd(0xFE)
    Return()

    # Function_16_5070 end

    def Function_17_52F7(): pass

    label("Function_17_52F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_5304")
    Jump("loc_5453")

    label("loc_5304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_530E")
    Jump("loc_5453")

    label("loc_530E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_5442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_53B6")

    ChrTalk(    #212
        0xFE,
        (
            "Now that the exams are finally over, it's time to\x01",
            "make my feelings known to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "I can't let Hans get ahead of me in the race for\x01",
            "her heart!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_543F")

    label("loc_53B6")

    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #214
        0xFE,
        "D-Don't look! I'm in the process of writing a letter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "Who's it to? Duh! Lucy!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_543F")

    Jump("loc_5453")

    label("loc_5442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_544C")
    Jump("loc_5453")

    label("loc_544C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_5453")

    label("loc_5453")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5466")
    OP_4A(0xFE, 255)

    label("loc_5466")

    Return()

    # Function_17_52F7 end

    def Function_18_5467(): pass

    label("Function_18_5467")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_5474")
    Jump("loc_5628")

    label("loc_5474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_547E")
    Jump("loc_5628")

    label("loc_547E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_5617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_5500")

    ChrTalk(    #216
        0x1E,
        (
            "#1779FAh, you are here to have a look around the\x01",
            "school?\x02\x03",

            "Haha. Oh, that won't be a problem at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5614")

    label("loc_5500")


    ChrTalk(    #217
        0x1E,
        (
            "#1775FMy name is Lechter, and I currently serve as the\x01",
            "president of this academy's Student Council.\x02\x03",

            "#1779FAh, you are here to have a look around the school?\x02\x03",

            "Haha. Oh, that won't be a problem at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x105,
        (
            "#045F(Who is this person, and why does he look like\x01",
            "Lechter?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_5614")

    Jump("loc_5628")

    label("loc_5617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5621")
    Jump("loc_5628")

    label("loc_5621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_5628")

    label("loc_5628")

    TalkEnd(0xFE)
    Return()

    # Function_18_5467 end

    def Function_19_562C(): pass

    label("Function_19_562C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_5639")
    Jump("loc_57F3")

    label("loc_5639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_5643")
    Jump("loc_57F3")

    label("loc_5643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_57E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_56BC")

    ChrTalk(    #219
        0xFE,
        "Hmm... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "Oh, it's just that I'm actually thinking of\x01",
            "sending my son to this academy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DF")

    label("loc_56BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_5748")

    ChrTalk(    #221
        0xFE,
        "What a fine young man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "I can certainly see how he ended up the president\x01",
            "of such an esteemed academy's Student Council.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DF")

    label("loc_5748")


    ChrTalk(    #223
        0xFE,
        (
            "So this is the president of the academy's\x01",
            "Student Council.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "What a fine young man! How fitting for such an\x01",
            "esteemed academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x105,
        "#045F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_57DF")

    Jump("loc_57F3")

    label("loc_57E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_57EC")
    Jump("loc_57F3")

    label("loc_57EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_57F3")

    label("loc_57F3")

    TalkEnd(0xFE)
    Return()

    # Function_19_562C end

    def Function_20_57F7(): pass

    label("Function_20_57F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_582F")

    ChrTalk(    #226
        0x27,
        (
            "#1795F*sigh*...\x02\x03",

            "That idiot...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A5C")

    label("loc_582F")

    EventBegin(0x1)
    Fade(1000)
    OP_6D(42200, 0, 38800, 0)
    SetChrPos(0x105, 41600, 0, 38200, 0)
    SetChrPos(0x152, 42180, 0, 37500, 0)
    SetChrPos(0x13B, 41140, 0, 37100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #227
        0x27,
        (
            "#1793FHow did he manage to get away?\x02\x03",

            "I had him attached to me with handcuffs this time,\x01",
            "too... He shouldn't have been able to.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x152, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #228
        0x105,
        "#043FUmm... Lucy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x27,
        (
            "#1793FLechter can actually teleport, you know.\x02\x03",

            "There's no way I can keep him under control\x01",
            "anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x152,
        "#737F(L-Lucy! Don't give up!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x13B,
        (
            "#645F(Being forced to deal with him all the time\x01",
            "seems to be finally making her crack...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x13)
    EventEnd(0x4)

    label("loc_5A5C")

    TalkEnd(0xFE)
    Return()

    # Function_20_57F7 end

    def Function_21_5A60(): pass

    label("Function_21_5A60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_5B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_5AC5")

    ChrTalk(    #232
        0xFE,
        "This makes three victories and two losses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "She really is a good rival.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B8E")

    label("loc_5AC5")


    ChrTalk(    #234
        0xFE,
        "Aww... Looks like I couldn't beat Lucy this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "I've been trying a bunch of new study methods,\x01",
            "but they just weren't enough, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        "I wonder what kinds of study methods she uses?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_5B8E")

    TalkEnd(0xFE)
    Return()

    # Function_21_5A60 end

    def Function_22_5B92(): pass

    label("Function_22_5B92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_5CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_5C2A")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #237
        0x26,
        (
            "...I don't mind losing to THE Leo Lorentz. \x01",
            "That's basically inevitable.\x02\x03",

            "Lechter, though? Aidios, Aaanything but that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF7")

    label("loc_5C2A")


    ChrTalk(    #238
        0x26,
        "Hi there, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x26,
        (
            "Like I said yesterday, our club's going to start\x01",
            "meeting again tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x26,
        (
            "So make sure you use today to get yourself\x01",
            "well rested and back in peak shape!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        "#040FYou bet.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_5CF7")

    Jump("loc_5E90")

    label("loc_5CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_5D5E")

    ChrTalk(    #242
        0x26,
        (
            "Don't get involved with the Student Council\x01",
            "president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x26,
        "Seriously. Don't.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E90")

    label("loc_5D5E")


    ChrTalk(    #244
        0x13B,
        "#640FExcuse me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x26,
        "Yes...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x13B,
        (
            "#640FYou wouldn't have happened to see the Student\x01",
            "Council president anywhere, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x26,
        "Ah, yes. The Student Council...president...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x26,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x26,
        (
            "You don't want to get involved with him.\x01",
            "Trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x26,
        "That's all I'm gonna say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x105,
        "#045FR-Right...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_5E90")

    TalkEnd(0xFE)
    Return()

    # Function_22_5B92 end

    def Function_23_5E94(): pass

    label("Function_23_5E94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_6004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_5F2D")

    ChrTalk(    #252
        0xFE,
        (
            "I wonder if the judges liked the falcon on his\x01",
            "shoulder or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "I mean, it did make for a good picture, but still...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6004")

    label("loc_5F2D")


    ChrTalk(    #254
        0xFE,
        (
            "...I ended up being forced to draw a portrait of\x01",
            "the Student Council president a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "I didn't expect what would happen, though... \x01",
            "It ended up winning this contest I entered it in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "...Why?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_6004")

    TalkEnd(0xFE)
    Return()

    # Function_23_5E94 end

    def Function_24_6008(): pass

    label("Function_24_6008")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_6174")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_60C2")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #257
        0x15,
        (
            "#640FYes, that's right. I just need you to fill out\x01",
            "your club's planned budget here.\x02\x03",

            "#643FSo, you put an outline of your club's activities\x01",
            "here, then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6174")

    label("loc_60C2")


    ChrTalk(    #258
        0x15,
        (
            "#640FHiya, Kloe!\x02\x03",

            "I'm just going around all the club captains like\x01",
            "I said earlier.\x02\x03",

            "#648FIt's an easier job than trying to find Lechter,\x01",
            "at least... But hey! What isn't?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_6174")

    TalkEnd(0xFE)
    Return()

    # Function_24_6008 end

    def Function_25_6178(): pass

    label("Function_25_6178")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    OP_21()
    OP_C4(0x0, 0x800)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #259
        (
            "\x18\x07\x0CI'd sworn to myself that I would stop relying on\x01",
            "other people.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #260
        (
            "\x18\x07\x0CI'd had enough of being restricted in how to live.\x01",
            "I'd had enough of following the rails laid out for\x01",
            "me by other people.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #261
        (
            "\x18\x07\x0CI was going to put my own two feet on the ground\x01",
            "and start living my own life, by myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #262
        "\x18\x07\x0CThat was my resolve, and I intended to abide by it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #263
        (
            "\x18\x07\x0CBut somewhere in my heart, I had already realized\x01",
            "that 'resolve' of mine was nothing more than an\x01",
            "excuse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x15, 255)
    OP_4A(0x12, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x15, 21)
    SetChrChipByIndex(0x12, 22)
    SetChrChipByIndex(0x10, 15)
    SetChrChipByIndex(0x11, 20)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 19)
    SetChrChipByIndex(0x16, 17)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x105, 4960, 250, 30360, 270)
    SetChrPos(0x14, 500, 200, 30000, 90)
    SetChrPos(0x11, 500, 200, 32000, 90)
    SetChrPos(0x16, -2750, 100, 34100, 90)
    SetChrPos(0x12, -2750, 200, 30000, 90)
    SetChrPos(0x15, -2750, 200, 32000, 90)
    SetChrPos(0x10, 500, 200, 34100, 90)
    SetChrPos(0x17, -5900, 100, 32000, 90)
    SetChrPos(0x13, -5900, 100, 34100, 90)
    SetChrPos(0x18, 5300, 250, 32119, 270)
    OP_6D(4200, 0, 32500, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    SoundLoad(233)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #264
        "\x07\x05[Social Studies Classroom - First-Year Joint Class]\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1E()
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #265
        0x18,
        (
            "#11PSettle down, settle down. I've got someone to \x01",
            "introduce to you all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x18,
        "#11PThis is our new transfer student, Kloe Rinz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x18,
        (
            "#11PShe's going to be studying...oh...social studies,\x01",
            "apparently! You'll be with me, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x105, 400)
    Sleep(300)

    ChrTalk(    #268
        0x18,
        (
            "#5PWell, why don't you introduce yourself to \x01",
            "the class?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x18, 400)
    Sleep(300)

    ChrTalk(    #269
        0x105,
        "#047F#12P...Of course.\x02",
    )

    CloseMessageWindow()

    def lambda_66E2():
        OP_6D(1700, 0, 33000, 1500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_66E2)

    def lambda_66FA():
        OP_67(0, 4600, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_66FA)

    def lambda_6712():
        OP_6B(3300, 1500)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_6712)
    OP_8C(0x105, 270, 400)

    def lambda_6729():
        OP_8E(0xFE, 0x116C, 0xFA, 0x7698, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6729)
    Sleep(300)
    OP_8C(0x18, 270, 500)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x2D, 0x0)
    Sleep(500)

    ChrTalk(    #270
        0x105,
        (
            "#042F#2PMy name is Kloe Rinz, and starting today, I will\x01",
            "be a first-year student at this academy.\x02\x03",

            "I've been looking forward to beginning my\x01",
            "life at this wonderful academy for some time,\x01",
            "so I'm truly delighted to be here.\x02\x03",

            "It's an honor to be able to count myself among\x01",
            "your number.\x02\x03",

            "#543FI'm still an inexperienced child in many ways, so\x01",
            "I fear I may cause you all trouble in the coming\x01",
            "days and weeks...\x02\x03",

            "#542F...but I intend to work as hard as I can for the\x01",
            "betterment of myself, my class, and my school,\x01",
            "so I do hope we can all get along.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x18, 0x3, 0x0, 0x1C)
    OP_22(0xE9, 0x0, 0x64)
    Sleep(2000)
    OP_44(0x18, 0x3)
    Sleep(2000)

    NpcTalk(    #271
        0x15,
        "Bespectacled Girl",
        (
            "#647F(I sure wasn't expecting a transfer student at\x01",
            "this time of year.)\x02\x03",

            "#649F(I wonder if she's from a rich family or something?\x01",
            "She sure sounds stuffy, so it would fit...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #272
        0x12,
        "Short-Haired Boy",
        (
            "#730F#6P(She's obviously got some kinda special\x01",
            "circumstances to be enrolling in May.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #273
        0x14,
        "Freyja",
        "#6PExcuse me, but could I ask a question?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #274
        0x14,
        "Freyja",
        "#6PWhere do you live? You're from Liberl, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x105,
        (
            "#044FUmm...\x02\x03",

            "#542FYes. I'm from...Grancel.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #276
        0x11,
        "Thelma",
        "Do you have any hobbies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x105,
        "#045FErm... Not especially.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #278
        0x14,
        "Freyja",
        "#6PWhat? For reals?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #279
        0x14,
        "Freyja",
        "#6PThat's kind of boring...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x105,
        (
            "#043FUmm...\x02\x03",

            "Still...no matter how much I think about it, \x01",
            "nothing comes to mind.\x02\x03",

            "#049F(I suppose I could say making sweets...)\x02\x03",

            "(...but I don't feel like I do that enough\x01",
            "for it to qualify as a hobby.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #281
        0x16,
        "Rhody",
        (
            "#5PIsn't the entrance exam for transfer students\x01",
            "supposed to be crazy hard?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #282
        0x16,
        "Rhody",
        "#5PYou must be really smart to be able to pass it!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #283
        0x17,
        "Mickey",
        "#2PHarder than the one the rest of us took?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #284
        0x17,
        "Mickey",
        "#2PNo way! That was nuts as it was!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #285
        0x10,
        "Logic",
        "#5PYou must be quite smart...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xAE, 0x0, 0x64)
    OP_43(0x18, 0x3, 0x0, 0x1C)
    Sleep(2000)
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #286
        0x105,
        "#043FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x18,
        "#11POkay, class! That's enough!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x18,
        (
            "#11PI'm sure you must all have things you want\x01",
            "to ask our new student, but they can wait\x01",
            "until after class!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x18, 0x0, 0x0, 0x1B)
    OP_44(0x18, 0x3)
    TurnDirection(0x18, 0x105, 400)
    Sleep(300)

    ChrTalk(    #289
        0x18,
        "#5PGo and take a seat, Kloe.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x18, 400)
    Sleep(300)

    ChrTalk(    #290
        0x105,
        "#044F#12P...Oh. Yes, ma'am.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 225, 400)
    Sleep(300)

    def lambda_6F3B():

        label("loc_6F3B")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_6F3B")

    QueueWorkItem2(0x18, 2, lambda_6F3B)
    OP_43(0x105, 0x0, 0x0, 0x1A)
    Sleep(3000)
    OP_44(0x18, 0x2)
    OP_8C(0x18, 270, 400)
    Sleep(300)

    ChrTalk(    #291
        0x18,
        (
            "#11PAll right, then. Time to get started with our\x01",
            "lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x18,
        "#11PIf you would, open your textbooks to page 23.\x02",
    )

    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x105, 0x0)
    Sleep(500)
    Fade(300)
    SetChrSubChip(0x15, 2)
    Sleep(500)

    NpcTalk(    #293
        0x15,
        "Bespectacled Girl",
        (
            "#647F#5P(Hmm... A mysterious transfer student...)\x02\x03",

            "#640F(Now there's a surefire recipe for catching\x01",
            "my interest.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7081():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7081)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x2D, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_25_6178 end

    def Function_26_70AC(): pass

    label("Function_26_70AC")


    def lambda_70B2():
        OP_8E(0xFE, 0x94C, 0x0, 0x6FCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70B2)
    WaitChrThread(0x105, 0x1)

    def lambda_70D2():
        OP_8E(0xFE, 0xFFFFE764, 0x0, 0x6FCC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70D2)
    WaitChrThread(0x105, 0x1)

    def lambda_70F2():
        OP_8E(0xFE, 0xFFFFE764, 0x0, 0x7210, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70F2)
    WaitChrThread(0x105, 0x1)
    Fade(500)
    SetChrPos(0x105, -5900, 100, 30000, 90)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 23)
    Return()

    # Function_26_70AC end

    def Function_27_712D(): pass

    label("Function_27_712D")

    OP_24(0xAE, 0x5A)
    Sleep(200)
    OP_24(0xAE, 0x50)
    Sleep(200)
    OP_24(0xAE, 0x46)
    Sleep(200)
    OP_24(0xAE, 0x3C)
    Sleep(200)
    OP_24(0xAE, 0x32)
    Sleep(200)
    OP_24(0xAE, 0x28)
    Sleep(200)
    OP_24(0xAE, 0x1E)
    Sleep(200)
    OP_24(0xAE, 0x14)
    Sleep(200)
    OP_24(0xAE, 0xA)
    Sleep(200)
    OP_24(0xAE, 0x0)
    Return()

    # Function_27_712D end

    def Function_28_7183(): pass

    label("Function_28_7183")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7221")
    OP_62(0x14, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x16, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x11, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    Jump("Function_28_7183")

    label("loc_7221")

    Return()

    # Function_28_7183 end

    def Function_29_7222(): pass

    label("Function_29_7222")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_4A(0x10, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1C, 255)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #294
        "\x07\x00Two weeks passed at the academy...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #295
        (
            "\x07\x00Despite the passing of time, the students' interest\x01",
            "in the transfer student showed no sign of letting up,\x01",
            "and she was soon the talk of the whole school.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #296
        (
            "\x07\x00All anyone wanted to talk about was her--how smart\x01",
            "she was, how unusually polite she was, among other\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #297
        (
            "\x07\x00Her peers thought the formalities were largely due\x01",
            "to nerves and that she would naturally ease up over\x01",
            "time, but the reality was somewhat different...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_6D(37080, 0, 31600, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrPos(0x105, 2160, 0, 34220, 270)
    SetChrPos(0x19, 32800, 0, 33500, 180)
    SetChrPos(0x10, 32800, 0, 33500, 180)
    SetChrPos(0x1D, 32800, 0, 33500, 180)
    SetChrPos(0x1C, 32800, 0, 33500, 180)
    SetChrPos(0x1A, 43000, 0, 30600, 0)
    OP_A3(0x3)

    def lambda_754C():
        OP_6B(3400, 6000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_754C)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_70(0x2, 0xF)
    OP_73(0xF)

    def lambda_7576():
        OP_8E(0xFE, 0x8020, 0x0, 0x7788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7576)
    WaitChrThread(0x19, 0x1)

    def lambda_7596():
        OP_8E(0xFE, 0x8688, 0x0, 0x7788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7596)
    WaitChrThread(0x19, 0x1)

    ChrTalk(    #298 op#A op#5
        0x19,
        "#25A#5PWhew... I'm glad that's over.\x05\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x3, 0x0, 0x1F)

    def lambda_75E8():
        OP_8E(0xFE, 0x8020, 0x0, 0x72D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_75E8)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #299 op#A op#5
        0x10,
        (
            "#30A#5PPhew! Glad I attended class today.\x01",
            "We ended up covering so much...\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x21)

    def lambda_765F():
        OP_8E(0xFE, 0x8020, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_765F)
    WaitChrThread(0x1D, 0x1)
    OP_8C(0x1D, 0, 400)

    ChrTalk(    #300 op#A op#5
        0x1D,
        "#30A#12PCome on, Monika! It's time for practice!\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301 op#A op#5
        0x1C,
        "#2P#17AComing!\x05\x02",
    )

    CloseMessageWindow()
    OP_4A(0x18, 255)
    OP_43(0x18, 0x0, 0x0, 0x1E)
    Sleep(500)

    def lambda_76E2():
        OP_8E(0xFE, 0x8020, 0x0, 0x7A44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_76E2)
    WaitChrThread(0x1C, 0x1)
    Sleep(300)

    def lambda_7707():

        label("loc_7707")

        TurnDirection(0xFE, 0x1D, 400)
        OP_48()
        Jump("loc_7707")

    QueueWorkItem2(0x1C, 2, lambda_7707)
    OP_43(0x1D, 0x3, 0x0, 0x23)
    Sleep(100)
    OP_44(0x1C, 0x2)
    OP_43(0x1C, 0x3, 0x0, 0x22)
    OP_A2(0x3)
    WaitChrThread(0x18, 0x0)
    Fade(1000)
    OP_6D(-3060, 0, 32780, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(45000, 0)
    OP_6E(220, 0)
    SetChrPos(0x18, 2880, 0, 26500, 0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7140, 0, 34280, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -7140, 0, 33020, 0)
    OP_71(0x1002, 0x0)
    ExitThread()
    OP_43(0x105, 0x2, 0x0, 0x2)

    def lambda_77CE():
        OP_6D(4059, 0, 32780, 4000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_77CE)
    WaitChrThread(0x2D, 0x0)

    def lambda_77EB():
        OP_8E(0xFE, 0xB40, 0x0, 0x71E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_77EB)

    def lambda_7806():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_7806)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x18, 270, 400)
    Sleep(800)
    OP_8C(0x18, 315, 400)
    Sleep(800)
    OP_8C(0x18, 270, 400)
    Sleep(300)

    ChrTalk(    #302
        0x18,
        "#11POh, dear. Did everyone go home already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x18,
        "#11PI haven't handed out all these printouts yet...\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0x2)
    SetChrSubChip(0x105, 0)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x105, 180, 400)

    ChrTalk(    #304
        0x105,
        (
            "#044FOh, it's Ms. Wiola...\x02\x03",

            "(She looks like she needs help with something.\x01",
            "Maybe I could volunteer...?)\x02\x03",

            "#047F(...No time like the present!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7976():
        OP_6D(4370, 0, 31610, 2000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7976)

    def lambda_798E():
        OP_6B(3580, 2000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_798E)

    def lambda_799E():
        OP_8E(0xFE, 0xB40, 0x0, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_799E)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x2D, 0x0)
    Sleep(300)

    ChrTalk(    #305
        0x105,
        (
            "#042F#5PU-Umm... Ms. Wiola, is there anything I can help\x01",
            "you with?\x02\x03",

            "You seem rather troubled about something...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x105, 400)

    ChrTalk(    #306
        0x18,
        (
            "#12PWell, there is, but I'd feel a little bad asking\x01",
            "you to help me with it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x18,
        "#12PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x18,
        "#12P...Well, if you insist!\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #309
        0x105,
        "#542F#5PO-Of course.\x02",
    )

    CloseMessageWindow()

    def lambda_7AF5():
        OP_8E(0xFE, 0xB40, 0x0, 0x7404, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7AF5)
    WaitChrThread(0x18, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #310
        "\x07\x05Ms. Wiola handed a pile of printouts to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #311
        0x18,
        (
            "#12PCould you go and hand these out to all of the\x01",
            "social studies students, then? One each.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x18,
        (
            "#12PThey're rather important, too, so try and see\x01",
            "that everyone gets one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x105,
        "#042F#5PI'll get to work right away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x18,
        "#12PThank you so much! Okay, gotta run!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x18,
        "#12PThere's a staff meeting starting soon!\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x18, 180, 600)

    def lambda_7CB9():
        OP_8E(0xFE, 0xB40, 0x0, 0x6784, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7CB9)
    Sleep(300)

    def lambda_7CD9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_7CD9)
    WaitChrThread(0x18, 0x1)
    OP_63(0x18)
    Sleep(500)
    SetChrFlags(0x18, 0x80)
    Sleep(500)

    ChrTalk(    #316
        0x105,
        "#047F#5PLet's see...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Sleep(300)

    def lambda_7D28():
        OP_6D(3300, 0, 35650, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7D28)

    def lambda_7D40():
        OP_8E(0xFE, 0x8D4, 0x0, 0x85CA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7D40)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x2D, 0x0)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #317
        0x105,
        (
            "#044F#12POh, this is a list of this year's credits.\x02\x03",

            "#042FNo wonder she wanted these handed out right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #318
        0x105,
        (
            "#047F#11P(I might as well start with the students still here.)\x02\x03",

            "(After that, I can go and speak with the ones\x01",
            "who have gone to their respective clubs, as well\x01",
            "as those who have returned to their dormitories.)\x02\x03",

            "#042F...Okay! To work, I go!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F65)
    OP_59()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2880, 0, 31000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x2C, 1300, 180, 34060, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x800)
    OP_51(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_29_7222 end

    def Function_30_7FE7(): pass

    label("Function_30_7FE7")

    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrPos(0x18, 47100, 0, 35300, 180)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_801A():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_801A)
    WaitChrThread(0x18, 0x1)

    def lambda_803A():
        OP_8E(0xFE, 0x9E34, 0x0, 0x9664, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_803A)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_806C():
        OP_8E(0xFE, 0x9D6C, 0x0, 0x8EF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_806C)
    WaitChrThread(0x18, 0x1)

    def lambda_808C():
        OP_8E(0xFE, 0x9C40, 0x0, 0x81B0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_808C)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_80BE():
        OP_8E(0xFE, 0x92E0, 0x0, 0x7918, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_80BE)
    WaitChrThread(0x18, 0x1)

    def lambda_80DE():
        OP_8E(0xFE, 0x8020, 0x0, 0x7918, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_80DE)
    WaitChrThread(0x18, 0x1)

    def lambda_80FE():
        OP_8E(0xFE, 0x8020, 0x0, 0x82DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_80FE)
    WaitChrThread(0x18, 0x1)
    Return()

    # Function_30_7FE7 end

    def Function_31_8119(): pass

    label("Function_31_8119")


    def lambda_811F():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x7788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_811F)
    Sleep(500)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_8156():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_8156)
    WaitChrThread(0x19, 0x1)
    Sleep(1000)
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_A6(0x3)
    OP_63(0x19)
    Sleep(500)

    def lambda_818B():

        label("loc_818B")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_818B")

    QueueWorkItem2(0x1A, 2, lambda_818B)

    def lambda_819C():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_819C)
    Sleep(500)
    OP_44(0x1A, 0x2)
    OP_43(0x1A, 0x3, 0x0, 0x20)
    WaitChrThread(0x19, 0x1)

    def lambda_81CC():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_81CC)
    WaitChrThread(0x19, 0x1)

    def lambda_81EC():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_81EC)
    WaitChrThread(0x19, 0x1)

    def lambda_820C():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_820C)
    WaitChrThread(0x19, 0x1)
    Return()

    # Function_31_8119 end

    def Function_32_8227(): pass

    label("Function_32_8227")


    def lambda_822D():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x7E2B, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_822D)
    WaitChrThread(0x1A, 0x1)

    def lambda_824D():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_824D)
    WaitChrThread(0x1A, 0x1)

    def lambda_826D():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_826D)
    WaitChrThread(0x1A, 0x1)

    def lambda_828D():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_828D)
    WaitChrThread(0x1A, 0x1)

    def lambda_82AD():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_82AD)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_32_8227 end

    def Function_33_82C8(): pass

    label("Function_33_82C8")


    def lambda_82CE():
        OP_8E(0xFE, 0x9088, 0x0, 0x72D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_82CE)
    WaitChrThread(0x10, 0x1)

    def lambda_82EE():
        OP_8E(0xFE, 0x9920, 0x0, 0x7B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_82EE)
    WaitChrThread(0x10, 0x1)

    def lambda_830E():
        OP_8E(0xFE, 0x9920, 0x0, 0x8AFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_830E)
    WaitChrThread(0x10, 0x1)

    def lambda_832E():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_832E)
    WaitChrThread(0x10, 0x1)

    def lambda_834E():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_834E)
    WaitChrThread(0x10, 0x1)

    def lambda_836E():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_836E)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_33_82C8 end

    def Function_34_8389(): pass

    label("Function_34_8389")

    Sleep(400)

    def lambda_8394():
        OP_8E(0xFE, 0x8534, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8394)
    WaitChrThread(0xFE, 0x1)

    def lambda_83B4():
        OP_8E(0xFE, 0x9218, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83B4)
    WaitChrThread(0xFE, 0x1)

    def lambda_83D4():
        OP_8E(0xFE, 0x99E8, 0x0, 0x7D00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83D4)
    WaitChrThread(0xFE, 0x1)

    def lambda_83F4():
        OP_8E(0xFE, 0x99E8, 0x0, 0x8BD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83F4)
    WaitChrThread(0xFE, 0x1)

    def lambda_8414():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8414)
    WaitChrThread(0xFE, 0x1)

    def lambda_8434():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8434)
    WaitChrThread(0xFE, 0x1)

    def lambda_8454():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8454)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_34_8389 end

    def Function_35_846F(): pass

    label("Function_35_846F")


    def lambda_8475():
        OP_8E(0xFE, 0x9218, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8475)
    WaitChrThread(0x1D, 0x1)

    def lambda_8495():
        OP_8E(0xFE, 0x99E8, 0x0, 0x7D00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8495)
    WaitChrThread(0x1D, 0x1)

    def lambda_84B5():
        OP_8E(0xFE, 0x99E8, 0x0, 0x8BD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_84B5)
    WaitChrThread(0x1D, 0x1)

    def lambda_84D5():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_84D5)
    WaitChrThread(0x1D, 0x1)

    def lambda_84F5():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_84F5)
    WaitChrThread(0x1D, 0x1)

    def lambda_8515():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8515)
    WaitChrThread(0x1D, 0x1)
    Return()

    # Function_35_846F end

    def Function_36_8530(): pass

    label("Function_36_8530")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    OP_4A(0x11, 255)
    OP_4A(0x1B, 255)
    Fade(1000)
    OP_6D(-5200, 0, 34200, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(3760, 0)
    OP_6C(50000, 0)
    OP_6E(222, 0)
    SetChrPos(0x105, -7140, 0, 31540, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #319
        0x11,
        "#5PReally? I had no idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x1B,
        (
            "#2PWell, the Republic is pretty huge in terms\x01",
            "of land mass and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x1B,
        (
            "#2PJust traveling on foot isn't going to cut it.\x01",
            "You need a more effective means of\x01",
            "transportation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x105,
        "#542F#12PE-Excuse me...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x1B, 180, 400)
    Sleep(300)

    ChrTalk(    #323
        0x1B,
        "#5POh, Kloe. Hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x1B,
        "#5PCan we help you with something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x105,
        (
            "#047F#12PWell, you see...\x02\x03",

            "#040FMs. Wiola has entrusted me with the task of giving\x01",
            "printouts to all of the social studies students...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #326
        "\x07\x05Kloe gave Roy and Thelma a copy of the printout each.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #327
        0x11,
        "#5PHey! It's a list of all our credits.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x11,
        (
            "#5PThanks for going out of your way to\x01",
            "deliver these, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x105,
        (
            "#045F#12PNot at all.\x02\x03",

            "#542FI apologize for intruding on your conversation,\x01",
            "too.\x02\x03",

            "#543FI'll get out of your way now. Have a good day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x1B,
        "#5PO-Oh, right...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)

    def lambda_8905():

        label("loc_8905")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_8905")

    QueueWorkItem2(0x11, 2, lambda_8905)

    def lambda_8916():

        label("loc_8916")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_8916")

    QueueWorkItem2(0x1B, 2, lambda_8916)
    OP_43(0x105, 0x3, 0x0, 0x25)
    Sleep(3000)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    OP_63(0x1B)
    Sleep(500)

    ChrTalk(    #331
        0x11,
        "#5PCrazy how polite she is, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x1B,
        "#6PYeah, I guess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x1B,
        (
            "#6PShe's a bit TOO polite, though, if you ask me.\x01",
            "Makes it hard to feel comfortable talking to\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A0F():
        OP_6B(3660, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_8A0F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x2D, 0x0)
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0x2)
    OP_44(0x1B, 0x2)
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, 33000, 0, 31400, 180)
    OP_6D(33000, 0, 31400, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F67)
    EventEnd(0x0)
    Return()

    # Function_36_8530 end

    def Function_37_8AA4(): pass

    label("Function_37_8AA4")


    def lambda_8AAA():
        OP_8E(0xFE, 0xFFFFE41C, 0x0, 0x6FF4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8AAA)
    WaitChrThread(0x105, 0x1)

    def lambda_8ACA():
        OP_8E(0xFE, 0xBB8, 0x0, 0x6FF4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8ACA)
    WaitChrThread(0x105, 0x1)
    Return()

    # Function_37_8AA4 end

    def Function_38_8AE5(): pass

    label("Function_38_8AE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-4340, 0, 32800, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrPos(0x105, 2960, 0, 26500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8B5A():
        OP_6D(3680, 0, 32800, 5000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_8B5A)
    FadeToBright(2000, 0)
    Sleep(4000)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_8B8A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8B8A)

    def lambda_8B9C():
        OP_8E(0xFE, 0xB90, 0x0, 0x6FF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8B9C)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x105, 270, 500)
    Sleep(500)
    OP_8C(0x105, 0, 500)
    Sleep(500)

    def lambda_8BEB():
        OP_6D(3680, 0, 34800, 1100)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_8BEB)

    def lambda_8C03():
        OP_67(0, 5700, -10000, 1100)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8C03)

    def lambda_8C1B():
        OP_8E(0xFE, 0x870, 0x0, 0x8534, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C1B)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 270, 600)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x2C, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #334
        0x105,
        "#047F#5P*sigh*\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x105, 0, 400)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #335
        0x105,
        (
            "#049F#5P...\x02\x03",

            "Can I really keep going on like this?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x105, 180, 350)
    Sleep(300)

    def lambda_8CE9():
        OP_8E(0xFE, 0x870, 0x0, 0x6F7C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8CE9)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x105, 0x1)
    OP_6D(33000, 0, 33500, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrPos(0x105, 33000, 0, 33500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_70(0x2, 0xF)
    OP_73(0xF)

    def lambda_8D8A():
        OP_8E(0xFE, 0x80E8, 0x0, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8D8A)
    WaitChrThread(0x105, 0x1)
    OP_6F(0x2, 15)
    OP_70(0x2, 0x0)

    def lambda_8DB8():
        OP_6D(42120, 0, 34520, 5000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_8DB8)

    def lambda_8DD0():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8DD0)

    def lambda_8DE0():
        OP_8E(0xFE, 0x9E98, 0x0, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8DE0)
    WaitChrThread(0x105, 0x1)

    def lambda_8E00():
        OP_8E(0xFE, 0x9E98, 0x0, 0x80E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8E00)
    WaitChrThread(0x105, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 55160, 0, 34080, 0)

    NpcTalk(    #336
        0x1D,
        "Voice",
        (
            "#3P#1SSo, yeah, that transfer student came by\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 90, 500)
    Sleep(500)

    NpcTalk(    #337
        0x1D,
        "Voice",
        "#3P#1SOh, the super smart one?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #338
        0x1D,
        "Voice",
        "#3P#1SYeah. Anyway...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0x1D,
        "Voice",
        "#3P#1S...so, yeah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #340
        0x105,
        (
            "#043FU-Umm...\x02\x03",

            "#049F(I-I should hurry back to my room and go over\x01",
            "what we learned in class!)\x02\x03",

            "(I need to go over our credits list again, too!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FB1():
        OP_8E(0xFE, 0x9E98, 0x0, 0x96B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8FB1)
    WaitChrThread(0x105, 0x1)

    def lambda_8FD1():
        OP_8E(0xFE, 0xB608, 0xFFFFF830, 0x96B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8FD1)
    WaitChrThread(0x105, 0x1)

    def lambda_8FF1():
        OP_8E(0xFE, 0xB608, 0xFFFFF254, 0x8AAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8FF1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_8AE5 end

    def Function_39_901E(): pass

    label("Function_39_901E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_6D(-4350, 200, 33340, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x1E, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x18, 255)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x105, 23)
    SetChrChipByIndex(0x1E, 26)
    SetChrChipByIndex(0x19, 24)
    SetChrChipByIndex(0x1D, 20)
    SetChrChipByIndex(0x1C, 18)
    SetChrChipByIndex(0x1B, 16)
    SetChrChipByIndex(0x10, 15)
    SetChrChipByIndex(0x11, 20)
    SetChrPos(0x19, 500, 200, 30000, 90)
    SetChrPos(0x1E, 500, 200, 32000, 90)
    SetChrPos(0x105, 500, 200, 34100, 90)
    SetChrPos(0x1D, -2750, 200, 30000, 90)
    SetChrPos(0x1C, -2750, 200, 32000, 90)
    SetChrPos(0x1B, -2750, 100, 34100, 90)
    SetChrPos(0x10, -5900, 100, 30000, 90)
    SetChrPos(0x11, -5900, 100, 32000, 90)
    SetChrPos(0x18, 4440, 250, 29740, 270)

    def lambda_91CB():
        OP_6D(2070, 200, 33190, 5500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_91CB)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x105, 0x3, 0x0, 0x2B)
    Sleep(1000)
    OP_62(0x1E, 0x6E, 1800, 0x1C, 0x21, 0x12C, 0x0)
    Sleep(2000)
    SetChrSubChip(0x105, 2)
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    WaitChrThread(0x2D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x1E, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1D, 0x4)
    ClearChrFlags(0x1C, 0x4)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    OP_6D(6180, 0, 3680, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x21, 255)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x26, 29)
    SetChrChipByIndex(0x27, 28)
    SetChrChipByIndex(0x28, 16)
    SetChrChipByIndex(0x29, 19)
    SetChrChipByIndex(0x15, 21)
    SetChrChipByIndex(0x16, 17)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x26, 500, 200, 0, 90)
    SetChrPos(0x27, 500, 200, 2000, 90)
    SetChrPos(0x28, 500, 200, 4100, 90)
    SetChrPos(0x29, -2750, 200, 0, 90)
    SetChrPos(0x15, -2750, 200, 2000, 90)
    SetChrPos(0x16, -2750, 100, 4100, 90)
    SetChrPos(0x17, -5900, 100, 0, 90)
    SetChrPos(0x21, 5300, 250, 2120, 270)

    def lambda_93EE():
        OP_6D(-790, 0, 3010, 5500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_93EE)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x105, 0x3, 0x0, 0x2C)
    Sleep(1000)
    OP_62(0x15, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x15, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(2000)
    WaitChrThread(0x2D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    ClearChrFlags(0x29, 0x4)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    OP_6D(89540, 1500, 32299, 0)
    OP_67(0, 6390, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x22, 255)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x23, 0x4)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x1F, 27)
    SetChrChipByIndex(0x1A, 25)
    SetChrChipByIndex(0x23, 20)
    SetChrChipByIndex(0x24, 18)
    SetChrChipByIndex(0x25, 17)
    SetChrChipByIndex(0x12, 22)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 19)
    SetChrPos(0x1F, 90500, 200, 30000, 90)
    SetChrPos(0x1A, 90500, 200, 32000, 90)
    SetChrPos(0x23, 90500, 200, 34100, 90)
    SetChrPos(0x24, 87250, 200, 30000, 90)
    SetChrPos(0x25, 87250, 200, 32000, 90)
    SetChrPos(0x12, 87250, 100, 34100, 90)
    SetChrPos(0x13, 84100, 100, 30000, 90)
    SetChrPos(0x14, 84100, 100, 32000, 90)
    SetChrPos(0x22, 92400, 0, 35300, 270)
    OP_43(0x22, 0x0, 0x0, 0x29)
    SoundLoad(138)

    def lambda_9635():
        OP_6D(89540, 200, 32299, 4500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_9635)

    def lambda_964D():
        OP_67(0, 5500, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_964D)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x105, 0x3, 0x0, 0x2D)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x12, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_22(0x8A, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x22, 0x0)

    def lambda_96CE():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_96CE)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x25, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x2D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_23(0x8A)
    Sleep(2000)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    OP_6D(41540, 0, 38140, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(14000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x15, 40560, 0, 36200, 70)
    SetChrPos(0x12, 41900, 0, 37040, 230)
    SetChrPos(0x105, 37840, 0, 28560, 14)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x15, 11)
    SetChrSubChip(0x15, 0)
    SetChrChipByIndex(0x12, 10)
    SetChrSubChip(0x12, 0)
    OP_4A(0x15, 255)
    OP_4A(0x12, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #341
        0x12,
        "#734F#11PAhhh... We're finally free!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x15,
        (
            "#645F#6PI knew this place wouldn't go easy on us...\x01",
            "Those were really hard.\x02\x03",

            "I feel like I just wanna curl up in bed and\x01",
            "sleep for a week now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9975():
        OP_8E(0xFE, 0xA0DC, 0x0, 0x8854, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9975)
    Sleep(1300)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_99C3():

        label("loc_99C3")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_99C3")

    QueueWorkItem2(0x15, 2, lambda_99C3)
    Sleep(100)

    def lambda_99D9():

        label("loc_99D9")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_99D9")

    QueueWorkItem2(0x12, 2, lambda_99D9)
    Sleep(300)

    ChrTalk(    #343
        0x15,
        (
            "#640F#5POh, Kloe!\x02\x03",

            "How'd the exams go for you?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)
    OP_44(0x15, 0x2)
    OP_44(0x12, 0x2)
    TurnDirection(0x105, 0x15, 400)
    Sleep(300)

    ChrTalk(    #344
        0x105,
        "#045F#12PWell...all right, I suppose?\x02",
    )

    CloseMessageWindow()

    def lambda_9A67():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_9A67)
    TurnDirection(0x12, 0x15, 500)
    Sleep(1200)

    def lambda_9A81():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_9A81)
    TurnDirection(0x12, 0x105, 500)
    Sleep(300)

    ChrTalk(    #345
        0x15,
        (
            "#649F#5PNow, now. There's no need to be modest.\x01",
            "We know you probably finished in half the\x01",
            "time and got all the answers right, to boot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x12,
        "#730F#11PThe smile says it all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x105,
        "#041F#12PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x15,
        "#641F#5PI wish I had your brain. Sure we can't swap?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 7)
    SetChrSubChip(0x1F, 0)
    OP_4A(0x1F, 255)
    SetChrPos(0x1F, 46130, 0, 28570, 315)

    def lambda_9BC2():
        OP_8E(0xFE, 0xA5B4, 0x0, 0x8430, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9BC2)
    Sleep(500)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0x1F, 0x1)
    Sleep(300)

    ChrTalk(    #349
        0x1F,
        (
            "#1780FThis isn't the place to be loitering.\x01",
            "You're stopping people from getting\x01",
            "to the stairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9CC6():

        label("loc_9CC6")

        TurnDirection(0xFE, 0x1F, 500)
        OP_48()
        Jump("loc_9CC6")

    QueueWorkItem2(0x15, 2, lambda_9CC6)

    def lambda_9CD7():

        label("loc_9CD7")

        TurnDirection(0xFE, 0x1F, 500)
        OP_48()
        Jump("loc_9CD7")

    QueueWorkItem2(0x12, 2, lambda_9CD7)

    def lambda_9CE8():

        label("loc_9CE8")

        TurnDirection(0xFE, 0x1F, 500)
        OP_48()
        Jump("loc_9CE8")

    QueueWorkItem2(0x105, 2, lambda_9CE8)
    Sleep(300)

    ChrTalk(    #350
        0x105,
        "#044F#5POops...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(160, 110, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #351
        "\x07\x00#3SW-We're sorry!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_9D62():
        OP_8F(0xFE, 0x9E20, 0x0, 0x85DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D62)

    def lambda_9D7D():
        OP_8F(0xFE, 0x9C04, 0x0, 0x8BF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9D7D)

    def lambda_9D98():
        OP_8F(0xFE, 0xA5AA, 0x0, 0x92D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9D98)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_9DC2():
        OP_8E(0xFE, 0xA23A, 0x0, 0x8A02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9DC2)
    WaitChrThread(0x1F, 0x1)

    def lambda_9DE2():
        OP_8E(0xFE, 0xA154, 0x0, 0x97EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9DE2)
    WaitChrThread(0x1F, 0x1)
    Sleep(300)

    ChrTalk(    #352
        0x1F,
        "#1782F#5POh, and one more thing...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1F, 190, 400)
    Sleep(300)

    ChrTalk(    #353
        0x1F,
        (
            "#1780F#5PThe Student Council's work resumes today.\x02\x03",

            "I will be expecting both of you in the council\x01",
            "room at 2 o'clock for a meeting.\x02\x03",

            "#1783FDon't even think about being late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x15,
        "#642FY-Yes, sir!\x02",
    )


    ChrTalk(    #355
        0x12,
        "#732F#4PY-Yes, sir!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #356
        0x1F,
        (
            "#1782F#5PAs for you, Kloe...\x02\x03",

            "#1781FYou may do as you see fit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F62():
        OP_8E(0xFE, 0xB554, 0xFFFFF830, 0x97EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9F62)
    WaitChrThread(0x1F, 0x1)
    OP_44(0x105, 0x2)
    OP_44(0x15, 0x2)
    OP_44(0x12, 0x2)

    def lambda_9F8E():
        OP_8E(0xFE, 0xB554, 0xFFFFF254, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9F8E)
    WaitChrThread(0x1F, 0x1)
    SetChrFlags(0x1F, 0x80)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #357
        0x105,
        "#044F#6PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x15,
        (
            "#648F#5PI'm guessing that's his way of saying he'd\x01",
            "like you to come along, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 240, 400)

    def lambda_A077():
        OP_8F(0xFE, 0xA280, 0x0, 0x8F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A077)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #359
        0x12,
        (
            "#730F#11PYou might not technically be a member, but\x01",
            "you're our honorary Lechter Catcher. We kind\x01",
            "of need you at this point.\x02\x03",

            "#731FI'll bet he's acknowledged you because of that,\x01",
            "because believe me, that's a real special talent\x01",
            "you've got there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 14, 400)
    Sleep(300)

    ChrTalk(    #360
        0x105,
        (
            "#045F#6PA-Ahaha...\x02\x03",

            "I'm not sure I've done enough to warrant that,\x01",
            "personally...\x02\x03",

            "#048FIf it's okay for me to go, maybe I will, though.\x01",
            "It sounds like fun.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A243():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_A243)
    TurnDirection(0x12, 0x105, 500)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #361
        0x12,
        (
            "#734F#11PYou might be a bit disappointed if you go along\x01",
            "expecting fun...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x15,
        (
            "#640F#5PWe'd be happy to have you, though. Fun or no fun.\x02\x03",

            "#641FSo if you're up for it, so are we!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x12,
        (
            "#731F#11PNice! Let's go get ourselves some lunch,\x01",
            "then we can head over there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x105,
        "#041F#6PAll right.\x02",
    )

    CloseMessageWindow()

    def lambda_A3B3():
        OP_8C(0xFE, 14, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A3B3)
    OP_43(0x12, 0x3, 0x0, 0x28)

    def lambda_A3C8():
        OP_8C(0xFE, 60, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_A3C8)
    OP_43(0x15, 0x3, 0x0, 0x28)
    Sleep(400)

    def lambda_A3E2():
        OP_8E(0xFE, 0xA140, 0x0, 0x904C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A3E2)
    WaitChrThread(0x105, 0x1)
    OP_43(0x105, 0x3, 0x0, 0x28)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x2F6C)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_39_901E end

    def Function_40_A468(): pass

    label("Function_40_A468")

    WaitChrThread(0xFE, 0x2)

    def lambda_A473():
        OP_8E(0xFE, 0xA7BC, 0x0, 0x96C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A473)
    WaitChrThread(0xFE, 0x1)

    def lambda_A493():
        OP_8E(0xFE, 0xB860, 0xFFFFF830, 0x96C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A493)
    WaitChrThread(0xFE, 0x1)

    def lambda_A4B3():
        OP_8E(0xFE, 0xB860, 0xFFFFF254, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4B3)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_40_A468 end

    def Function_41_A4CE(): pass

    label("Function_41_A4CE")

    OP_8E(0x22, 0x15D9C, 0x0, 0x89E4, 0x7D0, 0x0)
    OP_8E(0x22, 0x15D9C, 0x0, 0x7080, 0x7D0, 0x0)
    OP_8E(0x22, 0x14FB4, 0x0, 0x7080, 0x7D0, 0x0)
    OP_8E(0x22, 0x14FB4, 0x0, 0x89E4, 0x7D0, 0x0)
    Return()

    # Function_41_A4CE end

    def Function_42_A51F(): pass

    label("Function_42_A51F")

    OP_62(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFE)
    Return()

    # Function_42_A51F end

    def Function_43_A53A(): pass

    label("Function_43_A53A")

    OP_43(0x19, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x1C, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x1D, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x1B, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x19, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x2A)
    Sleep(1000)
    Return()

    # Function_43_A53A end

    def Function_44_A59B(): pass

    label("Function_44_A59B")

    OP_43(0x29, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x28, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x26, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x17, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x27, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x16, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x29, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x28, 0x3, 0x0, 0x2A)
    Sleep(1000)
    Return()

    # Function_44_A59B end

    def Function_45_A5FC(): pass

    label("Function_45_A5FC")

    OP_43(0x13, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x1F, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x25, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x14, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x1A, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x24, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x23, 0x3, 0x0, 0x2A)
    Return()

    # Function_45_A5FC end

    def Function_46_A64C(): pass

    label("Function_46_A64C")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(116660, 0, 4640, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x20, 0)
    SetChrPos(0x105, 115970, 0, 2460, 0)
    Sleep(1000)

    ChrTalk(    #365
        0x20,
        "#780F#5POh, good day, Kloe. Can I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x105,
        (
            "#543F#12PActually...I have some business that I need to\x01",
            "take care of outside the academy.\x02\x03",

            "#542FSo I came to ask for permission to leave the\x01",
            "grounds.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #367
        "\x07\x05Kloe gave the dean a brief explanation of what she needed to do.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #368
        0x20,
        (
            "#783F#5POh, I see...\x02\x03",

            "#780FNaturally, I have no objections to granting you\x01",
            "permission.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #369
        "\x07\x05Kloe received permission to leave the grounds.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #370
        0x105,
        "#048F#12PThank you very much, Dean Collins.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x20,
        (
            "#780F#5PStill, I've been quite pleased to see you finally\x01",
            "adjusting to life here.\x02\x03",

            "#781FI've heard plenty of stories about you running\x01",
            "around the grounds lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x105,
        (
            "#045F#12PA-Ahaha...\x02\x03",

            "Well, I've been helping the Student Council\x01",
            "with their work from time to time.\x02\x03",

            "And, well, a certain element of their work\x01",
            "does involve a lot of running...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x20,
        "#781F#5PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x105,
        "#542F#12PWell, if that is all, I should probably get to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x20,
        "#780F#5POh, of course. Take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x105,
        "#041F#12PThank you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    def lambda_AACE():
        OP_8E(0xFE, 0x1C908, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AACE)
    WaitChrThread(0x105, 0x1)

    def lambda_AAEE():
        OP_8E(0xFE, 0x1C908, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AAEE)
    WaitChrThread(0x105, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_AB18():
        OP_8E(0xFE, 0x1C908, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AB18)

    def lambda_AB33():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AB33)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x20)
    Sleep(500)

    ChrTalk(    #377
        0x20,
        (
            "#781F#5PHaha... She looks so much more chipper now.\x02\x03",

            "#780FI suppose I have him to thank for that.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(59000, 0, 1400, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, 59000, 0, 1400, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x1E, 0x80)
    OP_63(0x1E)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 40990, 0, 5500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F6D)
    EventEnd(0x0)
    Return()

    # Function_46_A64C end

    def Function_47_AC78(): pass

    label("Function_47_AC78")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #378
        "\x07\x05A meeting is going on in the faculty lounge.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #379
        0x105,
        (
            "#047F(I should probably keep away to avoid\x01",
            "disturbing them.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_47_AC78 end

    def Function_48_AD12(): pass

    label("Function_48_AD12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_AE73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_ADB0")

    ChrTalk(    #380
        0x105,
        (
            "#040FThe second highest ranking was Leo,\x01",
            "and the third was Rigel...\x02\x03",

            "#045F...Oh. It looks like I was the highest among the\x01",
            "first years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE70")

    label("loc_ADB0")


    ChrTalk(    #381
        0x105,
        (
            "#040FOh, here are the examination results. Let's see\x01",
            "who the top five scorers among the third years\x01",
            "were...\x02\x03",

            "#044FNumber one was...Lechter Arundel?!\x02\x03",

            "But he was barely in any classes!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_AE70")

    Jump("loc_AF3D")

    label("loc_AE73")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #382
        (
            "\x07\x05※Schedule Changes※\x01",
            "18th - Period 2   - Social Studies/Phys. Ed. -> Social Science Major\x01",
            "19th - Period 3/4 - Year Group Joint Class -> Individual Majors\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_AF3D")

    TalkEnd(0xFF)
    Return()

    # Function_48_AD12 end

    def Function_49_AF41(): pass

    label("Function_49_AF41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AF85")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #383
        "\x07\x05It's still warm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_B029")

    label("loc_AF85")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #384
        "\x07\x05It's still warm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #385
        0x13B,
        (
            "#647FHe couldn't have gone far!\x02\x03",

            "#1891FLet's find him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x152,
        "#732FGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x105,
        "#042FO-Of course...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B029")

    TalkEnd(0xFF)
    Return()

    # Function_49_AF41 end

    def Function_50_B02D(): pass

    label("Function_50_B02D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #388
        "\x07\x05Quiet in the halls! --Student Council\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_50_B02D end

    SaveToFile()

Try(main)
