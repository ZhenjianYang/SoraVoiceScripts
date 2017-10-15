from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0130   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0130.x',
        MapIndex            = 3,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0130_1 ._SN',
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
        'Father Divine',                        # 9
        'Sister May',                           # 10
        'Father Kevin',                         # 11
        'Miner Pierre',                         # 12
        'Crew Mem. Quint',                      # 13
        'Miner Heinrich',                       # 14
        'Claire',                               # 15
        'Armand',                               # 16
        'Ellie',                                # 17
        'Anton',                                # 18
        'Attendant',                            # 19
        'Bloom',                                # 20
        'Euridice',                             # 21
        'Luke',                                 # 22
        'Pat',                                  # 23
        'Serra',                                # 24
        'Tabitha',                              # 25
        'Freemont',                             # 26
        'Ida',                                  # 27
        'Aryll',                                # 28
        'エキストラ',                           # 29
        'エキストラ',                           # 30
        'エキストラ',                           # 31
        'エキストラ',                           # 32
        'エキストラ',                           # 33
        "Groom's Family",                       # 34
        "Groom's Family",                       # 35
        "Groom's Family",                       # 36
        "Bride's Family",                       # 37
        "Bride's Family",                       # 38
        "Bride's Family",                       # 39
        "Bride's Friend",                       # 40
        "Bride's Friend",                       # 41
        'Targeting Camera',                     # 42
        'Kitten',                               # 43
        'Kitten',                               # 44
        'Kitten',                               # 45
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT27/CH03080 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01290 ._CH',             # 04
        'ED6_DT07/CH01070 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01150 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01690 ._CH',             # 09
        'ED6_DT27/CH03005 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01013 ._CH',             # 0C
        'ED6_DT07/CH01033 ._CH',             # 0D
        'ED6_DT07/CH01160 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01133 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01700 ._CH',             # 12
        'ED6_DT07/CH01053 ._CH',             # 13
        'ED6_DT07/CH01223 ._CH',             # 14
        'ED6_DT07/CH01593 ._CH',             # 15
        'ED6_DT07/CH01233 ._CH',             # 16
        'ED6_DT07/CH01183 ._CH',             # 17
        'ED6_DT07/CH01030 ._CH',             # 18
        'ED6_DT07/CH01200 ._CH',             # 19
        'ED6_DT07/CH01470 ._CH',             # 1A
        'ED6_DT07/CH01490 ._CH',             # 1B
        'ED6_DT07/CH01230 ._CH',             # 1C
        'ED6_DT07/CH01480 ._CH',             # 1D
        'ED6_DT07/CH01213 ._CH',             # 1E
        'ED6_DT07/CH01130 ._CH',             # 1F
        'ED6_DT26/CH20311 ._CH',             # 20
        'ED6_DT07/CH01493 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT27/CH03080P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01290P._CP',             # 04
        'ED6_DT07/CH01070P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01150P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01690P._CP',             # 09
        'ED6_DT27/CH03005P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01013P._CP',             # 0C
        'ED6_DT07/CH01033P._CP',             # 0D
        'ED6_DT07/CH01160P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01133P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01700P._CP',             # 12
        'ED6_DT07/CH01053P._CP',             # 13
        'ED6_DT07/CH01223P._CP',             # 14
        'ED6_DT07/CH01593P._CP',             # 15
        'ED6_DT07/CH01233P._CP',             # 16
        'ED6_DT07/CH01183P._CP',             # 17
        'ED6_DT07/CH01030P._CP',             # 18
        'ED6_DT07/CH01200P._CP',             # 19
        'ED6_DT07/CH01470P._CP',             # 1A
        'ED6_DT07/CH01490P._CP',             # 1B
        'ED6_DT07/CH01230P._CP',             # 1C
        'ED6_DT07/CH01480P._CP',             # 1D
        'ED6_DT07/CH01213P._CP',             # 1E
        'ED6_DT07/CH01130P._CP',             # 1F
        'ED6_DT26/CH20311P._CP',             # 20
        'ED6_DT07/CH01493P._CP',             # 21
    )

    DeclNpc(
        X                   = 58800,
        Z                   = 1000,
        Y                   = 52200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -16830,
        Z                   = 0,
        Y                   = 42890,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55420,
        Z                   = 0,
        Y                   = 46990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 58970,
        Z                   = 0,
        Y                   = 47900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 62060,
        Z                   = 0,
        Y                   = 43550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 56050,
        Z                   = 0,
        Y                   = 40700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 55340,
        Z                   = 0,
        Y                   = 47470,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 47270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 58300,
        Z                   = 0,
        Y                   = 44200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57670,
        Z                   = 0,
        Y                   = 48880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55310,
        Z                   = 150,
        Y                   = 45960,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56390,
        Z                   = 150,
        Y                   = 45990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 54680,
        Z                   = 0,
        Y                   = 44910,
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
        X                   = 55400,
        Z                   = 0,
        Y                   = 44910,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56470,
        Z                   = 150,
        Y                   = 44510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 56150,
        Z                   = 0,
        Y                   = 41510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 61860,
        Z                   = 150,
        Y                   = 42920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 62700,
        Z                   = 150,
        Y                   = 42950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62960,
        Z                   = 0,
        Y                   = 43610,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54500,
        Z                   = 150,
        Y                   = 42970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55920,
        Z                   = 150,
        Y                   = 42970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55090,
        Z                   = 150,
        Y                   = 41510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62110,
        Z                   = 150,
        Y                   = 41430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63630,
        Z                   = 150,
        Y                   = 41440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57680,
        Z                   = 0,
        Y                   = 43380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 58780,
        Z                   = 0,
        Y                   = 46800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 63110,
        Z                   = 0,
        Y                   = 46830,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 57650,
        Z                   = 0,
        Y                   = 42350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -16100,
        Z                   = 0,
        Y                   = 45910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 54130,
        Z                   = 0,
        Y                   = 50110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 52890,
        Z                   = 0,
        Y                   = 48010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 52980,
        Z                   = 0,
        Y                   = 46970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63200,
        Z                   = 0,
        Y                   = 43610,
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
        X                   = 63700,
        Z                   = 0,
        Y                   = 43610,
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
        X                   = 64099,
        Z                   = 0,
        Y                   = 43610,
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


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52200,
        TriggerZ            = 5000,
        TriggerY            = 52260,
        TriggerRange        = 600,
        ActorX              = 52200,
        ActorZ              = 5600,
        ActorY              = 52260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6A2",          # 00, 0
        "Function_1_8A0",          # 01, 1
        "Function_2_8EB",          # 02, 2
        "Function_3_A68",          # 03, 3
        "Function_4_A8C",          # 04, 4
        "Function_5_A91",          # 05, 5
        "Function_6_2B21",         # 06, 6
        "Function_7_3458",         # 07, 7
        "Function_8_3587",         # 08, 8
        "Function_9_3B96",         # 09, 9
        "Function_10_3C6F",        # 0A, 10
        "Function_11_3D6D",        # 0B, 11
        "Function_12_3F3B",        # 0C, 12
        "Function_13_41C3",        # 0D, 13
        "Function_14_4B20",        # 0E, 14
        "Function_15_527F",        # 0F, 15
        "Function_16_55D4",        # 10, 16
        "Function_17_569F",        # 11, 17
        "Function_18_5701",        # 12, 18
        "Function_19_5791",        # 13, 19
        "Function_20_581E",        # 14, 20
        "Function_21_58AD",        # 15, 21
        "Function_22_592B",        # 16, 22
        "Function_23_59BE",        # 17, 23
        "Function_24_5A52",        # 18, 24
        "Function_25_5AC9",        # 19, 25
        "Function_26_5BEB",        # 1A, 26
        "Function_27_68B0",        # 1B, 27
        "Function_28_690E",        # 1C, 28
        "Function_29_695F",        # 1D, 29
        "Function_30_69E8",        # 1E, 30
    )


    def Function_0_6A2(): pass

    label("Function_0_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C")
    SetChrChipByIndex(0x14, 24)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -16010, 0, 43960, 180)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrPos(0x9, 59550, 0, 48300, 270)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xF, 58560, 0, 48300, 90)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x10, -15950, 0, 43090, 270)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x17, 31)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -15930, 0, 42250, 0)
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_7D9")

    label("loc_76C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777")
    Jump("loc_7D9")

    label("loc_777")

    SetChrChipByIndex(0x14, 24)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 56320, 0, 46950, 270)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x19, 33)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x10)
    SetChrPos(0x19, 55160, 0, 46950, 90)
    ClearChrFlags(0x19, 0x80)
    OP_43(0x19, 0x0, 0x0, 0x2)

    label("loc_7D9")

    Jump("loc_83B")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7EB")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_83B")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_80E")
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_83B")

    label("loc_80E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_822")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_83B")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_82C")
    Jump("loc_83B")

    label("loc_82C")

    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    label("loc_83B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86B")
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_86B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x2000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88A")
    Event(1, 7)

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89F")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_89F")

    Return()

    # Function_0_6A2 end

    def Function_1_8A0(): pass

    label("Function_1_8A0")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C3")
    OP_65(0x1, 0x1)

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D5")
    Jump("loc_8EA")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")
    Jump("loc_8EA")

    label("loc_8E0")

    OP_D2(0x700A8, 0x700AC, 0x21)

    label("loc_8EA")

    Return()

    # Function_1_8A0 end

    def Function_2_8EB(): pass

    label("Function_2_8EB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_910")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A52")

    label("loc_910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_929")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A52")

    label("loc_929")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A52")

    label("loc_942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A52")

    label("loc_95B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A52")

    label("loc_974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A52")

    label("loc_98D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A52")

    label("loc_9A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A52")

    label("loc_9BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A52")

    label("loc_9D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A52")

    label("loc_9F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A52")

    label("loc_A0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A23")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A52")

    label("loc_A23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A52")

    label("loc_A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A52")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A52")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A67")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A52")

    label("loc_A67")

    Return()

    # Function_2_8EB end

    def Function_3_A68(): pass

    label("Function_3_A68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B")
    OP_8D(0xFE, 54500, 46700, 56400, 48400, 2000)
    Jump("Function_3_A68")

    label("loc_A8B")

    Return()

    # Function_3_A68 end

    def Function_4_A8C(): pass

    label("Function_4_A8C")

    Call(0, 5)
    Return()

    # Function_4_A8C end

    def Function_5_A91(): pass

    label("Function_5_A91")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE2")
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(    #0
        0x8,
        "Oh...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE4")

    ChrTalk(    #1
        0x8,
        "Well, if it isn't Joshua.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFF")

    label("loc_AE4")


    ChrTalk(    #2
        0x8,
        "Is that Joshua there?\x02",
    )

    CloseMessageWindow()

    label("loc_AFF")


    ChrTalk(    #3
        0x102,
        "#1035FYes... I'm back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "I've been waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Hmm... You seem much more at peace.\x01",
            "Very calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "Have you discovered the road you must walk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#1040FYes, somehow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "...Estelle, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Right now, the world is descending into chaos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "However, no matter what happens, you\x01",
            "must not lose sight of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "The light of hope that guides us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "It exists nowhere but inside your own heart.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002FYeah... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1040FI shall keep those words close.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD9")

    ChrTalk(    #15
        0x8,
        "Please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "Now, then, I would love to talk more, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "Things are incredibly busy at the moment,\x01",
            "so let us stop here for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1016FAhaha... Sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1040FYes, another time, then.\x01",
            "Thank you, Father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9")

    OP_A2(0x1)
    OP_A2(0x209E)
    Jump("loc_121F")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EA2")

    ChrTalk(    #20
        0x8,
        (
            "No matter what should happen, you\x01",
            "must not lose sight of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "That which will guide us in\x01",
            "the end is our own heart.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9F")

    ChrTalk(    #22
        0x8,
        "Now, I must prepare for the ceremony.\x02",
    )

    CloseMessageWindow()

    label("loc_E9F")

    Jump("loc_121F")

    label("loc_EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_105D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC9")

    ChrTalk(    #23
        0x8,
        "Phew! The ceremony went off without a hitch.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #24
        0x8,
        "Did you all attend as well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1011FAh, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1040FYes, a little at the very end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "It is worthwhile to contemplate such\x01",
            "turning points in life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "After all, it's not such a long way\x01",
            "away for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_105A")

    label("loc_FC9")


    ChrTalk(    #29
        0x8,
        (
            "It is worthwhile to contemplate such\x01",
            "turning points in life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "It does connect, after all, to thinking\x01",
            "about one's overall goal in life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105A")

    Jump("loc_121F")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(    #31
        0x8,
        (
            "There will be a wedding in the church\x01",
            "today, so I'm busy preparing for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Even beneath cloudy skies birds sing,\x01",
            "and below the last snows grow the buds\x01",
            "of spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "Even should the world be overrun with\x01",
            "misfortune, we must endure and carry on.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_121F")

    label("loc_116E")


    ChrTalk(    #34
        0x8,
        (
            "Even beneath cloudy skies birds sing,\x01",
            "and below the last snows grow the buds\x01",
            "of spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "Even should the world be overrun with\x01",
            "misfortune, we must endure and carry on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121F")

    Jump("loc_2B1D")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 5)), scpexpr(EXPR_END)), "loc_17C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1358")

    ChrTalk(    #36
        0x8,
        (
            "I treated the two young men who were\x01",
            "incapacitated by their drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "There should be no concerns of\x01",
            "alcohol poisoning now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "No matter how confident you are, excessive\x01",
            "drinking should be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "If you try to keep up with Aina,\x01",
            "you'll ruin your health very quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C4")

    label("loc_1358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D3")

    ChrTalk(    #40
        0x8,
        (
            "Oh, yes, about that 'contest' in\x01",
            "the bar from a bit ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "I treated the two young men who were\x01",
            "incapacitated by their drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "There should be no concerns of\x01",
            "alcohol poisoning now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EF")
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #43
        0x8,
        "...Ah. Speak of the devils.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        "Olivier. Are you feeling well now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x104,
        (
            "#035FHeh, somehow.\x02\x03",

            "My apologies for taking up your time,\x01",
            "good sir, but you need worry no more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "That's good to hear. However...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "No matter how confident you are, excessive\x01",
            "drinking should be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "If you try to keep up with Aina,\x01",
            "you'll ruin your health very quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1007FY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        "#034FI-I will keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C7")

    label("loc_15EF")


    ChrTalk(    #51
        0x8,
        (
            "No matter how confident you are, excessive\x01",
            "drinking should be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "If you try to keep up with Aina,\x01",
            "you'll ruin your health very quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1007FY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        "#025F*sigh* I will keep that in mind.\x02",
    )

    CloseMessageWindow()

    label("loc_16C7")

    OP_28(0x76, 0x1, 0x800)
    OP_A2(0xE)
    Jump("loc_17C4")

    label("loc_16D3")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #55
        0x8,
        (
            "Seeing Estelle's growth is of great\x01",
            "comfort to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "Even when you continue on to your next appointed\x01",
            "destination, do not forget the feelings of today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Believe in what you hold in your heart,\x01",
            "no matter the time or place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_1ADA")

    label("loc_17C7")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #58
        0x8,
        "Oh, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "Your deeds of late have reached even my ears.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "You have done well to overcome this hardship.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "Allow me to offer my own thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1008FAhaha...\x02\x03",

            "It feels kinda embarrassing being\x01",
            "complimented by you, Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020FWe should be the ones thanking you.\x02\x03",

            "Treating the afflicted and contacting the\x01",
            "grand cathedral... We owe you much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #64
        0x8,
        "No, I simply did my duty as a priest.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #65
        0x8,
        (
            "Still, it is a great comfort to me to see\x01",
            "Estelle's growth in these troubled times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "Even when you continue on to your next appointed\x01",
            "destination, do not forget the feelings of today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1006FI won't!\x02\x03",

            "Now, if you'll excuse us, Father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "Take care on your way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "May the guidance of the Goddess go with you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5D)

    label("loc_1ADA")

    Jump("loc_2B1D")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_21BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 2)), scpexpr(EXPR_END)), "loc_1BC6")

    ChrTalk(    #70
        0x8,
        (
            "Nothing comes from cursing one's weakness\x01",
            "or failures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "Right now, all anyone can do is try their best\x01",
            "to overcome what hardships may come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "Ultimately, that is the fastest\x01",
            "way to resolve the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B8")

    label("loc_1BC6")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #73
        0x8,
        "Oh, Estelle and Scherazard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "Have you already met Father Kevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1025FAh, yeah.\x02\x03",

            "He's minding the Perzel Farm at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "I see, so that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "Still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "I sense some hesitation from you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1026FWh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "You're not satisfied or okay, but for now you're\x01",
            "carrying on... That's the impression I get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "In which case, you should be commended for\x01",
            "choosing to step forward rather than being\x01",
            "trapped by hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        "It seems you are moving in a positive direction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "Perhaps thanks to the guidance\x01",
            "of your good seniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1017FAhaha... Yeah, you're probably right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F23")

    ChrTalk(    #85
        0x104,
        (
            "#031FHeh, 'tis a bit embarrassing to be thanked so.\x02\x03",

            "Still, it is true that I have more or\x01",
            "less raised Estelle to be who she is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #86
        0x101,
        "#1007F...Uh, wait. Why is Olivier in this conversation?\x02",
    )

    CloseMessageWindow()
    Jump("loc_209E")

    label("loc_1F23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC2")

    ChrTalk(    #87
        0x106,
        (
            "#051FHeh. Well, ain't that humble for once?\x02\x03",

            "If only you were always this good at listening,\x01",
            "that'd be a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        "#021FAbsolutely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_209E")

    label("loc_1FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_203E")

    ChrTalk(    #89
        0x108,
        (
            "#071FHey, hey! What's this, now?\x01",
            "You're being humble for once.\x02\x03",

            "How unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        "#020FAbsolutely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_209E")

    label("loc_203E")


    ChrTalk(    #91
        0x103,
        (
            "#021FMy! Aren't you being honest\x01",
            "for once?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #92
        0x101,
        "#1007FMmmmrrr... I'm always honest.\x02",
    )

    CloseMessageWindow()

    label("loc_209E")


    ChrTalk(    #93
        0x8,
        (
            "Nothing comes from cursing one's weakness\x01",
            "or failures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "Right now, all anyone can do is try their best\x01",
            "to overcome what hardships may come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "Ultimately, that is the fastest\x01",
            "way to resolve the situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #96
        0x101,
        "#1006FYes, Father...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        "#020FYes, we'll do that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1892)

    label("loc_21B8")

    Jump("loc_2B1D")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22B7")

    ChrTalk(    #98
        0x8,
        (
            "Unfortunately, I haven't found any clues\x01",
            "in the texts I have available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "I have studied medicine to care for\x01",
            "the mind and body, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "There are still secrets hidden all across\x01",
            "this land that even I have no knowledge of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_22B7")


    ChrTalk(    #101
        0x8,
        (
            "Oh, hello. You're certainly out and\x01",
            "about early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "Unfortunately, I haven't found any clues\x01",
            "in the texts I have available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "I have studied medicine to care for\x01",
            "the mind and body, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "There are still secrets hidden all across\x01",
            "this land that even I have no knowledge of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "To we, the followers of the Septian Church,\x01",
            "the truth is yet distant and shrouded in\x01",
            "darkness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "For us to reach that answer,\x01",
            "I must redouble my efforts.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_247F")

    Jump("loc_2B1D")

    label("loc_2482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_28A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 1)), scpexpr(EXPR_END)), "loc_25A5")

    ChrTalk(    #107
        0x8,
        (
            "There are things that can be seen precisely\x01",
            "because one cannot see them with the eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "Not to be tossed about by an ever-changing\x01",
            "outside world, but to quietly speak to the\x01",
            "self...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "Spend your days like that and the fog will\x01",
            "become an ally instead of an enemy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289E")

    label("loc_25A5")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #110
        0x8,
        "...Oh, Estelle. And Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "It has been a while.\x01",
            "Have you been doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1011FAh, yeah... It has been a while, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        (
            "#020FWe're fine. I'm glad to see you're looking\x01",
            "good, too, Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        "Welcome home, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "Right now, Rolent is locked away by fog.\x01",
            "Even seeing your immediate surroundings\x01",
            "is quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "However, there are things that can be seen\x01",
            "precisely because one cannot see them with\x01",
            "the eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "Not to be tossed about by an ever-changing\x01",
            "outside world, but to quietly speak to the\x01",
            "self...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "Spend your days like that and the fog will\x01",
            "become an ally instead of an enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1007F(...I understood, like, 30% of that.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x103,
        (
            "#020F(His words are always rich\x01",
            "with meaning.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1891)

    label("loc_289E")

    Jump("loc_2B1D")

    label("loc_28A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 1)), scpexpr(EXPR_END)), "loc_2922")

    ChrTalk(    #121
        0x8,
        "Estelle, welcome home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "Oh, Aidios, She Who Dwells Above.\x01",
            "Give your guidance to these wandering lambs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1D")

    label("loc_2922")


    ChrTalk(    #123
        0x8,
        "Why, Estelle, welcome home.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x142, 400)

    ChrTalk(    #124
        0x8,
        "And you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x142,
        (
            "#1060FPleasure to meetcha, Father.\x01",
            "I'm Kevin Graham, wandering priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "Ah, I did hear that someone from\x01",
            "the High Seat would be stationed in\x01",
            "Grancel soon. Would that be you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x142,
        (
            "#1060FYup, guilty as charged!\x02\x03",

            "Now, it's, uh, kinda a long story as to\x01",
            "why I'm out here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #128
        0x8,
        "...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x142, 400)

    ChrTalk(    #129
        0x8,
        "(Father Kevin.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x142,
        "#1060F(Yeah?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        "(Please...protect Estelle, in every way you can.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x142,
        (
            "#1063F(...!)\x02\x03",

            "#1060F(Yeah. Don't worry.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1031)

    label("loc_2B1D")

    TalkEnd(0x8)
    Return()

    # Function_5_A91 end

    def Function_6_2B21(): pass

    label("Function_6_2B21")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_2C7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF9")

    ChrTalk(    #133
        0x9,
        (
            "Ahh, now that the ceremony is over\x01",
            "I can finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "To have a wedding at a time like this,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x9,
        (
            "That's just like Rolent. Nothing seems to\x01",
            "faze this city or its people.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2C7C")

    label("loc_2BF9")


    ChrTalk(    #136
        0x9,
        (
            "To have a wedding at a time like this,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "That's just like Rolent. Nothing seems to\x01",
            "faze this city or its people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7C")

    Jump("loc_3454")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C95")
    Call(0, 7)
    Jump("loc_2D30")

    label("loc_2C95")


    ChrTalk(    #138
        0x9,
        (
            "Once the exchange of rings is finished,\x01",
            "then it's time to seal the oath of love\x01",
            "with a kiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "W-Well, I'm sure you've practiced that\x01",
            "enough, yes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D30")

    Jump("loc_3454")

    label("loc_2D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2EF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2DC3")

    ChrTalk(    #140
        0xFE,
        (
            "I'm not very familiar with Arteria or the\x01",
            "people from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Perhaps the way the priest talks is\x01",
            "the Arterian style?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EED")

    label("loc_2DC3")


    ChrTalk(    #142
        0xFE,
        (
            "A bit ago, a traveling priest was\x01",
            "talking to Father Divine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Apparently, that traveling priest\x01",
            "was dispatched from the Arterian\x01",
            "High Seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I was surprised at how young and, well,\x01",
            "casual he was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I thought the priests from the central Church\x01",
            "were all super serious and austere.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2EED")

    Jump("loc_3454")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_307E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F95")

    ChrTalk(    #146
        0xFE,
        (
            "That priest from a moment ago...\x01",
            "He left a very different impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I wonder if that kind of style is\x01",
            "popular in the capital right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307B")

    label("loc_2F95")


    ChrTalk(    #148
        0xFE,
        (
            "A bit ago, a priest came from\x01",
            "the cathedral in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "Between his hairstyle and the way he spoke,\x01",
            "he certainly left quite the impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I wonder if that kind of style is\x01",
            "popular in the capital right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_307B")

    Jump("loc_3454")

    label("loc_307E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3268")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3123")

    ChrTalk(    #151
        0xFE,
        (
            "Father Divine was up all night researching\x01",
            "to try and find something that might help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "As a sister of the church I need to\x01",
            "do my best too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3265")

    label("loc_3123")


    ChrTalk(    #153
        0xFE,
        (
            "Father Divine was up all night researching\x01",
            "to try and find something that might help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I tried to keep offering up prayers for\x01",
            "as long as my will would hold, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I eventually fell asleep, and when\x01",
            "I came to it was morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "*sigh* I have a long way to go if I am\x01",
            "to ever match up to Father Divine.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3265")

    Jump("loc_3454")

    label("loc_3268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_33E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3319")

    ChrTalk(    #157
        0xFE,
        (
            "Today the church was engulfed in a fog\x01",
            "so thick it seemed like something out of\x01",
            "a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "It would have been perfect if the\x01",
            "fog had cleared quickly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E0")

    label("loc_3319")


    ChrTalk(    #159
        0xFE,
        (
            "Today the church was engulfed in a fog\x01",
            "so thick it seemed like something out of\x01",
            "a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "It was so beautiful... Ah, but I guess this\x01",
            "isn't really the time to be admiring the\x01",
            "darn thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_33E0")

    Jump("loc_3454")

    label("loc_33E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_3454")

    ChrTalk(    #161
        0xFE,
        "Aidios, You Who Dwell Above In Splendor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Please watch over the people of Rolent\x01",
            "today, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3454")

    TalkEnd(0x9)
    Return()

    # Function_6_2B21 end

    def Function_7_3458(): pass

    label("Function_7_3458")

    OP_4A(0x9, 255)
    OP_4A(0xF, 255)

    ChrTalk(    #163
        0x9,
        "I shall guide you, so take one step forward...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "And place the ring you have on the\x01",
            "left ring finger of your bride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xF,
        "O-Okay... Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        "You should practice it before the ceremony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "When you're nervous, you won't be able to\x01",
            "do even the most simple things.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x8)
    ClearChrFlags(0xF, 0x10)
    OP_4B(0x9, 255)
    OP_4B(0xF, 255)
    Return()

    # Function_7_3458 end

    def Function_8_3587(): pass

    label("Function_8_3587")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 6)), scpexpr(EXPR_END)), "loc_3604")

    ChrTalk(    #168
        0xA,
        (
            "#1060FI've got a bit more studyin' up here\x01",
            "at the church before I head off.\x02\x03",

            "You all take care now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B92")

    label("loc_3604")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #169
        0xA,
        "#1062FOh, heya, everyone. Great work out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1017FYeah, you too, Kevin.\x02\x03",

            "You were a big help. Thanks for\x01",
            "taking care of Tio and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "#1061FHaha, it was nothin', nothin'.\x01",
            "No big deal.\x02\x03",

            "Anything for my beloved Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#1008FAgain with that stuff? C'mon.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3891")

    ChrTalk(    #173
        0x103,
        (
            "#021FReally, he'd be a good match for someone\x01",
            "else we know in the smooth talker department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        (
            "#035FSmooth talker'? Schera, you wound me...\x02\x03",

            "#030FI take beauty very seriously! I mean every\x01",
            "compliment that passes my lips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1007FThat makes it kinda worse...\x02\x03",

            "#1011F...Uh, anyway, what are you going\x01",
            "to do now, Kevin?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3959")

    label("loc_3891")


    ChrTalk(    #176
        0x103,
        (
            "#021FReally, he'd be a good match for someone\x01",
            "else we know in the smooth talker department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1016FAhaha, you might be on to something there...\x02\x03",

            "#1011FAnyway, Kevin, what are your plans now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3959")


    ChrTalk(    #178
        0xA,
        (
            "#1068FWell, I think I'll keep workin' my way\x01",
            "around the countryside, visitin' the churches.\x02\x03",

            "I've got some business I need\x01",
            "to take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1015FJust a spot of business, huh?\x02\x03",

            "#1002F...Or so you say, but it's probably\x01",
            " really important, isn't it?\x02\x03",

            "Was it really just a coincidence you\x01",
            "happened to stop here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "#1064FOoh... Estelle, sometimes you're so\x01",
            "sharp it hurts.\x02\x03",

            "#1066FWell, all that aside...\x02\x03",

            "I hope we can trade info sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1006FYeah, let's do that sometime.\x02\x03",

            "Well, you take care of yourself, Kevin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        "#1062FYou, too, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5E)

    label("loc_3B92")

    TalkEnd(0xA)
    Return()

    # Function_8_3587 end

    def Function_9_3B96(): pass

    label("Function_9_3B96")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3BEB")

    ChrTalk(    #183
        0xFE,
        (
            "I am deeply thankful I was able\x01",
            "to return to town safely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6B")

    label("loc_3BEB")


    ChrTalk(    #184
        0xFE,
        (
            "Thanks to the Goddess, I returned\x01",
            "to town safely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Please, Great Aidios, continue to watch\x01",
            "over and protect us...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3C6B")

    TalkEnd(0xB)
    Return()

    # Function_9_3B96 end

    def Function_10_3C6F(): pass

    label("Function_10_3C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3C7B")
    SetChrFlags(0xC, 0x10)

    label("loc_3C7B")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3CEA")

    ChrTalk(    #186
        0xFE,
        (
            "Would someone, SOMETHING,\x01",
            "please clear this damn fog?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "I'm seriously begging ya!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D69")

    label("loc_3CEA")


    ChrTalk(    #188
        0xFE,
        (
            "I don't have much else to do,\x01",
            "so I'm here praying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "Well, it's in my own style, but\x01",
            "I'm praying with all my heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3D69")

    TalkEnd(0xC)
    Return()

    # Function_10_3C6F end

    def Function_11_3D6D(): pass

    label("Function_11_3D6D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3E0B")

    ChrTalk(    #190
        0xFE,
        (
            "Man, Pierre sure does love his one-on-one\x01",
            "time with the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Churches aren't really my thing,\x01",
            "so I just pass the time here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F37")

    label("loc_3E0B")


    ChrTalk(    #192
        0xFE,
        (
            "Man, Pierre sure does love his one-on-one\x01",
            "time with the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "He always stops by the church\x01",
            "before grabbing lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "If you ask him, he'd say it was the Goddess\x01",
            "that saved our butts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "I wonder if he's spared a thought for the\x01",
            "bracers that brought us back to town in\x01",
            "one piece.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3F37")

    TalkEnd(0xD)
    Return()

    # Function_11_3D6D end

    def Function_12_3F3B(): pass

    label("Function_12_3F3B")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3FAC")

    ChrTalk(    #196
        0xFE,
        "Father Divine's holding out on me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "Maybe it's time I shifted\x01",
            "my aim to the sister.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4061")

    label("loc_3FAC")


    ChrTalk(    #198
        0xFE,
        "All the signs point to a case...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Father Divine's guard is too tough.\x01",
            "I can't get any details out of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "Maybe I should switch gears and pump\x01",
            "the sister for info.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_4061")

    Jump("loc_41BF")

    label("loc_4064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_41BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_40DC")

    ChrTalk(    #201
        0xFE,
        (
            "A bunch of bracers operating together\x01",
            "this early in the morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "Ah-HA! Something's afoot!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41BF")

    label("loc_40DC")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #203
        0xFE,
        "Huh? Estelle and Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "A bunch of bracers operating together\x01",
            "this early in the morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "Ah-HA! I smell a case!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I can't just stand here.\x01",
            "Time for Claire to get the scoop!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_41BF")

    TalkEnd(0xE)
    Return()

    # Function_12_3F3B end

    def Function_13_41C3(): pass

    label("Function_13_41C3")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41DC")
    Call(0, 7)
    Jump("loc_42CA")

    label("loc_41DC")


    ChrTalk(    #207
        0xFE,
        (
            "My family was against having a wedding\x01",
            "at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "I really want us to be husband and wife properly\x01",
            "with the blessings of the Goddess as soon as\x01",
            "possible, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Ellie and I talked about it\x01",
            "and decided on a time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42CA")

    Jump("loc_4B1C")

    label("loc_42CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4316")

    ChrTalk(    #210
        0xFE,
        "Ahh, Ellie...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AF1")

    label("loc_4316")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_43A9")

    ChrTalk(    #211
        0xFE,
        (
            "Well, then, bracers.\x01",
            "Please take care of the ring for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "If you find anything out,\x01",
            "come here again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DB")

    label("loc_43A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4422")

    ChrTalk(    #213
        0xFE,
        (
            "Well, then, bracers.\x01",
            "Please take care of the ring for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "If you find anything out,\x01",
            "come here again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DB")

    label("loc_4422")

    OP_A2(0x8)

    ChrTalk(    #215
        0xFE,
        "Ah, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "H-How is it?\x01",
            "Is the investigation going well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#1015FIt's okay.\x02\x03",

            "It's going to take a bit longer, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "It's okay. I'll be patient.\x02",
    )

    CloseMessageWindow()

    label("loc_44DB")

    Jump("loc_4AF1")

    label("loc_44DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_45CA")

    ChrTalk(    #220
        0xFE,
        (
            "Hmm. The grand cathedral's hard\x01",
            "to toss aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "But I guess I really would rather we\x01",
            "have our wedding here in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "To swear our love at the place we met\x01",
            "may sound kinda simple, but there's a\x01",
            "holy sense to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF1")

    label("loc_45CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4634")

    ChrTalk(    #223
        0xFE,
        "Ah, my adorable Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Just as the fog engulfs the city,\x01",
            "I am wrapped in your love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF1")

    label("loc_4634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4682")

    ChrTalk(    #225
        0xFE,
        "Come closer, Ellie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "I want to see nothing but your smile.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AF1")

    label("loc_4682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4AF1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_479D")

    ChrTalk(    #227
        0xFE,
        "Trembling lips like the petals of roses...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "And from those lips fell...words of\x01",
            "acceptance from Ellie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "At last... At last, our futures\x01",
            "were sworn to each other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "Ahh, just remembering it makes\x01",
            "me feel like I might go mad!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48F2")

    label("loc_479D")


    ChrTalk(    #231
        0xFE,
        "Trembling lips like the petals of roses...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "And from those lips fell...words of\x01",
            "acceptance from Ellie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "At last... At last, our futures\x01",
            "were sworn to each other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "Ahh, and yet...is the Goddess merciless?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "Ahhhhhhh, I'm sure this is our\x01",
            "final trial before marriage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "I swear I shall endure it...for your sake,\x01",
            "Ellie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F2")

    Jump("loc_4AF1")

    label("loc_48F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49CB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #237
        0xFE,
        "Your eyes, confused from my sudden proposal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Ahh, that brief moment of silence\x01",
            "that felt like an eternity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Even now my heart feels like\x01",
            "it's going to tear itself apart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF1")

    label("loc_49CB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #240
        0xFE,
        "Ahh, that wonderful Birthday Celebration evening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Ellie... Every time I see your face the\x01",
            "emotion of that night comes back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "We stared at each other underneath the\x01",
            "lights of the stars and the fireworks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "I put my dedication into words,\x01",
            "and conveyed them to you...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AF1")

    Jump("loc_4B1C")

    label("loc_4AF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_4B11")
    Call(1, 1)
    Jump("loc_4B15")

    label("loc_4B11")

    Call(1, 0)

    label("loc_4B15")

    Jump("loc_4B1C")

    label("loc_4B18")

    Call(1, 3)

    label("loc_4B1C")

    TalkEnd(0xF)
    Return()

    # Function_13_41C3 end

    def Function_14_4B20(): pass

    label("Function_14_4B20")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFF")

    ChrTalk(    #244
        0xFE,
        (
            "Father in heaven... I wonder\x01",
            "if you can hear me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "Your little girl's going to be a bride today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "I'll finally wear this dress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "It's very lovely, and I'm sure you'd\x01",
            "like it, Father.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_4C76")

    label("loc_4BFF")


    ChrTalk(    #248
        0xFE,
        (
            "Father in heaven... Your little girl's going\x01",
            "to be a bride today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "I hope you will continue to watch over me.\x02",
    )

    CloseMessageWindow()

    label("loc_4C76")

    Jump("loc_527B")

    label("loc_4C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4C92")

    ChrTalk(    #250
        0xFE,
        "Armand...\x02",
    )

    CloseMessageWindow()
    Jump("loc_527B")

    label("loc_4C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D1D")

    ChrTalk(    #251
        0xFE,
        "We'll be waiting right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "I'm sure it'll be a hard mission,\x01",
            "but I hope you'll give it your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_527B")

    label("loc_4D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4DCC")

    ChrTalk(    #253
        0xFE,
        (
            "I'd like to have a lovely ceremony in\x01",
            "the capital's grand cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "We'll cut the tape on a start for our new\x01",
            "life in the land of our memories. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EBC")

    label("loc_4DCC")

    OP_A2(0x9)

    ChrTalk(    #255
        0xFE,
        (
            "We've decided to start preparations\x01",
            "for our wedding ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "Personally, I'd like to have a lovely ceremony\x01",
            "in the capital's grand cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "We'll cut the tape on a start for our new\x01",
            "life in the land of our memories. ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBC")

    Jump("loc_527B")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4F01")

    ChrTalk(    #258
        0xFE,
        (
            "Hey, Armand, that expression isn't\x01",
            "very beautiful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_527B")

    label("loc_4F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4F54")

    ChrTalk(    #259
        0xFE,
        "I'm so embarrassed, Armand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "Who knows who could be watching?\x02",
    )

    CloseMessageWindow()
    Jump("loc_527B")

    label("loc_4F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_527B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5061")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #261
        0xFE,
        (
            "Armand was waiting for my answer\x01",
            "like a puppy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "He looked so pitiful, so I decided\x01",
            "to stop teasing him and answered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        "And so...we swore our futures to each other.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "Ahhh... It was the most wonderful moment\x01",
            "of my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_527B")

    label("loc_5061")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5143")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #265
        0xFE,
        "I pushed down a wonderfully happy feeling...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "And as I peeked at his expression, I pretended\x01",
            "to think for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "Teehee. Armand's face at that moment...\x01",
            "I doubt I'll ever forget it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_527B")

    label("loc_5143")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #268
        0xFE,
        (
            "I can still remember the night of the\x01",
            "Birthday Celebration like it was yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "Before my eyes rose the white walls of Grancel\x01",
            "Castle... And above my head, the night sky\x01",
            "was studded with twinkling stars...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "After a few moments he spoke. Yes...\x01",
            "He said the words I had been longing for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_527B")

    TalkEnd(0x10)
    Return()

    # Function_14_4B20 end

    def Function_15_527F(): pass

    label("Function_15_527F")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_5487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53EF")

    ChrTalk(    #271
        0xFE,
        (
            "It was such a wonderful ceremony that I just\x01",
            "want to bask in the moment for a bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "So my husband and I decided\x01",
            "to remain here for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "This might be the first time my husband and\x01",
            "I have come to the chapel since our wedding\x01",
            "ceremony...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "Sometime soon, we might just\x01",
            "have to come back here and go over our\x01",
            "own oaths again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_5484")

    label("loc_53EF")


    ChrTalk(    #275
        0xFE,
        (
            "It was such a wonderful ceremony that I just\x01",
            "want to bask in the moment for a bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "So my husband and I decided\x01",
            "to remain here for a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5484")

    Jump("loc_55D0")

    label("loc_5487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_5491")
    Jump("loc_55D0")

    label("loc_5491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_55D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5537")

    ChrTalk(    #277
        0xFE,
        "Oh, no. You shouldn't be over here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "You're going to wear the bride's dress soon,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "You can look forward to the ceremony.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_55D0")

    label("loc_5537")


    ChrTalk(    #280
        0xFE,
        (
            "Apparently, it's a pure-white dress. Your\x01",
            "boyfriend must've really gone all out, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "Heehee! I can't help but recall\x01",
            "my own wedding ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D0")

    TalkEnd(0x14)
    Return()

    # Function_15_527F end

    def Function_16_55D4(): pass

    label("Function_16_55D4")

    TalkBegin(0x21)

    ChrTalk(    #282
        0xFE,
        (
            "Hmph, you don't have to have a\x01",
            "ceremony on a day like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "I told the groom time and time again\x01",
            "that he should delay it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "But he's pretty stubborn.\x01",
            "He wouldn't hear a word of it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x21)
    Return()

    # Function_16_55D4 end

    def Function_17_569F(): pass

    label("Function_17_569F")

    TalkBegin(0x22)

    ChrTalk(    #285
        0xFE,
        "Armand's really nervous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "I'm kinda worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "Hopefully he doesn't mess up...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_17_569F end

    def Function_18_5701(): pass

    label("Function_18_5701")

    TalkBegin(0x23)

    ChrTalk(    #288
        0xFE,
        (
            "We're going to have the reception\x01",
            "party in the local bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "I heard the food there is really good,\x01",
            "so I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x23)
    Return()

    # Function_18_5701 end

    def Function_19_5791(): pass

    label("Function_19_5791")

    TalkBegin(0x24)

    ChrTalk(    #290
        0xFE,
        "The entire kingdom's having trouble right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "This is my precious granddaughter's wedding\x01",
            "ceremony... I hope it goes okay.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x24)
    Return()

    # Function_19_5791 end

    def Function_20_581E(): pass

    label("Function_20_581E")

    TalkBegin(0x25)

    ChrTalk(    #292
        0xFE,
        (
            "Other married women are helping\x01",
            "us get her dressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "It makes me smile to see that sense of\x01",
            "community still remains in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x25)
    Return()

    # Function_20_581E end

    def Function_21_58AD(): pass

    label("Function_21_58AD")

    TalkBegin(0x26)

    ChrTalk(    #294
        0xFE,
        "They said we can't go into this room right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "Mmmmrrrrrr... I really wanted to see my\x01",
            "sister's dress, too.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x26)
    Return()

    # Function_21_58AD end

    def Function_22_592B(): pass

    label("Function_22_592B")

    TalkBegin(0x27)

    ChrTalk(    #296
        0xFE,
        (
            "At first, I couldn't believe it when I heard\x01",
            "that Ellie was getting married.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "*sigh* I guess I've really been beaten\x01",
            "to the punch.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x27)
    Return()

    # Function_22_592B end

    def Function_23_59BE(): pass

    label("Function_23_59BE")

    TalkBegin(0x28)

    ChrTalk(    #298
        0xFE,
        (
            "At first I was happy to come\x01",
            "to my friend's wedding, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "Now I'm all worked up. I feel like\x01",
            "I need to find someone for me soon.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x28)
    Return()

    # Function_23_59BE end

    def Function_24_5A52(): pass

    label("Function_24_5A52")

    TalkBegin(0x17)

    ChrTalk(    #300
        0xFE,
        "Oh, will you be going to the wedding, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "You're still a bit early. I'm\x01",
            "about to go dress the bride.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_24_5A52 end

    def Function_25_5AC9(): pass

    label("Function_25_5AC9")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7C")

    ChrTalk(    #302
        0xFE,
        "Ahh, weddings are so touching.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "Remembering our own time made\x01",
            "me a bit wet in the eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "W-We're not even family, either...\x01",
            "It's a bit embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_5BE7")

    label("loc_5B7C")


    ChrTalk(    #305
        0xFE,
        "Weddings are so touching.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "We're not even family, but I still found\x01",
            "myself a bit wet in the eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BE7")

    TalkEnd(0x19)
    Return()

    # Function_25_5AC9 end

    def Function_26_5BEB(): pass

    label("Function_26_5BEB")

    EventBegin(0x0)
    OP_D2(0x27020F, 0x270214, 0x2)
    OP_D2(0x27043F, 0x270442, 0x3)
    OP_D2(0x270440, 0x270443, 0x4)
    OP_D2(0x260221, 0x260226, 0x6)
    OP_D2(0x260220, 0x260225, 0x7)
    SetChrChipByIndex(0x2A, 2)
    SetChrChipByIndex(0x2B, 3)
    SetChrChipByIndex(0x2C, 4)
    OP_51(0x2A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CE8")
    Call(0, 29)
    Call(0, 30)

    label("loc_5CE8")

    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0x21, 0x0)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x24, 0x0)
    OP_44(0x25, 0x0)
    OP_44(0x26, 0x0)
    OP_44(0x27, 0x0)
    OP_44(0x28, 0x0)
    SetChrPos(0x10, 58450, 1000, 50290, 0)
    SetChrPos(0xF, 59530, 1000, 50290, 0)
    SetChrPos(0x8, 59000, 1000, 52160, 180)
    SetChrPos(0x9, 60720, 1000, 52500, 180)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 61680, 0, 44470, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x23, 0x4)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x28, 0x4)
    SetChrChipByIndex(0x23, 30)
    SetChrSubChip(0x23, 0)
    SetChrChipByIndex(0x24, 33)
    SetChrSubChip(0x24, 0)
    SetChrChipByIndex(0x25, 22)
    SetChrSubChip(0x25, 0)
    SetChrPos(0x21, 53270, 0, 45590, 45)
    SetChrPos(0x22, 53920, 0, 45100, 0)
    SetChrPos(0x23, 54210, 150, 45960, 0)
    SetChrPos(0x24, 61700, 150, 45960, 0)
    SetChrPos(0x25, 63570, 0, 45960, 0)
    SetChrPos(0x26, 62600, 0, 45960, 0)
    SetChrPos(0x27, 63880, 0, 44470, 0)
    SetChrPos(0x28, 62690, 10, 44470, 0)
    SetChrPos(0x101, 58510, 0, 40820, 0)
    SetChrPos(0x102, 59450, 0, 40800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F42")
    SetChrPos(0xF8, 57880, 0, 39620, 0)
    SetChrPos(0xF9, 60090, 0, 39620, 0)
    Jump("loc_5F64")

    label("loc_5F42")

    SetChrPos(0xF9, 57880, 0, 39620, 0)
    SetChrPos(0xF8, 60090, 0, 39620, 0)

    label("loc_5F64")

    OP_6D(58360, 0, 41870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    OP_20(0x3E8)
    Sleep(1000)
    OP_21()
    OP_1D(0x60)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #307
        0x101,
        "#1011F#6PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        (
            "#1040F#5PHaha.\x02\x03",

            "Nice timing.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_600D():
        OP_6C(330000, 4000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_600D)
    OP_6D(59020, 1000, 50230, 4000)

    ChrTalk(    #309
        0x8,
        "...Now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x8,
        (
            "Please exchange your rings and\x01",
            "seal your oath with a kiss...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x1B)
    Sleep(200)
    OP_43(0x12, 0x1, 0x0, 0x1C)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    OP_8C(0xF, 270, 400)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    def lambda_60B7():
        OP_94(0x0, 0xFE, 0x0, 0x96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_60B7)
    OP_94(0x0, 0x10, 0x0, 0x96, 0x1F4, 0x0)
    Sleep(500)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 59030, 1000, 50240, 330)
    SetChrPos(0xD, 59300, 1000, 50400, 263)

    NpcTalk(    #311
        0xB,
        "Armand",
        "#3PEllie...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #312
        0xD,
        "Ellie",
        "#4PArmand...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)

    def lambda_6151():
        OP_94(0x0, 0xFE, 0x0, 0x96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6151)
    OP_94(0x0, 0x10, 0x0, 0x96, 0x1F4, 0x0)
    OP_62(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #313
        0x8,
        "In the name of the Goddess of creation, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x8,
        "Here and now, I declare you man and wife.\x02",
    )

    CloseMessageWindow()
    OP_22(0xBF, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Fade(1000)
    OP_6D(58360, 0, 41870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D4")

    ChrTalk(    #315
        0x107,
        "#067FAwww, it's so lovely.\x02",
    )

    CloseMessageWindow()

    label("loc_65D4")


    ChrTalk(    #316
        0x101,
        "#1017F#6PAhaha, yeah. Gets you right in the heart, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x102,
        "#1053F#5PYeah, it really does.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6714")

    ChrTalk(    #318
        0x106,
        "#057F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #319
        0x101,
        (
            "#1019F#6PAgate, why are you glaring at the\x01",
            "bride and groom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x106,
        (
            "#552FNo, I'm not, it's just...\x02\x03",

            "How can you watch something so embarrassing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#1015F#6PReally? I think it's nice.\x02",
    )

    CloseMessageWindow()

    label("loc_6714")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6780")

    ChrTalk(    #322
        0x108,
        (
            "#071FHaha, must be something that brought us here.\x02\x03",

            "Let us offer our own blessings, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6898")

    ChrTalk(    #323
        0x103,
        (
            "#025FAhhh, I really love her dress...\x02\x03",

            "#020FOh! The ceremony's over, so now we\x01",
            "get to the good stuff.\x02\x03",

            "Once the bride and groom leave, hurry outside.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #324
        0x101,
        "#1011F#6PHuh? Why?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #325
        0x102,
        (
            "#1040F#2PAh, yes...\x02\x03",

            "There's an event the women won't want to miss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6898")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0100   ._SN", 117, 0, 0)
    IdleLoop()
    Return()

    # Function_26_5BEB end

    def Function_27_68B0(): pass

    label("Function_27_68B0")

    OP_8E(0xFE, 0xED30, 0x3E8, 0xC472, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEBD2, 0x3E8, 0xC472, 0x7D0, 0x0)
    OP_8C(0xF, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xF, 0, 400)
    OP_8E(0xFE, 0xED30, 0x3E8, 0xCD14, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_27_68B0 end

    def Function_28_690E(): pass

    label("Function_28_690E")

    OP_8E(0xFE, 0xE146, 0x3E8, 0xC472, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8C(0x10, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8C(0x10, 0, 400)
    OP_8E(0xFE, 0xE146, 0x0, 0xBEF0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_690E end

    def Function_29_695F(): pass

    label("Function_29_695F")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_69DB"),
        (1, "loc_69E1"),
        (SWITCH_DEFAULT, "loc_69E7"),
    )


    label("loc_69DB")

    OP_A2(0x1200)
    Jump("loc_69E7")

    label("loc_69E1")

    OP_A2(0x1201)
    Jump("loc_69E7")

    label("loc_69E7")

    Return()

    # Function_29_695F end

    def Function_30_69E8(): pass

    label("Function_30_69E8")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_30_69E8 end

    SaveToFile()

Try(main)
