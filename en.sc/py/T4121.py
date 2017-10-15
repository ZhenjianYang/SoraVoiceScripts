from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4121_1 ._SN',
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
        'Elnan',                                # 9
        'Scherazard',                           # 10
        'Agate',                                # 11
        'Olivier',                              # 12
        'Kloe',                                 # 13
        'Tita',                                 # 14
        'Zin',                                  # 15
        'Lt. Col. Cid',                         # 16
        'Anelace',                              # 17
        'Gaspard',                              # 18
        'Nonna',                                # 19
        'Berden',                               # 20
        'Latanya',                              # 21
        'Tran',                                 # 22
        'Dick',                                 # 23
        'Raleigh',                              # 24
        'Troy',                                 # 25
        'Fisher',                               # 26
        'Lloyd',                                # 27
        'Percy',                                # 28
        'Zacharias',                            # 29
        'Tom',                                  # 30
        'Shep',                                 # 31
        'Chaeli',                               # 32
        'Cready',                               # 33
        'Spencer',                              # 34
        'Percy',                                # 35
        'Bill',                                 # 36
        'Ilene',                                # 37
        'Deitus',                               # 38
        'Tabasa',                               # 39
        'Sammy',                                # 40
        'Jane',                                 # 41
        'Fisher',                               # 42
        'Baral',                                # 43
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT06/CH20053 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH00033 ._CH',             # 07
        'ED6_DT07/CH00073 ._CH',             # 08
        'ED6_DT27/CH03590 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01630 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01463 ._CH',             # 0D
        'ED6_DT07/CH01270 ._CH',             # 0E
        'ED6_DT07/CH01050 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01100 ._CH',             # 11
        'ED6_DT07/CH01160 ._CH',             # 12
        'ED6_DT07/CH01470 ._CH',             # 13
        'ED6_DT07/CH01060 ._CH',             # 14
        'ED6_DT07/CH01140 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01690 ._CH',             # 18
        'ED6_DT07/CH01150 ._CH',             # 19
        'ED6_DT07/CH01140 ._CH',             # 1A
        'ED6_DT07/CH01460 ._CH',             # 1B
        'ED6_DT07/CH01490 ._CH',             # 1C
        'ED6_DT07/CH01180 ._CH',             # 1D
        'ED6_DT07/CH01120 ._CH',             # 1E
        'ED6_DT07/CH01130 ._CH',             # 1F
        'ED6_DT07/CH00023 ._CH',             # 20
        'ED6_DT07/CH00053 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT06/CH20053P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH00033P._CP',             # 07
        'ED6_DT07/CH00073P._CP',             # 08
        'ED6_DT27/CH03590P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01630P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01463P._CP',             # 0D
        'ED6_DT07/CH01270P._CP',             # 0E
        'ED6_DT07/CH01050P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01100P._CP',             # 11
        'ED6_DT07/CH01160P._CP',             # 12
        'ED6_DT07/CH01470P._CP',             # 13
        'ED6_DT07/CH01060P._CP',             # 14
        'ED6_DT07/CH01140P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01690P._CP',             # 18
        'ED6_DT07/CH01150P._CP',             # 19
        'ED6_DT07/CH01140P._CP',             # 1A
        'ED6_DT07/CH01460P._CP',             # 1B
        'ED6_DT07/CH01490P._CP',             # 1C
        'ED6_DT07/CH01180P._CP',             # 1D
        'ED6_DT07/CH01120P._CP',             # 1E
        'ED6_DT07/CH01130P._CP',             # 1F
        'ED6_DT07/CH00023P._CP',             # 20
        'ED6_DT07/CH00053P._CP',             # 21
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53970,
        Z                   = 0,
        Y                   = 1360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 57050,
        Z                   = 0,
        Y                   = 3000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 63570,
        Z                   = 0,
        Y                   = -2300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 66490,
        Z                   = 0,
        Y                   = -2200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 62300,
        Z                   = 0,
        Y                   = -3120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 120580,
        Z                   = 0,
        Y                   = -2280,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 121660,
        Z                   = 0,
        Y                   = -1200,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 120400,
        Z                   = 0,
        Y                   = -990,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 27820,
        Z                   = 0,
        Y                   = 62520,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 84510,
        Z                   = 0,
        Y                   = 56870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 92000,
        Z                   = 300,
        Y                   = 61850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 117070,
        Z                   = 0,
        Y                   = -1300,
        Direction           = 132,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 118280,
        Z                   = 0,
        Y                   = -2510,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 114540,
        Z                   = 0,
        Y                   = -500,
        Direction           = 228,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 113510,
        Z                   = 0,
        Y                   = -1480,
        Direction           = 273,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 57640,
        Z                   = 0,
        Y                   = -910,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 58990,
        Z                   = 0,
        Y                   = -920,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 117510,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 342,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -870,
        Z                   = 0,
        Y                   = 2340,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 540,
        Z                   = 0,
        Y                   = 2330,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -2600,
        Z                   = 0,
        Y                   = -1720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 3340,
        Z                   = 0,
        Y                   = -3440,
        Direction           = 289,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 1560,
        Z                   = 0,
        Y                   = -1380,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 1550,
        Z                   = 0,
        Y                   = -180,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 117540,
        Z                   = 0,
        Y                   = 3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 125600,
        Z                   = 0,
        Y                   = -3380,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 36,
    )


    DeclActor(
        TriggerX            = -2600,
        TriggerZ            = 0,
        TriggerY            = 820,
        TriggerRange        = 800,
        ActorX              = -4460,
        ActorZ              = 1500,
        ActorY              = 960,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28140,
        TriggerZ            = 0,
        TriggerY            = 61240,
        TriggerRange        = 800,
        ActorX              = 27820,
        ActorZ              = 1500,
        ActorY              = 62520,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25070,
        TriggerZ            = 0,
        TriggerY            = 56080,
        TriggerRange        = 800,
        ActorX              = 24330,
        ActorZ              = 3000,
        ActorY              = 55900,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24870,
        TriggerZ            = 0,
        TriggerY            = 57940,
        TriggerRange        = 800,
        ActorX              = 23860,
        ActorZ              = 2500,
        ActorY              = 58100,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24860,
        TriggerZ            = 0,
        TriggerY            = 59860,
        TriggerRange        = 800,
        ActorX              = 23870,
        ActorZ              = 2800,
        ActorY              = 59950,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6F2",          # 00, 0
        "Function_1_B26",          # 01, 1
        "Function_2_B99",          # 02, 2
        "Function_3_C91",          # 03, 3
        "Function_4_D27",          # 04, 4
        "Function_5_EA3",          # 05, 5
        "Function_6_111C",         # 06, 6
        "Function_7_405B",         # 07, 7
        "Function_8_5BC2",         # 08, 8
        "Function_9_966D",         # 09, 9
        "Function_10_96BC",        # 0A, 10
        "Function_11_970B",        # 0B, 11
        "Function_12_975A",        # 0C, 12
        "Function_13_97A9",        # 0D, 13
        "Function_14_97F8",        # 0E, 14
        "Function_15_9874",        # 0F, 15
        "Function_16_98EF",        # 10, 16
        "Function_17_9957",        # 11, 17
        "Function_18_99BE",        # 12, 18
        "Function_19_9A0F",        # 13, 19
        "Function_20_9A60",        # 14, 20
        "Function_21_9A7C",        # 15, 21
        "Function_22_9A98",        # 16, 22
        "Function_23_9AB4",        # 17, 23
        "Function_24_9AD0",        # 18, 24
        "Function_25_C2E2",        # 19, 25
        "Function_26_C32A",        # 1A, 26
        "Function_27_C372",        # 1B, 27
        "Function_28_C3BA",        # 1C, 28
        "Function_29_C402",        # 1D, 29
        "Function_30_C497",        # 1E, 30
        "Function_31_DE8B",        # 1F, 31
        "Function_32_DEA7",        # 20, 32
        "Function_33_DEC3",        # 21, 33
        "Function_34_DEDF",        # 22, 34
        "Function_35_DEFB",        # 23, 35
        "Function_36_DF21",        # 24, 36
        "Function_37_DF45",        # 25, 37
        "Function_38_E516",        # 26, 38
        "Function_39_E59C",        # 27, 39
        "Function_40_E61D",        # 28, 40
        "Function_41_E696",        # 29, 41
    )


    def Function_0_6F2(): pass

    label("Function_0_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_709")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_709")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_746")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 60680, 200, -3460, 270)

    label("loc_777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_79A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C7")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_7C7")

    Jump("loc_9E1")

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_8D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_802")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)

    label("loc_802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_833")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 55450, 200, -2270, 180)

    label("loc_833")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_860")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_860")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_883")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8A6")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_8A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D3")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_8D3")

    Jump("loc_9E1")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_935")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_905")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_905")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_932")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_932")

    Jump("loc_9E1")

    label("loc_935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96E")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_96E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_991")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_9B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E1")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_A6D")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_A88")

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A7C")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_A88")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A88")
    SetChrFlags(0x1B, 0x80)

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A9E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)
    Jump("loc_B25")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_ABD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 37)
    Jump("loc_B25")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD1")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_B25")

    label("loc_AD1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_ADD"),
        (SWITCH_DEFAULT, "loc_B25"),
    )


    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF5")
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_B22")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0D")
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_B22")

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B22")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_B22")

    Jump("loc_B25")

    label("loc_B25")

    Return()

    # Function_0_6F2 end

    def Function_1_B26(): pass

    label("Function_1_B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B42")
    OP_B1("t4121_y")
    Jump("loc_B4B")

    label("loc_B42")

    OP_B1("t4121_n")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_B61")
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_B83")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_B77")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jump("loc_B83")

    label("loc_B77")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_B98")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_B98")

    Return()

    # Function_1_B26 end

    def Function_2_B99(): pass

    label("Function_2_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BB8")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_BCD")

    label("loc_BB8")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_BCD")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1C")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_C1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C3F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C62")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C8F")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_C8F")

    OP_0D()
    Return()

    # Function_2_B99 end

    def Function_3_C91(): pass

    label("Function_3_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CAC")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_CBD")

    label("loc_CAC")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_CBD")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF8")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_CF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D25")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_D25")

    OP_0D()
    Return()

    # Function_3_C91 end

    def Function_4_D27(): pass

    label("Function_4_D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D48")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_D5F")

    label("loc_D48")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_D5F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DC1")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    SetChrSubChip(0xA, 0)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)

    label("loc_DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF7")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 55450, 200, -2270, 180)

    label("loc_DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E29")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrSubChip(0xB, 0)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E4C")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E6F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA1")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrSubChip(0xE, 0)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_EA1")

    OP_0D()
    Return()

    # Function_4_D27 end

    def Function_5_EA3(): pass

    label("Function_5_EA3")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_A3(0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F49")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 60680, 200, -3460, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2E")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F49")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_F49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FB5")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    SetChrSubChip(0xA, 0)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9A")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB5")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100E")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF3")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100E")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_100E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1076")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrSubChip(0xE, 0)
    SetChrPos(0xE, 54780, 0, -5080, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105B")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_105B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1076")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_1076")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_111B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05A standby member was equipped with a Zero Field Generator.\x01",
            "It has been recovered and added to party inventory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_111B")

    Return()

    # Function_5_EA3 end

    def Function_6_111C(): pass

    label("Function_6_111C")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0x10A, -2600, 0, 1150, 270)
    SetChrPos(0x101, -2600, 0, 300, 270)
    SetChrPos(0x9, -500, -130, -7700, 354)
    SetChrPos(0xA, 500, -130, -7700, 354)
    OP_6D(1280, 0, -3520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_11BB():
        OP_6D(-4090, 0, 1200, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_11BB)

    def lambda_11D3():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11D3)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_28(0x80, 0x1, 0x1000)

    ChrTalk(    #1
        0x8,
        (
            "#760F#6PI see. The both of you have done well.\x02\x03",

            "Well, then! Here's your reward, based\x01",
            "on your performance during training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1004F#6PHuh? We get paid for training? Umm,\x01",
            "not that I'll complain, but are you sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#760F#6PNaturally. It is part of your job, after all.\x02\x03",

            "It won't be a problem so long as you\x01",
            "put your new skills to good use for the\x01",
            "Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016F#6PAh-haha...\x01",
            "Right, um, I'll do my best!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x7E, 0x4, 0x10)
    OP_AF(0xCD, 0x7E)
    Sleep(100)
    OP_28(0x7F, 0x4, 0x10)
    OP_28(0x7F, 0x4, 0x20)
    OP_28(0x80, 0x4, 0x10)
    OP_28(0x80, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #5
        0x8,
        (
            "#761F#6PIt does seem like you two had\x01",
            "quite a fulfilling training period.\x01",
            "You even carry yourselves differently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1006F#6PIt was! I learned a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#1310F#4PIf I ever get the chance,\x01",
            "I'd love to go again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#761F#6PHah! I'm glad to hear it.\x02\x03",

            "#760FSpeaking of which, Kurt and the others\x01",
            "remained at the training grounds, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F#6PYeah. Carna and Grant are doing\x01",
            "some expert-level stuff, I think.\x02\x03",

            "They said they won't be\x01",
            "back for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        (
            "#1316F#4PI think I get what Elnan is poking at,\x01",
            "though. The guild's down three full,\x01",
            "skilled bracers now.\x02\x03",

            "We're gonna be reeeeally busy from\x01",
            "now on...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)
    Sleep(400)

    ChrTalk(    #11
        0x10A,
        (
            "#810F#4PAnd on top of that, Cassius is still\x01",
            "devoting all his time to the military,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #12
        0x101,
        (
            "#1011F#6POh, yeah.\x02\x03",

            "If I remember right, he's currently\x01",
            "working out of Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#760F#6PCassius--Brigadier General Bright--has been\x01",
            "welcomed back into the army and is\x01",
            "now the head of military command.\x02\x03",

            "He's essentially the head of Her Majesty's\x01",
            "Royal Army at this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(900)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)
    Sleep(400)

    ChrTalk(    #14
        0x101,
        (
            "#1004F#6PWha?! He's the head of the army now?!\x02\x03",

            "I thought General Morgan had that\x01",
            "position!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#760F#6PAs I understand it, that was the original\x01",
            "idea, but Morgan himself proposed\x01",
            "giving Cassius full rein.\x02\x03",

            "#761FHe seems to be entrusting the future\x01",
            "of the army to your father, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1019F#6PThe future? Entrusted to Dad?\x01",
            "Well, we're doomed, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#819F#4PHaha... Well, I can see Cassius being\x01",
            "given that much responsibility, y'know?\x02\x03",

            "#1314FThat's gonna mean we're down our\x01",
            "S-rank hero, too, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#764F#6PI think it's safe to say we'll have\x01",
            "plenty of support from the military\x01",
            "from now on. However...\x02\x03",

            "#762FAt the same time, we have new\x01",
            "threats to concern ourselves with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#814F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002F#6PRight. You mean the society.\x02\x03",

            "Did they start to do stuff\x01",
            "while we were away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#764F#6PNo. They've done nothing...obvious.\x01",
            "But that is, admittedly, how they work.\x02\x03",

            "#765FWhat has happened are several strange\x01",
            "occurrences over the past month.\x02\x03",

            "One example would be the changes\x01",
            "in the wild beasts and monsters in\x01",
            "various regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1026F#6PThe monsters have changed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#812F#4PUh, do you mind defining 'change,' Elnan?\x01",
            "I hope it isn't what I think it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#762F#6PTo start with, heretofore undocumented\x01",
            "types of monsters are showing up all\x01",
            "across the country.\x02\x03",

            "Even the existing monsters have become\x01",
            "far more vicious and powerful. Travel\x01",
            "has become significantly more dangerous.\x02\x03",

            "No one has been able to put forward an\x01",
            "explanation as to why this is happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10A,
        (
            "#1317F#4PSo every beastie out there is\x01",
            "nastier, just 'cause? Oh, man...\x02\x03",

            "#815FIt's definitely the society's doing!\x01",
            "They're trying to turn us all into\x01",
            "monster kibble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#764F#6PCalm yourself, Anelace.\x01",
            "We still don't have enough evidence\x01",
            "to be certain of anything.\x02\x03",

            "#762FWe do know one thing, though...\x01",
            "Things definitely began happening after\x01",
            "the queen's birthday celebrations.\x02\x03",

            "That we know for certain. The first reports\x01",
            "came in practically the day after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        "#813F#4PAw, crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1003F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#760F#6PDon't look so glum. We've actually\x01",
            "been formulating a response, of sorts.\x02\x03",

            "And I'd very much like for the two of\x01",
            "you to be a part of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004F#6PA 'response'...?\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    SetChrName("Woman's Voice")

    NpcTalk(    #31
        0x9,
        "Woman's Voice",
        (
            "#2PAh, you two are here already?\x01",
            "I wanted to meet you at the port!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_2161():
        OP_6D(-340, 0, -2920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2161)

    def lambda_2179():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2179)

    def lambda_2191():
        TurnDirection(0x101, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2191)
    Sleep(100)

    def lambda_21A4():
        TurnDirection(0x10A, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_21A4)
    Sleep(100)

    def lambda_21B7():
        TurnDirection(0x8, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21B7)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_21EA():
        OP_8E(0x9, 0xFFFFFE0C, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_21EA)

    def lambda_2205():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2205)
    Sleep(300)

    def lambda_221C():
        OP_8E(0xA, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_221C)

    def lambda_2237():
        OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2237)

    def lambda_2249():
        TurnDirection(0x101, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2249)

    def lambda_2257():
        TurnDirection(0x10A, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2257)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #32
        0x10A,
        "#814F#4PSchera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1004F#6PAnd Agate, too!\x01",
            "This is, uh, a surprise!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22CA():
        OP_6D(-2940, 0, 920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22CA)

    def lambda_22E2():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E2)

    def lambda_22FA():
        OP_8F(0x9, 0xFFFFF5EC, 0x0, 0xFFFFFB96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_22FA)
    Sleep(300)

    def lambda_231A():
        OP_8F(0xA, 0xFFFFFA06, 0x0, 0xFFFFFACE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_231A)

    def lambda_2335():

        label("loc_2335")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_2335")

    QueueWorkItem2(0x101, 2, lambda_2335)
    Sleep(1000)

    def lambda_234B():
        OP_8E(0x10A, 0xFFFFF952, 0x0, 0x15E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_234B)
    WaitChrThread(0x10A, 0x2)
    OP_8C(0x10A, 180, 400)
    WaitChrThread(0x9, 0x0)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0xA, 0x0)
    TurnDirection(0xA, 0x10A, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)

    ChrTalk(    #34
        0x9,
        (
            "#021FWelcome back, you two.\x01",
            "It's good to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "#051F#5PHeh, you two got back sooner\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1001F#4PI'm really happy to see you,\x01",
            "too, Schera!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)
    Sleep(400)

    ChrTalk(    #37
        0x101,
        (
            "#1017F#6PAnd Agate, hi.\x01",
            "It's been a while, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "#053F#5PYeah, think the last time we saw\x01",
            "each other was during the queen's\x01",
            "birthday shindig...\x02\x03",

            "#552F...The old man told me about\x01",
            "Joshua, you know.\x02\x03",

            "#051FI'd heard you were pretty broken\x01",
            "up over it, but you seem back\x01",
            "on your feet already, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1016F#6PHeheh... Yeah, mostly.\x02\x03",

            "#1008FMore to the point, though...\x01",
            "why are you two together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10A,
        (
            "#1310F#2PGood question! I should get a camera.\x01",
            "This is like seein' a King Penguin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#023FOh, really, it isn't THAT rare, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#053F#5PGotta admit we don't work together\x01",
            "that often, Scherazard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#760FActually, Scherazard and Agate are\x01",
            "here to begin a special mission.\x02\x03",

            "I asked them to come here\x01",
            "today for a specific reason.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)

    ChrTalk(    #44
        0x101,
        "#1004F#6PA mission?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #45
        0x8,
        (
            "#762FIndeed. They will be tasked with\x01",
            "investigating the Society of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        "#1005F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        (
            "#1317F#4PWait, like, chasing down their agents\x01",
            "and stuff? Isn't that dangerous?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#020FI wish it was that exciting.\x01",
            "'Investigating' might be a little too\x01",
            "specific, though.\x02\x03",

            "We're barely even certain the society\x01",
            "exists at this point, you realize,\x01",
            "despite what Cassius says.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #49
        0xA,
        (
            "#053F#5PWe're gonna be wandering all across Liberl,\x01",
            "keeping an eye out for anything resembling\x01",
            "a secret society bent on world domination...\x02\x03",

            "#051FThis is probably not gonna be the\x01",
            "most exciting job ever, is the point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1015F#6POh, I get it...\x02\x03",

            "#1007FI guess groping around in the dark is\x01",
            "the best we can do right now, huh...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)

    ChrTalk(    #51
        0x101,
        (
            "#1011F#6PSo, I'm guessing you want\x01",
            "us to tag along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#760FYes, I'd like to assign the two of you\x01",
            "to assist Scherazard and Agate.\x02\x03",

            "The plan is to have Schera and Agate\x01",
            "investigate different areas separately.\x02\x03",

            "I would like for them to have a partner,\x01",
            "though. Just in case the society really\x01",
            "is as dangerous as we think it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        (
            "#818F#4POkay, so one of us helps Schera...\x02\x03",

            "...and the other helps Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#760FExactly.\x02\x03",

            "Are you willing to assist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1018F#6PYou bet we are!\x02\x03",

            "I was going to go looking for the society\x01",
            "on my own anyway, so this is perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#1310F#4PI wanna help, too.\x02\x03",

            "There's no way I can just sit around when\x01",
            "there's suspicious stuff going on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#761FThank you.\x01",
            "I'm glad we have the help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x10A, 0xA, 400)
    Sleep(400)

    ChrTalk(    #58
        0x9,
        (
            "#020FWell, then! The one remaining hurdle\x01",
            "would be team formation.\x02\x03",

            "I'd be fine with either of you, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#051F#5PWe all know each other, basically.\x02\x03",

            "You two figure out how it'll\x01",
            "work out best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1007F#6PMmmph... Of course you have\x01",
            "to push the decision on to us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #61
        0x101,
        (
            "#1015F#6PWhat do you think, Anelace?\x01",
            "How should we do this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #62
        0x10A,
        (
            "#817F#4PHmmmmm... Well...\x02\x03",

            "This might be kinda irresponsible\x01",
            "of me...\x02\x03",

            "#810F...but I think it might be best if\x01",
            "you decide, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1004F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        (
            "#810F#4PYou've only been a full bracer\x01",
            "for a little while, right?\x02\x03",

            "You probably haven't found\x01",
            "your style as a bracer yet...\x02\x03",

            "#811FSo how about using this as\x01",
            "a chance to see what kinda\x01",
            "bracer you want to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1011F#6PAnelace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#027FWell, well! Look at you, Anelace!\x02\x03",

            "When did you learn to talk\x01",
            "like a professional?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #67
        0x10A,
        "#811F#2PHeh-heh! Leave it to meee! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "#053F#5PEither way, girl's got a point.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #69
        0xA,
        (
            "#050F#5PSchera and I are the same rank, but\x01",
            "the ways we fight are way different.\x02\x03",

            "I barely use arts except for support once\x01",
            "in a while. I focus more on cutting things\x01",
            "down with my sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#020FAnd I emphasize speed, the\x01",
            "range of my whip, and orbal arts.\x02\x03",

            "You can't really go 'wrong' with\x01",
            "either of us, I think.\x02\x03",

            "#021FKeep in mind that being a bracer\x01",
            "involves much more than just fighting,\x01",
            "though.\x02\x03",

            "Think hard and choose the partner\x01",
            "you think matches you best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #71
        0x101,
        (
            "#1007F#6PHmmmm...\x02\x03",

            "#1008FWell, then I'll... \x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_B7(0x9)
    OP_31(0x5, 0x0, 0x2A)
    OP_31(0x5, 0xFE, 0x0)
    OP_41(0x5, 0x9E, 0xFF)
    OP_41(0x5, 0xFF, 0xFF)
    OP_41(0x5, 0x120, 0xFF)
    OP_41(0x5, 0x283, 0x0)
    OP_41(0x5, 0x270, 0x1)
    OP_41(0x5, 0x267, 0x2)
    OP_41(0x5, 0x25E, 0x5)
    OP_35(0x5, 0x8C)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x100)
    OP_31(0x2, 0x0, 0x2A)
    OP_31(0x2, 0xFE, 0x0)
    OP_41(0x2, 0x44, 0xFF)
    OP_41(0x2, 0xFF, 0xFF)
    OP_41(0x2, 0x120, 0xFF)
    OP_41(0x2, 0x280, 0x0)
    OP_41(0x2, 0x2C8, 0x1)
    OP_41(0x2, 0x264, 0x2)
    OP_41(0x2, 0x26D, 0x4)
    OP_35(0x2, 0x8C)
    OP_35(0x2, 0x0)
    OP_BB(0x2, 0x6, 0xF0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x18\x07\x05Which partner will you choose?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "...I'll pick Schera!\x01",      # 0
            "...I'll pick Agate!\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_345A"),
        (1, "loc_3460"),
        (SWITCH_DEFAULT, "loc_3466"),
    )


    label("loc_345A")

    OP_A2(0x1200)
    Jump("loc_3466")

    label("loc_3460")

    OP_A2(0x1201)
    Jump("loc_3466")

    label("loc_3466")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3A43")

    ChrTalk(    #73
        0x9,
        (
            "#020FI thought so.\x01",
            "Well, then, we'll work together.\x02\x03",

            "#021FI'll be expecting great things\x01",
            "from our newest full bracer, mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1007F#6PEugh... I think I made a mistake...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #75
        0x10A,
        (
            "#1310F#2PSo that means I'll go with Agate.\x02\x03",

            "#811FI'll do my best, I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "#051F#5PI'll be countin' on you.\x02\x03",

            "#053FAnyway, now that that's sorted...\x02\x03",

            "The next step is figuring out how\x01",
            "we're gonna wander the country,\x01",
            "lookin' for shadows.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #77
        0x9,
        "#020FAny thoughts, Elnan?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    def lambda_3657():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3657)

    def lambda_3665():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3665)

    def lambda_3673():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3673)
    Sleep(400)

    ChrTalk(    #78
        0x8,
        (
            "#764FHmm. Possibly.\x02\x03",

            "#760FI would suggest beginning by going to help\x01",
            "the regions with the busiest branches.\x02\x03",

            "In fact, I just received pleas for aid from\x01",
            "the Ruan and Bose branches today.\x01",
            "Rather desperate-sounding ones, at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#026FHm. That makes some sense with\x01",
            "both Grant and Carna being away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10A, 400)

    ChrTalk(    #80
        0xA,
        "#050F#5PAnelace. You're familiar with Bose, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #81
        0x10A,
        "#816F#2PWell, duh! I am a Bose kid, after all.\x02",
    )

    CloseMessageWindow()

    def lambda_3833():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3833)

    def lambda_3841():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3841)

    ChrTalk(    #82
        0xA,
        (
            "#050F#5PWe'll handle the junk at\x01",
            "the Bose branch, then.\x02\x03",

            "I've got some business up\x01",
            "that way anyhow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1011F#6PThat's right, your hometown\x01",
            "is Ravennue Village.\x02\x03",

            "Need to make a quick trip home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        "#053F#5P...Somethin' like that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #85
        0x9,
        (
            "#021FWe'll head to the Ruan branch, then.\x02\x03",

            "#020FIs that all right with you, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #86
        0x101,
        (
            "#1006F#6POf course!\x02\x03",

            "#1012FMan, I wonder how everyone\x01",
            "in Ruan is doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#760FI'll contact the branches\x01",
            "ahead of your arrival.\x02\x03",

            "Be careful, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4046")

    label("loc_3A43")


    ChrTalk(    #88
        0xA,
        (
            "#053F#5PHuh, all right then.\x02\x03",

            "#050FJust keep in mind you're a full bracer\x01",
            "now. I ain't gonna go easy on you.\x02\x03",

            "Hope you're ready.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #89
        0x101,
        (
            "#1006F#6PYeah, I know.\x02\x03",

            "#1016FI kinda thought you might say\x01",
            "something macho like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        "#055F#5PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#027FCome on, now. Starting off with\x01",
            "an argument is probably not the\x01",
            "best way to begin this trip.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 400)

    ChrTalk(    #92
        0x9,
        (
            "#021FAnyway, that will make Anelace\x01",
            "and me the other team.\x02\x03",

            "#020FI'm looking forward to seeing\x01",
            "how your training turned out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10A,
        (
            "#816F#2PHeck yeah!\x02\x03",

            "#811FHeheh! It feels like forever since\x01",
            "we worked together, Schera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "#053F#5PSo with that out of the way...\x02\x03",

            "#050FThe next step is figuring out how\x01",
            "we're gonna wander the country,\x01",
            "lookin' for shadows.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #95
        0x9,
        "#020FAny thoughts, Elnan?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    def lambda_3D4A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D4A)

    def lambda_3D58():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D58)

    def lambda_3D66():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3D66)
    Sleep(400)

    ChrTalk(    #96
        0x8,
        (
            "#764FHmm. Possibly.\x02\x03",

            "#760FI would suggest beginning by going\x01",
            "to help the regions with the busiest\x01",
            "branches.\x02\x03",

            "In fact, I just received pleas for aid from\x01",
            "the Ruan and Rolent branches today.\x01",
            "Rather desperate-sounding ones, at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "#025FThat sounds just lovely... I suppose\x01",
            "I have been away from Rolent for too\x01",
            "long.\x02\x03",

            "#020FI'd best go help Aina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10A,
        (
            "#810F#4PYeah, I think that's for the best.\x02\x03",

            "#811FIt's been a while since I've seen\x01",
            "Aina, too! This'll be fun!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #99
        0xA,
        (
            "#051F#5PWe'll head to Ruan, then.\x02\x03",

            "You're cool with that, right, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #100
        0x101,
        (
            "#1006F#6POf course!\x02\x03",

            "#1012FMan, I wonder how everyone\x01",
            "in Ruan is doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#760FI'll contact the branches\x01",
            "ahead of your arrival.\x02\x03",

            "Be careful, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4046")

    FadeToDark(1500, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_111C end

    def Function_7_405B(): pass

    label("Function_7_405B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_406C")
    Call(0, 38)

    label("loc_406C")

    EventBegin(0x0)
    SetChrPos(0x101, -2600, 0, 1230, 270)
    SetChrPos(0xF7, -2600, 0, 190, 270)
    SetChrPos(0xD, -2020, 0, -990, 270)
    SetChrPos(0xC, -1560, 0, -30, 270)
    SetChrPos(0xB, -1600, 0, 1080, 270)
    SetChrPos(0xE, -1910, 0, 2020, 270)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6D(-7190, 0, 1580, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_413F():
        OP_6D(-3380, 0, 980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_413F)

    def lambda_4157():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4157)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #102
        0x8,
        (
            "#761F#6PWelcome, everyone, and thank you\x01",
            "for coming.\x02\x03",

            "#760FI've read the reports from Ruan and\x01",
            "Zeiss.\x02\x03",

            "Good work, truly. You've done well in\x01",
            "opposing the society thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1007F#7PI doubt the guys we've fought would\x01",
            "agree...\x02\x03",

            "Both that masked man and the guy\x01",
            "with sunglasses didn't really seem\x01",
            "to take it, or us, seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#760F#6PEven knowing that the society is\x01",
            "moving is valuable, Estelle. Don't\x01",
            "disparage yourself.\x02\x03",

            "Your successes should make the\x01",
            "Royal Army trust us even further.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_43D9")

    ChrTalk(    #105
        0x106,
        (
            "#050F#6PSo, speakin' of which, what does the\x01",
            "army want with us?\x02\x03",

            "Somethin' society-related?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_43D9")


    ChrTalk(    #106
        0x103,
        (
            "#020F#6POn that note, why does the army want\x01",
            "to see us?\x02\x03",

            "I'm guessing it has something to do\x01",
            "with the society?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444D")


    ChrTalk(    #107
        0x8,
        (
            "#764F#6PYes, about that...\x02\x03",

            "#762FIt seems they don't want to discuss it\x01",
            "over the phone.\x02\x03",

            "An army official will be coming by soon\x01",
            "to explain the situation in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "#035FSomething that cannot be discussed\x01",
            "by phone, they say?\x02\x03",

            "#030FWhat they mean is that they do not wish\x01",
            "to risk any unwelcome ears listening in\x01",
            "on the call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1020F#7PWait, you can do that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "#762F#6POh, yes. It's quite possible.\x02\x03",

            "Telephones are convenient, but with\x01",
            "the right equipment, intercepting a\x01",
            "conversation signal is not very difficult.\x02\x03",

            "#764FWe use a scrambling device between\x01",
            "branches to prevent interception of\x01",
            "guild business. Unfortunately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1015F#7PThe, uh, 'scrambling' doesn't work with\x01",
            "the army for some reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#765F#6PYes. The army uses a different system.\x02\x03",

            "All calls between us are thus completely\x01",
            "open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1007F#7PWell, that's ducky.\x02\x03",

            "#1019FWhy can't the army just share a mixer-\x01",
            "scrambler thingamajigger with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "#070F#4PWe ARE working together, but we're still\x01",
            "an international citizen's group and they're\x01",
            "a national defense force.\x02\x03",

            "As much as your father trusts us, Estelle,\x01",
            "I don't think they can give us something\x01",
            "so sensitive so easily.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_498D")

    ChrTalk(    #115
        0x106,
        (
            "#053F#6PHang on, Elnan.\x02\x03",

            "#051FIt still sounds like you've got some\x01",
            "idea of what this is all about.\x02\x03",

            "Otherwise, you wouldn't've bothered\x01",
            "calling us outta Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A33")

    label("loc_498D")


    ChrTalk(    #116
        0x103,
        (
            "#026F#6PHmmm... Elnan?\x02\x03",

            "#020FFrom the sound of things, you do have\x01",
            "some idea of what this is all about, yes?\x02\x03",

            "I doubt you would've called us directly\x01",
            "otherwise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A33")


    ChrTalk(    #117
        0x8,
        (
            "#761F#6PAh! Am I being that transparent?\x02\x03",

            "#760FI can only hazard a guess, really, but\x01",
            "I believe it's very likely this has to do with\x01",
            "the signing of the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1004F#7PThe non-aggression pact?\x02\x03",

            "#1015FI remember hearing something about that...\x02\x03",

            "What exactly is going on with that, anyway?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #119
        0xC,
        (
            "#040F#5PIt is a treaty affecting Liberl, Erebonia, and\x01",
            "Calvard, proposed by Grandmother.\x02\x03",

            "In short, it says all countries involved will\x01",
            "attempt at all times to solve international\x01",
            "disputes without resorting to force.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 400)

    def lambda_4C79():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4C79)
    Sleep(50)

    def lambda_4C8C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4C8C)
    Sleep(50)

    def lambda_4C9F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4C9F)
    Sleep(50)

    def lambda_4CB2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4CB2)
    Sleep(300)

    ChrTalk(    #120
        0x101,
        (
            "#1004F#7PWhoa!\x02\x03",

            "So, like, it'll end war?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "#047F#5PWell...no. There's no true enforcement mechanism\x01",
            "beyond simply being known as a treaty-breaker, so\x01",
            "enforcing it like that would be difficult...\x02\x03",

            "#040FIt should still be something of a deterrent, though,\x01",
            "and it will hopefully promote more friendly relations\x01",
            "between ourselves and others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1011F#7POkay, I get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xE,
        (
            "#071F#4PQueen Alicia does it again! She's got\x01",
            "a good eye for this kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xD,
        (
            "#061F#5PIt'd be neat if that made the countries\x01",
            "nicer to each other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#760F#6PThe pact is being signed in a large ceremony\x01",
            "at the Erbe Royal Villa next weekend.\x02\x03",

            "Dignitaries from all three nations will be\x01",
            "attending, and the media is paying close\x01",
            "attention.\x02\x03",

            "#764F...Which is to say, they may as well have\x01",
            "painted a sign on the roof of the Villa saying,\x01",
            "'Ouroboros, please attack us.'\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    def lambda_5024():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5024)
    Sleep(50)

    def lambda_5037():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5037)
    Sleep(50)

    def lambda_504A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_504A)
    Sleep(50)

    def lambda_505D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_505D)
    Sleep(50)

    def lambda_5070():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5070)
    Sleep(300)

    ChrTalk(    #126
        0x101,
        "#1002F#7POh... Yeah, that could really get ugly...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5130")

    ChrTalk(    #127
        0x106,
        (
            "#053F#6PHm. Got our work cut out for us, then.\x02\x03",

            "#051FGuess we just wait here for the army\x01",
            "official for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51B2")

    label("loc_5130")


    ChrTalk(    #128
        0x103,
        (
            "#026F#6PThis is going to be quite the task,\x01",
            "isn't it...?\x02\x03",

            "#020FSo you just want us to wait here for\x01",
            "the army official, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B2")


    ChrTalk(    #129
        0x8,
        (
            "#760F#6PCorrect.\x02\x03",

            "We do have some time before he's\x01",
            "scheduled to arrive, so feel free to--\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #130
        0x8,
        "#763F#6POh, pardon me a moment.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    def lambda_52B2():
        OP_6D(-4530, 0, 870, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52B2)
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    Sleep(400)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #131
        0x8,
        (
            "#760F#6PHello. This is the Grancel Bracer Guild branch.\x02\x03",

            "Yes... Yes...\x02\x03",

            "#763F...\x02\x03",

            "#765FI see... Yes.\x02\x03",

            "That certainly is a problem.\x02\x03",

            "#764FJust a moment, please...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #132
        0x101,
        "#1015FIs that the army on the phone?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(    #133
        0x8,
        (
            "#760F#6PNo, it's a member of the Erbe Royal Villa\x01",
            "staff.\x02\x03",

            "They seem to have a lost child from one\x01",
            "of the tourists in their care.\x02\x03",

            "Unfortunately, they can't seem to actually\x01",
            "locate her parents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1004FThat's awful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        "#043F#2PDo they want us to help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#760F#6PJust so, Your Highness. They've asked\x01",
            "for our aid in locating the child's parents\x01",
            "or guardians.\x02\x03",

            "There's still some time before our guest\x01",
            "from the army is due to arrive. Would you\x01",
            "mind taking care of this?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5683")

    ChrTalk(    #137
        0x101,
        (
            "#1006FSure! We'd be glad to.\x02\x03",

            "You're in, right, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x106,
        (
            "#051F#5PCan't say no to a kid in need.\x01",
            "Let's head out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56F5")

    label("loc_5683")


    ChrTalk(    #139
        0x101,
        (
            "#1006FSure! We'd be glad to.\x02\x03",

            "You're in, right, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        "#021F#5POf course! Let's get over to the villa.\x02",
    )

    CloseMessageWindow()

    label("loc_56F5")


    ChrTalk(    #141
        0x8,
        "#760F#6PThank you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #142
        0x8,
        (
            "#761F#6PHello? Yes, we have a team of bracers we\x01",
            "can dispatch immediately.\x02\x03",

            "#760FAnd your name, sir? ...Yes... Understood.\x02\x03",

            "Well, then, our bracers will be over as\x01",
            "soon as they are able.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(800)
    OP_8C(0x8, 90, 400)

    def lambda_57F8():
        OP_6D(-3380, 0, 980, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57F8)

    def lambda_5810():
        OP_8E(0xFE, 0xFFFFEE80, 0x0, 0x3C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5810)
    Sleep(500)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #143
        0x8,
        (
            "#760F#6PThe lost child is in the charge of a\x01",
            "butler named Raymond.\x02\x03",

            "Once you arrive at the villa, inquire\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1006F#7PAll right, then!\x02\x03",

            "#1015FWait a sec. 'Raymond'... Why does\x01",
            "that ring a bell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xE,
        (
            "#073F#4PWasn't he that one butler we found?\x02\x03",

            "You know, when we saved Kloe during\x01",
            "the coup. He was hiding under a counter.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #146
        0x101,
        "#1006F#7PRight, Nial's friend!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "#761F#6PAh, good! If you know him, that\x01",
            "should make things even easier.\x02\x03",

            "#760FWell, then. Good luck.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-5650, 0, -18030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #148
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5B09")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_5B1E")

    label("loc_5B09")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_5B1E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0x0, -140, 0, 90, 180)
    SetChrPos(0x1, -140, 0, 90, 180)
    SetChrPos(0x2, -140, 0, 90, 180)
    SetChrPos(0x3, -140, 0, 90, 180)
    OP_6D(-140, 0, 90, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x160B)
    OP_4B(0x8, 255)
    OP_28(0x89, 0x4, 0x2)
    OP_28(0x89, 0x4, 0x8)
    OP_28(0x89, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_7_405B end

    def Function_8_5BC2(): pass

    label("Function_8_5BC2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BDD")
    Call(0, 38)
    Call(0, 39)
    AddParty(0x2E, 0xFF, 0xFF)

    label("loc_5BDD")

    SetChrPos(0xF, -2310, 0, 2150, 180)
    ClearChrFlags(0xF, 0x80)
    OP_4A(0x8, 255)
    Call(0, 29)
    SetChrPos(0xFA, -2600, 0, 500, 360)
    SetChrPos(0xFB, -1500, 0, 480, 360)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x12F, 0x80)
    OP_6D(-110, -250, -5770, 0)
    OP_67(0, 7440, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0xC)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x12F, 0x1, 0x0, 0xA)
    Sleep(800)

    ChrTalk(    #149
        0x101,
        (
            "#1006F#6PWe're back, Elnan!\x02\x03",

            "#1004FOh!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CEA():
        OP_6D(-2890, 0, 1460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CEA)

    def lambda_5D02():
        OP_67(0, 7350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D02)

    def lambda_5D1A():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D1A)

    def lambda_5D2A():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5D2A)
    Sleep(100)

    def lambda_5D3D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D3D)
    Sleep(200)

    def lambda_5D50():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_5D50)
    Sleep(100)

    def lambda_5D63():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_5D63)
    WaitChrThread(0xFB, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5DA9")

    ChrTalk(    #150
        0x107,
        "#560F#6PHi, Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E0C")

    label("loc_5DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5DDD")

    ChrTalk(    #151
        0x108,
        "#070F#6PEstelle. Welcome back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E0C")

    label("loc_5DDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5E0C")

    ChrTalk(    #152
        0x104,
        "#030F#6PAh, you've returned.\x02",
    )

    CloseMessageWindow()

    label("loc_5E0C")

    Sleep(300)

    def lambda_5E17():
        OP_8E(0xFE, 0xFFFFF5D8, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5E17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xFA)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E4F")
    OP_43(0xFB, 0x0, 0x0, 0x14)
    Sleep(400)
    OP_43(0xFA, 0x0, 0x0, 0x15)
    Jump("loc_5E62")

    label("loc_5E4F")

    OP_43(0xFB, 0x0, 0x0, 0x16)
    Sleep(400)
    OP_43(0xFA, 0x0, 0x0, 0x17)

    label("loc_5E62")


    def lambda_5E68():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0x1E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_5E68)
    Sleep(200)

    def lambda_5E88():
        OP_8E(0xFE, 0xFFFFF678, 0x0, 0xFFFFFD58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_5E88)
    Sleep(300)

    def lambda_5EA8():
        OP_8E(0xFE, 0xFFFFFB14, 0x0, 0xFFFFFDC6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_5EA8)
    Sleep(300)

    def lambda_5EC8():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xFFFFF984, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 0, lambda_5EC8)
    WaitChrThread(0x101, 0x0)
    OP_8C(0xF, 180, 400)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0xF8, 0x0)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #153
        0xF,
        (
            "#701FHello again, Miss Bright. We seem\x01",
            "to be running into each other quite\x01",
            "a bit these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1018F#6PWell, hey there, Colonel Cid!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12F, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FFE")

    ChrTalk(    #155
        0x106,
        (
            "#051FThought the old man might send you, Cid.\x02\x03",

            "You're back from Leiston Fortress, I see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6064")

    label("loc_5FFE")


    ChrTalk(    #156
        0x103,
        (
            "#027FAh, so Cassius sent you to help us.\x01",
            "That makes sense.\x02\x03",

            "You came from Leiston, I'm guessing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6064")


    ChrTalk(    #157
        0xF,
        (
            "#701FThat's right.\x02\x03",

            "I just arrived here a little while ago on\x01",
            "one of our patrol ships. I apologize for\x01",
            "the wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1011F#6PNo, it's okay.\x02\x03",

            "We actually had a little job of our own\x01",
            "to take care of.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)

    ChrTalk(    #159
        0x8,
        (
            "#763F#6PHmm...?\x02\x03",

            "Speaking of which, would that young\x01",
            "lady be...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #160
        0x101,
        (
            "#1015F#7POh, right. Yeah, she is.\x02\x03",

            "Some stuff went down, so we\x01",
            "had to bring her along.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)

    ChrTalk(    #161
        0x101,
        (
            "#1011F#6PHey, Renne?\x02\x03",

            "We've got some things we need to\x01",
            "talk about with the army man. Can\x01",
            "you go wait on the second floor?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_626D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_626D)

    def lambda_627B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_627B)
    Sleep(200)

    def lambda_628E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_628E)

    def lambda_629C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_629C)
    Sleep(200)

    def lambda_62AF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_62AF)

    def lambda_62BD():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_62BD)
    Sleep(500)

    ChrTalk(    #162
        0x12F,
        "#264F#5POh... Is this work stuff?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1025F#6PYeah, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x12F,
        (
            "#266F#5POh... I guess I don't mind.\x02\x03",

            "You're just like Papa. It's always\x01",
            "work, work, work.\x02\x03",

            "I don't really like that very much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1013F#6PAw...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_642E")

    ChrTalk(    #166
        0x107,
        (
            "#560F#5PUm, Renne?\x02\x03",

            "I can play with you for a little\x01",
            "while if you want.\x02\x03",

            "#061FI wanna get to know you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6497")

    label("loc_642E")


    ChrTalk(    #167
        0x107,
        (
            "#560F#2PUm... Renne, right?\x02\x03",

            "Do you want to talk for a little while?\x02\x03",

            "#061FI wanna get to know you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6497")

    TurnDirection(0x12F, 0x107, 400)

    ChrTalk(    #168
        0x12F,
        (
            "#264F#5PWith you?\x02\x03",

            "#263FWell, okay, I guess we could.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6540")

    ChrTalk(    #169
        0x107,
        "#067F#5PHeehee, okay!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #170
        0x107,
        "#560F#5PWe'll be on the second floor, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6588")

    label("loc_6540")


    ChrTalk(    #171
        0x107,
        (
            "#067F#2PHeehee, okay!\x02\x03",

            "#560FWe'll be on the second floor, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6588")

    Sleep(100)

    def lambda_6593():

        label("loc_6593")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_6593")

    QueueWorkItem2(0x101, 2, lambda_6593)

    def lambda_65A4():

        label("loc_65A4")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_65A4")

    QueueWorkItem2(0xF7, 2, lambda_65A4)

    def lambda_65B5():

        label("loc_65B5")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_65B5")

    QueueWorkItem2(0xF, 2, lambda_65B5)

    def lambda_65C6():

        label("loc_65C6")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_65C6")

    QueueWorkItem2(0x8, 2, lambda_65C6)

    def lambda_65D7():

        label("loc_65D7")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_65D7")

    QueueWorkItem2(0x104, 2, lambda_65D7)

    def lambda_65E8():

        label("loc_65E8")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_65E8")

    QueueWorkItem2(0x105, 2, lambda_65E8)

    def lambda_65F9():

        label("loc_65F9")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_65F9")

    QueueWorkItem2(0x108, 2, lambda_65F9)

    def lambda_660A():
        OP_6D(-680, 2000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_660A)

    def lambda_6622():
        OP_67(0, 7350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_6622)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6652")
    OP_43(0x107, 0x1, 0x0, 0x10)
    OP_43(0x12F, 0x1, 0x0, 0x11)
    Jump("loc_668B")

    label("loc_6652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6670")
    OP_43(0x107, 0x1, 0x0, 0xE)
    OP_43(0x12F, 0x1, 0x0, 0xF)
    Jump("loc_668B")

    label("loc_6670")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_668B")
    OP_43(0x107, 0x1, 0x0, 0x10)
    OP_43(0x12F, 0x1, 0x0, 0x11)

    label("loc_668B")

    WaitChrThread(0x12F, 0x1)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0xF, 0x2)
    OP_44(0x8, 0x2)
    OP_44(0x104, 0x2)
    OP_44(0x105, 0x2)
    OP_44(0x108, 0x2)

    def lambda_66BC():
        OP_6D(-2800, 0, 1820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_66BC)

    def lambda_66D4():
        OP_67(0, 7350, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_66D4)

    def lambda_66EC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66EC)

    def lambda_66FA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_66FA)
    Sleep(50)

    def lambda_670D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_670D)

    def lambda_671B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_671B)
    Sleep(50)

    def lambda_672E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_672E)

    def lambda_673C():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_673C)
    Sleep(50)

    def lambda_674F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_674F)

    def lambda_675D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_675D)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF, 0x3)
    Sleep(200)

    ChrTalk(    #172
        0x101,
        "#1016F#6PPhew! Saved by the Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#760FHmm... Well, your report on the situation\x01",
            "can wait for now.\x02\x03",

            "Let's hear out Colonel Cid first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1006F#6PSure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6849")

    ChrTalk(    #175
        0x106,
        "#051F#6PLay it on us, Cid.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6869")

    label("loc_6849")


    ChrTalk(    #176
        0x103,
        "#020F#6PGo ahead, Colonel.\x02",
    )

    CloseMessageWindow()

    label("loc_6869")


    ChrTalk(    #177
        0xF,
        (
            "#703FThank you. I'm in a hurry myself.\x02\x03",

            "#700FSo, this is an official request from the\x01",
            "Royal Army.\x02\x03",

            "There's a series of incidents we'd like\x01",
            "you to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1004F#6PIncidents? Why does the way you\x01",
            "say that make me shiver a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xF,
        (
            "#700FYou're aware of the non-aggression\x01",
            "pact, yes?\x02\x03",

            "I'm afraid threatening letters have\x01",
            "been delivered to all parties involved\x01",
            "in the signing.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #180
        0x101,
        "#1020F#6PSomeone's threatening the treaty?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x105,
        (
            "#043FThat's... That's not good at all.\x02\x03",

            "What did the letters say, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xF,
        "#703FPlease, have a look.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #183
        (
            "\x07\x05To all parties involved in the non-aggression\x01",
            "pact: immediately back down from this act of\x01",
            "deceit and false compromise.\x02\x03",

            "Should you not, a great disaster will be visited\x01",
            "upon you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1000)

    ChrTalk(    #184
        0x101,
        "#1019F#6PWhat in the...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CA2")

    ChrTalk(    #185
        0x106,
        (
            "#053F#6PYeah, that's a threat, all right.\x02\x03",

            "#552FIs this the whole thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D05")

    label("loc_6CA2")


    ChrTalk(    #186
        0x103,
        (
            "#026F#6PWell, that isn't very open to interpretation,\x01",
            "is it?\x02\x03",

            "#022FIs this the entire letter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D05")


    ChrTalk(    #187
        0xF,
        (
            "#700FYes, that's the entire thing.\x02\x03",

            "As you may have noticed, there is no name\x01",
            "or any other indication of a sender.\x02\x03",

            "Normally, I'd simply dismiss it as a prank.\x01",
            "However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x104,
        (
            "#035F...However, something about the\x01",
            "situation makes you believe it's more\x01",
            "than a bad joke, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xF,
        (
            "#702FYes. It's the volume of letters sent,\x01",
            "you see.\x02\x03",

            "#703FThe first arrived at Leiston Fortress.\x02\x03",

            "Copies were then sent to the airship company,\x01",
            "Grancel Cathedral, Hotel Roenbaum, and the\x01",
            "Liberl News Service.\x02\x03",

            "#700FTHEN copies arrived at both the Erebonian\x01",
            "and Calvard embassies, the Erbe Royal Villa,\x01",
            "and even Grancel Castle itself.\x02\x03",

            "Nine letters in total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1020F#6PWho'd send that many letters?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x108,
        (
            "#072F#3PYeah... That'd be a lot of work for a\x01",
            "prank in poor taste.\x02\x03",

            "I can see why the army would start to\x01",
            "get concerned.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70E7")

    ChrTalk(    #192
        0x106,
        (
            "#050F#6PI don't get it, though. The airship company?\x01",
            "The Liberl News? The friggin' hotel and\x01",
            "a church?\x02\x03",

            "They don't seem to have anything to\x01",
            "do with the signing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719C")

    label("loc_70E7")


    ChrTalk(    #193
        0x103,
        (
            "#022F#6PIt's strange, though. The airship company,\x01",
            "the Liberl News, and even the hotel and\x01",
            "cathedral...\x02\x03",

            "None of these locations have anything to\x01",
            "do with the signing, do they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_719C")


    ChrTalk(    #194
        0xF,
        (
            "#700FThey are not totally unrelated, to be honest.\x02\x03",

            "#703FThe airship company shall be sending out\x01",
            "charter vessels to ferry the Imperial and\x01",
            "Republican officials here.\x02\x03",

            "They will, of course, be staying at\x01",
            "the Roenbaum.\x02\x03",

            "#700FFurthermore, the church--or, specifically,\x01",
            "Archbishop Currant of the cathedral--has\x01",
            "been asked to be an observer at the signing.\x02\x03",

            "And the Liberl News has been preparing\x01",
            "a special report on the pact and signing\x01",
            "for weeks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1015F#6PSo they ARE all connected, somehow.\x02\x03",

            "So do we have any idea who's behind it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x104,
        (
            "#032FThat could be a difficult question to\x01",
            "answer.\x02\x03",

            "This is an international matter...\x01",
            "meaning anyone from Liberl, Erebonia,\x01",
            "or Calvard could be responsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x108,
        (
            "#074F#3PYes. The war hawks in either the Empire\x01",
            "OR the Republic, for starters...\x02\x03",

            "It could even be someone from another\x01",
            "country entirely who isn't happy to see\x01",
            "all three countries working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x105,
        (
            "#042FOf course, there are plenty of suspects\x01",
            "in Liberl as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1007F#6PAnd we can't forget the obvious answer:\x01",
            "the society.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7606")

    ChrTalk(    #200
        0x106,
        (
            "#050F#6PSo what exactly do you want us to\x01",
            "investigate here, Cid?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_763E")

    label("loc_7606")


    ChrTalk(    #201
        0x103,
        (
            "#022F#6PSo what will we be investigating,\x01",
            "Colonel?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763E")


    ChrTalk(    #202
        0xF,
        (
            "#701FRight, then. The mission.\x02\x03",

            "We would like for you to investigate all the\x01",
            "locations that have received the letters,\x01",
            "and see if anyone has any further leads.\x02\x03",

            "Minus Leiston and Erbe, that is. We'll\x01",
            "handle those. The other seven locations\x01",
            "are yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x8,
        (
            "#764FSo, the airship company, Grancel Cathedral,\x01",
            "Hotel Roenbaum, the Liberl News...\x02\x03",

            "#762F...the Erebonian embassy, the Calvardian embassy,\x01",
            "and Grancel Castle... That will involve a bit of\x01",
            "walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x104,
        (
            "#030FHeh... More to the point, uniformed soldiers\x01",
            "asking around would attract a great deal of\x01",
            "unwanted attention.\x02\x03",

            "Now that you lack an Intelligence Division,\x01",
            "it makes sense to ask the guild to help\x01",
            "investigate such matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xF,
        (
            "#701FAs embarrassing as the situation is, you're\x01",
            "exactly right. Without a functional Intelligence\x01",
            "Division, we're very limited in what we can do.\x02\x03",

            "However, the new general plan from the top\x01",
            "brass is to have the guild help us with as\x01",
            "many tasks as possible.\x02\x03",

            "This is simply one case of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#1019F#6POh, really. Thanks a heap, Dad.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A98")

    ChrTalk(    #207
        0x106,
        (
            "#551F#6PYeah, that's about what I'd expect\x01",
            "from the old man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ADA")

    label("loc_7A98")


    ChrTalk(    #208
        0x103,
        (
            "#021F#6PNow, now. Take it as a sign of Cassius'\x01",
            "faith in us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ADA")


    ChrTalk(    #209
        0xF,
        (
            "#701FHaha! I must admit, it was my\x01",
            "request to ask for you, however.\x02\x03",

            "I've been placed in charge of the\x01",
            "defense of the capital region until\x01",
            "the signing ceremony.\x02\x03",

            "I would like as much information\x01",
            "as I can possibly obtain in order to\x01",
            "prepare a proper defense.\x02\x03",

            "Can I ask you to take this job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1015F#6POh, well...I DO want to help...\x02\x03",

            "But we're really kinda hip-deep\x01",
            "in another case at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        (
            "#760FThat girl, right.\x02\x03",

            "Let us hear your report on that\x01",
            "situation now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        (
            "\x07\x05Estelle explained the situation with Renne being\x01",
            "abandoned at the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #213
        0xF,
        (
            "#702FI see... Yes, an abandoned child is a\x01",
            "problem you cannot simply ignore.\x02\x03",

            "Why would anyone do such a thing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1002F#6PIt's kind of freaking me out, too.\x01",
            "I actually met her parents once, briefly.\x02\x03",

            "They seemed like this really thoughtful,\x01",
            "loving couple. They adore Renne, from\x01",
            "what I saw.\x02\x03",

            "I have to think something really, really\x01",
            "serious happened to them to make them\x01",
            "leave her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        (
            "#764FPossibly.\x02\x03",

            "They may have gotten entangled in\x01",
            "something and wanted to keep their\x01",
            "child out of it.\x02\x03",

            "#760FI do see an opportunity to kill two\x01",
            "birds with one stone, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "#760FRenne and her parents are foreigners,\x01",
            "remember?\x02\x03",

            "You'll need to inquire at the hotel and\x01",
            "the embassies regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#1006F#6PHey, I think I know where you're going\x01",
            "with this...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80DC")

    ChrTalk(    #219
        0x106,
        (
            "#051F#6PAnd it just so happens they got threatened.\x02\x03",

            "We'd want to check with the airship company,\x01",
            "too, come to think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8182")

    label("loc_80DC")


    ChrTalk(    #220
        0x103,
        (
            "#027F#6PAh, and all of those places were threatened.\x01",
            "That IS rather handy, in an unfortunate way.\x02\x03",

            "The airship company may have travel\x01",
            "records for them as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8182")


    ChrTalk(    #221
        0xF,
        (
            "#701FI'll put out a general alert to all army\x01",
            "posts to watch for her parents, as well.\x02\x03",

            "Should they pass through any of the\x01",
            "gate checkpoints, we should know. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1008F#6PThanks, Colonel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        (
            "#761FSounds like you can take the job after all.\x02\x03",

            "#760FColonel, you may leave the investigation\x01",
            "itself to us.\x02\x03",

            "I presume you'll want the final report in\x01",
            "paper and in person, however?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xF,
        (
            "#701FYes. We'd prefer to avoid telephones to\x01",
            "avoid any risk of interception.\x02\x03",

            "You'll be able to find me at the Erbe\x01",
            "Royal Villa beginning today, actually.\x02\x03",

            "I'm sorry for the extra trouble, but could\x01",
            "I ask that you bring the final report there\x01",
            "in person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#1006F#6PSure!\x02\x03",

            "We'll see you at the villa once\x01",
            "we know what's up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xF,
        "#701FI wish you luck, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85C9")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05After seeing Colonel Cid out, Estelle's team decided to\x01",
            "split up to investigate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #228
        (
            "\x07\x05Estelle, Zin, Olivier, and Kloe were to head to the\x01",
            "embassies, Grancel Castle, and the Liberl News...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #229
        (
            "\x07\x05...while Agate would investigate the cathedral, hotel, and\x01",
            "airship company on his own.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_870B")

    label("loc_85C9")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")
    SetChrName("")

    AnonymousTalk(    #230
        (
            "\x07\x05After seeing Colonel Cid out, Estelle's team decided to\x01",
            "split up to investigate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #231
        (
            "\x07\x05Estelle, Zin, Olivier, and Kloe were to head to the\x01",
            "embassies, Grancel Castle, and the Liberl News...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #232
        (
            "\x07\x05...while Scherazard would investigate the cathedral, hotel,\x01",
            "and airship company on her own.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_870B")

    ClearChrFlags(0x12F, 0x80)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, -570, 0, 970, 90)
    SetChrPos(0xF7, -940, 0, -70, 90)
    SetChrPos(0x104, -2280, 0, 810, 90)
    SetChrPos(0x108, -2280, 0, 1980, 90)
    SetChrPos(0x105, -1080, 0, 2040, 90)
    SetChrPos(0x107, 1570, 0, 170, 270)
    SetChrPos(0x12F, 1710, 0, 1240, 270)
    OP_9F(0x12F, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6D(-160, 0, 1660, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #233
        0x101,
        (
            "#1006F#6POkay, we'll be heading out.\x02\x03",

            "Tita, Renne, sorry to leave you two behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x12F,
        (
            "#265F#2POh, it's okay!\x02\x03",

            "#261FWe're going out shopping!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        "#1004F#6PEr, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x107,
        (
            "#560F#2PS-Sorry, Estelle.\x02\x03",

            "Renne really wants to visit the\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x12F,
        (
            "#264F#2PWhy, that's not how I remember\x01",
            "things, Tita.\x02\x03",

            "#263FAs I recall, you were the one who\x01",
            "said she wanted to look at all the\x01",
            "stuffed animals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x107,
        "#067FAwww, Renne...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1025F#6PHaha... Well, um...\x02\x03",

            "I know you're bored, Renne, but since I'm not\x01",
            "sure when we'll find out something about your\x01",
            "parents, I'd like for you to wait here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x12F,
        "#267F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x107,
        "#063F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#1019F#6POh, c'mon, that's so not fair.\x01",
            "DOUBLE doe-eye stares?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B25")

    ChrTalk(    #243
        0x106,
        (
            "#051F#6PAh, it'll be cool.\x02\x03",

            "Tita's with her, so they should be fine\x01",
            "if they're just out shopping and stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB8")

    label("loc_8B25")


    ChrTalk(    #244
        0x103,
        (
            "#021F#6PI don't really see a problem, Estelle.\x02\x03",

            "If Tita's with her, it should be safe\x01",
            "enough to let them go out shopping\x01",
            "and around the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BB8")


    ChrTalk(    #245
        0x101,
        (
            "#1007F#6P...I guess so.\x02\x03",

            "#1006FOkay, Tita, Renne?\x02\x03",

            "We'll be back by this evening, so you\x01",
            "need to be back by then, too, okay?\x02\x03",

            "And the capital's a really big place,\x01",
            "so don't get lost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x107,
        "#061F#2PWe will, and we won't! ♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)

    ChrTalk(    #247
        0x107,
        "#560FRenne, let's go!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x107, 400)

    ChrTalk(    #248
        0x12F,
        "#265F#2PAfter you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #249
        0x12F,
        "#261F#2PSee you, everyone. ♪\x02",
    )

    CloseMessageWindow()

    def lambda_8D0C():
        OP_6D(-230, 0, -3670, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8D0C)
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)

    def lambda_8D30():

        label("loc_8D30")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_8D30")

    QueueWorkItem2(0x101, 1, lambda_8D30)

    def lambda_8D41():

        label("loc_8D41")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_8D41")

    QueueWorkItem2(0x8, 1, lambda_8D41)

    def lambda_8D52():

        label("loc_8D52")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_8D52")

    QueueWorkItem2(0xF7, 1, lambda_8D52)

    def lambda_8D63():

        label("loc_8D63")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_8D63")

    QueueWorkItem2(0x108, 1, lambda_8D63)

    def lambda_8D74():

        label("loc_8D74")

        TurnDirection(0xFE, 0x12F, 0)
        OP_48()
        Jump("loc_8D74")

    QueueWorkItem2(0x104, 1, lambda_8D74)

    def lambda_8D85():

        label("loc_8D85")

        TurnDirection(0xFE, 0x12F, 0)
        OP_48()
        Jump("loc_8D85")

    QueueWorkItem2(0x105, 1, lambda_8D85)
    Sleep(200)
    OP_43(0x12F, 0x1, 0x0, 0x13)
    WaitChrThread(0x12F, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x108, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x8, 0x1)
    Sleep(500)
    OP_6D(-2590, 0, 1610, 2000)

    ChrTalk(    #250
        0x105,
        "#048F#4PHaha, they sure became fast friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        (
            "#1016F#5PYeah, it's really easy to become friends\x01",
            "at that age. Man, youth. I feel all old now!\x02\x03",

            "#1015FAlthooough...Tita and Renne together...\x02\x03",

            "Why does that combination send a chill\x01",
            "of doom down my spine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #252
        0x105,
        "#044F#4POh? I think they'll be fine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #253
        0x101,
        (
            "#1025F#5PTita's kind of easy to push around,\x01",
            "though.\x02\x03",

            "I get the feeling Renne might try to\x01",
            "drag her into all kinds of stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x105,
        "#045F#4PThat...might be a good point...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9020")

    ChrTalk(    #255
        0x106,
        (
            "#050F#2POh, yeah, Elnan.\x02\x03",

            "Did you get the names of that kid's\x01",
            "parents?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_906D")

    label("loc_9020")


    ChrTalk(    #256
        0x103,
        (
            "#020F#2PAh, yes, Elnan.\x02\x03",

            "Did you find out the names of Renne's\x01",
            "parents?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_906D")


    def lambda_9073():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9073)
    Sleep(50)

    def lambda_9086():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9086)
    Sleep(50)

    def lambda_9099():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9099)
    Sleep(50)

    def lambda_90AC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_90AC)
    Sleep(50)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #257
        0x8,
        (
            "#764FIt took a little insistent asking, but she\x01",
            "eventually gave them.\x02\x03",

            "#762FHer father is a trader from Crossbell.\x02\x03",

            "Harold and Sophia Hayworth are their\x01",
            "names.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1015FTrader from Crossbell...\x01",
            "Harold and Sophia Hayworth...\x02\x03",

            "#1006FOkay, got it written down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9225")

    ChrTalk(    #259
        0x106,
        (
            "#051FI got it, too.\x02\x03",

            "All right. Let's get this\x01",
            "investigation started.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9275")

    label("loc_9225")


    ChrTalk(    #260
        0x103,
        (
            "#021FAs do I.\x02\x03",

            "So! Let's start asking around\x01",
            "about them and these letters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9275")


    ChrTalk(    #261
        0x8,
        (
            "#760FSo, remember: Estelle's group will\x01",
            "visit the embassies, Grancel Castle,\x01",
            "and the Liberl News.\x02\x03",

            "Zin, Olivier, we will be counting on\x01",
            "your aid at the embassies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x104,
        (
            "#035F#6PFear not. My brilliant smile can open\x01",
            "any door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x108,
        (
            "#070FWe'll make sure you see the\x01",
            "ambassadors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        (
            "#760FYour Highness, your help would be\x01",
            "invaluable at Grancel Castle.\x02\x03",

            "Please introduce Estelle to whoever\x01",
            "can best help our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x105,
        "#040FOf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x8,
        (
            "#761FAs for the Liberl News, I believe you\x01",
            "yourself have an 'in' for that, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#1006FYeah! I can bug Nial about it.\x01",
            "He kinda owes me at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9583")

    ChrTalk(    #268
        0x8,
        (
            "#760FAnd that leaves the cathedral, the airship\x01",
            "company, and the Roenbaum.\x02\x03",

            "Agate, good luck with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x106,
        "#051F#2PNo prob. Shouldn't take too long.\x02",
    )

    CloseMessageWindow()
    Jump("loc_963C")

    label("loc_9583")


    ChrTalk(    #270
        0x8,
        (
            "#760FAnd that leaves the cathedral, the airship\x01",
            "company, and the Roenbaum.\x02\x03",

            "Scherazard, good luck with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x103,
        (
            "#020F#2PI shouldn't have too much trouble.\x01",
            "I'll try to be quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_963C")


    ChrTalk(    #272
        0x101,
        "#1018FSo, let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_8_5BC2 end

    def Function_9_966D(): pass

    label("Function_9_966D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -320, -500, -7250, 0)

    def lambda_9694():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9694)
    OP_8E(0xFE, 0xFFFFFCEA, 0xFFFFFF06, 0xFFFFED54, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_9_966D end

    def Function_10_96BC(): pass

    label("Function_10_96BC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_96E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_96E3)
    OP_8E(0xFE, 0x140, 0xFFFFFE0C, 0xFFFFE458, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_10_96BC end

    def Function_11_970B(): pass

    label("Function_11_970B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 560, -500, -7230, 0)

    def lambda_9732():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9732)
    OP_8E(0xFE, 0x1B8, 0xFFFFFF06, 0xFFFFEC96, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_11_970B end

    def Function_12_975A(): pass

    label("Function_12_975A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -320, -500, -7250, 0)

    def lambda_9781():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9781)
    OP_8E(0xFE, 0xFFFFFE34, 0xFFFFFF06, 0xFFFFE7DC, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_12_975A end

    def Function_13_97A9(): pass

    label("Function_13_97A9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 560, -500, -7230, 0)

    def lambda_97D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_97D0)
    OP_8E(0xFE, 0x2D0, 0xFFFFFF06, 0xFFFFE7DC, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_13_97A9 end

    def Function_14_97F8(): pass

    label("Function_14_97F8")

    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFF6C8, 0x0, 0xFFFFF646, 0x9C4, 0x0)
    OP_8E(0xFE, 0x3DE, 0x0, 0xFFFFF61E, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD7A, 0x0, 0xFFFFFEE8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE10, 0x0, 0x12B6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_97F8 end

    def Function_15_9874(): pass

    label("Function_15_9874")


    def lambda_987A():

        label("loc_987A")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_987A")

    QueueWorkItem2(0x12F, 2, lambda_987A)
    Sleep(2300)
    OP_44(0x12F, 0x2)
    OP_8E(0xFE, 0x3DE, 0x0, 0xFFFFF61E, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD7A, 0x0, 0xFFFFFEE8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE10, 0x0, 0x12B6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_9874 end

    def Function_16_98EF(): pass

    label("Function_16_98EF")

    OP_8C(0xFE, 90, 500)
    OP_8E(0xFE, 0x5BE, 0x0, 0xFFFFFFE2, 0x9C4, 0x0)
    OP_8E(0xFE, 0xDFC, 0x0, 0x708, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE2E, 0x0, 0x1338, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_98EF end

    def Function_17_9957(): pass

    label("Function_17_9957")


    def lambda_995D():

        label("loc_995D")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_995D")

    QueueWorkItem2(0x12F, 2, lambda_995D)
    Sleep(800)
    OP_44(0x12F, 0x2)
    OP_8E(0xFE, 0xDFC, 0x0, 0x708, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE10, 0x0, 0x12B6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_9957 end

    def Function_18_99BE(): pass

    label("Function_18_99BE")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x276, 0xFFFFFF06, 0xFFFFE6CE, 0x7D0, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_99E9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_99E9)
    OP_8E(0xFE, 0x1E0, 0xFFFFFE0C, 0xFFFFE3AE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_99BE end

    def Function_19_9A0F(): pass

    label("Function_19_9A0F")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x276, 0xFFFFFF06, 0xFFFFE6CE, 0x7D0, 0x0)

    def lambda_9A30():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A30)
    OP_8E(0xFE, 0x1E0, 0xFFFFFE0C, 0xFFFFE3AE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_19_9A0F end

    def Function_20_9A60(): pass

    label("Function_20_9A60")

    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0x668, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_9A60 end

    def Function_21_9A7C(): pass

    label("Function_21_9A7C")

    OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x230, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_21_9A7C end

    def Function_22_9A98(): pass

    label("Function_22_9A98")

    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0x668, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_22_9A98 end

    def Function_23_9AB4(): pass

    label("Function_23_9AB4")

    OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x230, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_23_9AB4 end

    def Function_24_9AD0(): pass

    label("Function_24_9AD0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AF3")
    Call(0, 38)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)

    label("loc_9AF3")

    ClearMapFlags(0x1)
    OP_6D(-40, -250, -5780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9B69")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1780, 0, 1670, 270)
    Jump("loc_9B7F")

    label("loc_9B69")

    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1780, 0, 1670, 270)

    label("loc_9B7F")

    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x19)
    Sleep(400)
    OP_43(0x105, 0x0, 0x0, 0x1A)
    Sleep(400)
    OP_43(0x108, 0x0, 0x0, 0x1C)
    Sleep(400)
    OP_43(0x104, 0x0, 0x0, 0x1B)
    OP_0D()
    WaitChrThread(0x104, 0x0)

    ChrTalk(    #273
        0x101,
        "#1011F#6PWe're baaack!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9BF9")

    def lambda_9BEE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9BEE)
    Jump("loc_9C07")

    label("loc_9BF9")


    def lambda_9BFF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9BFF)

    label("loc_9C07")


    def lambda_9C0D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9C0D)

    def lambda_9C1B():
        OP_6D(-2910, 0, 830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9C1B)

    def lambda_9C33():
        OP_67(0, 6310, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C33)

    def lambda_9C4B():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9C4B)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9C8E")

    ChrTalk(    #274
        0xA,
        "#051F#4PYo. There you are.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CA9")

    label("loc_9C8E")


    ChrTalk(    #275
        0x9,
        "#021F#4PWelcome back!\x02",
    )

    CloseMessageWindow()

    label("loc_9CA9")


    def lambda_9CAF():
        OP_8E(0xFE, 0xFFFFF880, 0x0, 0x3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9CAF)
    Sleep(200)

    def lambda_9CCF():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9CCF)
    Sleep(500)

    def lambda_9CEF():
        OP_8E(0xFE, 0xFFFFF5F6, 0x0, 0xFFFFFC36, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9CEF)
    Sleep(500)

    def lambda_9D0F():
        OP_8E(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D0F)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #276
        0x101,
        "#1016FSorry! I know we're a bit late.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #277
        0x101,
        "#1011FHey, where're Tita and Renne?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x8,
        (
            "#761F#6PThey returned just before you did.\x02\x03",

            "I believe they're enjoying the spoils of\x01",
            "a hard-fought shopping campaign on\x01",
            "the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #279
        0x101,
        (
            "#1016FSounds like they had fun.\x02\x03",

            "#1006FAnyway, we've got a lot to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x8,
        "#760F#6PYes, please.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x101, 0, 400)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A099")

    ChrTalk(    #281
        0xA,
        (
            "#051F#4PI see. Not bad.\x02\x03",

            "Sounds like you guys learned a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        (
            "#1007FI guess. We didn't get anything decisive,\x01",
            "though.\x02\x03",

            "#1015FAgate, did you find anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xA,
        (
            "#053F#4PHonestly? I got jack all.\x02\x03",

            "The hotel, the cathedral, the airship\x01",
            "company...\x02\x03",

            "Nobody had a single friggin' clue\x01",
            "of who coulda sent the letters.\x02\x03",

            "#050FThe head guy at the airship company\x01",
            "was sweatin' quartz that a demand for\x01",
            "money might come in next...\x02\x03",

            "But at this point? Not so much as\x01",
            "another peep.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A292")

    label("loc_A099")


    ChrTalk(    #284
        0x9,
        (
            "#027F#4PI see.\x02\x03",

            "Sounds like you had a fairly\x01",
            "productive day, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#1007FI guess. We didn't get anything decisive,\x01",
            "though.\x02\x03",

            "#1015FSchera, did you find anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x9,
        (
            "#025F#4PI managed to find a very large pile of\x01",
            "nothing.\x02\x03",

            "The hotel, the cathedral, the airship\x01",
            "company...\x02\x03",

            "No one had the slightest clue as to\x01",
            "who would send such letters.\x02\x03",

            "#022FThe leader of the airship company\x01",
            "is deathly afraid the sender might\x01",
            "demand money next...\x02\x03",

            "There haven't been any followup letters,\x01",
            "though, to anyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A292")


    ChrTalk(    #287
        0x101,
        (
            "#1007FDamn.\x02\x03",

            "#1002FDoesn't really narrow things\x01",
            "down much...\x02\x03",

            "How likely do you think it is the\x01",
            "society's behind all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#764F#6PI don't think we can safely say that\x01",
            "at this point.\x02\x03",

            "#762FTheir primary focus up till now has\x01",
            "been experimenting with those bizarre\x01",
            "'Gospel' orbments they possess.\x02\x03",

            "And we know the Gospels can create\x01",
            "phenomena otherwise unimaginable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x104,
        (
            "#032F#5PThose devices certainly haven't shown\x01",
            "an ability to create threatening letters\x01",
            "from nowhere, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x108,
        (
            "#072F#3PYeah, this doesn't really seem like it\x01",
            "matches the society's M.O.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015FHuh... I guess Ruan and Zeiss just\x01",
            "have me on edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x8,
        (
            "#764F#6PNo, it's perfectly understandable.\x02\x03",

            "#760FRegardless, I think we can safely say\x01",
            "we've done our part.\x02\x03",

            "I'll compile all your testimonies into a\x01",
            "report.\x02\x03",

            "Could I ask you to deliver it to Colonel\x01",
            "Cid at the Erbe Royal Villa tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_ACE2")

    ChrTalk(    #293
        0x101,
        (
            "#1025FSure.\x02\x03",

            "We didn't find the sender in the end,\x01",
            "so I feel kinda bad, but I guess it's all\x01",
            "we can do.\x02\x03",

            "#1004FOh! Erbe! Right! Agate, did you find\x01",
            "anything out about Renne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xA,
        (
            "#050F#4PI did, actually. Or actually, I... Wait,\x01",
            "lemme start over.\x02\x03",

            "I went to the hotel first. The kid and\x01",
            "her folks stayed there for about two\x01",
            "weeks.\x02\x03",

            "Same room the entire stay, typical\x01",
            "tourist stuff.\x02\x03",

            "They just checked out this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        "#1002FOkay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xA,
        (
            "#555F#4PThen I went to the cathedral.\x02\x03",

            "While they were here, the Hayworths\x01",
            "came to worship a bunch of times.\x02\x03",

            "Thing is, the priest who attended 'em\x01",
            "said they felt...'off' when they did.\x02\x03",

            "Like they were distracted during prayer\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x105,
        "#043F#5PThat would match what Miss Hilda said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x101,
        "#1015FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "#053F#4PAnd then, at the airship company...\x02\x03",

            "#552FThat's where I found zip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        "#1004FWait. What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xA,
        (
            "#555F#4PHarold, Sophia, and Renne Hayworth of\x01",
            "Crossbell, right?\x02\x03",

            "There have been exactly zero passengers\x01",
            "by that name and nationality coming\x01",
            "through here for at LEAST half a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        "#1020FNo way! But--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x104,
        (
            "#032F#5PThat IS a mystery...\x02\x03",

            "Though perhaps they traveled by land?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #304
        "\x18\x07\x05Did Renne come to Liberl by land?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "She must have.\x01",        # 0
            "Wait a minute...\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AB2A"),
        (1, "loc_AC10"),
        (SWITCH_DEFAULT, "loc_ACDF"),
    )


    label("loc_AB2A")


    ChrTalk(    #305
        0x101,
        (
            "#1015FShe must have.\x02\x03",

            "I mean, I guess we can go\x01",
            "ask Renne herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "#552F#4PNo.\x02\x03",

            "Remember when we met her at\x01",
            "Air-Letten?\x02\x03",

            "She was goin' on about seeing a\x01",
            "big lake when her airship landed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        "#1002FHey, that's right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACDF")

    label("loc_AC10")

    OP_2B(0x89, 0x2)

    ChrTalk(    #308
        0x101,
        (
            "#1020FWait a minute... That can't be right.\x02\x03",

            "When we first met her, she was talking\x01",
            "about landing in an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xA,
        (
            "#552F#4PRight, at Air-Letten.\x02\x03",

            "She said she saw a big lake on\x01",
            "the way down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACDF")

    label("loc_ACDF")

    Jump("loc_B46E")

    label("loc_ACE2")


    ChrTalk(    #310
        0x101,
        (
            "#1025FSure...\x02\x03",

            "We didn't find the sender in the end,\x01",
            "so I feel kinda bad, but I guess it's all\x01",
            "we can do.\x02\x03",

            "#1004FOh! Erbe! Right! Schera, did you find\x01",
            "anything out about Renne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x9,
        (
            "#020F#4PI did have some results on that end,\x01",
            "though not in the way I expected.\x02\x03",

            "Let me start with the hotel. The\x01",
            "Hayworths, all three of them, definitely\x01",
            "stayed there for about two weeks.\x02\x03",

            "They kept the same room for the entire\x01",
            "time, in a fairly typical tourist fashion.\x02\x03",

            "It was only just this morning that they\x01",
            "checked out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        "#1002FOkay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        (
            "#022F#4PI then visited the cathedral.\x02\x03",

            "It seems the Hayworths came to worship\x01",
            "a number of times while they were here.\x02\x03",

            "However, the father who ministered to\x01",
            "them said he felt there was something...\x01",
            "'off' about their behavior.\x02\x03",

            "That they seemed distracted during\x01",
            "prayer, specifically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x105,
        "#043F#5PThat would match what Miss Hilda said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#1015FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x9,
        (
            "#522F#4PAnd finally, the airship company...\x02\x03",

            "That's where things get VERY strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        "#1004FStrange? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x9,
        (
            "#026F#4PTheir names are Harold, Sophia, and\x01",
            "Renne Hayworth from Crossbell, yes?\x02\x03",

            "#022FThere are no records of anyone matching\x01",
            "those names, nor that nationality. And the\x01",
            "records go back six months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        "#1020FNo way! But--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x104,
        (
            "#032F#5PThat IS a mystery.\x02\x03",

            "Though perhaps they traveled by land?\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #321
        "\x18\x07\x05Did Renne come to Liberl by land?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "She must have.\x01",        # 0
            "Wait a minute...\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B2B0"),
        (1, "loc_B3A5"),
        (SWITCH_DEFAULT, "loc_B46E"),
    )


    label("loc_B2B0")


    ChrTalk(    #322
        0x101,
        (
            "#1015FShe must have.\x02\x03",

            "I mean, I guess we can go\x01",
            "ask Renne herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x9,
        (
            "#522F#4PEr, Estelle?\x02\x03",

            "Remember what Renne said when\x01",
            "we met her at Air-Letten?\x02\x03",

            "She talked about seeing a lake when\x01",
            "the AIRSHIP landed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x101,
        "#1002FHey, that's right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B46E")

    label("loc_B3A5")

    OP_2B(0x89, 0x2)

    ChrTalk(    #325
        0x101,
        (
            "#1020FWait a minute... That can't be right.\x02\x03",

            "When we first met her, she was talking\x01",
            "about landing in an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x9,
        (
            "#022F#4PYes, at Air-Letten.\x02\x03",

            "She said she saw a lake on the\x01",
            "way down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B46E")

    label("loc_B46E")


    ChrTalk(    #327
        0x8,
        (
            "#764F#6PHm. Troubling.\x02\x03",

            "#762FIt's possible they were traveling\x01",
            "under assumed names.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #328
        0x101,
        "#1020FAssumed names? Why would they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x108,
        (
            "#072F#3PThey may have had something to hide,\x01",
            "or they may have been hiding FROM\x01",
            "someone.\x02\x03",

            "Either way, they must've known something\x01",
            "was wrong before they set out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        "#1003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x8,
        (
            "#764F#6PI've contacted every guild branch in\x01",
            "the country about Renne's parents.\x02\x03",

            "For the moment, all we can do is\x01",
            "wait for more information to come in.\x02\x03",

            "#760FAs for Renne herself...\x02\x03",

            "I think it would be best if she stayed\x01",
            "in the care of the guild for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        (
            "#1007FYeah. I'd feel terrible if she got wrapped\x01",
            "up in something.\x02\x03",

            "#1006FCould you leave her with me, maybe?\x02\x03",

            "This mission kinda feels personal now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x8,
        (
            "#761F#6PI was going to suggest that, actually.\x01",
            "Thank you.\x02\x03",

            "The guild will pay for everyone's lodgings\x01",
            "while you're in Grancel, naturally.\x02\x03",

            "That includes Renne, so don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        (
            "#1016FThanks, Elnan.\x02\x03",

            "#1004FOh! Wait, speaking of staying the night...\x01",
            "We might not actually need that tonight!\x01",
            "You see...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BB1C")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #335
        "\x07\x05Estelle told Agate about the invitation to stay at the castle.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #336
        0x8,
        "#763F#6PMy, that's quite an invitation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xA,
        (
            "#053F#4PYeah, and I think I'll pass.\x02\x03",

            "#050FThe castle's a bit too rich for\x01",
            "my blood. I'm not really keen\x01",
            "on staying there.\x02\x03",

            "'Sides, it'll be easier for Elnan\x01",
            "to reach one of us at the hotel\x01",
            "if something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1015FOh, I hadn't thought of that.\x02\x03",

            "We might hear something about\x01",
            "Renne's parents... I guess I should\x01",
            "stay at the hotel too, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #339
        0x101,
        "#1025F#6PSorry, Kloe.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #340
        0x105,
        (
            "#048FHaha. No, don't worry.\x02\x03",

            "I'll explain the situation to Hilda.\x01",
            "I'm sure she won't mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD97")

    label("loc_BB1C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #341
        "\x07\x05Estelle told Schera about the invitation to stay at the castle.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #342
        0x8,
        "#763F#6PMy, that's quite an invitation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x9,
        (
            "#025F#4PIt is. Honestly, I'd absolutely love to\x01",
            "stay there again, but...\x02\x03",

            "#020FI'm afraid I'll need to decline this time.\x02\x03",

            "It will be far easier for the guild to\x01",
            "reach at least one of us at the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x101,
        (
            "#1015FOh, I hadn't thought of that.\x02\x03",

            "We might hear something about\x01",
            "Renne's parents... I guess I should\x01",
            "stay at the hotel too, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #345
        0x101,
        "#1025F#6PSorry, Kloe.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #346
        0x105,
        (
            "#048FHaha. No, don't worry.\x02\x03",

            "I'll explain the situation to Hilda.\x01",
            "I'm sure she won't mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD97")


    ChrTalk(    #347
        0x104,
        (
            "#030F#5PZin and I are to stay at our respective\x01",
            "embassies.\x02\x03",

            "The princess shall retire to her castle,\x01",
            "naturally.\x02\x03",

            "So that means you two and the girls\x01",
            "will be staying at the hotel, then?\x02\x03",

            "#031FHmm. Parting on these terms would\x01",
            "be dreadfully dull.\x02\x03",

            "Since we're all together this evening,\x01",
            "shall we enjoy a nice dinner at the bar?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    def lambda_BEEF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEEF)

    def lambda_BEFD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_BEFD)
    Sleep(500)

    ChrTalk(    #348
        0x101,
        (
            "#1006F#4PGood idea!\x02\x03",

            "And, you know, I'd actually like\x01",
            "to hear you play the piano again,\x01",
            "Olivier. It's been a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #349
        0x104,
        (
            "#035F#5PAh, sweet maiden, you know just\x01",
            "how to pluck my heartstrings.\x02\x03",

            "#037FHave you come to appreciate a\x01",
            "mature flavor at last, I wonder? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1019F#4PI'm going to SNAP those heartstrings\x01",
            "if you keep it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x108,
        (
            "#070F#6PSnapping or no, we should get going.\x02\x03",

            "With a group this large, it could be\x01",
            "hard to find seating.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C13A")

    ChrTalk(    #352
        0xA,
        (
            "#051FAll right, let's gather up the kids and\x01",
            "get on over to the bar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C170")

    label("loc_C13A")


    ChrTalk(    #353
        0x9,
        "#021FAll right, let's call the girls and be off.\x02",
    )

    CloseMessageWindow()

    label("loc_C170")

    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #354
        (
            "\x07\x05That evening, Estelle's group and Renne had dinner at the\x01",
            "Sunnybell Inn.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #355
        (
            "\x07\x05Olivier, as if it were second nature, took to the piano after a\x01",
            "few drinks...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #356
        "\x07\x05Ultimately, even Mueller and Nial were called to come and join.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #357
        "\x07\x05And so passed a pleasant evening in Grancel.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x4, 0xFF)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C2D1")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_C2D5")

    label("loc_C2D1")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_C2D5")

    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4153   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_9AD0 end

    def Function_25_C2E2(): pass

    label("Function_25_C2E2")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -150, -500, -7230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C309():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C309)
    OP_8E(0xFE, 0xFFFFFEDE, 0xFFFFFF06, 0xFFFFEC82, 0x7D0, 0x0)
    Return()

    # Function_25_C2E2 end

    def Function_26_C32A(): pass

    label("Function_26_C32A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 590, -500, -7250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C351():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C351)
    OP_8E(0xFE, 0x38E, 0xFFFFFF06, 0xFFFFE8F4, 0x7D0, 0x0)
    Return()

    # Function_26_C32A end

    def Function_27_C372(): pass

    label("Function_27_C372")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 190, -500, -7250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C399():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C399)
    OP_8E(0xFE, 0xFFFFFFCE, 0xFFFFFF06, 0xFFFFE796, 0x7D0, 0x0)
    Return()

    # Function_27_C372 end

    def Function_28_C3BA(): pass

    label("Function_28_C3BA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, -500, -7250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C3E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C3E1)
    OP_8E(0xFE, 0xFFFFFC22, 0xFFFFFF06, 0xFFFFE886, 0x7D0, 0x0)
    Return()

    # Function_28_C3BA end

    def Function_29_C402(): pass

    label("Function_29_C402")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C427")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_C427")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C451")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C443")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_C447")

    label("loc_C443")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_C447")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_C451")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C47B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C46D")
    AddParty(0x6, 0xFA, 0xFF)
    Jump("loc_C471")

    label("loc_C46D")

    AddParty(0x6, 0xFB, 0xFF)

    label("loc_C471")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_C47B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C496")
    AddParty(0x7, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_C496")

    Return()

    # Function_29_C402 end

    def Function_30_C497(): pass

    label("Function_30_C497")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4BC")
    Call(0, 38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C4B8")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_C4BC")

    label("loc_C4B8")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_C4BC")

    OP_4A(0xC, 255)
    OP_4A(0x8, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x101, 90, -500, -7250, 0)
    SetChrPos(0xF7, 90, -500, -7250, 0)
    SetChrPos(0x107, 90, -500, -7250, 0)
    SetChrPos(0x12F, 90, -500, -7250, 0)
    SetChrPos(0xC, -2130, 0, -50, 270)
    SetChrPos(0xE, -2170, 0, 1060, 270)
    OP_6D(-4300, 0, 1620, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #358
        0x101,
        "#2PWe're baaack!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    OP_8C(0x8, 135, 400)
    OP_8C(0xE, 180, 400)

    def lambda_C5AC():

        label("loc_C5AC")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_C5AC")

    QueueWorkItem2(0x8, 1, lambda_C5AC)

    ChrTalk(    #359
        0xE,
        "#070F#2PHey, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        "#041F#5PWelcome back!\x02",
    )

    CloseMessageWindow()

    def lambda_C5F8():
        OP_6D(-3840, 0, 950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5F8)

    def lambda_C610():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C610)
    OP_43(0x101, 0x0, 0x0, 0x1F)
    Sleep(600)
    OP_8C(0xE, 90, 400)

    def lambda_C63B():
        OP_8E(0xFE, 0xFFFFF93E, 0x0, 0x5FA, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_C63B)
    Sleep(200)
    OP_8C(0xC, 90, 400)

    def lambda_C662():
        OP_8E(0xFE, 0xFFFFFAF6, 0x0, 0x230, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_C662)
    WaitChrThread(0xE, 0x0)

    def lambda_C682():

        label("loc_C682")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_C682")

    QueueWorkItem2(0xE, 1, lambda_C682)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(400)
    WaitChrThread(0xC, 0x0)

    def lambda_C6A4():

        label("loc_C6A4")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_C6A4")

    QueueWorkItem2(0xC, 1, lambda_C6A4)
    OP_43(0x107, 0x1, 0x0, 0x21)
    Sleep(600)
    OP_43(0x12F, 0x1, 0x0, 0x22)
    WaitChrThread(0x12F, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_44(0xE, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x8, 0x1)
    OP_8C(0xC, 270, 400)
    OP_8C(0xE, 270, 400)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #361
        0x8,
        "#760F#6PYou delivered the report, I take it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x101,
        "#1000FYep! No problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x8,
        (
            "#760F#6PWe just received the mission fee from\x01",
            "the army a moment ago.\x02\x03",

            "Here, let me give you the reward.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8B, 0x4, 0x10)
    OP_AF(0xCD, 0x8B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #364
        0x101,
        (
            "#1001F#2PHaha! Yay for Colonel Cid! He does\x01",
            "some fast work.\x02\x03",

            "#1015FAnyway, more importantly... I'd heard\x01",
            "some of the old Intelligence guys were\x01",
            "seen near Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x8,
        (
            "#762F#6PAh, so the villa was contacted as well.\x01",
            "I thought that might be the case.\x02\x03",

            "We were just talking about that, as it\x01",
            "so happens.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CDF7")

    ChrTalk(    #366
        0x106,
        (
            "#050F#5PSounded like some guild members\x01",
            "found them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x8,
        "#764F#6PYes... It was Scherazard and Anelace.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #368
        0x101,
        "#1004F#2PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x8,
        (
            "#762F#6PThey discovered a base the Intelligence\x01",
            "Division fugitives had been using in the\x01",
            "abandoned mine near Ravennue.\x02\x03",

            "Unfortunately, the base itself had already\x01",
            "been abandoned as well by the time they\x01",
            "found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        "#1002F#2PThat's where we fought those bandits!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x106,
        (
            "#555F#5PTch... Why didn't we think to look there?\x02\x03",

            "You said their base was abandoned.\x01",
            "Any idea where they went after that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x8,
        (
            "#765F#6PActually, former Intelligence special\x01",
            "forces men have been seen all over\x01",
            "the Bose region.\x02\x03",

            "The border garrison is currently\x01",
            "investigating the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x101,
        (
            "#1015F#2POh, man...\x02\x03",

            "Should we pack it up and head over\x01",
            "to Bose to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x8,
        (
            "#762F#6PNo. There's a chance this is simply\x01",
            "a distraction.\x02\x03",

            "Until we get a request for help from the\x01",
            "Bose branch directly, I would prefer not\x01",
            "to act rashly.\x02\x03",

            "There's another reason for caution, as\x01",
            "well. It seems the society has a hand\x01",
            "in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x101,
        "#1020F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x106,
        "#054F#5PAw, hell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x8,
        (
            "#764F#6PScherazard and Anelace encountered one\x01",
            "of their agents in the abandoned mine.\x02\x03",

            "#762FAnother 'Enforcer,' Campanella the Fool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x106,
        "#555F#5PSon of... Another one, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D2D4")

    label("loc_CDF7")


    ChrTalk(    #379
        0x103,
        (
            "#020F#5PYes, it sounded like some fellow\x01",
            "guild members found them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x8,
        "#764F#6PYes... It was Agate and Anelace.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #381
        0x101,
        "#1004F#2PWha?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x8,
        (
            "#762F#6PThey discovered a base the Intelligence\x01",
            "Division fugitives had been using in the\x01",
            "abandoned mine near Ravennue.\x02\x03",

            "Unfortunately, the base itself had already\x01",
            "been abandoned as well by the time they\x01",
            "found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x101,
        "#1002F#2PThat's where we fought those bandits!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x103,
        (
            "#026F#5PI see...\x01",
            "I wouldn't have thought to look there.\x02\x03",

            "#022FYou said they'd abandoned it already.\x01",
            "Do we have any idea where they went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x8,
        (
            "#765F#6PActually, former Intelligence special\x01",
            "forces men have been seen all over\x01",
            "the Bose region.\x02\x03",

            "The border garrison is currently\x01",
            "investigating the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        (
            "#1015F#2POh, man...\x02\x03",

            "Should we pack it up and head over to\x01",
            "Bose to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x8,
        (
            "#762F#6PNo, until we get a request for help from\x01",
            "the Bose branch directly, I would prefer\x01",
            "not to act rashly.\x02\x03",

            "There's another reason for caution, as\x01",
            "well. It seems the society has a hand\x01",
            "in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        "#1020F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x103,
        "#024F#5PYou're kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#764F#6PAgate and Anelace encountered one of\x01",
            "their agents in the abandoned mine.\x02\x03",

            "#762FAnother 'Enforcer,' Campanella the Fool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x103,
        "#022F#5PHmmm. Another new face...\x02",
    )

    CloseMessageWindow()

    label("loc_D2D4")


    ChrTalk(    #392
        0x8,
        (
            "#762F#6PThey also found several strange things\x01",
            "in the ruins of the base.\x02\x03",

            "Firstly, they discovered plans for something\x01",
            "called an 'Orgueille,' which seems to be\x01",
            "some form of orbal-driven vehicle...\x02\x03",

            "They also found a memo, written in cipher,\x01",
            "discussing a 'tea party' of some sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        (
            "#1015F#2POrgueille? Tea party...?\x02\x03",

            "#1007FWell, that explains everything and leaves\x01",
            "us with no questions. No, siree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x107,
        (
            "#065F#5PWhat do you mean by 'orbal driven vehicle'?\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xC,
        (
            "#049FI'm more concerned about what a 'tea party'\x01",
            "could refer to...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_43(0x12F, 0x1, 0x0, 0x23)
    Sleep(2000)
    OP_63(0x101)
    OP_63(0x107)
    OP_63(0xC)
    OP_63(0xE)
    OP_63(0x8)
    OP_63(0xF7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D5D0")

    ChrTalk(    #396
        0x106,
        (
            "#552F#5PTch... Hard to sit on our butts after\x01",
            "hearin' all that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D626")

    label("loc_D5D0")


    ChrTalk(    #397
        0x103,
        (
            "#025F#5PGoodness. It's hard to simply stay\x01",
            "here and wait after hearing all that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D626")

    OP_8C(0xE, 180, 400)

    ChrTalk(    #398
        0xE,
        (
            "#070F#4PC'mon, cool your heads, guys.\x02\x03",

            "The army and our guildmates are\x01",
            "working hard over there.\x02\x03",

            "I'm sure they'll keep things under control.\x01",
            "We'll hear about it soon enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x8,
        (
            "#760F#6PExactly. I know it may make you nervous,\x01",
            "but please remain in Grancel for the time\x01",
            "being.\x02\x03",

            "For now, you may do as you please.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)

    ChrTalk(    #400
        0x101,
        "#1007F#2PAll right... I'm sure Olivier will appreci--\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 45, 400)
    Sleep(500)
    OP_8C(0x101, 135, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #401
        0x101,
        "#1004F#2PHey, wait. Where'd Olivier go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x8,
        (
            "#760F#6PAh, yes. The Erebonian embassy called\x01",
            "a little while ago.\x02\x03",

            "It was Olivier. He said that he had a small\x01",
            "piece of business to attend to and left.\x02\x03",

            "He did say he would return quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x101,
        "#1015F#2PHuh. I wonder what that's about.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D923():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D923)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #404
        0x101,
        "#1004F#2PWait, speaking of missing...\x02",
    )

    CloseMessageWindow()

    def lambda_D961():
        OP_6D(-2510, 0, -500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D961)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #405
        0x101,
        "#1026F#4PWhere... Where did Renne go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x107,
        "#064F#6PWhaaat?\x02",
    )

    CloseMessageWindow()

    def lambda_D9BE():
        OP_8C(0xC, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_D9BE)

    def lambda_D9CC():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_D9CC)
    Sleep(100)

    def lambda_D9DF():
        OP_8C(0x8, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_D9DF)

    def lambda_D9ED():
        OP_8C(0xE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_D9ED)
    Sleep(100)
    OP_43(0x107, 0x1, 0x0, 0x24)
    OP_8C(0x107, 180, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 180, 300)
    OP_44(0x107, 0x1)

    ChrTalk(    #407
        0x107,
        (
            "#065F#6PHuh? ...Oh!\x02\x03",

            "She was here just a minute ago!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DA64():
        OP_6D(-3840, 0, 950, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DA64)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #408
        0x101,
        (
            "#1015F#2PCrap...\x02\x03",

            "Do you think she got bored with all\x01",
            "the talking and went out to play?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)

    def lambda_DAE5():
        OP_8C(0x8, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DAE5)

    def lambda_DAF3():
        OP_8C(0xC, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DAF3)

    def lambda_DB01():
        OP_8C(0x107, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_DB01)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DB63")

    ChrTalk(    #409
        0x106,
        (
            "#051F#5PTalk WAS gettin' kind of heavy.\x01",
            "I know I'd book it if I was a kid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB9F")

    label("loc_DB63")


    ChrTalk(    #410
        0x103,
        (
            "#524F#5PIt's quite possible. We WERE going\x01",
            "on a bit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB9F")


    ChrTalk(    #411
        0x101,
        (
            "#1007F#2PWell, this isn't good.\x02\x03",

            "#1015FDarn it... We do need to do\x01",
            "something about her if we're\x01",
            "going to leave Grancel.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(500)

    ChrTalk(    #412
        0x101,
        "#1006F#2P...I'm gonna go look for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x107,
        (
            "#560F#5PI'll come, too!\x02\x03",

            "I think I might know\x01",
            "where Renne went!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #414
        0x101,
        "#1006F#2PThanks, Tita.\x02",
    )

    CloseMessageWindow()

    def lambda_DCC2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCC2)
    Sleep(50)

    def lambda_DCD5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_DCD5)
    OP_8C(0x107, 315, 400)
    OP_8C(0xE, 270, 400)

    ChrTalk(    #415
        0x101,
        "#1015F#2PSorry, Elnan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x8,
        (
            "#760F#6PNot at all.\x02\x03",

            "While you're out, I'll get the other branches\x01",
            "up to speed and see if I can learn anything\x01",
            "new.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    RemoveParty(0x2E, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-5650, 0, -18030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #417
        (
            "\x07\x05Please form your party. You may choose one additional\x01",
            "member aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DE64")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_DE75")

    label("loc_DE64")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_DE75")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_30_C497 end

    def Function_31_DE8B(): pass

    label("Function_31_DE8B")

    OP_8E(0xFE, 0xFFFFF600, 0x0, 0x1F4, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_31_DE8B end

    def Function_32_DEA7(): pass

    label("Function_32_DEA7")

    OP_8E(0xFE, 0xFFFFF952, 0x0, 0xFFFFFCFE, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_32_DEA7 end

    def Function_33_DEC3(): pass

    label("Function_33_DEC3")

    OP_8E(0xFE, 0xFFFFF646, 0x0, 0xFFFFF9B6, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_33_DEC3 end

    def Function_34_DEDF(): pass

    label("Function_34_DEDF")

    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xFFFFF70E, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_34_DEDF end

    def Function_35_DEFB(): pass

    label("Function_35_DEFB")

    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFFFB0, 0xFFFFFE0C, 0xFFFFE3B8, 0x7D0, 0x0)
    SetChrFlags(0x12F, 0x80)
    Return()

    # Function_35_DEFB end

    def Function_36_DF21(): pass

    label("Function_36_DF21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF44")
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_36_DF21")

    label("loc_DF44")

    Return()

    # Function_36_DF21 end

    def Function_37_DF45(): pass

    label("Function_37_DF45")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF65")
    Call(0, 38)
    Call(0, 40)
    FadeToBright(0, 0)

    label("loc_DF65")

    Fade(1000)
    SetChrPos(0x101, 26120, 0, 58670, 270)
    SetChrPos(0x107, 26210, 0, 57560, 270)
    SetChrPos(0xF7, 27510, 0, 57390, 270)
    SetChrPos(0xF9, 27360, 0, 58520, 270)
    OP_8C(0x19, 180, 0)
    OP_6D(25020, 0, 58400, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #418
        0x101,
        "#1018F#6PHmm... 'Colorless fish'... Hey!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E071")

    ChrTalk(    #419
        0x106,
        "#051F#2PAhhh, I get it. Fish prints.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E096")

    label("loc_E071")


    ChrTalk(    #420
        0x103,
        "#021F#2POf course. Fish prints.\x02",
    )

    CloseMessageWindow()

    label("loc_E096")

    OP_4A(0x19, 255)
    OP_6D(26740, 0, 61110, 1200)

    ChrTalk(    #421
        0x19,
        (
            "Oh? Interested in my fish print,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x19,
        (
            "That's proof of my hard-earned glory,\x01",
            "that is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x19,
        (
            "Settle on down, and I'll tell you the\x01",
            "tale of my valor!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1B7")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_E1F5")

    label("loc_E1B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1DE")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_E1F5")

    label("loc_E1DE")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_E1F5")

    Sleep(1000)

    def lambda_E200():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E200)
    Sleep(100)

    def lambda_E213():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_E213)
    Sleep(100)

    def lambda_E226():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E226)
    Sleep(100)

    def lambda_E239():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_E239)
    Sleep(500)

    ChrTalk(    #424
        0x101,
        (
            "#1016F#1PEr, we'll have to take a rain check\x01",
            "on that, I'm afraid...\x02\x03",

            "#1006FSir, did a girl in a white dress\x01",
            "come by here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x19,
        (
            "Ah, she's your friend? Cute girl,\x01",
            "that one, if a bit of an oddball.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x19,
        (
            "She asked me a very strange\x01",
            "question and then left, just like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x101,
        "#1007F#1PI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x107,
        "#065F#1PWhat was the question, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x19,
        "Hmm... If I remember rightly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x19,
        (
            "'Do you know where the bitter,\x01",
            "spicy, delicious store is?'\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E43A")

    ChrTalk(    #431
        0x108,
        "#070F#1PSounds like a riddle to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E467")

    label("loc_E43A")


    ChrTalk(    #432
        0x105,
        "#045F#1PIt's definitely another riddle.\x02",
    )

    CloseMessageWindow()

    label("loc_E467")


    ChrTalk(    #433
        0x101,
        "#1006F#5PBitter, spicy, delicious, got it.\x02",
    )

    CloseMessageWindow()

    def lambda_E49D():
        OP_6D(26150, 0, 59560, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E49D)
    OP_8C(0x101, 135, 400)
    OP_8C(0xF7, 315, 400)
    OP_8C(0xF9, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #434
        0x101,
        "#1006F#6PAll right! Time to hit the stores!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1632)
    OP_28(0x8C, 0x1, 0x40)
    OP_4B(0x19, 255)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    EventEnd(0x0)
    Return()

    # Function_37_DF45 end

    def Function_38_E516(): pass

    label("Function_38_E516")

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
        (0, "loc_E58F"),
        (1, "loc_E595"),
        (SWITCH_DEFAULT, "loc_E59B"),
    )


    label("loc_E58F")

    OP_A2(0x1200)
    Jump("loc_E59B")

    label("loc_E595")

    OP_A2(0x1201)
    Jump("loc_E59B")

    label("loc_E59B")

    Return()

    # Function_38_E516 end

    def Function_39_E59C(): pass

    label("Function_39_E59C")

    ClearMapFlags(0x1)
    OP_6D(-5650, 0, -18030, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E5DF")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_E5FD")

    label("loc_E5DF")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_E5FD")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_39_E59C end

    def Function_40_E61D(): pass

    label("Function_40_E61D")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E65C")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_E676")

    label("loc_E65C")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_E676")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_40_E61D end

    def Function_41_E696(): pass

    label("Function_41_E696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E6A7")
    OP_2A(0xBD, 0xBE, 0xFFFF)
    Jump("loc_E6F4")

    label("loc_E6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_E6BE")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xA9, 0xFFFF)
    Jump("loc_E6F4")

    label("loc_E6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_E6D3")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xFFFF)
    Jump("loc_E6F4")

    label("loc_E6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E6E6")
    OP_2A(0xAA, 0xAC, 0xC4, 0xFFFF)
    Jump("loc_E6F4")

    label("loc_E6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E6F4")
    OP_2A(0xAA, 0xAC, 0xFFFF)

    label("loc_E6F4")

    TalkEnd(0xFF)
    Return()

    # Function_41_E696 end

    SaveToFile()

Try(main)
