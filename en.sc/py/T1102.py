from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1102   ._SN',
        MapName             = 'Bose',
        Location            = 'T1102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 43,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1102_1 ._SN',
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
        'Passenger',                            # 15
        'Passenger',                            # 16
        'Passenger',                            # 17
        'Passenger',                            # 18
        'Passenger',                            # 19
        'Passenger',                            # 20
        'Nial',                                 # 21
        'Dorothy',                              # 22
        'Captain Schwarz',                      # 23
        'General Morgan',                       # 24
        'Receptionist Ted',                     # 25
        'Lakely',                               # 26
        'Norm',                                 # 27
        'Berna',                                # 28
        'Aldan',                                # 29
        'Corna',                                # 30
        'Morie',                                # 31
        'Cecilia Passenger',                    # 32
        'Cecilia Passenger',                    # 33
        'Cecilia Passenger',                    # 34
        'Cecilia Passenger',                    # 35
        'Cecilia Passenger',                    # 36
        'Captain Petrov',                       # 37
        'Crew Mem. Nora',                       # 38
        'Forklift',                             # 39
        'Shaque',                               # 40
        'Skyship',                              # 41
        '飛行艇影',                             # 42
        'フォークリフト',                       # 43
        'Bose - North Block',                   # 44
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
        'ED6_DT07/CH00050 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH01110 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH01130 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT07/CH01150 ._CH',             # 0B
        'ED6_DT07/CH02060 ._CH',             # 0C
        'ED6_DT07/CH02070 ._CH',             # 0D
        'ED6_DT27/CH03580 ._CH',             # 0E
        'ED6_DT07/CH02080 ._CH',             # 0F
        'ED6_DT07/CH01290 ._CH',             # 10
        'ED6_DT06/CH20063 ._CH',             # 11
        'ED6_DT06/CH20129 ._CH',             # 12
        'ED6_DT06/CH20051 ._CH',             # 13
        'ED6_DT07/CH01450 ._CH',             # 14
        'ED6_DT07/CH01210 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
        'ED6_DT07/CH01453 ._CH',             # 18
        'ED6_DT07/CH00051 ._CH',             # 19
        'ED6_DT07/CH00061 ._CH',             # 1A
        'ED6_DT07/CH01050 ._CH',             # 1B
        'ED6_DT07/CH01020 ._CH',             # 1C
        'ED6_DT07/CH01170 ._CH',             # 1D
        'ED6_DT07/CH01440 ._CH',             # 1E
        'ED6_DT07/CH01540 ._CH',             # 1F
        'ED6_DT26/CH20311 ._CH',             # 20
        'ED6_DT07/CH01460 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00050P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH01110P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH01130P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT07/CH01150P._CP',             # 0B
        'ED6_DT07/CH02060P._CP',             # 0C
        'ED6_DT07/CH02070P._CP',             # 0D
        'ED6_DT27/CH03580P._CP',             # 0E
        'ED6_DT07/CH02080P._CP',             # 0F
        'ED6_DT07/CH01290P._CP',             # 10
        'ED6_DT06/CH20063P._CP',             # 11
        'ED6_DT06/CH20129P._CP',             # 12
        'ED6_DT06/CH20051P._CP',             # 13
        'ED6_DT07/CH01450P._CP',             # 14
        'ED6_DT07/CH01210P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
        'ED6_DT07/CH01453P._CP',             # 18
        'ED6_DT07/CH00051P._CP',             # 19
        'ED6_DT07/CH00061P._CP',             # 1A
        'ED6_DT07/CH01050P._CP',             # 1B
        'ED6_DT07/CH01020P._CP',             # 1C
        'ED6_DT07/CH01170P._CP',             # 1D
        'ED6_DT07/CH01440P._CP',             # 1E
        'ED6_DT07/CH01540P._CP',             # 1F
        'ED6_DT26/CH20311P._CP',             # 20
        'ED6_DT07/CH01460P._CP',             # 21
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46050,
        Z                   = 0,
        Y                   = 19400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27300,
        Z                   = -10000,
        Y                   = 26800,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 48500,
        Z                   = 1500,
        Y                   = 36800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 0,
        Y                   = 14100,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 1500,
        Y                   = 47600,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 1500,
        Y                   = 49740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48340,
        Z                   = 0,
        Y                   = 12210,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 44940,
        Z                   = 0,
        Y                   = 15680,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 50290,
        Z                   = 0,
        Y                   = 16239,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 51900,
        Z                   = 0,
        Y                   = 13500,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 51890,
        Z                   = 0,
        Y                   = 14350,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 45050,
        Z                   = 0,
        Y                   = 11720,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 48780,
        Z                   = 1500,
        Y                   = 43400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 48140,
        Z                   = 0,
        Y                   = 18710,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 29420,
        Z                   = -3000,
        Y                   = 17280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 50900,
        Z                   = 0,
        Y                   = 18020,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48090,
        Z                   = 3000,
        Y                   = -20910,
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
        X                   = 48000,
        Y                   = -2000,
        Z                   = 25600,
        Range               = 52000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x6E8C,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )


    DeclActor(
        TriggerX            = 46070,
        TriggerZ            = 0,
        TriggerY            = 18140,
        TriggerRange        = 600,
        ActorX              = 46050,
        ActorZ              = 1500,
        ActorY              = 19400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25480,
        TriggerZ            = -3000,
        TriggerY            = 11080,
        TriggerRange        = 1600,
        ActorX              = 25480,
        ActorZ              = -1000,
        ActorY              = 11080,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47780,
        TriggerZ            = 0,
        TriggerY            = 15880,
        TriggerRange        = 800,
        ActorX              = 47780,
        ActorZ              = 2200,
        ActorY              = 15880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34950,
        TriggerZ            = -10000,
        TriggerY            = 24520,
        TriggerRange        = 800,
        ActorX              = 34950,
        ActorZ              = -7800,
        ActorY              = 24520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60000,
        TriggerZ            = 0,
        TriggerY            = 17090,
        TriggerRange        = 800,
        ActorX              = 60000,
        ActorZ              = 1500,
        ActorY              = 17090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 42,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_70E",          # 00, 0
        "Function_1_8A5",          # 01, 1
        "Function_2_9C5",          # 02, 2
        "Function_3_9E9",          # 03, 3
        "Function_4_9EE",          # 04, 4
        "Function_5_16C7",         # 05, 5
        "Function_6_1B72",         # 06, 6
        "Function_7_1FE1",         # 07, 7
        "Function_8_2A7F",         # 08, 8
        "Function_9_3389",         # 09, 9
        "Function_10_35E0",        # 0A, 10
        "Function_11_36A0",        # 0B, 11
        "Function_12_37C9",        # 0C, 12
        "Function_13_3939",        # 0D, 13
        "Function_14_3A05",        # 0E, 14
        "Function_15_3A7F",        # 0F, 15
        "Function_16_3B1D",        # 10, 16
        "Function_17_3E77",        # 11, 17
        "Function_18_4183",        # 12, 18
        "Function_19_42D0",        # 13, 19
        "Function_20_444A",        # 14, 20
        "Function_21_4654",        # 15, 21
        "Function_22_46CF",        # 16, 22
        "Function_23_4BDA",        # 17, 23
        "Function_24_549E",        # 18, 24
        "Function_25_5C3F",        # 19, 25
        "Function_26_7CE3",        # 1A, 26
        "Function_27_7D96",        # 1B, 27
        "Function_28_7DD3",        # 1C, 28
        "Function_29_7DFC",        # 1D, 29
        "Function_30_7E57",        # 1E, 30
        "Function_31_7EA0",        # 1F, 31
        "Function_32_7EB7",        # 20, 32
        "Function_33_820A",        # 21, 33
        "Function_34_855D",        # 22, 34
        "Function_35_868A",        # 23, 35
        "Function_36_86DB",        # 24, 36
        "Function_37_87C6",        # 25, 37
        "Function_38_9311",        # 26, 38
        "Function_39_9397",        # 27, 39
        "Function_40_9518",        # 28, 40
        "Function_41_9582",        # 29, 41
        "Function_42_9601",        # 2A, 42
        "Function_43_968F",        # 2B, 43
        "Function_44_97C7",        # 2C, 44
    )


    def Function_0_70E(): pass

    label("Function_0_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_724")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_77E")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_743")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 25)
    Jump("loc_77E")

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_762")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_77E")

    label("loc_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_77E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_802")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x19, 48770, 1500, 42170, 0)
    SetChrPos(0x1A, 31910, -10000, 26200, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_7FF")

    label("loc_7E9")

    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x25, 51300, 1500, 35740, 96)

    label("loc_7FF")

    Jump("loc_8A4")

    label("loc_802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_81B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_818")
    ClearChrFlags(0x1D, 0x80)

    label("loc_818")

    Jump("loc_8A4")

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_836")
    SetChrPos(0x1C, 46320, 3000, -1140, 0)
    Jump("loc_8A4")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_867")
    SetChrFlags(0x1C, 0x80)
    SetChrPos(0x1A, 25620, -10000, 26830, 45)
    SetChrPos(0x1B, 25890, -3000, 17040, 0)
    Jump("loc_8A4")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_89D")
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x19, 0x10)
    SetChrPos(0x19, 27300, -10000, 26800, 0)
    SetChrPos(0x1A, 48500, 1500, 36800, 0)
    Jump("loc_8A4")

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_8A4")

    label("loc_8A4")

    Return()

    # Function_0_70E end

    def Function_1_8A5(): pass

    label("Function_1_8A5")

    OP_16(0x2, 0xFA0, 0xFFFE8518, 0xFFFE98A0, 0x230042)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    OP_B1("T1102_2")
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_6F(0x7, 410)
    Jump("loc_93D")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_90C")
    OP_B1("T1102_3")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_93D")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_920")
    OP_B1("T1102_2")
    Jump("loc_93D")

    label("loc_920")

    OP_B1("T1102_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0x9, 0x4)

    label("loc_93D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_947")
    Jump("loc_97E")

    label("loc_947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_957")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_97E")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_967")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_97E")

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_977")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_97E")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_97E")

    label("loc_97E")

    OP_64(0x1, 0x1)
    OP_A1(0x2A, 0xD)
    SetChrPos(0x2A, 26510, -3000, 10000, 135)
    OP_72(0xD, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C4")
    OP_65(0x1, 0x1)

    label("loc_9C4")

    Return()

    # Function_1_8A5 end

    def Function_2_9C5(): pass

    label("Function_2_9C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9E8")
    OP_8D(0xFE, 45950, 15590, 50720, 11210, 1500)
    Jump("Function_2_9C5")

    label("loc_9E8")

    Return()

    # Function_2_9C5 end

    def Function_3_9E9(): pass

    label("Function_3_9E9")

    Call(0, 4)
    Return()

    # Function_3_9E9 end

    def Function_4_9EE(): pass

    label("Function_4_9EE")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_B4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAA")

    ChrTalk(    #0
        0x18,
        (
            "That customer over there...\x01",
            "He's real stubborn and refuses to move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x18,
        (
            "I'm not sure what to do. It's not like we can\x01",
            "launch a ship on wishes and fairy dust.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_B47")

    label("loc_AAA")


    ChrTalk(    #2
        0x18,
        (
            "Mmmmm, but having him hang around\x01",
            "here'll only cause more trouble. ARGH.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x18,
        (
            "We still don't have a clear idea of when\x01",
            "we'll be able to resume service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B47")

    Jump("loc_16C3")

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C47")

    ChrTalk(    #4
        0x18,
        (
            "Man, there's a bunch of customers here\x01",
            "who don't have any place to go now that\x01",
            "they're stuck here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x18,
        (
            "We're trying to pull together some lodging\x01",
            "for them, but you can imagine how much\x01",
            "of a mess that is right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 180, 400)
    SetChrFlags(0x18, 0x10)
    OP_A2(0x0)
    Jump("loc_CDF")

    label("loc_C47")


    ChrTalk(    #6
        0x18,
        (
            "The Company will provide lodging for\x01",
            "everyone! Yes, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x18,
        (
            "We're currently in the process of\x01",
            "arranging it, so please wait a little\x01",
            "longer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDF")

    Jump("loc_16C3")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D8B")

    ChrTalk(    #8
        0x18,
        (
            "The talk around town is that you guys\x01",
            "were pivotal in stopping the dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x18,
        (
            "I'll be toasting the guild with a couple\x01",
            "drinks tonight, trust me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E89")

    label("loc_D8B")


    ChrTalk(    #10
        0x18,
        "Hey, everyone! Great work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x18,
        (
            "The talk around town is that you guys\x01",
            "were pivotal in stopping the dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x18,
        (
            "First the sky bandits, now this.\x01",
            "You've saved Bose twice now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x18,
        (
            "I'll be toasting the guild with a couple\x01",
            "drinks tonight, trust me!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E89")

    Jump("loc_16C3")

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(    #14
        0x18,
        (
            "The Arseille's flight plan is getting\x01",
            "real erratic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x18,
        (
            "Guess the capture plan's hitting its\x01",
            "climax, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCA")

    label("loc_F0D")


    ChrTalk(    #16
        0x18,
        (
            "The Arseille's flight plan is getting\x01",
            "real erratic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x18,
        (
            "Guess the capture plan's hitting its\x01",
            "climax, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x18,
        (
            "I hope this whole thing ends soon\x01",
            "so we can get flights going again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FCA")

    Jump("loc_16C3")

    label("loc_FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_111A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1052")

    ChrTalk(    #19
        0x18,
        (
            "The army airship you'll be boarding\x01",
            "will be docking soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x18,
        (
            "You're to go meet it at Dock One,\x01",
            "to the right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_1052")

    OP_62(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #21
        0x18,
        (
            "You guys are the bracers I was told about,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x18,
        (
            "The army airship you'll be boarding\x01",
            "will be docking soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x18,
        (
            "You're to go meet it at Dock One,\x01",
            "to the right.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1117")

    Jump("loc_16C3")

    label("loc_111A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11AA")

    ChrTalk(    #24
        0x18,
        (
            "There was this huge shadow flying\x01",
            "northwest just now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x18,
        (
            "Man, I'm just glad it didn't run into\x01",
            "any ships along the way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1236")

    label("loc_11AA")


    ChrTalk(    #26
        0x18,
        (
            "Th-There was this huge shadow\x01",
            "flying off just now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x18,
        (
            "The way it looked... No way.\x01",
            "Was it really a dragon?\x01",
            "Like from the legends?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1236")

    Jump("loc_16C3")

    label("loc_1239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_16C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 3)), scpexpr(EXPR_END)), "loc_14AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12FB")

    ChrTalk(    #28
        0x18,
        (
            "The flight schedule's been real steady\x01",
            "lately, and I'm glad for it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x18,
        (
            "I think it's because ever since the coup\x01",
            "ended, the world's stabilized quite a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1443")

    label("loc_12FB")


    ChrTalk(    #30
        0x18,
        (
            "The flight schedule's been real steady\x01",
            "lately, and I'm glad for it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x18,
        (
            "I think it's because ever since the coup\x01",
            "ended, the world's stabilized quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x18,
        (
            "There was that scare with the sky bandits\x01",
            "too, sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x18,
        (
            "But nobody's seen or heard from them in a\x01",
            "while, so they're probably a long way\x01",
            "from Liberl by now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1443")

    Jump("loc_14A9")

    label("loc_1446")


    ChrTalk(    #34
        0x18,
        "Agate, man, you're always so busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x18,
        (
            "You really need to find some time\x01",
            "to relax, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A9")

    Jump("loc_16C3")

    label("loc_14AC")

    TurnDirection(0x18, 0x106, 0)

    ChrTalk(    #36
        0x18,
        "Oh, hey, Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        "#051FYo, Ted. How're you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x18,
        (
            "Not too bad. You got in on that\x01",
            "flight a bit ago, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x18,
        (
            "You, uh...here to visit the hometown\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        (
            "#053FNo, it's work this time.\x02\x03",

            "#051FProbably gonna stop in once things are\x01",
            "settled, though.\x01",
            "(Or get strong-armed into it...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x18,
        (
            "Well, ain't a bad idea to visit home every\x01",
            "now and then, y'know? Like, remember\x01",
            "what you're fightin' for and stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x18,
        (
            "Anyway, hey, if I can do anything for\x01",
            "you, you know where to find me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x106,
        "#051FYeah, of course.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A43)
    OP_A2(0x0)

    label("loc_16C3")

    TalkEnd(0x18)
    Return()

    # Function_4_9EE end

    def Function_5_16C7(): pass

    label("Function_5_16C7")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_173C")

    ChrTalk(    #44
        0xFE,
        "The flight schedule is back to normal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I can FINALLY set out on this trip I've\x01",
            "been delaying!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6E")

    label("loc_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17AA")

    ChrTalk(    #46
        0xFE,
        (
            "The scheduled flights still haven't been\x01",
            "restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Perhaps I should delay my trip.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1834")

    label("loc_17AA")


    ChrTalk(    #48
        0xFE,
        (
            "The scheduled flights still haven't been\x01",
            "restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "When will the army let us fly again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Perhaps I should delay my trip.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1834")

    Jump("loc_1B6E")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_18C0")

    ChrTalk(    #51
        0xFE,
        (
            "*sigh* Of course flights are canceled\x01",
            "just as I set off on my trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "I must be cursed when it comes to travel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B5")

    label("loc_18C0")


    ChrTalk(    #53
        0xFE,
        (
            "Thanks to the army's orders, the flights\x01",
            "that are usually scheduled to come through\x01",
            "are grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "*sigh* Of course flights are canceled\x01",
            "just as I set off on my trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Last time I planned a trip was during\x01",
            "that sky bandit scare.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_19B5")

    Jump("loc_1B6E")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1A15")

    ChrTalk(    #56
        0xFE,
        "Wh-What was that?! A monster?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Sweet Aidios, where did THAT come from...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B6E")

    label("loc_1A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A8D")

    ChrTalk(    #58
        0xFE,
        (
            "I have a ticket reserved for Grancel\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I hope the afternoon flight will be\x01",
            "relaxing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6E")

    label("loc_1A8D")


    ChrTalk(    #60
        0xFE,
        (
            "I have a ticket reserved for Grancel\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I had a hard time before when the sky\x01",
            "bandit scare happened and the flights\x01",
            "were canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "That whole incident really made me\x01",
            "appreciate airships all the more.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1B6E")

    TalkEnd(0x1B)
    Return()

    # Function_5_16C7 end

    def Function_6_1B72(): pass

    label("Function_6_1B72")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C12")

    ChrTalk(    #63
        0xFE,
        "I come to this port every day, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Why was I not here the one time the\x01",
            "Arseille showed up?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "I'm an IDIOT! A complete idiot!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CD1")

    label("loc_1C12")


    ChrTalk(    #66
        0xFE,
        (
            "I was going to take pictures of the airships\x01",
            "this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I don't know now.\x01",
            "I don't feel up to it anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The shock of missing the Arseille has\x01",
            "robbed me of my passion!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1CD1")

    Jump("loc_1FDD")

    label("loc_1CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1E12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 6)), scpexpr(EXPR_END)), "loc_1D2D")

    ChrTalk(    #69
        0xFE,
        "I... I missed the Arseille...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "I'm an IDIOT! A complete idiot!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0F")

    label("loc_1D2D")


    ChrTalk(    #71
        0xFE,
        "Hey, hey, you all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Is it true the Arseille's in port here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015FEr, it WAS, but, uh.\x02\x03",

            "I'm afraid it's already left.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xFE)

    ChrTalk(    #74
        0xFE,
        (
            "#3SNo...\x01",
            "Noooooooooooooooooooooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "I, I missed it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A46)

    label("loc_1E0F")

    Jump("loc_1FDD")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1FDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1ECA")

    ChrTalk(    #76
        0xFE,
        (
            "I may have missed the Arseille,\x01",
            "but this was still a great photo trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "If fate finally leads me to the Arseille\x01",
            "someday, I will take ALL the pictures of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDD")

    label("loc_1ECA")


    ChrTalk(    #78
        0xFE,
        "Finally back in Bose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I've been going all over, from Grancel to\x01",
            "Zeiss to here, chasing the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "While I ultimately never found it,\x01",
            "it was still a good trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Next time, though, I'll capture the Arseille\x01",
            "on film for sure--it can't elude me\x01",
            "forever!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1FDD")

    TalkEnd(0x1C)
    Return()

    # Function_6_1B72 end

    def Function_7_1FE1(): pass

    label("Function_7_1FE1")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2116")

    ChrTalk(    #82
        0xFE,
        "Darn it all! The Cecilia's engine is just fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "None of the components are damaged at all.\x01",
            "This thing SHOULD work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I thought I might find the reason for the\x01",
            "orbal failure by looking at the Cecilia's\x01",
            "engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "But the way this is going, I'm barking up\x01",
            "the wrong tree.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2193")

    label("loc_2116")


    ChrTalk(    #86
        0xFE,
        "Darn it all! The Cecilia's engine is just fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "None of the components are damaged at all.\x01",
            "This thing SHOULD work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2193")

    Jump("loc_2A7B")

    label("loc_2196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_235B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C7")

    ChrTalk(    #88
        0xFE,
        (
            "I'm going over the Cecilia's engines,\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "If she's been knocked out by the same thing\x01",
            "that's gotten to the rest of the orbments, I'd\x01",
            "like to know what the internals look like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Gonna take a good, close look inside and\x01",
            "figure out what happened when it stopped.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2358")

    label("loc_22C7")


    ChrTalk(    #91
        0xFE,
        (
            "I'm going over the Cecilia's engines,\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Gonna take a good, close look inside and\x01",
            "figure out what happened when it stopped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2358")

    Jump("loc_2A7B")

    label("loc_235B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_242E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_23BF")

    ChrTalk(    #93
        0xFE,
        "Next up is the Linde.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Gonna get her in the air without\x01",
            "a second's delay!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_23BF")


    ChrTalk(    #95
        0xFE,
        "Aaaaaall right! Next up is the Linde.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "It's a good feeling, knowing the ships're\x01",
            "running again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_242B")

    Jump("loc_2A7B")

    label("loc_242E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_24C1")

    ChrTalk(    #97
        0xFE,
        (
            "Ah, you kids.\x01",
            "How's your investigation going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I don't know exactly what you intend\x01",
            "to do, but make sure you settle this, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7B")

    label("loc_24C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_26DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2560")

    ChrTalk(    #99
        0xFE,
        (
            "The Arseille puts even the rumors to\x01",
            "shame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I mean, it performs like an angel of\x01",
            "She Above, sure, but it's also so easy\x01",
            "to work on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DC")

    label("loc_2560")


    ChrTalk(    #101
        0xFE,
        "Mmmmm, the Arseille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "At first I thought a giant pain in the\x01",
            "butt had wandered into my dock,\x01",
            "but it's better than even the rumors say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "I mean, it performs like an angel of\x01",
            "She Above, sure, but it's also so easy\x01",
            "to work on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Being able to do inspections and service\x01",
            "is more important than even I'd realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Heh, bet it'd be real obvious in an\x01",
            "emergency.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_26DC")

    Jump("loc_2A7B")

    label("loc_26DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_285C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_275E")

    ChrTalk(    #106
        0xFE,
        "That army ship should be here soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Right now we're getting ready to get\x01",
            "it docked up and serviced.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2859")

    label("loc_275E")


    ChrTalk(    #108
        0xFE,
        "That army ship should be here soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Right now we're getting ready to get\x01",
            "it docked up and serviced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Apparently the army has some big plan\x01",
            "to save us all, so they've stopped the\x01",
            "usual flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "I just hope their plan is worth it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2859")

    Jump("loc_2A7B")

    label("loc_285C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2956")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28C9")

    ChrTalk(    #112
        0xFE,
        "An ancient dragon, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Damn it all to Gehenna.\x01",
            "As if things weren't already bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2953")

    label("loc_28C9")


    ChrTalk(    #114
        0xFE,
        "Can't be. That, thing just now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Was that...an ancient dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Damn it all to Gehenna.\x01",
            "As if things weren't already bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2953")

    Jump("loc_2A7B")

    label("loc_2956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_29D5")

    ChrTalk(    #117
        0xFE,
        (
            "Got a bit of time before the Linde\x01",
            "comes bumblin' in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "I should give the equipment a once-over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A7B")

    label("loc_29D5")


    ChrTalk(    #119
        0xFE,
        (
            "All right, the Cecilia got underway\x01",
            "no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Got a bit of time before the Linde\x01",
            "comes bumblin' in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "I should give the equipment a once-over.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2A7B")

    TalkEnd(0x19)
    Return()

    # Function_7_1FE1 end

    def Function_8_2A7F(): pass

    label("Function_8_2A7F")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B37")

    ChrTalk(    #122
        0xFE,
        (
            "The Cecilia's still stuck in port like it\x01",
            "has been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Even the boss is losing his cool over\x01",
            "all this now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "I've never seen him so worked up before.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2B9E")

    label("loc_2B37")


    ChrTalk(    #125
        0xFE,
        (
            "Even the boss is losing his cool over\x01",
            "all this now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "I've never seen him so worked up before.\x02",
    )

    CloseMessageWindow()

    label("loc_2B9E")

    Jump("loc_3385")

    label("loc_2BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB1")

    ChrTalk(    #127
        0xFE,
        (
            "It's not just the Cecilia, the guidance\x01",
            "lights and ground equipment aren't\x01",
            "working either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "We've had our share of trouble before,\x01",
            "but I've never seen anything like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I wonder if this is all because of that\x01",
            "strange event last night?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2D65")

    label("loc_2CB1")


    ChrTalk(    #130
        0xFE,
        (
            "It's not just the Cecilia, the guidance\x01",
            "lights and ground equipment aren't\x01",
            "working either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "We've had our share of trouble before,\x01",
            "but I've never seen anything like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D65")

    Jump("loc_3385")

    label("loc_2D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2DF8")

    ChrTalk(    #132
        0xFE,
        (
            "Flights are going on schedule again,\x01",
            "thankfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "The market's back in business, too,\x01",
            "so everything's back to normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA5")

    label("loc_2DF8")


    ChrTalk(    #134
        0xFE,
        (
            "Flights are going on schedule again,\x01",
            "thankfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "The market's back in business, too,\x01",
            "so everything's back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Time for me to get back to work, too!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2EA5")

    Jump("loc_3385")

    label("loc_2EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F05")

    ChrTalk(    #137
        0xFE,
        (
            "I never thought I'd ever work the\x01",
            "dock where the ARSEILLE was berthed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE0")

    label("loc_2F05")


    ChrTalk(    #138
        0xFE,
        (
            "I never thought I'd ever work the\x01",
            "dock where the ARSEILLE was berthed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I had trouble even staying calm at first!\x01",
            "Glad I managed to pull myself together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "It's all thanks to the boss'\x01",
            "constant training.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2FE0")

    Jump("loc_3385")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_304C")

    ChrTalk(    #141
        0xFE,
        (
            "Normal flights've been canceled,\x01",
            "but we've got an army ship coming in,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3105")

    label("loc_304C")


    ChrTalk(    #142
        0xFE,
        (
            "Normal flights've been canceled,\x01",
            "but we've got an army ship coming in,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "We're trying to get ready, but those\x01",
            "army birds are so different than\x01",
            "commercial liners!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3105")

    Jump("loc_3385")

    label("loc_3108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_31CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3154")

    ChrTalk(    #144
        0xFE,
        (
            "Wh-Wh-What was that huge monster that\x01",
            "just flew off?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C9")

    label("loc_3154")


    ChrTalk(    #145
        0xFE,
        (
            "Wh-Wh-What was that huge monster that\x01",
            "just flew off?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "It was practically the size of a\x01",
            "passenger liner!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_31C9")

    Jump("loc_3385")

    label("loc_31CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3385")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_327D")

    ChrTalk(    #147
        0xFE,
        "All right, that's the Cecilia in the air.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Scheduled liners don't have much\x01",
            "time between takeoff and landing,\x01",
            "so it's always a race to get them ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3385")

    label("loc_327D")


    ChrTalk(    #149
        0xFE,
        "The Cecilia's arrived on time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "No equipment problems... Check.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "All right, we managed to send it off\x01",
            "with no delays again! Somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "Scheduled liners don't have much\x01",
            "time between takeoff and landing,\x01",
            "so it's always a race to get them ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3385")

    TalkEnd(0x1A)
    Return()

    # Function_8_2A7F end

    def Function_9_3389(): pass

    label("Function_9_3389")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_35DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3449")

    ChrTalk(    #153
        0xFE,
        (
            "We talked about Lila coming to visit us,\x01",
            "but I think I would like to come back\x01",
            "here someday, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Everyone, please keep Lila safe until\x01",
            "one or the other happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35DC")

    label("loc_3449")


    ChrTalk(    #155
        0xFE,
        (
            "Everyone! Hello again.\x01",
            "Thank you again for everything you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1011FOh, Ms. Corna!\x02\x03",

            "Are you heading back home now\x01",
            "that you've found Lila?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #157
        0xFE,
        (
            "Yes. I'm still a little sad to leave her behind,\x01",
            "but I know she's safe. That's enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "Please, take care of Lila for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1006FI promise we will!\x02\x03",

            "And give our best to the rest of your\x01",
            "family, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Of course. Farewell!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_35DC")

    TalkEnd(0x1D)
    Return()

    # Function_9_3389 end

    def Function_10_35E0(): pass

    label("Function_10_35E0")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3667")

    ChrTalk(    #161
        0xFE,
        (
            "When are the flights going to get\x01",
            "moving again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Argh, just standing around like this\x01",
            "is really frustrating!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_369C")

    label("loc_3667")


    ChrTalk(    #163
        0xFE,
        (
            "When are the flights going to get\x01",
            "moving again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369C")

    TalkEnd(0x1E)
    Return()

    # Function_10_35E0 end

    def Function_11_36A0(): pass

    label("Function_11_36A0")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3718")

    ChrTalk(    #164
        0xFE,
        "I'm going to wait right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I mean, who knows when the ships\x01",
            "might start working again, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C5")

    label("loc_3718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_37C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3788")

    ChrTalk(    #166
        0xFE,
        (
            "Mmmph! How long are they going to\x01",
            "keep us waiting here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "I need to hurry to Ruan!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_37C5")

    label("loc_3788")


    ChrTalk(    #168
        0xFE,
        (
            "Mmmph! How long are they going to\x01",
            "keep us waiting here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C5")

    TalkEnd(0x1F)
    Return()

    # Function_11_36A0 end

    def Function_12_37C9(): pass

    label("Function_12_37C9")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3890")

    ChrTalk(    #169
        0xFE,
        (
            "Apparently it's some kind of engine fault\x01",
            "with a cause they can't determine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I've used these ships for years and this\x01",
            "is the first time I've ever seen something\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3935")

    label("loc_3890")


    ChrTalk(    #171
        0xFE,
        (
            "Apparently it's some kind of engine fault\x01",
            "with a cause they can't determine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I wonder if it's the same thing causing\x01",
            "the orbments in town to stop working.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3935")

    TalkEnd(0x20)
    Return()

    # Function_12_37C9 end

    def Function_13_3939(): pass

    label("Function_13_3939")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C0")

    ChrTalk(    #173
        0xFE,
        (
            "Oh, dear, oh, dear... I didn't think we'd\x01",
            "be stopping here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "My child is with me, too.\x01",
            "How am I to get home?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_3A01")

    label("loc_39C0")


    ChrTalk(    #175
        0xFE,
        (
            "Oh, dear, oh, dear... I didn't think we'd\x01",
            "be stopping here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A01")

    TalkEnd(0x21)
    Return()

    # Function_13_3939 end

    def Function_14_3A05(): pass

    label("Function_14_3A05")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A55")

    ChrTalk(    #176
        0xFE,
        "Hey, what's wrong with the ship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Why isn't it going?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3A7B")

    label("loc_3A55")


    ChrTalk(    #178
        0xFE,
        "Hey, what's wrong with the ship?\x02",
    )

    CloseMessageWindow()

    label("loc_3A7B")

    TalkEnd(0x22)
    Return()

    # Function_14_3A05 end

    def Function_15_3A7F(): pass

    label("Function_15_3A7F")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEA")

    ChrTalk(    #179
        0xFE,
        "The scheduled flights aren't running?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "Damn it all, just as I get off work, too!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_3B19")

    label("loc_3AEA")


    ChrTalk(    #181
        0xFE,
        "Damn it all, just as I get off work, too!\x02",
    )

    CloseMessageWindow()

    label("loc_3B19")

    TalkEnd(0x23)
    Return()

    # Function_15_3A7F end

    def Function_16_3B1D(): pass

    label("Function_16_3B1D")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C12")

    ChrTalk(    #182
        0xFE,
        (
            "It's just as I feared. Nothing is\x01",
            "wrong with the ship itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "It's this thrice-damned strangeness with the\x01",
            "orbments preventing the engines from\x01",
            "activating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "That's that, then.\x01",
            "There's very little we can do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_3CD5")

    label("loc_3C12")


    ChrTalk(    #185
        0xFE,
        (
            "The engines are non-functional due to this\x01",
            "damned 'phenomenon' or whatever you want\x01",
            "to call it, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "There's nothing we can do against something\x01",
            "we can't even see except sit here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD5")

    Jump("loc_3E73")

    label("loc_3CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD2")

    ChrTalk(    #187
        0xFE,
        (
            "The engine not functioning gives us more\x01",
            "problems than simply getting airborne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Hells! We had to operate the ramp via\x01",
            "hand-crank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I do wish our passengers understood the\x01",
            "theory behind orbal engines a wee bit more.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_3E73")

    label("loc_3DD2")


    ChrTalk(    #190
        0xFE,
        (
            "Ah, regardless. If this had to happen,\x01",
            "by Aidios' grace had it happen on land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "If this had happened in the air, we'd\x01",
            "all be at Her side at this point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E73")

    TalkEnd(0x24)
    Return()

    # Function_16_3B1D end

    def Function_17_3E77(): pass

    label("Function_17_3E77")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F21")

    ChrTalk(    #192
        0xFE,
        (
            "It seems like resuming our flights will\x01",
            "be really difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "All of the maintenance crews are scratching\x01",
            "their heads over our problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3FB1")

    label("loc_3F21")


    ChrTalk(    #194
        0xFE,
        (
            "It seems like resuming our flights will\x01",
            "be really difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "I wonder if the company's trying to come\x01",
            "up with a response to all this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB1")

    Jump("loc_417F")

    label("loc_3FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_417F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E6")

    ChrTalk(    #196
        0xFE,
        (
            "Our ship was stopped in dock before it\x01",
            "could even take its first morning flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "There's some kind of severe problem,\x01",
            "so we can't take off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "None of the passengers were injured,\x01",
            "thank Aidios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "If this had happened after we took off,\x01",
            "it really would've been a crisis!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_417F")

    label("loc_40E6")


    ChrTalk(    #200
        0xFE,
        (
            "Our ship was stopped in dock before it\x01",
            "could even take its first morning flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "We still have no idea when we will\x01",
            "be able to resume service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417F")

    TalkEnd(0x25)
    Return()

    # Function_17_3E77 end

    def Function_18_4183(): pass

    label("Function_18_4183")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425B")

    ChrTalk(    #202
        0xFE,
        (
            "The goods I ordered were supposed to\x01",
            "arrive today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Who would've guessed flights would be\x01",
            "canceled? Well, that's a fork stuck in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "I'll have to find replacement stock\x01",
            "from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_42CC")

    label("loc_425B")


    ChrTalk(    #205
        0xFE,
        (
            "The goods I ordered were supposed to\x01",
            "arrive today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I'll have to find replacement stock\x01",
            "from somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42CC")

    TalkEnd(0x26)
    Return()

    # Function_18_4183 end

    def Function_19_42D0(): pass

    label("Function_19_42D0")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43CC")

    ChrTalk(    #207
        0xFE,
        "Hmm. Scheduled flights are canceled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "It's not a surprise, I suppose, with\x01",
            "orbments the way they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Still quite an issue. Shipping will be\x01",
            "impossible for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I'll have to look for a buyer locally,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_4446")

    label("loc_43CC")


    ChrTalk(    #211
        0xFE,
        (
            "If the flights aren't running,\x01",
            "then shipping is impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "My only recourse now is to look\x01",
            "for buyers locally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4446")

    TalkEnd(0x27)
    Return()

    # Function_19_42D0 end

    def Function_20_444A(): pass

    label("Function_20_444A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    OP_6D(76390, 30000, 24550, 0)
    OP_67(0, 45040, -55000, 0)
    OP_6B(900, 0)
    OP_6C(321000, 0)
    OP_6E(262, 0)
    StopSound(0xA410, 0x3D090, 0x0)
    OP_A1(0x28, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    SetChrPos(0x28, 62250, 10650, 41990, 0)
    OP_6F(0x7, 60)
    OP_A1(0x29, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0x29, 62250, 5650, 41990, 0)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 100)
    SetChrFlags(0x1A, 0x80)
    OP_22(0x79, 0x0, 0x64)
    OP_43(0x28, 0x0, 0x0, 0x16)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x0, 0x7D0)
    OP_DE("Bose")
    FadeToBright(2000, 0)
    WaitChrThread(0x28, 0x0)
    OP_48()
    Fade(1000)
    StopSound(0xA410, 0x222E0, 0x0)
    OP_6D(55790, 1500, 37990, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    OP_71(0xB, 0x4)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0x7, 411)
    OP_70(0x7, 0x1C2)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x7)
    OP_43(0xE, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xF, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_43(0x10, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_43(0x11, 0x1, 0x0, 0x15)
    Sleep(1200)
    OP_43(0x12, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0x13, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0x8, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xB, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xA, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xD, 0x1, 0x0, 0x15)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_444A end

    def Function_21_4654(): pass

    label("Function_21_4654")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 62290, 1600, 42020, 180)
    OP_8E(0xFE, 0xF352, 0x5DC, 0x93EE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xDD72, 0x5DC, 0x93EE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xC0F8, 0x5DC, 0x93EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC0F8, 0x0, 0x6018, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_21_4654 end

    def Function_22_46CF(): pass

    label("Function_22_46CF")


    def lambda_46D5():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_46D5)

    def lambda_46F0():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_46F0)
    Sleep(100)

    def lambda_4710():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4710)

    def lambda_472B():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_472B)
    Sleep(100)

    def lambda_474B():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_474B)

    def lambda_4766():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4766)
    Sleep(100)

    def lambda_4786():
        OP_6D(76390, 20000, 24550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4786)
    Sleep(100)

    def lambda_47A3():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_47A3)

    def lambda_47BE():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_47BE)
    Sleep(100)

    def lambda_47DE():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_47DE)

    def lambda_47F9():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_47F9)
    Sleep(100)

    def lambda_4819():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4819)

    def lambda_4834():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4834)
    Sleep(100)

    def lambda_4854():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4854)

    def lambda_486F():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_486F)
    Sleep(100)

    def lambda_488F():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_488F)

    def lambda_48AA():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_48AA)
    Sleep(100)

    def lambda_48CA():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_48CA)

    def lambda_48E5():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_48E5)
    Sleep(100)

    def lambda_4905():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4905)
    Sleep(3200)

    def lambda_4925():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4925)

    def lambda_4940():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4940)
    Sleep(200)

    def lambda_4960():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4960)

    def lambda_497B():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_497B)
    Sleep(200)

    def lambda_499B():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_499B)

    def lambda_49B6():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_49B6)
    Sleep(200)

    def lambda_49D6():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_49D6)

    def lambda_49F1():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_49F1)
    Sleep(200)

    def lambda_4A11():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4A11)

    def lambda_4A2C():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4A2C)
    Sleep(200)

    def lambda_4A4C():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4A4C)

    def lambda_4A67():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4A67)
    Sleep(200)

    def lambda_4A87():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4A87)

    def lambda_4AA2():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4AA2)
    Sleep(200)

    def lambda_4AC2():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4AC2)

    def lambda_4ADD():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4ADD)
    Sleep(100)

    def lambda_4AFD():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4AFD)

    def lambda_4B18():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4B18)
    Sleep(100)

    def lambda_4B38():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4B38)

    def lambda_4B53():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4B53)
    WaitChrThread(0x28, 0x1)
    WaitChrThread(0x29, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x28, 62250, -5650, 41990, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_B0(0x7, 0x3C)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x1)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_70(0xA, 0xC8)
    Sleep(2500)
    OP_44(0x101, 0x1)
    Return()

    # Function_22_46CF end

    def Function_23_4BDA(): pass

    label("Function_23_4BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BE7")
    Return()

    label("loc_4BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D2")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C14")
    Call(0, 38)
    Call(0, 39)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_4C14")

    OP_A2(0x1A1D)
    Fade(1000)
    Call(0, 34)
    OP_6D(48920, 1500, 32350, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(246000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 49200, 250, 25720, 0)
    SetChrPos(0x103, 48730, 0, 24660, 0)
    SetChrPos(0x105, 49640, 0, 24560, 0)
    SetChrPos(0x108, 48740, 0, 23580, 0)
    SetChrPos(0x104, 49910, 0, 23460, 0)

    def lambda_4CB8():
        OP_8E(0xFE, 0xC030, 0x5DC, 0x8322, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CB8)
    Sleep(300)

    def lambda_4CD8():
        OP_8E(0xFE, 0xBE5A, 0x5DC, 0x7EB7, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4CD8)
    Sleep(70)

    def lambda_4CF8():
        OP_8E(0xFE, 0xC2EC, 0x5DC, 0x7ED6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4CF8)
    Sleep(300)

    def lambda_4D18():
        OP_8E(0xFE, 0xBE64, 0x5DC, 0x7A76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4D18)
    Sleep(80)

    def lambda_4D38():
        OP_8E(0xFE, 0xC2F6, 0x5DC, 0x7A62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D38)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    StopSound(0xA410, 0x38270, 0x1770)

    def lambda_4D72():
        OP_6D(53530, 1500, 39100, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D72)

    def lambda_4D8A():
        OP_67(0, 8530, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D8A)

    def lambda_4DA2():
        OP_6B(4300, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DA2)

    def lambda_4DB2():
        OP_6E(431, 6000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4DB2)
    Sleep(1500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(1500)
    OP_8C(0x101, 45, 400)
    Sleep(3000)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x1)
    Fade(1000)
    StopSound(0xA410, 0x222E0, 0x0)
    OP_6D(48920, 1500, 32350, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(246000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #213
        0x101,
        (
            "#1015FHmmmm. Looks like the military ship\x01",
            "hasn't shown up yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F11")

    ChrTalk(    #214
        0x103,
        (
            "#020FWe should have enough time to visit the\x01",
            "merchants if we need anything.\x02\x03",

            "What do you want to do, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5008")

    label("loc_4F11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F95")

    ChrTalk(    #215
        0x108,
        (
            "#070FWe should still have some time for\x01",
            "shopping before the ship arrives.\x02\x03",

            "What do you say, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5008")

    label("loc_4F95")


    ChrTalk(    #216
        0x103,
        (
            "#020FWe should have enough time to visit the\x01",
            "merchants if we need anything.\x02\x03",

            "What do you want to do, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5008")

    OP_8C(0x101, 180, 400)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Wait For The Army Ship\x01",      # 0
            "Back To Town\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517B")

    ChrTalk(    #217
        0x101,
        (
            "#1006FLet's head back and\x01",
            "pick up a few things.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 35)
    OP_6D(50090, 0, 24550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 50090, 0, 24550, 180)
    SetChrPos(0x103, 50090, 0, 24550, 180)
    SetChrPos(0x104, 50090, 0, 24550, 180)
    SetChrPos(0x105, 50090, 0, 24550, 180)
    SetChrPos(0x108, 50090, 0, 24550, 180)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_30(0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    Jump("loc_51CF")

    label("loc_517B")


    ChrTalk(    #218
        0x101,
        (
            "#1006FLet's just go ahead and wait\x01",
            "for the ship to arrive.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 24)

    label("loc_51CF")

    Jump("loc_549B")

    label("loc_51D2")

    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_51F0"),
        (2, "loc_5230"),
        (3, "loc_526F"),
        (4, "loc_52B6"),
        (7, "loc_52FB"),
        (SWITCH_DEFAULT, "loc_5337"),
    )


    label("loc_51F0")


    ChrTalk(    #219
        0x101,
        (
            "#1015FSeems like we've still got some\x01",
            "time until ten...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5337")

    label("loc_5230")

    TurnDirection(0x103, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #220
        0x103,
        "#023FOh, are we done with everything else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5337")

    label("loc_526F")

    TurnDirection(0x104, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #221
        0x104,
        (
            "#033FAre we prepared for a dragon hunt,\x01",
            "you think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5337")

    label("loc_52B6")

    TurnDirection(0x105, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #222
        0x105,
        (
            "#040FShall we wait for the ship to arrive,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5337")

    label("loc_52FB")

    TurnDirection(0x108, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #223
        0x108,
        "#073FSure we're ready to hunt a dragon?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5337")

    label("loc_5337")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Wait For The Army Ship\x01",      # 0
            "Back To Town\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543E")
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_6D(50090, 0, 24550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 50090, 0, 24550, 180)
    SetChrPos(0x103, 50090, 0, 24550, 180)
    SetChrPos(0x104, 50090, 0, 24550, 180)
    SetChrPos(0x105, 50090, 0, 24550, 180)
    SetChrPos(0x108, 50090, 0, 24550, 180)
    OP_0D()
    Jump("loc_549B")

    label("loc_543E")

    FadeToBright(300, 0)

    ChrTalk(    #224
        0x101,
        (
            "#1006FLet's just go ahead and wait\x01",
            "for the ship to arrive.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 24)

    label("loc_549B")

    EventEnd(0x0)
    Return()

    # Function_23_4BDA end

    def Function_24_549E(): pass

    label("Function_24_549E")

    EventBegin(0x0)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_6D(50030, 1500, 34090, 0)
    OP_67(0, 6950, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(107000, 0)
    OP_6E(282, 0)
    SetChrPos(0x101, 51300, 1500, 34000, 270)
    SetChrPos(0x8, 50450, 1500, 32850, 315)
    SetChrPos(0xA, 50510, 1500, 35270, 225)
    SetChrPos(0x9, 48710, 1500, 33730, 45)
    SetChrPos(0xD, 48780, 1500, 35090, 135)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #225
        0x101,
        (
            "#1011F#6PSo the airship that's gonna pick us up is\x01",
            "gonna be one of those big, reinforced army\x01",
            "ones, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xA,
        (
            "#040FYes, one of our guard airships.\x02\x03",

            "They make up most of our military ships,\x01",
            "so I'd imagine that's what we'll be on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x8,
        (
            "#026FMmm. The typical Royal Army guard airship is\x01",
            "usually well rounded--strong firepower, a large\x01",
            "load capacity and good mobility...\x02\x03",

            "#020FThough that's what I know from ten years ago.\x01",
            "They've been upgraded some since their initial\x01",
            "deployment, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xA,
        (
            "#047FYes, in addition to giving them better armor and\x01",
            "engines and such, we have specialized the ships\x01",
            "by varying their equipment.\x02\x03",

            "#040FPatrol craft, scout craft, attack craft...\x02\x03",

            "The principle--at least as I understand it--\x01",
            "is to ensure the squadrons are flexible by\x01",
            "giving each one mission-specific equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xD,
        (
            "#070F#6PJust what I'd expect from the country that\x01",
            "invented airship warfare.\x02\x03",

            "#075FWe have airship 'squadrons' in Calvard,\x01",
            "but they're nothing more than showboats,\x01",
            "really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x9,
        (
            "#035FHeh. The Empire is little different.\x02\x03",

            "#030FWe use airship squadrons, but the Empire's\x01",
            "strength has always lain in its cavalry\x01",
            "divisions--our tanks, in this age.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    OP_20(0xBB8)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #231
        (
            "\x07\x05Attention please, a Royal Army vessel will be\x01",
            "landing at Port 1 momentarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #232
        (
            "\x07\x05All non-affiliated personnel, please refrain from\x01",
            "entering Port 1.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #233
        0x101,
        "#1006FHey, here we go!\x02",
    )

    CloseMessageWindow()
    OP_22(0x125, 0x1, 0x14)
    Sleep(400)
    OP_24(0x125, 0x1E)
    Sleep(400)
    OP_24(0x125, 0x28)
    Sleep(400)
    OP_24(0x125, 0x32)
    Sleep(400)
    OP_24(0x125, 0x3C)
    Sleep(400)
    OP_24(0x125, 0x46)
    Sleep(400)
    OP_24(0x125, 0x50)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x101,
        (
            "#1015FEr, huh?\x02\x03",

            "I don't think I've heard this engine sound before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xA,
        "#044FOh, my... That's...\x02",
    )

    CloseMessageWindow()

    def lambda_5BB2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BB2)
    Sleep(100)

    def lambda_5BC5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5BC5)
    Sleep(100)

    def lambda_5BD8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5BD8)
    Sleep(100)

    def lambda_5BEB():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5BEB)
    Sleep(100)
    OP_8C(0xD, 45, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #236
        0x101,
        "#1004F#4PAh!\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x100000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_549E end

    def Function_25_5C3F(): pass

    label("Function_25_5C3F")

    EventBegin(0x0)
    OP_DB()
    ClearMapFlags(0x100000)
    OP_6D(76390, 30000, 28060, 0)
    OP_67(0, 45040, -55000, 0)
    OP_6B(900, 0)
    OP_6C(321000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 51120, 1800, 37530, 90)
    SetChrPos(0x8, 49540, 1500, 37920, 90)
    SetChrPos(0x9, 49180, 1500, 36690, 90)
    SetChrPos(0xA, 50880, 1800, 38460, 90)
    SetChrPos(0xD, 49140, 1500, 38860, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_E5(0x8, 0x0, 0x0)
    OP_E5(0xA, 0x0, 0x0)
    OP_E5(0xD, 0x0, 0x0)
    OP_E5(0x9, 0x0, 0x0)
    StopSound(0xA410, 0x3D090, 0x0)
    OP_A1(0x28, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 251)
    SetChrPos(0x28, 62500, 17500, 44000, 0)
    OP_A1(0x29, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0x29, 62500, -2000, 44000, 0)
    OP_75(0x8, 0x0, 0x0)
    OP_74(0x8, 0x0, 0x0)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 100)
    OP_71(0xB, 0x4)
    FadeToBright(1000, 0)
    Call(0, 33)
    Fade(500)
    OP_6D(51270, 1800, 38190, 0)
    OP_67(0, 9040, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    StopSound(0xA410, 0x222E0, 0x0)
    OP_E5(0x8, 0x0, 0x1)
    OP_E5(0xA, 0x0, 0x1)
    OP_E5(0xD, 0x0, 0x1)
    OP_E5(0x9, 0x0, 0x1)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_70(0xA, 0xC8)
    Sleep(2500)
    OP_DC()

    ChrTalk(    #237
        0x101,
        (
            "#1008F#6PAh-hahahahaha...\x02\x03",

            "Sooooo...we're gonna be riding the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xA,
        (
            "#044F#6PJulia didn't mention this at all when\x01",
            "I spoke with her last night...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 62300, 1500, 38740, 270)
    SetChrPos(0x15, 62370, 1500, 40090, 270)
    SetChrChipByIndex(0x15, 17)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0x7, 1888)
    OP_70(0x7, 0x758)
    OP_73(0x7)
    Sleep(500)

    NpcTalk(    #239
        0x14,
        "Man's Voice",
        "#3PYo, Estelle!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #240
        0x15,
        "Girl's Voice",
        "#3PHiiiii, everybody! Long time no see!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5FF9():
        OP_6D(55520, 1500, 39550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5FF9)

    def lambda_6011():
        OP_67(0, 5390, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6011)

    def lambda_6029():
        OP_6B(4040, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6029)

    def lambda_6039():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_6039)

    def lambda_6049():
        OP_6E(236, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6049)

    def lambda_6059():

        label("loc_6059")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_6059")

    QueueWorkItem2(0x101, 1, lambda_6059)

    def lambda_606A():

        label("loc_606A")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_606A")

    QueueWorkItem2(0x8, 1, lambda_606A)

    def lambda_607B():

        label("loc_607B")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_607B")

    QueueWorkItem2(0x9, 1, lambda_607B)

    def lambda_608C():

        label("loc_608C")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_608C")

    QueueWorkItem2(0xA, 1, lambda_608C)

    def lambda_609D():

        label("loc_609D")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_609D")

    QueueWorkItem2(0xD, 1, lambda_609D)

    def lambda_60AE():
        OP_8E(0xFE, 0xE68C, 0x5DC, 0x97C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_60AE)
    Sleep(500)

    def lambda_60CE():
        OP_8E(0xFE, 0xE77C, 0x5DC, 0x9C04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_60CE)
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x101, 400)
    WaitChrThread(0x15, 0x1)
    TurnDirection(0x15, 0x101, 400)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)

    ChrTalk(    #241
        0x101,
        "#1020F#5PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x8,
        "#023F#5PIs that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x14,
        (
            "#141F#4PHeheh. We seem to have a habit of meeting\x01",
            "in the strangest damn places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x15,
        (
            "#151F#4PEsteeelle! Everyone!\x01",
            "It's so great to see you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        (
            "#1004F#5PWh-Wh-Wh...\x02\x03",

            "Why are Nial and Dorothy on the Arseille?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x16, 62600, 1500, 42300, 180)
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x4)
    ClearChrFlags(0x16, 0x80)
    Sleep(500)

    NpcTalk(    #246
        0x16,
        "Woman's Voice",
        "#7PAllow me to explain.\x02",
    )

    CloseMessageWindow()

    def lambda_6287():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6287)

    def lambda_6295():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6295)

    def lambda_62A3():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_62A3)

    def lambda_62B1():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_62B1)

    def lambda_62BF():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_62BF)

    def lambda_62CD():

        label("loc_62CD")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_62CD")

    QueueWorkItem2(0x101, 1, lambda_62CD)

    def lambda_62DE():

        label("loc_62DE")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_62DE")

    QueueWorkItem2(0xA, 1, lambda_62DE)

    def lambda_62EF():

        label("loc_62EF")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_62EF")

    QueueWorkItem2(0xD, 1, lambda_62EF)

    def lambda_6300():

        label("loc_6300")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_6300")

    QueueWorkItem2(0x14, 1, lambda_6300)

    def lambda_6311():

        label("loc_6311")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_6311")

    QueueWorkItem2(0x15, 1, lambda_6311)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    OP_8E(0x16, 0xF488, 0x5DC, 0x9AE2, 0x7D0, 0x0)
    OP_8E(0x16, 0xE86C, 0x5DC, 0x93EE, 0x7D0, 0x0)
    OP_8E(0x16, 0xE100, 0x5DC, 0x93EE, 0x7D0, 0x0)
    TurnDirection(0x16, 0x101, 400)
    OP_44(0x101, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)

    def lambda_6383():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6383)
    Sleep(100)

    def lambda_6396():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6396)

    ChrTalk(    #247
        0x101,
        "#1004F#5PJulia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xA,
        (
            "#542F#5PJulia...you awful tease!\x02\x03",

            "Why didn't you tell me last night that\x01",
            "you'd be coming in the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x16,
        (
            "#171F#4PHaha. I get to have my fun with surprises\x01",
            "SOMETIMES, my princess.\x02\x03",

            "My apologies if I startled you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        (
            "#045F#5POhhh, Julia.\x02\x03",

            "#048FI take it that, if you're using the Arseille,\x01",
            "it's part of Grandmother's plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x16,
        "#170F#4PJust so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        "#1008F#5PEr. What's Her Majesty got to do with this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x16,
        (
            "#176F#4PIf the famous, cutting-edge Arseille gets\x01",
            "involved, those living in fear of the dragon\x01",
            "may have their concerns eased...\x02\x03",

            "#170FI believe that is her thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#1006F#5POh, good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x9,
        (
            "#031F#5PAh, Queen Alicia continues to impress!\x02\x03",

            "#030FThe reporters are, I assume,\x01",
            "along for the very same reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x14,
        (
            "#141F#4PYeah, pretty much.\x02\x03",

            "The whole damn country's losing it\x01",
            "over this dragon thing.\x02\x03",

            "Looks like they're hoping us humble\x01",
            "reporters can produce a little something\x01",
            "to calm the masses.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x14, 400)

    ChrTalk(    #257
        0x16,
        "#178F#6PMr. Burns, remember...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x16, 400)
    Sleep(500)

    ChrTalk(    #258
        0x14,
        (
            "#147F#4PI know, I know.\x01",
            "I won't give away any state secrets.\x02\x03",

            "#140FI AM gonna be pokin' my head around to some\x01",
            "extent, though. I ain't writin' straight\x01",
            "propaganda, here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x16,
        "#176F#6P...As you wish.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x17, 62600, 1500, 42300, 180)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x80)

    NpcTalk(    #260
        0x17,
        "Older Man's Voice",
        "#7PHmph. On time for once, I see.\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_696B():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_696B)

    def lambda_6979():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6979)

    def lambda_6987():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6987)

    def lambda_6995():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6995)

    def lambda_69A3():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_69A3)

    def lambda_69B1():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_69B1)

    def lambda_69BF():

        label("loc_69BF")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_69BF")

    QueueWorkItem2(0x101, 1, lambda_69BF)

    def lambda_69D0():

        label("loc_69D0")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_69D0")

    QueueWorkItem2(0xA, 1, lambda_69D0)

    def lambda_69E1():

        label("loc_69E1")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_69E1")

    QueueWorkItem2(0xD, 1, lambda_69E1)

    def lambda_69F2():

        label("loc_69F2")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_69F2")

    QueueWorkItem2(0x14, 1, lambda_69F2)

    def lambda_6A03():

        label("loc_6A03")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_6A03")

    QueueWorkItem2(0x15, 1, lambda_6A03)

    def lambda_6A14():

        label("loc_6A14")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_6A14")

    QueueWorkItem2(0x16, 1, lambda_6A14)
    OP_43(0x17, 0x0, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x16, 0x0, 0x0, 0x1C)
    WaitChrThread(0x17, 0x0)
    OP_44(0xA, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)

    def lambda_6A4D():
        OP_8C(0x14, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6A4D)

    def lambda_6A5B():
        OP_8C(0x15, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6A5B)

    def lambda_6A69():
        OP_8C(0x16, 270, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6A69)

    ChrTalk(    #261
        0x101,
        "#1004F#5PGeneral Morgan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x8,
        (
            "#027F#5PGeneral, allow me to express our thanks\x01",
            "for allowing us aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x17,
        (
            "#163F#4PWell, Her Majesty's opinion helped.\x02\x03",

            "#160FLet me be clear on this upfront so there's no\x01",
            "misunderstanding. You bracers are nothing\x01",
            "more than observers on this mission.\x02\x03",

            "All you'll be allowed to do is watch as\x01",
            "we execute the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#1006F#5PI'm fine with that.\x02\x03",

            "If the army can settle things,\x01",
            "I sure won't complain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xD,
        (
            "#071F#5PI look forward to seeing what\x01",
            "you can do, General.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x17,
        (
            "#163F#4PHmph. Very well.\x02\x03",

            "#160FYour Highness, please, this way.\x01",
            "We shall accompany you to the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xA,
        "#043F#5PBut--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x17,
        (
            "#160F#4PWe cannot allow the princess to board as a\x01",
            "mere passenger on her own airship.\x02\x03",

            "It would affect the crew's morale,\x01",
            "Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xA,
        "#047F#5P...Very well.\x02",
    )

    CloseMessageWindow()
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xA, 0x0, 0x0, 0x1D)
    Sleep(1000)

    def lambda_6DB7():
        OP_6D(56780, 1800, 39570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DB7)
    OP_43(0x17, 0x0, 0x0, 0x1E)

    def lambda_6DD6():

        label("loc_6DD6")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_6DD6")

    QueueWorkItem2(0x14, 1, lambda_6DD6)

    def lambda_6DE7():

        label("loc_6DE7")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_6DE7")

    QueueWorkItem2(0x15, 1, lambda_6DE7)

    def lambda_6DF8():

        label("loc_6DF8")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_6DF8")

    QueueWorkItem2(0x16, 1, lambda_6DF8)
    Sleep(5000)

    ChrTalk(    #270
        0x101,
        (
            "#1007F#5PWell, he's as icy as always.\x02\x03",

            "#1019FI wish he'd just accept that us 'dumb civvy\x01",
            "bracers' are, you know, something\x01",
            "approaching competent.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)
    OP_8C(0x16, 270, 400)
    Sleep(500)

    ChrTalk(    #271
        0x16,
        (
            "#171F#4PHaha. The general is a hardheaded,\x01",
            "old-school sort of man. I doubt he'll\x01",
            "ever change his opinions quickly.\x02\x03",

            "Allow me to lead you aboard the ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 315, 400)

    def lambda_6F6B():
        OP_6D(55700, 1500, 38800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F6B)

    def lambda_6F83():
        OP_6B(3800, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6F83)

    def lambda_6F93():
        OP_8E(0xFE, 0xE100, 0x5DC, 0x93EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6F93)
    Sleep(100)

    def lambda_6FB3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6FB3)
    Sleep(100)

    def lambda_6FC6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6FC6)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 270, 400)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x16, 18)
    Sleep(100)
    OP_99(0x16, 0x0, 0x1, 0x5DC)
    Sleep(500)

    ChrTalk(    #272
        0x16,
        (
            "#178F#4PAnd on that note. Allow me to finally\x01",
            "welcome you properly, as allies and\x01",
            "friends of long standing!\x02\x03",

            "Welcome aboard the Arseille, flagship\x01",
            "of the Royal Guard and Liberl!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_DB()
    OP_22(0x75, 0x0, 0x64)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_6F(0x7, 1)
    OP_6D(61820, 6050, 54410, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(542, 0)
    FadeToBright(1500, 0)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 200)
    OP_70(0xA, 0x64)
    Sleep(2500)
    OP_23(0x75)
    OP_22(0x125, 0x0, 0x64)
    OP_43(0x28, 0x0, 0x0, 0x1A)
    Sleep(3000)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x28, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x190, 0x0, 0x190, 0x0)

    def lambda_71DE():
        OP_6D(59670, 1800, 67060, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71DE)

    def lambda_71F6():
        OP_67(0, 8260, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_71F6)

    def lambda_720E():
        OP_6B(3830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_720E)

    def lambda_721E():
        OP_6C(204000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_721E)

    def lambda_722E():
        OP_6E(593, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_722E)

    def lambda_723E():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_723E)

    def lambda_7254():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7254)
    Sleep(400)

    def lambda_726F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_726F)

    def lambda_7285():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7285)
    Sleep(400)

    def lambda_72A0():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_72A0)

    def lambda_72B6():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_72B6)
    Sleep(400)

    def lambda_72D1():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_72D1)

    def lambda_72E7():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_72E7)
    Sleep(300)

    def lambda_7302():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7302)

    def lambda_7318():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7318)
    Sleep(300)

    def lambda_7333():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7333)

    def lambda_7349():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7349)
    Sleep(300)

    def lambda_7364():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7364)

    def lambda_737A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_737A)
    Sleep(300)

    def lambda_7395():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7395)

    def lambda_73AB():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_73AB)
    Sleep(200)

    def lambda_73C6():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_73C6)

    def lambda_73DC():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_73DC)
    Sleep(200)

    def lambda_73F7():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_73F7)

    def lambda_740D():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_740D)
    Sleep(200)

    def lambda_7428():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7428)

    def lambda_743E():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_743E)
    Sleep(200)

    def lambda_7459():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7459)

    def lambda_746F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_746F)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x125)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(49170, 1500, 37540, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 49530, 1500, 28520, 0)
    SetChrPos(0xC, 48750, 1500, 28520, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_0D()
    OP_DC()

    NpcTalk(    #273
        0xB,
        "Young Man's Voice",
        "#3PDamn, too late!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0xB, 25)

    def lambda_7594():
        OP_8E(0xFE, 0xC17A, 0x5DC, 0x9344, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7594)
    Sleep(500)
    SetChrChipByIndex(0xC, 26)

    def lambda_75B9():
        OP_8E(0xC, 0xBE6E, 0x5DC, 0x925E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_75B9)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)

    ChrTalk(    #274
        0xC,
        "#065FThey're gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xB,
        (
            "#551F#6PWe shoulda headed out a bit earlier...\x02\x03",

            "#051FAh, well. We'll leave the dragon-watching\x01",
            "to the rest of the gang.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #276
        0xC,
        (
            "#560F#4PY-Yeah.\x02\x03",

            "#562FBut, but... Awwwww.\x02\x03",

            "I wanted to ride the Arseille...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #277
        0xB,
        (
            "#051F#6PC'mon, shortstuff. There's more to life\x01",
            "than gawkin' at machines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xC,
        (
            "#560F#4PAww, but, there's so much to see!\x02\x03",

            "An engine room with eight of the new\x01",
            "model engines...\x02\x03",

            "A next generation bridge with all the best\x01",
            "information-processing equipment...\x02\x03",

            "#067FIt'd be a dreeeeam...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xB,
        "#551F#6PFor the... Your eyes're lit up like candles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        (
            "#067F#4PHeehee...\x02\x03",

            "#064FBut still, Agate. What do we do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xB,
        (
            "#053F#6PGood question...\x02\x03",

            "#051FWell, first off, I'm gonna need a new greatsword\x01",
            "if I want to keep bein' the Heavy Blade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "#063F#4POh, right.\x02\x03",

            "Yeah, I guess you can't really repair\x01",
            "a sword that gets broken that badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xB,
        (
            "#053F#6PYeah, gonna have to buy a new one.\x02\x03",

            "#552FLet's go order one at the weapon store\x01",
            "in the South Block.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, 49650, 1500, 28520, 0)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x18, 255)

    NpcTalk(    #284
        0x18,
        "Young Man's Voice",
        "#3PAgate!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7A46():
        OP_6D(49650, 1500, 35920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A46)

    def lambda_7A5E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7A5E)
    Sleep(50)

    def lambda_7A71():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7A71)
    OP_8E(0x18, 0xC094, 0x5DC, 0x8A3E, 0xFA0, 0x0)

    ChrTalk(    #285
        0xB,
        "#052F#5PYo, Ted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xC,
        (
            "#064FYou're the receptionist here,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x18,
        (
            "#4PAh, looks like you didn't make it\x01",
            "in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x18,
        (
            "#4PI can try to raise the Arseille\x01",
            "on the radio if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xB,
        (
            "#053F#5PNah, that's okay.\x02\x03",

            "#051FSo you came out here just to see\x01",
            "if I'd caught the flight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x18,
        "#4PThat too, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x18,
        (
            "#4PWe actually just got a rush delivery on the\x01",
            "flight last night, with your name on it.\x01",
            "I just found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xB,
        "#052F#5PA rush delivery for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x18,
        (
            "#4PYeah, a small package.\x01",
            "Return address says 'Russell'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xB,
        "#055F#5PWh--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xC,
        "#065FF-From Grandpa?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_5C3F end

    def Function_26_7CE3(): pass

    label("Function_26_7CE3")

    OP_22(0x77, 0x0, 0x64)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x96)
    OP_73(0x7)
    OP_6F(0x7, 151)
    OP_70(0x7, 0x14A)
    Sleep(3300)
    OP_75(0x8, 0x0, 0x2)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x8, 0x0, 0x1)
    Sleep(250)
    OP_74(0x8, 0x0, 0x2)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x8, 0x0, 0x3)
    Sleep(250)
    OP_74(0x8, 0x0, 0x4)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x8, 0x0, 0x5)
    Sleep(250)
    OP_74(0x8, 0x0, 0x6)
    Sleep(250)
    OP_74(0x8, 0x0, 0x7)
    OP_73(0x7)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 330)
    OP_70(0x7, 0x1AE)
    Return()

    # Function_26_7CE3 end

    def Function_27_7D96(): pass

    label("Function_27_7D96")

    OP_8E(0xFE, 0xF488, 0x5DC, 0x9CA4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE916, 0x5DC, 0x94CA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE006, 0x5DC, 0x93BC, 0x7D0, 0x0)
    Return()

    # Function_27_7D96 end

    def Function_28_7DD3(): pass

    label("Function_28_7DD3")

    OP_8E(0xFE, 0xE682, 0x5DC, 0x9416, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE718, 0x5DC, 0x9092, 0x7D0, 0x0)
    Return()

    # Function_28_7DD3 end

    def Function_29_7DFC(): pass

    label("Function_29_7DFC")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xD21E, 0x5DC, 0x9434, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE9C0, 0x5DC, 0x9498, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF28A, 0x5DC, 0x9C7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF32A, 0x5DC, 0xA348, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_7DFC end

    def Function_30_7E57(): pass

    label("Function_30_7E57")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xE9C0, 0x5DC, 0x9498, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF28A, 0x5DC, 0x9C7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF32A, 0x5DC, 0xA348, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_7E57 end

    def Function_31_7EA0(): pass

    label("Function_31_7EA0")

    OP_72(0x7, 0x20)
    OP_73(0x7)
    OP_6F(0x7, 600)
    OP_70(0x7, 0x32A)
    Return()

    # Function_31_7EA0 end

    def Function_32_7EB7(): pass

    label("Function_32_7EB7")

    OP_43(0x101, 0x3, 0x0, 0x1F)
    OP_22(0x79, 0x0, 0x64)

    def lambda_7EC9():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7EC9)

    def lambda_7EE4():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7EE4)
    Sleep(100)

    def lambda_7F04():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7F04)
    Sleep(100)

    def lambda_7F24():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7F24)
    Sleep(100)

    def lambda_7F44():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7F44)

    def lambda_7F5F():
        OP_6D(76390, 20000, 24550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F5F)
    Sleep(100)

    def lambda_7F7C():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7F7C)
    Sleep(100)

    def lambda_7F9C():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7F9C)
    Sleep(100)

    def lambda_7FBC():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7FBC)
    Sleep(100)

    def lambda_7FDC():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7FDC)
    Sleep(100)

    def lambda_7FFC():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7FFC)
    Sleep(100)

    def lambda_801C():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_801C)
    Sleep(100)

    def lambda_803C():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_803C)
    Sleep(100)

    def lambda_805C():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_805C)

    def lambda_8077():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8077)
    Sleep(3500)

    def lambda_8097():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8097)
    Sleep(100)

    def lambda_80B7():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_80B7)
    Sleep(100)

    def lambda_80D7():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_80D7)
    Sleep(100)

    def lambda_80F7():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_80F7)
    Sleep(100)

    def lambda_8117():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8117)
    Sleep(100)

    def lambda_8137():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8137)
    Sleep(100)

    def lambda_8157():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8157)
    Sleep(100)

    def lambda_8177():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8177)
    Sleep(100)

    def lambda_8197():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8197)
    Sleep(100)

    def lambda_81B7():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_81B7)
    WaitChrThread(0x28, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x28, 62500, 0, 44000, 0)
    OP_44(0x101, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Return()

    # Function_32_7EB7 end

    def Function_33_820A(): pass

    label("Function_33_820A")

    OP_43(0x101, 0x3, 0x0, 0x1F)
    OP_22(0x125, 0x0, 0x64)

    def lambda_821C():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_821C)

    def lambda_8237():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8237)
    Sleep(100)

    def lambda_8257():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8257)
    Sleep(100)

    def lambda_8277():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8277)
    Sleep(100)

    def lambda_8297():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8297)

    def lambda_82B2():
        OP_6D(76390, 20000, 24550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_82B2)
    Sleep(100)

    def lambda_82CF():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_82CF)
    Sleep(100)

    def lambda_82EF():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_82EF)
    Sleep(100)

    def lambda_830F():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_830F)
    Sleep(100)

    def lambda_832F():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_832F)
    Sleep(100)

    def lambda_834F():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_834F)
    Sleep(100)

    def lambda_836F():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_836F)
    Sleep(100)

    def lambda_838F():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_838F)
    Sleep(100)

    def lambda_83AF():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_83AF)

    def lambda_83CA():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_83CA)
    Sleep(3500)

    def lambda_83EA():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_83EA)
    Sleep(100)

    def lambda_840A():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_840A)
    Sleep(100)

    def lambda_842A():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_842A)
    Sleep(100)

    def lambda_844A():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_844A)
    Sleep(100)

    def lambda_846A():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_846A)
    Sleep(100)

    def lambda_848A():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_848A)
    Sleep(100)

    def lambda_84AA():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_84AA)
    Sleep(100)

    def lambda_84CA():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_84CA)
    Sleep(100)

    def lambda_84EA():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_84EA)
    Sleep(100)

    def lambda_850A():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_850A)
    WaitChrThread(0x28, 0x1)
    OP_23(0x125)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x28, 62500, 0, 44000, 0)
    OP_44(0x101, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Return()

    # Function_33_820A end

    def Function_34_855D(): pass

    label("Function_34_855D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85A3")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xF9, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_85A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85FD")
    RemoveParty(0x3, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E5")
    AddParty(0x3, 0xF9, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_85FD")

    label("loc_85E5")

    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_85FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8657")
    RemoveParty(0x4, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_863F")
    AddParty(0x4, 0xF9, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_8657")

    label("loc_863F")

    AddParty(0x4, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_8657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8689")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_8689")

    Return()

    # Function_34_855D end

    def Function_35_868A(): pass

    label("Function_35_868A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_869E")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_869E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_86B2")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)

    label("loc_86B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_86C6")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_86C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_86DA")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)

    label("loc_86DA")

    Return()

    # Function_35_868A end

    def Function_36_86DB(): pass

    label("Function_36_86DB")

    EventBegin(0x0)
    OP_DB()
    OP_6D(66690, 9370, 39660, 0)
    OP_67(0, 45340, -55000, 0)
    OP_6B(900, 0)
    OP_6C(316000, 0)
    OP_6E(403, 0)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_6F(0x7, 1)
    OP_75(0x8, 0x0, 0x0)
    OP_74(0x8, 0x0, 0x0)
    SetChrFlags(0x1A, 0x80)
    FadeToBright(2000, 0)

    def lambda_875A():
        OP_6D(66900, 7780, 39660, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_875A)

    def lambda_8772():
        OP_67(0, 34090, -55000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8772)
    Sleep(1000)

    def lambda_878F():
        OP_6B(700, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_878F)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_36_86DB end

    def Function_37_87C6(): pass

    label("Function_37_87C6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87DD")
    Call(0, 38)
    AddParty(0x2, 0xF8, 0xFF)

    label("loc_87DD")

    OP_6D(55720, 1500, 38000, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(122000, 0)
    OP_6E(236, 0)
    OP_A1(0x28, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    SetChrPos(0x28, 62500, 0, 44000, 0)
    OP_6F(0x7, 1)
    OP_A1(0x29, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0x29, 62500, -5100, 44000, 0)
    OP_75(0x8, 0x0, 0x0)
    OP_74(0x8, 0x0, 0x0)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 200)
    OP_71(0xB, 0x4)
    SetChrPos(0x101, 51260, 1800, 37530, 90)
    SetChrPos(0xB, 49290, 1500, 39050, 90)
    SetChrPos(0xC, 49650, 1500, 40020, 135)
    SetChrPos(0x108, 49230, 1500, 36580, 90)
    SetChrPos(0x105, 51230, 1800, 38480, 90)
    SetChrPos(0x103, 49640, 1500, 38070, 90)
    SetChrPos(0x104, 48700, 1500, 37550, 90)
    SetChrPos(0x17, 59050, 1500, 38120, 270)
    SetChrPos(0x16, 59700, 1500, 38870, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x16, 0x4)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 19)
    SetChrSubChip(0x105, 1)
    SetChrFlags(0x1A, 0x80)
    OP_22(0x75, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #296
        0x16,
        (
            "#176FThe Arseille will patrol in Bose airspace\x01",
            "while you search.\x02\x03",

            "#170FOnce you've discovered the dragon's\x01",
            "location, please contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        "#1006FRoger! Leave it to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x105,
        (
            "#048F#2PI'll have Sieg carry a message once we\x01",
            "find it.\x02\x03",

            "If I'm not with them,\x01",
            "I'll ask him to stay near Estelle.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #299
        0x105,
        "Sieg",
        "#311F#5PScreee. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x17,
        (
            "#163FYour Highness, if you do accompany them,\x01",
            "please take the greatest care.\x02\x03",

            "#160FEstelle Bright. Agate Crosner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xB,
        "#052F#2P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x17,
        (
            "#163FIf the dragon escapes the valley, the army\x01",
            "will move to contain it with everything\x01",
            "we have.\x02\x03",

            "We will not allow the people of Liberl\x01",
            "to come to harm again.\x02\x03",

            "#160FSo...do everything you can. Don't worry\x01",
            "about protecting others. Focus on your\x01",
            "mission and leave the rest to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1025FGeneral...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xB,
        (
            "#051F#2PSo, basically, 'I got your back'?\x01",
            "Never thought I'd hear that from you,\x01",
            "General.\x02\x03",

            "What brought that out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x17,
        "#163FNothing but politeness, Mr. Crosner.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 0, 400)
    Sleep(500)

    ChrTalk(    #307
        0x17,
        "#160F#4PCaptain. Get us in the air.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x16,
        "#171FSir!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_DB()
    Fade(1000)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    def lambda_8D9B():

        label("loc_8D9B")

        TurnDirection(0x101, 0x28, 400)
        OP_48()
        Jump("loc_8D9B")

    QueueWorkItem2(0x103, 2, lambda_8D9B)

    def lambda_8DAC():

        label("loc_8DAC")

        TurnDirection(0x103, 0x28, 400)
        OP_48()
        Jump("loc_8DAC")

    QueueWorkItem2(0x103, 3, lambda_8DAC)

    def lambda_8DBD():

        label("loc_8DBD")

        TurnDirection(0x105, 0x28, 400)
        OP_48()
        Jump("loc_8DBD")

    QueueWorkItem2(0x105, 3, lambda_8DBD)

    def lambda_8DCE():

        label("loc_8DCE")

        TurnDirection(0x108, 0x28, 400)
        OP_48()
        Jump("loc_8DCE")

    QueueWorkItem2(0x108, 3, lambda_8DCE)

    def lambda_8DDF():

        label("loc_8DDF")

        TurnDirection(0x104, 0x28, 400)
        OP_48()
        Jump("loc_8DDF")

    QueueWorkItem2(0x104, 3, lambda_8DDF)

    def lambda_8DF0():

        label("loc_8DF0")

        TurnDirection(0xB, 0x28, 400)
        OP_48()
        Jump("loc_8DF0")

    QueueWorkItem2(0xB, 3, lambda_8DF0)

    def lambda_8E01():

        label("loc_8E01")

        TurnDirection(0xC, 0x28, 400)
        OP_48()
        Jump("loc_8E01")

    QueueWorkItem2(0xC, 3, lambda_8E01)
    OP_6D(61820, 6050, 54410, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(542, 0)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 200)
    OP_70(0xA, 0x64)
    Sleep(2500)
    OP_23(0x75)
    OP_22(0x125, 0x0, 0x64)
    OP_43(0x28, 0x0, 0x0, 0x1A)
    Sleep(3000)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x28, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x190, 0x0, 0x190, 0x0)

    def lambda_8EE0():
        OP_6D(59670, 1800, 67060, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EE0)

    def lambda_8EF8():
        OP_67(0, 8260, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8EF8)

    def lambda_8F10():
        OP_6B(3830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8F10)

    def lambda_8F20():
        OP_6C(204000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F20)

    def lambda_8F30():
        OP_6E(593, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8F30)

    def lambda_8F40():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8F40)

    def lambda_8F56():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8F56)
    Sleep(400)

    def lambda_8F71():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8F71)

    def lambda_8F87():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8F87)
    Sleep(400)

    def lambda_8FA2():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8FA2)

    def lambda_8FB8():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8FB8)
    Sleep(400)

    def lambda_8FD3():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8FD3)

    def lambda_8FE9():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8FE9)
    Sleep(300)

    def lambda_9004():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_9004)

    def lambda_901A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_901A)
    Sleep(300)

    def lambda_9035():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_9035)

    def lambda_904B():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_904B)
    Sleep(300)

    def lambda_9066():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_9066)

    def lambda_907C():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_907C)
    Sleep(300)

    def lambda_9097():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_9097)

    def lambda_90AD():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_90AD)
    Sleep(200)

    def lambda_90C8():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_90C8)

    def lambda_90DE():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_90DE)
    Sleep(200)

    def lambda_90F9():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_90F9)

    def lambda_910F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_910F)
    Sleep(200)

    def lambda_912A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_912A)

    def lambda_9140():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9140)
    Sleep(200)

    def lambda_915B():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_915B)

    def lambda_9171():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9171)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x125)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x103, 0x2)
    OP_44(0x103, 0x3)
    OP_44(0x105, 0x3)
    OP_44(0x108, 0x3)
    OP_44(0x104, 0x3)
    OP_44(0xB, 0x3)
    OP_44(0xC, 0x3)
    SetChrName("")

    AnonymousTalk(    #309
        (
            "\x07\x05Please form your party.\x01",
            "You may choose one other member aside from the\x01",
            "mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x1A24)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1103   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_37_87C6 end

    def Function_38_9311(): pass

    label("Function_38_9311")

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
        (0, "loc_938A"),
        (1, "loc_9390"),
        (SWITCH_DEFAULT, "loc_9396"),
    )


    label("loc_938A")

    OP_A2(0x1200)
    Jump("loc_9396")

    label("loc_9390")

    OP_A2(0x1201)
    Jump("loc_9396")

    label("loc_9396")

    Return()

    # Function_38_9311 end

    def Function_39_9397(): pass

    label("Function_39_9397")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9447")
    AddParty(0x2, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_9447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9494")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_947C")
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9494")

    label("loc_947C")

    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_9494")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_94E1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C9")
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_94E1")

    label("loc_94C9")

    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_94E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9506")
    AddParty(0x7, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_9506")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_39_9397 end

    def Function_40_9518(): pass

    label("Function_40_9518")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #310
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Ruan\x01",
            "⇒ To Erebonia\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_9518 end

    def Function_41_9582(): pass

    label("Function_41_9582")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #311
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_9582 end

    def Function_42_9601(): pass

    label("Function_42_9601")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #312
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_42_9601 end

    def Function_43_968F(): pass

    label("Function_43_968F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_969C")
    Return()

    label("loc_969C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96AE")
    Return()

    label("loc_96AE")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x18)"), scpexpr(EXPR_END)), "loc_96E9")
    Call(0, 44)
    Jump("loc_97C0")

    label("loc_96E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_96F8")
    Call(0, 44)
    Jump("loc_97C0")

    label("loc_96F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_976A")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #313
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_97C0")

    label("loc_976A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #314
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_97C0")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_43_968F end

    def Function_44_97C7(): pass

    label("Function_44_97C7")

    TalkBegin(0x18)

    ChrTalk(    #315
        0x18,
        (
            "Hmm. Sorry, gang, I don't recognize\x01",
            "the girl in that picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x18,
        (
            "She's definitely not someone who works\x01",
            "here at the port, and I don't recognize\x01",
            "her as a passenger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x18,
        (
            "Maybe she, like--hell, I dunno--got adopted\x01",
            "by someone and lives all rich and happy?\x01",
            "That'd be the storybook ending!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_44_97C7 end

    SaveToFile()

Try(main)
