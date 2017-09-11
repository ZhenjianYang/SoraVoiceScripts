from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Dorothy',                              # 9
        'Factory Chief Murdock',                # 10
        'Supervisor Travis',                    # 11
        'Hazel',                                # 12
        'Sotiria',                              # 13
        'Elise',                                # 14
        'Muriel',                               # 15
        'Stain',                                # 16
        'Vince',                                # 17
        'Elwyn',                                # 18
        'Wong',                                 # 19
        'Lane',                                 # 20
        'Cosimo',                               # 21
        'Monika',                               # 22
        'Bruno',                                # 23
        'Igor',                                 # 24
        'Priam',                                # 25
        'Irene',                                # 26
        'Rehmann',                              # 27
        'Rudi',                                 # 28
        'Faye',                                 # 29
        'Erick',                                # 30
        'Constance',                            # 31
        'Hugo',                                 # 32
        'Antoine',                              # 33
        'Prometheus',                           # 34
        'Ray',                                  # 35
        'Terry',                                # 36
        'Dr. Miriam',                           # 37
        'Wilmont',                              # 38
        'Maintenance Chief Gustav',             # 39
        ' ',                                    # 40
        'Zeiss Landing Port',                   # 41
        'Zeiss - City Block',                   # 42
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01190 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01760 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01530 ._CH',             # 0E
        'ED6_DT07/CH01250 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01150 ._CH',             # 11
        'ED6_DT07/CH01450 ._CH',             # 12
        'ED6_DT07/CH01500 ._CH',             # 13
        'ED6_DT07/CH01550 ._CH',             # 14
        'ED6_DT07/CH01450 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01700 ._CH',             # 18
        'ED6_DT07/CH01100 ._CH',             # 19
        'ED6_DT07/CH01220 ._CH',             # 1A
        'ED6_DT07/CH01660 ._CH',             # 1B
        'ED6_DT07/CH01430 ._CH',             # 1C
        'ED6_DT07/CH01450 ._CH',             # 1D
        'ED6_DT07/CH02440 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01190P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01760P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01530P._CP',             # 0E
        'ED6_DT07/CH01250P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01150P._CP',             # 11
        'ED6_DT07/CH01450P._CP',             # 12
        'ED6_DT07/CH01500P._CP',             # 13
        'ED6_DT07/CH01550P._CP',             # 14
        'ED6_DT07/CH01450P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01700P._CP',             # 18
        'ED6_DT07/CH01100P._CP',             # 19
        'ED6_DT07/CH01220P._CP',             # 1A
        'ED6_DT07/CH01660P._CP',             # 1B
        'ED6_DT07/CH01430P._CP',             # 1C
        'ED6_DT07/CH01450P._CP',             # 1D
        'ED6_DT07/CH02440P._CP',             # 1E
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
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
        TalkScenaIndex      = 38,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        X                   = -23030,
        Z                   = 8000,
        Y                   = 86970,
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
        X                   = 28060,
        Z                   = 8000,
        Y                   = 58980,
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
        X                   = -10910,
        Y                   = 7000,
        Z                   = 63300,
        Range               = -12900,
        Unknown_10          = 0x2328,
        Unknown_14          = 0xD480,
        Unknown_18          = 0x0,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = -19010,
        Y                   = 7000,
        Z                   = 74090,
        Range               = -26870,
        Unknown_10          = 0x2328,
        Unknown_14          = 0x12714,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = -50430,
        Y                   = 24000,
        Z                   = 53980,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = -35690,
        Y                   = 9750,
        Z                   = 58940,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 54,
    )

    DeclEvent(
        X                   = -23010,
        Y                   = 7750,
        Z                   = 74850,
        Range               = 1500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 55,
    )


    DeclActor(
        TriggerX            = -50000,
        TriggerZ            = 25000,
        TriggerY            = 54010,
        TriggerRange        = 800,
        ActorX              = -50000,
        ActorZ              = 26000,
        ActorY              = 54010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 44,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6A6",          # 00, 0
        "Function_1_E70",          # 01, 1
        "Function_2_10C0",         # 02, 2
        "Function_3_10F6",         # 03, 3
        "Function_4_127E",         # 04, 4
        "Function_5_12A2",         # 05, 5
        "Function_6_12C6",         # 06, 6
        "Function_7_12EA",         # 07, 7
        "Function_8_130E",         # 08, 8
        "Function_9_1332",         # 09, 9
        "Function_10_1356",        # 0A, 10
        "Function_11_137A",        # 0B, 11
        "Function_12_137B",        # 0C, 12
        "Function_13_13E0",        # 0D, 13
        "Function_14_1445",        # 0E, 14
        "Function_15_14AB",        # 0F, 15
        "Function_16_14F2",        # 10, 16
        "Function_17_154C",        # 11, 17
        "Function_18_15F0",        # 12, 18
        "Function_19_1676",        # 13, 19
        "Function_20_17F8",        # 14, 20
        "Function_21_18B0",        # 15, 21
        "Function_22_18D1",        # 16, 22
        "Function_23_1BD8",        # 17, 23
        "Function_24_1C7C",        # 18, 24
        "Function_25_1CEE",        # 19, 25
        "Function_26_1D4F",        # 1A, 26
        "Function_27_1DCC",        # 1B, 27
        "Function_28_1DF3",        # 1C, 28
        "Function_29_1E5B",        # 1D, 29
        "Function_30_2039",        # 1E, 30
        "Function_31_2938",        # 1F, 31
        "Function_32_2D9D",        # 20, 32
        "Function_33_2E46",        # 21, 33
        "Function_34_2F88",        # 22, 34
        "Function_35_2F8F",        # 23, 35
        "Function_36_2F96",        # 24, 36
        "Function_37_3042",        # 25, 37
        "Function_38_34EF",        # 26, 38
        "Function_39_35C8",        # 27, 39
        "Function_40_3615",        # 28, 40
        "Function_41_3890",        # 29, 41
        "Function_42_3D8A",        # 2A, 42
        "Function_43_4383",        # 2B, 43
        "Function_44_4399",        # 2C, 44
        "Function_45_4421",        # 2D, 45
        "Function_46_477F",        # 2E, 46
        "Function_47_4AD9",        # 2F, 47
        "Function_48_5917",        # 30, 48
        "Function_49_6274",        # 31, 49
        "Function_50_6779",        # 32, 50
        "Function_51_6ED0",        # 33, 51
        "Function_52_716A",        # 34, 52
        "Function_53_7384",        # 35, 53
        "Function_54_7C00",        # 36, 54
        "Function_55_7C04",        # 37, 55
    )


    def Function_0_6A6(): pass

    label("Function_0_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_6B4")
    OP_A3(0x3FA)
    Event(0, 50)

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_6CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 51)

    label("loc_6CB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_6E3"),
        (103, "loc_722"),
        (107, "loc_722"),
        (104, "loc_735"),
        (SWITCH_DEFAULT, "loc_73D"),
    )


    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9")
    OP_A2(0x51B)
    Event(0, 46)
    Jump("loc_71F")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70C")
    Event(0, 48)
    Jump("loc_71F")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71F")
    OP_A2(0x537)
    Event(0, 49)

    label("loc_71F")

    Jump("loc_73D")

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_732")
    Event(0, 47)

    label("loc_732")

    Jump("loc_73D")

    label("loc_735")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_73D")

    label("loc_73D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_79F")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_832")
    SetChrPos(0xD, -21460, 8000, 58770, 270)
    SetChrPos(0x10, -20870, 8000, 59640, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -23240, 8000, 57820, 45)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -23310, 8000, 59800, 135)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_868")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_89E")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -25190, 8000, 66790, 275)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -17150, 8000, 63800, 358)
    Jump("loc_E6F")

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_98D")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -23800, 10000, 46930, 180)
    OP_43(0x11, 0x0, 0x0, 0x3)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -23170, 8000, 59080, 91)
    OP_43(0x12, 0x0, 0x0, 0x5)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -25200, 8000, 67400, 272)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -31870, 10000, 49240, 326)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -33120, 10000, 50470, 135)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -48310, 22000, 49830, 163)
    Jump("loc_E6F")

    label("loc_98D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_CF9")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -30660, 9000, 60810, 69)
    OP_43(0xA, 0x0, 0x0, 0x3)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, -24500, 8750, 51360, 18)
    OP_51(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -34110, 10000, 62990, 166)
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -27110, 8000, 60420, 69)
    SetChrFlags(0x1B, 0x10)
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -27070, 8000, 59620, 359)
    SetChrFlags(0x1C, 0x10)
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -33870, 10000, 57010, 292)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -30810, 10000, 48800, 320)
    OP_43(0x1D, 0x0, 0x0, 0x7)
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32630, 10000, 58920, 255)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -26600, 8000, 55790, 279)
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -21730, 8000, 53410, 270)
    OP_43(0x1F, 0x0, 0x0, 0x8)
    OP_51(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -29430, 8000, 57220, 85)
    SetChrFlags(0x17, 0x10)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -22660, 8000, 61960, 82)
    OP_43(0x21, 0x0, 0x0, 0xA)
    OP_51(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -33530, 10000, 52430, 296)
    OP_51(0x22, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -33770, 10000, 51140, 330)
    OP_51(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -25860, 8000, 60310, 263)
    OP_51(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -21670, 8000, 66490, 242)
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -23200, 10000, 47850, 272)
    OP_43(0x20, 0x0, 0x0, 0x9)
    OP_51(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -30230, 10000, 47900, 298)
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6F")

    label("loc_CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D4C")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    Jump("loc_E6F")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_D82")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_DB8")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_E10")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_E6F")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E6F")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)

    label("loc_E6F")

    Return()

    # Function_0_6A6 end

    def Function_1_E70(): pass

    label("Function_1_E70")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x30052)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9A")
    OP_B1("t3101_y")
    Jump("loc_EA3")

    label("loc_E9A")

    OP_B1("t3101_n")

    label("loc_EA3")

    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF6")

    label("loc_EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF6")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0A")
    OP_72(0x3, 0x10)
    Jump("loc_F0E")

    label("loc_F0A")

    OP_64(0x0, 0x1)

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1090")
    LoadEffect(0x0, "map\\\\mp011_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -49690, 25000, 54030, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39390, 22000, 56200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39390, 22000, 61640, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39850, 19620, 65980, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -39770, 17290, 50070, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x0, 0xFF, 0xFF, -37130, 10000, 58950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)

    label("loc_1090")

    OP_72(0x0, 0x10)
    OP_6F(0x0, 60)

    label("loc_109C")

    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x27, 0x0, 0x0, 0x2)
    Return()

    # Function_1_E70 end

    def Function_2_10C0(): pass

    label("Function_2_10C0")

    OP_72(0x5, 0x20)
    OP_72(0x4, 0x20)

    label("loc_10CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10F5")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_10CA")

    label("loc_10F5")

    Return()

    # Function_2_10C0 end

    def Function_3_10F6(): pass

    label("Function_3_10F6")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1126")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1268")

    label("loc_1126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1268")

    label("loc_113F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1158")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1268")

    label("loc_1158")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1171")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1268")

    label("loc_1171")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1268")

    label("loc_118A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A3")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1268")

    label("loc_11A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BC")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1268")

    label("loc_11BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1268")

    label("loc_11D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1268")

    label("loc_11EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1207")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1268")

    label("loc_1207")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1220")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1268")

    label("loc_1220")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1239")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1268")

    label("loc_1239")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1252")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1268")

    label("loc_1252")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1268")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_127D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1268")

    label("loc_127D")

    Return()

    # Function_3_10F6 end

    def Function_4_127E(): pass

    label("Function_4_127E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A1")
    OP_8D(0xFE, -35270, 61360, -33040, 64150, 3000)
    Jump("Function_4_127E")

    label("loc_12A1")

    Return()

    # Function_4_127E end

    def Function_5_12A2(): pass

    label("Function_5_12A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C5")
    OP_8D(0xFE, -26390, 55950, -19770, 61950, 3000)
    Jump("Function_5_12A2")

    label("loc_12C5")

    Return()

    # Function_5_12A2 end

    def Function_6_12C6(): pass

    label("Function_6_12C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E9")
    OP_8D(0xFE, -25190, 68440, -20920, 71850, 3000)
    Jump("Function_6_12C6")

    label("loc_12E9")

    Return()

    # Function_6_12C6 end

    def Function_7_12EA(): pass

    label("Function_7_12EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130D")
    OP_8D(0xFE, -32689, 46510, -30620, 50700, 3000)
    Jump("Function_7_12EA")

    label("loc_130D")

    Return()

    # Function_7_12EA end

    def Function_8_130E(): pass

    label("Function_8_130E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1331")
    OP_8D(0xFE, -25190, 54660, -20780, 60740, 3000)
    Jump("Function_8_130E")

    label("loc_1331")

    Return()

    # Function_8_130E end

    def Function_9_1332(): pass

    label("Function_9_1332")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1355")
    OP_8D(0xFE, -26510, 46520, -19100, 49060, 3000)
    Jump("Function_9_1332")

    label("loc_1355")

    Return()

    # Function_9_1332 end

    def Function_10_1356(): pass

    label("Function_10_1356")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1379")
    OP_8D(0xFE, -23960, 59250, -21170, 66410, 3000)
    Jump("Function_10_1356")

    label("loc_1379")

    Return()

    # Function_10_1356 end

    def Function_11_137A(): pass

    label("Function_11_137A")

    Return()

    # Function_11_137A end

    def Function_12_137B(): pass

    label("Function_12_137B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_13DC")

    ChrTalk(    #0
        0xFE,
        (
            "#690FThat is a LOT of smoke.\x02\x03",

            "If the central factory's fans\x01",
            "can't catch it all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DC")

    TalkEnd(0xFE)
    Return()

    # Function_12_137B end

    def Function_13_13E0(): pass

    label("Function_13_13E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1441")

    ChrTalk(    #1
        0xFE,
        (
            "I haven't run that hard in I don't\x01",
            "know how long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Ugh, I don't feel right...\x02",
    )

    CloseMessageWindow()

    label("loc_1441")

    TalkEnd(0xFE)
    Return()

    # Function_13_13E0 end

    def Function_14_1445(): pass

    label("Function_14_1445")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(    #3
        0xFE,
        "Back there is all smoke now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "*gasp* *pant* I really thought\x01",
            "I was done for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A7")

    TalkEnd(0xFE)
    Return()

    # Function_14_1445 end

    def Function_15_14AB(): pass

    label("Function_15_14AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_14EE")

    ChrTalk(    #5
        0xFE,
        "Is anyone injured?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Please speak up if you are.\x02",
    )

    CloseMessageWindow()

    label("loc_14EE")

    TalkEnd(0xFE)
    Return()

    # Function_15_14AB end

    def Function_16_14F2(): pass

    label("Function_16_14F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1548")

    ChrTalk(    #7
        0xFE,
        "Wh-What do we do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If there's a fire, we'll lose all\x01",
            "of our data!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1548")

    TalkEnd(0xFE)
    Return()

    # Function_16_14F2 end

    def Function_17_154C(): pass

    label("Function_17_154C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_15EC")

    ChrTalk(    #9
        0xFE,
        "...Strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "That isn't smoke from a fire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "And there are no explosive\x01",
            "experiments going on right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "So what's making that smoke?\x02",
    )

    CloseMessageWindow()

    label("loc_15EC")

    TalkEnd(0xFE)
    Return()

    # Function_17_154C end

    def Function_18_15F0(): pass

    label("Function_18_15F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(    #13
        0xFE,
        "It seems everyone got out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "For a moment I flashed back\x01",
            "to the sky bandits' attack,\x01",
            "and my legs just froze. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_1672")

    TalkEnd(0xFE)
    Return()

    # Function_18_15F0 end

    def Function_19_1676(): pass

    label("Function_19_1676")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1721")

    ChrTalk(    #15
        0xFE,
        (
            "Now that I think about it,\x01",
            "I haven't seen Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "No matter though. He's probably\x01",
            "just shut himself up in the lab\x01",
            "and lost himself in work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A7")

    label("loc_1721")

    OP_A2(0xA)

    ChrTalk(    #17
        0xFE,
        (
            "Going up and down those stairs?\x01",
            "No problem at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "If it weren't for them, what\x01",
            "would we do? Jump off the\x01",
            "damn terrace?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A7")

    Jump("loc_17F4")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_17F4")

    ChrTalk(    #19
        0xFE,
        "Owowowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I threw out my back on those\x01",
            "blasted stairs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F4")

    TalkEnd(0xFE)
    Return()

    # Function_19_1676 end

    def Function_20_17F8(): pass

    label("Function_20_17F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_18AC")

    ChrTalk(    #21
        0xFE,
        (
            "We were in the middle of a\x01",
            "meeting when the place\x01",
            "filled up with smoke...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It was all I could do to get\x01",
            "myself out of there safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I hope nobody got left.\x02",
    )

    CloseMessageWindow()

    label("loc_18AC")

    TalkEnd(0xFE)
    Return()

    # Function_20_17F8 end

    def Function_21_18B0(): pass

    label("Function_21_18B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_18CD")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #24
        0xFE,
        "NIIYAAO!\x02",
    )

    CloseMessageWindow()

    label("loc_18CD")

    TalkEnd(0xFE)
    Return()

    # Function_21_18B0 end

    def Function_22_18D1(): pass

    label("Function_22_18D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_1951")

    ChrTalk(    #25
        0xFE,
        (
            "Ugh. The building is all\x01",
            "full of smoke now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I'm finished for today. I don't\x01",
            "care. I'm going home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7F")

    label("loc_1951")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19D1")

    ChrTalk(    #27
        0xFE,
        (
            "Ugh. The entire building\x01",
            "smells like smoke now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I'm finished for today. I don't\x01",
            "care. I'm going home.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_1B7F")

    label("loc_19D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1A6C")

    ChrTalk(    #29
        0xFE,
        (
            "Ugh. The entire building\x01",
            "smells like smoke now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "So I'm just going home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Sorry. Can you bring me that\x01",
            "book tomorrow instead?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_1B7F")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1B08")

    ChrTalk(    #32
        0xFE,
        (
            "Ugh. The entire building\x01",
            "smells like smoke now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "So I'm just going home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If you want to talk about that\x01",
            "job, ask me tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_1B7F")

    label("loc_1B08")


    ChrTalk(    #35
        0xFE,
        (
            "Thanks to all that running\x01",
            "all my muscles are sore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I'm finished for today. I don't\x01",
            "care. I'm going home.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_1B7F")

    Jump("loc_1BD4")

    label("loc_1B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1BD4")

    ChrTalk(    #37
        0xFE,
        (
            "How many years has it been\x01",
            "since I've moved that fast...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_1BD4")

    TalkEnd(0xFE)
    Return()

    # Function_22_18D1 end

    def Function_23_1BD8(): pass

    label("Function_23_1BD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1C78")

    ChrTalk(    #39
        0x9,
        (
            "#800FIf the professor is here, he'll\x01",
            "be in the workshop up on 3.\x02\x03",

            "Check there first. And make sure\x01",
            "you get out at the slightest sign\x01",
            "of trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C78")

    TalkEnd(0xFE)
    Return()

    # Function_23_1BD8 end

    def Function_24_1C7C(): pass

    label("Function_24_1C7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1CEA")

    ChrTalk(    #40
        0x8,
        (
            "#154FI really want to go with you all,\x01",
            "but I guess that's out...\x02\x03",

            "Estelle, you all be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEA")

    TalkEnd(0xFE)
    Return()

    # Function_24_1C7C end

    def Function_25_1CEE(): pass

    label("Function_25_1CEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1D4B")

    ChrTalk(    #41
        0xFE,
        (
            "H-Have all the guests been\x01",
            "properly evacuated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "This smoke is incredible.\x02",
    )

    CloseMessageWindow()

    label("loc_1D4B")

    TalkEnd(0xFE)
    Return()

    # Function_25_1CEE end

    def Function_26_1D4F(): pass

    label("Function_26_1D4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1DC8")

    ChrTalk(    #43
        0xFE,
        (
            "I can't find Professor Russell\x01",
            "anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "He wouldn't still be inside...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Oh, what should I do?!\x02",
    )

    CloseMessageWindow()

    label("loc_1DC8")

    TalkEnd(0xFE)
    Return()

    # Function_26_1D4F end

    def Function_27_1DCC(): pass

    label("Function_27_1DCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1DEF")

    ChrTalk(    #46
        0xFE,
        "Rudi, are you okay?\x02",
    )

    CloseMessageWindow()

    label("loc_1DEF")

    TalkEnd(0xFE)
    Return()

    # Function_27_1DCC end

    def Function_28_1DF3(): pass

    label("Function_28_1DF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1E57")

    ChrTalk(    #47
        0xFE,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Sm-smoke... *hack* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "...in...lungs... *cough* *hack*\x02",
    )

    CloseMessageWindow()

    label("loc_1E57")

    TalkEnd(0xFE)
    Return()

    # Function_28_1DF3 end

    def Function_29_1E5B(): pass

    label("Function_29_1E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1EE1")

    ChrTalk(    #50
        0xFE,
        (
            "Did you see how many soldiers\x01",
            "came out of there? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "They didn't seem to have any\x01",
            "problems with the smoke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F43")

    label("loc_1EE1")

    OP_A2(0xD)

    ChrTalk(    #52
        0xFE,
        (
            "This is some mess, all this\x01",
            "smoke in the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "My throat's all dried out!\x02",
    )

    CloseMessageWindow()

    label("loc_1F43")

    Jump("loc_2035")

    label("loc_1F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1F85")

    ChrTalk(    #54
        0xFE,
        "Aaahh, man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "What is going ON around here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2035")

    label("loc_1F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2035")

    ChrTalk(    #56
        0xFE,
        (
            "I've got to be the only pilot in\x01",
            "the kingdom who flies an orbalship\x01",
            "while wearing a maintenance uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "It's not about looks though,\x01",
            "right? It's about SKILL.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2035")

    TalkEnd(0xFE)
    Return()

    # Function_29_1E5B end

    def Function_30_2039(): pass

    label("Function_30_2039")

    TalkBegin(0x18)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2099")
    OP_0D()
    OP_A9(0x4D)
    OP_56(0x0)
    TalkEnd(0x18)
    Return()

    label("loc_2099")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20AA")
    TalkEnd(0x18)
    Return()

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_END)), "loc_2126")

    ChrTalk(    #58
        0x18,
        (
            "Looks like the Royal Army\x01",
            "fleet is coming into port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x18,
        (
            "That's funny, there ain't nothing\x01",
            "going on here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_221B")

    ChrTalk(    #60
        0x18,
        (
            "Workin' hard, or hardly\x01",
            "workin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x18,
        (
            "I tell ya', the factory ship's sure been\x01",
            "getting a workout lately. Been in and out\x01",
            "of port a lot, and on really short notice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x18,
        (
            "The boarding pad has been pretty\x01",
            "quiet this morning, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_221B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_22FA")

    ChrTalk(    #63
        0x18,
        "Looks like another busy day!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x18,
        (
            "Speaking of busy, Rehmann just\x01",
            "came running up here like a\x01",
            "madman a little bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x18,
        (
            "Seems he had to get a factory\x01",
            "ship out of here in a hurry.\x01",
            "That must've been a pain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_22FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2367")

    ChrTalk(    #66
        0x18,
        "Morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x18,
        (
            "There ain't nothing like one of\x01",
            "these energy drinks first thing\x01",
            "in the morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_241E")

    ChrTalk(    #68
        0x18,
        "Thanks for working so late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x18,
        (
            "Geez, what a busy day.\x01",
            "I'm completely exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x18,
        (
            "I'm closing up shop soon, so\x01",
            "if there's something you want,\x01",
            "you better speak up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_241E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_24AA")

    ChrTalk(    #71
        0x18,
        (
            "I saw a bunch of guys in blue \x01",
            "military uniforms come out of\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x18,
        "What were they doing in there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_252F")

    label("loc_24AA")

    OP_A2(0xB)

    ChrTalk(    #73
        0x18,
        (
            "Whew. Looks like the big\x01",
            "fuss is finally over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x18,
        (
            "What were those military guys\x01",
            "doing under all that smoke,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252F")

    Jump("loc_2934")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_259A")

    ChrTalk(    #75
        0x18,
        "O-Okay, everybody, just relax!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x18,
        (
            "Here, everyone just have a\x01",
            "cold drink and calm down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_26B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2632")

    ChrTalk(    #77
        0x18,
        (
            "Yeah, that guy Rehmann over\x01",
            "there? He's a pilot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x18,
        (
            "Of course, he only flies the\x01",
            "factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x18,
        "But flying's flying, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B6")

    label("loc_2632")

    OP_A2(0xB)

    ChrTalk(    #80
        0x18,
        (
            "That guy Rehmann over there\x01",
            "looks like a mechanic, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x18,
        "Really, the guy's a pilot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x18,
        "Books and covers, right? Ha!\x02",
    )

    CloseMessageWindow()

    label("loc_26B6")

    Jump("loc_2934")

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_27FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(    #83
        0x18,
        (
            "I can't just think about sales. I have\x01",
            "to worry about management, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x18,
        (
            "Having a 'down home, friendly'\x01",
            "store is an easy thing to say,\x01",
            "but hard to actually do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F8")

    label("loc_2772")

    OP_A2(0xB)

    ChrTalk(    #85
        0x18,
        (
            "Our dream is to have at least\x01",
            "one store of our own some day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x18,
        (
            "I'd love to have a warm little\x01",
            "store like the Bell Station.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F8")

    Jump("loc_2934")

    label("loc_27FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2876")

    ChrTalk(    #87
        0x18,
        (
            "The girl selling flowers over\x01",
            "there? Irene? She's my sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x18,
        (
            "Go on and take a look at her\x01",
            "flower shop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_28E1")

    ChrTalk(    #89
        0x18,
        "How about a nice, cold drink?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x18,
        (
            "We carry all kinds of good\x01",
            "and healthy stuff!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2934")

    label("loc_28E1")

    OP_A2(0xB)

    ChrTalk(    #91
        0x18,
        (
            "You look like you've been\x01",
            "working hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x18,
        "How about a nice, cold drink?\x02",
    )

    CloseMessageWindow()

    label("loc_2934")

    TalkEnd(0x18)
    Return()

    # Function_30_2039 end

    def Function_31_2938(): pass

    label("Function_31_2938")

    TalkBegin(0x19)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2998")
    OP_0D()
    OP_A9(0x4E)
    OP_56(0x0)
    TalkEnd(0x19)
    Return()

    label("loc_2998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29A9")
    TalkEnd(0x19)
    Return()

    label("loc_29A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_END)), "loc_2A09")

    ChrTalk(    #93
        0x19,
        (
            "I heard a siren coming from\x01",
            "the boarding area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x19,
        "...I wonder what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A89")

    ChrTalk(    #95
        0x19,
        (
            "I have all kinds of beautiful\x01",
            "flowers! Please have a look!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x19,
        (
            "How about a flower to help\x01",
            "forget your troubles?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2B1A")

    ChrTalk(    #97
        0x19,
        (
            "*sigh* All the people are too\x01",
            "busy talking to even LOOK\x01",
            "at my flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x19,
        (
            "Oh well. It's to be expected.\x01",
            "It was quite an ordeal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2B59")

    ChrTalk(    #99
        0x19,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x19,
        "Don't my flowers smell nice?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2BA4")

    ChrTalk(    #101
        0x19,
        "Good evening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x19,
        (
            "There's still time before\x01",
            "I close today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C34")

    ChrTalk(    #103
        0x19,
        (
            "Just when the smoke stopped,\x01",
            "all of those soldiers came out\x01",
            "of the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x19,
        (
            "Do you think they were the\x01",
            "ones who stopped it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2C53")

    ChrTalk(    #105
        0x19,
        "Oh my goodness!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2CC2")

    ChrTalk(    #106
        0x19,
        "Zeiss has so few trees.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x19,
        (
            "I'd love to take a trip to see the\x01",
            "flowers in the town of Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D40")

    ChrTalk(    #108
        0x19,
        (
            "That's my brother over there\x01",
            "selling drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x19,
        (
            "Our dream is to make enough\x01",
            "money to open our own store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D99")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D99")

    ChrTalk(    #110
        0x19,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x19,
        (
            "I have all kinds of beautiful\x01",
            "flowers! Please have a look!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D99")

    TalkEnd(0x19)
    Return()

    # Function_31_2938 end

    def Function_32_2D9D(): pass

    label("Function_32_2D9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2DF3")

    ChrTalk(    #112
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Think I'll have a drink to calm\x01",
            "my nerves a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E42")

    label("loc_2DF3")

    OP_A2(0x6)

    ChrTalk(    #114
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I can't believe this. I don't think\x01",
            "I can go back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E42")

    TalkEnd(0xFE)
    Return()

    # Function_32_2D9D end

    def Function_33_2E46(): pass

    label("Function_33_2E46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2EEF")

    ChrTalk(    #116
        0xFE,
        (
            "I'm glad to see you're okay, \x01",
            "but I haven't seen Russell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "He's probably okay, though.\x01",
            "I'm pretty sore over here,\x01",
            "but I'm sure he's fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2EEF")

    OP_A2(0x7)

    ChrTalk(    #118
        0xFE,
        (
            "Look at you, Igor. How did you\x01",
            "manage not to get hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "You really barreled down the\x01",
            "emergency stairs. That must\x01",
            "have been tough on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F84")

    TalkEnd(0xFE)
    Return()

    # Function_33_2E46 end

    def Function_34_2F88(): pass

    label("Function_34_2F88")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_34_2F88 end

    def Function_35_2F8F(): pass

    label("Function_35_2F8F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_35_2F8F end

    def Function_36_2F96(): pass

    label("Function_36_2F96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_303E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2FE6")

    ChrTalk(    #120
        0xFE,
        (
            "Royal Guard uniforms...\x01",
            "That is troubling news indeed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303E")

    label("loc_2FE6")

    OP_A2(0x0)

    ChrTalk(    #121
        0xFE,
        (
            "Do you think the people\x01",
            "responsible for the attack\x01",
            "were really Royal Guardsmen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_303E")

    TalkEnd(0xFE)
    Return()

    # Function_36_2F96 end

    def Function_37_3042(): pass

    label("Function_37_3042")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30AF")

    ChrTalk(    #122
        0xFE,
        "I just can't calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Maybe some nice flowers will \x01",
            "help me clear my head...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3156")

    label("loc_30AF")

    OP_A2(0x1)

    ChrTalk(    #124
        0xFE,
        "Still though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "They still haven't found the ones who\x01",
            "attacked the central factory yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Are the Royal Army and the\x01",
            "Bracer Guild even doing\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3156")

    Jump("loc_34EB")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3204")

    ChrTalk(    #127
        0xFE,
        (
            "I've asked lots of people and\x01",
            "they all say they saw soldiers\x01",
            "in blue at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Vince saw them, too. I never did\x01",
            "trust those puffed up guardsmen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EB")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_328F")

    ChrTalk(    #129
        0xFE,
        (
            "Every time I go shopping, \x01",
            "Vince starts to complain\x01",
            "about every little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "He can be so difficult sometimes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3471")

    label("loc_328F")

    OP_A2(0x1)
    TurnDirection(0xD, 0x107, 400)

    ChrTalk(    #131
        0xFE,
        (
            "Hello, Tita. Showing some\x01",
            "guests around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        (
            "#060FOh, hello, Elise.\x02\x03",

            "Looking for some new flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "Yes, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Every time I go shopping, \x01",
            "Vince starts to complain\x01",
            "about every little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "He's as particular as certain\x01",
            "other people I could name.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xD, 400)

    ChrTalk(    #136
        0x10,
        (
            "I'm not obsessive, it's just that\x01",
            "Mother can be so obtuse.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 300)
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0xFE,
        "What did you just say?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #138
        0x107,
        "#065FPlease, don't fight...\x02",
    )

    CloseMessageWindow()

    label("loc_3471")

    Jump("loc_34EB")

    label("loc_3474")


    ChrTalk(    #139
        0xFE,
        "Ooh, look at these flowers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I'd love to plant these on the\x01",
            "veranda, but I'm afraid the\x01",
            "colors might clash...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EB")

    TalkEnd(0xFE)
    Return()

    # Function_37_3042 end

    def Function_38_34EF(): pass

    label("Function_38_34EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_35C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_358D")

    ChrTalk(    #141
        0xFE,
        (
            "Even the Royal Guardsmen were\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "Jackpot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Okay, that's it. I am SO going\x01",
            "to be a receptionist at the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C4")

    label("loc_358D")

    OP_A2(0x2)

    ChrTalk(    #144
        0xFE,
        (
            "What?!\x01",
            "The Royal Guard were here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Score!\x02",
    )

    CloseMessageWindow()

    label("loc_35C4")

    TalkEnd(0xFE)
    Return()

    # Function_38_34EF end

    def Function_39_35C8(): pass

    label("Function_39_35C8")

    TalkBegin(0xFE)

    ChrTalk(    #146
        0xFE,
        "I don't think it's a fire...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "So what's all that smoke then?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_35C8 end

    def Function_40_3615(): pass

    label("Function_40_3615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_371F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_36A0")

    ChrTalk(    #148
        0xFE,
        (
            "No one knows if the people \x01",
            "in the blue uniforms were \x01",
            "really soldiers or not yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Who could they have been?\x02",
    )

    CloseMessageWindow()
    Jump("loc_371C")

    label("loc_36A0")

    OP_A2(0x3)

    ChrTalk(    #150
        0xFE,
        (
            "I'm sure both the Royal Guardsmen\x01",
            "and the Bracer Guild are doing the\x01",
            "best they can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "We just aren't hearing it.\x02",
    )

    CloseMessageWindow()

    label("loc_371C")

    Jump("loc_388C")

    label("loc_371F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_378B")

    ChrTalk(    #152
        0xFE,
        (
            "What I said I saw were, 'Men\x01",
            "in blue soldiers' uniforms.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "I didn't say Royal Guardsmen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_388C")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_37D5")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #154
        0xFE,
        (
            "Keep up the hard work at \x01",
            "the factory, Tita.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3853")

    label("loc_37D5")

    TurnDirection(0xFE, 0x107, 0)
    OP_A2(0x3)

    ChrTalk(    #155
        0xFE,
        "Hello, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x107,
        "#560FHello, Vince!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Off to work at the factory?\x01",
            "Well, do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x107,
        "#061FThank you!\x02",
    )

    CloseMessageWindow()

    label("loc_3853")

    Jump("loc_388C")

    label("loc_3856")


    ChrTalk(    #159
        0xFE,
        (
            "Mother, there are enough flowers\x01",
            "on the veranda.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_388C")

    TalkEnd(0xFE)
    Return()

    # Function_40_3615 end

    def Function_41_3890(): pass

    label("Function_41_3890")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3972")

    ChrTalk(    #160
        0xFE,
        (
            "I guess I better be getting\x01",
            "back to the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Here I am giving stuff away for\x01",
            "free... I'm sure my wife'll have a\x01",
            "field day with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "But I was able to help some\x01",
            "people out, so that's good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A4C")

    label("loc_3972")

    OP_A2(0x4)

    ChrTalk(    #163
        0xFE,
        "Finally...the smoke's cleared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I'm glad to hear there were\x01",
            "no injuries at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I heard some stuff was stolen,\x01",
            "but they can just build more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I guess I better be getting\x01",
            "back to the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4C")

    Jump("loc_3D86")

    label("loc_3A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(    #167
        0xFE,
        "Try to help wherever you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "Be careful out there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D86")

    label("loc_3A9E")

    OP_A2(0x4)

    ChrTalk(    #169
        0xFE,
        "Hey, are you guys all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I'm Elwyn, from the general\x01",
            "goods store. I heard something\x01",
            "happened and ran over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I brought some stuff from \x01",
            "my store, too, so if you need\x01",
            "anything just let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "This is an emergency!\x01",
            "Don't worry about the money.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Proxy Puppet]\x01",        # 0
            "[Celestial Balm]\x01",      # 1
            "[Petrify]\x01",             # 2
        )
    )

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C76")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #173
        "\x07\x00Received \x07\x02Proxy Puppet\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x145, 1)
    Jump("loc_3D30")

    label("loc_3C76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CDB")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #174
        "\x07\x00Received \x07\x02Celestial Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1FD, 1)
    Jump("loc_3D30")

    label("loc_3CDB")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #175
        "\x07\x00Received \x07\x02Petrify Quartz\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x27F, 1)

    label("loc_3D30")

    Sleep(100)

    ChrTalk(    #176
        0xFE,
        "There you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Try to help wherever you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "Be careful out there!\x02",
    )

    CloseMessageWindow()

    label("loc_3D86")

    TalkEnd(0xFE)
    Return()

    # Function_41_3890 end

    def Function_42_3D8A(): pass

    label("Function_42_3D8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_3ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3E41")

    ChrTalk(    #179
        0xFE,
        (
            "I can't believe something like\x01",
            "this would happen while I\x01",
            "wasn't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "I'll never be able to look Gundolf\x01",
            "in the eye... He left me in charge\x01",
            "of things!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC9")

    label("loc_3E41")

    OP_A2(0x5)

    ChrTalk(    #181
        0xFE,
        (
            "The central factory was\x01",
            "attacked...inconceivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "I need to get back to the guild and\x01",
            "check in on the current situation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC9")

    Jump("loc_437F")

    label("loc_3ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_437F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3F80")

    ChrTalk(    #183
        0xFE,
        (
            "I can't believe something like\x01",
            "this would happen while I\x01",
            "wasn't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "I'll never be able to look Gundolf\x01",
            "in the eye... He left me in charge\x01",
            "of things!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3F80")

    OP_A2(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4272")
    OP_A2(0x5CD)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #185
        0xFE,
        "It's you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        "#501FWong...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "I...I just got back to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "What in the Goddess' name\x01",
            "is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#003FWell, you see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #190
        0x106,
        (
            "#050FHey, what are you doing?\x02\x03",

            "Get your butts back to the guild!\x01",
            "We've got no time for chit-chat!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #191
        0x101,
        (
            "#009FGrrr...\x02\x03",

            "#007FI hate it when Agate's right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #192
        0x102,
        "#018FI don't know why...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x12, 400)

    ChrTalk(    #193
        0x106,
        (
            "#053FI'm talking to you, TOO!\x02\x03",

            "You're a bracer, aren't you?\x01",
            "Get out there!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #194
        0xFE,
        "You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "Sorry, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x106,
        (
            "#053FHmph.\x02\x03",

            "Our job's to worry about what\x01",
            "to do next, not what's already\x01",
            "said and done.\x02\x03",

            "#050FLet's get moving.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_421A():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_421A)
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(    #197
        0x101,
        "#000FBye, Wong...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #198
        0xFE,
        "Okay. See you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#010FLet's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42F7")

    label("loc_4272")


    ChrTalk(    #200
        0xFE,
        (
            "The central factory was\x01",
            "attacked...inconceivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "I need to get back to the guild and\x01",
            "check in on the current situation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F7")

    Jump("loc_437F")

    label("loc_42FA")


    ChrTalk(    #202
        0xFE,
        (
            "The central factory was\x01",
            "attacked...inconceivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "I need to get back to the guild and\x01",
            "check in on the current situation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437F")

    TalkEnd(0xFE)
    Return()

    # Function_42_3D8A end

    def Function_43_4383(): pass

    label("Function_43_4383")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x546)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A2(0x546)
    Return()

    # Function_43_4383 end

    def Function_44_4399(): pass

    label("Function_44_4399")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #204
        "\x07\x05Pressing the button does nothing. The elevator cannot be used at the moment.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_44_4399 end

    def Function_45_4421(): pass

    label("Function_45_4421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_451A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449C")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(    #205
        0x102,
        (
            "#012FI'm concerned about the\x01",
            "professor. We have to check\x01",
            "out the central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FC")

    label("loc_449C")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(    #206
        0x102,
        (
            "#012FI'm concerned about the\x01",
            "professor. Why don't we check\x01",
            "out the central factory?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FC")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_477E")

    label("loc_451A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477E")
    OP_A2(0x50B)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_8C(0x102, 90, 0)
    OP_8C(0x101, 90, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #207
        0x101,
        "#004FWhoa, what's this?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(6010, 2000, 59020, 0)
    OP_67(0, 2920, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -13400, 8000, 59680, 90)
    SetChrPos(0x102, -13620, 8000, 58750, 90)
    OP_0D()

    def lambda_45FA():
        OP_6D(-13820, 9000, 59010, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45FA)
    Sleep(1000)
    OP_67(0, 11000, -10000, 5000)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    Fade(1000)
    OP_6D(-13480, 8000, 59160, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #208
        0x102,
        (
            "#014FSome kind of...moving staircase.\x02\x03",

            "It IS a really long climb,\x01",
            "so I guess it would be tough\x01",
            "without it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#007FYeah, but to have the whole\x01",
            "thing moving underneath you?\x02\x03",

            "#509FThis place has been full\x01",
            "of surprises ever since\x01",
            "we got here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        "#019FNo kidding.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_477E")

    Return()

    # Function_45_4421 end

    def Function_46_477F(): pass

    label("Function_46_477F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-35180, 10000, 58970, 0)
    OP_6B(2410, 0)
    OP_6C(270000, 0)
    SetChrPos(0x101, -34470, 10000, 59690, 225)
    SetChrPos(0x102, -34480, 10000, 58410, 315)
    SetChrPos(0x107, -35490, 10000, 59000, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497F")

    ChrTalk(    #211
        0x101,
        (
            "#501FSo...Elmo.\x01",
            "Sounds kinda fun.\x02\x03",

            "There's a hot spring there,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x107,
        (
            "#061FRight. It's a real nice place.\x02\x03",

            "My grandpa's taken me there\x01",
            "a few times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x102,
        "#010FSo which way do we go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x107,
        (
            "#560FHmmm...\x02\x03",

            "There's a big field outside the\x01",
            "south entrance of town.\x02\x03",

            "You just follow that road\x01",
            "due south to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#006FGot it. Due south from\x01",
            "the south entrance.\x02\x03",

            "#001FWell, let's go, then!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD0")

    label("loc_497F")


    ChrTalk(    #216
        0x101,
        (
            "#501FSo...Elmo.\x01",
            "Sounds kinda fun.\x02\x03",

            "There's a hot spring there,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x107,
        (
            "#061FRight. It's a real nice place.\x02\x03",

            "My grandpa's taken me there\x01",
            "a few times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x102,
        (
            "#010FWell, then. Let's set out.\x02\x03",

            "Just go out the south entrance,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x107,
        (
            "#560FRight. Then just follow along\x01",
            "the south road to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#006FOkay. Let's get going!\x02",
    )

    CloseMessageWindow()

    label("loc_4AD0")

    OP_28(0x40, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_46_477F end

    def Function_47_4AD9(): pass

    label("Function_47_4AD9")

    EventBegin(0x0)
    OP_28(0x41, 0x4, 0x2)
    OP_28(0x41, 0x4, 0x4)
    OP_28(0x41, 0x1, 0x1)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 60)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_6D(-14970, 8000, 55370, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(224000, 0)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    RemoveParty(0xF, 0xFF)
    SetChrPos(0x101, -14050, 8000, 56120, 270)
    SetChrPos(0x102, -13280, 8000, 55260, 270)
    SetChrPos(0x107, -13040, 8000, 57050, 270)
    SetChrPos(0x8, -12520, 8000, 56020, 270)
    SetChrPos(0x1C, -37650, 10000, 59010, 0)
    SetChrPos(0x1B, -37650, 10000, 59010, 0)
    SetChrPos(0x17, -37650, 10000, 59010, 0)
    SetChrPos(0xB, -37650, 10000, 59010, 0)
    SetChrPos(0xA, -37650, 10000, 59010, 0)
    SetChrPos(0x9, -26520, 8000, 57300, 0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xB, 0x80)

    def lambda_4C22():

        label("loc_4C22")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4C22")

    QueueWorkItem2(0xB, 1, lambda_4C22)

    def lambda_4C33():
        OP_8E(0xFE, 0xFFFF9E12, 0x1F40, 0xE2CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4C33)
    FadeToBright(2000, 0)
    OP_20(0x5DC)
    OP_0D()
    OP_21()
    OP_1D(0x51)

    ChrTalk(    #221
        0x101,
        "#004F#5PHuh?!\x02",
    )

    CloseMessageWindow()

    def lambda_4C73():
        OP_6D(-25700, 8000, 55810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C73)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    FadeToBright(2000, 0)
    StopSound(0x0, 0x3D090, 0x0)
    OP_6D(-35690, 20250, 58940, 0)
    OP_67(0, 20360, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(294000, 0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x23, 0x4)
    SetChrFlags(0xA, 0x80)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x17, 0)
    OP_4A(0xB, 0)
    OP_4A(0xA, 0)
    OP_4A(0x24, 0)
    SetChrPos(0x11, -37650, 10000, 59010, 0)
    SetChrPos(0x22, -37650, 10000, 59010, 0)
    SetChrPos(0x23, -37650, 10000, 59010, 0)
    StopSound(0x0, 0x0, 0x2710)

    def lambda_4DA2():
        OP_6C(225000, 11000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4DA2)
    ClearChrFlags(0xB, 0x80)

    def lambda_4DB7():

        label("loc_4DB7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4DB7")

    QueueWorkItem2(0xB, 1, lambda_4DB7)

    def lambda_4DC8():
        OP_8E(0xFE, 0xFFFF9E12, 0x1F40, 0xE2CC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4DC8)
    Sleep(500)
    ClearChrFlags(0x11, 0x80)

    def lambda_4DED():

        label("loc_4DED")

        OP_8C(0xFE, 166, 0)
        OP_48()
        Jump("loc_4DED")

    QueueWorkItem2(0x11, 1, lambda_4DED)

    def lambda_4DFE():
        OP_8E(0xFE, 0xFFFF7CAC, 0x2710, 0xF000, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4DFE)
    Sleep(500)
    ClearChrFlags(0x17, 0x80)

    def lambda_4E23():

        label("loc_4E23")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_4E23")

    QueueWorkItem2(0x17, 1, lambda_4E23)

    def lambda_4E34():
        OP_8E(0xFE, 0xFFFF8D0A, 0x1F40, 0xDF84, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4E34)
    Sleep(1000)
    ClearChrFlags(0x22, 0x80)

    def lambda_4E59():

        label("loc_4E59")

        OP_8C(0xFE, 296, 0)
        OP_48()
        Jump("loc_4E59")

    QueueWorkItem2(0x22, 1, lambda_4E59)

    def lambda_4E6A():
        OP_8E(0xFE, 0xFFFF7F36, 0x2710, 0xDBF6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_4E6A)

    def lambda_4E85():
        OP_6D(-35440, 14790, 58910, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E85)
    Sleep(1000)

    def lambda_4EA2():
        OP_67(0, 12040, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EA2)
    ClearChrFlags(0x23, 0x80)

    def lambda_4EBF():

        label("loc_4EBF")

        OP_8C(0xFE, 330, 0)
        OP_48()
        Jump("loc_4EBF")

    QueueWorkItem2(0x23, 1, lambda_4EBF)

    def lambda_4ED0():
        OP_8E(0xFE, 0xFFFF7E6E, 0x2710, 0xD886, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_4ED0)
    Sleep(1000)
    ClearChrFlags(0x1C, 0x80)

    def lambda_4EF5():

        label("loc_4EF5")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_4EF5")

    QueueWorkItem2(0x1C, 1, lambda_4EF5)

    def lambda_4F06():
        OP_8E(0xFE, 0xFFFF9642, 0x1F40, 0xE8E4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_4F06)
    Sleep(1000)
    ClearChrFlags(0x1B, 0x80)

    def lambda_4F2B():

        label("loc_4F2B")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_4F2B")

    QueueWorkItem2(0x1B, 1, lambda_4F2B)

    def lambda_4F3C():
        OP_8E(0xFE, 0xFFFF961A, 0x1F40, 0xEC04, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_4F3C)
    Sleep(2000)

    def lambda_4F5C():
        OP_6D(-26430, 8000, 57990, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F5C)

    def lambda_4F74():
        OP_67(0, 11000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F74)

    def lambda_4F8C():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F8C)

    def lambda_4F9C():

        label("loc_4F9C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4F9C")

    QueueWorkItem2(0x9, 1, lambda_4F9C)
    Sleep(300)
    ClearChrFlags(0xA, 0x80)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xA, 0xFFFF96E2, 0x1F40, 0xE54C, 0xFA0, 0x0)
    Sleep(1000)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(    #222
        0xA,
        (
            "*cough* *cough* I...\x01",
            "I thought I was a goner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x9,
        (
            "#800FWell, you're all right.\x01",
            "That's what's important.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(    #224
        0x9,
        "#804FOkay, that's every section, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)

    ChrTalk(    #225
        0xB,
        "It's all the full-timers, at least...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        "#2PChief!\x02",
    )

    CloseMessageWindow()

    def lambda_50CF():
        OP_6D(-25700, 8000, 55810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50CF)

    def lambda_50E7():

        label("loc_50E7")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_50E7")

    QueueWorkItem2(0x9, 1, lambda_50E7)

    def lambda_50F8():

        label("loc_50F8")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_50F8")

    QueueWorkItem2(0xB, 1, lambda_50F8)

    def lambda_5109():

        label("loc_5109")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5109")

    QueueWorkItem2(0xA, 1, lambda_5109)

    def lambda_511A():
        OP_8E(0xFE, 0xFFFFA010, 0x1F40, 0xDD9A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_511A)
    Sleep(300)

    def lambda_513A():
        OP_8E(0xFE, 0xFFFF9F16, 0x1F40, 0xDA0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_513A)
    Sleep(300)

    def lambda_515A():
        OP_8E(0xFE, 0xFFFFA2D6, 0x1F40, 0xE146, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_515A)
    Sleep(300)

    def lambda_517A():
        OP_8E(0xFE, 0xFFFFA52E, 0x1F40, 0xDBA6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_517A)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x9, 0)

    ChrTalk(    #227
        0x9,
        (
            "#802F#2PAh, it's you...\x01",
            "Back from Elmo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#002FWhat's with all the commotion?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x9,
        (
            "#804F#2PThere was some kind of gas\x01",
            "leak inside the building.\x02\x03",

            "Everything from the fifth floor\x01",
            "down is full of fumes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x102,
        "#012F#5PDon't tell us there was a fire...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        (
            "#803F#2PI doubt it, since the extinguishers\x01",
            "haven't been set off.\x02\x03",

            "That doesn't mean I've been\x01",
            "able to figure out why this\x01",
            "is happening, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x107,
        (
            "#063FE-Excuse me, Chief.\x01",
            "Where's my grandpa?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(    #233
        0x9,
        "#802F#2PAh, that's right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(    #234
        0x9,
        (
            "#802F#2PMiss Hazel, is everyone\x01",
            "accounted for?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)

    ChrTalk(    #235
        0xB,
        "#4PW-Well...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0xB, 0)

    ChrTalk(    #236
        0xB,
        (
            "#4PWe're fully staffed today, but\x01",
            "Professor Russell isn't among\x01",
            "those evacuated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x107,
        "#065F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x9,
        (
            "#804F#2PWhat?! You mean he's\x01",
            "still in there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#005FLet us handle this, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        "#012F#5PWe'll figure this out.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(    #241
        0x9,
        "#805F#2PTh-Thank you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #242
        0x107,
        "#065FI-I'm going, too...!\x02",
    )

    CloseMessageWindow()

    def lambda_5519():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5519)

    def lambda_5527():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5527)

    def lambda_5535():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5535)

    def lambda_5543():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5543)

    def lambda_5551():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5551)
    Sleep(400)

    ChrTalk(    #243
        0x101,
        "#004F#2PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x9,
        "#802F#2PTita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x107,
        (
            "#062FI know a lot about the\x01",
            "central factory...\x02\x03",

            "I can show them the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#003F#2PTita...\x02\x03",

            "#002FOkay... Come with us, then.\x01",
            "Stay close!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x102,
        (
            "#012F#5PBut if it gets too dangerous,\x01",
            "you have to come back here,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x107,
        "#063FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        (
            "#155FUmm... Would it be okay\x01",
            "if I came wi--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56B3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56B3)

    def lambda_56C1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56C1)

    def lambda_56CF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_56CF)
    Sleep(400)

    ChrTalk(    #250
        0x101,
        "#002F#2PNo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        (
            "#015F#5PSorry, but we need you\x01",
            "to stay back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x8,
        (
            "#154FGee, thanks for taking the\x01",
            "time to think about it...\x02\x03",

            "But hey, what can you do?\x01",
            "Just be careful, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "#800F#2PIf the professor is in there,\x01",
            "he's probably in the third\x01",
            "floor workshop.\x02\x03",

            "I'd check there, first.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5805():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5805)

    def lambda_5813():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5813)

    def lambda_5821():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5821)
    Sleep(400)

    ChrTalk(    #254
        0x101,
        "#006FGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x102,
        "#012F#5PWe'll be off, then.\x02",
    )

    CloseMessageWindow()
    OP_44(0x21, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x24, 0x1)
    OP_4B(0x21, 0)
    OP_4B(0x11, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x17, 0)
    OP_4B(0xB, 0)
    OP_4B(0xA, 0)
    OP_4B(0x24, 0)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x17, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x22, 0x40)
    ClearChrFlags(0x23, 0x40)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    OP_4B(0xA, 255)
    OP_4B(0x9, 255)
    OP_4B(0xB, 255)
    OP_4B(0x8, 255)
    OP_43(0x9, 0x0, 0x0, 0x3)
    OP_43(0xA, 0x0, 0x0, 0x3)
    OP_43(0xB, 0x0, 0x0, 0x3)
    OP_8C(0x8, 270, 0)
    SetMapFlags(0x2000000)
    SetMapFlags(0x800)
    OP_A2(0x52C)
    EventEnd(0x0)
    Return()

    # Function_47_4AD9 end

    def Function_48_5917(): pass

    label("Function_48_5917")

    EventBegin(0x0)
    OP_6D(-35220, 10000, 59310, 0)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x21, 0)
    OP_4A(0x11, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x17, 0)
    OP_4A(0xB, 0)
    OP_4A(0xA, 0)
    OP_4A(0x24, 0)
    SetChrPos(0x1C, -26070, 8000, 62840, 63)
    SetChrPos(0x1B, -25060, 8000, 63650, 180)
    SetChrPos(0x24, -24740, 8000, 62540, 3)
    SetChrPos(0xB, -37650, 10000, 59010, 0)
    SetChrPos(0xA, -28440, 8000, 62590, 129)
    SetChrPos(0x9, -26520, 8000, 57300, 0)
    SetChrPos(0x101, -34600, 10000, 59260, 90)
    SetChrPos(0x106, -35290, 10000, 58430, 90)
    SetChrPos(0x102, -35240, 10000, 60170, 90)
    SetChrPos(0x107, -35880, 10000, 59390, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -26240, 8000, 58320, 270)
    SetChrPos(0x8, -27270, 8000, 58010, 270)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)

    def lambda_5A3E():

        label("loc_5A3E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5A3E")

    QueueWorkItem2(0x8, 1, lambda_5A3E)

    def lambda_5A4F():

        label("loc_5A4F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5A4F")

    QueueWorkItem2(0x9, 1, lambda_5A4F)

    def lambda_5A60():
        OP_8E(0xFE, 0xFFFF9232, 0x1F40, 0xE6AA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5A60)

    def lambda_5A7B():
        OP_8E(0xFE, 0xFFFF9458, 0x1F40, 0xEA1A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A7B)

    def lambda_5A96():
        OP_8E(0xFE, 0xFFFF9764, 0x1F40, 0xED3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A96)

    def lambda_5AB1():
        OP_8E(0xFE, 0xFFFF8F30, 0x1F40, 0xEC86, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5AB1)

    def lambda_5ACC():
        OP_6D(-27780, 8000, 59800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5ACC)

    def lambda_5AE4():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5AE4)
    FadeToBright(1000, 0)

    def lambda_5AFD():

        label("loc_5AFD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5AFD")

    QueueWorkItem2(0x106, 1, lambda_5AFD)

    def lambda_5B0E():

        label("loc_5B0E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5B0E")

    QueueWorkItem2(0x101, 1, lambda_5B0E)

    def lambda_5B1F():

        label("loc_5B1F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5B1F")

    QueueWorkItem2(0x102, 1, lambda_5B1F)

    def lambda_5B30():

        label("loc_5B30")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5B30")

    QueueWorkItem2(0x107, 1, lambda_5B30)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #256
        0x8,
        "#151FHey, they're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x9,
        (
            "#801FGood, you're all right.\x02\x03",

            "When the soldiers showed\x01",
            "up, I thought something\x01",
            "serious had happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x106,
        "#055F#3PSoldiers...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#005FHold on a second! Soldiers?\x01",
            "Not guys dressed in black?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x9,
        (
            "#802FNo idea what you mean.\x02\x03",

            "They were dressed in blue and\x01",
            "white military uniforms. Polite\x01",
            "enough, but...\x02\x03",

            "I got the feeling they didn't\x01",
            "come from the Air-Letten\x01",
            "checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x8,
        (
            "#151FThey definitely seemed like\x01",
            "Royal Guardsmen to me.\x02\x03",

            "I thought they looked so cool\x01",
            "that I snapped off a picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        "#004FRoyal Guardsmen... Huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x102,
        (
            "#012FThe ones who took away\x01",
            "Mayor Dalmore...\x02\x03",

            "But why would they be here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x107,
        (
            "#062FU-Umm...\x02\x03",

            "They weren't with my grandpa,\x01",
            "were they?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x9,
        (
            "#805FWith the professor...?\x02\x03",

            "N-No... They did have some really\x01",
            "big baggage with them, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x107,
        "#065F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#005FIt had to be them!\x01",
            "No doubt about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x106,
        (
            "#057F#3PIf they changed into military\x01",
            "uniforms in the elevator...\x02\x03",

            "#056FDamn it! It's the oldest trick\x01",
            "in the book, and they pulled\x01",
            "it off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x9,
        (
            "#802FWait... Wait just a minute!\x01",
            "What's all this supposed to\x01",
            "mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#016FWe'll have to fill you in later.\x02\x03",

            "Which way did these soldiers go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x9,
        (
            "#805FT-Towards town...and they moved\x01",
            "like they had a purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x106,
        "#054F#3PWe're going after them!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x40)

    def lambda_603F():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_603F)
    Sleep(200)

    ChrTalk(    #273
        0x101,
        (
            "#005FNo WAY I'm letting them\x01",
            "get away!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_608B():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_608B)
    Sleep(400)

    def lambda_60AB():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60AB)
    Sleep(100)

    def lambda_60CB():
        OP_8E(0xFE, 0xFFFFCC7A, 0x1F40, 0xEB1E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_60CB)
    Sleep(2000)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(    #274
        "\x07\x05And so, Estelle and company split up to search the streets of Zeiss.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #275
        (
            "\x07\x05But in the end, they could find no trace of the men who had taken the\x01",
            "professor.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #276
        (
            "\x07\x05The incident was reported to the Royal Army, and a unit was sent to Zeiss\x01",
            "from the stronghold at the lake, to aid in the investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x40000000)
    ClearMapFlags(0x2000000)
    OP_A2(0x536)
    OP_28(0x41, 0x1, 0x40)
    ClearMapFlags(0x800)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3115   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_48_5917 end

    def Function_49_6274(): pass

    label("Function_49_6274")

    EventBegin(0x0)
    OP_6D(-36480, 10000, 59730, 0)
    OP_67(0, 7190, -10000, 0)
    OP_6B(3350, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, -23800, 10000, 46930, 180)
    OP_43(0x11, 0x0, 0x0, 0x3)
    RemoveParty(0xF, 0xFF)
    SetChrPos(0x101, -34420, 10000, 58850, 270)
    SetChrPos(0x107, -34550, 10000, 57970, 315)
    SetChrPos(0x106, -33590, 10000, 59410, 270)
    SetChrPos(0x102, -34780, 10000, 59820, 225)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36000, 10000, 58980, 90)
    OP_4A(0x8, 255)
    OP_6F(0x0, 60)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #277
        0x8,
        (
            "#153F#1POh, right... I have to buy\x01",
            "some more photo-quartz.\x02\x03",

            "#150FExcuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#501FOkay...\x01",
            "Thanks for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x8,
        (
            "#154F#1POh, I didn't do anything.\x02\x03",

            "I was just supposed to check up on\x01",
            "some information for the editors.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #280
        0x8,
        (
            "#150F#1PWell... Try and cheer up,\x01",
            "okay, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x107,
        (
            "#560FAh...\x02\x03",

            "I will...\x01",
            "Thank you, Miss Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x8,
        (
            "#150F#1PDon't worry. I'm sure that Estelle\x01",
            "and Joshua will crack this case\x01",
            "and be able to help your grandpa.\x02\x03",

            "#151FSee you later...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    def lambda_6530():
        OP_6D(-35480, 10000, 59730, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6530)
    OP_8E(0x8, 0xFFFF6D02, 0x2710, 0xE66E, 0xBB8, 0x0)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #283
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()

    def lambda_6582():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_6582)

    def lambda_6590():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6590)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #284
        0x101,
        (
            "#006F#2PTita...\x02\x03",

            "#006FPlease don't look so sad. I'm\x01",
            "sure your grandpa is just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x102,
        (
            "#010F#4PRight. Since he's one of the kingdom's\x01",
            "foremost scientific minds, I can't\x01",
            "imagine anyone wanting to hurt him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #286
        0x107,
        (
            "#063FI...\x02\x03",

            "#067F...You're right.\x01",
            "He has to be okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x106,
        "#552F#2P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #288
        0x101,
        "#004F#1PWhat's with that look?\x02",
    )

    CloseMessageWindow()

    def lambda_6711():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6711)

    def lambda_671F():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_671F)

    ChrTalk(    #289
        0x106,
        (
            "#053F#2P...Nothin'.\x02\x03",

            "#050FTime's a' wasting.\x01",
            "Let's go to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x41, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_49_6274 end

    def Function_50_6779(): pass

    label("Function_50_6779")

    EventBegin(0x0)
    OP_6D(-22950, 8000, 63790, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -22960, 8000, 73260, 0)
    SetChrPos(0x101, -21990, 8000, 74030, 0)
    SetChrPos(0x107, -23770, 8000, 73860, 0)

    def lambda_67F1():
        OP_8E(0xFE, 0xFFFFA646, 0x1F40, 0xF5F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67F1)
    Sleep(300)

    def lambda_6811():
        OP_8E(0xFE, 0xFFFFA934, 0x1F40, 0xF9BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6811)
    Sleep(300)

    def lambda_6831():
        OP_8E(0xFE, 0xFFFFA4C0, 0x1F40, 0xFABE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6831)
    FadeToBright(1000, 0)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 135, 400)

    ChrTalk(    #290
        0x102,
        (
            "#010FNow, then...\x01",
            "To the guild first?\x02\x03",

            "Maybe they've learned something\x01",
            "about that airship from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#006FYeah, and they might have\x01",
            "some intel from the Royal\x01",
            "Armed Forces.\x02\x03",

            "#004FWhat are you going to do, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x107,
        (
            "#560FUmm...\x02\x03",

            "I think I'm going to look\x01",
            "after Agate.\x02\x03",

            "Since he hasn't woken up yet,\x01",
            "I don't think he should be left\x01",
            "alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        (
            "#501FTita...\x02\x03",

            "#001FThat's fine. Let us take care\x01",
            "of finding the professor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x107,
        (
            "#063FI'm sorry. All I ever do is\x01",
            "cause trouble for you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#506FWould you listen to this kid?\x01",
            "Where's that old spirit? Buck\x01",
            "up, sweetie. We'll sort this out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        (
            "#010FI think it's a great idea for\x01",
            "you to stay with him until he\x01",
            "wakes up.\x02\x03",

            "We trust you to take\x01",
            "care of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x107,
        "#560FO-Okay...!\x02",
    )

    CloseMessageWindow()

    def lambda_6B55():

        label("loc_6B55")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_6B55")

    QueueWorkItem2(0x101, 1, lambda_6B55)

    def lambda_6B66():

        label("loc_6B66")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_6B66")

    QueueWorkItem2(0x102, 1, lambda_6B66)
    OP_8C(0x107, 225, 400)

    def lambda_6B7E():
        OP_6C(270000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6B7E)

    def lambda_6B8E():
        OP_6D(-22510, 8000, 63590, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_6B8E)
    OP_8E(0x107, 0xFFFF9124, 0x1F40, 0xEDBC, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFF770C, 0x2710, 0xE95C, 0x1388, 0x0)
    SetChrFlags(0x107, 0x80)

    ChrTalk(    #298
        0x101,
        (
            "#006F*sigh*... That's one brave kid.\x01",
            "She's so sweet.\x02\x03",

            "I'm kinda surprised that she\x01",
            "cares so much about a guy with\x01",
            "absolutely no manners, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #299
        0x102,
        (
            "#010FWell...\x02\x03",

            "Come to think of it, you\x01",
            "two are pretty similar to\x01",
            "each other.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #300
        0x101,
        (
            "#004FHuh?!\x02\x03",

            "#009FI have NOTHING in common with\x01",
            "that jerk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x102,
        (
            "#019FHow about your tendency to\x01",
            "go off half-cocked, or how\x01",
            "soft-hearted you are?\x02\x03",

            "#010FHe talks like a big jerk, but\x01",
            "he's always trying to protect\x01",
            "others.\x02\x03",

            "I think that Tita sees that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        (
            "#509FGrrrr... Well, I can't really\x01",
            "argue with that...\x02\x03",

            "#007FFine. Let's just go see\x01",
            "what's up at the guild.\x02\x03",

            "Until Agate's up and about\x01",
            "again, we've got plenty we\x01",
            "can investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x102,
        "#019FThat sounds fine.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x107, -22820, 8000, 62610, 0)
    EventEnd(0x0)
    RemoveParty(0x6, 0xFF)
    Return()

    # Function_50_6779 end

    def Function_51_6ED0(): pass

    label("Function_51_6ED0")

    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(-23500, 8000, 69230, 0)
    OP_67(0, 8490, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(306000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -24660, 8000, 82550, 0)
    SetChrPos(0x102, -22920, 8000, 83030, 0)

    def lambda_6F3C():
        OP_8E(0xFE, 0xFFFFA146, 0x1F40, 0x10E28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F3C)
    Sleep(500)

    def lambda_6F5C():
        OP_8E(0xFE, 0xFFFFA7CC, 0x1F40, 0x111DE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F5C)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #304
        0x101,
        (
            "#007FOkay, heart... Aaaany time you\x01",
            "want to go back to normal running\x01",
            "speed would be just fine.\x02",
        )
    )

    WaitChrThread(0x101, 0x1)
    TurnDirection(0x102, 0x101, 400)
    CloseMessageWindow()

    ChrTalk(    #305
        0x102,
        (
            "#012FIf we waste any more time here,\x01",
            "those Intelligence Division\x01",
            "people will catch up with us.\x02\x03",

            "We should head to town\x01",
            "while we have time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #306
        0x101,
        (
            "#002FOkay.\x02\x03",

            "Umm... We take the east road\x01",
            "to get to Grancel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x102,
        (
            "#012FRight. And the Sanktheim Gate\x01",
            "is to the north, along the\x01",
            "Ritter Roadway.\x02\x03",

            "Pass through the gate, and\x01",
            "you're right by Grancel.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x54, 0x1, 0x10)
    OP_20(0x5DC)
    Sleep(500)
    EventEnd(0x0)
    OP_1D(0xD)
    Return()

    # Function_51_6ED0 end

    def Function_52_716A(): pass

    label("Function_52_716A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_END)), "loc_7265")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E5")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #308
        0x102,
        (
            "#012FIt's probably best if we stay\x01",
            "away from the terminal.\x02\x03",

            "Come on, we need to leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7247")

    label("loc_71E5")


    ChrTalk(    #309
        0x101,
        (
            "#002FThose intelligence goons\x01",
            "are going to be coming\x01",
            "this way...\x02\x03",

            "We should get out of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7247")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7383")

    label("loc_7265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7296")
    Call(0, 53)
    Jump("loc_7383")

    label("loc_7296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7383")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730A")

    ChrTalk(    #310
        0x102,
        (
            "#012FI'm concerned about the professor.\x01",
            "We have to check out the central\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7368")

    label("loc_730A")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(    #311
        0x102,
        (
            "#012FI'm concerned about the professor.\x01",
            "We have to check out the central\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7368")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7383")

    Return()

    # Function_52_716A end

    def Function_53_7384(): pass

    label("Function_53_7384")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_73B5")
    OP_A2(0x1C)
    Jump("loc_73B8")

    label("loc_73B5")

    OP_A2(0x1A)

    label("loc_73B8")

    Jump("loc_73ED")

    label("loc_73BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_73ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73EA")
    OP_A2(0x1C)
    Jump("loc_73ED")

    label("loc_73EA")

    OP_A2(0x1B)

    label("loc_73ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_763D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_7487")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #312
        0x102,
        (
            "#017FHey, Estelle. Weren't you\x01",
            "supposed to return some\x01",
            "books to the archives?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #313
        0x101,
        "#008FOh, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_755B")

    label("loc_7487")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #314
        0x102,
        (
            "#010FHey, you haven't returned\x01",
            "those books to the archives\x01",
            "yet, have you?\x02\x03",

            "We need to go to the central\x01",
            "factory before we check in.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #315
        0x101,
        (
            "#000FOh, yeah. We need to go\x01",
            "to the central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_755B")

    Jump("loc_763A")

    label("loc_755E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_75AB")

    ChrTalk(    #316
        0x102,
        (
            "#010FWe need to go to the central\x01",
            "factory before we check in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763A")

    label("loc_75AB")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #317
        0x102,
        (
            "#010FBy the way, don't you need\x01",
            "to return some books to the\x01",
            "archives?\x02\x03",

            "We need to go to the central\x01",
            "factory before we check in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763A")

    Jump("loc_7BE4")

    label("loc_763D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_7869")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_76DF")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #318
        0x102,
        (
            "#010FHey, Estelle. We need to deliver\x01",
            "that letter to Faye, in the\x01",
            "underground workshop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #319
        0x101,
        "#000FOkay, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_777F")

    label("loc_76DF")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #320
        0x102,
        (
            "#010FEstelle, we need to deliver\x01",
            "that letter to Faye.\x02\x03",

            "Before we check in, let's go\x01",
            "to the basement workshop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #321
        0x101,
        "#004FOh, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_777F")

    Jump("loc_7866")

    label("loc_7782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_77DB")

    ChrTalk(    #322
        0x102,
        (
            "#010FWe need to deliver that letter\x01",
            "to Faye, in the underground\x01",
            "workshop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7866")

    label("loc_77DB")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #323
        0x102,
        (
            "#010FBy the way, we still need to\x01",
            "deliver that letter to Faye.\x02\x03",

            "Before we check in, we have to\x01",
            "go to the basement workshop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7866")

    Jump("loc_7BE4")

    label("loc_7869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_7BE4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_7950")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #324
        0x102,
        (
            "#010FHey, Estelle. We have to\x01",
            "deliver that book and letter\x01",
            "to the central factory.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #325
        0x101,
        (
            "#000FOh, right.\x02\x03",

            "Faye's in the underground workshop,\x01",
            "and the archives are on the second\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A75")

    label("loc_7950")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #326
        0x102,
        (
            "#010FBy the way, we haven't\x01",
            "dropped that book off\x01",
            "at the archives.\x02\x03",

            "Nor have we delivered\x01",
            "Faye's letter to her.\x02\x03",

            "We need to go to the central\x01",
            "factory before we check in.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #327
        0x101,
        (
            "#000FOhh, right.\x02\x03",

            "Faye's in the underground workshop,\x01",
            "and the archives are on the second\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A75")

    Jump("loc_7BE4")

    label("loc_7A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_7B25")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #328
        0x102,
        (
            "#010FWe haven't returned that book\x01",
            "to the reference room, nor\x01",
            "have we delivered that letter.\x02\x03",

            "We need to go to the central\x01",
            "factory before we check in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE4")

    label("loc_7B25")

    OP_A2(0x19)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #329
        0x102,
        (
            "#014FBy the way, we haven't\x01",
            "dropped that book off\x01",
            "at the reference room.\x02\x03",

            "Nor have we delivered\x01",
            "Faye's letter to her.\x02\x03",

            "We need to go to the central\x01",
            "factory before we check in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE4")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_7384 end

    def Function_54_7C00(): pass

    label("Function_54_7C00")

    SetPlaceName(0x85)
    Return()

    # Function_54_7C00 end

    def Function_55_7C04(): pass

    label("Function_55_7C04")

    SetPlaceName(0x81)
    Return()

    # Function_55_7C04 end

    SaveToFile()

Try(main)
